import requests
import json
from flask import *
from flask_restful import *

class Send_Message(Resource):
    def post(self):
        web_hook_url = 'https://hooks.slack.com/services/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'
        print(request.form['msg'])
        slack_msg = {'text': request.form['msg']}

        requests.post(web_hook_url, data=json.dumps(slack_msg))
