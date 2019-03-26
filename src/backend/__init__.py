from flask import Flask
from flask_jwt_extended import JWTManager
from flask_sqlalchemy import SQLAlchemy

from .config import config

jwt = JWTManager()
db = SQLAlchemy()

app_settings = config['default']


def create_app():
    app = Flask(__name__)
    app.config.from_object(app_settings)

    jwt.init_app(app)
    db.init_app(app)

    from .apis import bp as api_blueprint
    app.register_blueprint(api_blueprint, url_prefix='/apis/v1')

    return app
