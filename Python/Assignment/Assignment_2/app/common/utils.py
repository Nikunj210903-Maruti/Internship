import os

path = os.path.dirname(os.path.abspath(__file__))
UPLOAD_FOLDER = os.path.join(path, 'static/images')
ALLOWED_EXTENSIONS = {'png'}

def read_id():
    file=open("app/common/data.txt","r")
    return file.read()

def write_id(id):
    file = open("app/common/data.txt", "w")
    file.write(str(id))

def output_html(data,code,headers=None):
    from flask import Response
    resp=Response(data,mimetype='text/html',headers=headers)
    resp.status_code=code
    return resp

def allowed_file(filename):
    print(filename)
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def toCst(time):
    import datetime
    import pytz
    try:
        d1 = datetime.datetime.strptime(time, "%Y-%m-%dT%H:%M")
        local_tz = pytz.timezone('Asia/Kolkata')
        date_temp = local_tz.localize(d1, is_dst=None)
        now_cst = date_temp.astimezone(pytz.timezone('CST6CDT'))
        return now_cst
    except:
        raise Exception("Enter date in format '2019-12-29 15:56'")

def validation(file,form):
    filename = file["photo"]
    if allowed_file(filename.filename):
        return True
    return False

def check_expire_time(given_timezone, ex_time):
    import datetime
    import pytz
    tz_NY = pytz.timezone(given_timezone)
    datetime_NY = datetime.datetime.now(tz_NY)
    now_cst = datetime_NY.astimezone(pytz.timezone('CST6CDT'))

    local_tz = pytz.timezone('CST6CDT')
    ex_time = local_tz.localize(ex_time, is_dst=None)
    if now_cst > ex_time:
        return True
    else:
        return False

def toLocal(time,tz):
    import pytz
    local_tz = pytz.timezone('CST6CDT')
    time = local_tz.localize(time, is_dst=None)
    now_cst = time.astimezone(pytz.timezone(tz))
    return now_cst

def get_logger():
    import logging
    logger = logging.getLogger(__name__)
    file_handler = logging.FileHandler("app/log/logfile.log")
    formatter = logging.Formatter('%(asctime)s:%(name)s:%(message)s')
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)
    logger.setLevel(logging.DEBUG)
    return logger

