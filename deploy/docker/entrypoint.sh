#!/usr/bin/env bash
set -euo pipefail

# Static .env mounted at /app/.env is the source of truth (EC2 + local Docker).
# shellcheck disable=SC1091
source /load-env.sh

export PORT="${PORT:-10000}"
export POSTGRES_PASSWORD="${POSTGRES_PASSWORD:-postgres}"
export NEXTAUTH_SECRET="${NEXTAUTH_SECRET:-dev-change-me-in-production}"
export PUBLIC_URL="${RENDER_EXTERNAL_URL:-${PUBLIC_URL:-http://127.0.0.1:${PORT}}}"
export EMBED_INFRA="${EMBED_INFRA:-false}"

export FASTAPI_URL="http://127.0.0.1:8000"
export FASTIFY_URL="http://127.0.0.1:3001"
export FRONTEND_URL="${PUBLIC_URL}"
export NEXTAUTH_URL="${PUBLIC_URL}"
export LLM_ENABLED="${LLM_ENABLED:-true}"
export CODEGEN_LLM_ENABLED="${CODEGEN_LLM_ENABLED:-true}"
export EXPORT_FAST_MODE="${EXPORT_FAST_MODE:-true}"
export EXPORT_CACHE_TTL_SEC="${EXPORT_CACHE_TTL_SEC:-900}"
export NODE_ENV="${NODE_ENV:-production}"

urlencode() {
  python -c 'from urllib.parse import quote_plus; import sys; print(quote_plus(sys.argv[1]))' "$1"
}

