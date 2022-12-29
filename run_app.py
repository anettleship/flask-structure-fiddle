from app.app_factory import create_app
import app.config as config

app = create_app(config.development())

def main(app):

    app.run()

if __name__ == "__main__":
    main(app)

