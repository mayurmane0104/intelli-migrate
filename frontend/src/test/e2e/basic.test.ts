import { test, expect } from '@playwright/test';

test.beforeEach(async ({ page }) => {
    // Perform login
    await page.goto('/login');
    await page.fill('input[type="email"]', 'admin@MigrationStudio.io');
    await page.fill('input[type="password"]', 'password123');
    await page.click('button:has-text("Sign In")');

    // Wait for redirect to organizations
    await expect(page).toHaveURL(/.*dashboard\/organizations/);
});

test('dashboard (organizations) loads correctly', async ({ page }) => {
    await expect(page.locator('h1')).toContainText('Organizations');
    await expect(page.getByRole('navigation').first()).toBeVisible();
});

test('navigation to settings works', async ({ page }) => {
    await page.click('text=Settings');
    await expect(page).toHaveURL(/.*settings/);
    await expect(page.locator('h1')).toContainText('Global Control');
});
