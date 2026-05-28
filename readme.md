# Bookly API

**Bookly** is a robust REST API service built with _FastAPI_ to manage book reviews. This project serves as an advanced implementation of API development practices, covering production-ready features beyond basic CRUD operations.

## Key Features

- **RESTful CRUD API**: Full management of book and review resources.
- **User Authentication**: Secure user management featuring _JWT_ authentication, password hashing with _passlib_, and role-based access control (RBAC).
- **Database Management**: Utilizes _SQLModel_ and _PostgreSQL_ for data persistence with asynchronous sessions and _Alembic_ for database migrations.
- **Background Tasks**: Offloads intensive tasks (such as sending verification emails) using _Celery_ and _Redis_.
- **API Documentation**: Interactive documentation automatically generated via _SwaggerUI_ and _ReDoc_.
- **Testing**: Comprehensive testing suite using _Pytest_ for unit testing and _Schemathesis_ for document-driven testing.

## Tech Stack

- **Framework**: _FastAPI_
- **ORM**: _SQLModel_
- **Database**: _PostgreSQL_
- **Migration Tool**: _Alembic_
- **Task Queue**: _Celery_ with _Redis_
- **Security**: _PyJWT_, _passlib_

## Getting Started

1.  **Clone the repository**: `git clone <your-repository-url>`
2.  **Install dependencies**: `pip install -r requirements.txt`
3.  **Setup Environment**: Configure your `.env` file with database and Redis connection strings.
4.  **Run Migrations**: `alembic upgrade head`
5.  **Start the Server**: `fastapi dev source/main.py`

## Documentation

Once the server is running, you can access the interactive API documentation at:

- **SwaggerUI**: `/docs`
- **ReDoc**: `/redoc`
