#!/usr/bin/env bash
# One-shot bootstrap for Oracle Cloud Always Free VM (Ubuntu 22.04/24.04 ARM or x86).
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO_ROOT="$(cd "$ROOT/../.." && pwd)"

cd "$ROOT"

if [[ ! -f .env ]]; then
  cp .env.example .env
  echo "Created deploy/oracle/.env — edit APP_DOMAIN (VM public IP) and passwords, then re-run."
  exit 1
fi

# shellcheck disable=SC1091
source .env

if [[ "${POSTGRES_PASSWORD}" == "change-me-strong-password" ]]; then
  echo "Edit deploy/oracle/.env and set POSTGRES_PASSWORD and NEXTAUTH_SECRET before deploying."
  exit 1
fi

if ! command -v docker >/dev/null 2>&1; then
  echo "Installing Docker..."
  curl -fsSL https://get.docker.com | sh
  sudo usermod -aG docker "$USER" || true
  echo "Docker installed. If 'permission denied', run: newgrp docker   then re-run this script."
fi

if ! docker compose version >/dev/null 2>&1; then
  echo "Docker Compose plugin missing. Install docker-compose-plugin package."
  exit 1
fi

echo "Building and starting full stack..."
docker compose up -d --build

echo "Running database migrations..."
docker compose --profile setup run --rm migrate

echo ""
echo "=========================================="
echo " Deployment complete"
echo "=========================================="
echo " Migration Studio UI : ${PUBLIC_SCHEME:-http}://${APP_DOMAIN}:3000"
echo " Fastify / Socket.IO : ${PUBLIC_SCHEME:-http}://${API_DOMAIN}:3001"
echo " Parser API / docs   : ${PUBLIC_SCHEME:-http}://${PARSER_DOMAIN}:8000/docs"
echo ""
echo " Oracle Cloud: open ingress rules for TCP 3000, 3001, 8000 (and 80/443 if using HTTPS profile)."
echo " US team: share the UI URL above and create accounts via Register."
echo ""
echo " Optional HTTPS with domains:"
echo "   docker compose --profile https up -d"
echo "=========================================="
