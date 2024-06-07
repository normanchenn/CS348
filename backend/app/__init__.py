"""
Init file for Flask
"""

# Imports
import os
from flask import Flask
from .config import DevelopmentConfig, ProductionConfig
from .routes.api import api_v1 as api_v1_blueprint
from .routes.main import main as main_blueprint


def create_app():
    """Creates the flask app

    Returns:
        app (Flask): flask app
    """
    app = Flask(__name__)

    if os.getenv("FLASK_ENV") == "production":
        app.config.from_object(ProductionConfig())
    else:
        app.config.from_object(DevelopmentConfig())

    app.register_blueprint(main_blueprint)
    app.register_blueprint(api_v1_blueprint)

    return app
