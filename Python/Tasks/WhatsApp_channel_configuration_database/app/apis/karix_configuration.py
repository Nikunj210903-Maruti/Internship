from flask_restful import Resource , marshal
from ..common.model import model
import json
from flask import request
from ..services.get_channel_data import get_channel_provider_from_channel_id

class Karix_Configuration(Resource):
    def get(self, bot_id,channel_id):
        try:
            provider = get_channel_provider_from_channel_id(channel_id)
            result = provider.get_data_from_whatsapp_channel_configuration(bot_id)
            if not result:
                result={}
                webhook_url = provider.create_webhook_url()
                result['webhook_url'] = webhook_url
                print(result)
            return marshal(result,model), 200
        except Exception as e:
            print(e)
            return {"message": str(e)}, 404

    def post(self, bot_id,channel_id):
        try:
            provider = get_channel_provider_from_channel_id(channel_id)
            data = request.get_json()
            provider.validate_data(data)
            bot_phone_number = data['bot_phone_number']
            webhook_url = data['webhook_url']
            auth_details = data['auth_details']
            validated = provider.validate_user(auth_details['uid'],auth_details['utoken'])
            if not validated:
                raise Exception("Account Information is Incorrect")
            provider.put_data_into_whatsapp_channel_configuration_on_duplicate_update("1", bot_id,bot_phone_number,webhook_url, json.dumps(auth_details),"2019-12-30T12:45","1","2019-12-30T12:45","1")
            try:
                provider.insert_data_into_channel_configuration(bot_id,"1","1","2019-12-30T12:45","1","2019-12-30T12:45","1")
            except:
                pass

            return {"message" : "Saved your details successfully"}, 200

        except Exception as e:
            return {"message" : str(e)} , 401


