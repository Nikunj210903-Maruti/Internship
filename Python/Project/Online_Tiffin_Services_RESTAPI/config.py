class Config(object):
    DEBUG = False
    TESTING = False
    SECRET_KEY = "secret_key"
    USER = "root"
    PASSWORD = "Nikunj210903"
    DATABASE_NAME = "Online_Tiffin_Services"
    HOST = "localhost"

class Production_config(Config):
    pass

class Development_config(Config):
    DEBUG = True

class Testing_config(Config):
    TESTING = True