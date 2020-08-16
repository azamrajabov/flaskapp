from flask import render_template
from app import app
import sentry_sdk
from sentry_sdk.integrations.flask import FlaskIntegration


sentry_sdk.init(
    dsn="https://ef289e49683a40e2b5ad86e8e9f5d91e@sentry.io/2727567",
    integrations=[FlaskIntegration()]
)


@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Miguel'}
    posts = [
        {
            'author': {'username': 'John'},
            'body': app.config['SECRET_KEY']
        },
        {
            'author': {'username': 'Susan'},
            'body': app.config['SQLALCHEMY_DATABASE_URI']
        }
    ]
    return render_template('index.html', title='Home', user=user, posts=posts)
