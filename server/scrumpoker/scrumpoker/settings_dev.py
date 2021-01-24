from .settings_base import *

ALLOWED_HOSTS = ["*"]
DATABASES["default"] = env.db()
CORS_ORIGIN_WHITELIST += ['http://localhost:3000']