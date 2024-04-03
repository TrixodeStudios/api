FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Make port 5000 available to the world outside this container
EXPOSE 5000

# Define the command to run the app using Gunicorn, adjusted for the 'start' directory
CMD ["gunicorn", "-w", "4", "-b", "0.0.0.0:5000", "start.app:app"]
