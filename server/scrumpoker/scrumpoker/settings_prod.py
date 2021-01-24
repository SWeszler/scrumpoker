import io
import os

import environ
import google.auth
from google.cloud import secretmanager as sm

# Import the original settings from each template
from .settings_base import *

try:
    from .local import *
except ImportError:
    pass


# Pull django-environ settings file, stored in Secret Manager
SETTINGS_NAME = "application_settings"

_, project = google.auth.default()
client = sm.SecretManagerServiceClient()
name = f"projects/{project}/secrets/{SETTINGS_NAME}/versions/latest"
payload = client.access_secret_version(name=name).payload.data.decode("UTF-8")

env = environ.Env()
env.read_env(io.StringIO(payload))

# Setting this value from django-environ
print('secrets from env:', env("SECRET_KEY"), env("DEBUG"))
SECRET_KEY = env("SECRET_KEY")

# Allow all hosts to access Django site
for host in env("ALLOWED_HOSTS").split(','):
    ALLOWED_HOSTS += [host]

# Allow CORS
for host in env("CORS_ORIGIN_WHITELIST").split(','):
    CORS_ORIGIN_WHITELIST += [host]

# Default false. True allows default landing pages to be visible
DEBUG = env("DEBUG")

# Set this value from django-environ
DATABASES["default"] = env.db()

INSTALLED_APPS += ["storages"] # for django-storages
if "scrumpoker" not in INSTALLED_APPS:
     INSTALLED_APPS += ["scrumpoker"] # for custom data migration

# Define static storage via django-storages[google]
GS_BUCKET_NAME = env("GS_BUCKET_NAME")
STATICFILES_DIRS = []
DEFAULT_FILE_STORAGE = "storages.backends.gcloud.GoogleCloudStorage"
STATICFILES_STORAGE = "storages.backends.gcloud.GoogleCloudStorage"
GS_DEFAULT_ACL = "publicRead"