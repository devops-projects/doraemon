from flask_restful import Resource

from ..decorators import request_state


class UserApi(Resource):
    method_decorators = [request_state]

    def get(self):
        pass

    def post(self):
        pass

    def put(self):
        pass
