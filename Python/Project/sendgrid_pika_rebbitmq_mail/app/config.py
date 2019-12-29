import datetime
import json
import os
from distutils.util import strtobool

__all__ = ['configure_app']


def configure_app(app):
    app.config[
        'RABBIT_MQ_URL_PARAMETER'] = "amqp://guest:guest@localhost:5672/%2F"
    app.config['RABBIT_MQ_HOST_URL'] = "http://localhost:15672"
    app.config['RABBIT_MQ_USERNAME'] = "guest"
    app.config['RABBIT_MQ_PASSWORD'] = "guest"
    app.config['RMQ_EXCHANGE'] = "sample.direct"
    app.config['TEMPLATE_ID'] = 'd-c2e00e5d56f045fca53f5ec5e47c1873'
    app.config['FROM_EMAIL'] = 'nikunjbhai.nb@example.com'
    app.config['API_KEY'] = "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"
