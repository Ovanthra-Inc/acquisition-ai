# Stage 1: Build dependencies
FROM python:3.11-slim as builder

WORKDIR /app
COPY worker/requirements.txt .
RUN pip install --no-cache-dir --prefix=/install -r requirements.txt

# Stage 2: Runtime
FROM python:3.11-slim

WORKDIR /app
ENV PYTHONPATH=/shared_lib

COPY --from=builder /install /usr/local
COPY shared_lib /shared_lib
RUN pip install -e /shared_lib

COPY worker/ .

COPY docker-entrypoint.sh /usr/local/bin/
RUN chmod +x /usr/local/bin/docker-entrypoint.sh
CMD ["/usr/local/bin/docker-entrypoint.sh"]
