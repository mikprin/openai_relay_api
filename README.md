Here’s a detailed `README.md` file for your FastAPI and OpenAI service project.

---

# FastAPI OpenAI Service

This project is a FastAPI-based web service that interfaces with the OpenAI API to create chat completions. It provides a simple endpoint to send messages to OpenAI's models and retrieve responses. The service is secured with an authorization token and is designed to be containerized using Docker and Docker Compose.

## Features

- FastAPI framework for building high-performance web APIs.
- Asynchronous interaction with OpenAI's API to create chat completions.
- Secured with an Authorization token.
- Easily deployable using Docker and Docker Compose.
- Environment variable management using `.env` files.

## Prerequisites

To run this project, you’ll need:

- **Python 3.10+**
- **Docker** and **Docker Compose**
- An **OpenAI API Key**

## Setup

### 1. Clone the repository

```bash
git clone https://github.com/your-username/fastapi-openai-service.git
cd fastapi-openai-service
```

### 2. Create a `.env` file

Create a `.env` file in the root of your project directory to store environment variables securely. The `.env` file should look like this:

```bash
OPENAI_API_KEY=your_openai_api_key_here
AUTH_TOKEN=your_secret_auth_token_here
PORT=8000
```

- **OPENAI_API_KEY**: Your OpenAI API key.
- **AUTH_TOKEN**: A token for securing the FastAPI endpoint.
- **PORT**: The port on which the FastAPI service will run (default is 8000).

### 3. Install dependencies (for local development)

If you want to run the service locally, you can install the required dependencies:

```bash
pip install -r requirements.txt
```

### 4. Run the FastAPI Service

You can run the service locally using Uvicorn:

```bash
uvicorn main:app --host 0.0.0.0 --port 8000
```

Now the API will be available at `http://localhost:8000`.

## API Endpoint

### `POST /api/open_ai_request`

This endpoint allows you to send a list of messages to OpenAI and get a chat completion response.

#### Request Body:

- `model_name`: The name of the OpenAI model to use (e.g., `gpt-4`, `gpt-3.5-turbo`).
- `messages`: A list of message objects. Each message object should contain a `role` (e.g., `system`, `user`, `assistant`) and `content`.

#### Example Request:

```json
{
  "model_name": "gpt-4",
  "messages": [
    {"role": "system", "content": "You are a helpful assistant."},
    {"role": "user", "content": "Tell me a joke."}
  ]
}
```

#### Example Response:

```json
{
  "response": "Why don't scientists trust atoms? Because they make up everything!"
}
```

### Authorization

The API expects an `Authorization` header containing the token specified in the `.env` file. If the token is incorrect or missing, a `403 Forbidden` error will be returned.

#### Example Header:

```bash
Authorization: your_secret_auth_token_here
```

## Docker

The project is fully containerized using Docker. To build and run the service in a Docker container, follow these steps:

### 1. Build and Run with Docker Compose

Ensure Docker and Docker Compose are installed, then run:

```bash
docker-compose up --build
```

This will:

- Build the Docker image.
- Start the FastAPI service on `http://localhost:8000`.

### 2. Stopping the Service

To stop the service, run:

```bash
docker-compose down
```

## Development

### Install Dependencies

If you are developing locally, you can install the project dependencies using:

```bash
pip install -r requirements.txt
```

### Running Tests

To add tests, you can use Python's `pytest` framework. Make sure you install `pytest`:

```bash
pip install pytest
```

You can then run the tests using:

```bash
pytest
```

## Project Structure

```bash
.
├── Dockerfile              # Docker configuration
├── docker-compose.yml      # Docker Compose configuration
├── main.py                 # Main FastAPI application code
├── requirements.txt        # Python dependencies
└── .env                    # Environment variables (not in version control)
```

## Technologies Used

- **[FastAPI](https://fastapi.tiangolo.com/)**: A modern, fast (high-performance) web framework for building APIs with Python 3.6+.
- **[OpenAI API](https://beta.openai.com/docs/)**: Used for generating chat completions via GPT-3/GPT-4 models.
- **[Docker](https://www.docker.com/)**: Containerization platform to simplify deployment.
- **[Docker Compose](https://docs.docker.com/compose/)**: A tool for defining and running multi-container Docker applications.
- **[Python dotenv](https://pypi.org/project/python-dotenv/)**: For loading environment variables from a `.env` file.

## Troubleshooting

### Common Errors

- **403 Unauthorized**: Ensure you are passing the correct authorization token in the headers.
- **OpenAI API errors**: Make sure your API key is valid and the OpenAI service is available.

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.

## Contributing

Feel free to open issues or submit pull requests for any improvements or bugs found.

---

This README gives a comprehensive guide to set up, use, and develop the FastAPI OpenAI service, whether locally or within a Docker environment.# openai_relay_api