# Upstash / Render users sometimes paste the redis-cli command instead of the URL.
normalize_redis_url() {
  local raw="$1"
  raw="${raw//$'\r'/}"
  raw="${raw//$'\n'/}"
  raw="${raw#"${raw%%[![:space:]]*}"}"
  raw="${raw%"${raw##*[![:space:]]}"}"
  raw="${raw#\"}"; raw="${raw%\"}"
  raw="${raw#\'}"; raw="${raw%\'}"

  if [[ "${raw}" == *"rediss://"* ]]; then
    raw="$(printf '%s' "${raw}" | sed -E 's#.*(rediss://[^[:space:]"'\'']+).*#\1#')"
  elif [[ "${raw}" == *"redis://"* ]]; then
    raw="$(printf '%s' "${raw}" | sed -E 's#.*(redis://[^[:space:]"'\'']+).*#\1#')"
  fi

  raw="$(printf '%s' "${raw}" | sed -E 's#:6379:6379#:6379#g')"

  if [[ "${raw}" == redis://* ]] && [[ "${raw}" == *upstash.io* ]]; then
    raw="rediss://${raw#redis://}"
  fi

  printf '%s' "${raw}"
}

# ── Helpers for embedded Postgres (EMBED_INFRA=true only) ────────────────────

postgres_bin_dir() {
  ls -1d /usr/lib/postgresql/*/bin 2>/dev/null | sort -V | tail -1
}

run_as_postgres() {
  local PG_BIN
  PG_BIN="$(postgres_bin_dir)"
  su postgres -s /bin/bash <<EOF
export PATH="${PG_BIN}:\$PATH"
$*
EOF
}

# ── Connectivity probes ───────────────────────────────────────────────────────

# Works for both local and cloud Postgres (Neon, RDS, etc.) via psycopg3.
# Accepts a full DATABASE_URL including ?sslmode=require.
wait_for_postgres() {
  local url="${1:?DATABASE_URL required}"
  echo "==> Waiting for PostgreSQL (psycopg probe)..."
  for _ in $(seq 1 30); do
    if python -c "
import sys
try:
    import psycopg
    conn = psycopg.connect('${url}', connect_timeout=5)
    conn.close()
    sys.exit(0)
except Exception:
    sys.exit(1)
" 2>/dev/null; then
      echo "==> PostgreSQL ready."
      return 0
    fi
    sleep 2
  done
  echo "ERROR: Cannot connect to PostgreSQL at given DATABASE_URL after 60s"
  exit 1
}

wait_for_rabbitmq() {
  local url="${1:?CELERY_BROKER_URL required}"
  echo "==> Waiting for RabbitMQ (kombu probe)..."
  for _ in $(seq 1 30); do
    if python -c "
import sys
try:
    from kombu import Connection
    conn = Connection('${url}')
    conn.connect()
    conn.release()
    sys.exit(0)
except Exception:
    sys.exit(1)
" 2>/dev/null; then
      echo "==> RabbitMQ ready."
      return 0
    fi
    sleep 2
  done
  echo "ERROR: Cannot connect to RabbitMQ."
  exit 1
}

wait_for_redis() {
  local url="${1:?REDIS_URL required}"
  echo "==> Waiting for Redis..."
  for _ in $(seq 1 30); do
    if python -c "
import sys, redis
try:
    client = redis.from_url('${url}', socket_connect_timeout=5, socket_timeout=5)
    client.ping()
    sys.exit(0)
except Exception:
    sys.exit(1)
" 2>/dev/null; then
      echo "==> Redis ready."
      return 0
    fi
    sleep 2
  done
  echo "ERROR: Cannot connect to Redis."
  exit 1
}

wait_for_chroma() {
  local host="${1:?chroma host required}"
  local port="${2:-8000}"
  echo "==> Waiting for ChromaDB at ${host}:${port}..."
  for _ in $(seq 1 120); do
    if curl -fsS "http://${host}:${port}/api/v2/heartbeat" >/dev/null 2>&1 \
      || curl -fsS "http://${host}:${port}/api/v1/heartbeat" >/dev/null 2>&1; then
      return 0
    fi
    sleep 1
  done
  echo "ERROR: ChromaDB not ready at ${host}:${port}"
  exit 1
}

maybe_ingest_kb() {
  if [ "${CHROMA_AUTO_INGEST:-true}" != "true" ]; then
    return 0
  fi
  if [ -z "${CHROMA_HOST:-}" ]; then
    return 0
  fi
  echo "==> Populating knowledge base in ChromaDB..."
  cd /app
  python mule_parser/scripts/ingest_kb.py || echo "WARN: KB ingest failed (ChromaDB may still be starting)"
}

# ── Infrastructure bootstrap ─────────────────────────────────────────────────

if [ "${EMBED_INFRA}" = "true" ]; then
  # Embedded mode: local Postgres + Redis run inside the container (local dev only).
  # Requires postgresql + redis-server installed in the image.
  PG_BIN="$(postgres_bin_dir)"
  if [ -z "${PG_BIN}" ] || [ ! -x "${PG_BIN}/initdb" ]; then
    echo "ERROR: PostgreSQL binaries not found — EMBED_INFRA=true requires postgresql in the image."
    exit 1
  fi

  ENCODED_POSTGRES_PASSWORD="$(urlencode "${POSTGRES_PASSWORD}")"
  export DATABASE_URL="postgresql://${POSTGRES_USER}:${ENCODED_POSTGRES_PASSWORD}@127.0.0.1:5432/${POSTGRES_DB}"
  export REDIS_URL="redis://127.0.0.1:6379"
  export CELERY_BROKER_URL="redis://127.0.0.1:6379/0"
  export CHROMA_HOST="${CHROMA_HOST:-127.0.0.1}"
  export CHROMA_PORT="${CHROMA_PORT:-8100}"
  SUPERVISORD_CONF="/etc/supervisor/conf.d/migration.embed.conf"

  echo "==> Initializing embedded PostgreSQL..."
  PG_LOG="${PGDATA}/postgresql.log"
  mkdir -p "${PGDATA}" /var/run/postgresql
  chown -R postgres:postgres "${PGDATA}" /var/run/postgresql

  if [ ! -f "${PGDATA}/PG_VERSION" ]; then
    run_as_postgres "initdb -D \"${PGDATA}\" --auth=trust"
    echo "host all all 127.0.0.1/32 trust" >> "${PGDATA}/pg_hba.conf"
  fi

  run_as_postgres "pg_ctl -D \"${PGDATA}\" -l \"${PG_LOG}\" start"
  wait_for_postgres "${DATABASE_URL}"

  run_as_postgres "psql -tc \"SELECT 1 FROM pg_database WHERE datname='${POSTGRES_DB}'\" | grep -q 1 || createdb \"${POSTGRES_DB}\""
  run_as_postgres "psql -c \"ALTER USER ${POSTGRES_USER} WITH PASSWORD '${POSTGRES_PASSWORD}';\""
else
  # External mode: Neon (managed Postgres) + self-hosted Redis + RabbitMQ.
  : "${DATABASE_URL:?DATABASE_URL is required when EMBED_INFRA=false}"
  : "${REDIS_URL:?REDIS_URL is required when EMBED_INFRA=false}"
  : "${CELERY_BROKER_URL:?CELERY_BROKER_URL is required when EMBED_INFRA=false}"

  # Rewrite localhost/127.0.0.1 to service hostnames for Docker network
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
  
  SUPERVISORD_CONF="/etc/supervisor/conf.d/migration.external.conf"

  # Probes
  wait_for_postgres "${DATABASE_URL}"
  wait_for_rabbitmq "${CELERY_BROKER_URL}"
  wait_for_redis "${REDIS_URL}"

  export CHROMA_HOST="${CHROMA_HOST:-}"
  export CHROMA_PORT="${CHROMA_PORT:-8000}"
  if [ -n "${CHROMA_HOST}" ]; then
    wait_for_chroma "${CHROMA_HOST}" "${CHROMA_PORT}"
    maybe_ingest_kb
  fi
fi

echo "==> Running Prisma migrations..."
cd /app/frontend
npx prisma migrate deploy

mkdir -p /var/lib/chromadb

echo "==> Starting application services (supervisord)..."
echo "    Mode: EMBED_INFRA=${EMBED_INFRA}"
echo "    Env file: ${APP_ENV_FILE:-/app/.env} ($([ -f /app/.env ] && echo present || echo missing))"
echo "    ChromaDB: ${CHROMA_HOST:-disabled}:${CHROMA_PORT:-n/a}"
echo "    Public URL: ${PUBLIC_URL}"
echo "    Health check: http://127.0.0.1:${PORT}/health"
exec /usr/bin/supervisord -c "${SUPERVISORD_CONF}"
