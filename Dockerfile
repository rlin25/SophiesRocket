# Use an official Python runtime as a base image
FROM python:3.11-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the current project files into the container
COPY . /app

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Set the environment variable to avoid Python buffering logs
ENV PYTHONUNBUFFERED=1

# Command to run the bot
CMD ["python", "./src/bot.py"]
