import json
from flask.views import MethodView
from flask import request, jsonify, Response
from marshmallow import ValidationError
from app import db, redis_client
from app.models import User
from app.schema import UserSchema


class UserPostAPI(MethodView):
    """
    User registration API that allows posting of a key / value pair into a database table (INCLUDES CACHING)
    sample data :-
            {
            "first_name":"steave",
            "last_name":"jobs",
            "username":"AppleUser",
            "password":"Apple@123",
            "email":"iphone@user.com"
            }
    """

    def post(self):
        key = "message"
        value = "User registered successfully!"
        redis_client.set(key, value, ex=10)
        cached_data = redis_client.get("message").decode('utf-8')
        user_schema = UserSchema()
        data = request.get_json()
        try:
            # Validating and deserializing input
            user_data = user_schema.load(data)
        except ValidationError as err:
            return jsonify(err.messages), 422

        # Create new user and set password
        user = User(
            first_name=user_data['first_name'],
            last_name=user_data['last_name'],
            username=user_data['username'],
            password=user_data['password'],
            email=user_data.get('email')
        )

        user.set_password(user_data['password'])
        db.session.add(user)
        db.session.commit()
        return jsonify({'message': cached_data}), 201


class UsersListAPI(MethodView):
    """
    API that allows the user to list all users from the database (INCLUDES CACHING)
    :return: cached data
    """

    def get(self):
        users = User.query.all()
        user_schema = UserSchema(many=True)
        users_data = user_schema.dump(users)
        redis_client.set('data', json.dumps(users_data), ex=10)  # here we set caching for List of data
        cached_data = redis_client.get("data")  # here we get data from cache
        cached_data = cached_data.decode('utf-8')
        cached_data_json = json.loads(cached_data)
        return jsonify({'data': cached_data_json}), 200  # here returned cached data everytime


class UserRetrieveAPI(MethodView):
    """
    API that allows the user to retrieve user from the database
    """

    def get(self, user_id):
        user = User.query.get(user_id)

        if not user:
            return jsonify({'message': 'User not found'}), 404

        user_schema = UserSchema()
        user_data = user_schema.dump(user)

        return jsonify(user_data), 200


class UserDeleteAPI(MethodView):
    """
    API that allows the user to delete user from the database
    """

    def delete(self, user_id):
        user = User.query.get(user_id)

        if not user:
            return jsonify({'message': 'User not found'}), 404

        db.session.delete(user)
        db.session.commit()

        return jsonify({'message': 'User deleted successfully'}), 200
