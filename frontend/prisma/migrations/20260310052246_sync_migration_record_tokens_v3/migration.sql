-- AlterTable
ALTER TABLE "MigrationBatch" ADD COLUMN     "totalTokens" INTEGER NOT NULL DEFAULT 0;

-- AlterTable
ALTER TABLE "MigrationRecord" ADD COLUMN     "tokens" INTEGER NOT NULL DEFAULT 0;
