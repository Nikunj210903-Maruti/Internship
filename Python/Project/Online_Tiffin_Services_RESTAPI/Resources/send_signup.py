from flask_restful import  Resource
from Common.utils import *
from flask import *

class Send_signup(Resource):
    # @marshal_with(resource_fields)
    def get(self):
        return output_html(render_template("signup.html"),200)

    def post(self):
        return output_html(render_template("signup.html"),200)