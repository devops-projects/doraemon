from flask_restful import Resource
from flask_jwt_extended import jwt_required

from ..decorators import request_state


class UserListAPI(Resource):

    @request_state
    @jwt_required
    def get(self):
        pass
