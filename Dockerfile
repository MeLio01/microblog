FROM python:3.8-slim-buster

WORKDIR /microblog

COPY . /microblog

RUN pip install poetry
# RUN poetry install
RUN chmod +x start_app.sh