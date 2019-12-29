import os
import datetime
from flask import *

def output_html(data,code,headers=None):
    resp = Response(data,mimetype='text/html',headers=headers)
    resp.status_code=code
    return resp