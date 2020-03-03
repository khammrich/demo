from flask import Flask, url_for, Markup, render_template, request, Response
from flask_sqlalchemy import SQLAlchemy
from flask_redis import FlaskRedis
from flask_login import login_manager
from flask_session import sessions
# from flask_wtf import form
# from werkzeug import url_encode
# Globally accessible libraries
db = SQLAlchemy()
r = FlaskRedis()


def create_app():
    """Initialize the core application."""
    app = Flask(__name__,
                instance_relative_config=False,
                template_folder="templates",
                static_folder="static")
    app.config.from_object('config.Config')

    # Initialize Plugins
    db.init_app(app)
    r.init_app(app)

    with app.app_context():
        # Include our Routes
        from . import routes
        from . import forms
        from . import models

        # Register Blueprints
        # app.register_blueprint(auth.auth_bp)
        # app.register_blueprint(admin.admin_bp)

        return app
