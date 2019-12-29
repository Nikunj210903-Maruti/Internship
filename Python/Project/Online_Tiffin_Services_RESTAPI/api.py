from flask import *
from flask_restful import Api

from Resources.index import Index
from Resources.signup import Signup
from Resources.signin import Signin
from Resources.send_signin import Send_signin
from Resources.send_signup import Send_signup
from Resources.signout import Signout
from Resources.order import Order
import logging


logger = logging.getLogger(__name__)

file_handler = logging.FileHandler("log/logfile.log")
formatter =logging.Formatter('%(asctime)s:%(name)s:%(message)s')
file_handler.setFormatter(formatter)

logger.addHandler(file_handler)
logger.setLevel(logging.DEBUG)

app = Flask(__name__, template_folder="template")
api = Api(app,catch_all_404s=True)

app.config["ENV"]="development"

if app.config["ENV"]== "production":
    app.config.from_object("config.Production_config")
    logger.debug("App is in Production mode")
elif app.config["ENV"]== "development":
    app.config.from_object("config.Development_config")
    logger.debug("App is in Development mode")
else:
    app.config.from_object("config.Testing_config")
    logger.debug("App is in Testing mode")

@app.errorhandler(404)
def not_found(e):
    return render_template("error.html")

api.add_resource(Index, '/')
api.add_resource(Send_signin, '/send_signin')
api.add_resource(Send_signup, '/send_signup')
api.add_resource(Signup, '/signup')
api.add_resource(Signin, '/signin')
api.add_resource(Signout, '/signout')
api.add_resource(Order, '/order')

if __name__ == '__main__':
    app.run(debug=True)
