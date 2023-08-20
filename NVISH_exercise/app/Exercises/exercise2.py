from flask import jsonify, request
from app.config import Config


def authorization_api():
    """
    Authentication using pre-shared secrets that added in request header
    :arg: Authorization (secret key) This param use in header
    :return: Success/Fail message
    """
    auth_key = request.headers.get('Authorization')
    if auth_key == Config.SECRET_KEY:
        return jsonify({'message': 'Authorization successful'}), 200
    else:
        return jsonify({'message': 'Authorization failed'}), 401
