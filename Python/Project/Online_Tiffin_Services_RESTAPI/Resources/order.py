from flask_restful import  Resource
import json
from flask import *
from Common.utils import *
import pymysql.cursors
from Database.connection import con as con
from Database.queries import *

import logging

logger = logging.getLogger(__name__)

file_handler = logging.FileHandler("log/logfile.log")
formatter =logging.Formatter('%(asctime)s:%(name)s:%(message)s')
file_handler.setFormatter(formatter)

logger.addHandler(file_handler)
logger.setLevel(logging.DEBUG)

class Order(Resource):
    def post(self):
        pass

    def get(self):
        if 'username' in session:
            data = json.loads(request.args.get('order'))
            username = str(session['username'])
            connection = con()
            try:
                insert('user_order',connection,username, data['Cake'][1],data['Chocolate'][1])
                logger.debug("Order taken successfully from user " + username)
                return request.args.get('order')

            except Exception as e:
                print(str(e))
                logger.error("there is an error while making order from user " + username)
                return output_html(render_template('error.html'), 200)