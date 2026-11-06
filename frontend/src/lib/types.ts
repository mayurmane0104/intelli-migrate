/* ─── Enums / Unions ─── */
export type Role = 'admin' | 'developer' | 'viewer';
export type Environment = 'dev' | 'test' | 'prod';
export type TargetPlatform = 'aws' | 'sap-integration-suite';
export type MigrationType =
    // AWS Serverless
    | 'mule3-lambda'
    | 'mule4-lambda'
    | 'apiled-apigateway'
    | 'batch-stepfunction'
    // SAP Integration Suite (Cloud Integration)
    | 'mule-to-cpi-iflow'
    | 'mule-to-sap-apim'
    | 'mule-batch-to-cpi';
export type TargetRuntime =
    // AWS Runtimes
    | 'nodejs'
    | 'python'
    | 'java'
    // SAP CPI Runtimes
    | 'groovy'
    | 'cpi-xml'
    | 'xslt';
export type ExportFormat = 'zip' | 'cloudformation' | 'terraform' | 'sam' | 'cpi-package' | 'cpi-iflow' | 'cpi-tenant-push';
export type SourceType = 'git' | 'zip';
export type FileStatus = 'pending' | 'in-progress' | 'completed' | 'failed';
export type ProjectStatus = 'pending' | 'in-progress' | 'completed' | 'failed';
export type MigrationLogLevel = 'success' | 'error' | 'warning' | 'info';

export interface MigrationRecord {
    id: string;
    provider: LLMProviderType;
    model: string;
    content: string; // The full report
    code?: string;   // The extracted clean source code
    systemPrompt?: string; // New
    userPrompt?: string;   // New
    rawResponse?: string;  // New
    tokens: number;
    createdAt: string;
}

export interface MigrationBatch {
    id: string;           // = session.sessionId, shared by ALL files in a run
    projectId: string;
    provider: string;
    model: string;
    status: 'completed' | 'partial' | 'stopped';
    startedAt: string;
    completedAt: string;
    triggeredBy: { userId: string; userName: string };   // user who started the batch
    fileResults: Array<{
        fileId: string;
        fileName: string;
        filePath: string;
        status: 'completed' | 'failed';
    }>;
    totalFiles: number;
    completedFiles: number;
    failedFiles: number;
    totalTokens: number;
}

export interface MigrationConfig {
    targetPlatform?: TargetPlatform;
    migrationType: MigrationType;
    targetRuntime: TargetRuntime;
    fileName?: string;
    filePath?: string;
    instructions?: string;
    projectId?: string;
    fileId?: string;
    projectStructure?: string;
}

/* ─── Domain Models ─── */
export interface User {
    id: string;
    name: string;
    email: string;
    role: Role;
    avatar: string;
}

export interface Organization {
    id: string;
    name: string;
    description: string;
    owner: string;
    createdAt: string;
    workspaceCount: number;
    logo: string;
}

export interface Workspace {
    id: string;
    orgId: string;
    name: string;
    environment: Environment;
    memberCount: number;
    projectCount: number;
}

export interface Project {
    id: string;
    workspaceId: string;
    orgId: string;
    name: string;
    description: string;
    targetPlatform?: TargetPlatform;
    migrationType: MigrationType;
    targetRuntime: TargetRuntime;
    sourceType: SourceType;
    status: ProjectStatus;
    totalFiles: number;
    migratedFiles: number;
    failedFiles: number;
    migrationRuns: number;
    createdAt: string;
    lastActivity: string;
}

export interface ProjectFile {
    id: string;
    projectId: string;
    name: string;
    path: string;
    type: 'file' | 'folder';
    language: string;
    status: FileStatus;
    content: string;
    migratedContent: string; // The full report
    migratedCode?: string;   // The extracted clean source code
    migrations?: MigrationRecord[];
    activeMigrationId?: string;
    children: string[];
    size: number;
    tokens?: number; // Total tokens accumulated for the active migration
    lastModified: string;
}

export interface MigrationLog {
    id: string;
    projectId: string;
    fileName: string;
    timestamp: string;
    status: MigrationLogLevel;
    message: string;
    stackTrace?: string;
    duration?: number;
}

