FROM python:3.8-slim-buster
RUN apt-get update

COPY . /app
WORKDIR /app
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

CMD python __main__.py