# 🏋️ Fitness Tracker API

A RESTful backend API for a fitness tracking application built with **FastAPI**, **PostgreSQL**, and **SQLAlchemy 2.0**.

The project demonstrates modern backend development practices using asynchronous Python, database migrations, authentication, automated testing, containerization, and continuous integration.

---

# 🚀 Tech Stack

## Backend
- Python 3.14
- FastAPI
- SQLAlchemy 2.0
- Pydantic v2
- AsyncPG

## Database
- PostgreSQL
- Alembic

## Authentication
- JWT Authentication
- Password hashing with bcrypt

## Testing
- Pytest
- Async test environment
- Service layer testing

## DevOps
- Docker
- Docker Compose
- GitHub Actions (CI)

---

# 📂 Project Structure

```text
FitnessTracker/
│
├── .github/
│   └── workflows/
│       └── ci.yml                # GitHub Actions CI pipeline
│
├── app/
│   ├── __init__.py
│   ├── main.py                   # FastAPI application entry point
│   ├── config.py                 # Environment configuration
│   ├── database.py               # Database connection and session management
│   ├── dependencies.py           # Shared FastAPI dependencies
│   │
│   ├── models/                   # SQLAlchemy database models
│   │
│   ├── schemas/                  # Pydantic request and response schemas
│   │
│   ├── routers/                  # API endpoints
│   │
│   ├── services/                 # Business logic layer
│   │
│   └── utils/                    # JWT and security utilities
│
├── tests/
│   ├── conftest.py               # Pytest fixtures and test database setup
│   ├── test_auth.py              # Authentication tests
│   ├── test_exercise.py          # Exercise tests
│   ├── test_statistic.py         # Statistics tests
│   └── test_workout.py           # Workout tests
│
├── alembic/
│   ├── versions/                 # Migration files
│   ├── env.py                    # Alembic configuration
│   └── script.py.mako            # Migration template
│
├── .dockerignore
├── .env.example                  # Environment variables template
├── .gitignore
├── alembic.ini                   # Alembic configuration
├── docker-compose.yml            # Docker services configuration
├── Dockerfile                    # Application container configuration
├── pyproject.toml                # Project configuration and tools
├── requirements.txt              # Python dependencies
└── README.md
```

---

# ✨ Features

## Authentication
- User registration
- Secure password hashing
- JWT authentication
- Protected API endpoints

## Exercises & Workouts
- Exercise CRUD operations
- Workout CRUD operations
- Workout sets tracking
- Workout history

## Statistics
- Exercise progress tracking
- Maximum weight statistics
- Workout analytics

## Database
- PostgreSQL integration
- SQLAlchemy ORM
- Async database operations
- Alembic migrations

## Development
- Dockerized application
- Automated testing
- Continuous Integration with GitHub Actions

---

# 🚀 Installation

## 1. Clone the repository

```bash
git clone https://github.com/d3arkw/FitnessTracker.git

cd FitnessTracker
```

---

## 2. Configure environment variables

Create `.env` file from `.env.example`:

```bash
cp .env.example .env
```

Configure required variables:

```env
DB_HOST=db
DB_PORT=5432
DB_NAME=fitnesstracker
DB_USER=postgres
DB_PASSWORD=your_password

SECRET_KEY=your_secret_key
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
```

---

## 3. Build Docker containers

```bash
docker compose build
```

---

## 4. Start the application

```bash
docker compose up -d
```

---

## 5. Check running containers

```bash
docker compose ps
```

If everything started successfully, open:

Swagger UI:

```
http://localhost:8080/docs
```

ReDoc:

```
http://localhost:8080/redoc
```

---

# 🧪 Testing

The project uses **Pytest** for automated testing.

Run tests inside Docker:

```bash
docker compose run --rm <service_name> pytest
```

Tests cover:

- Authentication logic
- Exercise services
- Workout services
- Statistics services

---

# ⚙️ Continuous Integration

The project uses **GitHub Actions** for automated CI.

The CI pipeline runs on:

- Push to the `main` branch
- Pull requests

Workflow steps:

- Checkout repository
- Configure environment variables
- Prepare Docker environment
- Run automated tests with Pytest

This ensures that new changes do not break existing functionality.

---

# 🛣️ Roadmap

## ✅ Completed

- [x] Project setup
- [x] PostgreSQL integration
- [x] SQLAlchemy configuration
- [x] Alembic migrations
- [x] User model
- [x] User registration
- [x] Password hashing
- [x] JWT authentication
- [x] Exercise CRUD
- [x] Workout CRUD
- [x] Workout history
- [x] Progress statistics
- [x] Input validation with Pydantic
- [x] Docker support
- [x] Automated testing with Pytest
- [x] GitHub Actions CI pipeline

## 🚀 Future Improvements

- [ ] Production deployment
- [ ] Refresh token mechanism
- [ ] Redis integration
- [ ] Background task processing

---

# 📚 Learning Goals

This project provided practical experience with:

- Modern Python backend development
- FastAPI architecture
- Async programming
- SQLAlchemy ORM
- PostgreSQL database design
- Alembic migrations
- REST API development
- Authentication and authorization
- Service-layer architecture
- Automated testing
- Docker and Docker Compose
- GitHub Actions CI
- Git workflow

---

# 📄 License

This project is created for portfolio and educational purposes.