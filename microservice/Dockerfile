# Use an official Python runtime as a parent image
FROM python:3.8-slim

# Set the working directory to /app
WORKDIR /app

# Copy the 'src' directory into the container at /app/src
COPY ./src /app/src

# Copy the 'data' directory into the container at /app/data
COPY ./data /app/data

COPY ./data /app/new_folder

# Set the working directory to /app/src
WORKDIR /app/src

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Set the working directory back to /app
WORKDIR /app

# Make port 5000 available to the world outside this container
EXPOSE 5000

# Define environment variable
ENV NAME World

# Run app.py when the container launches
CMD ["python", "src/app.py"]
