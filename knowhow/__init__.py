"""
App builder.
"""

from flask import Flask
import logging
from config import config


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])

    from knowhow.main import main
    app.register_blueprint(main)

    return app
