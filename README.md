# SCI Weather
## Requirements
* Django 1.10
* gunicorn 19.6.0

## CDN
* DataTable
* jQuery

## Deploying with Docker
* `docker-compose build --force-rm`
* `docker run -it --rm -v $(pwd)/db:/app/db sciweather_web bash ./db_config.sh` to create migrations and migrate.
This is container level, but the database file will be mounted from host, so it is persistance.
* `docker run -it --rm -v $(pwd)/db:/app/db sciweather_web python manage.py createsuperuser` if necessary.
* `docker-compose up`. Application should listen at port 80 on machine.

## Running with Development Server
* `chown <user>:<user> db/db.sqlite3` to allow development server to read/write the database file. File will be root:root if
running the docker locally before.
* `cd web/`
* `ln -s ../db db` to simulate the db folder and also use the existing database. This have to be removed if we are going
to deploy with Docker.
* `python manage.py runserver` to start the development server.
