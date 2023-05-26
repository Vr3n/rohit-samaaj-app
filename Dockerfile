FROM python:3.10-slim-buster


# setting work dir.
WORKDIR /usr/sec/app

# env variables.
ENV PYTHONBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

# install psycopg dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# install dependencies.
RUN pip install --upgrade pip
COPY ./requirements.txt ./
RUN pip install -r requirements.txt

# COPY to code to docker container.
COPY ./ ./