export interface Toast {
    id: string;
    type: 'success' | 'error' | 'warning' | 'info';
    title: string;
    message: string;
}

/* ─── API-aligned request/response shapes (ready for backend) ─── */
export interface MigrationRequest {
    projectId: string;
    migrationType: MigrationType;
    targetRuntime: TargetRuntime;
    fileIds?: string[];
}

export interface MigrationResult {
    fileId: string;
    status: 'completed' | 'failed';
    migratedContent: string;
    migratedCode?: string;
    logs: MigrationLog[];
    duration: number;
}

export interface ExportRequest {
    projectId: string;
    format: 'zip' | 'cloudformation' | 'terraform' | 'sam';
}

/* ─── Job Processing Types ─── */
export type JobStatus = 'queued' | 'running' | 'done' | 'failed';

export interface MigrationJob {
    id: string;
    projectId: string;
    fileId: string;
    batchId?: string; // Grouping ID for projects sync
    fileName: string;
    filePath: string;
    jobType?: string; // e.g. 'REFACTOR', 'VALIDATE', 'EXPORT'
    status: JobStatus;
    progress: number;
    streamedContent: string;
    tokens: number;
    logs: MigrationLog[];
    startedAt?: string;
    completedAt?: string;
    duration?: number;
    error?: string;
    migrations?: MigrationRecord[]; // New
}

export interface MigrationSessionState {
    projectId: string;
    sessionId: string;
    status: 'idle' | 'running' | 'completed' | 'stopped';
    jobs: MigrationJob[];
    totalJobs: number;
    completedJobs: number;
    failedJobs: number;
    currentJobId: string | null;
    startedAt?: string;
    completedAt?: string;
}

export type SSEEventType =
    | 'session:start'
    | 'job:queued' | 'job:start' | 'job:token' | 'job:log' | 'job:progress' | 'job:done' | 'job:failed'
    | 'session:complete' | 'session:stopped';

/* Analysis / IR Projection Types */
export interface IRSummary {
    flows: number;
    apis_detected: number;
    transformations: number;
    integrations: string[];
    complexity_score: string;
    estimated_migration_time: string;
    confidence_score: number;
    validation_status: string;
}

export interface MigrationReadinessSummary {
    flows_analyzed: number;
    connectors_detected: string[];
    complex_transformations: number;
    error_handling_present: boolean;
    unsupported_components: number;
    confidence_score: number;
    migration_readiness: string;
    migration_readiness_label: string;
}

export interface AnalysisInventorySummary {
    mule_configuration_files: string[];
    flow_type_counts: Record<string, number>;
    flows: Array<{
        name: string;
        type: string;
        file: string;
        high_level: string;
        activities: string[];
        connectors: string[];
        transformations: string[];
    }>;
    connectors: Array<{
        name: string;
        connector_type: string;
        connection_details: string[];
        file: string;
    }>;
    dataweave_transformations: Array<Record<string, unknown>>;
    properties_used: Array<Record<string, unknown>>;
    error_handling_and_logging: Array<Record<string, unknown>>;
    munit_test_cases: Array<Record<string, unknown>>;
    readiness_suggestions: string[];
}

export interface ConfidenceBreakdown {
    parsing_confidence: number;
    parsing_level: string;
    transformation_understanding: number;
    transformation_level: string;
    overall_confidence: number;
    overall_level: string;
}

export interface GenerationPreview {
    lambda_functions: number;
    step_functions: number;
    api_gateways: number;
    iam_roles_policies: boolean;
    artifacts: string[];
}

export interface StructuredFlow {
    flow_name: string;
    flow_type: string;
    high_level_summary: string;
    source: string;
    trigger: string;
    transformations: string[];
    connectors: string[];
    connector_operations: Array<{
        connector: string;
        operations: string[];
    }>;
    error_handling: string[];
    detected_patterns: string[];
    confidence: number;
    step_details: Array<{
        index: number;
        title: string;
        detail: string;
        category: string;
        connector: string;
        operation: string;
        condition: string;
        mapping: string;
    }>;
    dependencies: string[];
    decision_logic: string[];
    data_flow: Array<{
        source: string;
        target: string;
        transformation: string;
    }>;
    batch_job?: {
        name: string;
        steps: Array<{
            step: string;
            accept_expression: string;
            condition: string;
            actions: string[];
        }>;
    } | null;
    business_logic: Record<string, unknown>;
    steps: Array<{
        id: string;
        type: string;
        name: string;
        category: string;
        configRef: string | null;
        line: number | null;
    }>;
}

