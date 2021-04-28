import os

class Config:

    SECRET_KEY=os.environ.get('SECRET_KEY')
    # SQLALCHEMY_DATABASE_URI ='postgresql+psycopg2://ubuntustan:ubuntustan@localhost/pitch'
    
    SQLALCHEMY_TRACK_MODIFICATIONS = False 

    UPLOADED_PHOTOS_DEST ='app/static/photos'

    #  email configurations
    MAIL_SERVER='smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")
    SUBJECT_PREFIX = 'Pitch-App!'
    SENDER_EMAIL = 'danstanmshivs@gmail.com'

    @staticmethod
    def init_app(app):
        pass

class ProdConfig(Config):
    '''
    Production  configuration child class
    Args:
        Config: The parent configuration class with General configuration settings
    '''
    SQLALCHEMY_DATABASE_URI = "postgresql://dwosuyycltvhlc:1eabc28e865a24df4a3c4886fd6632b75b1aa5b2911ca2ad9b027a7919cde652@ec2-54-87-112-29.compute-1.amazonaws.com:5432/dcbl0lb2jcva2q?sslmode=require"

class TestConfig(Config):
    SQLALCHEMY_DATABASE_URI ='postgresql+psycopg2://postgres:@localhost/pitch_test'


class DevConfig(Config):
    '''
    Development  configuration child class
    Args:
        Config: The parent configuration class with General configuration settings
    '''
    SQLALCHEMY_DATABASE_URI ='postgresql+psycopg2://postgres:test123@localhost/pitch'

    DEBUG = True

config_options = {
'development':DevConfig,
'production':ProdConfig,
'test':TestConfig
}