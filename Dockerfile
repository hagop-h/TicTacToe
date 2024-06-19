FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . .


# RUN pip install --no-cache-dir -r requirements.txt

RUN chmod +x TicTacToe.py

# Run TicTacToe.py when the container launches
CMD ["python", "./TicTacToe.py"]
