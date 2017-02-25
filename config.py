class Config(object):
    DEBUG = False
    TESTING = False

    ADMINS = frozenset(['appdev.bobchen@gmail.com'])
    SECRET_KEY = 'secretkey'

    WTF_CSRF_ENABLED = True

    THREADS_PER_PAGE = 2

class DevelopmentConfig(Config):
    DEBUG = True

class TestingConfig(Config):
    TESTING = True
