FROM python:3.11-slim

WORKDIR /app
ENV PYTHONPATH=/app:/shared_lib

COPY worker/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy shared library
COPY shared_lib /shared_lib
RUN pip install -e /shared_lib

COPY worker/ .

CMD ["celery", "-A", "app.core.celery_app", "worker", "--loglevel=info"]
