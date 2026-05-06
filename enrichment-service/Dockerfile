FROM python:3.11-slim

WORKDIR /app
ENV PYTHONPATH=/shared_lib

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY shared_lib /shared_lib
RUN pip install -e /shared_lib

COPY enrichment-service/ .

COPY docker-entrypoint.sh /usr/local/bin/
RUN chmod +x /usr/local/bin/docker-entrypoint.sh
CMD ["/usr/local/bin/docker-entrypoint.sh"]
# CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
