#!/usr/bin/env bash
set -euo pipefail
cd frontend
exec npx tsx src/server/app.ts
