import os
from app.lib import environment
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    SECRET_KEY = environment.get_secret_key() or 'you-will-never-guess-localhost'
    SQLALCHEMY_DATABASE_URI = environment.get_database_url() or \
        'mysql+pymysql://root:root@localhost/2gonyc'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
