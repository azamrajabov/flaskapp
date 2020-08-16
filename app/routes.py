from flask import render_template, flash, redirect
from app import app
import sentry_sdk
from sentry_sdk.integrations.flask import FlaskIntegration
from app.forms.login import LoginForm


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
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': {'username': 'Susan'},
            'body': 'The Avengers movie was so cool!'
        }
    ]
    return render_template('index.html', title='Home', user=user, posts=posts)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for user {}, remember_me={}'.format(
            form.username.data, form.remember_me.data))
        return redirect('/index')
    return render_template('login.html', title='Sign In', form=form)
