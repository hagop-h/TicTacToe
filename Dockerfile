# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . .

# Install any needed packages specified in requirements.txt
# If your script has dependencies, create a requirements.txt and uncomment the next line
# RUN pip install --no-cache-dir -r requirements.txt

# Make sure the script is executable
RUN chmod +x TicTacToe.py

# Run TicTacToe.py when the container launches
CMD ["python", "./TicTacToe.py"]
