import { PrismaClient } from '@prisma/client';
import { mockProjects, mockFiles } from './src/lib/mockData';

const prisma = new PrismaClient();

async function main() {
    console.log('Seeding database with mock data...');

    // 0. Seed User
    await prisma.user.upsert({
        where: { id: 'user-1' },
        update: {},
        create: {
            id: 'user-1',
            name: 'Harsh Patel',
            email: 'admin@MigrationStudio.io',
            role: 'admin',
        }
    });

    // 1. Seed Org
    await prisma.organization.upsert({
        where: { id: 'org-1' },
        update: {},
        create: {
            id: 'org-1',
            userId: 'user-1',
            name: 'Acme Corporation',
            owner: 'Harsh Patel',
        }
    });

    // 2. Seed Workspace
    await prisma.workspace.upsert({
        where: { id: 'ws-1' },
        update: {},
        create: {
            id: 'ws-1',
            userId: 'user-1',
            orgId: 'org-1',
            name: 'Development',
            environment: 'dev',
        }
    });

    // 3. Seed Projects
    for (const project of mockProjects) {
        await prisma.project.upsert({
            where: { id: project.id },
            update: {},
            create: {
                id: project.id,
                userId: 'user-1',
                orgId: project.orgId || 'org-1',
                workspaceId: project.workspaceId || 'ws-1',
                name: project.name,
                description: project.description,
                migrationType: project.migrationType,
                targetRuntime: project.targetRuntime,
                sourceType: project.sourceType || 'local',
                status: project.status,
                totalFiles: project.totalFiles,
                migratedFiles: project.migratedFiles,
                failedFiles: project.failedFiles,
                createdAt: new Date(project.createdAt),
            },
        });
    }

    // 4. Seed Files
    let count = 0;
    for (const file of mockFiles) {
        if (file.type === 'folder') continue;

        await prisma.projectFile.upsert({
            where: { id: file.id },
            update: {},
            create: {
                id: file.id,
                projectId: file.projectId,
                name: file.name,
                path: file.path,
                type: file.type,
                language: file.language,
                status: 'pending',
                content: 'b64:' + Buffer.from(file.content || '', 'utf8').toString('base64'),
                size: file.size,
            },
        });
        count++;
    }

    console.log(`Seed completed successfully. Inserted ${count} files.`);
}

main()
    .catch((e) => {
        console.error(e);
        process.exit(1);
    })
    .finally(async () => {
        await prisma.$disconnect();
    });
