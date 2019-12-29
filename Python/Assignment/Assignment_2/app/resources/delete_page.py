from flask_restful import Resource
from ..common.utils import output_html
from flask import render_template
from ..database.connection import con
from ..database.querie import select

class Delete_page(Resource):
    def get(self):
        connection = con()
        data = select(connection,"1","1")
        return output_html(render_template("delete.html", data=data), 200)

    def post(self):
        pass