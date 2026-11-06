#!/usr/bin/env bash
set -euo pipefail
cd frontend
npx prisma migrate deploy
exec npm run start
