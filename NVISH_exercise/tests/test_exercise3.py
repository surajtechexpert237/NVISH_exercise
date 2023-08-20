# Test cases for POST API
from app import db
from app.models import User


def test_user_post_endpoint_valid_input(app):
    """
    Valid data is provided
    """
    data = {
        'first_name': 'Mark',
        'last_name': 'Doe',
        'username': 'mark21',
        'password': 'password123',
        'email': 'mark@gmail.com'
    }
    with app.test_client() as client:
        response = client.post('/save', json=data)

    assert response.status_code == 201
    response_data = response.json
    assert 'message' in response_data
    assert response_data['message'] == 'User registered successfully!'



def test_user_post_endpoint_missing_email_field(app):
    """
    Email field is missing
    """
    data = {
        'first_name': 'Mark',
        'last_name': 'Doe',
        'username': 'mark21',
        'password': 'password123'
    }
    with app.test_client() as client:
        response = client.post('/save', json=data)

    assert response.status_code == 422
    assert response.json == {'email': ['Missing data for required field.']}
    
    
def test_user_post_endpoint_email_already_exists(app):
    """
    Email already exists
    """
    user = User(first_name='mark', last_name='Doe', username='markdoe', password='password123',
                email='mark@gmail.com')
    db.session.add(user)
    db.session.commit()

    data = {
        'first_name': 'Mark',
        'last_name': 'Doe',
        'username': 'mark21',
        'password': 'password123',
        'email': 'mark@gmail.com'
    }
    with app.test_client() as client:
        response = client.post('/save', json=data)

    assert response.status_code == 422
    assert response.json == {'email': ['Email already exists!']}


def test_user_post_endpoint_username_already_exists(app):
    """
    Username already exists
    """
    user = User(first_name='mark', last_name='Doe', username='markdoe', password='password123',
                email='mark@gmail.com')
    db.session.add(user)
    db.session.commit()

    data = {
        'first_name': 'Mark',
        'last_name': 'Doe',
        'username': 'markdoe',
        'password': 'password123',
        'email': 'markdoe@gmail.com'
    }
    with app.test_client() as client:
        response = client.post('/save', json=data)

    assert response.status_code == 422
    assert response.json == {'username': ['Username already exists!']}


def test_user_post_endpoint_missing_first_name(app):
    """
    First name field is missing
    """
    data = {
        'email': 'mark@gmail.com',
        'last_name': 'Doe',
        'username': 'mark21',
        'password': 'password123'
    }
    with app.test_client() as client:
        response = client.post('/save', json=data)

    assert response.status_code == 422
    assert response.json == {'first_name': ['Missing data for required field.']}


def test_user_post_endpoint_missing_last_name(app):
    """
    Last name field is missing
    """
    data = {
        'email': 'mark@gmail.com',
        'first_name': 'Doe',
        'username': 'mark21',
        'password': 'password123'
    }
    with app.test_client() as client:
        response = client.post('/save', json=data)

    assert response.status_code == 422
    assert response.json == {'last_name': ['Missing data for required field.']}


def test_user_post_endpoint_missing_username_name(app):
    """
    Username field is missing
    """
    data = {
        'email': 'mark@gmail.com',
        'first_name': 'Doe',
        'last_name': 'mark',
        'password': 'password123'
    }
    with app.test_client() as client:
        response = client.post('/save', json=data)

    assert response.status_code == 422
    assert response.json == {'username': ['Missing data for required field.']}


def test_user_post_endpoint_missing_password_name(app):
    """
    Password field is missing
    """
    data = {
        'email': 'mark@gmail.com',
        'first_name': 'Doe',
        'last_name': 'mark',
        'username': 'mark21'
    }
    with app.test_client() as client:
        response = client.post('/save', json=data)

    assert response.status_code == 422
    assert response.json == {'password': ['Missing data for required field.']}


def test_user_post_endpoint_invalid_email(app):
    """
    Invalid email is passed
    """
    data = {
        'email': 'markgmail.com',
        'first_name': 'Doe',
        'last_name': 'mark',
        'username': 'mark21',
        'password': 'password123'
    }
    with app.test_client() as client:
        response = client.post('/save', json=data)

    assert response.status_code == 422
    assert response.json == {"email": [
        "Not a valid email address."
    ]}


def test_user_post_endpoint_username_less_than_6_characters(app):
    """
    Username contains less than 6 characters
    """
    data = {
        'email': 'mark@gmail.com',
        'first_name': 'Doe',
        'last_name': 'mark',
        'username': 'mark2',
        'password': 'password123'
    }
    with app.test_client() as client:
        response = client.post('/save', json=data)

    assert response.status_code == 422
    assert response.json == {"username": [
        "Username must be between 6 and 20 characters"
    ]}

def test_user_post_endpoint_username_greater_than_20_characters(app):
    """
    Username contains more than 20 characters
    """
    data = {
        'email': 'mark@gmail.com',
        'first_name': 'Doe',
        'last_name': 'mark',
        'username': 'mark222222222222222222222222',
        'password': 'password123'
    }
    with app.test_client() as client:
        response = client.post('/save', json=data)

    assert response.status_code == 422
    assert response.json == {"username": [
        "Username must be between 6 and 20 characters"
    ]}

def test_user_post_endpoint_username_other_than_alphanumeric(app):
    """
    Username contains charcters other than alphanumeric
    """
    data = {
        'email': 'mark@gmail.com',
        'first_name': 'Doe',
        'last_name': 'mark',
        'username': 'markdoe*',
        'password': 'password123'
    }
    with app.test_client() as client:
        response = client.post('/save', json=data)

    assert response.status_code == 422
    assert response.json == {"username": [
        "Username must contain only alphanumeric characters"
    ]}


