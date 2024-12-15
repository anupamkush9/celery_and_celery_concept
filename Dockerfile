FROM python:3.8

RUN pip install --upgrade pip
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /src

COPY . .

RUN pip3 install -r requirements.txt
