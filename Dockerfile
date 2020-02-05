FROM python:3.7-alpine
MAINTAINER diaa

ENV PYTHONUNBUFFERED 1

COPY ./requirements.txt /requirements.txt
RUN pip install -r /requirements.txt

RUN rm -rf /app

RUN adduser --disabled-password --gecos "" --home /app app
USER app



WORKDIR /app
COPY ./app /app

