TaskFlow API

A clean, production-oriented REST API for managing tasks, built with Flask and SQLAlchemy.

Features

- Application factory architecture
- Modular Flask Blueprints
- RESTful task endpoints
- SQLite database for local development
- SQLAlchemy ORM
- Environment-based configuration
- Structured JSON error responses
- Automated test suite
- GitHub Actions continuous integration
- Production WSGI entry point
- Health-check endpoint

Project Structure

app/
├── api/
├── models/
├── config.py
├── errors.py
├── extensions.py
└── __init__.py

tests/
├── conftest.py
├── test_health.py
└── test_tasks.py

Local Setup

Create a virtual environment:

python -m venv .venv

Activate it and install dependencies:

pip install -r requirements.txt

Copy the environment template:

cp .env.example .env

Run the application:

flask --app wsgi run

The API will be available at:

http://127.0.0.1:5000

Testing

Run:

pytest

Health Check

GET /api/health

License

MIT
