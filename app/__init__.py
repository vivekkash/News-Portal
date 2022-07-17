from flask import Flask
from .routes import news

def create_app():

    app = Flask(__name__)

    app.config.from_prefixed_env()

    app.register_blueprint(news)

    return app


