# Use an official Python runtime as parent image
FROM python:3.7.4-alpine

# Set the working directory
WORKDIR /usr/src/dist

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Install required packages
RUN apk update \
  && apk add --virtual build-deps gcc python3-dev musl-dev \
  && apk add postgresql-dev \
  && pip install psycopg2

# Install pipenv
RUN pip install --upgrade pip
RUN pip install pipenv

# Copy Pipfiles to WORKDIR
COPY ./Pipfile /usr/src/dist/Pipfile
COPY ./Pipfile.lock /usr/src/dist/Pipfile.lock

# Install any needed packages specified in the Pipfile.lock
RUN pipenv install --system --ignore-pipfile --dev

# Copy entrypoint.sh
COPY ./conf/entrypoint.sh /usr/src/dist/conf/entrypoint.sh

# Copy the current directory contents into the container
COPY . /usr/src/dist

# Run entrypoint.sh
ENTRYPOINT ["/usr/src/dist/conf/entrypoint.sh"]
