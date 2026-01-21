# BloodConnect - Setup & Installation Guide

## Project Created Successfully! ✅

Your full-stack BloodConnect application has been created with the following structure:

```
bloodconnect-1/
├── frontend/                    # Next.js React Frontend
│   ├── pages/                   # Next.js pages
│   │   ├── _app.tsx            # Next.js app wrapper
│   │   ├── index.tsx           # Home page
│   │   ├── dashboard.tsx       # Dashboard page
│   │   └── about.tsx           # About page
│   ├── components/
│   │   └── Navbar.tsx          # Navigation component
│   ├── styles/
│   │   └── globals.css         # Global styles with Tailwind
│   ├── utils/
│   │   └── api.ts              # Axios API client
│   ├── package.json
│   ├── tsconfig.json
│   ├── next.config.js
│   ├── tailwind.config.js
│   ├── postcss.config.js
│   ├── Dockerfile
│   └── README.md
│
├── backend/                     # FastAPI Backend
│   ├── app/
│   │   ├── api/                # API route handlers
│   │   │   ├── users.py        # User endpoints
│   │   │   ├── blood_requests.py # Blood request endpoints
│   │   │   ├── health.py       # Health check endpoint
│   │   │   └── __init__.py
│   │   ├── models/
│   │   │   ├── models.py       # SQLAlchemy ORM models
│   │   │   └── __init__.py
│   │   ├── schemas/
│   │   │   ├── schemas.py      # Pydantic validation schemas
│   │   │   └── __init__.py
│   │   ├── database/
│   │   │   ├── database.py     # Database configuration
│   │   │   └── __init__.py
│   │   ├── config/
│   │   │   ├── settings.py     # App configuration
│   │   │   └── __init__.py
│   │   ├── main.py             # FastAPI app instance
│   │   └── __init__.py
│   ├── requirements.txt
│   ├── .env.example
│   ├── Dockerfile
│   └── README.md
│
├── docker-compose.yml           # Docker Compose configuration
├── README.md                    # Main project README
└── .gitignore
```

## Installation & Running

### Option 1: Quick Start with Docker (Recommended)

Prerequisites:
- Docker and Docker Compose installed

```bash
cd /Users/nithinkrishnan/Documents/Development/BloodConnect/bloodconnect-1
docker-compose up --build
```

This will automatically:
1. Create and run PostgreSQL database (port 5432)
2. Build and run FastAPI backend (port 8000)
3. Build and run Next.js frontend (port 3000)

Visit the app at: http://localhost:3000

### Option 2: Manual Setup

#### Backend Setup

```bash
cd backend

# Create virtual environment
python -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Set up environment
cp .env.example .env

# Update .env with your PostgreSQL connection
# DATABASE_URL=postgresql://bloodconnect:bloodconnect@localhost:5432/bloodconnect_db

# Run the server
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

Backend available at: http://localhost:8000
- API Docs: http://localhost:8000/docs
- ReDoc: http://localhost:8000/redoc

#### Frontend Setup

```bash
cd frontend

# Install dependencies
npm install

# Create .env.local
cat > .env.local << EOF
NEXT_PUBLIC_API_URL=http://localhost:8000/api
EOF

# Run development server
npm run dev
```

Frontend available at: http://localhost:3000

## Database Setup (If Not Using Docker)

Create PostgreSQL database:

```sql
-- Connect to PostgreSQL as admin
psql -U postgres

-- Create database
CREATE DATABASE bloodconnect_db;

-- Create user
CREATE USER bloodconnect WITH PASSWORD 'bloodconnect';

-- Set permissions
ALTER ROLE bloodconnect SET client_encoding TO 'utf8';
ALTER ROLE bloodconnect SET default_transaction_isolation TO 'read committed';
ALTER ROLE bloodconnect SET default_transaction_deferrable TO on;
ALTER ROLE bloodconnect SET timezone TO 'UTC';

-- Grant privileges
GRANT ALL PRIVILEGES ON DATABASE bloodconnect_db TO bloodconnect;
```

## Available API Endpoints

### Health Check
```
GET /api/health
```

### Users
```
GET    /api/users                    # List all users
POST   /api/users                    # Create user
GET    /api/users/{user_id}          # Get user by ID
PUT    /api/users/{user_id}          # Update user
DELETE /api/users/{user_id}          # Delete user
```

### Blood Requests
```
GET    /api/blood-requests           # List requests
POST   /api/blood-requests           # Create request
GET    /api/blood-requests/{id}      # Get request by ID
PUT    /api/blood-requests/{id}      # Update request
DELETE /api/blood-requests/{id}      # Delete request
```

## Technology Stack

### Frontend
- ✅ Next.js 14 (React framework)
- ✅ React 18 (UI library)
- ✅ TypeScript (Type safety)
- ✅ Tailwind CSS (Styling)
- ✅ Axios (HTTP client)

### Backend
- ✅ FastAPI (Web framework)
- ✅ SQLAlchemy (ORM)
- ✅ Pydantic (Data validation)
- ✅ PostgreSQL (Database)
- ✅ Uvicorn (ASGI server)

### DevOps
- ✅ Docker (Containerization)
- ✅ Docker Compose (Orchestration)

## Next Steps

1. **Install Dependencies**
   - Backend: `pip install -r requirements.txt`
   - Frontend: `npm install`

2. **Configure Database**
   - Update `.env` with your PostgreSQL connection

3. **Run the Application**
   - Using Docker: `docker-compose up --build`
   - Or manually start backend and frontend

4. **Explore the API**
   - Visit http://localhost:8000/docs for interactive API docs

5. **Customize**
   - Add more pages in `frontend/pages/`
   - Add more API routes in `backend/app/api/`
   - Extend database models in `backend/app/models/`

## Troubleshooting

**Backend won't connect to PostgreSQL**
- Ensure PostgreSQL is running
- Check DATABASE_URL in .env is correct
- Verify user permissions

**Frontend can't connect to backend**
- Ensure backend is running on port 8000
- Check NEXT_PUBLIC_API_URL in .env.local

**Port conflicts**
- Change ports in docker-compose.yml or uvicorn/npm commands

## File Locations

- Root: `/Users/nithinkrishnan/Documents/Development/BloodConnect/bloodconnect-1/`
- Frontend: `./frontend/`
- Backend: `./backend/`

Happy coding! 🩸❤️
