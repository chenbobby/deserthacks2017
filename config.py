class Config(object):
    DEBUG = False
    TESTING = False

    ADMINS = frozenset(['appdev.bobchen@gmail.com'])
    SECRET_KEY = 'secretkey'

    THREADS_PER_PAGE = 2

class DevelopmentConfig(Config):
    DEBUG = True

class TestingConfig(Config):
    TESTING = True
