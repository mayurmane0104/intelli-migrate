import { test, expect } from '@playwright/test';

test.describe('Comprehensive Application Flow', () => {
    test.beforeEach(async ({ page }) => {
        // 1. Authentication Flow
        await page.goto('/login');
        await page.fill('input[type="email"]', 'admin@MigrationStudio.io');
        await page.fill('input[type="password"]', 'password123');
        await page.click('button:has-text("Sign In")');
        await expect(page).toHaveURL(/.*dashboard\/organizations/);
    });

    test('Organization and Workspace Navigation', async ({ page }) => {
        // 2. Organization Selection
        await page.click('div.group:has-text("Acme Corporation")');
        await page.waitForURL(/.*workspaces/);
        await expect(page.locator('nav').getByText('Acme Corporation').first()).toBeVisible({ timeout: 15000 });

        // 3. Workspace Selection
        await page.click('div.group:has-text("Development")');
        await page.waitForURL(/.*projects/);
        await expect(page.locator('h1')).toContainText('Projects', { timeout: 10000 });

        // 4. Project Selection - Navigates to Project Dashboard
        await page.locator('div.group:has-text("Order Processing API")').first().click();
        await page.waitForURL(/.*projects\/p-\d+/);
        await expect(page.locator('h1').first()).toContainText('Order Processing API', { timeout: 15000 });
    });

    test('Project Editor and Migration Flow', async ({ page }) => {
        // Navigate via Dashboard flow
        await page.goto('/dashboard/organizations');
        await page.click('div.group:has-text("Acme Corporation")');
        await page.click('div.group:has-text("Development")');
        await page.locator('div.group:has-text("Order Processing API")').first().click();
        await page.waitForURL(/.*projects\/p-\d+/);

        // Click "Start Migration" button (if total files > 0)
        // If not, we check if the button or the editor link exists.
        const startButton = page.getByRole('button', { name: /Start Migration|Import Code/ });
        await expect(startButton).toBeVisible({ timeout: 15000 });
        await page.goto(page.url() + '/editor');
        await page.waitForURL(/.*editor/);
        await expect(page.locator('nav[aria-label="Breadcrumb"]').getByText('Order Processing API').first()).toBeVisible({ timeout: 15000 });

        // 6. Migration History (Sidebar)
        await page.locator('aside nav').getByText('History').click();
        await page.waitForURL(/.*history/);
        await expect(page.locator('h1')).toContainText('Migration History', { timeout: 15000 });
    });

    test('Settings and Profile Flow', async ({ page }) => {
        // 7. Settings Access (via Sidebar)
        await page.locator('aside nav').getByText('Settings').click();
        await page.waitForURL(/.*settings/);
        await expect(page.locator('h1')).toContainText('Global Control', { timeout: 10000 });

        // 8. Profile Access (via Topbar Menu)
        const userMenu = page.locator('header').getByRole('button', { name: /Harsh|User/ });
        await userMenu.click();
        await page.click('text=Profile');
        await page.waitForURL(/.*profile/);
        await expect(page.locator('h1')).toContainText('Account Settings', { timeout: 10000 });
    });
});
