# BloodConnect Backend

A FastAPI backend for the BloodConnect blood donation platform with PostgreSQL database.

## Getting Started

### Prerequisites
- Python 3.9+
- PostgreSQL 12+

### Installation

1. Create and activate a virtual environment:

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Set up environment variables:

```bash
cp .env.example .env
```

4. Update `.env` with your PostgreSQL connection details:

```
DATABASE_URL=postgresql://user:password@localhost:5432/bloodconnect_db
```

### Running the Server

```bash
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

The API will be available at `http://localhost:8000`
- API Docs: `http://localhost:8000/docs`
- ReDoc: `http://localhost:8000/redoc`

## Project Structure

- `app/` - Main application code
  - `api/` - API endpoints
  - `models/` - SQLAlchemy database models
  - `schemas/` - Pydantic schemas
  - `database/` - Database configuration
  - `config/` - Application configuration
  - `main.py` - FastAPI application instance

## Database Setup

Create a PostgreSQL database:

```sql
CREATE DATABASE bloodconnect_db;
CREATE USER bloodconnect WITH PASSWORD 'bloodconnect';
ALTER ROLE bloodconnect SET client_encoding TO 'utf8';
ALTER ROLE bloodconnect SET default_transaction_isolation TO 'read committed';
ALTER ROLE bloodconnect SET default_transaction_deferrable TO on;
ALTER ROLE bloodconnect SET timezone TO 'UTC';
GRANT ALL PRIVILEGES ON DATABASE bloodconnect_db TO bloodconnect;
```

## API Endpoints

### Users
- `GET /api/users` - List all users
- `POST /api/users` - Create a new user
- `GET /api/users/{user_id}` - Get user by ID
- `PUT /api/users/{user_id}` - Update user
- `DELETE /api/users/{user_id}` - Delete user

### Blood Requests
- `GET /api/blood-requests` - List all blood requests
- `POST /api/blood-requests` - Create a new blood request
- `GET /api/blood-requests/{request_id}` - Get blood request by ID
- `PUT /api/blood-requests/{request_id}` - Update blood request
- `DELETE /api/blood-requests/{request_id}` - Delete blood request

### Health
- `GET /api/health` - Health check endpoint

## Technologies

- FastAPI
- SQLAlchemy
- PostgreSQL
- Pydantic
- Uvicorn
