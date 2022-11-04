from flask import Flask
from initial_blueprint import initial_blueprint

app = Flask(__name__)
app.register_blueprint(initial_blueprint)

app.run()