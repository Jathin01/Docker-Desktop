# Use a lightweight base image
FROM registry-1.docker.io/library/python:3.9-slim

# Set the working directory inside the container
WORKDIR /home/data

# Copy Python script and text files into the container
COPY script.py .
COPY IF-1.txt .
COPY AlwaysRememberUsThisWay-1.txt .

# Create output directory
RUN mkdir -p /home/data/output

# Run the script when the container starts
CMD ["python", "script.py"]
