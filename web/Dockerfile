FROM python:2.7
ARG debug
ARG secret_key
# We needs these environment variable since we are using the
# the manage.py to setup the migration.
ENV DJANGO_DEBUG "$debug"
ENV DJANGO_SECRET_KEY "$secret_key"
RUN mkdir /app/
WORKDIR /app/
ADD requirements.txt /app/
RUN pip install -r requirements.txt
ADD . /app/
# Collect static files.
RUN python manage.py collectstatic --noinput
RUN chmod -R 755 static/
CMD /usr/local/bin/gunicorn weather.wsgi:application -b :8000
