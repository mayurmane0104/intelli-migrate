# syntax=docker/dockerfile:1.7
# Migration Studio image
# Parser + Celery + Fastify + Next.js + Caddy (single PORT)
# Postgres: Neon (managed) | Redis: Upstash (managed TLS)
# Set EMBED_INFRA=true only for local dev with embedded postgres+redis (requires extra apt packages)

# ── Build Next.js ────────────────────────────────────────────────────────────
FROM node:20-bookworm-slim AS next-builder
WORKDIR /studio
RUN apt-get update && apt-get install -y --no-install-recommends openssl ca-certificates \
    && rm -rf /var/lib/apt/lists/*
COPY frontend/package.json frontend/package-lock.json ./
RUN npm config set fetch-retries 5 \
    && npm config set fetch-retry-mintimeout 20000 \
    && npm config set fetch-retry-maxtimeout 120000 \
    && npm ci
COPY frontend/ ./
# Same-origin mode: client uses window.location.origin when unset
ENV NEXT_PUBLIC_APP_URL=
ENV NEXT_PUBLIC_API_URL=
# Prisma config loads at build time; no DB connection happens during generate/build.
ENV DATABASE_URL="postgresql://postgres:build@127.0.0.1:5432/migration_studio"
RUN npx prisma generate && npm run build

# ── Runtime image ────────────────────────────────────────────────────────────
FROM python:3.12-bookworm

ENV DEBIAN_FRONTEND=noninteractive \
    PYTHONUNBUFFERED=1 \
    PYTHONPATH=/app \
    PORT=10000 \
    EMBED_INFRA=false \
    APP_ENV_FILE=/app/.env

RUN apt-get update && apt-get install -y --no-install-recommends \
    curl ca-certificates gnupg supervisor \
    && curl -fsSL https://deb.nodesource.com/setup_20.x | bash - \
    && apt-get install -y nodejs \
    && curl -1sLf 'https://dl.cloudsmith.io/public/caddy/stable/gpg.key' | gpg --dearmor -o /usr/share/keyrings/caddy-stable-archive-keyring.gpg \
    && curl -1sLf 'https://dl.cloudsmith.io/public/caddy/stable/debian.deb.txt' | tee /etc/apt/sources.list.d/caddy-stable.list \
    && apt-get update && apt-get install -y caddy \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

# Runtime deps include boto3/OpenAI; Anthropic and Google GenAI SDKs are optional.
ARG INSTALL_LLM=false
ENV PIP_DEFAULT_TIMEOUT=60 \
    PIP_RETRIES=5 \
    PIP_DISABLE_PIP_VERSION_CHECK=1

COPY mule_parser/requirements-docker.txt /app/mule_parser/requirements-docker.txt
RUN --mount=type=cache,target=/root/.cache/pip,sharing=locked \
    --mount=type=secret,id=pip_config,target=/etc/pip.conf,required=false \
    python -m pip install --prefer-binary --timeout 60 --retries 5 \
        --index-url https://pypi.org/simple \
        --extra-index-url https://pypi.python.org/simple \
        -r /app/mule_parser/requirements-docker.txt \
    && if [ "$INSTALL_LLM" = "true" ]; then \
         python -m pip install --prefer-binary --timeout 60 --retries 5 \
             --index-url https://pypi.org/simple \
             --extra-index-url https://pypi.python.org/simple \
             anthropic google-genai; \
       fi

COPY mule_parser /app/mule_parser
COPY --from=next-builder /studio /app/frontend

COPY deploy/docker/Caddyfile /etc/caddy/Caddyfile
COPY deploy/docker/supervisord.embed.conf /etc/supervisor/conf.d/migration.embed.conf
COPY deploy/docker/supervisord.external.conf /etc/supervisor/conf.d/migration.external.conf
COPY deploy/docker/load-env.sh /load-env.sh
COPY deploy/docker/entrypoint.sh /entrypoint.sh
COPY deploy/docker/start-nextjs.sh /entrypoint-start-nextjs.sh
COPY deploy/docker/start-fastify.sh /entrypoint-start-fastify.sh
RUN chmod +x /load-env.sh /entrypoint.sh /entrypoint-start-nextjs.sh /entrypoint-start-fastify.sh \
    && mkdir -p /var/log/supervisor /var/lib/chromadb

EXPOSE 10000

HEALTHCHECK --interval=30s --timeout=10s --start-period=300s --retries=5 \
    CMD sh -c 'curl -fsS "http://127.0.0.1:${PORT:-10000}/health" || exit 1'

ENTRYPOINT ["/entrypoint.sh"]
