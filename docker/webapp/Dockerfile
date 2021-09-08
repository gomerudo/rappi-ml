FROM python:3.9.7-slim-buster

# flask port
EXPOSE 5001

# We will store our source code here
ENV APP_DIR /home/rappiml
ENV FLASK_APP=rappiapp

RUN apt-get update -y && apt-get install -y git

RUN mkdir ${APP_DIR}
COPY python/webapp ${APP_DIR}/webapp

WORKDIR ${APP_DIR}/webapp

RUN python3.9 -m pip install --upgrade pip
RUN python3.9 -m pip install pandas mlflow pymysql
RUN python3.9 -m pip install -e .
