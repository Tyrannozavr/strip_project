# pull the official base image
FROM python:3.10.6-alpine

# set work directory
WORKDIR /usr/src/app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install dependencies
RUN pip install --upgrade pip
COPY ./requirements.txt /usr/src/app
RUN pip install -r requirements.txt

COPY ./scrypt.sh /usr/src/app/scrypt.sh
COPY . /usr/src/app/
# copy project
COPY . /usr/src/app

EXPOSE 8000

ENTRYPOINT ["/usr/src/app/scrypt.sh"]
