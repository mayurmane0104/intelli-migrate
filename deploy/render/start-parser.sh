#!/usr/bin/env bash
# Run Celery worker + FastAPI in one Render web service (workers are not free on Render).
set -euo pipefail

export PYTHONPATH="${PYTHONPATH:-.}"

celery -A mule_parser.api.celery_app:celery_app worker --loglevel=info --concurrency=1 &

exec uvicorn mule_parser.api.app:app --host 0.0.0.0 --port "${PORT:-8000}"
