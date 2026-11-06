import { describe, it, expect, vi, beforeEach } from 'vitest';
import axios from 'axios';
import { projectApi } from '@/lib/api';

vi.mock('axios', () => {
    const mockAxios: any = vi.fn();
    mockAxios.defaults = { withCredentials: true };
    mockAxios.isAxiosError = (err: any) => Boolean(err?.isAxiosError);
    return { default: mockAxios };
});

describe('Project API', () => {
    beforeEach(() => {
        vi.clearAllMocks();
    });

    it('should list projects', async () => {
        const mockProjects = [
            { id: '1', name: 'Project 1' },
            { id: '2', name: 'Project 2' }
        ];

        (axios as any).mockResolvedValue({
            data: { projects: mockProjects },
            headers: { 'x-total-count': '100' },
        });

        const result = await projectApi.list('ws-1');
        expect(result.projects).toEqual(mockProjects);
        expect(axios).toHaveBeenCalledWith(expect.objectContaining({
            url: expect.stringContaining('/api/projects?workspaceId=ws-1'),
            method: 'GET',
        }));
    });

    it('should handle API errors', async () => {
        const axiosError: any = new Error('Server Error');
        axiosError.isAxiosError = true;
        axiosError.response = {
            status: 500,
            data: { error: 'Server Error' },
            headers: {},
        };

        (axios as any).mockRejectedValue(axiosError);

        await expect(projectApi.list('ws-1')).rejects.toThrow('Server Error');
    });
});

