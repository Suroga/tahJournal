# Tah-journal

Расчёт данных для заполнения тахеометрического журнала

[![Built with Cookiecutter Django](https://img.shields.io/badge/built%20with-Cookiecutter%20Django-ff69b4.svg?logo=cookiecutter)](https://github.com/cookiecutter/cookiecutter-django/)
[![Black code style](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/ambv/black)

## Settings


## Basic Commands

make migrations:

`docker-compose -f local.yml run --rm django python manage.py makemigrations`

apply migrations:

`docker-compose -f local.yml run --rm django python manage.py migrate`

Create super-user:

`docker-compose -f local.yml run --rm django python manage.py createsuperuser`

### Live reloading and Sass CSS compilation

Moved to [Live reloading and SASS compilation](https://cookiecutter-django.readthedocs.io/en/latest/developing-locally.html#sass-compilation-live-reloading).

## Deployment

The following details how to deploy this application.

### Docker

See detailed [cookiecutter-django Docker documentation](http://cookiecutter-django.readthedocs.io/en/latest/deployment-with-docker.html).
