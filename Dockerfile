# Use the latest Python image as base
FROM python:latest

# Copy the books and Python scripts to the container
COPY /books /tmp/books
COPY main.py /tmp/main.py
COPY stats.py /tmp/stats.py

# Set the default command to run when the container starts
CMD ["python3", "/tmp/main.py", "/tmp/books/frankenstein.txt"]