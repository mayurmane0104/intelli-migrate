-- CreateTable: Organization
CREATE TABLE "Organization" (
    "id" TEXT NOT NULL,
    "userId" TEXT NOT NULL,
    "name" TEXT NOT NULL,
    "description" TEXT NOT NULL DEFAULT '',
    "owner" TEXT NOT NULL DEFAULT '',
    "logo" TEXT NOT NULL DEFAULT '',
    "createdAt" TIMESTAMP(3) NOT NULL DEFAULT CURRENT_TIMESTAMP,

    CONSTRAINT "Organization_pkey" PRIMARY KEY ("id")
);

-- CreateTable: Workspace
CREATE TABLE "Workspace" (
    "id" TEXT NOT NULL,
    "userId" TEXT NOT NULL,
    "orgId" TEXT NOT NULL,
    "name" TEXT NOT NULL,
    "environment" TEXT NOT NULL DEFAULT 'dev',
    "memberCount" INTEGER NOT NULL DEFAULT 1,

    CONSTRAINT "Workspace_pkey" PRIMARY KEY ("id")
);

-- Add fileResults column to MigrationBatch
ALTER TABLE "MigrationBatch" ADD COLUMN "fileResults" JSONB NOT NULL DEFAULT '[]';

-- CreateIndex
CREATE UNIQUE INDEX "Organization_name_key" ON "Organization"("name");
CREATE INDEX "Organization_userId_idx" ON "Organization"("userId");
CREATE INDEX "Workspace_orgId_idx" ON "Workspace"("orgId");
CREATE INDEX "Workspace_userId_idx" ON "Workspace"("userId");
CREATE UNIQUE INDEX "Workspace_orgId_name_key" ON "Workspace"("orgId", "name");

-- AddForeignKey: Organization → User
ALTER TABLE "Organization" ADD CONSTRAINT "Organization_userId_fkey"
    FOREIGN KEY ("userId") REFERENCES "User"("id") ON DELETE CASCADE ON UPDATE CASCADE;

-- AddForeignKey: Workspace → User
ALTER TABLE "Workspace" ADD CONSTRAINT "Workspace_userId_fkey"
    FOREIGN KEY ("userId") REFERENCES "User"("id") ON DELETE CASCADE ON UPDATE CASCADE;

-- AddForeignKey: Workspace → Organization
ALTER TABLE "Workspace" ADD CONSTRAINT "Workspace_orgId_fkey"
    FOREIGN KEY ("orgId") REFERENCES "Organization"("id") ON DELETE CASCADE ON UPDATE CASCADE;

-- AddForeignKey: Project → Workspace
ALTER TABLE "Project" ADD CONSTRAINT "Project_workspaceId_fkey"
    FOREIGN KEY ("workspaceId") REFERENCES "Workspace"("id") ON DELETE CASCADE ON UPDATE CASCADE;

-- AddForeignKey: Project → Organization
ALTER TABLE "Project" ADD CONSTRAINT "Project_orgId_fkey"
    FOREIGN KEY ("orgId") REFERENCES "Organization"("id") ON DELETE CASCADE ON UPDATE CASCADE;
