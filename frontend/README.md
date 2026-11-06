# Migration Studio — Comprehensive Documentation

> **AI-Powered MuleSoft-to-AWS Code Migration Platform**
>
> Version 0.1.0 · Built with Next.js 16, Fastify, Prisma, BullMQ & Socket.IO

---

## Table of Contents

1. [Product Overview](#1-product-overview)
2. [System Architecture](#2-system-architecture)
3. [Technology Stack](#3-technology-stack)
4. [Database Schema](#4-database-schema)
5. [Functional Modules](#5-functional-modules)
   - [5.1 Authentication & Authorization](#51-authentication--authorization)
   - [5.2 Organizations, Workspaces & Projects](#52-organizations-workspaces--projects)
   - [5.3 Code Import (Git / ZIP)](#53-code-import-git--zip)
   - [5.4 AI-Powered Migration Engine](#54-ai-powered-migration-engine)
   - [5.5 Code Editor & Diff Viewer](#55-code-editor--diff-viewer)
   - [5.6 Migration Logs & History](#56-migration-logs--history)
   - [5.7 Export & Deployment](#57-export--deployment)
   - [5.8 LLM Settings Management](#58-llm-settings-management)
6. [API Reference](#6-api-reference)
7. [Real-Time Event System](#7-real-time-event-system)
8. [LLM Provider Details](#8-llm-provider-details)
9. [Local Development Setup](#9-local-development-setup)
10. [Production Deployment Guide](#10-production-deployment-guide)
11. [Testing](#11-testing)
12. [Troubleshooting](#12-troubleshooting)

---

## 1. Product Overview

**Migration Studio** is a full-stack web application that automates the migration of **MuleSoft** integration projects to **AWS serverless** architectures. It leverages Large Language Models (LLMs) to analyze MuleSoft source code (XML flows, DataWeave scripts, RAML specs) and generate production-ready AWS Lambda handlers, CDK infrastructure code, and comprehensive migration reports.

### Key Capabilities

| Capability | Description |
|---|---|
| **Multi-LLM Support** | Switch between Claude, GPT-4o, Gemini, or a built-in Mock provider |
| **Streaming Migration** | Real-time token-by-token streaming of LLM output via Socket.IO |
| **Batch Processing** | Migrate entire projects with BullMQ job queues (start, stop, resume, retry) |
| **Multiple Migration Types** | Mule 3→Lambda, Mule 4→Lambda, API-Led→API Gateway, Batch→Step Functions |
| **Multiple Target Runtimes** | Node.js 20.x (TypeScript), Python 3.12, Java 21 |
| **Code Import** | Import source code from Git repositories or ZIP file uploads |
| **Monaco Code Editor** | Full-featured in-browser editor with syntax highlighting |
| **Side-by-Side Diff** | Compare original MuleSoft vs. migrated AWS code |
| **Migration History** | Per-file versioned migration records with prompt/response audit trail |
| **Export** | Download migrated code as ZIP, CloudFormation, Terraform, or SAM |
| **Multi-Tenant** | Organization → Workspace → Project hierarchy |

---

## 2. System Architecture

```mermaid
block-beta
  columns 3

  Browser["Browser Client\nNext.js 16 React App · Monaco Editor · Socket.IO Client"]:3

  space:3

  NextJS["Next.js API Routes\n(Port 3000)\n/api/auth · /api/organizations\n/api/workspaces · /api/projects\n/api/files · /api/import\n/api/export · /api/migration\n/api/settings"]:1
  space:1
  Fastify["Fastify Server (Port 3001)\nSocket.IO Server\nBullMQ Worker\n(Migration Jobs)"]:1

  space:3

  PostgreSQL[("PostgreSQL\n(Prisma ORM)")]:1
  Redis[("Redis\n(Port 6379)")]:1
  LLM["LLM APIs\nClaude / GPT / Gemini"]:1

  Browser -- "HTTP REST" --> NextJS
  Browser -- "WebSocket" --> Fastify
  NextJS --> PostgreSQL
  Fastify --> PostgreSQL
  Fastify --> Redis
  Fastify --> LLM
```

### Two-Server Architecture

| Server | Port | Purpose |
|--------|------|---------|
| **Next.js App** | `3000` | Frontend React app + REST API routes for CRUD operations |
| **Fastify Server** | `3001` | Real-time migration engine — BullMQ worker, Socket.IO, LLM streaming |

The Next.js server handles all CRUD operations (orgs, workspaces, projects, files, settings) and authentication. The Fastify server handles long-running migration jobs with queue management and real-time token streaming.

---

## 3. Technology Stack

### Frontend
| Technology | Purpose |
|---|---|
| **Next.js 16** | React meta-framework (App Router, SSR) |
| **React 19** | UI components |
| **Zustand** | Client-side state management |
| **Monaco Editor** | In-browser code editing (`@monaco-editor/react`) |
| **Framer Motion** | Animations and transitions |
| **Tailwind CSS 4** | Utility-first CSS framework |
| **Primer React** | GitHub-style UI component library |
| **Recharts** | Data visualisation (charts/graphs) |
| **Socket.IO Client** | Real-time communication with Fastify server |
| **Axios** | HTTP client for API calls |

### Backend
| Technology | Purpose |
|---|---|
| **Next.js API Routes** | RESTful API for CRUD operations |
| **Fastify** | High-performance server for migration engine |
| **Prisma ORM** | Database access and migrations (PostgreSQL) |
| **BullMQ** | Redis-backed job queue for migration tasks |
| **Socket.IO** | WebSocket server for real-time token streaming |
| **ioredis** | Redis client for BullMQ connections |

### Infrastructure & Services
| Technology | Purpose |
|---|---|
| **PostgreSQL** | Primary relational database |
| **Redis** | Job queue backend (BullMQ) |
| **NextAuth.js** | Authentication (credentials + OAuth) |
| **Clerk** | Alternative authentication provider |
| **bcryptjs** | Password hashing |
| **JSZip** | ZIP file import/export handling |

### AI / LLM
| Provider | Default Model | Status |
|---|---|---|
| **Mock** | `local-simulation` | Built-in (no API key needed) |
| **Anthropic Claude** | `claude-3-5-sonnet-20241022` | Production |
| **OpenAI** | `gpt-4o` | Production |
| **Google Gemini** | `gemini-2.5-flash` | Production |

### Testing
| Tool | Type |
|---|---|
| **Vitest** | Unit tests (jsdom environment) |
| **Playwright** | End-to-end browser tests |
| **Testing Library** | React component tests |

---

## 4. Database Schema

The application uses **PostgreSQL** with **Prisma ORM**. The schema follows a hierarchical multi-tenant model.

### Entity Relationship

```
User
 ├── Organization (one:many)
 │    └── Workspace (one:many)
 │         └── Project (one:many)
 │              ├── ProjectFile (one:many)
 │              │    └── MigrationRecord (one:many)
 │              ├── MigrationLog (one:many)
 │              └── MigrationBatch (one:many)
 ├── Account (one:many, OAuth)
 ├── Session (one:many)
 └── UserSettings (one:one)
```

### Core Models

#### User
| Field | Type | Description |
|---|---|---|
| `id` | String (CUID) | Primary key |
| `name` | String? | Display name |
| `email` | String (unique) | Login email |
| `password` | String? | Hashed password (credentials provider) |
| `role` | String | `admin` \| `developer` \| `viewer` |

#### Organization
| Field | Type | Description |
|---|---|---|
| `id` | String (CUID) | Primary key |
| `userId` | String (FK) | Owner user |
| `name` | String (unique) | Organization name |
| `description` | String | Description |
| `owner` | String | Display name of owner |
| `logo` | String | Logo URL |

#### Workspace
| Field | Type | Description |
|---|---|---|
| `id` | String (CUID) | Primary key |
| `orgId` | String (FK) | Parent organization |
| `name` | String | Workspace name (unique per org) |
| `environment` | String | `dev` \| `test` \| `prod` |
| `memberCount` | Int | Number of members |

#### Project
| Field | Type | Description |
|---|---|---|
| `id` | String (CUID) | Primary key |
| `workspaceId` | String (FK) | Parent workspace |
| `orgId` | String (FK) | Parent organization |
| `name` | String | Project name |
| `migrationType` | String | `mule3-lambda` \| `mule4-lambda` \| `apiled-apigateway` \| `batch-stepfunction` |
| `targetRuntime` | String | `nodejs` \| `python` \| `java` |
| `sourceType` | String | `git` \| `zip` |
| `status` | String | `pending` \| `in-progress` \| `completed` \| `failed` |
| `totalFiles` | Int | Total file count |
| `migratedFiles` | Int | Successfully migrated files |
| `failedFiles` | Int | Failed migrations |
| `migrationRuns` | Int | Number of migration runs |

#### ProjectFile
| Field | Type | Description |
|---|---|---|
| `id` | String (CUID) | Primary key |
| `projectId` | String (FK) | Parent project |
| `name` | String | File name |
| `path` | String | Full file path |
| `type` | String | `file` \| `folder` |
| `language` | String? | Detected programming language |
| `status` | String | `pending` \| `in-progress` \| `completed` \| `failed` |
| `content` | Text | Base64-encoded source content |
| `migratedContent` | Text? | Base64-encoded migration report (Markdown) |
| `migratedCode` | Text? | Base64-encoded extracted clean code |
| `activeMigrationId` | String? | Current batch/session ID |

#### MigrationRecord
| Field | Type | Description |
|---|---|---|
| `id` | String (CUID) | Primary key |
| `fileId` | String (FK) | Associated file |
| `provider` | String | LLM provider used (e.g., `claude`, `mock`) |
| `model` | String | Specific model (e.g., `claude-3-5-sonnet-20241022`) |
| `content` | Text | Base64-encoded full migration report |
| `code` | Text? | Base64-encoded extracted code |
| `systemPrompt` | Text? | Base64-encoded system prompt sent to LLM |
| `userPrompt` | Text? | Base64-encoded user prompt sent to LLM |
| `rawResponse` | Text? | Base64-encoded raw LLM response |
| `tokens` | Int | Estimated token count |

#### MigrationBatch
| Field | Type | Description |
|---|---|---|
| `id` | String (CUID) | Primary key / Session ID |
| `projectId` | String (FK) | Associated project |
| `provider` | String | LLM provider |
| `model` | String | LLM model |
| `status` | String | `running` \| `completed` \| `partial` \| `stopped` |
| `totalFiles` | Int | Files in batch |
| `completedFiles` | Int | Successfully completed |
| `failedFiles` | Int | Failed count |
| `totalTokens` | Int | Cumulative tokens |
| `triggeredById` | String | User who started the batch |
| `fileResults` | JSON | Array of per-file results |

#### MigrationLog
| Field | Type | Description |
|---|---|---|
| `id` | String (CUID) | Primary key |
| `projectId` | String (FK) | Associated project |
| `fileName` | String | Name of the file |
| `status` | String | `success` \| `error` \| `warning` \| `info` |
| `message` | Text | Log message |
| `stackTrace` | Text? | Error stack trace |
| `duration` | Int? | Duration in milliseconds |

---

## 5. Functional Modules

### 5.1 Authentication & Authorization

**Implementation:** NextAuth.js with Prisma Adapter

| Feature | Route | Description |
|---|---|---|
| Email/Password Login | `POST /api/auth/login` | Validates credentials using bcrypt |
| User Registration | `POST /api/auth/register` | Creates user with hashed password |
| Logout | `POST /api/auth/logout` | Ends session |
| Session Check | `GET /api/auth/me` | Returns current user info |
| Password Update | `PUT /api/auth/me/password` | Change password (requires current) |
| Profile Update | `PUT /api/auth/me` | Update display name, avatar, etc. |
| OAuth | NextAuth providers | Google, Apple (configurable) |

**Middleware Protection:**
- All `/dashboard/*` routes require authentication
- Unauthenticated users are redirected to `/login`
- Authenticated users accessing `/login` or `/register` are redirected to `/dashboard/organizations`
- Protected pages set no-cache headers to prevent back-button issues after logout

**Role-Based Access:**
- Roles: `admin`, `developer`, `viewer`
- Enforced via `RoleGuard` component on the frontend

### 5.2 Organizations, Workspaces & Projects

The platform uses a three-level hierarchy for multi-tenancy:

```
Organization (e.g., "Acme Corporation")
  └── Workspace (e.g., "Development", environment: dev/test/prod)
       └── Project (e.g., "Payment API Migration")
            └── Files (imported MuleSoft source code)
```

**Workflow:**
1. **Create Organization** — top-level tenant container
2. **Create Workspace** — within an org, environment-specific (dev/test/prod)
3. **Create Project** — within a workspace, configured with:
   - **Migration Type**: `mule3-lambda` | `mule4-lambda` | `apiled-apigateway` | `batch-stepfunction`
   - **Target Runtime**: `nodejs` | `python` | `java`
   - **Source Type**: `git` | `zip`
4. **Import Code** — Git clone or ZIP upload into the project
5. **Run Migration** — AI processes each file

**Dashboard Pages:**
| Page | Route | Description |
|---|---|---|
| Organizations | `/dashboard/organizations` | List/create organizations |
| Workspaces | `/dashboard/workspaces` | List/create workspaces per org |
| Projects | `/dashboard/projects` | List/create/manage projects |
| Settings | `/dashboard/settings` | LLM provider configuration |
| Profile | `/dashboard/profile` | User profile management |
| Help | `/dashboard/help` | Documentation/help center |

### 5.3 Code Import (Git / ZIP)

**Git Import:**
1. User enters a Git repository URL
2. **Connection Test** (`GET /api/import/git?repoUrl=...`) — validates repo accessibility, returns metadata (name, description, stars, default branch, file count)
3. **Import** (`POST /api/import/git`) — clones repository and ingests files into the database
4. Supports: branch selection, authentication tokens, sub-path filtering

**ZIP Import:**
1. User uploads a `.zip` file via drag-and-drop or file picker
2. **Upload** (`POST /api/import/zip`) — server extracts the archive using JSZip
3. Files are stored as base64-encoded blobs in `ProjectFile` records

**Import Components:**
- `ImportPanel.tsx` — orchestrates the import workflow
- `GitImport.tsx` — Git-specific connection form
- `ZipUpload.tsx` — ZIP drag-and-drop uploader

### 5.4 AI-Powered Migration Engine

This is the core of the platform — the end-to-end flow of migrating a file:

**Flow Diagram:**
```mermaid
sequenceDiagram
    actor User
    participant UI as Browser UI
    participant Fastify as Fastify Server :3001
    participant Queue as BullMQ Queue
    participant Worker as BullMQ Worker
    participant DB as PostgreSQL
    participant LLM as LLM API
    participant WS as Socket.IO

    User->>UI: Clicks "Migrate"
    UI->>Fastify: POST /api/projects/:id/migrate
    Fastify->>DB: Check CONCURRENCY_LOCK
    Fastify->>DB: Create MigrationBatch
    Fastify->>DB: Reset file statuses to pending

    loop For each fileId
        Fastify->>Queue: Add migration-job
    end

    Fastify-->>UI: {success, jobs[], migrationId}

    loop Process jobs (concurrency: 1)
        Queue->>Worker: Dequeue job
        Worker->>DB: 1. Fetch file content
        Worker->>Worker: 2. Decode base64 content
        Worker->>DB: 3. Fetch project file tree
        Worker->>Worker: 4. Build system + user prompts
        Worker->>DB: 5. Create MigrationRecord (early)
        Worker->>DB: Mark file status: in-progress

        Worker->>LLM: 6. Stream migration request
        loop Token-by-token streaming
            LLM-->>Worker: token
            Worker->>WS: jobEvents.emit(token)
            WS-->>UI: job:token event
        end

        Worker->>Worker: 7. Extract [PRIMARY_CODE_BLOCK]
        Worker->>DB: 8. Update ProjectFile (completed)
        Worker->>DB: 9. Update MigrationRecord (rawResponse)
        Worker->>DB: 10. Update MigrationBatch (stats)
        Worker->>WS: job:completed event
        WS-->>UI: job:completed
    end
```

**Concurrency Control:**
- Only one migration session per user at a time
- Enforced via `CONCURRENCY_LOCK` — checks for active `MigrationBatch` before starting new batch
- Returns HTTP 409 if a batch is already running

**Batch Operations:**
| Operation | API | Description |
|---|---|---|
| Start | `POST /api/projects/:id/migrate` | Queue all selected files |
| Stop | `POST /api/projects/:id/stop` | Remove waiting/active jobs, mark batch as stopped |
| Resume | `POST /api/projects/:id/resume` | Re-queue pending/failed files |
| Retry File | `POST /api/projects/:id/retry-file` | Re-queue a single failed file |
| Active Batch | `GET /api/projects/:id/active-batch` | Check if a batch is in progress |

**Prompt Engineering:**
The system uses structured, runtime-aware prompts:
- **System Prompt**: Defines the LLM role ("expert MuleSoft-to-AWS migration architect"), includes migration context table (source version, target service, runtime, SDK, naming conventions), and specifies exact Markdown report structure
- **User Prompt**: Includes file metadata, project file tree for context, and the actual source code
- **Instruction Files** (`src/lib/prompts/`): Additional domain knowledge injected from Markdown files:
  - `architecture.md` — core service mappings (Mule→AWS)
  - `runtime.md` — Node.js best practices, `[PRIMARY_CODE_BLOCK]` extraction
  - `logic.md` — DataWeave-to-JavaScript/Python conversion patterns

**Migration Report Output (per file):**
1. Executive Summary
2. MuleSoft Flow Analysis
3. AWS Architecture Mapping (component table)
4. AWS CDK Code (infrastructure-as-code)
5. Lambda Handler Code (production-ready, wrapped in `[PRIMARY_CODE_BLOCK]`)
6. DataWeave Conversion
7. Migration Checklist
8. Risks and Recommendations

### 5.5 Code Editor & Diff Viewer

**Components:**
- `CodeEditor.tsx` — Monaco Editor integration for viewing/editing source and migrated code
- `DiffViewer.tsx` — Side-by-side comparison of original (left) vs. migrated (right) code
- `FileTree.tsx` — Hierarchical file browser with status indicators (pending/in-progress/completed/failed)
- `LiveStreamPanel.tsx` — Real-time display of streaming LLM output
- `MigrationPanel.tsx` — Controls: start/stop migration, select files, choose provider/model

**Features:**
- Syntax highlighting for XML, DataWeave, RAML, TypeScript, Python, Java
- File status badges (colored indicators per file)
- Resizable panels via `ResizablePanels.tsx`
- Dark/light theme support via `next-themes`

### 5.6 Migration Logs & History

**Migration Logs:** (`MigrationLog` model)
- Per-event log entries with severity levels: `success`, `error`, `warning`, `info`
- Stack traces captured for failures
- Duration tracking per file migration
- Components: `LogViewer.tsx`, `MigrationLogs.tsx`

**Migration History:** (`MigrationRecord` model)
- Per-file versioned history of every migration attempt
- Stores: provider, model, full content, extracted code, system prompt, user prompt, raw response
- Allows switching between migration versions per file
- Component: `MigrationHistory.tsx`

**Batch History:** (`MigrationBatch` model)
- Per-project batch records with aggregate stats
- Tracks: who triggered, total/completed/failed files, total tokens
- Component: `JobTracker.tsx` — real-time batch progress tracker

### 5.7 Export & Deployment

**Export Formats:**
| Format | Description |
|---|---|
| **ZIP** | Download migrated code as a ZIP archive |
| **CloudFormation** | AWS CloudFormation template |
| **Terraform** | HashiCorp Terraform configuration |
| **SAM** | AWS Serverless Application Model |

**Export API:**
| Method | Endpoint | Description |
|---|---|---|
| `POST` | `/api/export/download` | Generate download for project |
| `POST` | `/api/export/push` | Push to remote repository |

**Component:** `ExportPanel.tsx` — full export workflow UI

### 5.8 LLM Settings Management

**Configuration per user** (stored in `UserSettings` model):
- Active provider selection (mock/claude/openai/gemini)
- Per-provider: API key, model, enabled flag
- Editor settings (theme, font size, last model)

**API:**
| Method | Endpoint | Description |
|---|---|---|
| `GET` | `/api/settings/llm` | Fetch settings (API keys masked) |
| `GET` | `/api/settings/llm?reveal=true` | Fetch settings (API keys visible) |
| `PUT` | `/api/settings/llm` | Save settings |
| `POST` | `/api/settings/llm/test` | Test provider connection |

**Available Models per Provider:**
| Provider | Models |
|---|---|
| Claude | claude-3-5-sonnet-20241022, claude-3-5-haiku-20241022, claude-3-opus-20240229 |
| OpenAI | gpt-4o, gpt-4o-mini, o3-mini |
| Gemini | gemini-2.5-flash, gemini-2.5-pro, gemini-2.0-flash |

---

## 6. API Reference

### Auth Routes
| Method | Endpoint | Body/Params | Response |
|---|---|---|---|
| `POST` | `/api/auth/login` | `{email, password}` | `{user}` |
| `POST` | `/api/auth/register` | `{name, email, password}` | `{user}` |
| `POST` | `/api/auth/logout` | — | `{success}` |
| `GET` | `/api/auth/me` | — | `{user}` |
| `PUT` | `/api/auth/me` | `Partial<User>` | `{user}` |
| `PUT` | `/api/auth/me/password` | `{currentPassword, newPassword}` | `{success}` |

### Organization Routes
| Method | Endpoint | Body/Params | Response |
|---|---|---|---|
| `GET` | `/api/organizations` | — | `{organizations[]}` |
| `POST` | `/api/organizations` | `{name, description, owner, logo}` | `{organization}` |
| `GET` | `/api/organizations/:orgId` | — | `{organization}` |

### Workspace Routes
| Method | Endpoint | Body/Params | Response |
|---|---|---|---|
| `GET` | `/api/workspaces?orgId=` | query: `orgId` | `{workspaces[]}` |
| `POST` | `/api/workspaces` | `{orgId, name, environment, memberCount}` | `{workspace}` |
| `GET` | `/api/workspaces/:wsId` | — | `{workspace}` |

### Project Routes
| Method | Endpoint | Body/Params | Response |
|---|---|---|---|
| `GET` | `/api/projects?workspaceId=` | query: `workspaceId` | `{projects[]}` |
| `POST` | `/api/projects` | `{workspaceId, orgId, name, description, migrationType, targetRuntime, sourceType}` | `{project}` |
| `GET` | `/api/projects/:projectId` | — | `{project}` |
| `PUT` | `/api/projects/:projectId` | `Partial<Project>` | `{project}` |

### File Routes
| Method | Endpoint | Body/Params | Response |
|---|---|---|---|
| `GET` | `/api/files?projectId=` | query: `projectId` | `{files[]}` |
| `GET` | `/api/files/:fileId` | — | `{file}` |
| `PUT` | `/api/files/:fileId` | `Partial<ProjectFile>` | `{file}` |

### Import Routes
| Method | Endpoint | Body/Params | Response |
|---|---|---|---|
| `GET` | `/api/import/git?repoUrl=&branch=&token=` | query params | Repo metadata |
| `POST` | `/api/import/git` | `{repoUrl, projectId, branch?, token?, subPath?}` | `{success, filesImported, repoName}` |
| `POST` | `/api/import/zip` | `FormData: file + projectId` | `{success, filesExtracted}` |

### Migration Routes (Next.js)
| Method | Endpoint | Body/Params | Response |
|---|---|---|---|
| `POST` | `/api/migration/start` | `{projectId}` | `{session}` |
| `POST` | `/api/migration/stop` | `{projectId}` | `{success}` |
| `GET` | `/api/migration/status?projectId=` | — | `MigrationStatus` |
| `POST` | `/api/migration/file` | `{fileId}` | `{status, migratedContent, log}` |
| `POST` | `/api/migration/retry` | `{projectId}` | `{retriedCount}` |
| `GET` | `/api/migration/logs?projectId=` | — | `{logs[]}` |
| `DELETE` | `/api/migration/logs?projectId=` | — | `{success}` |
| `GET` | `/api/migration/batches?projectId=` | — | `{batches[]}` |

### Migration Routes (Fastify :3001)
| Method | Endpoint | Body/Params | Response |
|---|---|---|---|
| `POST` | `/api/projects/:id/migrate` | `{fileIds, config, llmSettings, migrationId?}` | `{success, jobs[], migrationId}` |
| `POST` | `/api/projects/:id/stop` | `{migrationId?}` | `{success, stoppedCount}` |
| `POST` | `/api/projects/:id/resume` | `{migrationId, llmSettings}` | `{success, jobs[], migrationId}` |
| `POST` | `/api/projects/:id/retry-file` | `{fileId, migrationId, config, llmSettings}` | `{success, jobId}` |
| `GET` | `/api/projects/:id/active-batch` | — | `{success, batch}` |
| `GET` | `/api/projects/:id/files` | — | `{success, files[]}` (with migrations) |

### Export Routes
| Method | Endpoint | Body/Params | Response |
|---|---|---|---|
| `POST` | `/api/export/download` | `{projectId, format}` | `{success, downloadUrl}` |
| `POST` | `/api/export/push` | `{projectId, target, repoUrl?, branch?}` | `{success, message}` |

### Settings Routes
| Method | Endpoint | Body/Params | Response |
|---|---|---|---|
| `GET` | `/api/settings/llm` | query: `?reveal=true` (optional) | `{settings}` |
| `PUT` | `/api/settings/llm` | `{settings: Partial<LLMSettings>}` | `{settings, saved}` |
| `POST` | `/api/settings/llm/test` | `{provider, apiKey?, model?}` | `{success, message}` |

---

## 7. Real-Time Event System

Socket.IO events bridge the Fastify server to the browser for live migration feedback.

### Connection Flow
```
Browser → socket.connect('http://localhost:3001')
Browser → socket.emit('join:project', projectId)
         → Server joins socket to room "project:{projectId}"
```

### Server-to-Client Events
| Event | Payload | Trigger |
|---|---|---|
| `job:progress` | `{jobId, fileId, progress}` | BullMQ worker progress update |
| `job:token` | `{jobId, token}` | Each streamed LLM token |
| `job:completed` | `{jobId, fileId, result}` | Job finishes successfully |
| `job:failed` | `{jobId, fileId, error}` | Job fails |
| `migration:stopped` | `{projectId, migrationId}` | Batch stopped by user |

### Internal Event Bridge
`jobEvents` (Node.js `EventEmitter`) bridges BullMQ worker → Socket.IO server:
- Worker emits `token` events on `jobEvents`
- Fastify server listens and forwards to the correct Socket.IO room

---

## 8. LLM Provider Details

### Provider Architecture

All providers implement the `LLMProvider` interface:
```typescript
interface LLMProvider {
    name: string;
    model?: string;
    streamMigration(sourceContent: string, config: MigrationConfig): AsyncGenerator<string>;
    testConnection(): Promise<{ success: boolean; message: string }>;
}
```

### Factory Pattern
`createLLMProvider(settings)` — selects provider based on `LLMSettings.activeProvider`:
- If no settings or `mock` → `MockLLMProvider`
- If provider config missing API key or disabled → fallback to `MockLLMProvider`
- Otherwise → instantiates the appropriate provider class

### Provider Details

| Provider | API Endpoint | Auth Header | Streaming Format |
|---|---|---|---|
| **Mock** | — | — | Simulated token-by-token delay |
| **Claude** | `api.anthropic.com/v1/messages` | `x-api-key` | SSE: `content_block_delta` |
| **OpenAI** | `api.openai.com/v1/chat/completions` | `Authorization: Bearer` | SSE: `choices[0].delta.content` |
| **Gemini** | `generativelanguage.googleapis.com/v1beta` | Query param `key=` | SSE: `candidates[0].content.parts[0].text` |

### Code Extraction
After the LLM produces a full Markdown report, the `extractPrimaryCode()` function:
1. Looks for `[PRIMARY_CODE_BLOCK]` / `[/PRIMARY_CODE_BLOCK]` markers
2. Extracts the fenced code block within those markers
3. Falls back to selecting the longest code block if markers are absent

---

## 9. Local Development Setup

### Prerequisites

| Requirement | Version | Installation |
|---|---|---|
| **Node.js** | ≥ 20.x LTS | [nodejs.org](https://nodejs.org) |
| **npm** or **bun** | Latest | Comes with Node.js / [bun.sh](https://bun.sh) |
| **PostgreSQL** | ≥ 15 | [postgresql.org](https://www.postgresql.org/download/) |
| **Redis** | ≥ 7 | [redis.io](https://redis.io) or via Docker |
| **Git** | Latest | [git-scm.com](https://git-scm.com) |

### Step-by-Step Setup

#### Step 1: Clone the Repository
```bash
git clone <your-repo-url>
cd AnyCodeStudio/migration-studio
```

#### Step 2: Install Dependencies
```bash
npm install
# or
bun install
```

#### Step 3: Configure Environment Variables
Copy the example env file and fill in your values:
```bash
cp .env.example .env
```

Edit `.env` with the following required variables:

```env
# ── Database ──
DATABASE_URL="postgresql://postgres:YOUR_PASSWORD@localhost:5432/migration_studio"

# ── Redis (required for BullMQ migration queue) ──
REDIS_URL="redis://localhost:6379"

# ── URLs ──
NEXT_PUBLIC_APP_URL="http://localhost:3000"
NEXT_PUBLIC_API_URL="http://localhost:3001"
FRONTEND_URL="http://localhost:3000"

# ── NextAuth (required) ──
NEXTAUTH_URL="http://localhost:3000"
NEXTAUTH_SECRET="generate-a-32-char-random-string-here"

# ── OAuth (optional) ──
GOOGLE_CLIENT_ID=""
GOOGLE_CLIENT_SECRET=""

# ── AI Providers (all optional — Mock works by default) ──
ANTHROPIC_API_KEY=""
ANTHROPIC_MODEL="claude-sonnet-4-20250514"
```

> **Generate NEXTAUTH_SECRET:** Run `openssl rand -hex 32` to generate a secure secret.

#### Step 4: Set Up PostgreSQL Database
```bash
# Create the database
psql -U postgres -c "CREATE DATABASE migration_studio;"

# Run Prisma migrations to create all tables
npx prisma migrate deploy

# Generate Prisma client
npx prisma generate
```

#### Step 5: Start Redis
```bash
# Using Docker (recommended on Windows):
docker run -d --name redis -p 6379:6379 redis:7

# Or if installed natively:
redis-server
```

#### Step 6: Seed Demo Data (Optional)
```bash
npx tsx seed-demo.ts
```
This creates a demo user, organization, workspace, project, and sample MuleSoft files.

#### Step 7: Start the Application

You need **two terminals** running simultaneously:

**Terminal 1 — Next.js Frontend + API (port 3000):**
```bash
npm run dev
```

**Terminal 2 — Fastify Migration Server (port 3001):**
```bash
npm run dev:server
```

#### Step 8: Open the Application
Navigate to **http://localhost:3000** in your browser.

> **Quick Start:** The mock LLM provider works out of the box without any API keys. To use real AI providers, configure API keys in **Dashboard → Settings → LLM Providers**.

### Verification Checklist

| Check | Expected Result |
|---|---|
| `http://localhost:3000` | Login page loads |
| `http://localhost:3001` | Fastify server responds |
| Register a new account | User created successfully |
| Create Org → Workspace → Project | All saved to PostgreSQL |
| Import files (ZIP or Git) | Files appear in file tree |
| Run migration (Mock provider) | Streaming output in real-time |
| View diff (source vs. migrated) | Side-by-side comparison works |

---

## 10. Production Deployment Guide

### Recommended Infrastructure

```mermaid
block-beta
  columns 2

  LB["Load Balancer\n(ALB / NGINX)"]:2

  NextJS["Next.js App\n(Port 3000)\nVercel / Docker"]
  Fastify["Fastify Server\n(Port 3001)\nEC2 / ECS / GKE / Docker"]

  PostgreSQL[("PostgreSQL\nRDS / Cloud SQL")]
  Redis[("Redis (Managed)\nElastiCache / Redis Cloud")]

  LB --> NextJS
  LB --> Fastify
  NextJS --> PostgreSQL
  Fastify --> PostgreSQL
  Fastify --> Redis
```

### Option A: Vercel + Separate Backend

**Best for:** Quick deployment with managed Next.js hosting.

#### Step 1: Deploy Next.js to Vercel
```bash
# Install Vercel CLI
npm i -g vercel

# Deploy
vercel --prod
```

**Vercel Environment Variables:**
```
DATABASE_URL=postgresql://user:pass@your-rds-endpoint:5432/migration_studio
NEXTAUTH_URL=https://your-domain.com
NEXTAUTH_SECRET=<production-secret>
NEXT_PUBLIC_APP_URL=https://your-domain.com
NEXT_PUBLIC_API_URL=https://api.your-domain.com
```

#### Step 2: Deploy Fastify Server to AWS EC2 / ECS

**Dockerfile for Fastify Server:**
```dockerfile
FROM node:20-alpine AS builder
WORKDIR /app
COPY package*.json ./
RUN npm ci --production=false
COPY . .
RUN npx prisma generate
RUN npm run build

FROM node:20-alpine
WORKDIR /app
COPY --from=builder /app/node_modules ./node_modules
COPY --from=builder /app/dist ./dist
COPY --from=builder /app/prisma ./prisma
COPY --from=builder /app/src/lib/prompts ./src/lib/prompts
COPY --from=builder /app/package.json ./

ENV NODE_ENV=production
EXPOSE 3001
CMD ["node", "dist/server/app.js"]
```

**Environment Variables for Fastify:**
```
DATABASE_URL=postgresql://user:pass@your-rds-endpoint:5432/migration_studio
REDIS_URL=redis://your-elasticache-endpoint:6379
FRONTEND_URL=https://your-domain.com
```

#### Step 3: Set Up Managed PostgreSQL
- **AWS:** Amazon RDS (PostgreSQL 15+)
- **Google Cloud:** Cloud SQL
- **Alternative:** Supabase, Neon, PlanetScale

```bash
# Run migrations on production database
DATABASE_URL="postgresql://..." npx prisma migrate deploy
```

#### Step 4: Set Up Managed Redis
- **AWS:** ElastiCache for Redis
- **Google Cloud:** Memorystore for Redis
- **Alternative:** Upstash, Redis Cloud

### Option B: Full Docker Compose

**For self-hosted deployments:**

```yaml
# docker-compose.yml
version: '3.8'

services:
  postgres:
    image: postgres:15-alpine
    environment:
      POSTGRES_USER: postgres
      POSTGRES_PASSWORD: ${DB_PASSWORD}
      POSTGRES_DB: migration_studio
    ports:
      - "5432:5432"
    volumes:
      - pgdata:/var/lib/postgresql/data
    healthcheck:
      test: ["CMD-SHELL", "pg_isready -U postgres"]
      interval: 5s
      timeout: 5s
      retries: 5

  redis:
    image: redis:7-alpine
    ports:
      - "6379:6379"
    volumes:
      - redisdata:/data
    healthcheck:
      test: ["CMD", "redis-cli", "ping"]
      interval: 5s
      timeout: 5s
      retries: 5

  nextjs:
    build:
      context: .
      dockerfile: Dockerfile.nextjs
    ports:
      - "3000:3000"
    environment:
      DATABASE_URL: postgresql://postgres:${DB_PASSWORD}@postgres:5432/migration_studio
      REDIS_URL: redis://redis:6379
      NEXTAUTH_URL: ${APP_URL}
      NEXTAUTH_SECRET: ${NEXTAUTH_SECRET}
      NEXT_PUBLIC_APP_URL: ${APP_URL}
      NEXT_PUBLIC_API_URL: ${API_URL}
    depends_on:
      postgres:
        condition: service_healthy
      redis:
        condition: service_healthy

  fastify:
    build:
      context: .
      dockerfile: Dockerfile.fastify
    ports:
      - "3001:3001"
    environment:
      DATABASE_URL: postgresql://postgres:${DB_PASSWORD}@postgres:5432/migration_studio
      REDIS_URL: redis://redis:6379
      FRONTEND_URL: ${APP_URL}
    depends_on:
      postgres:
        condition: service_healthy
      redis:
        condition: service_healthy

volumes:
  pgdata:
  redisdata:
```

**Deploy:**
```bash
# Set environment
export DB_PASSWORD=your-secure-password
export NEXTAUTH_SECRET=$(openssl rand -hex 32)
export APP_URL=https://your-domain.com
export API_URL=https://api.your-domain.com

# Build and start
docker compose up -d --build

# Run migrations
docker compose exec nextjs npx prisma migrate deploy
```

### Option C: AWS ECS / Fargate

1. **Push Docker images** to Amazon ECR
2. **Create ECS Cluster** with Fargate launch type
3. **Create two Task Definitions**: one for Next.js, one for Fastify
4. **Create two Services** with Application Load Balancer
5. **Configure ALB** routing:
   - `your-domain.com` → Next.js service (port 3000)
   - `api.your-domain.com` → Fastify service (port 3001)
6. **Set up RDS** (PostgreSQL) and **ElastiCache** (Redis)

### Production Checklist

| Item | Status | Notes |
|---|---|---|
| SSL/TLS certificates | Required | Use ACM (AWS), Let's Encrypt, or Cloudflare |
| Environment variables | Required | Never commit `.env` to git |
| Database migrations | Required | `npx prisma migrate deploy` |
| Redis persistence | Recommended | Enable AOF or RDB snapshots |
| CORS configuration | Required | Update `FRONTEND_URL` to production domain |
| Rate limiting | Recommended | Add to Fastify and Next.js middleware |
| Logging aggregation | Recommended | CloudWatch, Datadog, or ELK stack |
| Health checks | Recommended | `/health` endpoint on both servers |
| Auto-scaling | Recommended | Scale Fastify workers based on queue depth |
| Backups | Required | Automated PostgreSQL backups (RDS snapshots) |
| Secret management | Recommended | AWS Secrets Manager, HashiCorp Vault |
| WebSocket routing | Required | Ensure ALB supports WebSocket upgrade for Socket.IO |
| DNS configuration | Required | A/CNAME records pointing to load balancer |

---

## 11. Testing

### Unit Tests (Vitest)
```bash
# Run all unit tests
npm run test:unit

# Run in watch mode
npm run test
```

**Configuration:** `vitest.config.ts`
- Environment: `jsdom`
- Path alias: `@/` → `./src/`
- Setup file: `./src/test/setup.ts`

### End-to-End Tests (Playwright)
```bash
# Run E2E tests
npm run test:e2e
```

**Configuration:** `playwright.config.ts`
- Test directory: `./src/test/e2e`
- Browser: Chromium
- Base URL: `http://localhost:3000`
- Auto-starts dev server if not running

---

## 12. Troubleshooting

### Common Issues

| Problem | Cause | Solution |
|---|---|---|
| `ECONNREFUSED :5432` | PostgreSQL not running | Start PostgreSQL service |
| `ECONNREFUSED :6379` | Redis not running | Start Redis service or Docker container |
| `Prisma schema drift` | DB schema out of sync | Run `npx prisma migrate deploy` |
| Migration hangs | BullMQ worker not running | Ensure `npm run dev:server` is running |
| No real-time updates | Socket.IO not connected | Check CORS settings and `NEXT_PUBLIC_API_URL` |
| `CONCURRENCY_LOCK` error | Another migration is active | Stop the active batch first |
| LLM API errors | Invalid API key or rate limit | Verify API key in Settings, check provider status |
| Files not appearing | Import failed silently | Check server logs for import errors |
| Blank migrated content | Base64 decode issue | Ensure `b64:` prefix is consistent |

### Useful Commands
```bash
# Reset database completely
npx prisma migrate reset

# Open Prisma Studio (visual DB browser)
npx prisma studio

# Check Redis connection
redis-cli ping

# View BullMQ queue status
# (use Prisma Studio or add Bull Board UI)
```

---

> **Migration Studio** — Transforming MuleSoft integrations into cloud-native AWS architectures, powered by AI.
