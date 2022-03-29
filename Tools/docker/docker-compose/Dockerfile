# builder
FROM python:3.10-slim as builder

RUN apt-get update \
  && rm -rf ~/.cache \
  && apt-get clean all

RUN mkdir /code
WORKDIR /code

# COPY ./requirements.txt /code/

RUN pip install -U pip 

COPY . /code/

FROM python:3.10-slim

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

# deploy
COPY --from=builder /usr/local/lib/python3.10/site-packages /usr/local/lib/python3.10/site-packages

WORKDIR /code
COPY . /code/

CMD ["python3.10", "/code/main.py"]
