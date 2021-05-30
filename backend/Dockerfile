FROM python:3

COPY requirements.txt /

RUN pip3 install -r /requirements.txt

COPY . /usr/src/app

WORKDIR /usr/src/app

# CMD python manage.py runserver 0.0.0.0:8000

ENTRYPOINT ["/usr/src/app/entrypoint.sh"]