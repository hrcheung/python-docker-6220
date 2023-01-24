# syntax=docker/dockerfile:1

FROM python:3.8-slim-buster

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt \
&& pip3 install pandas

COPY . .

CMD [ "python3", "app/main.py"]