from flask import Blueprint
from flask_restful import Api

bp = Blueprint('apis', __name__)
api = Api(bp)

from .auth import RegisterAPI, LoginAPI, LogoutAPI
from .user import UserListAPI

api.add_resource(RegisterAPI, '/auth/register')
api.add_resource(LoginAPI, '/auth/login')
api.add_resource(LogoutAPI, '/auth/logout')

api.add_resource(UserListAPI, '/users')
