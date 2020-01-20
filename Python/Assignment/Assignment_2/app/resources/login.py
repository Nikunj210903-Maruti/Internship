from flask_restful import Resource
from ..common.utils import output_html
from flask import render_template,request,redirect , url_for , session


class Login(Resource):
    def get(self):
        pass

    def post(self):
        username = request.form['username']
        password = request.form['password']
        if username=="admin" and password=="admin":
            session['username'] = username
            return redirect(url_for('swagger_ui.show'))
        else:
            return redirect(url_for("login_page"))