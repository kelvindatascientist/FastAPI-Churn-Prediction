# Use an official Python runtime as a parent image
FROM python:3.10-slim

# Create a working directory
WORKDIR /usr/src/app

# Copy the requirements file to the working directory
COPY requirements.txt .

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application's source code
COPY . .

# Expose port 80 (or 8000 commonly used by FastAPI/uvicorn)
EXPOSE 80

# Command to run the application with uvicorn
# We use host=0.0.0.0 so that it is accessible both inside Docker and from the host.
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]