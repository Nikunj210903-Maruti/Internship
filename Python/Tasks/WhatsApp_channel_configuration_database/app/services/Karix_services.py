from ..database.karix_configuration_queries import *
from ..common.schema import BotData




class Karix_interface():

    def get_data_from_whatsapp_channel_configuration(self , bot_id):
        from app.manage import get_logger
        logger = get_logger()
        result = select_whatsapp_channel_configuration('SELECT_WHATSAPP_CHANNEL_CONFIGURATION', bot_id)
        logger.info("Data fetched from Whatsapp_channel_confoguration table")
        return result

    def put_data_into_whatsapp_channel_configuration_on_duplicate_update(self,*data):
        from app.manage import get_logger
        logger = get_logger()
        insert_whatsapp_channel_configuration_on_duplicate_update('INSERT_WHATSAPP_CHANNEL_CONFIGURATION_ON_DUPLICATE_UPDATE', *data)
        logger.info("Data inserted from Whatsapp_channel_confoguration table")

    def insert_data_into_channel_configuration(self,*data):
        from app.manage import get_logger
        logger = get_logger()
        insert_channel_configuration('INSERT_CHANNEL_CONFIGURATION', *data)
        logger.info("Data inserted from channel_confoguration table")

    def create_webhook_url(self):
        import uuid
        from app import app
        from flask import current_app
        with app.app_context():
            host_url = current_app.config["KARIX_HOST_URL"]
            constant = str(current_app.config["KARIX_CONSTANT"])
            webhook_url = str(uuid.uuid1())
            webhook_url = host_url + "/" + constant + "/" + webhook_url
        return webhook_url

    def validate_user(self,username, password):
        from flask import current_app
        from requests.auth import HTTPBasicAuth
        from app import app
        import requests
        if not username or not password:
            raise Exception("Please provide username and password")
        with app.app_context():
            karix_authentication_url = current_app.config['KARIX_AUTHANTICATION_URL'] + str(username)
            res = requests.get(karix_authentication_url, auth=HTTPBasicAuth(username, password))
            if res.status_code == 200:
                return True
            else:
                return False

    def validate_data(self,data):
        result = BotData().load(data)





