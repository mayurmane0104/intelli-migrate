CREATE TABLE "SAPReference" (
    "id" TEXT NOT NULL,
    "userId" TEXT NOT NULL,
    "projectId" TEXT,
    "filename" TEXT NOT NULL,
    "artifactType" TEXT NOT NULL,
    "profile" JSONB NOT NULL,
    "createdAt" TIMESTAMP(3) NOT NULL DEFAULT CURRENT_TIMESTAMP,
    "expiresAt" TIMESTAMP(3) NOT NULL,
    CONSTRAINT "SAPReference_pkey" PRIMARY KEY ("id")
);

CREATE INDEX "SAPReference_userId_createdAt_idx" ON "SAPReference"("userId", "createdAt");
CREATE INDEX "SAPReference_projectId_idx" ON "SAPReference"("projectId");
CREATE INDEX "SAPReference_expiresAt_idx" ON "SAPReference"("expiresAt");

ALTER TABLE "SAPReference" ADD CONSTRAINT "SAPReference_userId_fkey"
    FOREIGN KEY ("userId") REFERENCES "User"("id") ON DELETE CASCADE ON UPDATE CASCADE;
ALTER TABLE "SAPReference" ADD CONSTRAINT "SAPReference_projectId_fkey"
    FOREIGN KEY ("projectId") REFERENCES "Project"("id") ON DELETE CASCADE ON UPDATE CASCADE;

ALTER TABLE "Project"
    ADD COLUMN "sapReferenceMode" TEXT NOT NULL DEFAULT 'standard',
    ADD COLUMN "sapValidation" JSONB,
    ADD COLUMN "sapValidationAt" TIMESTAMP(3),
    ADD COLUMN "sapConnection" JSONB,
    ADD COLUMN "sapConnectionAt" TIMESTAMP(3),
    ADD COLUMN "sapTestDeployment" JSONB,
    ADD COLUMN "sapTestDeploymentAt" TIMESTAMP(3);
