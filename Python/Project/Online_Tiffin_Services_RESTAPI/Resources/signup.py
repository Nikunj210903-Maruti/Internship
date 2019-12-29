from flask_restful import Resource
import os
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

class Signup(Resource):
    # @marshal_with(resource_fields)
    def get(self):
        pass

    def post(self):
        try:
            connection = con()
            username = request.form['username']
            email = request.form['email']
            password = request.form['password']
            photo = request.files['photo']


            if photo and allowed_file(photo.filename):
                filename = username + '.' + photo.filename.rsplit('.', 1)[1].lower()
                path = os.path.dirname(os.path.abspath(__file__))
                photo.save(os.path.join(os.path.join(path, '../static/images'), filename))
                image_path = os.path.join(UPLOAD_FOLDER, filename)
                insert('user', connection, username, email, password, image_path)
                logger.debug("User "+username+" signed up.")
                return redirect('/send_signin')
            else:
                error = "Please select your photo in jpeg,jpg or png format"
                return output_html(render_template('signup.html', error=error),200)
        except Exception as e:
            print(str(e))
            return output_html(render_template('error.html'), 200)
