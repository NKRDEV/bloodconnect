# BloodConnect - Blood Donation Platform

A full-stack web application for connecting blood donors with those in need. Built with modern technologies for scalability and user experience.

## Project Overview

BloodConnect is a comprehensive blood donation platform featuring:
- **Frontend**: React with Next.js for fast, SEO-friendly web interface
- **Backend**: FastAPI for high-performance REST API
- **Database**: PostgreSQL for reliable data storage
- **Containerization**: Docker for easy deployment

## Quick Start

### Option 1: Using Docker Compose (Recommended)

```bash
docker-compose up --build
```

This will start:
- PostgreSQL database on port 5432
- FastAPI backend on port 8000
- Next.js frontend on port 3000

### Option 2: Manual Setup

#### Backend Setup

1. Navigate to the backend directory:
```bash
cd backend
```

2. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Set up environment variables:
```bash
cp .env.example .env
```

5. Start PostgreSQL and update the DATABASE_URL in .env

6. Run the server:
```bash
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

Backend will be available at: `http://localhost:8000`
- API Documentation: `http://localhost:8000/docs`

#### Frontend Setup

1. Navigate to the frontend directory:
```bash
cd frontend
```

2. Install dependencies:
```bash
npm install
```

3. Create `.env.local`:
```
NEXT_PUBLIC_API_URL=http://localhost:8000/api
```

4. Run the development server:
```bash
npm run dev
```

Frontend will be available at: `http://localhost:3000`

## Project Structure

```
bloodconnect/
├── frontend/                 # Next.js React frontend
│   ├── pages/               # Next.js pages
│   ├── components/          # Reusable React components
│   ├── styles/              # CSS and Tailwind configuration
│   ├── utils/               # Utility functions
│   ├── package.json
│   ├── tsconfig.json
│   ├── next.config.js
│   ├── tailwind.config.js
│   └── README.md
│
├── backend/                 # FastAPI backend
│   ├── app/
│   │   ├── api/            # API endpoints
│   │   ├── models/         # SQLAlchemy models
│   │   ├── schemas/        # Pydantic schemas
│   │   ├── database/       # Database configuration
│   │   ├── config/         # App configuration
│   │   └── main.py         # FastAPI app instance
│   ├── requirements.txt
│   ├── .env.example
│   ├── Dockerfile
│   └── README.md
│
├── docker-compose.yml       # Docker compose configuration
└── README.md               # This file
```

## API Endpoints

### Health Check
- `GET /api/health` - Health check endpoint

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

## Technologies Used

### Frontend
- **Next.js 14** - React framework with server-side rendering
- **React 18** - UI library
- **TypeScript** - Type safety
- **Tailwind CSS** - Utility-first CSS framework
- **Axios** - HTTP client

### Backend
- **FastAPI** - Modern Python web framework
- **SQLAlchemy** - ORM for database
- **PostgreSQL** - Relational database
- **Pydantic** - Data validation
- **Uvicorn** - ASGI server

### DevOps
- **Docker** - Containerization
- **Docker Compose** - Multi-container orchestration

## Environment Variables

### Backend (.env)
```
DATABASE_URL=postgresql://bloodconnect:bloodconnect@localhost:5432/bloodconnect_db
API_V1_PREFIX=/api
PROJECT_NAME=BloodConnect
PROJECT_VERSION=0.1.0
DEBUG=True
```

### Frontend (.env.local)
```
NEXT_PUBLIC_API_URL=http://localhost:8000/api
```

## Database Setup

If running without Docker, create a PostgreSQL database:

```sql
CREATE DATABASE bloodconnect_db;
CREATE USER bloodconnect WITH PASSWORD 'bloodconnect';
ALTER ROLE bloodconnect SET client_encoding TO 'utf8';
ALTER ROLE bloodconnect SET default_transaction_isolation TO 'read committed';
ALTER ROLE bloodconnect SET default_transaction_deferrable TO on;
ALTER ROLE bloodconnect SET timezone TO 'UTC';
GRANT ALL PRIVILEGES ON DATABASE bloodconnect_db TO bloodconnect;
```

## Development

### Running Tests

Backend:
```bash
cd backend
pytest
```

Frontend:
```bash
cd frontend
npm test
```

### Building for Production

Backend:
```bash
cd backend
pip install -r requirements.txt
# Update .env for production
uvicorn app.main:app --host 0.0.0.0 --port 8000
```

Frontend:
```bash
cd frontend
npm run build
npm start
```

## Contributing

1. Create a feature branch
2. Make your changes
3. Test thoroughly
4. Submit a pull request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Support

For issues and questions, please open an issue in the repository.

## Features

### Current Features
- User registration and management
- Blood type tracking
- Blood request creation and management
- Health check endpoint
- CORS support for cross-origin requests
- Type-safe frontend with TypeScript
- Responsive design with Tailwind CSS

### Planned Features
- User authentication and authorization
- Donation history tracking
- Blood inventory management
- Real-time notifications
- Location-based blood request matching
- Mobile app
- Payment integration
- Analytics dashboard 
