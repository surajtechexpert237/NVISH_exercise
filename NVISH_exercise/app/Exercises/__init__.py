from flask import Blueprint

from app.Exercises.exercise1 import ping_api
from app.Exercises.exercise2 import authorization_api
from app.Exercises.exercise3 import UserPostAPI, UsersListAPI, UserRetrieveAPI, UserDeleteAPI

bp = Blueprint('bp', __name__)

from app.Exercises import exercise1
from app.Exercises import exercise2
from app.Exercises import exercise3

bp.add_url_rule('/ping', view_func=ping_api, methods=['GET'])
bp.add_url_rule('/authorize', view_func=authorization_api, methods=['POST'])

bp.add_url_rule('/save', view_func=UserPostAPI.as_view('save'), methods=['POST'])
bp.add_url_rule('/get', view_func=UsersListAPI.as_view('get'), methods=['GET'])
bp.add_url_rule('/get/<int:user_id>', view_func=UserRetrieveAPI.as_view('get_user_by_id'), methods=['GET'])
bp.add_url_rule('/delete/<int:user_id>', view_func=UserDeleteAPI.as_view('delete_user_by_id'), methods=['DELETE'])
