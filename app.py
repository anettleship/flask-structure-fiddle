from flask import Flask
from app_factory import create_app
import config


app = create_app(config.development)

app.run()