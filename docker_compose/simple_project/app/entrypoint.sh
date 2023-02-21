#!/bin/bash

echo "Waiting for postgres..."
while ! nc -z $DB_HOST $DB_PORT; do
  sleep 0.1
done
echo "PostgreSQL started"

echo "Collect static files"
python3 manage.py collectstatic --no-input --clear

echo "Apply database migrations"
python3 manage.py migrate --noinput


if [ $# == 0 ]; then
  gunicorn config.wsgi:application --bind 0.0.0.0:8000
else
  exec "$@"
fi