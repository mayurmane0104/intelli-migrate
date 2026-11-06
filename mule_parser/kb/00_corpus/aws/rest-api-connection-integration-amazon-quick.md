# REST API Connection integration - Amazon Quick

**Source:** [https://docs.aws.amazon.com/quick/latest/userguide/rest-api-integration.html](https://docs.aws.amazon.com/quick/latest/userguide/rest-api-integration.html)

---

With REST API Connection integration in Amazon Quick, you can perform actions with custom REST APIs and web services. This integration supports action execution only.

## What you can do

        
        With REST API Connection integration, you can perform actions with custom REST APIs and web services through the action connector.

- **Action connector**
- 
                    Perform HTTP requests, retrieve data, and interact with APIs using flexible authentication options. 

###### Note

REST API Connection integration doesn't support data access or knowledge base creation. It's designed specifically for task execution and API interactions with custom web services.

## Before you begin

        
        Before you set up REST API integration, make sure you have the following:

- 
                REST API endpoint with appropriate access permissions. 
- 
                API authentication credentials (OAuth, API key, or other). 
- 
                API documentation for the target web service. 

## Prepare API endpoint and authentication

        
        Before configuring the integration in Amazon Quick, prepare your REST API endpoint and authentication credentials. REST API Connection integration supports multiple authentication methods. Choose the method that matches your API requirements:

- **User authentication (OAuth)**
- 
                    Gather the following information from your API provider: - **Base URL**- REST API base URL.
- **Client ID**- OAuth application client ID.
- **Client Secret**- OAuth application client secret.
- **Token URL**- OAuth token endpoint.
- **Auth URL**- OAuth authorization endpoint.
- **Redirect URL**- OAuth redirect URI.
 
- **Service authentication (Service-to-service OAuth)**
- 
                    Gather the following information from your API provider: - **Authentication type**- OAuth 2.0 client credentials grant flow for service-to-service authentication.
- **Base URL**- REST API base URL.
- **Client ID**- OAuth application client identifier for service authentication.
- **Client secret**- OAuth application client secret for service authentication.
- **Token URL**- OAuth token endpoint for obtaining access tokens.
 

### Custom headers and parameters

You can use custom headers and parameters for flexible authentication and API interaction:

- Custom authentication headers. 
- API version headers. 
- Content-Type specifications. 
- Custom query parameters. 

## Set up REST API integration

        
        After you have prepared your API endpoint and authentication credentials, follow these steps to create your REST API integration:

- 
                In the Amazon Quick console, choose **Connectors**.
- 
                Choose the **Create for your team**tab.
- 
                Find and choose **REST API Connection**.
- 
                Fill in the integration details: - 
                        **Name**- Descriptive name for your REST API integration.
- 
                        **Description**(Optional) - Purpose of the integration.
 
- 
                        
- 
                Choose your connection type: - 
                        **User authentication**- OAuth-based authentication for individual user access.
- 
                        **Service authentication**- API key-based authentication for service access.
 
- 
                        
- 
                Fill in the connection settings based on your selected authentication method (either user or service). 
- 
                Select **Next**.
- 
                Review the actions that are available. 
- 
                Select **Create and continue**.

## Available task actions

        
        After you create your REST API integration, you can review the available actions for interacting with the REST API. Common REST API actions include:

- HTTP GET requests for data retrieval. 
- HTTP POST requests for data creation. 
- HTTP PUT/PATCH requests for data updates. 
- HTTP DELETE requests for data removal. 
- Custom endpoint interactions. 
- JSON and XML data processing. 
- Query parameter and header management. 

###### Note

The specific actions available depend on the REST API endpoints and the authentication permissions configured for your integration.

## API configuration options

        
        You can configure various aspects of your REST API integration to match your specific requirements.

### Endpoint configuration

Configure these endpoint settings:

- Base URL and endpoint paths. 
- HTTP method specifications. 
- Request and response format handling. 
- Error handling and retry logic. 

### Data handling

Configure how your integration processes different data formats:

- JSON request and response processing. 
- XML data transformation. 
- Form data and multipart uploads. 
- Binary data handling. 

## Manage REST API integrations

        
        After you create your REST API integration, you can manage it using these options:

- 
                **Edit integration**- Update authentication settings, base URL, or API configuration.
- 
                **Share integration**- Make the integration available to other users in your organization.
- 
                **Monitor usage**- View integration activity and API call metrics.
- 
                **Review actions**- See the complete list of available REST API actions.
- 
                **Test endpoints**- Validate API connectivity and authentication.
- 
                **Delete integration**- Remove the integration and revoke associated authentication.

###### Important

REST API integrations depend on the availability and configuration of the target web service. Changes to the API or authentication requirements may affect integration functionality.