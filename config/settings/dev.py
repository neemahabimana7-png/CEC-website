import os

from .base import *  # noqa: F401,F403

SETTINGS_ENV = "dev"

# This profile is explicitly for local development. A DEBUG=False value in
# a shared .env must not disable runserver's static asset handling here.
# Deployments use config.settings.prod, which always sets DEBUG=False.
DEBUG = True

SECRET_KEY = os.environ.get(
    "SECRET_KEY", "django-insecure-dev-only-key-do-not-use-in-production"
)

ALLOWED_HOSTS = [
    h.strip()
    for h in os.environ.get("ALLOWED_HOSTS", "").split(",")
    if h.strip()
] or ["localhost", "127.0.0.1", "testserver", "0.0.0.0"]
