from flask_restful import Resource
from flask import *
from Common.utils import *

import logging

logger = logging.getLogger(__name__)

file_handler = logging.FileHandler("log/logfile.log")
formatter =logging.Formatter('%(asctime)s:%(name)s:%(message)s')
file_handler.setFormatter(formatter)

logger.addHandler(file_handler)
logger.setLevel(logging.DEBUG)

class Signout(Resource):
    # @marshal_with(resource_fields)
    def get(self):
        if 'username' in session:
            username=session['username']
            session.pop('username', None)
            logger.debug("User " + username + " signed out")
            return redirect(url_for('index'))
        else:
            return output_html(render_template('error.html'), 200)

    def post(self):
        pass