from werkzeug.security import generate_password_hash

from app import db


class User(db.Model):
    """
    Create user table
    """
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    first_name = db.Column(db.String(25), nullable=False)
    last_name = db.Column(db.String(25), nullable=False)
    username = db.Column(db.String(25), unique=True, nullable=False)
    password = db.Column(db.String(128), nullable=False)
    email = db.Column(db.String(128), unique=True, nullable=False)

    def set_password(self, password):
        """
        Generates password hash
        :param password: password received from request
        :return: hashed password
        """
        self.password = generate_password_hash(password)
