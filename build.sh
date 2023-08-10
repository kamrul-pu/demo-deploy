#!/bin/bash

# Build the project
echo "Building the project...."
python3.9 -m pip install -r requirements.txt

echo "Make Migrations..."
python3.9 project/manage.py makemigrations --noinput
python3.9 project/manage.py migrate --noinput

echo "Collect Static..."
python3 project/manage.py collectstatic --oninput --clear

echo "Build Done..."
