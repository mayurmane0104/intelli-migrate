#!/usr/bin/env bash
# Load the static .env file mounted at /app/.env (Docker / EC2).
# Exports all keys into the current shell so supervisord + Python + Node inherit them.
set -euo pipefail

ENV_FILE="${APP_ENV_FILE:-/app/.env}"

if [ ! -f "${ENV_FILE}" ]; then
  if [ -f /app/mule_parser/.env ]; then
    ENV_FILE="/app/mule_parser/.env"
  else
    echo "==> No static .env at /app/.env (using process environment only)"
    return 0 2>/dev/null || exit 0
  fi
fi

echo "==> Loading static env from ${ENV_FILE}"

eval "$(python - <<'PY'
import os
import shlex
from pathlib import Path

try:
    from dotenv import dotenv_values
except ImportError:
    raise SystemExit(0)

path = Path(os.environ.get("APP_ENV_FILE", "/app/.env"))
if not path.is_file() and Path("/app/mule_parser/.env").is_file():
    path = Path("/app/mule_parser/.env")
if not path.is_file():
    raise SystemExit(0)

for key, val in dotenv_values(path).items():
    if val is None or key == "":
        continue
    print(f"export {key}={shlex.quote(str(val))}")
PY
)"

# Single canonical path for Python settings.py and Node dotenv fallbacks.
ln -sf "${ENV_FILE}" /app/.env 2>/dev/null || true
ln -sf "${ENV_FILE}" /app/mule_parser/.env 2>/dev/null || true

export APP_ENV_FILE="${ENV_FILE}"
export FASTAPI_URL="${FASTAPI_URL:-http://127.0.0.1:8000}"
export FASTIFY_URL="${FASTIFY_URL:-http://127.0.0.1:3001}"
export FRONTEND_URL="${FRONTEND_URL:-${PUBLIC_URL:-http://127.0.0.1:${PORT:-10000}}}"
export NEXTAUTH_URL="${NEXTAUTH_URL:-${PUBLIC_URL:-http://127.0.0.1:${PORT:-10000}}}"

# In Docker external mode, rewrite localhost/127.0.0.1 to service hostnames
if [ "${EMBED_INFRA:-false}" = "false" ]; then
  if [[ "${DATABASE_URL:-}" == *"localhost"* || "${DATABASE_URL:-}" == *"127.0.0.1"* ]]; then
    export DATABASE_URL="$(echo "${DATABASE_URL}" | sed -E 's#(localhost|127\.0\.0\.1)#postgres#g')"
  fi
  if [[ "${REDIS_URL:-}" == *"localhost"* || "${REDIS_URL:-}" == *"127.0.0.1"* ]]; then
    export REDIS_URL="$(echo "${REDIS_URL}" | sed -E 's#localhost|127.0.0.1#redis#g')"
  fi
  if [[ "${CELERY_BROKER_URL:-}" == *"localhost"* || "${CELERY_BROKER_URL:-}" == *"127.0.0.1"* ]]; then
    export CELERY_BROKER_URL="$(echo "${CELERY_BROKER_URL}" | sed -E 's#localhost|127.0.0.1#rabbitmq#g')"
  fi
  if [ "${CHROMA_HOST:-}" = "localhost" ] || [ "${CHROMA_HOST:-}" = "127.0.0.1" ]; then
    export CHROMA_HOST="chromadb"
  fi
fi

