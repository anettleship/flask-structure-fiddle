from flask import Blueprint
from app.app_factory import db
from app.models import User

api_blueprint = Blueprint("api_blueprint", __name__)


@api_blueprint.route("/")
def index():

    return "Api Route Returns This"

@api_blueprint.route("/users")
def user_list():
    users = db.session.execute(db.select(User).order_by(User.username)).scalars()
    return users