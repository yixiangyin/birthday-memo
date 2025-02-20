# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose port 5000 for Flask
EXPOSE 5000

# Set environment variable to indicate Flask should run in development mode
ENV FLASK_ENV=development

# Run the Flask app when the container starts
CMD ["flask", "run", "--host=0.0.0.0"]
