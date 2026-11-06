# Docker deployment (Docker Hub → EC2)

One workflow. These files are the only ones you need in `deploy/docker/`:

| File | Purpose |
|------|---------|
| **`Dockerfile`** | Build the image (run on your laptop) |
| **`docker-compose.yml`** | Run on EC2 (pull image from Docker Hub) |
| **`.env.example`** | Template — copy to `.env` on EC2 |
| **`entrypoint.sh`** | Container startup (used by Dockerfile — do not run manually) |
| **`load-env.sh`** | Loads mounted `/app/.env` (used by entrypoint) |
| **`Caddyfile`** | Web proxy inside container (port 10000) |
| **`supervisord.external.conf`** | Runs FastAPI + Next.js + Fastify + Celery |
| **`start-nextjs.sh` / `start-fastify.sh`** | Helper scripts (used by supervisord) |

Everything else in this folder is internal plumbing copied into the image by the Dockerfile.

---

## Step 0 — Local Development (Run App Locally)

To develop locally without building the Docker image (which ensures your local changes don't go to Docker Hub until verified), use the local docker-compose file. This spins up **only** the backing infrastructure (Postgres, ChromaDB, RabbitMQ, Redis) and exposes their ports.

```bash
# From the deploy/docker/ directory:
docker compose -f docker-compose.local.yml up -d
```

Once the infrastructure is up, you can run your applications natively on your host machine:

1. **Python Backend (FastAPI / Celery)**: Run it from `mule_parser/` or wherever your python environment is set up. They will be able to connect to `localhost:5432` (Postgres), `localhost:8000` (ChromaDB), `localhost:6379` (Redis), and `localhost:5672` (RabbitMQ).
2. **Next.js / Fastify**: Run `npm run dev` in your respective JS folders.

This way, your code runs directly from your file system and any changes are reflected immediately.

---

## Step 1 — Build & push (your laptop, repo root)

```bash
docker build -f deploy/docker/Dockerfile -t YOUR_DOCKERHUB_USER/migration-studio:latest .
docker push YOUR_DOCKERHUB_USER/migration-studio:latest
```

The Dockerfile keeps pip's package cache in a BuildKit cache mount and retries slow PyPI downloads with a 10-minute timeout. Rebuilding after a network timeout can reuse packages already downloaded. If your network requires a trusted package mirror, pass its pip configuration as a BuildKit secret so credentials aren't copied into the image:

```bash
docker build --secret id=pip_config,src=/path/to/pip.conf \
  -f deploy/docker/Dockerfile -t YOUR_DOCKERHUB_USER/migration-studio:latest .
```

Without a mirror configuration, pip uses its default PyPI index. If it reports `from versions: none` for a known package, verify that the build container can reach PyPI; changing the version pin won't repair an unavailable index.

---

## Step 2 — Run on EC2

On the EC2 instance, create a folder and copy two files from this repo:

```text
~/migration-studio/
  docker-compose.yml    ← from deploy/docker/docker-compose.yml
  .env                  ← copy from .env.example, fill in secrets
```

```bash
cd ~/migration-studio
cp /path/to/repo/deploy/docker/docker-compose.yml .
cp /path/to/repo/deploy/docker/.env.example .env
nano .env   # DATABASE_URL, REDIS_URL, AWS keys, PUBLIC_URL, etc.

export IMAGE=YOUR_DOCKERHUB_USER/migration-studio:latest
docker compose pull
docker compose up -d
```

Open **http://YOUR_EC2_PUBLIC_IP** (port **80**).

### EC2 security group

Allow inbound **TCP 80** from your IP (or `0.0.0.0/0`).

### Verify

```bash
curl http://127.0.0.1/health          # → ok
docker logs migration-studio-app --tail 50
# Should show: "Loading static env from /app/.env" and "[fastify] starting"
```

### Step 2 shows 503 on analysis

Usually Fastify (port 3001) or FastAPI (port 8000) is not up yet, or `/app/.env` is not mounted.

```bash
# Inside container:
docker exec migration-studio-app curl -s http://127.0.0.1:8000/health
docker exec migration-studio-app curl -s http://127.0.0.1:3001/api/projects/PROJECT_ID/analysis/latest
docker exec migration-studio-app test -f /app/.env && echo "env mounted"
docker logs migration-studio-app 2>&1 | grep -E 'fastify|parser|DATABASE_URL|error'
```

Wait 1–2 minutes after `docker compose up`, then click **Refresh** on Step 2.

---

## `.env` on EC2

Mounted read-only at `/app/.env` inside the container. Required keys:

```env
DATABASE_URL=postgresql://...neon...?sslmode=require
REDIS_URL=rediss://...upstash...
CELERY_BROKER_URL=rediss://.../0
NEXTAUTH_SECRET=...
PUBLIC_URL=http://YOUR_EC2_PUBLIC_IP
LLM_ENABLED=true
AWS_ACCESS_KEY_ID=...
AWS_SECRET_ACCESS_KEY=...
AWS_DEFAULT_REGION=us-east-2
BEDROCK_MODEL_ID=us.amazon.nova-lite-v1:0
```

---

## Optional overrides

```bash
HOST_PORT=8080 docker compose up -d   # use port 8080 instead of 80
ENV_FILE=/path/to/.env docker compose up -d
```

---

## Architecture

```text
Internet :80
    └── migration-studio-app (Caddy :10000)
            ├── Next.js  :3000  (UI)
            ├── Fastify  :3001  (API + Socket.IO)
            ├── FastAPI  :8000  (Python migration engine)
            └── Celery worker
    └── chromadb (vector KB, internal only)
```

External services (not in this compose): **Neon Postgres**, **Upstash Redis**, **AWS Bedrock**.
