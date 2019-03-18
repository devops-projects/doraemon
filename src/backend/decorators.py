from functools import wraps

from flask import jsonify, request


def request_state(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        return jsonify({
            "method": request.method,
            "url": request.url,
            "data": request.json,
        })

    return wrapper
