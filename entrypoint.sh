#!/bin/sh
python manage.py makemigrations
python manage.py migrate --no-input
gunicorn --bind :8000 recallcontrol.wsgi