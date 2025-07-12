#!/bin/bash
set -e

# Run migrations
echo "Running database migrations..."
alembic upgrade head

# Run seeding if database is empty
echo "Checking if database needs seeding..."
python seed.py

# Start the main app
echo "Starting the application..."
exec python main.py