def test_user_post_endpoint_first_name_containing_digits(app):
    """
    First name contains digits
    """
    data = {
        'email': 'mark@gmail.com',
        'first_name': 'Doe1',
        'last_name': 'mark',
        'username': 'markdoe',
        'password': 'password123'
    }
    with app.test_client() as client:
        response = client.post('/save', json=data)

    assert response.status_code == 422
    assert response.json == {"first_name": [
        "First name must contain only letters"
    ]}


def test_user_post_endpoint_last_name_containing_digits(app):
    """
    Last name contains digits
    """
    data = {
        'email': 'mark@gmail.com',
        'last_name': 'Doe1',
        'first_name': 'mark',
        'username': 'markdoe',
        'password': 'password123'
    }
    with app.test_client() as client:
        response = client.post('/save', json=data)

    assert response.status_code == 422
    assert response.json == {"last_name": [
        "Last name must contain only letters"
    ]}

def test_user_post_endpoint_password_length_less_than_6(app):
    """
    Password contains less than 6 characters
    """
    data = {
        'email': 'mark@gmail.com',
        'last_name': 'Doe',
        'first_name': 'mark',
        'username': 'markdoe',
        'password': 'pass'
    }
    with app.test_client() as client:
        response = client.post('/save', json=data)

    assert response.status_code == 422
    assert response.json == {"password": [
        "Password must be between 6 and 20 characters"
    ]}

def test_user_post_endpoint_password_length_greater_than_20(app):
    """
    Password contains more than 20 characters
    """
    data = {
        'email': 'mark@gmail.com',
        'last_name': 'Doe',
        'first_name': 'mark',
        'username': 'markdoe',
        'password': 'password123456123456123456123456'
    }
    with app.test_client() as client:
        response = client.post('/save', json=data)

    assert response.status_code == 422
    assert response.json == {"password": [
        "Password must be between 6 and 20 characters"
    ]}

def test_user_post_endpoint_invalid_http_method(client):
    """
    Invalid http method
    """
    response = client.get('/save')

    assert response.status_code == 405


def test_user_post_endpoint_no_json_provided(client):
    """
    No json data passed
    """
    response = client.post('/save')

    assert response.status_code == 415



# Test cases for List User API


def test_users_list_endpoint_empty_db(app):
    """
    Database is empty
    """
    with app.test_client() as client:
        response = client.get('/get')

    assert response.status_code == 200
    assert response.json['data'] == []


def test_users_list_endpoint_with_users(app):
    """
    Database contains users
    """
    user1 = User(first_name='Mark', last_name='Doe', username='Markdoe', password='password1',
                 email='mark@gmail.com')
    user2 = User(first_name='mark', last_name='Smith', username='marksmith', password='password2',
                 email='mark1@gmail.com')
    db.session.add_all([user1, user2])
    db.session.commit()

    with app.test_client() as client:
        response = client.get('/get')

    assert response.status_code == 200
    users_data = response.json['data']
    assert len(users_data) == 2

    assert users_data[0]['first_name'] == 'Mark'
    assert users_data[0]['last_name'] == 'Doe'
    assert users_data[0]['username'] == 'Markdoe'
    assert users_data[0]['email'] == 'mark@gmail.com'

    assert users_data[1]['first_name'] == 'mark'
    assert users_data[1]['last_name'] == 'Smith'
    assert users_data[1]['username'] == 'marksmith'
    assert users_data[1]['email'] == 'mark1@gmail.com'


def test_users_list_endpoint_invalid_http_method(app):
    """
    Invalid http method
    """
    with app.test_client() as client:
        response = client.post('/get')

    assert response.status_code == 405
    
    
# Test cases for Retrieving user API


def test_user_retrieve_endpoint_existing_user(app):
    """
    Retrive user that exists in database
    """
    user = User(first_name='mark', last_name='Doe', username='markdoe', password='password123',
                email='mark@gmail.com')
    db.session.add(user)
    db.session.commit()

    with app.test_client() as client:
        response = client.get('/get/1')

    assert response.status_code == 200
    user_data = response.json
    assert user_data['first_name'] == 'mark'
    assert user_data['last_name'] == 'Doe'
    assert user_data['username'] == 'markdoe'
    assert user_data['email'] == 'mark@gmail.com'


def test_user_retrieve_endpoint_nonexistent_user(app):
    """
    Retrieve user that doesn't exists in database
    """
    with app.test_client() as client:
        response = client.get('/get/1')

    assert response.status_code == 404
    assert response.json == {'message': 'User not found'}


def test_user_retrieve_endpoint_invalid_http_method(app):
    """
    Invalid http method
    """
    with app.test_client() as client:
        response = client.post('/get/1')

    assert response.status_code == 405
    
    
# Test Cases for delete user API

def test_user_delete_endpoint_existing_user(app):
    """
    Delete user that exists in database
    """
    user = User(first_name='mark', last_name='Doe', username='markdoe', password='password123',
                email='mark@gmail.com')
    db.session.add(user)
    db.session.commit()

    with app.test_client() as client:
        response = client.delete('/delete/1')

    assert response.status_code == 200
    assert response.json == {'message': 'User deleted successfully'}
    assert User.query.get(1) is None


def test_user_delete_endpoint_nonexistent_user(app):
    """
    Delete user that doesn't exists in database
    """
    with app.test_client() as client:
        response = client.delete('/delete/5')

    assert response.status_code == 404
    assert response.json == {'message': 'User not found'}


def test_user_delete_endpoint_invalid_http_method(app):
    """
    Invalid http method
    """
    with app.test_client() as client:
        response = client.get('/delete/1')

    assert response.status_code == 405
