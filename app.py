from flask import Flask
from app.app_factory import create_app
import app.config as config

if __name__ == '__main__':
    app = create_app(config.development())
    app.run()
