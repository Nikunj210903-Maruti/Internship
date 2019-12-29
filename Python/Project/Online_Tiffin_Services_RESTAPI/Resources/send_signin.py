from flask_restful import Resource
from Common.utils import *
from flask import *

class Send_signin(Resource):
    # @marshal_with(resource_fields)
    def get(self):
        return output_html(render_template("signin.html"),200)

    def post(self):
        return output_html(render_template("signin.html"),200)