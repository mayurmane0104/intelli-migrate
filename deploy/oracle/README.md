# Oracle Cloud — deploy everything in one go

Full stack: **PostgreSQL**, **Redis**, **FastAPI parser**, **Celery**, **Next.js UI**, **Fastify migration worker**.

## 1. Create the VM (Oracle Always Free)

1. Sign in at [Oracle Cloud](https://cloud.oracle.com) → **Create VM instance**
2. **Region:** pick a **US** region (e.g. `US East (Ashburn)` or `US West (Phoenix)`) for your US team
3. **Shape:** `VM.Standard.A1.Flex` (Ampere ARM) — Always Free eligible  
   - 4 OCPU, 24 GB RAM recommended for this stack
4. **Image:** Ubuntu 22.04 or 24.04
5. **Networking:** assign a **public IP**
6. **Ingress rules** (Security List / NSG) — allow from `0.0.0.0/0`:
   - TCP **22** (SSH)
   - TCP **3000** (Migration Studio UI)
   - TCP **3001** (Fastify / real-time migration)
   - TCP **8000** (Parser API — optional if only using UI)
   - TCP **80**, **443** (only if using HTTPS profile later)

## 2. SSH into the VM

```bash
ssh ubuntu@YOUR_VM_PUBLIC_IP
```

## 3. Clone the repo

```bash
sudo apt-get update && sudo apt-get install -y git
git clone https://github.com/YOUR_ORG/parsercopy.git
cd parsercopy/deploy/oracle
```

(Use your actual git remote, or `scp -r` the project from your PC.)

## 4. Configure environment

```bash
cp .env.example .env
nano .env
```

Set at minimum:

| Variable | Example | Purpose |
|----------|---------|---------|
| `APP_DOMAIN` | `203.0.113.10` | VM public IP (or `studio.yourcompany.com`) |
| `API_DOMAIN` | `203.0.113.10` | Same IP (or `api.yourcompany.com`) |
| `PARSER_DOMAIN` | `203.0.113.10` | Same IP (or `parser.yourcompany.com`) |
| `PUBLIC_SCHEME` | `http` | Use `https` only with real DNS + Caddy profile |
| `POSTGRES_PASSWORD` | strong random | Database password |
| `NEXTAUTH_SECRET` | output of `openssl rand -hex 32` | Session encryption |

**Important:** `NEXT_PUBLIC_*` URLs are baked in at **build** time. After changing `.env`, rebuild:

```bash
docker compose up -d --build
```

## 5. Deploy everything (one command)

```bash
chmod +x bootstrap.sh
./bootstrap.sh
```

This will:

- Install Docker (if missing)
- Build all images
- Start Postgres, Redis, parser, Celery, Fastify, Next.js
- Run Prisma migrations

## 6. Share with your US team

Send them:

- **UI:** `http://YOUR_VM_IP:3000`
- **API docs (optional):** `http://YOUR_VM_IP:8000/docs`

Each person: **Register** → create org → workspace → project → upload Mule ZIP.

## 7. Optional — HTTPS with a domain

1. Point DNS A records to the VM IP:
   - `studio.yourcompany.com`
   - `api.yourcompany.com`
2. Update `.env`:
   ```
   APP_DOMAIN=studio.yourcompany.com
   API_DOMAIN=api.yourcompany.com
   PARSER_DOMAIN=parser.yourcompany.com
   PUBLIC_SCHEME=https
   ```
3. Rebuild Next.js (public URLs changed):
   ```bash
   docker compose up -d --build
   docker compose --profile https up -d
   ```
4. Share `https://studio.yourcompany.com`

## Useful commands

```bash
# Logs
docker compose logs -f nextjs fastify parser

# Restart after code update
git pull
docker compose up -d --build
docker compose --profile setup run --rm migrate

# Stop everything
docker compose down

# Stop and wipe data (destructive)
docker compose down -v
```

## Resource notes (Always Free)

- ARM VM with 4 OCPU / 24 GB RAM is enough for a small team (5–10 users)
- First `docker compose build` may take 15–25 minutes on ARM
- Keep LLM disabled in `.env` for zero AI cost; enable AWS Bedrock keys only if needed

## Security checklist

- Change default passwords in `.env`
- Restrict Oracle ingress to your office IPs if possible (instead of `0.0.0.0/0`)
- Do not commit `.env` or files containing AWS keys
- For production, add HTTPS and consider Cloudflare Access in front of the UI
