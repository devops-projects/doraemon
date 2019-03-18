from flask import request, jsonify, make_response
from flask_restful import Resource
from flask_jwt_extended import create_access_token


class RegisterAPI(Resource):

    def post(self):
        pass


class LoginAPI(Resource):

    def post(self):
        if not request.is_json:
            return {"msg": "Missing JSON in request"}, 400

        username = request.json.get('username', None)
        password = request.json.get('password', None)

        if not username:
            return {"msg": "Missing username parameter"}, 400
        if not password:
            return {"msg": "Missing password parameter"}, 400

        if username != 'admin' or password != 'admin':
            return {"msg": "Bad username or password"}, 401

        access_token = create_access_token(identity=username)
        return make_response(jsonify({"access_token": access_token}), 200)


class LogoutAPI(Resource):

    def post(self):
        pass
