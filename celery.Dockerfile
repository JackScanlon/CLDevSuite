FROM python:3.10.2-slim-bullseye

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

RUN apt-get update -y -q && \
    apt-get upgrade -y -q

RUN apt-get install -y -q netcat \
                    gcc \
                    postgresql-contrib \
                    libpq-dev \
                    openssl \
                    python3-dev \
                    libssl-dev \
                    libsasl2-dev \
                    libldap2-dev \
                    curl \
                    gettext

RUN mkdir /app

RUN pip install --upgrade pip
COPY requirements.txt /app/requirements.txt
RUN pip install -r /app/requirements.txt