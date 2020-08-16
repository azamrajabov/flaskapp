import os

def get_rds_credentials():
    if not os.environ.get('rds_endpoint', None):
        return None
    return {
        'host': os.environ['rds_endpoint'],
        'username': os.environ['rds_username'],
        'password': os.environ['rds_password'],
        'db': os.environ['rds_db']
    }

def get_secret_key():
    return os.environ.get('SECRET_KEY', None)

def get_database_url():
    rds = get_rds_credentials()
    if not rds:
        return None
    return 'mysql+pymysql://{}:{}@{}/{}'.format(
        rds['username'], rds['password'], rds['host'], rds['db'])
