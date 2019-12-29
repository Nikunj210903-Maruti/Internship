from flask_restful import Resource
from ..common.utils import output_html
from flask import render_template

class Insert_page(Resource):
    def get(self):
        return output_html(render_template("insert.html"),200)

    def post(self):
        pass