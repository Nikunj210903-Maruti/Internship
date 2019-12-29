import pymysql.cursors
import os
from datetime import timedelta
from flask import *
from werkzeug.exceptions import *
from werkzeug.utils import secure_filename

app = Flask(__name__, template_folder="template")
app.secret_key = 'any random string'

path = os.path.dirname(os.path.abspath(__file__))
UPLOAD_FOLDER = os.path.join(path, 'static/images')
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 16MByte size


def allowed_file(filename):
    print(filename)
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.before_request
def make_session_permanent():
    session.permanent = True
    app.permanent_session_lifetime = timedelta(minutes=1)


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/send_signin', methods=['GET', 'POST'])
def send_signin():
    if request.method == 'POST' or request.method=='GET':
        return render_template('signin.html', error=None)


@app.route('/send_signup', methods=['GET', 'POST'])
def send_signup():
    if request.method == 'POST':
        return render_template('signup.html', error=None)


@app.route('/signin', methods=['GET', 'POST'])
def signin():
    try:
        error = None
        if request.method == 'POST':
            connection = pymysql.connect(host='localhost',
                                         user='root',
                                         password='Nikunj210903',
                                         db='Online_Tiffin_Services',
                                         charset='utf8mb4',
                                         cursorclass=pymysql.cursors.DictCursor)
            with connection.cursor() as cursor:
                sql = "SELECT `Username`, `Password` FROM `user` WHERE `Username`=%s and `Password`=%s"
                cursor.execute(sql, (request.form["username"], request.form['password']))
                result = cursor.fetchone()

                if result:
                    with connection.cursor() as cursor:
                        sql = "SELECT * FROM `items`"
                        cursor.execute(sql, ())
                        result = cursor.fetchall()
                        connection.close()
                    menu = result
                    data = {'username': request.form['username'], 'menu': menu}
                    return render_template('dashboard.html', data=data)
                else:
                    error = "Enter valid Username or Password"
                    return render_template('signin.html', error=error)
    except Exception as e:
        # error="Chooose another user name"
        return render_template('signin.html', error=str(e))


@app.route('/signup', methods=['POST', 'GET'])
def signup(filename=None):
    try:
        error = None
        if request.method == 'POST':
            connection = pymysql.connect(host='localhost',
                                         user='root',
                                         password='Nikunj210903',
                                         db='Online_Tiffin_Services',
                                         charset='utf8mb4',
                                         cursorclass=pymysql.cursors.DictCursor)
            username = request.form['username']
            email = request.form['email']
            password = request.form['password']
            photo = request.files['photo']

            if photo and allowed_file(photo.filename):
                filename = username + '.' + photo.filename.rsplit('.', 1)[1].lower()
                photo.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
                image_path = os.path.join(UPLOAD_FOLDER, filename)
                with connection.cursor() as cursor:
                    sql = "INSERT INTO `user` (Username,Email,Password,Photo) VALUES (%s, %s, %s,%s)"
                    cursor.execute(sql, (username, email, password, image_path))
                connection.commit()
                connection.close()
            else:
                error = "Please select your photo in jpeg,jpg or png format"
                return render_template('signup.html', error=error)

            return redirect('/send_signin')
    except Exception as e:
        print(e)
        return render_template('signup.html', error=str(e))


@app.route('/signout')
def logout():
    session.pop('username', None)
    return redirect(url_for('index'))


'''@app.route('/error')
def error():
    return render_template("error.html")'''

if __name__ == '__main__':
    app.run(debug=True)

