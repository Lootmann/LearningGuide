FROM python:3.10-slim-buster as builder

COPY ./requirements/docker.txt /code/
RUN pip install -U pip && pip install -r /code/docker.txt


FROM python:3.10-slim

COPY --from=builder /usr/local/lib/python3.10/site-packages /usr/local/lib/python3.10/site-packages

WORKDIR /code

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY . /code/
