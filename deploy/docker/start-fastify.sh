#!/usr/bin/env bash
set -euo pipefail
# shellcheck disable=SC1091
source /load-env.sh
cd /app/frontend
export NODE_ENV="${NODE_ENV:-production}"
export FASTIFY_PORT=3001
export PORT=3001
export NODE_OPTIONS="${NODE_OPTIONS:---max-old-space-size=384}"
: "${DATABASE_URL:?DATABASE_URL is required for Fastify — set it in /app/.env}"
echo "[fastify] starting on 127.0.0.1:3001 (DATABASE_URL set, FASTAPI_URL=${FASTAPI_URL})"
exec ./node_modules/.bin/tsx src/server/app.ts
