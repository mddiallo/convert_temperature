FROM python:3.9

# Set the working directory
WORKDIR /app

# Copy the requirements file
COPY requirements.txt .

# Install the dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application code
COPY . .

# Expose the port for the application
EXPOSE 5000

# Run the command to start the application
CMD ["flask", "run", "--host=0.0.0.0"]
