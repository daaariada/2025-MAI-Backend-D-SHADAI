#!/bin/sh

python manage.py migrate

python manage.py seed_db # тестовые данные

python manage.py collectstatic --noinput

exec gunicorn cathub.wsgi:application --bind 0.0.0.0:8000