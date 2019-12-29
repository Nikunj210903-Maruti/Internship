from flask_restful import Resource
from ..common.utils import output_html
from flask import render_template
import pytz

class Search__page(Resource):
    def get(self):
        return output_html(render_template("search.html",timezones=pytz.all_timezones),200)

    def post(self):
        pass