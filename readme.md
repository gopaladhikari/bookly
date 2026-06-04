# 📚 Bookly API

[![FastAPI](https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi)](https://fastapi.tiangolo.com/)
[![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)](https://www.python.org/)
[![PostgreSQL](https://img.shields.io/badge/postgresql-4169e1?style=for-the-badge&logo=postgresql&logoColor=white)](https://www.postgresql.org/)
[![Redis](https://img.shields.io/badge/redis-%23DD0031.svg?style=for-the-badge&logo=redis&logoColor=white)](https://redis.io/)

**Bookly** is a robust, production-ready REST API service designed for managing book reviews. Built with performance and scalability in mind, this project serves as an advanced implementation of modern API development, moving beyond basic CRUD operations to include asynchronous processing, secure authentication, and rigorous testing.

## ✨ Key Features

- **RESTful CRUD API**: Comprehensive endpoints for managing users, books, and reviews.
- **Secure Authentication**: JWT-based user authentication, password hashing with `passlib` and `bcrypt`, and Role-Based Access Control (RBAC).
- **Asynchronous Database Engine**: High-performance data persistence utilizing **SQLModel** and **PostgreSQL** with async sessions.
- **Automated Migrations**: Schema version control managed seamlessly via **Alembic**.
- **Background Task Processing**: Offloads CPU-intensive tasks (e.g., sending verification emails) using **Celery** workers and a **Redis** message broker.
- **Interactive API Documentation**: Auto-generated Swagger UI and ReDoc interfaces.
- **Comprehensive Testing**: Rigorous unit tests written in **Pytest** and property-based API testing via **Schemathesis**.

---

## 🛠️ Tech Stack

### Core

- **Web Framework**: FastAPI
- **ASGI Server**: Uvicorn
- **Language**: Python 3.10+

### Database & ORM

- **Database**: PostgreSQL (Neon)
- **ORM**: SQLModel (powered by SQLAlchemy)
- **Migrations**: Alembic

### Background Tasks & Caching

- **Task Queue**: Celery
- **Broker/Cache**: Redis

### Security & Testing

- **Auth**: PyJWT, Passlib (Bcrypt)
- **Testing**: Pytest, Schemathesis

---

## 🚀 Getting Started

Follow these instructions to set up the project locally for development and testing.

### Prerequisites

- Python 3.10 or higher
- PostgreSQL installed and running (or a cloud DB like Neon)
- Redis server installed and running

### 1. Clone the repository

```bash
git clone [https://github.com/gopaladhikari/bookly.git](https://github.com/gopaladhikari/bookly.git)
cd bookly
```
