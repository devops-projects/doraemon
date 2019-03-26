import os


class Config:
    JWT_SECRET_KEY = os.environ.get('JWT_SECRET_KEY') or 'hard to guess string'
    JWT_TOKEN_LOCATION = ['json']
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('DEV_DATABASE_URL')


class ProductionConfig(Config):
    pass


config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,

    'default': DevelopmentConfig
}
