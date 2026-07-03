# 🏋️ Fitness Tracker API

A RESTful backend API for a fitness tracking application built with **FastAPI**, **PostgreSQL**, and **SQLAlchemy**.

This project is being developed from scratch to learn modern backend development, database design, and REST API architecture using Python.

---

# 🚀 Tech Stack

- Python 3.13
- FastAPI
- PostgreSQL
- SQLAlchemy
- Alembic
- Pydantic
- Uvicorn
- python-dotenv

---

# 📂 Project Structure

```text
FitnessTracker/
│
├── alembic/
│   └── versions/             # Database migration history
│
├── app/
│   ├── __init__.py
│   ├── config.py             # Environment variables
│   ├── database.py           # SQLAlchemy configuration
│   └── main.py               # FastAPI application
│
├── models/
│   ├── __init__.py
│   └── user.py               # SQLAlchemy models
│
├── routers/                  # API routes
│
├── schemas/                  # Pydantic schemas
│
├── .env
├── .gitignore
├── alembic.ini
├── requirements.txt
└── README.md
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

# ⚙️ Installation

## Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/FitnessTracker.git
cd FitnessTracker
```

## Create a virtual environment

```bash
python -m venv venv
```

### macOS / Linux

```bash
source venv/bin/activate
```

### Windows

```bash
venv\Scripts\activate
```

## Install dependencies

```bash
pip install -r requirements.txt
```

## Create a `.env` file

```env
DATABASE_URL=postgresql+psycopg2://YOUR_USER:YOUR_PASSWORD@localhost:5432/YOUR_DATABASE
```

## Apply database migrations

```bash
alembic upgrade head
```

## Run the development server

```bash
uvicorn app.main:app --reload
```

Swagger documentation will be available at:

```
http://127.0.0.1:8000/docs
```

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

## 🚧 In Progress

- [ ] User authentication (JWT)

## 📌 Planned

- [ ] Workout CRUD
- [ ] Exercise CRUD
- [ ] Workout history
- [ ] Progress statistics
- [ ] Nutrition tracking
- [ ] Input validation
- [ ] Docker support
- [ ] Unit tests
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
