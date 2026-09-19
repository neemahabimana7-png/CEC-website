#!/bin/sh
set -eu

mkdir -p "${MEDIA_ROOT:-/data/media}" "${STATIC_ROOT:-/data/staticfiles}"

python manage.py migrate --noinput
python manage.py collectstatic --noinput

exec gunicorn config.wsgi:application \
    --bind 0.0.0.0:8000 \
    --workers "${GUNICORN_WORKERS:-1}" \
    --timeout "${GUNICORN_TIMEOUT:-120}"