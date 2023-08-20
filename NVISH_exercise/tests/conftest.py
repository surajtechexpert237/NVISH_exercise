import pytest

from app import create_app, db


@pytest.fixture
def client():
    """
    Create client for using pytest methods
    :return: client
    """
    app = create_app()
    app.config['TESTING'] = True

    with app.test_client() as client:
        yield client


@pytest.fixture
def app():
    """
    Create and drop database tables after usage
    :return: app
    """
    app = create_app()
    app.config['TESTING'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'

    with app.app_context():
        db.create_all()
        yield app
        db.session.remove()
        db.drop_all()
