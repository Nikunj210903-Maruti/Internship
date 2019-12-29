import csv
from app.common.queue_helper import publish_message
from app.common.constant import QueueEnum
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail
from flask import current_app

def publish(filename):
    '''for i in range(80):
        payload = {
                "name": 'Nikunj',
                "email": 'Email'
        }
        publish_message(QueueEnum.SEND_EMAIL.value['route'], payload=payload)'''

    with open(filename, 'r') as csvfile:
        csvreader = csv.DictReader(csvfile)
        for row in csvreader:
            payload = {
            "name": row['First Name'],
            "email": row['Email']
         }
            publish_message(QueueEnum.SEND_EMAIL.value['route'], payload=payload)



def consumerlogic(payload):
    from app import app
    with app.app_context():
        message = Mail(from_email=current_app.config['FROM_EMAIL'], to_emails=payload["email"])
        message.template_id = current_app.config['TEMPLATE_ID']
        message.dynamic_template_data = {'first_name': payload["name"], "meta": {"year": 2019},
                                         "link": {"unsubscribe": ""}}

        sendgrid_client = SendGridAPIClient(current_app.config['API_KEY'])
        response = sendgrid_client.send(message)
        return response.status_code

