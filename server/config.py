import redis
import os
from dotenv import load_dotenv


load_dotenv()


class ApplicationConfig:
    SECRET_KEY = os.environ['SECRET_KEY']

    SESSION_TYPE = 'redis'
    SESSION_PERMANENT = False
    SESSION_USE_SIGNER = True
    SESSION_REDIS = redis.from_url("redis://0.0.0.0:6379")
    SESSION_COOKIE_HTTPONLY = True
    REMEMBER_COOKIE_HTTPONLY = True
    SESSION_COOKIE_SAMESITE=None
#app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://postgres:123@0.0.0.0/postgres'