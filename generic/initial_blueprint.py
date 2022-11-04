from flask import Blueprint, current_app
import os


initial_blueprint = Blueprint("initial_blueprint", __name__)

@initial_blueprint.route("/")
def index():

    secret_key = current_app.secret_key

    if secret_key != None:
        if len(secret_key) > 0:
            return "Application passed basic healthcheck"

    raise EnvironmentError("Valid Secret Key not set!")
    