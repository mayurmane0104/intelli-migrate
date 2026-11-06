# Security and sandbox in apps in Quick - Amazon Quick

**Source:** [https://docs.aws.amazon.com/quick/latest/userguide/security-sandbox-apps.html](https://docs.aws.amazon.com/quick/latest/userguide/security-sandbox-apps.html)

---

Apps in Quick inherits the enterprise-grade authentication and authorization of Amazon Quick. Users access apps through their existing Quick identity, and every app runs inside a secure sandboxed iframe.

## Authentication

        - 
                **Single sign-on**— Users authenticate through their organization's identity provider (SSO, Active Directory, IAM) via Quick. No additional credentials are needed.
- 
                **Session security**— All app interactions run within an authenticated Quick session. Tokens are managed automatically by the platform.

## Authorization layers

        | Layer | What it controls | 
|---|---|
| App access | Who can view or edit the app (set by the app owner when sharing) | 
| Integration approval | Which connectors, spaces, and dashboards the app can access (set by the author during authoring) | 
| Runtime permissions | What data and actions are available to the viewer based on their own Quick permissions | 
| Connector auth | How the connector authenticates with the external API (configured by admin) | 

###### Important

App viewers can only access data they are already authorized to see in Quick. Embedding a dashboard visual does not bypass row-level security or column-level permissions.

## Integration consent model

        When the apps in Quick agent adds an integration to your app (action connector, space, dashboard visual, or AI inference), it prompts you for approval. This consent model ensures:

- 
                You know exactly what external calls your app makes. 
- 
                You control READ vs WRITE permissions. 
- 
                The published app never includes unapproved integrations. 
- 
                App viewers inherit the approved integration scope, not broader access. 

## Sandbox restrictions

        Every apps in Quick app runs inside a sandboxed iframe with strict security policies. The sandbox only permits script execution. All other capabilities (navigation, popups, direct network access) are restricted.

- 
                **Link navigation**— Apps cannot open external URLs directly. Users can follow links by pressing Cmd+Click (macOS) or Ctrl+Click (Windows).
- 
                **External resources**— The Content Security Policy blocks loading images, scripts, fonts, and other assets from external servers. Use inline SVG graphics, Base64-encoded image data, or image files loaded from a Amazon Quick space.
- 
                **Network requests**— App code cannot make direct HTTP requests to external servers. All communication with external systems goes through the secure bridge API or a registered action connector.
- 
                **File downloads**— File downloads must use the`downloadFile`function from the apps in Quick runtime library.