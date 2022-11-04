from flask import Blueprint

initial_blueprint = Blueprint("initial_blueprint", __name__)

@initial_blueprint.route("/")
def index():

    return "Blueprint functioning!"