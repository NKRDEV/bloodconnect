#!/bin/bash

# BloodConnect - Quick Start Script
# This script helps you get started with BloodConnect

echo "🩸 BloodConnect - Blood Donation Platform"
echo "=========================================="
echo ""

# Check if Docker is installed
if ! command -v docker &> /dev/null; then
    echo "⚠️  Docker is not installed. Please install Docker first."
    echo "Visit: https://www.docker.com/products/docker-desktop"
    exit 1
fi

echo "Available commands:"
echo ""
echo "1. Start with Docker (Recommended):"
echo "   docker-compose up --build"
echo ""
echo "2. Start Backend Only:"
echo "   cd backend"
echo "   python -m venv venv"
echo "   source venv/bin/activate"
echo "   pip install -r requirements.txt"
echo "   cp .env.example .env"
echo "   uvicorn app.main:app --reload"
echo ""
echo "3. Start Frontend Only:"
echo "   cd frontend"
echo "   npm install"
echo "   echo 'NEXT_PUBLIC_API_URL=http://localhost:8000/api' > .env.local"
echo "   npm run dev"
echo ""
echo "After running, visit:"
echo "  Frontend:    http://localhost:3000"
echo "  Backend:     http://localhost:8000"
echo "  API Docs:    http://localhost:8000/docs"
echo ""
