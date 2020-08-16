import os

def get_rds_credentials():
    if not os.environ.get('RDS_ENDPOINT', None):
        return None
    return {
        'host': os.environ['RDS_ENDPOINT'],
        'username': os.environ['RDS_USERNAME'],
        'password': os.environ['RDS_PASSWORD'],
        'db': os.environ['RDS_DB']
    }

def get_secret_key():
    return os.environ.get('SECRET_KEY', None)

def get_database_url():
    rds = get_rds_credentials()
    if not rds:
        return None
    return 'mysql+pymysql://{}:{}@{}/{}'.format(
        rds['username'], rds['password'], rds['host'], rds['db'])
