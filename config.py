import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'hard to guess string'
    MAIL_SERVER = 'smtp.163.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = False
    SSL_REDIRECT = False
    MAIL_USE_SSL = True
    FLASKY_MAIL_SUBJECT_PREFIX = '[Flasky]'
    FLASKY_MAIL_SENDER = 'zxqrenwen@163.com'
    FLASKY_ADMIN = 'zxqrenwen@163.com'
    MAIL_USERNAME = 'test'
    MAIL_PASSWORD = 'test'
    FLASKY_POSTS_PER_PAGE = 10
    FLASK_FOLLOWERS_PER_PAGE = 10
    FLASKY_FOLLOWERS_PER_PAGE =10
    FLASKY_COMMENTS_PER_PAGE = 10

    @staticmethod
    def init_app(app):
        pass


class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.environ.get(
        'DEV_DATABASE_URL') or 'mysql://root:123456@127.0.0.1/myblog_dev'


class TestingConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = os.environ.get(
        'TEST_DATABASE_URL') or 'mysql://root:123456@127.0.0.1/myblog_test'


class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.environ.get(
        'DATABASE_URL') or 'mysql://root:123456@127.0.0.1/myblog'


config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig
}
