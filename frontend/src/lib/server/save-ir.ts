import { mkdir, writeFile } from 'fs/promises';
import path from 'path';
import crypto from 'crypto';

type SaveIRInput = {
    projectId: string;
    projectName: string;
    sourceFile: string;
    irVersion?: string;
    ir: unknown;
};

type SaveIROutput = {
    saved: boolean;
    path: string;
};

function sanitizeName(value: string): string {
    return value
        .replace(/[^a-zA-Z0-9._-]/g, '_')
        .replace(/_+/g, '_')
        .replace(/^_+|_+$/g, '')
        .slice(0, 80) || 'unknown';
}

function formatTimestamp(date = new Date()): string {
    const y = date.getUTCFullYear();
    const m = String(date.getUTCMonth() + 1).padStart(2, '0');
    const d = String(date.getUTCDate()).padStart(2, '0');
    const hh = String(date.getUTCHours()).padStart(2, '0');
    const mm = String(date.getUTCMinutes()).padStart(2, '0');
    const ss = String(date.getUTCSeconds()).padStart(2, '0');
    return `${y}${m}${d}_${hh}${mm}${ss}`;
}

function shortHash(seed: string): string {
    return crypto.createHash('sha1').update(seed).digest('hex').slice(0, 6);
}

export async function saveIRToFile(input: SaveIRInput): Promise<SaveIROutput> {
    const baseDir = path.join(process.cwd(), 'IR_Outputs');
    const projectFolder = sanitizeName(input.projectName || input.projectId);
    const outputDir = path.join(baseDir, projectFolder);
    await mkdir(outputDir, { recursive: true });

    const sourceBase = sanitizeName(path.parse(input.sourceFile || 'unknown').name);
    const projectBase = sanitizeName(input.projectName || input.projectId);
    const ts = formatTimestamp();

    const payload = {
        projectId: input.projectId,
        sourceFile: input.sourceFile || 'unknown',
        generatedAt: new Date().toISOString(),
        irVersion: input.irVersion || 'unknown',
        ir: input.ir,
    };
    const content = JSON.stringify(payload, null, 2);

    for (let attempt = 0; attempt < 5; attempt++) {
        const entropy = `${input.projectId}:${input.sourceFile}:${Date.now()}:${attempt}:${Math.random()}`;
        const hash = shortHash(entropy);
        const fileName = `${projectBase}_${sourceBase}_${ts}_${hash}.json`;
        const filePath = path.join(outputDir, fileName);
        try {
            await writeFile(filePath, content, { encoding: 'utf-8', flag: 'wx' });
            return { saved: true, path: filePath };
        } catch (error: unknown) {
            const e = error as NodeJS.ErrnoException;
            if (e.code !== 'EEXIST') throw error;
        }
    }

    throw new Error('Could not generate a unique IR output file name after multiple attempts.');
}

