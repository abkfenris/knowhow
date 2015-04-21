"""
App builder.
"""

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import config


db = SQLAlchemy()


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])

    db.init_app(app)

    from knowhow.main import main
    app.register_blueprint(main)

    from admin import admin
    admin.init_app(app)

    return app
