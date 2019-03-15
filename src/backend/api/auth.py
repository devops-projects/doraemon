from flask_restful import Resource

from ..decorators import request_state


class AuthApi(Resource):
    method_decorators = [request_state]

    def get(self):
        pass

    def post(self):
        pass
