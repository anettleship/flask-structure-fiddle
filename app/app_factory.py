from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# Instantiate sqlalchemy db model here so we can import it into models.py
db = SQLAlchemy()

from api.api import api_blueprint
from generic.initial_blueprint import initial_blueprint

# import models after instantiating db, so we can import the db object and make subclasses from it in models.py
# this needs to be done ahead of the db.create_all() call, or SQLalchemy will not know about our models.
# In this case our blueprints already call upon some classes from Models, we do not wish to rely on these blueprints to do this.
import app.models

def create_app(config_class):
    """
    Application Factory function to instantiate an application from a given config class defined below.
    """

    app = Flask(__name__)

    app.config.from_object(config_class)

    register_blueprints(app)

    # if models are imported within our blueprints, we can only instantiate our db after importing blueprints
    # broadly, we must make sure we have imported models before this point, so that db.create_all() is aware of our models.
    init_database(app)

    # Where and how noow do we declare our Models classes as a subclass of db.Model?

    return app


def register_blueprints(app):
    """
    Helper function for application factory create_app()
    """

    app.register_blueprint(initial_blueprint, url_prefix="/healthcheck")
    app.register_blueprint(api_blueprint)

    return app


def init_database(app):
    """
    Function to initialise database as specified by settings config applied to app.
    """
    # db object has already been instantiated at the top of this file ahead of importing models and blueprints
    # SQL Database config has already been set by config object passed to create_app

    db.init_app(app)
    with app.app_context():
        db.create_all()

    return db