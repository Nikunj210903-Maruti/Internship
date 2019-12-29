from flask import *
import os

path = os.path.dirname(os.path.abspath(__file__))
UPLOAD_FOLDER = os.path.join(path, 'static/images')
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}


def output_html(data,code,headers=None):
    resp=Response(data,mimetype='text/html',headers=headers)
    resp.status_code=code
    return resp

def allowed_file(filename):
    print(filename)
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS