#!/bin/bash

# Start Ollama server in background
ollama serve &

# Wait a bit to ensure it's up
sleep 10

# Pull Mistral model
ollama pull mistral

# Run Streamlit app
streamlit run try.py --server.port=8080 --server.address=0.0.0.0
