"""
App builder.
"""

from flask import Flask
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy


from config import config

bootstrap = Bootstrap()
db = SQLAlchemy()


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])

    bootstrap.init_app(app)
    db.init_app(app)

    from knowhow.main import main, views, errors  # noqa
    app.register_blueprint(main)

    from knowhow.admin import admin
    admin.init_app(app)

    return app
