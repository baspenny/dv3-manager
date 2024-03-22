# Use the official Python image that comes with Debian and Python 3.12
FROM python:3.12-slim

# Set the working directory in the container
WORKDIR /app

# Copy the Pipfile and Pipfile.lock into the container
COPY Pipfile Pipfile.lock ./

# Install pipenv and project dependencies
RUN pip install --upgrade pip && \
    pip install pipenv && \
    pipenv install --system --deploy

# Copy the rest of your application's code
COPY . .
EXPOSE 8080
# The command to run the application using uvicorn
# Adjust the host to '0.0.0.0' to listen on all interfaces inside the container
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8080"]