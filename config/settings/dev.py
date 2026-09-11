import os

from .base import *  # noqa: F401,F403

SETTINGS_ENV = "dev"

DEBUG = os.environ.get("DEBUG", "True").lower() in ("1", "true", "yes")

SECRET_KEY = os.environ.get(
    "SECRET_KEY", "django-insecure-dev-only-key-do-not-use-in-production"
)

ALLOWED_HOSTS = [
    h.strip()
    for h in os.environ.get("ALLOWED_HOSTS", "").split(",")
    if h.strip()
] or ["localhost", "127.0.0.1", "testserver", "0.0.0.0"]