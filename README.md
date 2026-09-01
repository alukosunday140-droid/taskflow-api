TaskFlow API

A production-oriented REST API for task management, built with Flask and SQLAlchemy.

Overview

TaskFlow API provides a simple and maintainable backend for creating, reading, updating, and deleting tasks.

The project follows a modular Flask architecture with automated testing and continuous integration.

Features

- RESTful API
- Task CRUD operations
- SQLite database
- SQLAlchemy ORM
- Application factory pattern
- Flask Blueprints
- Structured JSON error responses
- Input validation
- Automated tests
- GitHub Actions CI
- Environment-based configuration
- Production WSGI entry point

API Endpoints

Method| Endpoint| Description
GET| "/api/health"| Health check
POST| "/api/tasks"| Create a task
GET| "/api/tasks"| List tasks
GET| "/api/tasks/<id>"| Get a task
PATCH| "/api/tasks/<id>"| Update a task
DELETE| "/api/tasks/<id>"| Delete a task

Example

Create a task

POST /api/tasks
Content-Type: application/json

{
  "title": "Learn Flask",
  "description": "Build a production-ready API"
}

Response

{
  "id": 1,
  "title": "Learn Flask",
  "description": "Build a production-ready API",
  "completed": false,
  "created_at": "2026-09-01T12:00:00+00:00"
}

Project Structure

taskflow-api/
├── .github/
│   └── workflows/
│       └── tests.yml
├── app/
│   ├── api/
│   │   ├── health.py
│   │   └── tasks.py
│   ├── models/
│   │   └── task.py
│   ├── config.py
│   ├── errors.py
│   ├── extensions.py
│   └── __init__.py
├── tests/
│   ├── conftest.py
│   ├── test_health.py
│   └── test_tasks.py
├── .env.example
├── .gitignore
├── pyproject.toml
├── requirements.txt
├── README.md
└── wsgi.py

Local Development

Create a virtual environment:

python -m venv .venv

Install dependencies:

pip install -r requirements.txt

Create your environment file:

cp .env.example .env

Run the application:

flask --app wsgi run

Running Tests

pytest

Production

The application exposes a WSGI entry point through "wsgi.py".

For production deployment, use a production WSGI server rather than Flask's development server.

Configuration

The following environment variables can be configured:

Variable| Purpose
"SECRET_KEY"| Application secret
"DATABASE_URL"| Database connection URL
"FLASK_ENV"| Development environment setting

Never commit real secrets or ".env" files to the repository.

License

MIT
