import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    SECRET_KEY = 'your_secret_key'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'database.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    TWILIO_ACCOUNT_SID = 'AC1fd51279bbd53e9411dd1dc948a22d2c'
    TWILIO_AUTH_TOKEN = '3e64a066e3836c645396cc4ae835697e'
    TWILIO_PHONE_NUMBER = '+15306076772'
