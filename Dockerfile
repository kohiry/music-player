FROM python:3.11-alpine

WORKDIR /backend

COPY requirements.txt .
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
COPY . .
