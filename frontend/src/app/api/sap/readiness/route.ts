import { NextRequest, NextResponse } from 'next/server';
import { getAuthUserId } from '@/lib/server/auth';
import { prisma } from '@/lib/prisma';

export async function GET(req: NextRequest) {
    const userId = await getAuthUserId(req);
    if (!userId) return NextResponse.json({ error: 'Authentication required' }, { status: 401 });
    const projectId = req.nextUrl.searchParams.get('projectId');
    if (!projectId) return NextResponse.json({ error: 'projectId is required' }, { status: 400 });
    const now = new Date();
    const project = await prisma.project.findFirst({ where: { id: projectId, userId }, include: {
        _count: { select: { files: true } },
        files: { orderBy: { lastModified: 'desc' }, take: 1, select: { lastModified: true } },
        sapReferences: { where: { userId, expiresAt: { gt: now } }, orderBy: { createdAt: 'desc' }, take: 1, select: { id: true } },
    } });
    if (!project) return NextResponse.json({ error: 'Project not found' }, { status: 404 });
    const source = project._count.files > 0;
    const target = project.targetPlatform === 'sap-integration-suite';
    const compatibility = project.sapValidation as { validation_status?: string } | null;
    const latestProjectInput = project.files[0]?.lastModified;
    const validationFresh = Boolean(project.sapValidationAt && project.sapValidationAt >= latestProjectInput);
    const tenant = project.sapConnection as { connection_status?: string } | null;
    const deployment = project.sapTestDeployment as { deployment_status?: string } | null;
    const connection = tenant?.connection_status || 'not_tested';
    const currentValidation = validationFresh ? compatibility : null;
    const readiness = !source || !target || currentValidation?.validation_status === 'error'
        ? 'needs_attention'
        : currentValidation?.validation_status === 'passed'
            ? 'ready'
            : currentValidation?.validation_status === 'warning'
                ? 'ready_with_warnings'
                : 'ready_for_generation';
    return NextResponse.json({
        source_project: source ? 'available' : 'missing_files',
        target_platform: target ? 'configured' : 'not_sap',
        reference_project: project.sapReferenceMode === 'reference' ? (project.sapReferences.length ? 'analyzed' : 'missing_or_expired') : 'skipped',
        target_compatibility: currentValidation?.validation_status || 'not_validated',
        sap_connection: connection,
        test_deployment: deployment?.deployment_status || 'not_run',
        migration_readiness: readiness,
        requires_tenant_for_generation: false,
        requires_tenant_for_direct_deployment: true,
        compatibility_checked_at: validationFresh ? project.sapValidationAt : null,
        connection_checked_at: project.sapConnectionAt,
        test_deployment_checked_at: project.sapTestDeploymentAt,
    });
}
