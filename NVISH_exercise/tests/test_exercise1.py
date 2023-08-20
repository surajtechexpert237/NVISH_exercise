def test_ping_api(client):
    """
    Proper data is provided
    """
    response = client.get('/ping')

    assert response.status_code == 200

    result = {
        'id': 123,
        'username': 'john_doe',
        'email': 'john@example.com',
        'full_name': 'John Doe',
        'age': 30,
        'country': 'USA'
    }

    assert response.json == result


def test_ping_endpoint_response_structure(client):
    """
    Checks response structure
    """
    response = client.get('/ping')
    response_data = response.json
    assert 'id' in response_data
    assert 'username' in response_data
    assert 'email' in response_data
    assert 'full_name' in response_data
    assert 'age' in response_data
    assert 'country' in response_data


def test_ping_endpoint_invalid_http_method(client):
    """
    Invalid http method provided
    """
    response = client.post('/ping')
    assert response.status_code == 405
