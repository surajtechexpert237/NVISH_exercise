from flask import jsonify


def ping_api():
    """
    API listener that responds to unauthenticated `/ping` calls
    :return: user details as json
    """
    user_details = {'id': 123, 'username': 'john_doe', 'email': 'john@example.com', 'full_name': 'John Doe',
                    'age': 30, 'country': 'USA'}
    return jsonify(user_details), 200
