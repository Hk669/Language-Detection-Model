# Language Detection Model

This repository contains code for a language detection model based on machine learning. The model is built using scikit-learn and deployed as a FastAPI web application using Docker.

## Features

- Predicts the language of a given text using a pre-trained language detection model.
- Supports multiple languages including Arabic, Danish, Dutch, English, French, German, Greek, Hindi, Italian, Kannada, Malayalam, Portuguese, Russian, Spanish, Swedish, Tamil, and Turkish.
- Provides a user-friendly API interface for making predictions.

## Setup and Installation

To run the language detection model locally, follow these steps:

1. Clone this repository: `git clone https://github.com/your-username/language-detection-model.git`
2. Install Docker on your machine: https://docs.docker.com/get-docker/
3. Build the Docker image: `docker build -t language-detection-app .`
4. Run the Docker container: `docker run -p 80:80 language-detection-app`
5. Access the API at `http://localhost:80` or `http://127.0.0.1:80`

## API Usage

Make a POST request to the `/predict` endpoint with the following JSON payload:

```json
{
  "text": "Enter your text here"
}
