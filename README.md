# 🏋️ Fitness Tracker API

A RESTful backend API for a fitness tracking application built with **FastAPI**, **PostgreSQL**, and **SQLAlchemy**.

This project is being developed from scratch to learn modern backend development, database design, and REST API architecture using Python.

---

# 🚀 Tech Stack

- Python 3.14
- FastAPI
- SQLAlchemy 2.0
- PostgreSQL
- Alembic
- Docker
- Docker Compose
- JWT Authentication
- Pytest
- AsyncPG
- Pydantic v2

---

# 📂 Project Structure

```text
FitnessTracker/
│
├── app/
│   ├── __init__.py
│   ├── main.py                   # FastAPI application entry point
│   ├── config.py                 # Application configuration and environment variables
│   ├── database.py               # Database connection and session management
│   ├── dependencies.py           # Shared FastAPI dependencies
│   │
│   ├── models/
│   │   ├── __init__.py
│   │   ├── exercise.py           # SQLAlchemy database models
│   │   ├── user.py               # SQLAlchemy database models
│   │   ├── workout.py            # SQLAlchemy database models
│   │   └── workoutset.py         # SQLAlchemy database models
│   │
│   ├── schemas/
│   │   ├── __init__.py
│   │   ├── exercises.py          # Pydantic request and response schemas
│   │   ├── statistic.py          # Pydantic request and response schemas
│   │   ├── user.py               # Pydantic request and response schemas
│   │   └── workouts.py           # Pydantic request and response schemas
│   │
│   ├── routers/
│   │   ├── __init__.py
│   │   ├── auth.py               # Authentication API endpoints
│   │   ├── exercises.py          # Exercises API endpoints
│   │   ├── statistics.py         # Statistics API endpoints
│   │   └── workouts.py           # Workouts API endpoints
│   │
│   ├── services/
│   │   ├── __init__.py
│   │   ├── auth_service.py       # Authentication business logic
│   │   ├── exercise_service.py   # Business logic for exercises
│   │   ├── statistics_service.py # Statistics business logic
│   │   └── workout_service.py    # Business logic for workout
│   │
│   └── utils/
│       ├── __init__.py
│       ├── jwt.py                # JWT token generation and validation
│       └── security.py           # Password hashing and verification
│
├── tests/
│   ├── conftest.py               # Pytest fixtures and test database setup
│   ├── test_auth.py              # Authentication tests
│   ├── test_exercise.py          # Exercise service tests
│   ├── test_statistic.py         # Statistics service tests
│   └── test_workout.py           # Workout service tests
│
├── alembic/                      # Database migration files
│   ├── versions/
│   ├── env.py                    # Alembic environment configuration
│   └── script.py.mako            # Migration template
│
├── .dockerignore
├── .env                          # Environment variables
├── .env.test                     # Test environment configuration
├── .gitignore
├── alembic.ini                   # Alembic configuration
├── docker-compose.yaml
├── Dockerfile                    # Docker file
├── pyproject.toml                # Project metadata and tool configuration (pytest)
├── README.md                     # Project documentation
└── requirements.txt              # Project dependencies

```

---

# ✨ Current Features

- ✅ FastAPI application initialized
- ✅ PostgreSQL connected
- ✅ Environment variables with `.env`
- ✅ SQLAlchemy Engine, Session and Base configured
- ✅ Alembic configured
- ✅ Initial `User` model
- ✅ First database migration created and applied

---

# 🚀 Installation

## 1. Clone the repository

```bash
git clone https://github.com/d3arkw/FitnessTracker.git
cd FitnessTracker
```

## 2. Configure environment variables

Create a `.env` file in the project root:

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

## 3. Build Docker containers

```bash
docker compose build
```

## 4. Start the application

```bash
docker compose up -d
```

## 5. Check running containers

```bash
docker compose ps
```

If everything started successfully, open:

- Swagger UI: http://localhost:8080/docs
- ReDoc: http://localhost:8080/redoc

---

# 🛣️ Roadmap

## ✅ Completed

- [x] Project setup
- [x] PostgreSQL integration
- [x] SQLAlchemy configuration
- [x] Alembic integration
- [x] User model
- [x] Initial migration
- [x] User registration
- [x] Password hashing
- [x] User authentication (JWT)
- [x] Exercise CRUD
- [x] Workout CRUD
- [x] Progress statistics
- [x] Docker support
- [x] Test coverage
- [x] Input validation
## 🚧 In Progress

- [ ] Workout history
## 📌 Planned

- [ ] Nutrition tracking
- [ ] CI/CD
- [ ] Deployment

---

# 📚 Learning Goals

The main purpose of this project is to gain hands-on experience with:

- FastAPI
- SQLAlchemy ORM
- PostgreSQL
- Alembic migrations
- REST API development
- Backend architecture
- Authentication & Authorization
- Clean project structure
- Git workflow
