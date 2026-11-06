#!/usr/bin/env bash
set -euo pipefail
# shellcheck disable=SC1091
source /load-env.sh
cd /app/frontend
export NODE_ENV="${NODE_ENV:-production}"
export HOSTNAME=127.0.0.1
export PORT=3000
export NEXTJS_PORT=3000
export NODE_OPTIONS="${NODE_OPTIONS:---max-old-space-size=384}"
: "${DATABASE_URL:?DATABASE_URL is required for Next.js — set it in /app/.env}"
: "${NEXTAUTH_SECRET:?NEXTAUTH_SECRET is required for Next.js — set it in /app/.env}"
echo "[nextjs] starting on 127.0.0.1:3000"
exec node node_modules/next/dist/bin/next start -H 127.0.0.1 -p 3000
