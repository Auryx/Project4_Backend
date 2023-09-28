#!/usr/bin/env bash

# exit on cmd fail
set -o errexit

# install dependencies
pip install -r dependencies.txt

# run migrations
python manage.py migrate

