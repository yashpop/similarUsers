import os
from flask import Flask
#from app import app
#app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))
#app.config['SECRET_KEY'] = 'you-will-never-guess'

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:////'+os.path.join(basedir,'app.db')

    SQLALCHEMY_TRACK_MODIFICATIONS = False
