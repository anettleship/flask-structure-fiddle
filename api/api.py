from flask import Blueprint, request, current_app
from app.app_factory import db
from app.models import User
from sqlite3 import IntegrityError

api_blueprint = Blueprint("api_blueprint", __name__)


@api_blueprint.route("/")
def index():

    return "Api Route Returns This"

@api_blueprint.route("/users")
def user_list():
    users = db.session.execute(db.select(User).order_by(User.username)).scalars()
    return list(users)

@api_blueprint.route("/add_user", methods=['GET'])
def add_user():
    username = request.args.get('username')
    email = request.args.get('email')
    last_user_num = db.session.execute(db.select(User).order_by(User.id)).first()
    if last_user_num == None:
        id = 0
    else:
        id = last_user_num[0].id + 1
    this_user = User(id, email, username)

    with current_app.app_context():
        db.session.add(this_user)
        try:
            db.session.commit()
        except IntegrityError:
            return f"{username} exists in database already"

    return f"{username} with email address {email} added to index {id}"