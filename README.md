# Django 2.0 Docker Bootstrap

Bootstrapped Django application dockerized with the following features:
* [Django 2.0](https://docs.djangoproject.com/en/2.0/releases/2.0/)
* Postgres
* SMTP server
* [Gentelella Boostrap admin template](https://colorlib.com/polygon/gentelella/)

## Setup

Install [Docker](https://www.docker.com/) and docker-compose.

`sudo apt-get install docker.io docker-compose`

Run `setup.sh` to create an email account for the SMTP server

Run `docker-compose up --build` to start the containers.

To create migrations, run the command

`docker-compose exec web python portal/manage.py makemigrations`

To apply the migrations, run the command

`docker-compose exec web python portal/manage.py migrate`
