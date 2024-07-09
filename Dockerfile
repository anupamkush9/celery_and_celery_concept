FROM python:3

RUN pip install --upgrade pip

ENV PYTHONDONTWRITEBYTECODE 1

# for setting python output directly to the terminal with out buffering
ENV PYTHONUNBUFFERED 1

WORKDIR /celery_app

COPY . .

RUN pip3 install -r requirements.txt
