from app import Config


def test_authorize_endpoint_success(client):
    """
    Correct secret key in header
    """
    headers = {'Authorization': Config.SECRET_KEY}
    response = client.post('/authorize', headers=headers)

    assert response.status_code == 200
    assert response.json == {'message': 'Authorization successful'}


def test_authorize_endpoint_failure(client):
    """
    Incorrect secret key in header
    """
    headers = {'Authorization': 'invalid_key'}
    response = client.post('/authorize', headers=headers)

    assert response.status_code == 401
    assert response.json == {'message': 'Authorization failed'}


def test_authorize_endpoint_no_header(client):
    """
    No header provided
    """
    response = client.post('/authorize')

    assert response.status_code == 401
    assert response.json == {'message': 'Authorization failed'}


def test_authorize_endpoint_invalid_http_method(client):
    """
    Invalid http method provided
    """
    response = client.get('/authorize')

    assert response.status_code == 405
