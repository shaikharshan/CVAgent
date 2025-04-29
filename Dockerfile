# Use base image with Ollama support (custom)
FROM ollama/ollama:latest

# Set working directory
WORKDIR /app

# Copy app code
COPY . .

# Install Python & Streamlit dependencies
RUN apt-get update && apt-get install -y python3-pip && \
    pip install --upgrade pip && \
    pip install -r requirements.txt

# Make script executable
RUN chmod +x entrypoint.sh

# Run the script
CMD ["./entrypoint.sh"]
