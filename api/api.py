from flask import Blueprint, request, current_app
from app.app_factory import db
from app.models import User
from sqlalchemy.exc import IntegrityError

api_blueprint = Blueprint("api_blueprint", __name__)


@api_blueprint.route("/")
def index():

    return "Api Route Returns This"

@api_blueprint.route("/users")
def user_list():
    users = db.session.execute(db.select(User).order_by(User.username)).all()
    return str([data.User.username for data in users])


@api_blueprint.route("/add_user", methods=['GET'])
def add_user():
    username = request.args.get('username')
    email = request.args.get('email')
    
    # get last id from table to insert next id 
    id = get_next_id(db, User) 
    this_user = User(id, email, username)

    # write this user to table
    result = write_table(db, this_user)

    if result == True:
        return f"{username} with email address {email} added to index {id}"
    else:
        return f"Error writing to database: {result}"
    

def get_next_id(db, modelclass):

    last_id = db.session.execute(db.select(modelclass).order_by(modelclass.id.desc())).first()
    if last_id != None:
        return last_id[0].id + 1
    else:
        return 0


def write_table(db, data):

    with current_app.app_context():
        db.session.add(data)
        try:
            db.session.commit()
        except IntegrityError as e:
            return e 

    return True 


