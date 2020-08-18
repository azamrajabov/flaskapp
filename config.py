import os
from app.lib import environment
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    SECRET_KEY = environment.get_secret_key() or 'you-will-never-guess-localhost'
    SQLALCHEMY_DATABASE_URI = environment.get_database_url() or \
        'mysql+pymysql://root:root@localhost/2gonyc'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    # mail
    # MAIL_SERVER = os.environ.get('MAIL_SERVER')
    # MAIL_PORT = int(os.environ.get('MAIL_PORT') or 25)
    # MAIL_USE_TLS = os.environ.get('MAIL_USE_TLS') is not None
    # MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    # MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
    ADMINS = ['azamrajabov@gmail.com']

    # MAIL_SERVER=smtp.googlemail.com
    # MAIL_PORT=587
    # MAIL_USE_TLS=1
    # MAIL_USERNAME=<your-gmail-username>
    # MAIL_PASSWORD=<your-gmail-password>

    MAIL_SERVER = 'localhost'
    MAIL_PORT = 8025

    POSTS_PER_PAGE = 5

