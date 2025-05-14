# Use the official Apify Python base image
FROM apify/actor-python:latest

# Install Tesseract dependencies
RUN apt-get update && \
    apt-get install -y tesseract-ocr libtesseract-dev libleptonica-dev && \
    apt-get clean

# Copy all files to the actor
COPY . ./

# Install Python packages
RUN pip install --upgrade pip && pip install -r requirements.txt

# Run your Python script
CMD ["python", "main.py"]
