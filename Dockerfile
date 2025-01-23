# Use the official Python 3 Alpine image as a base
FROM python:slim-bookworm

# Set the working directory in the container
WORKDIR /app
RUN mkdir /app/media

# Copy only the Python script (excluding the database file)
COPY app.py /app/
COPY requirements.txt /app/

# Install any Python dependencies here if needed
RUN pip install -r /app/requirements.txt

EXPOSE 8501

# Command to run the Python application
CMD ["streamlit", "run", "app.py"]