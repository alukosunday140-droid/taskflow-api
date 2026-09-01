from flask import Flask

from app.config import Config
from app.extensions import db


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    db.init_app(app)

    from app.models.task import Task  # noqa: F401

    from app.api import api_bp

    app.register_blueprint(api_bp)

    from app.errors import register_error_handlers

    register_error_handlers(app)

    with app.app_context():
        db.create_all()

    return app
