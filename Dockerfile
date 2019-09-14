# Use an official Python runtime as parent image
FROM python:3.7.4-slim

# Set the working directory
WORKDIR /dist

# Copy the current directory contents into the container
COPY . /dist

# Install pipenv
RUN pip install pipenv

# Install any needed packages specified in the Pipfile.lock
RUN pipenv install --system --ignore-pipfile --deploy

# Make port 8000 available to the world outside this container
EXPOSE 8000

# Define environment variable
ENV NAME World

# Run Django migrations
CMD ["python", "manage.py", "migrate"]

# Run Django server
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
