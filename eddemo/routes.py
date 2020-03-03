"""
Routes and views for the flask application.
"""
from flask import current_app as app
from datetime import datetime
from flask import render_template
from io import BytesIO
from eddemo.navi import nav
from eddemo.pyc2 import output


@app.route('/')
def home():
    """Landing page"""
    return render_template(
        'home.html',
        nav=nav,
        title="Flask and Jinja Demo Site",
        description="Work examples \
         with flask & Jinja."
    )


@app.route('/index')
def index():
    """Renders the home page."""
    return render_template(
        'index.html',
        nav=nav,
        title='Home Page',
        year=datetime.now().year
    )


@app.route('/contact')
def contact():
    """Renders the contact page."""
    return render_template(
        'contact.html',
        nav=nav,
        title='Contact me',
        year=datetime.now().year,
        message='The following are ways to contact me'
    )


@app.route('/about')
def about():
    """Renders the about page."""
    return render_template(
        'about.html',
        nav=nav,
        title='About this site',
        year=datetime.now().year,
        message='This site shows different applications of Flask'
    )


@app.route('/userauth')
def userauth():
    user = {'username': 'Miguel'}
    return render_template(
        'userauth.html',
        nav=nav,
        title='Home',
        user=user
    )


@app.route('/pythoncurl')
def pythoncurl():
    """Renders the Python cURL page."""
    return render_template(
        'pythoncurl.html',
        nav=nav,
        title='Python Curl',
        year=datetime.now().year,
        message='Your application description page.',
        output=output
    )

