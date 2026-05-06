FROM python:3.11-slim

WORKDIR /app
ENV PYTHONPATH=/app

COPY worker/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY worker/ .

CMD ["celery", "-A", "app.core.celery_app", "worker", "--loglevel=info", "-Q", "main-queue"]
