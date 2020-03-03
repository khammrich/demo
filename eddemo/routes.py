"""
Routes and views for the flask application.
"""
from flask import current_app as app
from datetime import datetime
from flask import render_template
from io import BytesIO
import pycurl


def navigation():
    nav = [{'name': 'Home', 'url': '/'},
            {'name': 'About', 'url': 'about'},
            {'name': 'pycURL', 'url': 'pythoncurl'}]


@app.route('/')
def home():
    """Landing page"""
    nav = [{'name': 'Home', 'url': 'home'},
           {'name': 'About', 'url': 'about'},
           {'name': 'pycURL', 'url': 'pythoncurl'}]
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
        title='Home Page',
        year=datetime.now().year
    )


@app.route('/contact')
def contact():
    """Renders the contact page."""
    return render_template(
        'contact.html',
        title='Contact',
        year=datetime.now().year,
        message='Your contact page.'
    )


@app.route('/about')
def about():
    """Renders the about page."""
    return render_template(
        'about.html',
        title='About',
        year=datetime.now().year,
        message='Your application description page.'
    )


@app.route('/userauth')
def userauth():
    user = {'username': 'Miguel'}
    return render_template(
        'userauth.html',
        title='Home',
        user=user
    )


@app.route('/pythoncurl')
def pythoncurl():
    """Renders the about page."""
    return render_template(
        'pythoncurl.html',
        title='Python Curl',
        year=datetime.now().year,
        message='Your application description page.'
    )


def curlcode():
    b_obj = BytesIO()
    crl = pycurl.Curl()

    # Set URL value
    crl.setopt(crl.URL, 'https://wiki.python.org/moin/BeginnersGuide')

    # Write bytes that are utf-8 encoded
    crl.setopt(crl.WRITEDATA, b_obj)

    # Perform a file transfer
    crl.perform()

    # End curl session
    crl.close()

    # Get the content stored in the BytesIO object (in byte characters)
    get_body = b_obj.getvalue()

    # Decode the bytes stored in get_body to HTML and print the result
    print('Output of GET request:\n%s' % get_body.decode('utf8'))
