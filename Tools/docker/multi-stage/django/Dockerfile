# FROM python:3.10.4-slim as builder
FROM python:3.10.4-slim as builder

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /app

COPY ./requirements.txt /app/

RUN pip install -U pip \
  && pip install -r /app/requirements.txt


# deploy
FROM python:3.10-slim-buster

RUN apt-get update \
  && apt-get clean \
  && rm -rf /var/lib/apt/lists/*

WORKDIR /app/

COPY --from=builder /usr/local/lib/python3.10/site-packages /usr/local/lib/python3.10/site-packages
COPY . /app/
