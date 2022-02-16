FROM python:3.8

ENV PYTHONUNBUFFERED 1

RUN mkdir /private_notes

WORKDIR /private_notes

ADD requirements.txt /private_notes/
RUN pip install -r requirements.txt


