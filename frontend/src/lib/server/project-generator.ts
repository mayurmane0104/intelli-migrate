import { PrismaClient } from '@prisma/client';
import fs from 'fs/promises';
import path from 'path';

const prisma = new PrismaClient();

const b64dec = (s: string): string => {
    if (typeof s === 'string' && s.startsWith('b64:')) {
        try { return Buffer.from(s.slice(4), 'base64').toString('utf8'); }
        catch { return s; }
    }
    return s;
};

export async function generatePhysicalProject(projectId: string): Promise<void> {
    const project = await prisma.project.findUnique({
        where: { id: projectId },
        include: { files: true }
    });

    if (!project) throw new Error(`Project ${projectId} not found`);

    const projectName = project.name.replace(/[^a-zA-Z0-9_-]/g, '-').toLowerCase();
    
    // Determine target runtime characteristics
    const isPython = project.targetRuntime === 'python';
    const isNode = project.targetRuntime === 'nodejs';
    const isJava = project.targetRuntime === 'java';
    
    const ext = isPython ? 'py' : (isNode ? 'ts' : 'java');
    
    // Use an absolute path under the main project directory
    const outputDir = path.resolve(process.cwd(), 'outputs', projectName);
    
    console.log(`[Project Generator] Clearing directory: ${outputDir}`);
    await fs.rm(outputDir, { recursive: true, force: true });
    
    const lambdaDir = path.join(outputDir, 'lambda');
    await fs.mkdir(lambdaDir, { recursive: true });

    // Identify successfully migrated files
    const completedFiles = project.files.filter(f => f.status === 'completed' && f.migratedCode);
    const lambdas: string[] = [];

    for (const file of completedFiles) {
        let code = b64dec(file.migratedCode!);
        
        // Use the original file name, mapped to the correct extension
        const baseName = path.parse(file.name).name.replace(/[^a-zA-Z0-9_]/g, '_');
        const fileName = `${baseName}.${ext}`;
        const filePath = path.join(lambdaDir, fileName);
        
        await fs.writeFile(filePath, code, 'utf8');
        lambdas.push(baseName);
    }

    // Generate boilerplate CDK files based on runtime
    if (isPython) {
        await generatePythonCDK(outputDir, projectName, lambdas);
    } else if (isNode) {
        await generateNodeCDK(outputDir, projectName, lambdas);
    } else {
        // Fallback or Java generic structure
        await fs.writeFile(path.join(outputDir, 'README.md'), `# ${projectName}\nMigration complete.\n`);
    }

    console.log(`[Project Generator] Successfully generated ${lambdas.length} lambdas for project ${projectName} at ${outputDir}`);
}

async function generatePythonCDK(outputDir: string, projectName: string, lambdas: string[]) {
    const cdkJson = {
        app: "python3 app.py",
        context: {}
    };
    await fs.writeFile(path.join(outputDir, 'cdk.json'), JSON.stringify(cdkJson, null, 2));
    
    const requirementsTxt = `aws-cdk-lib>=2.0.0
constructs>=10.0.0
`;
    await fs.writeFile(path.join(outputDir, 'requirements.txt'), requirementsTxt);
    
    let appPy = `#!/usr/bin/env python3
import os
import aws_cdk as cdk
from aws_cdk import (
    Stack,
    aws_lambda as _lambda,
    aws_apigateway as apigw
)
from constructs import Construct

class MigrationStack(Stack):
    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        api = apigw.RestApi(self, "${projectName}-api", rest_api_name="${projectName}")

`;

    for (const lName of lambdas) {
        const handlerName = `${lName.replace(/-/g, '_')}_handler`;
        appPy += `        ${handlerName} = _lambda.Function(
            self, '${lName}-Func',
            runtime=_lambda.Runtime.PYTHON_3_12,
            code=_lambda.Code.from_asset('lambda'),
            handler='${lName}.lambda_handler',
        )
        
        # Adding a default resource and ANY method to API gateway for this lambda
        resource_${handlerName} = api.root.add_resource('${lName.replace(/_/g, '-')}')
        resource_${handlerName}.add_method('ANY', apigw.LambdaIntegration(${handlerName}))

`;
    }

    appPy += `
app = cdk.App()
MigrationStack(app, "${projectName}-stack")
app.synth()
`;

    await fs.writeFile(path.join(outputDir, 'app.py'), appPy);
}

async function generateNodeCDK(outputDir: string, projectName: string, lambdas: string[]) {
    const cdkJson = {
        app: "npx ts-node bin/app.ts",
        context: {}
    };
    await fs.writeFile(path.join(outputDir, 'cdk.json'), JSON.stringify(cdkJson, null, 2));

    const packageJson = {
        name: projectName,
        version: "1.0.0",
        bin: {
            app: "bin/app.js"
        },
        scripts: {
            build: "tsc",
            cdk: "cdk"
        },
        dependencies: {
            "aws-cdk-lib": "2.100.0",
            "constructs": "^10.0.0"
        },
        devDependencies: {
            "typescript": "~5.2.2",
            "ts-node": "^10.9.1",
            "@types/node": "20.x"
        }
    };
    await fs.writeFile(path.join(outputDir, 'package.json'), JSON.stringify(packageJson, null, 2));

    await fs.mkdir(path.join(outputDir, 'bin'), { recursive: true });
    await fs.mkdir(path.join(outputDir, 'lib'), { recursive: true });

    let stackTs = `import * as cdk from 'aws-cdk-lib';
import { Construct } from 'constructs';
import * as lambda from 'aws-cdk-lib/aws-lambda';
import * as apigw from 'aws-cdk-lib/aws-apigateway';

export class MigrationStack extends cdk.Stack {
  constructor(scope: Construct, id: string, props?: cdk.StackProps) {
    super(scope, id, props);

    const api = new apigw.RestApi(this, '${projectName}-api', {
      restApiName: '${projectName}'
    });

`;

    for (const lName of lambdas) {
        const varName = lName.replace(/[^a-zA-Z0-9]/g, '') + 'Handler';
        stackTs += `    const ${varName} = new lambda.Function(this, '${lName}-Func', {
      runtime: lambda.Runtime.NODEJS_20_X,
      code: lambda.Code.fromAsset('lambda'),
      handler: '${lName}.handler'
    });

    const resource_${varName} = api.root.addResource('${lName.replace(/_/g, '-')}');
    resource_${varName}.addMethod('ANY', new apigw.LambdaIntegration(${varName}));

`;
    }

    stackTs += `  }
}
`;

    await fs.writeFile(path.join(outputDir, 'lib', 'migration-stack.ts'), stackTs);

    const appTs = `#!/usr/bin/env node
import 'source-map-support/register';
import * as cdk from 'aws-cdk-lib';
import { MigrationStack } from '../lib/migration-stack';

const app = new cdk.App();
new MigrationStack(app, '${projectName}-stack');
`;
    await fs.writeFile(path.join(outputDir, 'bin', 'app.ts'), appTs);
}
