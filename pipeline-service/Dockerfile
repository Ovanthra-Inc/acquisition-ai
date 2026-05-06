FROM python:3.11-slim

WORKDIR /app

ENV PYTHONPATH=/

COPY pipeline-service/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY shared_lib /shared_lib
COPY pipeline-service/app ./app

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
