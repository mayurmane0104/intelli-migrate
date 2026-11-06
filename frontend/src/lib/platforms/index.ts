import type {
    TargetPlatform,
    MigrationType,
    TargetRuntime,
    ExportFormat,
} from '../types';

export interface PlatformStrategy {
    id: TargetPlatform;
    displayName: string;
    description: string;
    defaultRuntime: TargetRuntime;
    supportedRuntimes: Array<{ id: TargetRuntime; label: string }>;
    supportedMigrationTypes: Array<{ id: MigrationType; label: string; desc: string }>;
    fileExtensionMap: Record<string, string>;
    folderMap: Record<string, string>;
    outputPaneTitle: string;
    exportFormats: Array<{ id: ExportFormat; label: string; desc: string; icon: string }>;
    connectorMappingLabels: Record<string, string>;
}

export const AWS_PLATFORM: PlatformStrategy = {
    id: 'aws',
    displayName: 'AWS Serverless',
    description: 'Transform MuleSoft flows into AWS Lambda, API Gateway, SQS, and Terraform/SAM',
    defaultRuntime: 'python',
    supportedRuntimes: [
        { id: 'python', label: 'Python 3.12 (AWS Lambda)' },
        { id: 'nodejs', label: 'Node.js 20.x (TypeScript)' },
        { id: 'java', label: 'Java 21 (GraalVM / Quarkus)' },
    ],
    supportedMigrationTypes: [
        { id: 'mule4-lambda', label: 'Mule 4 to AWS Lambda', desc: 'Standard Mule 4 XML & DataWeave to AWS serverless microservices' },
        { id: 'mule3-lambda', label: 'Mule 3 to AWS Lambda', desc: 'Legacy Mule 3 XML & MEL expressions to AWS Lambda' },
        { id: 'apiled-apigateway', label: 'API-Led to API Gateway', desc: 'Experience/Process/System APIs to API Gateway HTTP APIs' },
        { id: 'batch-stepfunction', label: 'Batch to Step Functions', desc: 'Mule batch jobs to AWS Step Functions state machines' },
    ],
    fileExtensionMap: {
        xml: 'py',
        dwl: 'py',
        raml: 'yaml',
        yaml: 'yaml',
        yml: 'yaml',
        json: 'json',
        properties: 'env',
    },
    folderMap: {
        mule: 'handlers',
        dwl: 'services',
        api: 'openapi',
        resources: 'config',
    },
    outputPaneTitle: 'AWS Lambda & Cloud-Native Output',
    exportFormats: [
        { id: 'zip', label: 'Raw Python / Node (ZIP)', desc: 'Complete deployable source code with handlers and tests', icon: '📦' },
        { id: 'terraform', label: 'Terraform (HCL)', desc: 'Terraform modules for API Gateway, Lambda, RDS, and IAM', icon: '🏗️' },
        { id: 'sam', label: 'AWS SAM Template', desc: 'template.yaml with serverless resources and least-privilege IAM', icon: '🚀' },
        { id: 'cloudformation', label: 'CloudFormation', desc: 'Automated CloudFormation deployment templates', icon: '☁️' },
    ],
    connectorMappingLabels: {
        http: 'API Gateway + Lambda',
        db: 'Amazon RDS / Aurora MySQL/PostgreSQL',
        sqs: 'Amazon SQS Queue',
        sns: 'Amazon SNS Topic',
        s3: 'Amazon S3 Bucket',
        sfdc: 'Salesforce REST Client (boto3 / simple_salesforce)',
        email: 'Amazon SES / SMTP Client',
        cache: 'Amazon ElastiCache Redis',
        secret: 'AWS Secrets Manager',
    },
};

export const SAP_CPI_PLATFORM: PlatformStrategy = {
    id: 'sap-integration-suite',
    displayName: 'SAP Integration Suite (Cloud Integration)',
    description: 'Migrate MuleSoft applications to SAP Cloud Integration (CPI) iFlows and Groovy scripts',
    defaultRuntime: 'groovy',
    supportedRuntimes: [
        { id: 'groovy', label: 'Apache Groovy 2.4 / 3.0 (CPI Scripts)' },
        { id: 'cpi-xml', label: 'BPMN2 iFlow Model + Camel XML' },
        { id: 'xslt', label: 'XSLT 2.0 / 3.0 (Message Mapping)' },
    ],
    supportedMigrationTypes: [
        { id: 'mule-to-cpi-iflow', label: 'Mule Flow to CPI iFlow', desc: 'Translates Mule flows into BPMN2 iFlow XML with Camel routes' },
        { id: 'mule-to-sap-apim', label: 'Mule API to SAP API Management', desc: 'Translates RAML/OAS into SAP API Portal proxies and policies' },
        { id: 'mule-batch-to-cpi', label: 'Mule Batch to CPI Splitter/Gatherer', desc: 'Converts batch jobs to CPI General Splitter + Gather pipelines' },
    ],
    fileExtensionMap: {
        xml: 'iflw',
        dwl: 'groovy',
        raml: 'edmx',
        yaml: 'edmx',
        yml: 'edmx',
        json: 'json',
        properties: 'prop',
    },
    folderMap: {
        mule: 'scenarioflows/integrationflow',
        dwl: 'script',
        api: 'edmx',
        resources: 'parameters',
    },
    outputPaneTitle: 'SAP Cloud Integration iFlow / Groovy Script',
    exportFormats: [
        { id: 'cpi-package', label: 'SAP CPI Content Package (ZIP)', desc: 'Complete Content Package archive for Design -> Integrations and APIs -> Import', icon: '📦' },
        { id: 'cpi-iflow', label: 'Individual Integration Flow (ZIP)', desc: 'Single iFlow archive for uploading into an existing package', icon: '🔄' },
        { id: 'cpi-tenant-push', label: 'Deploy to SAP BTP Tenant', desc: 'Direct push via SAP Cloud Integration OData Design-Time API', icon: '☁️' },
    ],
    connectorMappingLabels: {
        http: 'HTTPS / ProcessDirect Adapter',
        db: 'SAP JDBC Receiver Adapter',
        sqs: 'SAP Event Mesh / JMS Adapter',
        jms: 'JMS Sender/Receiver Adapter',
        s3: 'SFTP / Open Connectors Adapter',
        sfdc: 'Salesforce OData Adapter',
        email: 'Mail Receiver Adapter',
        sap: 'SAP RFC / IDoc Native Adapter',
        secret: 'SAP Security Materials (Credentials / Keystore)',
    },
};

export const PLATFORM_STRATEGIES: Record<TargetPlatform, PlatformStrategy> = {
    aws: AWS_PLATFORM,
    'sap-integration-suite': SAP_CPI_PLATFORM,
};

export function getPlatformStrategy(
    platform?: TargetPlatform | string,
    migrationType?: string,
    targetRuntime?: string,
): PlatformStrategy {
    if (platform === 'sap-integration-suite') {
        return SAP_CPI_PLATFORM;
    }
    if (migrationType && (migrationType.includes('cpi') || migrationType.includes('sap'))) {
        return SAP_CPI_PLATFORM;
    }
    if (targetRuntime && (targetRuntime === 'groovy' || targetRuntime === 'cpi-xml' || targetRuntime === 'xslt')) {
        return SAP_CPI_PLATFORM;
    }
    return AWS_PLATFORM;
}
