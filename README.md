# Migration Studio — Split Queue & Cache Infrastructure

This project uses a split architecture to handle background jobs and caching without hitting request limits on metered Redis plans (such as Upstash):

## Architecture Summary
* **Celery Broker**: RabbitMQ (self-hosted).
* **Result Backend**: Disabled (`task_ignore_result = True`) to prevent saving transient task states in memory/cache. All project and file migration states are saved directly to PostgreSQL.
* **Cache & BullMQ**: Local self-hosted Redis (configured as a cache with LRU eviction).
* **Source of Truth**: PostgreSQL (Neon database).

---

## Configuration & Connection Variables

The application services retrieve connection settings from the mounted `.env` file:

```env
# Cache Backend (Redis)
REDIS_URL=redis://localhost:6379/0

# Celery Broker (RabbitMQ)
RABBITMQ_USER=studio_user
RABBITMQ_PASS=studio_secure_password
RABBITMQ_VHOST=studio_vhost
CELERY_BROKER_URL=amqp://studio_user:studio_secure_password@localhost:5672/studio_vhost
```

### Celery configuration details (`mule_parser/api/celery_app.py`):
```python
celery_app = Celery("migration_worker", broker=RABBITMQ_URL)
# Result backend is removed, task results are ignored
```

---

## Health Check and Monitoring
You can monitor the connectivity status of all core components at any time via the health check endpoint:

* **Endpoint**: `GET /health`
* **Status Details**: Probes Neon database, Redis cache, and RabbitMQ Celery Broker.
* **Status Codes**: Returns `200 OK` on success, or `503 Service Unavailable` with degraded details when any component probe fails.
# SAP target reference onboarding

Migration Studio supports an optional SAP Integration Suite reference upload at `/dashboard/sap-onboarding`. A native iFlow ZIP or content package ZIP can be analyzed without requiring an SAP tenant connection. Choose “Skip – Use Standard SAP Compatibility” to continue with the existing built-in SAP generation workflow.

The analyzer reads archive entries without extracting them, validates ZIP paths and expansion limits, parses MANIFEST attributes and BPMN XML, and inventories common scripts, mappings, schemas, and resources. It records SHA-256 digests for resources as internal integrity identifiers. Uploaded scripts and expressions are never run. Credentials are redacted where recognized. Content package integrity metadata may be detected, but SAP's proprietary package hash is not verified or fabricated.

`POST /api/v1/sap/reference/upload` accepts a multipart ZIP and returns an analysis profile. The authenticated Next.js route `/api/sap/reference` stores that profile in the existing PostgreSQL database with the authenticated owner, optional project, and a 30-day expiry; archive bytes and extracted files are not retained. Project owners can retrieve, skip, or delete their reference profile through the same route. Expired rows are pruned as users access this feature. Apply the included Prisma migration with `cd frontend && npx prisma migrate deploy`. `POST /api/v1/sap/compatibility/validate` accepts individual iFlow ZIP files and returns local structural findings; the project onboarding route `/api/sap/compatibility/validate` attaches the owner's reference profile when available and stores the report on that project. SAP exports also receive a post-generation structural compatibility report in their manifest. When at least two distinct reference artifacts agree on a valid `Bundle-Version`, that observed version is used for generated SAP artifact manifests. When at least three reference identifiers show the same supported casing convention, generated iFlow filenames follow that convention; otherwise generated names retain the built-in naming rule. Arbitrary sample identifiers and flow logic are not copied into generated artifacts. Passing local checks does not confirm SAP import, deployment, permissions, or runtime behavior. The readiness API `/api/sap/readiness` derives its status from project files, target selection, stored compatibility findings, connection check, and test deployment status.

`POST /api/v1/sap/tenant/test-connection` tests OAuth authentication, read access to package and artifact APIs, and CSRF retrieval using the existing OData client. The authenticated Next.js route `/api/sap/tenant/test-connection` proxies the request; credentials are held only for the request and are not stored. Configure the same high-entropy, minimum-32-character `SAP_REFERENCE_API_KEY` on the FastAPI service and Next.js server; direct backend calls without it are rejected. Tenant and authorization URLs must use HTTPS SAP BTP `hana.ondemand.com` domains. Connection checks are read-only and deployment permission is always reported as unverified.

An optional test deployment is exposed through `/api/sap/tenant/test-deployment`. It requires both authenticated project ownership and an explicit confirmation phrase in the request. It uses unique `TISSA_TEST_` identifiers and refuses package/artifact collisions. It creates a minimal no-op test iFlow, uploads it individually, triggers deployment, and checks SAP's build/deploy task before querying runtime status; runtime is confirmed only when SAP reports `STARTED`. SAP's OData workflow returns a task ID and exposes `BuildAndDeployStatus` before runtime status ([SAP deployment status flow](https://help.sap.com/docs/integration-suite/sap-integration-suite/get-runtime-status-of-deployed-integration-flow?locale=en-US)). SAP documents design-time package deletion, but this implementation does not issue a DELETE request because the exact cleanup behavior has not been verified against a tenant; the UI warns that the uniquely named package may remain and must be removed manually. Never approve this action for a production tenant without reviewing that limitation.

Native iFlow exports contain an individual artifact archive and manifest. Native content package exports contain `resources.cnt` and nested artifact archives; this analyzer inspects both the package index and nested iFlows. Package index parsing is best-effort and proprietary integrity hashes are only identified as present. Adapter endpoint/authentication values are not emitted; the analyzer records adapter data only when an XML element or resource path makes its type identifiable.

The generated complete-package ZIP remains experimental while SAP integrity-hash compatibility is unresolved. Individual iFlow uploads through the existing OData client remain the preferred multi-iFlow delivery method. Live SAP import and deployment must be verified in the target tenant.
