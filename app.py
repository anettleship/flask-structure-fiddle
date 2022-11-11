from app.app_factory import create_app
import app.config as config


app = create_app(config.development())

app.run()

