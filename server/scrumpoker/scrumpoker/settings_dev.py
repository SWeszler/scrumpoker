from .settings_base import *
import environ

env = environ.Env()
SECRET_KEY = env('SECRET_KEY')
ALLOWED_HOSTS = ["*"]
DATABASES["default"] = env.db()
CORS_ORIGIN_WHITELIST += ['http://localhost:3000']
DEBUG=True