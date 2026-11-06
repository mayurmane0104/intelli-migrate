import { beforeEach, describe, expect, it, vi } from 'vitest';
import { fireEvent, render, screen, waitFor } from '@testing-library/react';
import SAPOnboardingPage from '@/app/dashboard/sap-onboarding/page';

vi.mock('@/contexts/AppContext', () => ({
    useApp: () => ({ selectedProject: { id: 'project-1', name: 'Payroll migration', targetPlatform: 'sap-integration-suite' } }),
}));

const profile = {
    reference_id: 'ref-1', artifact_type: 'iflow', analysis_status: 'completed',
    artifacts: [{ artifact_id: 'PayrollFlow' }], adapter_inventory: [], resource_inventory: [{}],
    script_inventory: [{}], mapping_inventory: [], validation_warnings: [], package_metadata: {},
};

function response(body: unknown, ok = true) {
    return { ok, status: ok ? 200 : 422, json: async () => body } as Response;
}

describe('SAP target onboarding', () => {
    beforeEach(() => {
        vi.restoreAllMocks();
        vi.stubGlobal('fetch', vi.fn(async (input: RequestInfo | URL, init?: RequestInit) => {
            const url = String(input);
            if (url.startsWith('/api/sap/reference?')) return response({ reference: null });
            if (url.startsWith('/api/sap/readiness')) return response({ migration_readiness: 'ready_for_generation', reference_project: 'skipped' });
            if (url === '/api/sap/reference' && init?.method === 'POST') return response({ ...profile, persisted: true });
            if (url === '/api/sap/reference' && init?.method === 'PUT') return response({ mode: 'standard' });
            if (url === '/api/sap/tenant/test-connection') return response({ connection_status: 'connected', authentication: 'passed', tenant_connectivity: 'passed', csrf_validation: 'passed', package_api_access: 'passed', artifact_api_access: 'passed', deployment_permission: 'not_verified' });
            if (url === '/api/sap/tenant/test-deployment') return response({ deployment_status: 'verified', package_id: 'TISSA_TEST_123', artifact_id: 'TISSA_TEST_FLOW_123', runtime_verification: 'passed', cleanup: 'not_supported' });
            if (url === '/api/sap/compatibility/validate') return response({ validation_status: 'passed', reference_used: true, summary: { total_artifacts: 1, passed: 1, warnings: 0, failed: 0 }, artifacts: [], disclaimer: 'Local structural validation only.' });
            return response({ error: `Unhandled ${init?.method || 'GET'} ${url}` }, false);
        }));
    });

    it('allows users to skip references without uploading an archive', async () => {
        render(<SAPOnboardingPage />);
        fireEvent.click(screen.getByText('Skip – Use Standard SAP Compatibility'));
        await waitFor(() => expect(fetch).toHaveBeenCalledWith('/api/sap/reference', expect.objectContaining({ method: 'PUT' })));
        expect(screen.getByText(/Reference upload is optional/)).toBeInTheDocument();
    });

    it('uploads and displays native reference analysis', async () => {
        const { container } = render(<SAPOnboardingPage />);
        fireEvent.click(screen.getByText('Upload Native SAP iFlow ZIP'));
        const file = new File(['native archive'], 'reference.zip', { type: 'application/zip' });
        const input = document.querySelector('input[type="file"]') as HTMLInputElement;
        fireEvent.change(input, { target: { files: [file] } });
        expect(await screen.findByText(/Analysis complete · iflow/)).toBeInTheDocument();
        fireEvent.click(screen.getByText('Analysis details'));
        expect(container.querySelector('pre')?.textContent).toContain('PayrollFlow');
        expect(screen.getByText(/Local structure analysis does not confirm/)).toBeInTheDocument();
    });

    it('tests the tenant connection without reporting deployment permission', async () => {
        render(<SAPOnboardingPage />);
        fireEvent.change(screen.getByLabelText('SAP tenant URL'), { target: { value: 'https://tenant.hana.ondemand.com' } });
        fireEvent.change(screen.getByLabelText('OAuth token URL'), { target: { value: 'https://auth.hana.ondemand.com/oauth/token' } });
        fireEvent.change(screen.getByLabelText('OAuth client ID'), { target: { value: 'client' } });
        fireEvent.change(screen.getByLabelText('OAuth client secret'), { target: { value: 'secret-value' } });
        fireEvent.click(screen.getByText('Test SAP Connection'));
        expect(await screen.findByText(/Connection: connected/)).toBeInTheDocument();
        expect(screen.getByText(/Deployment permission not_verified/)).toBeInTheDocument();
        expect((screen.getByLabelText('OAuth client secret') as HTMLInputElement).value).toBe('');
    });

    it('requires explicit approval before starting a test deployment', async () => {
        render(<SAPOnboardingPage />);
        const set = (label: string, value: string) => fireEvent.change(screen.getByLabelText(label), { target: { value } });
        set('SAP tenant URL', 'https://tenant.hana.ondemand.com');
        set('OAuth token URL', 'https://auth.hana.ondemand.com/oauth/token');
        set('OAuth client ID', 'client'); set('OAuth client secret', 'secret-value');
        const button = screen.getByText('Run SAP Test Deployment') as HTMLButtonElement;
        expect(button.disabled).toBe(true);
        fireEvent.click(screen.getByRole('checkbox'));
        expect(button.disabled).toBe(false);
        fireEvent.click(button);
        expect(await screen.findByText(/Deployment result: verified/)).toBeInTheDocument();
        const request = (fetch as ReturnType<typeof vi.fn>).mock.calls.find(([url]) => url === '/api/sap/tenant/test-deployment')?.[1] as RequestInit;
        expect(JSON.parse(String(request.body))).toMatchObject({ approved: true, approval_text: expect.stringContaining('I approve') });
        expect(screen.getByText(/Cleanup: not_supported/)).toBeInTheDocument();
    });
});
