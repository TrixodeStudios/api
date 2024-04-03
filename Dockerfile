FROM python:3.9-alpine


ENV PYTHONFAULTHANDLER=1 \
     PYTHONUNBUFFERED=1 \
     PYTHONDONTWRITEBYTECODE=1 \
     PIP_DISABLE_PIP_VERSION_CHECK=on

RUN apk --no-cache add ffmpeg
# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install -r requirements.txt --no-cache-dir

# Make port 5000 available to the world outside this container


# Define the command to run the app using Gunicorn, adjusted for the 'start' directory
CMD ["gunicorn", "-w", "4", "-b", "0.0.0.0:5000", "start.app:app"]




