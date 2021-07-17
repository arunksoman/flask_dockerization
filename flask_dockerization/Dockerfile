FROM python:3.8-alpine
LABEL maintainer="Arun K Soman <arunksoman5678@gmail.com>"
WORKDIR /flask_docker_post1
RUN apk --update --no-cache add python3-dev libffi-dev gcc musl-dev make libevent-dev build-base
COPY requirements.txt requirements.txt
RUN python -m pip install --upgrade pip setuptools
RUN pip install -r requirements.txt
EXPOSE 8080
COPY . .