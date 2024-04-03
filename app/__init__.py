# __init__.py
from flask import Flask
from app.urls import webhook_blueprint
from app.config import Config


def create_app():
    app = Flask(__name__)

    # Load configurations and logging settings
    env_path = "/Users/mohamed/Desktop/mY-pRojeCts/kzm/Kzm_WhatsApp_BOt/.env"
    Config(app, env_path)
    # Import and register blueprints, if any
    app.register_blueprint(webhook_blueprint)

    return app
