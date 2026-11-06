# Model Context Protocol (MCP) integration - Amazon Quick

**Source:** [https://docs.aws.amazon.com/quick/latest/userguide/mcp-integration.html](https://docs.aws.amazon.com/quick/latest/userguide/mcp-integration.html)

---

Model Context Protocol (MCP) is an open standard that defines how AI applications communicate with external tools and data sources. MCP uses a client-server architecture. AI applications act as clients that connect to MCP servers. Each MCP server exposes a set of tools. These tools are structured operations that the AI application can invoke to perform tasks, such as querying databases, calling APIs, or interacting with third-party services.

With MCP integration in Amazon Quick, you can connect to remote MCP servers so that your AI assistant can use the tools that those servers provide. For example, you can connect to an MCP server that provides access to your project management system. This connection allows the assistant to create tickets, look up issues, or update statuses as part of a conversation. Because MCP is an open standard, you can connect to any compatible server without building custom integrations for each tool.

You can connect to MCP servers that are reachable over the public internet. You can also connect to private MCP servers that are reachable from a virtual private cloud (VPC) in your AWS account by using a Amazon Quick VPC connection. The MCP server can be in the VPC, in another VPC reachable through peering or transit gateway, or on-premises reachable through AWS Direct Connect or VPN. For information about creating a VPC connection in Amazon Quick, see [Configuring VPC connections in Amazon Quick Sight](./working-with-aws-vpc.html).

###### Important

When you connect to a private MCP server through a VPC connection, the OAuth endpoints used by the MCP server must be reachable over the public internet. This applies to both user authentication (the authorization and token endpoints) and service authentication (the token endpoint). Private OAuth providers are not supported. MCP servers that do not require authentication are also supported.

## Supported capabilities

        
        MCP integration registers MCP server tools as actions in Amazon Quick.

- **Action connector**
- 
                    Each tool that an MCP server exposes registers as an action that your AI assistant can invoke during conversations. The integration secures these connections by using Proof Key for Code Exchange (PKCE) with the S256 challenge method and Resource Indicators (RFC 8707) to bind access tokens to specific MCP servers. 

## Before you begin

        
        Before you set up MCP integration, make sure that you have the following:

- 
                An MCP server endpoint with appropriate access. 
- 
                Authentication credentials for the MCP server, if required. For more information, see [Prepare MCP server setup and authentication](#mcp-integration-authentication).
- 
                An Amazon Quick Enterprise subscription. 
- 
                If you are connecting to a private MCP server, an active Amazon Quick VPC connection that has network access to the MCP server. For more information, see [Configuring VPC connections in Amazon Quick Sight](./working-with-aws-vpc.html).

###### Note

MCP integration supports remote servers only. HTTP streaming is preferred over Server-Sent Events (SSE). Local stdio connections are not supported.

## Prepare MCP server setup and authentication

        
        When you connect to an MCP server, Amazon Quick uses OAuth 2.0 Protected Resource Metadata (RFC 9728) to automatically discover authorization server information. The client sends an initial unauthenticated request to the MCP server. If the server responds with a 401 status that contains a `WWW-Authenticate` header with a `resource_metadata` URL, then Amazon Quick uses that URL to fetch the metadata document. If the header is not present, then Amazon Quick falls back to the well-known URI at the server root.

If the authorization server supports Dynamic Client Registration (DCR), then Amazon Quick automatically registers itself by using the discovered `registration_endpoint` from the authorization server metadata. No manual credential configuration is required. Amazon Quick supports both confidential and public client flows. DCR applies regardless of the authentication method that you choose.

If the authorization server does not support DCR, then you must manually provide credentials. Choose the authentication method that matches your MCP server requirements.

- **User authentication (OAuth)**
- 
                    Gather the following information from your MCP server configuration: - **Client ID**– The OAuth client ID.
- **Client Secret**– The OAuth client secret.
- **Token URL**– The OAuth token endpoint.
- **Authorization URL**– The OAuth authorization endpoint.
- **Redirect URL**– The OAuth redirect URI.
 
- **Service authentication (Service-to-Service)**
- 
                    Gather the following information from your MCP server configuration: - **Client ID**– The service client ID.
- **Client Secret**– The service client secret.
- **Token URL**– The service token endpoint.
 
- **No authentication**
- 
                    If the MCP server does not require authentication, no credentials are needed. Select this option for MCP servers that allow unauthenticated access. 

## Set up MCP integration

        
        After you prepare your MCP server configuration and authentication credentials, create your MCP integration.

- 
                In the Amazon Quick console, choose **Connectors**.
- 
                Choose the **Create for your team**tab.
- 
                Find and choose **Model Context Protocol (MCP)**.
- 
                On the **Create Integration**page, enter the integration details:- 
                        **Name**– A descriptive name for your MCP integration.
- 
                        **Description**(Optional) – The purpose of the integration.
- 
                        **MCP server endpoint**– The URL of the MCP server.
- 
                        **Connection type**– Choose how Amazon Quick connects to the MCP server:- 
                                **Public network**– Use this option for MCP servers that are reachable over the public internet.
- 
                                A named VPC connection – Use this option for private MCP servers. The dropdown lists the VPC connections that are configured on your Amazon Quick account. Choose the connection that has network access to your MCP server. If you don't see your VPC connection in the list, confirm that it is fully provisioned and active. For more information, see [Configuring VPC connections in Amazon Quick Sight](./working-with-aws-vpc.html).
 
- 
                                
 
- 
                        
- 
                Choose **Next**.
- 
                Select the authentication method (user, service, or no authentication). 
- 
                Enter the appropriate configuration details. 
- 
                Choose **Create and continue**.
- 
                Review the integration details. 
- 
                Choose **Next**.
- 
                Share the integration with other users if needed. 

After you create your MCP integration, Amazon Quick discovers the available tools and registers them as actions.

## Review integration

        
        After you configure authentication, review the MCP integration capabilities:

- 
                The system connects to the MCP server and discovers available capabilities. 
- 
                Review the list of available actions and tasks that the MCP server provides. 
- 
                Confirm the integration configuration and capabilities. 

### Capability discovery

During the connection process that is described in [Prepare MCP server setup and authentication](#mcp-integration-authentication), Amazon Quick also discovers and registers the tools that the MCP server provides. After discovery completes, each tool is listed as an action that you can review and turn on.

## Manage MCP integrations

        To edit, share, or delete your integration, see [Managing existing integrations](./integration-workflows.html#managing-existing-integrations).

## Troubleshooting

        Use the following guidance to diagnose and resolve common issues when you create or use an MCP integration in Amazon Quick.

### Connector creation issues

- 
                    **Connector passes discovery but fails at publish with**– This error usually means that one or more tool definitions in your MCP server's`Creation failed``tools/list`response contain an invalid`inputSchema`. Amazon Quick validates each tool's`inputSchema`against JSON Schema Draft 7 or later during the publish phase.The most common cause is the deprecated Draft 3 syntax, where `required`is a boolean inside a property definition (for example,`"required": true`). In JSON Schema Draft 7 and later,`required`must be an array of property names at the schema root, as a sibling of`properties`.Update your tool definitions to use the correct format and redeploy your MCP server. After you redeploy, delete the failed connector and create a new one to retrigger discovery and publish. The following example shows the incorrect Draft 3 syntax: `{ "type": "object", "properties": { "logNumber": { "type": "string", "description": "The permit log number", "required": true } } }`The following example shows the correct Draft 7 syntax: `{ "type": "object", "properties": { "logNumber": { "type": "string", "description": "The permit log number" } }, "required": ["logNumber"] }`Some MCP framework libraries and code generators emit Draft 3 syntax by default. Check your framework documentation for the option that selects the JSON Schema output version. You can also validate your schemas with any JSON Schema Draft 7 validator before you deploy. For more information about `inputSchema`requirements, see[Tools](https://modelcontextprotocol.io/specification/latest/server/tools)in the Model Context Protocol specification.You might also notice that connector creation hangs for two to five minutes before it fails. The elapsed time reflects internal retries during the publish phase, not a network timeout. The fix is the same: check your tool `inputSchema`definitions for JSON Schema Draft 7 compliance.

### VPC connection issues

- 
                    **VPC connection is not listed in the**– The VPC connection might appear in the dropdown before provisioning is complete. Wait until the VPC connection shows as available on the Amazon Quick admin page before you create an MCP integration against it. For more information, see**Connection type**dropdown, or MCP creation fails immediately after you select it[Configuring VPC connections in Amazon Quick Sight](./working-with-aws-vpc.html).
- 
                    **MCP creation fails because the MCP server hostname cannot be resolved**– Amazon Quick does not use the default VPC DNS resolver for MCP integrations. You must populate the**DNS resolver endpoints**field on the VPC connection with Route 53 Resolver inbound endpoint IP addresses that can resolve your MCP server hostname. This requirement applies to both private hostnames and to public hostnames that you want to resolve to a private address from within the VPC, such as endpoints fronted by AWS PrivateLink or a Route 53 private hosted zone. Without these resolver endpoints, the MCP server hostname cannot be resolved and integration creation fails. For more information, see[Configuring VPC connections in Amazon Quick Sight](./working-with-aws-vpc.html).
- 
                    **MCP server is unreachable from the VPC connection**– Traffic from Amazon Quick to your MCP server originates from the subnets that you selected during VPC connection setup. Confirm that route tables, network ACLs, and security groups allow traffic between those subnets and the MCP server endpoint. For general VPC networking guidance, see[Configuring VPC connections in Amazon Quick Sight](./working-with-aws-vpc.html).
- 
                    **Authentication fails when you use a private MCP server**– When you connect to a private MCP server through a VPC connection, the OAuth endpoints used by the MCP server must still be reachable over the public internet. This applies to both user authentication (authorization and token endpoints) and service authentication (token endpoint). Private OAuth providers are not supported. Confirm that the OAuth URLs that your MCP server returns in its protected resource metadata resolve over the public internet.

### Microsoft Entra ID issues

If your MCP server uses Microsoft Entra ID as the authorization server, the following errors are common during connector setup. These issues apply to both public network connections and private MCP servers that you reach through a VPC connection.

- 
                    `AADSTS9010010`– the v2.0 endpoint rejects the resource parameter`resource`parameter on OAuth requests as required by the MCP specification (RFC 8707). The Entra ID v2.0 endpoint rejects requests that include both a`resource`parameter and`scope`values. To resolve this error, configure your app registration to use the Entra ID v1.0 OAuth endpoints and set`accessTokenAcceptedVersion`to`2`in the app manifest.
- 
                    `AADSTS90009`– application requests a token for itself

If you encounter an issue that is not covered in the preceding sections, contact AWS Support through the Amazon Quick console or AWS Support Center.

## Limitations

        
        When you use MCP integrations in Amazon Quick, be aware of the following limitations:

- 
                MCP operations have a fixed 60-second timeout. Operations that exceed this limit automatically fail with an HTTP 424 error. 
- 
                For MCP servers that you reach through a VPC connection, the OAuth endpoints used by the MCP server must be reachable over the public internet. This applies to both user authentication and service authentication. Private OAuth providers are not supported. 
- 
                Custom HTTP headers are not supported in MCP operations. Only standard system headers are transmitted. 
- 
                Tool lists remain static after initial registration. To pick up server-side tool changes, you must delete the integration and recreate it. 
- 
                Connector creation might fail if the Amazon Quick callback URI is not allow-listed by third-party providers. 
- 
                Server connectivity issues result in immediate failure without retry attempts. 
- 
                Step-up authorization is not supported. If an MCP server requires additional scopes after the initial authorization (HTTP 403 with `insufficient_scope`), then you must re-authorize the entire connection. Incremental permission upgrades are not available.
- 
                Scope handling has the following limitations: - 
                        Amazon Quick does not extract the `scope`parameter from the server's initial 401`WWW-Authenticate`challenge. Amazon Quick determines scopes from the Protected Resource Metadata document instead.
- 
                        When the metadata does not specify supported scopes, Amazon Quick applies default scopes rather than omitting them. This behavior might cause authentication failures with servers that do not recognize the default scopes. 
 
- 
                        
- 
                Only Dynamic Client Registration (DCR) is supported for automatic client registration. Client ID Metadata Documents are not supported. 
- 
                Well-known URI discovery uses the server root path only. Path-specific metadata locations (path-insertion discovery) are not supported. This limitation might prevent discovery of servers that serve metadata only at path-specific URIs.