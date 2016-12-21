# SCI Weather
## Requirements
* Django 1.10
* gunicorn 19.6.0

## CDN
* DataTable
* jQuery

## Setup
* `docker-compose build --force-rm`
* `docker run -it --rm -v $(pwd)/db:/app/db sciweather_web bash ./db_config.sh`
* `docker run -it --rm -v $(pwd)/db:/app/db sciweather_web python manage.py createsuperuser` if necessary.
* `docker-compose up`
