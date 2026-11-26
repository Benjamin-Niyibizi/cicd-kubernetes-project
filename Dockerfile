FROM python:3.12-slim

RUN apt-get update \
    && apt-get install -y --no-install-recommends --only-upgrade libzstd1 \
    && rm -rf /var/lib/apt/lists/*
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PORT=5000

WORKDIR /app

COPY requirements.txt .
RUN python -m pip install --no-cache-dir -r requirements.txt

RUN useradd --create-home appuser

COPY app/ ./app/
COPY VERSION .

USER appuser

EXPOSE 5000

HEALTHCHECK --interval=30s --timeout=5s --start-period=10s --retries=3 \
    CMD python -c "import os, urllib.request; urllib.request.urlopen('http://127.0.0.1:' + os.environ['PORT'] + '/health', timeout=3)" || exit 1

CMD ["sh", "-c", "exec gunicorn --bind 0.0.0.0:${PORT} app.main:app"]
