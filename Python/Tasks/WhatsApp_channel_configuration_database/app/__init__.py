from .manage import create_app, app_init_task
from flask_restful import Api

app = create_app()
api = Api(app)
app_init_task(api)

def run_server():
    """Eventlet Server"""
    app.run(port=app.config.get('PORT'),debug=True)
