# Action connector APIs - Amazon Quick

**Source:** [https://docs.aws.amazon.com/quick/latest/userguide/action-connector-apis.html](https://docs.aws.amazon.com/quick/latest/userguide/action-connector-apis.html)

---

Action connector APIs let you programmatically create and manage connections between Amazon Quick and external services. These APIs support the action integration functionality that allows users to perform actions in third-party applications directly from Amazon Quick chat interfaces and automated workflows.

## What are action connector APIs?

        Action connectors serve as the foundational resources that enable integration with first and third party applications. Through these APIs, you can authenticate to applications, manage permissions, and control which actions are available to users within your Amazon Quick applications.

### How action connector APIs support action integrations

Action connector APIs provide the backend infrastructure for Amazon Quick action integrations. When you create an action connector through the API, you establish a secure connection that lets you:

- 
                    Execute actions in external services through chat interfaces. 
- 
                    Perform automated workflows in background processes. 
- 
                    Integrate third-party services with Amazon Quick applications. 
- 
                    Manage authentication and permissions for service access. 

The APIs handle the complex authentication flows, credential management, and permission controls needed to securely connect Amazon Quick with external services.

## Authentication methods

        Action connector APIs support multiple authentication methods to accommodate different use cases and security requirements:

### Managed authentication (3LO)

Three-Legged OAuth provides the simplest setup for personal access to third-party services:

- 
                    No initial configuration required. 
- 
                    User-specific authentication through service provider login. 
- 
                    Automatic token refresh with 90-day lifecycle. 
- 
                    Secure credential storage managed by Amazon Quick. 

### Service-to-service authentication (2LO)

For complex enterprise integrations:

- 
                    Supports client credentials OAuth flow. 
- 
                    Enables system-to-system interactions. 
- 
                    Requires client ID, client secret, and token URL configuration. 
- 
                    Suitable for automated workflows requiring sophisticated security. 
- 
                    OAuth - Dynamic Client Registration (DCR - applicable only for select MCP servers). 

### API key authentication

Simplified authentication for automated workflows:

- 
                    Single token-based authentication. 
- 
                    Service-level permissions. 
- 
                    Ideal for background processes and scheduled actions. 
- 
                    Requires valid API key from target service. 

### Basic Auth

Basic authentication provides a simple username/password authentication method:

- 
                    Uses standard HTTP Basic Authentication headers. 
- 
                    Credentials are base64 encoded. 
- 
                    Suitable for services that don't support OAuth or API keys. 
- 
                    Requires secure HTTPS connection. 
- 
                    Not recommended for public-facing services. 

### None

No authentication required:

- 
                    Used for public APIs and services. 
- 
                    No credentials or tokens needed. 
- 
                    Limited to read-only or public operations. 
- 
                    Typically used for public data feeds and documentation. 
- 
                    Should not be used for sensitive operations. 

## Permissions and access control

        Action connector APIs implement comprehensive permission controls through Access Control Lists (ACLs):

### Resource-level permissions

- 
                    **Owner**- Full control including delete and permission management.
- 
                    **Contributor**- Can use and modify connector settings.
- 
                    **Viewer**- Can view connector details and use enabled actions.

### API operations for permission management

- 
                    `DescribeActionConnectorPermissions`- Retrieve current permission settings.
- 
                    `UpdateActionConnectorPermissions`- Grant or revoke user permissions.

## Supported connector categories

         
            ### Dual-purpose connectors

These connectors support both action integrations and knowledge base creation:

- 
                    **Amazon S3**- Use the Admin Console to create Actions for file operations, use the webapp to create knowledge bases from S3 content.
- 
                    **Microsoft SharePoint**- Document management actions, content indexing.
- 
                    **OneDrive**- File operations, document search capabilities.
- 
                    **Confluence**- Content creation actions, knowledge base integration.

### Action-only connectors

Specialized for action execution without knowledge base capabilities:

- 
                    **Salesforce**- Enterprise CRM integration supporting account and contact operations, custom object CRUD operations, Sales process automation.
- 
                    **JIRA**- Issue tracking and project management.
- 
                    **Microsoft Outlook**- Send emails, manage calendar events, access contacts.
- 
                    **Slack**- Communication and notification workflows.
- 
                    **ServiceNow**- IT service management operations.
- 
                    **Zendesk**- Create tickets, update cases, search knowledge base.
- 
                    **PagerDuty**- Create incidents, manage escalations, update on-call schedules.
- 
                    **Asana**- Create actions, update projects, manage team workflows.
- 
                    **BambooHR**- Access employee data, manage time-off requests.
- 
                    **Smartsheet**- Update sheets, manage project data.
- 
                    **FactSet**- Access financial data, generate reports.
- 
                    **SAP**- Access SAP systems, execute business functions, and manage enterprise data.

### Knowledge base-only connectors

Focused on knowledge base integration without action capabilities:

- 
                    **Google Drive**- Document indexing and search.
- 
                    **Web Crawler**- Content discovery and indexing.

## API lifecycle management

         
            ### Credential management

- 
                    Automatic refresh token handling for OAuth action connectors. 
- 
                    Secure storage of authentication credentials using AWS KMS. 
- 
                    Support for credential rotation and updates. 
- 
                    Cross-account access for Amazon S3 connectors. 

### Connection updates

Use the `UpdateActionConnector` API to:

- 
                    Modify authentication credentials. 
- 
                    Update service configuration parameters. 
- 
                    Change action connector metadata. 

### Monitoring and troubleshooting

- 
                    Track API usage through CloudWatch metrics. 
- 
                    Monitor connection health and authentication status. 
- 
                    Implement error handling for common failure scenarios. 
- 
                    Use validation APIs to diagnose configuration issues. 

## Rate limiting and quotas

        Action connector APIs implement standard AWS API rate limiting:

- 
                Standard AWS API throttling applies to all operations. 
- 
                Connection validation may have additional limits. 
- 
                Action execution rates depend on target service capabilities. 
- 
                Implement exponential backoff for retry logic. 

## Cross-account support

        For Amazon S3 connectors, the APIs support cross-account access:

- 
                Specify different AWS account IDs during connector creation. 
- 
                Configure appropriate IAM permissions for cross-account access. 
- 
                Use AWS KMS for secure credential management across accounts. 
- 
                Validate permissions before enabling cross-account connections. 

## Error handling and troubleshooting

        Action connector APIs return standard AWS error responses:

### Common error types

- 
                    `AccessDeniedException`- Insufficient permissions for the operation.
- 
                    `InvalidParameterValueException`- One or more parameter values are invalid for the operation.
- 
                    Invalid configuration parameters - Service-specific configuration values are incorrect or missing. 
- 
                    `ResourceNotFoundException`- Connector or resource not found.
- 
                    `ThrottlingException`- Rate limit exceeded.
- 
                    `ConflictException`- Resource conflict or duplicate names.
- 
                    `InternalFailureException`- Internal service error occurred during request processing.
- 
                    `ResourceExistsException`- Attempt to create a resource that already exists.
- 
                    `InvalidNextTokenException`- The pagination token provided is invalid or expired.
- 
                    `AccessTokenNotFoundException`- User needs to authorize the connection (that is, sign-button). This exception is used by UX to ask users for authorization.
- 
                    `TokenResponseException`- Action setup is not valid.

Implement proper error handling in your applications to manage these scenarios gracefully and provide meaningful feedback to users.

## Using Action Connector APIs with AWS CLI

        You can use the AWS CLI to manage action connectors programmatically. The following examples demonstrate common operations using generic placeholder values.

### Creating an action connector

Use the `create-action-connector` command to create a new action connector for integrating with external services.

```
aws quicksight create-action-connector \
  --aws-account-id "123456789012" \
  --name "MyS3Connector" \
  --action-connector-id "my-s3-connector-id" \
  --type "AMAZON_S3" \
  --authentication-config '{
    "AuthenticationType": "IAM",
    "AuthenticationMetadata": {
      "IamConnectionMetadata": {
        "RoleArn": "arn:aws:iam::123456789012:role/MyConnectorRole"
      }
    }
  }' \
  --enabled-actions "CreateBucket" "ListBuckets" \
  --description "S3 connector for automation workflows" \
  --region "us-east-1"
            
```
### Listing action connectors

Use the `list-action-connectors` command to retrieve all action connectors in your account.

```
aws quicksight list-action-connectors \
  --aws-account-id "123456789012" \
  --max-results 10 \
  --region "us-east-1"
            
```
### Describing an action connector

Use the `describe-action-connector` command to get detailed information about a specific action connector.

```
aws quicksight describe-action-connector \
  --aws-account-id "123456789012" \
  --action-connector-id "my-s3-connector-id" \
  --region "us-east-1"
            
```
### Updating an action connector

Use the `update-action-connector` command to modify an existing action connector's configuration.

```
aws quicksight update-action-connector \
  --aws-account-id "123456789012" \
  --action-connector-id "my-s3-connector-id" \
  --name "UpdatedS3Connector" \
  --authentication-config '{
    "AuthenticationType": "IAM",
    "AuthenticationMetadata": {
      "IamConnectionMetadata": {
        "RoleArn": "arn:aws:iam::123456789012:role/UpdatedConnectorRole"
      }
    }
  }' \
  --enabled-actions "CreateBucket" "ListBuckets" "DeleteBucket" \
  --region "us-east-1"
            
```
### Searching action connectors

Use the `search-action-connectors` command to find action connectors based on specific criteria.

```
aws quicksight search-action-connectors \
  --aws-account-id "123456789012" \
  --max-results 5 \
  --filters '[{
    "Name": "ACTION_CONNECTOR_NAME",
    "Operator": "StringLike",
    "Value": "S3"
  }]' \
  --region "us-east-1"
            
```
### Managing action connector permissions

Use the `update-action-connector-permissions` command to grant or revoke permissions for an action connector.

```
aws quicksight update-action-connector-permissions \
  --aws-account-id "123456789012" \
  --action-connector-id "my-s3-connector-id" \
  --grant-permissions '[{
    "Actions": [
      "quicksight:DescribeActionConnector",
      "quicksight:UpdateActionConnector",
      "quicksight:DeleteActionConnector"
    ],
    "Principal": "arn:aws:quicksight:us-east-1:123456789012:user/default/myuser"
  }]' \
  --region "us-east-1"
            
```
### Viewing action connector permissions

Use the `describe-action-connector-permissions` command to view current permissions for an action connector.

```
aws quicksight describe-action-connector-permissions \
  --aws-account-id "123456789012" \
  --action-connector-id "my-s3-connector-id" \
  --region "us-east-1"
            
```
### Deleting an action connector

Use the `delete-action-connector` command to remove an action connector from your account.

```
aws quicksight delete-action-connector \
  --aws-account-id "123456789012" \
  --action-connector-id "my-s3-connector-id" \
  --region "us-east-1"
            
```
## Next steps

        After understanding action connector APIs, you can:

- 
                Review the complete API reference documentation for detailed parameter specifications. 
- 
                Explore specific connector setup guides for your target services. 
- 
                Implement authentication flows appropriate for your use case. 
- 
                Set up monitoring and error handling for production deployments. 
- 
                Configure permissions and access controls for your organization.