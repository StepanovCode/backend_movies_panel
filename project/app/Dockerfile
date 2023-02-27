# pull official base image
FROM python:3.10.0-alpine

# set work directory
WORKDIR /app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV DJANGO_SETTINGS_MODULE 'config.settings'

RUN apk update && apk add bash gettext
RUN pip install --upgrade pip

COPY requirements.txt ./

RUN pip install -r requirements.txt

COPY . .

EXPOSE 8000/tcp

RUN ["chmod", "+x", "./entrypoint.sh"]
RUN ["chmod", "+x", "./wait-for-it.sh"]

ENTRYPOINT ["sh", "./entrypoint.sh"]
