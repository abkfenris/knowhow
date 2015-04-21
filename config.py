import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or '+Ha;32+tYt9FDxNFN3U}xHA4mCqKE4nZ>VP9#(78ckp*9ey^'
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True


class DevelopmentConfig(Config):
    DEBUG = True
    SQL_ALCHEMY_DATABASE_URI = 'postgresql://localhost/knowhow'


class TestingConfig(Config):
    TESTING = True
    SQL_ALCHEMY_DATABASE_URI = 'sqlite:///testing.db'


class ProductionConfig(Config):
    pass


config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,

    'default': DevelopmentConfig
}
