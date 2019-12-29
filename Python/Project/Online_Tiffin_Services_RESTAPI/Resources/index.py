from flask_restful import Resource
from Common.utils import *
from flask import *

class Index(Resource):
    # @marshal_with(resource_fields)
    def get(self):
        return output_html(render_template("index.html"),200)

    def post(self):
        return output_html(render_template("index.html"),200)