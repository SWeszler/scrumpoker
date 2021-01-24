from .settings_base import *
import environ

env = environ.Env(
    DEBUG=(bool, False),
    CORS_ALLOW_ALL_ORIGINS=(bool, False)
)
SECRET_KEY = env('SECRET_KEY')
ALLOWED_HOSTS = ["*"]
DATABASES["default"] = env.db()
CORS_ALLOWED_ORIGINS += ['http://localhost:3000']
DEBUG = True
CORS_ALLOW_ALL_ORIGINS = env("CORS_ALLOW_ALL_ORIGINS")