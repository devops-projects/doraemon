from flask import Blueprint
from flask_restful import Api

from .auth import AuthApi
from .user import UserApi, UserApi

bp = Blueprint('api', __name__)
api = Api(bp)

api.add_resource(AuthApi, '/login', '/logout')
api.add_resource(UserApi, '/users', '/users/<string:user_id>')
