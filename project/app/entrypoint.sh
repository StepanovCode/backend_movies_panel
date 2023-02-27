#!/bin/sh

set -e

if [ -n "$DB_HOST" ]; then
  bash ./wait-for-it.sh "$DB_HOST:$DB_PORT"
fi

python manage.py collectstatic --noinput
python manage.py migrate --noinput
python manage.py loaddata movies.json
python manage.py compilemessages -l en -l ru
python manage.py createsuperuser

gunicorn config.wsgi:application --bind 0:8000

exec "$@"
