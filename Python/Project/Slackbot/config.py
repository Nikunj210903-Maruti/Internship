class Config(object):
    DEBUG = False
    TESTING = False

class Production_config(Config):
    pass

class Development_config(Config):
    DEBUG = True

class Testing_config(Config):
    TESTING = True




