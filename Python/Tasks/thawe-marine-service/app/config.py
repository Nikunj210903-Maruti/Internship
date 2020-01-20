import os
from builtins import int
from distutils.util import strtobool


def configure_app(app):
    #app.config['ENVIRONMENT'] = os.environ.get("ENVIRONMENT")
    #app.config['DEBUG'] = strtobool(os.environ.get("DEBUG", "0"))
    #app.config['TESTING'] = strtobool(os.environ.get("TESTING", "0"))
    app.config['PORT'] = int(os.environ.get("BOT_SETTINGS_SERVICE", 5009))

    app.config["MYSQL_DATABASE_HOST"] = os.environ.get("MYSQL_DATABASE_HOST")
    app.config["MYSQL_CORE_DATABASE"] = os.environ.get("MYSQL_DATABASE_NAME")
    app.config["MYSQL_DATABASE_USER"] = os.environ.get("MYSQL_DATABASE_USER")
    app.config["MYSQL_DATABASE_PASSWORD"] = os.environ.get("MYSQL_DATABASE_PASSWORD")

    # Logger
    app.config['GL_SERVER'] = os.environ.get("GL_SERVER", 'localhost')
    app.config['GL_PORT'] = int(os.environ.get("GL_PORT", 12201))
    app.config['ENABLE_GRAYLOG'] = int(os.environ.get('ENABLE_GRAYLOG', 0))

    app.config["ERROR_WEBHOOK_URL"] = os.environ.get("ERROR_WEBHOOK_URL")

    app.config['USER']="kunjvadodariya040798@gmail.com"
    app.config['PASSWORD'] = "Kunjvadodariya040798#"
    app.config['GOOGLE_IMAP_SERVER'] = "imap.gmail.com"
