# Use the official Python image from the Docker Hub
FROM python:3.10

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt .

# Install the dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the entire project into the container
COPY . .

# Expose the port the app runs on
EXPOSE 8000

# Set the environment variable to specify the settings module
ENV DJANGO_SETTINGS_MODULE=learning_log.settings

# Run the Django application using Gunicorn
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "learning_log.wsgi:application"]
