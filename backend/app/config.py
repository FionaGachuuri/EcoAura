import os
from dotenv import load_dotenv
from datetime import timedelta

load_dotenv()


def str_to_bool(value: str) -> bool:
    return str(value).lower() in ["true", "1", "yes"]


class Config:
    SECRET_KEY = os.getenv("SECRET_KEY", "default_secret_key")
    SQLALCHEMY_DATABASE_URI = os.getenv("SQLALCHEMY_DATABASE_URL", "postgresql://user:password@localhost/dbname")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    
    JWT_SECRET_KEY = os.getenv("JWT_SECRET_KEY", "default_jwt_secret_key")
    JWT_BLACKLIST_ENABLED = True
    JWT_BLACKLIST_TOKEN_CHECKS = ["access", "refresh"]
    JWT_ACCESS_TOKEN_EXPIRES = timedelta(hours=1)
    JWT_REFRESH_TOKEN_EXPIRES = timedelta(days=1)
    JWT_TOKEN_LOCATION = ["headers"]
    

class DevelopmentConfig(Config):
    DEBUG = True


class TestingConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = os.getenv("SQLALCHEMY_DATABASE_URL", "postgresql://user:password@localhost/test_db")
    JWT_BLACKLIST_ENABLED = False


class ProductionConfig(Config):
    DEBUG = False
    if not os.getenv("SECRET_KEY") or not os.getenv("JWT_SECRET_KEY"):
        raise ValueError("SECRET_KEY and JWT_SECRET_KEY must be set in production")
