# AggieDine — Microservice Template

Reusable FastAPI microservice template for the AggieDine backend. Clone this to bootstrap any new service (scraperAPI, recommendationService, feedService, etc.).

## Prerequisites

- Python 3.11+
- Docker & Docker Compose

## Quick Start

```bash
# 1. Copy the .env file and fill in values
cp .env.example .env

# 2. Start all services (app + PostgreSQL + Redis)
docker-compose up --build

# 3. Verify
curl http://localhost:8000/health
# Open http://localhost:8000/docs for Swagger UI
```

## Local Development (without Docker)

```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
# Set DATABASE_URL to a local PostgreSQL instance in .env
uvicorn app.main:app --reload
```

## Running Tests

```bash
pip install aiosqlite  # needed for test SQLite backend
pytest
```

## Database Migrations

```bash
# Generate a new migration after changing models
alembic revision --autogenerate -m "describe change"

# Apply migrations
alembic upgrade head
```

## Project Structure

```
app/
├── main.py            # FastAPI app factory, CORS, lifespan
├── config.py          # Pydantic Settings (env-based)
├── database.py        # Async SQLAlchemy engine + session
├── dependencies.py    # Reusable FastAPI dependencies
├── middleware/
│   └── auth.py        # AWS Cognito JWT verification
├── models/            # SQLAlchemy ORM models
├── schemas/           # Pydantic request/response schemas
├── routers/           # FastAPI route handlers
└── services/          # Business logic layer
```

## How to Clone for a New Service

1. Copy this directory → `<yourServiceName>/`
2. Update `SERVICE_NAME` in `.env`
3. Replace `example` models/schemas/routers/services with your domain
4. Add service-specific dependencies to `requirements.txt`
5. Run `docker-compose up` to start developing

## Environment Variables

| Variable | Description | Default |
|---|---|---|
| `SERVICE_NAME` | Name of this service | `template-service` |
| `PORT` | HTTP port | `8000` |
| `ENVIRONMENT` | `development` / `production` | `development` |
| `LOG_LEVEL` | Logging level | `info` |
| `DATABASE_URL` | PostgreSQL async connection string | see `.env.example` |
| `REDIS_URL` | Redis connection string | see `.env.example` |
| `AWS_COGNITO_REGION` | Cognito region | `us-east-1` |
| `AWS_COGNITO_USER_POOL_ID` | Cognito user pool ID | — |
| `AWS_COGNITO_APP_CLIENT_ID` | Cognito app client ID | — |
