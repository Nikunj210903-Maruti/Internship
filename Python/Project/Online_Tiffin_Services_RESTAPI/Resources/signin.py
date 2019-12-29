from flask_restful import Resource
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

class Signin(Resource):
    # @marshal_with(resource_fields)
    def get(self):
        pass

    def post(self):
        try:
            connection = con()
            result = select('user',connection,request.form["username"], request.form['password'])
            if result:
                session['username'] = request.form["username"]
                username = session['username']
                menu = select('items',connection)
                data = {'username': request.form['username'], 'menu': menu}
                logger.debug("User " + username + " signed in")
                return output_html(render_template('dashboard.html', data=data),200)

            else:
                error = "Enter valid Username or Password"
                return output_html(render_template('signin.html', error=error),200)
        except Exception as e:
            print(e)
            return output_html(render_template('error.html'), 200)