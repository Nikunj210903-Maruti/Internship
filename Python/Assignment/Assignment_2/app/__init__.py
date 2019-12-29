from .manage import create_app , init_task
from .common.utils import get_logger
from flask import render_template
from flask_restful import Api
from flask_swagger_ui import get_swaggerui_blueprint



def run_server():
    """Eventlet Server"""
    app.run(port=app.config.get('PORT'))

__all__ = ["app", "api", "cache_store", "socket", "jwt", "run_server"]

app = create_app()
api = Api(app)

init_task(api)




SWAGGER_URL = '/swagger'
API_URL = '/static/swagger/swagger.json'
SWAGGERUI_BLUEPRINT = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config={
        'app_name': "Seans-Python-Flask-REST-Boilerplate"
    }
)
app.register_blueprint(SWAGGERUI_BLUEPRINT, url_prefix=SWAGGER_URL)



@app.errorhandler(404)
def not_found(e):
    return render_template("error.html" , error ="Page Not Found")



