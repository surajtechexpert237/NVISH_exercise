from flask import Flask
from flask_marshmallow import Marshmallow
from flask_sqlalchemy import SQLAlchemy
from app.config import Config
import redis

db = SQLAlchemy()
ma = Marshmallow()
redis_client = redis.from_url(Config.REDIS_URL)


def create_app():
    print("************************")
    app = Flask(__name__)
    app.config.from_object(Config)
    db.init_app(app)
    ma.init_app(app)

    with app.app_context():
        from app.Exercises import bp
        app.register_blueprint(bp)
    return app
