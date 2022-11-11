from app.app_factory import db

class User(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, unique=True, nullable=False)
    email = db.Column(db.String) 

    def __init__(self, id: int, email: str, username: str):
        self.id = id
        self.email = email
        self.username = username



