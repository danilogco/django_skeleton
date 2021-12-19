FROM python:3.10-slim-bullseye

RUN python -m pip install --upgrade pip

WORKDIR /django_skeleton

COPY bin/ /django_skeleton/bin
COPY requirements.txt /django_skeleton/requirements.txt

RUN python -m pip install -r requirements.txt
