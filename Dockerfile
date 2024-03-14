FROM python:3

RUN pip install --upgrade pip
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONBUFFERED=1

WORKDIR /celery_app

COPY . .

RUN pip3 install -r requirements.txt
