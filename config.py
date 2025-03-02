import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    SECRET_KEY = 'your_secret_key'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'database.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    TWILIO_ACCOUNT_SID = 'YOUR_TWILIO_ACCOUNT_SID'
    TWILIO_AUTH_TOKEN = 'YOUR_TWILIO_AUTH_TOKEN'
    TWILIO_PHONE_NUMBER = 'YOUR_TWILIO_PHONE_NUMBER'
