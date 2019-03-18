from flask import Flask
from flask_jwt_extended import JWTManager

jwt = JWTManager()


def create_app():
    app = Flask(__name__)
    app.config['JWT_SECRET_KEY'] = "some-secret"
    app.config['JWT_TOKEN_LOCATION'] = ['json']

    jwt.init_app(app)

    from .api import bp as api_blueprint
    app.register_blueprint(api_blueprint, url_prefix='/api')

    return app
