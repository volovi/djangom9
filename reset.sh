#!/usr/bin/env sh
# exit on error
set -o errexit

./manage.py migrate m9 zero
./manage.py migrate m9
./manage.py seed
