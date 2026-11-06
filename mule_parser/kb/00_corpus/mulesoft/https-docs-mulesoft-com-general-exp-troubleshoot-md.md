# https://docs.mulesoft.com/general/exp-troubleshoot.md

**Source:** [https://docs.mulesoft.com/general/exp-troubleshoot.md](https://docs.mulesoft.com/general/exp-troubleshoot.md)

---

```
# Troubleshoot the Enhanced Experience
> For the full documentation index, see: https://docs.mulesoft.com/llms.txt
When authentication, connection, or data issues occur in the enhanced experience, use this
information to identify the cause and find solutions. Common issues include permission errors,
provider connection failures, rate limiting, missing data, and SSL certificate problems.
## Authentication and Permission Errors
Authentication and permission errors prevent you from accessing features or performing actions.
### 403 Forbidden Errors
If you receive a 403 Forbidden error:
1.  Check your permissions:
    1.  Review your Access Management permissions in
        [Enhanced Experience Permissions](exp-home-start#permissions).
    2.  Verify that you have the required permission for the action:
        See [Enhanced Experience Permissions](exp-home-start#permissions) for more information.
    3.  Ask your administrator to review your role assignments if needed.
2.  Check business group access:
    1.  Verify that youâ€™re working in the correct business group.
    2.  Confirm that you have permissions in the selected business group, not just at the
        organization level.
    3.  Ask your administrator to grant access to the specific business group if needed.
### 401 Unauthorized Errors
If you receive a 401 Unauthorized error:
1.  Check session status:
    1.  Verify that youâ€™re still signed in to the enhanced experience.
        If your session expired, sign in again.
    2.  Check the browser console for authentication errors (if you have developer tools access).
2.  Clear cached credentials:
    1.  Sign out of the enhanced experience.
    2.  Clear your browser cache and cookies.
    3.  Sign in again.
3.  Try a different browser:
    1.  Test with a different browser or incognito/private mode.
    2.  Disable browser extensions that might interfere with authentication.
### Permission Errors for Specific Actions
If you canâ€™t perform a specific action:
1.  Verify prerequisites:
    Some actions require specific service states (such as active or registered).
    1.  Check that required configurations are in place (for example, a gateway must be configured
        before creating instances).
    2.  Verify that the service exists and hasnâ€™t been deleted.
2.  Check feature availability:
    1.  Confirm that the feature is available in your environment.
        Some features might be in preview or require specific product access.
    2.  Ask your administrator about feature availability if needed.
## Connection Failures
Connection failures prevent you from connecting providers, running scanners, or accessing external
systems.
### Provider Connection Issues
If you canâ€™t connect a provider:
1.  Verify credentials:
    1.  Check that you entered valid credentials for the provider.
    2.  Confirm that the credentials havenâ€™t expired.
    3.  Test the credentials directly with the providerâ€™s console or API.
2.  Check network connectivity:
    1.  Verify that your network allows outbound connections to the provider.
    2.  Check for firewall rules that might block connections.
    3.  Confirm that proxy settings are correct if your organization uses a proxy.
3.  Review provider permissions:
    1.  Verify that the credentials have the required permissions on the provider side.
    2.  Check that the account has access to the resources you want to discover.
    3.  Review the providerâ€™s documentation for required IAM roles or permissions.
4.  Check provider status:
    1.  Verify that the providerâ€™s API is available and not experiencing outages.
    2.  Check the providerâ€™s status page for known issues.
    3.  Try connecting to the provider again after a few minutes.
### Scanner Connection Failures
If a scanner fails to connect or discover services:
1.  Check scanner authentication:
    1.  Verify that the scannerâ€™s authentication credentials are valid.
    2.  Refresh credentials if theyâ€™ve expired.
    3.  Reauthenticate with the provider if needed.
2.  Review scanner permissions:
    1.  Confirm that the scanner has permissions to access the target resources.
    2.  Check that the account has list or describe permissions for the resource types you want to
        discover.
    3.  Verify that the scanner can access all regions or zones if applicable.
3.  Check scanner configuration:
    1.  Review the scannerâ€™s settings in **Platform** > **Providers** > scanner name > **Settings**.
    2.  Verify that the scanner is targeting the correct resources or namespaces.
    3.  Check that filters are not excluding the resources you expect to discover.
4.  Review scan history:
    1.  From **Platform** > **Providers**, select the scanner to view its scan history.
    2.  Look for error messages in recent scan attempts.
    3.  Check whether previous scans succeeded or when the problem started.
### Gateway Connection Issues
If you canâ€™t connect to a gateway or gateway connections fail:
1.  Verify gateway endpoint:
    1.  Check that the gateway URL is correct and accessible.
    2.  Test the gateway endpoint from your network (for example, using curl or a browser).
    3.  Confirm that the gateway is running and accepting connections.
2.  Check SSL/TLS certificates:
    1.  Verify that the gatewayâ€™s SSL certificate is valid and not expired.
    2.  Check that the certificate chain is complete.
    3.  If using a self-signed certificate, verify that itâ€™s trusted by your organizationâ€™s
        certificate authority.
3.  Review gateway credentials:
    1.  Confirm that youâ€™re using valid credentials for the gateway.
    2.  Check that the credentials have the required permissions.
    3.  Verify that authentication is configured correctly on the gateway side.
4.  Check network path:
    1.  Verify that your network allows connections to the gatewayâ€™s port (typically 443 for HTTPS).
    2.  Check for firewall rules that might block connections.
    3.  Confirm that proxy settings are correct if your organization uses a proxy.
## Rate Limiting and Throttling
Rate limiting occurs if you exceed the allowed number of requests in a certain period.
### 429 Too Many Requests Errors
If you receive a 429 Too Many Requests error:
1.  Wait before retrying:
    Rate limits typically reset after a short period (usually 1â€“5 minutes).
    1.  Check the error message for retry-after information.
    2.  Wait at least 60 seconds before retrying the operation.
2.  Reduce request frequency:
    1.  Avoid running multiple scanners simultaneously if they target the same provider.
    2.  Space out manual scan runs rather than triggering them in quick succession.
    3.  Reduce the frequency of scheduled scans if youâ€™re hitting limits regularly.
3.  Review operation patterns:
    1.  Check whether automated processes or scripts are making excessive requests.
    2.  Review scanner schedules to avoid overlapping runs.
    3.  Contact your administrator if rate limits donâ€™t align with your usage needs.
4.  Provider rate limits:
    Provider rate limits (AWS, Azure, GCP) are separate from enhanced experience rate limits.
    1.  Check the providerâ€™s rate limit documentation for their specific limits.
    2.  Consider requesting a rate limit increase from the provider if needed.
## Data Not Appearing
If you expect to see data, but itâ€™s not appearing in the enhanced experience:
### Services Not Showing After Scanner Run
If a scanner ran successfully, but services arenâ€™t appearing:
1.  Check scanner results:
    1.  From **Platform** > **Providers**, select the scanner to view its scan history.
    2.  Verify that the scan reported discovering new services.
    3.  Check for any error messages in the scan history.
2.  Review catalog filters:
    1.  From **Portfolio**, check that youâ€™re viewing the correct catalog (APIs, Agents, MCP
        Servers, LLM Proxies, or Gateways).
    2.  Clear any filters that might be hiding the services.
    3.  Try using the search function to find specific services by name.
3.  Verify service type mapping:
    1.  Confirm that the discovered services are of the expected type.
    2.  Check that the providerâ€™s resources map to the catalog youâ€™re checking.
        Some resources might not be imported if they donâ€™t meet the criteria for the catalog.
4.  Check business group context:
    1.  Verify that youâ€™re viewing the correct business group or organization.
        Services might be registered in a different business group than youâ€™re currently viewing.
    2.  Switch business groups if needed to find the services.
### Metrics Not Displaying
If you expect to see metrics but theyâ€™re not appearing:
1.  Verify monitoring is enabled:
    1.  Check that monitoring is configured for the service or instance.
    2.  From the service detail page, select **Monitoring** to verify that monitoring is active.
    3.  Contact your administrator if monitoring needs to be enabled.
2.  Check time range:
    1.  Verify that youâ€™re viewing an appropriate time range for the data.
    2.  Expand the time range to see if data exists outside the current window.
        New services might not have historical data.
3.  Allow time for data collection:
    Metrics might take several minutes to appear after an event occurs.
    1.  Wait at least 5â€“10 minutes after creating or updating a service before expecting metrics.
    2.  Check again after the next monitoring collection cycle.
4.  Verify service activity:
    1.  Confirm that the service is receiving traffic or requests.
    2.  Check that the service is deployed and running.
    3.  Review service logs to verify that requests are being processed.
### Cost or Token Usage Data Missing
If cost or token usage data isnâ€™t appearing:
1.  Check governance strategy scope:
    1.  From **Governance** > **Strategies**, verify that a governance strategy targets the service.
    2.  Confirm that the strategy is active and not in draft state.
    3.  Check that the strategy includes cost or token tracking.
2.  Allow time for data aggregation:
    1.  Cost and token usage data can take several hours to appear after usage occurs.
    2.  Check again after 24 hours for the most complete data.
        Historical data might not be available for newly registered services.
3.  Verify service type:
    1.  Cost and token usage tracking applies primarily to LLM proxies and agents.
        APIs and other service types might not generate cost data.
    2.  Check the service type in **Portfolio** to confirm it supports cost tracking.
## Async Operations and Delays
Some operations run in the background and can take time to complete.
### Operations Appearing Stuck
If an operation appears stuck or takes longer than expected:
1.  Check operation type:
    Governance insights and conformance scoring run asynchronously and can take several minutes.
    1.  Large scanner runs discovering many services can take 10â€“30 minutes or longer.
        Policy application to multiple instances might process in the background.
2.  Review status indicators:
    1.  Look for progress indicators or status messages in the UI.
    2.  Check the service or scanner detail page for updated status.
    3.  Refresh the page to see if the operation has completed.
3.  Wait for background processing:
    1.  Allow at least 15â€“30 minutes for governance insights to complete after creating a strategy.
        Scanner runs can take varying amounts of time depending on the number of resources
        discovered.
        Cost data aggregation can take several hours.
4.  Check for errors:
    1.  Review the browser console for error messages (if you have developer tools access).
    2.  Check notification areas for error alerts.
    3.  If no error appears, but the operation doesnâ€™t complete after 30 minutes, contact support.
### Checking Background Job Status
To check the status of background operations:
1.  Scanner runs:
    1.  From **Platform** > **Providers**, select the scanner.
    2.  View the scan history on the **Overview** tab.
        The most recent entry shows the current or last completed scan.
2.  Governance operations:
    1.  From **Governance** > **Strategies**, select the strategy.
    2.  Check the status indicator next to the strategy name.
    3.  Review conformance reports for completion status.
3.  Service operations:
    1.  From **Portfolio**, select the service.
    2.  Check for status messages or progress indicators on the detail page.
    3.  Look for notifications in the notification area.
## Browser and Client Issues
Browser or client problems can affect your experience using the enhanced experience.
### Page Not Loading or Displaying Correctly
If pages donâ€™t load or appear correctly:
1.  Clear browser cache:
    1.  Clear your browser cache and cookies.
    2.  Hard refresh the page (Ctrl+Shift+R on Windows/Linux, Cmd+Shift+R on Mac).
    3.  Try accessing the enhanced experience in incognito/private mode.
2.  Check browser compatibility:
    1.  Verify that youâ€™re using a supported browser (Chrome, Firefox, Safari, or Edge).
    2.  Update your browser to the latest version.
    3.  Check [Browser Support for Anypoint Platform](browser-support) for specific version
        requirements.
3.  Disable browser extensions:
    1.  Temporarily disable browser extensions that might interfere with the enhanced experience.
        Ad blockers, privacy extensions, or script blockers can prevent features from working.
    2.  Test with extensions disabled to identify conflicts.
4.  Check browser console:
    1.  Open browser developer tools (F12 or Cmd+Option+I).
    2.  Review the console for error messages.
    3.  Share error messages with your administrator or support team if needed.
### Session Timeout Issues
If your session expires frequently or unexpectedly:
1.  Adjust session settings:
    1.  Check your organizationâ€™s session timeout policy.
    2.  Ask your administrator about extending session duration if needed.
        Security policies can limit maximum session duration.
2.  Stay active:
    1.  Keep a tab or window with the enhanced experience open and active.
        Periodic interaction prevents session timeouts.
    2.  Refresh the page if youâ€™ve been idle for an extended period.
3.  Re-authenticate:
    1.  Sign out and sign in again to start a fresh session.
    2.  Clear browser cache if re-authentication fails.
    3.  Check with your administrator if authentication fails repeatedly.
## SSL and Certificate Issues
SSL and certificate problems prevent secure connections to providers or gateways.
### Certificate Validation Failures
If you encounter certificate validation errors:
1.  Check certificate validity:
    1.  Verify that the certificate hasnâ€™t expired.
    2.  Confirm that the certificate is issued by a trusted certificate authority.
    3.  Check that the certificateâ€™s common name or subject alternative name matches the hostname.
2.  Review certificate chain:
    1.  Verify that the complete certificate chain is present.
    2.  Check that intermediate certificates are installed correctly.
    3.  Confirm that the root certificate is trusted by your system.
3.  Self-signed certificates:
    1.  If using self-signed certificates, verify that theyâ€™re trusted by your organization.
    2.  Ask your administrator about adding the certificate to your systemâ€™s trusted store.
    3.  Consider using certificates from a trusted certificate authority for production systems.
4.  Contact your administrator:
    1.  Share certificate error details with your administrator or security team.
        Your organization might need to update certificate trust settings.
    2.  Work with your administrator to resolve certificate trust issues.
## Getting Additional Help
If these troubleshooting steps donâ€™t resolve your issue:
1.  Contact your administrator:
    1.  Share specific error messages and steps to reproduce the problem.
    2.  Provide details about what you were trying to accomplish.
    3.  Include screenshots if they help illustrate the issue.
2.  Check documentation:
    1.  Review feature-specific documentation for additional guidance.
    2.  Check [Release Notes](exp-release-notes) for known issues.
3.  Gather diagnostic information:
    1.  Note exact error message and error code if provided.
    2.  Record the steps to reproduce the issue.
    3.  Check browser console for technical error details (F12 or Cmd+Option+I).
    4.  Note the time the error occurred and any patterns (happens consistently or intermittently).
## See Also
- [Enhanced Experience Permissions](exp-home-start#permissions)
- [Viewing Providers](exp-providers-manage)
- [Managing Scanners](exp-scanners-manage)
- [Browser Support for Anypoint Platform](browser-support)
```