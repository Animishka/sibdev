FROM python:3.9

MAINTAINER Mikhail Mikhailov <povsedn@yandex.ru>

RUN mkdir -p /deals_app
WORKDIR /deals_app

COPY . /deals_app

RUN pip install --no-cache-dir -r requirements.txt