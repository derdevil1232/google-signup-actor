# Start from Apify's Python base image
FROM apify/actor-python:latest

# Install Chrome and required libraries
RUN apt-get update && apt-get install -y \
    wget gnupg unzip tesseract-ocr libtesseract-dev libleptonica-dev \
    fonts-liberation libappindicator3-1 libasound2 libatk-bridge2.0-0 libatk1.0-0 \
    libcups2 libdbus-1-3 libgdk-pixbuf2.0-0 libnspr4 libnss3 libx11-xcb1 libxcomposite1 \
    libxdamage1 libxrandr2 xdg-utils --no-install-recommends && \
    wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb && \
    apt install -y ./google-chrome-stable_current_amd64.deb && \
    rm google-chrome-stable_current_amd64.deb && \
    apt-get clean

# Install Python dependencies
COPY requirements.txt .
RUN pip install --upgrade pip && pip install -r requirements.txt

# Copy the project files into the container
COPY . ./

# Run the Python script
CMD ["python", "main.py"]
