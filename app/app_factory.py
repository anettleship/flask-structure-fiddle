from flask import Flask
from generic.initial_blueprint import initial_blueprint
from flask_sqlalchemy import SQLAlchemy

import sys


def create_app(config_class):
    """
    Application Factory function to instantiate an application from a given config class defined below.
    """

    app = Flask(__name__)

    app.config.from_object(config_class)

    register_blueprints(app)

    db = init_database(app)

    # Where and how noow do we declare our Models classes as a subclass of db.Model?

    return app


def register_blueprints(app):
    """
    Helper function for application factory create_app()
    """

    app.register_blueprint(initial_blueprint, url_prefix="/healthcheck")

    return app


def init_database(app):
    """
    Function to initialise database as specified by settings config applied to app.
    """

    db = SQLAlchemy()

    # SQL Database config has already been set by config object passed to create_app

    db.init_app(app)    

    return db