FROM python:2.7
ENV DJANGO_DEBUG True
ENV DJANGO_SECRET_KEY 0x0%q8_%3%%5)sajk8n*5&z9+k2f0r7k($gm_5==n7!g@dc#55
RUN mkdir /usr/src/sci_weather/
WORKDIR /usr/src/sci_weather/
ADD requirements.txt /usr/src/sci_weather/
RUN pip install -r requirements.txt
ADD . /usr/src/sci_weather/
COPY ./myapp/static/ /usr/src/sci_weather/static
RUN python manage.py collectstatic --noinput
RUN chmod -R 755 static_files/
RUN python manage.py makemigrations
RUN python manage.py migrate
CMD /usr/local/bin/gunicorn weather.wsgi:application -b :8000
