# SCI Weather
## Requirements
* Django 1.10
* gunicorn 19.6.0

## CDN
* DataTable
* jQuery

## Deploying with Docker
```bash
DJANGO_DEBUG="False"
DJANGO_SECRET_KEY="some_key"
```
* `docker-compose build --force-rm`
* `docker run -it --rm -v $(pwd)/db:/app/db sciweather_web bash ./db_config.sh` to create migrations and migrate.
This is container level, but the database file will be mounted from host, so it is persistance.
* `docker run -it --rm -v $(pwd)/db:/app/db sciweather_web python manage.py createsuperuser` if necessary.
* `docker-compose up`. Application should listen at port 80 on machine.
* ` docker-compose up -d` to run the server in background. This has been test on digital ocean for 2 months, no problem found so far.

## Running with Development Server
* `chown <user>:<user> db/db.sqlite3` to allow development server to read/write the database file. File will be root:root if
running the docker locally before.
* `cd web/`
* `ln -s ../db db` to simulate the db folder and also use the existing database. This have to be removed if we are going
to deploy with Docker.
* `python manage.py runserver` to start the development server.

## To use the docker structure in another project
There are many changes required to make a custom Django project. How ever the minimum changes are the following:
* `os.path.join(BASE_DIR, "myapp", "static")` in sci_weather/web/weather/settings.py
* `CMD /usr/local/bin/gunicorn weather.wsgi:application -b :8000` in sci_weather/web/Dockerfile
