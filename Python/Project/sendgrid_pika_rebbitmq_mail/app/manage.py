import datetime
import logging
from logging.handlers import TimedRotatingFileHandler

from flask import Flask, current_app, request
from .config import configure_app

__all__ = ['create_app', 'app_init_task', 'ws_init']


def create_app():
    """Initialize Flask Application"""
    app = Flask(__name__)
    configure_app(app)
    # Config App Logger
    return app


def app_init_task():
    from app import app
    with app.app_context():
        # Start RabbitMQ Consumer
        from app.common.queue_helper import queue_init
        queue_init()


def configure_hook(app):
    def is_ignore_log():
        return not request.path.endswith(
            ('.png', '.jpg', '.jpeg', '.css', '.js', '.woff', '.ico', '.css.map''.js.map', '.svg'))

    @app.before_request
    def before_request():
        if is_ignore_log():
            app.logger.info('Request-Start')

    @app.teardown_request
    def teardown_request(exc):
        if is_ignore_log():
            app.logger.info('Request-End')
