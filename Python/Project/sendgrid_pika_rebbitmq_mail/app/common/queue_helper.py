from threading import Thread

import pika
import requests
from flask import current_app, json
from pika.exceptions import AMQPError



from app.common.constant import QueueEnum


def connect():
    from app import app
    with app.app_context():
        parameters = pika.URLParameters(current_app.config['RABBIT_MQ_URL_PARAMETER'])
        connection = pika.BlockingConnection(parameters)
        return connection

def close(connection):
    if connection is not None:
        connection.close()


class RabbitMqConnection(object):
    def __init__(self):
        self.conn = None

    def __enter__(self):
        self.conn = connect()
        return self.conn

    def __exit__(self, exc_type, exc_val, exc_tb):
        close(self.conn)


def create_queues():
    from app import app
    with app.app_context():
        exchange = current_app.config['RMQ_EXCHANGE']
        with RabbitMqConnection() as conn:
            for data in QueueEnum:
                channel = conn.channel()
                channel.exchange_declare(exchange=exchange, exchange_type='direct')
                channel.queue_declare(queue=data.value['queue'], durable=True)
                channel.queue_bind(exchange=exchange, routing_key=data.value['route'], queue=data.value['queue'])


def publish_message(route_key, payload, exchange_type='direct', delivery_mode=2):
    from app import app
    with app.app_context():
        app.logger.info("Payload %r " % json.dumps(payload))
        with RabbitMqConnection() as conn:
            channel = conn.channel()
            channel.exchange_declare(exchange=current_app.config['RMQ_EXCHANGE'], exchange_type=exchange_type)
            channel.basic_publish(exchange=current_app.config['RMQ_EXCHANGE'],
                                  routing_key=route_key,
                                  body=json.dumps(payload),
                                  properties=pika.BasicProperties(
                                      delivery_mode=delivery_mode,
                                  ))


class ConsumerSendEmail(Thread):
    def __init__(self,queue_name):
        self.queue_name = queue_name
        self._connection = None
        self._channel = None
        Thread.__init__(self)
        Thread.daemon = True
        self.start()

    def callback(self, ch, method, properties, body):
        from app.services.sendmail import consumerlogic
        payload = json.loads(body.decode())
        try:
            status_code = consumerlogic(payload)
            print(status_code)
            if 1:
                raise
            print("Success : ", payload)
            ch.basic_ack(delivery_tag=method.delivery_tag)
        except Exception as e:
            ch.basic_ack(delivery_tag=method.delivery_tag)
            publish_message(QueueEnum.UNSEND_EMAIL.value['route'], payload=payload)


    def run(self):
        self._connection = connect()
        self._channel = self._connection.channel()
        self._channel.basic_qos(prefetch_count=10)
        self._channel.basic_consume(self.callback, queue=self.queue_name, no_ack=False)
        self._channel.start_consuming()




class ConsumerUnsendEmail(Thread):
    def __init__(self, queue_name):
        self.queue_name = queue_name
        self._connection = None
        self._channel = None
        Thread.__init__(self)
        Thread.daemon = True
        self.start()

    def callback(self, ch, method, properties, body):
        try:
            print("unsend")
            ch.basic_ack(delivery_tag=method.delivery_tag)
        except Exception as e:
            print(e)


    def run(self):
        self._connection = connect()
        self._channel = self._connection.channel()
        self._channel.basic_qos(prefetch_count=10)
        #self._channel.basic_consume(self.callback, queue=self.queue_name, no_ack=False)
        #self._channel.start_consuming()



def start_consumer():
    from app import app
    with app.app_context():
        for data in QueueEnum:
            for worker in range(data.value['worker_count']):
                 consumer_map[data.name](queue_name=data.value['queue'])




def queue_init():
    create_queues()
    start_consumer()


def consumer_health_checkup():
    from app import app
    with app.app_context():
        url = current_app.config['RABBIT_MQ_HOST_URL']
        endpoint = '{0}/api/queues/'.format(url)
        response = requests.get(endpoint, auth=(current_app.config['RABBIT_MQ_USERNAME'],
                                                current_app.config['RABBIT_MQ_PASSWORD']))
        # RabbitMQ API to get queue details and it's consumers
        results = (json.loads(str(response.content, 'utf8')))
        if isinstance(results, list):
            # Iterate over queues response
            for result in results:
                # Iterate over QueueEnum
                for data in QueueEnum:
                    # It compare result's queue name with enum queue name
                    if result['name'] == data.value['queue'] and int(result['consumers']) < data.value['worker_count']:
                        # It finds dead consumers of the queue and starts the dead consumers
                        dead_workers = data.value['worker_count'] - int(result['consumers'])
                        for worker in range(dead_workers):
                            consumer_map[data.name](queue_name=data.value['queue'])
                        break


consumer_map = {
    QueueEnum.SEND_EMAIL.name: ConsumerSendEmail,
    QueueEnum.UNSEND_EMAIL.name: ConsumerUnsendEmail,
   }
