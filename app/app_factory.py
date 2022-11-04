from flask import Flask
from generic.initial_blueprint import initial_blueprint

import sys


def create_app(config_class):
    """
    Application Factory function to instantiate an application from a given config class defined below.
    """

    app = Flask(__name__)

    app.config.from_object(config_class)

    register_blueprints(app)

    return app


def register_blueprints(app):
    """
    Helper function for application factory create_app()
    """

    app.register_blueprint(initial_blueprint, url_prefix="/healthcheck")

    return app
    