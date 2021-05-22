FROM python:3.9
ENV PYTHONUNBUFFERED 1
WORKDIR /tests
COPY requirements.txt /tests/requirements.txt
RUN pip install -r requirements.txt
COPY . /tests

CMD python manage.py runserver 0.0.0.0:8000