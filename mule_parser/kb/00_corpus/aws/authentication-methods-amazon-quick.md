# Authentication methods - Amazon Quick

**Source:** [https://docs.aws.amazon.com/quick/latest/userguide/quick-action-auth.html](https://docs.aws.amazon.com/quick/latest/userguide/quick-action-auth.html)

---

Amazon Quick supports multiple authentication methods for action connectors. The available methods depend on the specific connector. During setup, you choose your authentication method from the **OAuth Configuration** options or from the connector-specific authentication settings.

## Default OAuth app

        Default OAuth app (also known as managed authentication or 3LO) is the recommended authentication method for personal access to third-party services. With this method, Amazon Quick manages the OAuth flow and no additional credentials are required from your organization.

**Key features:**

- 
                No additional credentials or configuration required. 
- 
                User-specific authentication through provider sign-in. 
- 
                Secure credential storage managed by Amazon Quick. 
- 
                Automatic token refresh. 
- 
                90-day refresh token lifecycle. 

**Setup process:**

- 
                Choose **Default OAuth app**as your OAuth configuration.
- 
                Complete the service provider sign-in flow. 
- 
                Grant the requested permissions. 
- 
                Confirm the connection. 

###### Note

Not all connectors support Default OAuth app. Check the connector-specific documentation for available authentication methods.

## Custom OAuth app

        Custom OAuth app authentication is for organizations that require specific control over the OAuth application configuration. Like Default OAuth app, this method uses a three-legged OAuth (3LO) flow where users sign in directly with the service provider. The difference is that you provide your own OAuth credentials instead of using the Amazon Quick managed application.

**Required information:**

- 
                Client ID 
- 
                Client Secret 
- 
                Domain URL 
- 
                Authorization URL 
- 
                Token URL 
- 
                Redirect URL 

**Setup process:**

- 
                Create an OAuth application in your service provider's developer console. 
- 
                Choose **Custom OAuth app**as your OAuth configuration.
- 
                Enter the credentials from your OAuth application. 
- 
                Complete the sign-in flow and validate the connection. 

## Service-to-Service OAuth

        Service-to-Service OAuth uses client credentials for server-to-server authentication without user interaction. This method is suitable for automated workflows and shared connectors where actions run under a service account.

**Required information:**

- 
                Client ID 
- 
                Client Secret 
- 
                Domain URL 
- 
                Token URL 
- 
                Service-specific parameters (varies by connector) 

## API key authentication

        Some connectors support API key authentication for service-level access. This method uses a single token for authentication and is common for connectors that don't support OAuth.

**Required information:**

- 
                Valid API key from the service provider 
- 
                Base URL or domain 
- 
                Service-specific parameters (such as email or account ID)