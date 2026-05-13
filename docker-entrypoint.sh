#!/bin/bash
set -e

# Extract the host and port from POSTGRES_SERVER if it contains them, otherwise default to db:5432
# Since POSTGRES_SERVER is usually just "db", we will wait for that.

echo "Waiting for postgres..."
# A simple wait loop could use nc, but python is available in our images
python -c "
import socket
import time
import os

host = os.environ.get('POSTGRES_SERVER', 'db')
port = 5432

# wait for up to 30 seconds
for _ in range(30):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((host, port))
        s.close()
        break
    except socket.error:
        time.sleep(1)
"
echo "Postgres is up!"

# Only run if alembic.ini exists (indicating it's an alembic project)
if [ -f "alembic.ini" ]; then
    echo "Running migrations..."
    # Suppress error if it fails because some services don't have alembic configured yet
    if command -v alembic >/dev/null 2>&1; then
        alembic upgrade head || echo "Alembic upgrade skipped or failed."
    else
        python -m alembic upgrade head || echo "Alembic upgrade skipped or failed."
    fi
else
    echo "Skipping migrations (not an alembic project)"
fi

echo "Starting service..."
if [ $# -gt 0 ]; then
    exec "$@"
else
    # Check if uvicorn is in path, if not try calling as python module
    if command -v uvicorn >/dev/null 2>&1; then
        exec uvicorn app.main:app --host 0.0.0.0 --port 8000
    else
        exec python -m uvicorn app.main:app --host 0.0.0.0 --port 8000
    fi
fi
