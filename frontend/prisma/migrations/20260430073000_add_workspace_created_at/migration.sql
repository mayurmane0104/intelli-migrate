-- Backfill schema drift: Workspace.createdAt exists in Prisma schema
-- but was omitted from the original Workspace table migration.
ALTER TABLE "Workspace"
ADD COLUMN IF NOT EXISTS "createdAt" TIMESTAMP(3) NOT NULL DEFAULT CURRENT_TIMESTAMP;
