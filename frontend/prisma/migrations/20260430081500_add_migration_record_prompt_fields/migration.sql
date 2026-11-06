-- Backfill schema drift on MigrationRecord prompt/response fields.
ALTER TABLE "MigrationRecord"
ADD COLUMN IF NOT EXISTS "systemPrompt" TEXT,
ADD COLUMN IF NOT EXISTS "userPrompt" TEXT,
ADD COLUMN IF NOT EXISTS "rawResponse" TEXT;
