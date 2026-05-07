FROM python:3.11-slim

WORKDIR /app
ENV PYTHONPATH=/shared_lib

COPY bff-service/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY shared_lib /shared_lib
RUN pip install -e /shared_lib

COPY bff-service/ .

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
