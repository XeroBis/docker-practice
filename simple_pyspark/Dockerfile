FROM openjdk:8

RUN apt-get update && apt-get install -y python3-pip

WORKDIR /app

COPY . /app

RUN pip install -r requirements.txt

