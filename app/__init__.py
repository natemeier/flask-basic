
from flask import Flask

from app.views.public import public


def create_app(config, debug=False):
    """Setup Flask application."""
    app = Flask(__name__)
    app.debug = debug
    app.config.from_object(config)

    app.register_blueprint(public)

    return app
