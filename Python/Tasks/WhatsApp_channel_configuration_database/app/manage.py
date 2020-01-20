from flask import Flask, current_app, request
from .config import configure_app
from .apis.karix_configuration import Karix_Configuration


def create_app():
    """Initialize Flask Application"""
    app = Flask(__name__)
    configure_app(app)
    return app

def app_init_task(api):
    api.add_resource(Karix_Configuration, '/v1/karix-channel-configuration/<bot_id>/<channel_id>')

def get_logger():
    import logging
    logger = logging.getLogger(__name__)
    file_handler = logging.FileHandler("data/log/logfile.txt")
    formatter = logging.Formatter('%(asctime)s:%(name)s:%(message)s')
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)
    logger.setLevel(logging.DEBUG)
    return logger