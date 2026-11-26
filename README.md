# Inventory CI/CD Project

## Overview
A simple inventory application is developed with Python and Flask.
Inventory data is stored in memory and is reset when the application restarts.

## Requirements
Python 3, pip, and Git are required.

## Installation
From the project directory, run:

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt -r requirements-dev.txt
```

## Run the application
```bash
python -m flask --app app.main run --host 127.0.0.1 --port 5000
```

## Endpoints
- GET /items
- GET /items/<id>
- GET /inventory/summary
- GET /health
- GET /version

## Verification
```bash
python -m pytest -v
ruff check app tests
```
## Example request

The application health status is checked with:

```bash
curl http://127.0.0.1:5000/health
```

Expected response:

```json
{"status":"ok"}
```
