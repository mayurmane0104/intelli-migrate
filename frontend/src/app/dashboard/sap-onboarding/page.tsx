'use client';

import { useEffect, useState } from 'react';
import { useApp } from '@/contexts/AppContext';
import { ArrowUpTrayIcon, CheckCircleIcon, CloudIcon, DocumentMagnifyingGlassIcon, ShieldCheckIcon } from '@heroicons/react/24/outline';

type Profile = {
    reference_id: string; artifact_type: string; analysis_status: string; artifacts: { artifact_id: string | null }[];
    adapter_inventory: { type: string }[]; resource_inventory: unknown[]; script_inventory: unknown[];
    mapping_inventory: unknown[]; validation_warnings: string[]; package_metadata: Record<string, unknown>;
};
type Compatibility = { validation_status: string; reference_used: boolean; summary: { total_artifacts: number; passed: number; warnings: number; failed: number }; artifacts: { artifact_id: string; status: string; warnings: string[]; errors: string[] }[]; disclaimer: string };

export default function SAPOnboardingPage() {
    const { selectedProject } = useApp();
    const [choice, setChoice] = useState<'upload' | 'skip'>('skip');
    const [profile, setProfile] = useState<Profile | null>(null);
    const [filename, setFilename] = useState('');
    const [busy, setBusy] = useState(false);
    const [error, setError] = useState('');
    const [tenantUrl, setTenantUrl] = useState('');
    const [tokenUrl, setTokenUrl] = useState('');
    const [clientId, setClientId] = useState('');
    const [clientSecret, setClientSecret] = useState('');
    const [connection, setConnection] = useState<Record<string, string> | null>(null);
    const [testingConnection, setTestingConnection] = useState(false);
    const [compatibility, setCompatibility] = useState<Compatibility | null>(null);
    const [validating, setValidating] = useState(false);
    const [readiness, setReadiness] = useState<Record<string, string> | null>(null);
    const [testApproved, setTestApproved] = useState(false);
    const [testDeployment, setTestDeployment] = useState<Record<string, unknown> | null>(null);
    const [deployingTest, setDeployingTest] = useState(false);

    useEffect(() => {
        const query = selectedProject ? `?projectId=${encodeURIComponent(selectedProject.id)}` : '';
        fetch(`/api/sap/reference${query}`, { cache: 'no-store' })
            .then(async response => response.ok ? response.json() : null)
            .then(data => { if (data?.reference) { setProfile(data.reference); setChoice('upload'); setFilename(data.reference.filename || 'Saved SAP reference'); } })
            .catch(() => {});
    }, [selectedProject?.id]);

    useEffect(() => {
        if (!selectedProject?.id) { setReadiness(null); return; }
        fetch(`/api/sap/readiness?projectId=${encodeURIComponent(selectedProject.id)}`, { cache: 'no-store' })
            .then(async response => response.ok ? response.json() : null)
            .then(setReadiness).catch(() => setReadiness(null));
    }, [selectedProject?.id, profile, compatibility, connection, testDeployment]);

    async function testConnection() {
        setTestingConnection(true); setConnection(null);
        try {
            const response = await fetch('/api/sap/tenant/test-connection', { method: 'POST', headers: { 'content-type': 'application/json' }, body: JSON.stringify({ tenant_url: tenantUrl, token_url: tokenUrl, client_id: clientId, client_secret: clientSecret, projectId: selectedProject?.id }) });
            const result = await response.json();
            setConnection(result);
            setClientSecret('');
        } catch { setConnection({ connection_status: 'failed', error: 'Connection check could not be completed.' }); }
        finally { setTestingConnection(false); setClientSecret(''); }
    }

    async function skipReference() {
        setChoice('skip'); setProfile(null); setError('');
        if (selectedProject?.id) {
            const response = await fetch('/api/sap/reference', { method: 'PUT', headers: { 'content-type': 'application/json' }, body: JSON.stringify({ projectId: selectedProject.id, mode: 'standard' }) });
            if (!response.ok) setError('Skip selection could not be saved for this project.');
        }
    }

    async function validateGenerated(files: FileList | null) {
        if (!files?.length || !selectedProject?.id) return;
        const form = new FormData(); form.set('projectId', selectedProject.id);
        Array.from(files).forEach(file => form.append('files', file));
        setValidating(true); setCompatibility(null); setError('');
        try {
            const response = await fetch('/api/sap/compatibility/validate', { method: 'POST', body: form });
            const result = await response.json();
            if (!response.ok) throw new Error(result.detail || result.error || 'Generated artifact validation failed.');
            setCompatibility(result);
        } catch (e) { setError(e instanceof Error ? e.message : 'Generated artifact validation failed.'); }
        finally { setValidating(false); }
    }

    async function runTestDeployment() {
        if (!selectedProject?.id || !testApproved) return;
        setDeployingTest(true); setTestDeployment(null); setError('');
        try {
            const response = await fetch('/api/sap/tenant/test-deployment', {
                method: 'POST', headers: { 'content-type': 'application/json' },
                body: JSON.stringify({ tenant_url: tenantUrl, token_url: tokenUrl, client_id: clientId,
                    client_secret: clientSecret, projectId: selectedProject.id, approved: true,
                    approval_text: 'I approve creating and deploying a temporary SAP test package and iFlow' }),
            });
            const result = await response.json();
            if (!response.ok) throw new Error(result.detail || result.error || 'Test deployment failed.');
            setTestDeployment(result); setClientSecret(''); setTestApproved(false);
        } catch (e) { setError(e instanceof Error ? e.message : 'Test deployment failed.'); }
        finally { setDeployingTest(false); setClientSecret(''); }
    }

    async function upload(file?: File) {
        if (!file) return;
        setChoice('upload'); setFilename(file.name); setProfile(null); setError('');
        if (!file.name.toLowerCase().endsWith('.zip') || file.size > 50 * 1024 * 1024) {
            setError('Choose a ZIP archive smaller than 50 MB.'); return;
        }
        const body = new FormData(); body.set('file', file);
        if (selectedProject?.id) body.set('projectId', selectedProject.id);
        setBusy(true);
        try {
            const response = await fetch('/api/sap/reference', { method: 'POST', body });
            const result = await response.json();
            if (!response.ok) throw new Error(result.detail || result.error || 'Reference archive could not be analyzed.');
            setProfile(result);
        } catch (e) { setError(e instanceof Error ? e.message : 'Reference analysis failed.'); }
        finally { setBusy(false); }
    }

    async function removeReference() {
        if (!profile?.reference_id) return;
        const response = await fetch(`/api/sap/reference?referenceId=${encodeURIComponent(profile.reference_id)}`, { method: 'DELETE' });
        if (response.ok) { setProfile(null); setFilename(''); setChoice('skip'); }
    }

    return <main className="max-w-5xl mx-auto p-6 lg:p-10 space-y-7">
        <header><p className="text-xs font-bold uppercase tracking-[.18em] text-primary-600">Migration setup</p><h1 className="text-3xl font-bold mt-2">Configure Your SAP Target Environment</h1><p className="text-gray-500 mt-2 max-w-3xl">Prepare your target environment, optionally provide a native SAP reference project, and validate compatibility before migration.</p></header>
        <section className="rounded-2xl border bg-white dark:bg-gray-900 p-6 space-y-4">
            <h2 className="font-semibold text-lg">Source and target</h2>
            <div className="grid md:grid-cols-2 gap-4"><div className="rounded-xl border p-4"><div className="text-xs text-gray-500">SOURCE PROJECT</div><p className="font-medium mt-1">{selectedProject?.name || 'Select a MuleSoft project in the workspace'}</p><p className="text-sm text-gray-500 mt-1">Existing source analysis remains unchanged.</p></div><div className="rounded-xl border p-4"><div className="text-xs text-gray-500">TARGET PLATFORM</div><p className="font-medium mt-1">{selectedProject?.targetPlatform === 'sap-integration-suite' ? 'SAP Integration Suite' : 'SAP target not selected for this project'}</p><p className="text-sm text-gray-500 mt-1">{selectedProject?.targetPlatform === 'sap-integration-suite' ? 'Cloud Integration (CPI)' : selectedProject ? 'Choose SAP Integration Suite in Project Setup.' : 'Select a project to see its target platform.'}</p>{selectedProject && selectedProject.targetPlatform !== 'sap-integration-suite' && <a className="mt-2 inline-block text-xs text-primary-700 underline" href={`/dashboard/projects/${selectedProject.id}/settings`}>Open Project Setup</a>}</div></div>
        </section>
        <section className="rounded-2xl border bg-white dark:bg-gray-900 p-6 space-y-5">
            <div><h2 className="font-semibold text-lg">SAP Target Reference <span className="text-sm font-normal text-gray-500">(Optional)</span></h2><p className="text-sm text-gray-500 mt-1">Upload an existing SAP Integration Suite iFlow or native content package export. We inspect structure, metadata, adapters and resources to improve target compatibility. Scripts are never executed.</p></div>
            <div className="grid md:grid-cols-3 gap-3"><button onClick={() => setChoice('upload')} className={`text-left p-4 rounded-xl border ${choice === 'upload' ? 'border-primary-600 bg-primary-50/50' : ''}`}><b>Upload Native SAP iFlow ZIP</b><p className="text-xs text-gray-500 mt-2">One exported integration flow</p></button><button onClick={() => setChoice('upload')} className={`text-left p-4 rounded-xl border ${choice === 'upload' ? 'border-primary-600 bg-primary-50/50' : ''}`}><b>Upload Native Content Package ZIP</b><p className="text-xs text-gray-500 mt-2">Package export with iFlow artifacts</p></button><button onClick={skipReference} className={`text-left p-4 rounded-xl border ${choice === 'skip' ? 'border-primary-600 bg-primary-50/50' : ''}`}><b>Skip – Use Standard SAP Compatibility</b><p className="text-xs text-gray-500 mt-2">Continue using built-in SAP rules</p></button></div>
            {choice === 'upload' && <label className="flex cursor-pointer flex-col items-center justify-center rounded-xl border-2 border-dashed p-8 text-center hover:border-primary-500"><ArrowUpTrayIcon className="h-8 w-8 text-gray-400"/><span className="font-medium mt-2">{filename || 'Choose a native SAP ZIP archive'}</span><span className="text-xs text-gray-500 mt-1">ZIP · Up to 50 MB · No extraction to public folders</span><input type="file" accept=".zip,application/zip" className="sr-only" onChange={e => upload(e.target.files?.[0])}/></label>}
            {busy && <p className="text-sm text-primary-700">Validating and analyzing archive…</p>}{error && <p role="alert" className="rounded-lg bg-red-50 p-3 text-sm text-red-700">{error}</p>}
            {profile && <div className="rounded-xl bg-emerald-50 dark:bg-emerald-950/20 p-5 space-y-4"><div className="flex items-center justify-between"><div className="flex items-center gap-2 font-semibold text-emerald-800"><CheckCircleIcon className="h-5 w-5"/>Analysis complete · {profile.artifact_type.replace('_', ' ')}</div><button onClick={removeReference} className="text-xs text-red-700 underline">Remove reference</button></div><div className="grid grid-cols-2 md:grid-cols-5 gap-3 text-sm"><Metric label="iFlows" value={profile.artifacts.length}/><Metric label="Adapters" value={profile.adapter_inventory.length}/><Metric label="Scripts" value={profile.script_inventory.length}/><Metric label="Mappings" value={profile.mapping_inventory.length}/><Metric label="Resources" value={profile.resource_inventory.length}/></div><details><summary className="cursor-pointer text-sm font-medium">Analysis details</summary><pre className="mt-3 overflow-auto text-xs">{JSON.stringify({ artifacts: profile.artifacts, package_metadata: profile.package_metadata, adapter_inventory: profile.adapter_inventory, warnings: profile.validation_warnings }, null, 2)}</pre></details><p className="text-xs text-gray-600">Local structure analysis does not confirm SAP import or runtime compatibility. This profile expires after 30 days.</p></div>}
            {choice === 'skip' && <p className="text-sm rounded-lg bg-blue-50 dark:bg-blue-950/20 p-3 text-blue-900 dark:text-blue-100">Reference upload is optional. Standard SAP generation and local validation remain available without a reference project.</p>}
        </section>
        <section className="rounded-2xl border bg-white dark:bg-gray-900 p-6 space-y-4"><div><h2 className="font-semibold text-lg">Generated Artifact Compatibility</h2><p className="text-sm text-gray-500 mt-1">After generating target artifacts, select individual iFlow ZIPs for local structural checks. The saved reference profile is applied when available.</p></div><label className={`inline-flex rounded-lg border px-4 py-2 text-sm font-medium ${selectedProject ? 'cursor-pointer hover:border-primary-500' : 'opacity-50'}`}>{validating ? 'Validating…' : 'Select generated iFlow ZIPs'}<input type="file" accept=".zip,application/zip" multiple disabled={!selectedProject || validating} className="sr-only" onChange={e => validateGenerated(e.target.files)}/></label>{!selectedProject && <p className="text-xs text-amber-700">Select a project to associate validation results.</p>}{compatibility && <div className="rounded-xl bg-gray-50 dark:bg-gray-950 p-4 space-y-2"><p className="font-semibold">{compatibility.validation_status} · {compatibility.summary.passed} passed · {compatibility.summary.warnings} warnings · {compatibility.summary.failed} failed</p>{compatibility.artifacts.map(item => <div key={item.artifact_id} className="text-sm"><b>{item.artifact_id}</b> · {item.status}{[...item.errors, ...item.warnings].map((message, i) => <p key={i} className="ml-3 text-xs text-gray-500">{message}</p>)}</div>)}<p className="text-xs text-gray-500">{compatibility.disclaimer}</p></div>}</section>
        <section className="rounded-2xl border bg-white dark:bg-gray-900 p-6 space-y-4"><div className="flex items-center gap-3"><ShieldCheckIcon className="h-6 w-6 text-gray-400"/><div><h2 className="font-semibold">SAP Tenant Connection</h2><p className="text-sm text-gray-500">Credentials are sent only for this read-only test and are not stored by this workflow. Connection testing does not deploy anything.</p></div></div><div className="grid md:grid-cols-2 gap-3"><input aria-label="SAP tenant URL" placeholder="https://<tenant>.hana.ondemand.com" value={tenantUrl} onChange={e => setTenantUrl(e.target.value)} className="rounded-lg border p-3 text-sm dark:bg-gray-950"/><input aria-label="OAuth token URL" placeholder="https://<auth>.hana.ondemand.com/oauth/token" value={tokenUrl} onChange={e => setTokenUrl(e.target.value)} className="rounded-lg border p-3 text-sm dark:bg-gray-950"/><input aria-label="OAuth client ID" placeholder="OAuth client ID" value={clientId} onChange={e => setClientId(e.target.value)} className="rounded-lg border p-3 text-sm dark:bg-gray-950"/><input aria-label="OAuth client secret" type="password" autoComplete="new-password" placeholder="OAuth client secret" value={clientSecret} onChange={e => setClientSecret(e.target.value)} className="rounded-lg border p-3 text-sm dark:bg-gray-950"/></div><button disabled={testingConnection || !tenantUrl || !tokenUrl || !clientId || !clientSecret} onClick={testConnection} className="rounded-lg bg-primary-600 px-4 py-2 text-sm font-semibold text-white disabled:opacity-50">{testingConnection ? 'Testing…' : 'Test SAP Connection'}</button>{connection && <div className="rounded-lg bg-gray-50 dark:bg-gray-950 p-4 text-sm"><p className="font-semibold">Connection: {connection.connection_status || connection.error}</p><p className="text-xs text-gray-500 mt-2">Auth {connection.authentication || '—'} · Tenant {connection.tenant_connectivity || '—'} · CSRF {connection.csrf_validation || '—'} · Package API {connection.package_api_access || '—'} · Artifact API {connection.artifact_api_access || '—'} · Deployment permission {connection.deployment_permission || 'not verified'}</p>{connection.error && <p className="text-xs text-red-600 mt-2">{connection.error}</p>}</div>}<div className="text-xs text-gray-500">Readiness: SAP target selected · reference {profile ? 'analyzed' : choice === 'skip' ? 'skipped' : 'not uploaded'} · tenant {connection?.connection_status || 'not tested'}</div></section>
        <section className="rounded-2xl border border-amber-300 bg-white dark:bg-gray-900 p-6 space-y-4"><div><h2 className="font-semibold">Optional Test Deployment to SAP BTP</h2><p className="text-sm text-gray-600 dark:text-gray-400 mt-1">This creates a unique test content package, uploads a minimal iFlow, and requests deployment. The test package is not automatically deleted; cleanup is not implemented in this workflow, so you will need to remove it manually after reviewing the result.</p></div><label className="flex gap-3 text-sm"><input type="checkbox" checked={testApproved} onChange={e => setTestApproved(e.target.checked)}/><span>I approve creating and deploying a temporary SAP test package and iFlow. I understand the package may remain in my tenant.</span></label><button disabled={!testApproved || deployingTest || !selectedProject || !tenantUrl || !tokenUrl || !clientId || !clientSecret} onClick={runTestDeployment} className="rounded-lg bg-amber-700 px-4 py-2 text-sm font-semibold text-white disabled:opacity-50">{deployingTest ? 'Running SAP test deployment…' : 'Run SAP Test Deployment'}</button>{testDeployment && <div className="rounded-lg bg-gray-50 dark:bg-gray-950 p-4 text-sm"><p className="font-semibold">Deployment result: {String(testDeployment.deployment_status || 'unknown')}</p><p>Package: {String(testDeployment.package_id || 'not created')} · iFlow: {String(testDeployment.artifact_id || 'not uploaded')}</p><p className="text-xs text-gray-500 mt-1">Runtime verification: {String(testDeployment.runtime_verification || 'not checked')} · Cleanup: {String(testDeployment.cleanup || 'not performed')}</p>{Boolean(testDeployment.error) && <p className="text-xs text-red-600">{String(testDeployment.error)}</p>}</div>}</section>
        <section className="rounded-2xl border bg-white dark:bg-gray-900 p-6"><h2 className="font-semibold">Migration Readiness</h2>{readiness ? <div className="mt-3 grid grid-cols-2 md:grid-cols-4 gap-3 text-xs">{Object.entries(readiness).filter(([key]) => !key.endsWith('_at') && key !== 'requires_tenant_for_generation' && key !== 'requires_tenant_for_direct_deployment').map(([key, value]) => <div key={key} className="rounded-lg bg-gray-50 dark:bg-gray-950 p-3"><div className="text-gray-500">{key.replaceAll('_', ' ')}</div><b>{value}</b></div>)}</div> : <p className="mt-2 text-sm text-gray-500">Select a project to load its current checks.</p>}</section>
        <div className="text-xs text-gray-400 flex items-center gap-2"><CloudIcon className="h-4 w-4"/><DocumentMagnifyingGlassIcon className="h-4 w-4"/>OData individual iFlow delivery remains the supported direct deployment path; package ZIP integrity hash verification is not asserted.</div>
    </main>;
}

function Metric({ label, value }: { label: string; value: number }) { return <div className="rounded-lg bg-white/70 dark:bg-gray-900/50 p-3"><div className="text-lg font-bold">{value}</div><div className="text-xs text-gray-500">{label}</div></div>; }
