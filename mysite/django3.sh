#!/bin/bash
echo "python3 makemigrations"
python3 mysite/manage.py makemigrations
sleep 5s
echo "python3 migrate"
python3 mysite/manage.py migrate
sleep 10s
echo "python3 runserver 0.0.0.0:8000"
python3 mysite/manage.py runserver 0.0.0.0:8000