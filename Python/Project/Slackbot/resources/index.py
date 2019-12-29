from flask_restful import *
from flask import *
from common.utils import *

class Index(Resource):
    def get(self):
        return output_html(render_template('msg.html'),200)
    def post(self):
        return output_html(render_template('msg.html'), 200)

