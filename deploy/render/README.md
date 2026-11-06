# Render Deployment — Migration Studio (Single Container)

Deploy the full Migration Studio stack on [Render](https://render.com) as a single Docker container.

**Database**: [Neon](https://neon.tech) (serverless Postgres — free tier, no 30-day expiry)  
**Redis**: [Upstash](https://upstash.com) (serverless Redis with TLS — free tier, persistent)

---

## Architecture

```
Internet → Render (Docker container)
              ├── Caddy (port 10000, reverse proxy)
              ├── Next.js (port 3000, UI)
              ├── Fastify (port 3001, API)
              ├── FastAPI/uvicorn (port 8000, parser)
              └── Celery worker
                        ↓               ↓
                   Neon Postgres    Upstash Redis
                   (managed SSL)    (managed TLS)
```

---

## Step 1 — Set up Neon Postgres

1. Go to [console.neon.tech](https://console.neon.tech) → **New Project**
2. Choose a region close to your Render region (e.g. `us-east-2` for Oregon)
3. After creation, go to **Connection Details** → copy the **Connection string**

It looks like:
```
postgresql://neondb_owner:password@ep-xxx.region.aws.neon.tech/neondb?sslmode=require
```

> [!IMPORTANT]
> Keep the `?sslmode=require` part — it is required for Neon connections.

---

## Step 2 — Set up Upstash Redis

1. Go to [console.upstash.com](https://console.upstash.com) → **Create Database**
2. Choose **Regional** and a region matching your Render service (e.g. `US-East-1`)
3. **Enable TLS** (required)
4. After creation, copy the **REDIS_URL** from the details page

It looks like:
```
rediss://default:password@host.upstash.io:port
```

> [!IMPORTANT]
> Upstash URLs start with `rediss://` (double-s = TLS). This is different from plain `redis://`.

---

## Step 3 — Deploy to Render

### Option A — Blueprint (recommended)

1. Push this repository to GitHub
2. Go to [Render Dashboard](https://dashboard.render.com) → **New** → **Blueprint**
3. Connect your GitHub repo
4. Set blueprint file path: **`deploy/render/render.yaml`**
5. Click **Apply** — this creates one **Docker web service** called `migration-studio`

First deploy takes **10–20 minutes** (Docker build).

6. After deploy, go to the service → **Environment** tab
7. Set these three values:

| Key | Value |
|-----|-------|
| `DATABASE_URL` | Neon connection string (from Step 1) |
| `REDIS_URL` | Upstash REDIS_URL (from Step 2) |
| `CELERY_BROKER_URL` | Same as REDIS_URL with `/0` at end |

8. Click **Save Changes** → Render will redeploy automatically

### Option B — Manual

1. **New → Web Service → Deploy an existing image or Docker file**
2. Connect GitHub repo
3. Settings:
   - **Dockerfile path**: `deploy/docker/Dockerfile`
   - **Docker build context**: `.` (repo root)
   - **Instance type**: Free
   - **Region**: Oregon (or nearest to your team)
   - **Health check path**: `/health`

4. Add environment variables (Environment tab):

| Key | Value |
|-----|-------|
| `DATABASE_URL` | Neon connection string |
| `REDIS_URL` | Upstash `rediss://...` URL |
| `CELERY_BROKER_URL` | Same as `REDIS_URL` + `/0` |
| `NEXTAUTH_SECRET` | Run `openssl rand -hex 32` locally and paste result |
| `EMBED_INFRA` | `false` |
| `PUBLIC_URL` | Your service's `.onrender.com` URL |
| `NEXTAUTH_URL` | Same as `PUBLIC_URL` |
| `FRONTEND_URL` | Same as `PUBLIC_URL` |
| `LLM_ENABLED` | `false` (or `true` if you set up Bedrock) |

5. Click **Create Web Service**

---

## Step 4 — Verify

| Check | URL |
|-------|-----|
| UI loads | `https://your-service.onrender.com` |
| Health (all green) | `https://your-service.onrender.com/health` |
| Parser Swagger | `https://your-service.onrender.com/docs` |

The `/health` endpoint returns:
```json
{
  "status": "ok",
  "service": "mule-parser",
  "db": "ok",
  "redis": "ok"
}
```

If `db` or `redis` shows `"error"`, check the environment variables and Render logs.

---

## Step 5 — Share with your team

Send only the service URL:
```
https://your-service.onrender.com
```

Each person registers their own account. No VPN needed.

**Cold start tip**: Free-tier services sleep after 15 minutes idle. The first request takes ~60 seconds. The page auto-refreshes.

---

## Local Testing (Render-mirror)

To test the exact Render setup locally before deploying:

```bash
# 1. Fill in your Neon + Upstash credentials
cp deploy/docker/.env.example mule_parser/.env
# edit mule_parser/.env — set DATABASE_URL and REDIS_URL

# 2. Run the single-container Render-mirror compose
docker compose -f deploy/docker/docker-compose.render.yml up --build

# 3. Open http://localhost:8080
```

---

## Optional: Enable LLM (AWS Bedrock)

Add these in the Render dashboard → Environment:

```
LLM_ENABLED=true
CODEGEN_LLM_ENABLED=true
AWS_ACCESS_KEY_ID=...
AWS_SECRET_ACCESS_KEY=...
AWS_DEFAULT_REGION=us-east-2
BEDROCK_MODEL_ID=us.amazon.nova-lite-v1:0
```

Never commit secrets to git.

---

## Optional: Custom Domain

On your Render service → Settings → Custom Domains → add `studio.yourcompany.com`

Then update environment variables:
- `PUBLIC_URL`, `NEXTAUTH_URL`, `FRONTEND_URL` → `https://studio.yourcompany.com`

---

## Troubleshooting

| Problem | Fix |
|---------|-----|
| `/health` shows `db: "error"` | Check `DATABASE_URL` in Render env — ensure `?sslmode=require` is included |
| `/health` shows `redis: "error"` | Check `REDIS_URL` — must start with `rediss://` (double-s = TLS) |
| UI loads but migrations hang | Check Render logs for `prisma migrate deploy` errors |
| "Starting…" forever | Free service waking from sleep — wait 60s and refresh |
| Build fails | Check `frontend/package-lock.json` is committed |
| Celery tasks not running | Confirm `CELERY_BROKER_URL` is set (same as REDIS_URL + `/0`) |
| Monthly suspend | 750 free hours used — wait for month reset or upgrade to Starter ($7/mo) |

---

## Cost Summary

| Resource | Free tier |
|----------|-----------|
| Render Docker service | 750 hrs/mo, sleeps when idle |
| Neon Postgres | 0.5 GB storage, no expiry |
| Upstash Redis | 10,000 commands/day, TLS included |

**Typical demo cost: $0/month** on all three free tiers.