export interface AnalysisValidation {
    status: string;
    confidence_score: number;
    unsupported_connectors: Array<{
        connector_type: string;
        config_name: string;
        severity: string;
        message: string;
    }>;
    complex_transformations: Array<{
        flow_name: string;
        transformation_id: string;
        severity: string;
        message: string;
    }>;
    missing_elements: string[];
    risk_flags: Array<Record<string, unknown>>;
    blockers: string[];
    warnings: string[];
}

export interface ProjectAnalysisPayload {
    summary: IRSummary;
    migration_readiness_summary: MigrationReadinessSummary;
    inventory_summary?: AnalysisInventorySummary;
    confidence_breakdown: ConfidenceBreakdown;
    generation_preview: GenerationPreview;
    risk_warnings: string[];
    structured_flows: StructuredFlow[];
    validation: AnalysisValidation;
    raw_ir?: Record<string, unknown> | null;
}

export interface AnalysisJobView {
    jobId: string;
    projectId: string;
    jobType: 'analysis' | 'migration';
    status: 'queued' | 'running' | 'completed' | 'failed';
    progressPct: number;
    currentStage: string;
    createdAt: string;
    startedAt?: string | null;
    completedAt?: string | null;
    error?: string | null;
    analysis?: ProjectAnalysisPayload;
}

export type MigrationWorkflowState =
    | 'UPLOAD_COMPLETE'
    | 'PARSER_COMPLETE'
    | 'IR_GENERATED'
    | 'IR_APPROVED'
    | 'MAPPING_GENERATED'
    | 'MAPPING_APPROVED'
    | 'ARCHITECTURE_GENERATED'
    | 'ARCHITECTURE_APPROVED'
    | 'CODE_GENERATED'
    | 'EXPORT_READY';

export interface ApprovalRecord {
    stage: string;
    approval_timestamp: string;
    user_id: string;
    approved_version: string;
    ir_hash: string;
    mapping_version: string;
    architecture_version: string;
    agent_version: string;
    notes?: string;
}

export interface MigrationWorkflow {
    project_id: string;
    state: MigrationWorkflowState;
    analysis_job_id?: string;
    migration_job_id?: string;
    ir_hash?: string;
    mapping_version?: string;
    architecture_version?: string;
    code_version?: string;
    approvals: ApprovalRecord[];
    mapping_review?: MappingReviewPayload;
    architecture_review?: ArchitectureReviewPayload;
    generated_code?: Array<Record<string, unknown>>;
    audit_trail?: Record<string, unknown>;
    updated_at?: string;
}

export interface MappingReviewRow {
    flowName: string;
    muleComponent: string;
    awsTarget: string;
    confidence: number;
    migrationNotes: string;
    template: string;
    manualReview: boolean;
}

export interface MappingReviewPayload {
    summary?: Record<string, unknown>;
    mappings: MappingReviewRow[];
}

export interface ArchitectureReviewRow {
    awsService: string;
    purpose: string;
    generatedResourceName: string;
    estimatedCostCategory: string;
    count: number;
}

export interface ArchitectureReviewPayload {
    architecture: ArchitectureReviewRow[];
    summary?: Record<string, unknown>;
}

/* ─── LLM Configuration Types ─── */
export type LLMProviderType = 'nova' | 'claude' | 'openai' | 'gemini';

export interface LLMProviderConfig {
    apiKey: string;
    model: string;
    enabled: boolean;
}

export interface LLMSettings {
    activeProvider: LLMProviderType;
    providers: {
        nova: LLMProviderConfig;      // Amazon Nova Lite (AWS Bedrock) — primary
        claude: LLMProviderConfig;
        openai: LLMProviderConfig;
        gemini: LLMProviderConfig;
    };
    theme: 'light' | 'dark' | 'system';
    notifications: boolean;
}
