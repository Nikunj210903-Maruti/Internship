import logging
import os
from logging.handlers import TimedRotatingFileHandler

from flask import Flask
from flask_log_request_id import RequestID
from flask_restful import Api
from pygelf import GelfUdpHandler

from .common import make_dir, GrayLogContextFilter, RequestFormatter, errors, APP_NAME, PRODUCT_NAME
from .config import configure_app

__all__ = ['create_app', 'create_api', 'app_init']


def create_app():
    """Initialize Flask Application"""
    app = Flask(__name__)
    configure_app(app)
    configure_logging(app)
    RequestID(app)
    configure_hook(app)
    return app


def create_api(app):
    """ Initialize Flask RESTful"""
    api = Api(app, prefix="/api", errors=errors)
    return api


def configure_logging_log_file(app):
    """Track Logging in Log file"""
    log_folder_location = os.path.abspath(os.path.join(__file__, '..', '..', 'data', 'logs'))

    make_dir(log_folder_location)

    app.logger.setLevel(logging.INFO)
    log_file = '{0}/log'.format(log_folder_location)
    handler = TimedRotatingFileHandler(log_file, when='midnight',
                                       interval=1, encoding='utf8', backupCount=1825)
    handler.setLevel(logging.INFO)

    formatter = RequestFormatter(
        '[%(asctime)s] [%(levelname)s] [%(correlation_id)s] '
        '[%(method)s] [%(path_info)s] [%(query_string)s] '
        '[%(pathname)s] %(funcName)s: %(lineno)d : %(message)s] '
        '[%(ip_address)s] [%(http_origin)s] [%(user_agent)s] ')
    handler.setFormatter(formatter)
    app.logger.addHandler(handler)


def configure_graylog(app):
    """Set up Graylog"""

    additional_fields = {
        "app": APP_NAME,
        "facility": PRODUCT_NAME,
        "environment": app.config['ENVIRONMENT']}

    app.logger.setLevel(logging.INFO)
    gelf_upd_handler = GelfUdpHandler(host=app.config["GL_SERVER"],
                                      port=app.config["GL_PORT"],
                                      include_extra_fields=True,
                                      compress=False,
                                      chunk_size=1300,
                                      **additional_fields)

    gelf_upd_handler.debug = True
    gelf_upd_handler.setLevel(logging.INFO)
    app.logger.addFilter(GrayLogContextFilter())
    app.logger.addHandler(gelf_upd_handler)


def configure_logging(app):
    """Set up the global logging settings."""

    if app.config["ENABLE_GRAYLOG"]:
        configure_graylog(app)
    else:
        configure_logging_log_file(app)


def configure_hook(app):
    @app.before_request
    def before_request():
        app.logger.info('Request-Start')

    @app.teardown_request
    def teardown_request(exc):
        app.logger.info('Request-End')


def app_init():
    pass
    # from .core import init_queue_service
    # init_queue_service()
