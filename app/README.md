# LLM Translation API using FastAPI

A simple Python application that uses the OpenAI GPT-4 API to translate English text into French and serves it through a REST API built with FastAPI. This project demonstrates how to build, test, and deploy a modular and extendable LLM-powered API.

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Project Structure](#project-structure)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Configuration](#configuration)
- [Running the Application](#running-the-application)
- [API Endpoints](#api-endpoints)
- [Testing](#testing)
- [Contributing](#contributing)
- [License](#license)
- [Credits](#credits)

## Overview

This project builds a REST API endpoint for a language translation application that leverages an LLM (using OpenAI’s GPT-4 API) to translate input English text into French. The API is built with [FastAPI](https://fastapi.tiangolo.com/), which provides automatic interactive documentation via OpenAPI. The project is designed for ease of development, extendability, and follows best practices like virtual environment management and dependency tracking.

## Features

- **REST API Endpoint:** A POST endpoint (`/translate/`) that accepts text input and returns the French translation.
- **Environment Configuration:** Uses a `.env` file for managing sensitive configuration (e.g. the OpenAI API key).
- **Modular Codebase:** Organized into modules for configuration, business logic (translation), and API endpoint definitions.
- **Automatic Documentation:** Interactive API docs available at `/docs` once the server is running.
- **Testing:** Comprehensive test coverage using pytest and FastAPI’s TestClient.
- **Extensible Structure:** Easily extendable to add more endpoints or business logic.

## Project Structure

```plaintext
llm-translate-api/
├── app/
│   ├── __init__.py
│   ├── config.py         # Loads environment variables
│   ├── main.py           # FastAPI app and endpoint definitions
│   └── translator.py     # Business logic: translation function using OpenAI API
├── tests/
│   └── test_translator.py  # Pytest test cases for the API endpoints
├── .env                  # Environment file containing sensitive keys
├── requirements.txt      # List of project dependencies
└── README.md             # Project documentation
```

## Prerequisites

- **Python 3.7+** – Install via [Homebrew](https://brew.sh) (e.g., `brew install python3`) or from [python.org](https://www.python.org/).
- **Visual Studio Code** – Recommended for development.
- **VS Code Python Extension** – Provides linting, debugging, IntelliSense, and virtual environment support.
- **Git** – For version control and repository management.

## Installation

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/yourusername/llm-translate-api.git
   cd llm-translate-api
   ```

2. **Create and Activate a Virtual Environment:**

   ```
   python3 -m venv .venv
   source .venv/bin/activate
   ```

3. **Install Dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

## Configuration

1. **Create a `.env` File:**

   In the project root, create a file named `.env` and add your OpenAI API key:

   ```dotenv
   OPENAI_API_KEY=your_openai_api_key_here
   ```

2. **Configure Environment Variables:**

   The `app/config.py` file automatically loads variables from the `.env` file using the `python-dotenv` package.

## Running the Application

1. **Run the Server:**

   With the virtual environment activated, start the API server using Uvicorn:

   ```bash
   uvicorn app.main:app --reload
   ```

   - `app.main:app` tells Uvicorn to look in the `app/main.py` file for the FastAPI instance named `app`.
   - The `--reload` flag enables auto-reloading during development.

2. **Access Interactive Documentation:**

   Open your browser and navigate to [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs) to view and test the API endpoints interactively.

## API Endpoints

- **POST `/translate/`**

  - **Description:** Accepts a JSON payload with the key `input_str` and returns the French translation.
  - **Request Body Example:**

    ```json
    {
      "input_str": "Hello, world!"
    }
    ```

  - **Response Example:**

    ```json
    {
      "translated_text": "French: Hello, world!"
    }
    ```

## Testing

This project uses `pytest` and FastAPI's `TestClient` for testing.

1. **Run Tests:**

   ```bash
   pytest tests/test_translator.py
   ```

2. **Test Coverage:**

   The tests cover:
   - Standard translation requests
   - Empty input strings
   - Missing or invalid input (triggering validation errors)
   - Exception handling (ensuring a 500 error is returned)
   - Special characters and long input texts

## Contributing

Contributions are welcome! To contribute:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature/your-feature`).
3. Make your changes and commit them (`git commit -m 'Add some feature'`).
4. Push to your branch (`git push origin feature/your-feature`).
5. Open a pull request.

Please follow the existing code style and include tests for any new features.


## Credits

- Built with [FastAPI](https://fastapi.tiangolo.com/) and [Uvicorn](https://www.uvicorn.org/).
- Inspired by the [DataCamp tutorial](https://www.datacamp.com/tutorial/serving-an-llm-application-as-an-api-endpoint-using-fastapi-in-python).