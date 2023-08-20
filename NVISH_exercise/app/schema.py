from marshmallow import Schema, fields, validates, ValidationError

from app.models import User


class UserSchema(Schema):
    """
    Schema that serializes and validates all the fields
    """
    id = fields.Integer(dump_only=True)
    first_name = fields.String(required=True)
    last_name = fields.String(required=True)
    username = fields.String(required=True)
    password = fields.String(required=True, load_only=True)
    email = fields.Email(required=True)

    @validates('first_name')
    def validate_first_name(self, first_name):
        if not first_name:
            raise ValidationError('First name field cannot be empty')
        if not first_name.isalpha():
            raise ValidationError('First name must contain only letters')

    @validates('last_name')
    def validate_last_name(self, last_name):
        if not last_name:
            raise ValidationError('Last name field cannot be empty')
        if not last_name.isalpha():
            raise ValidationError('Last name must contain only letters')

    @validates('username')
    def validate_username(self, username):
        if not username:
            raise ValidationError('Username field cannot be empty')
        if User.query.filter_by(username=username).first():
            raise ValidationError('Username already exists!')
        if len(username) < 6 or len(username) > 20:
            raise ValidationError('Username must be between 6 and 20 characters')
        if not username.isalnum():
            raise ValidationError('Username must contain only alphanumeric characters')

    @validates('password')
    def validate_password(self, password):
        if not password:
            raise ValidationError('Password field cannot be empty')
        if len(password) < 6 or len(password) > 20:
            raise ValidationError('Password must be between 6 and 20 characters')

    @validates('email')
    def validate_email(self, email):
        if not email:
            raise ValidationError('Email field cannot be empty')
        if User.query.filter_by(email=email).first():
            raise ValidationError('Email already exists!')


class UserResponseSchema(UserSchema):
    """
    Schema used to get fields for response
    """
    class Meta:
        fields = ('id', 'first_name', 'last_name', 'username', 'email')
