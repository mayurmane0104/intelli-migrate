# OpenAPI Specification integration - Amazon Quick

**Source:** [https://docs.aws.amazon.com/quick/latest/userguide/openapi-integration.html](https://docs.aws.amazon.com/quick/latest/userguide/openapi-integration.html)

---

With OpenAPI Specification integration, you can create custom integrations based on OpenAPI schemas. This allows you to connect to any API that provides an OpenAPI specification. For Amazon Quick subscription requirements, see [Set up integrations in the console](./integration-console-setup-process.html).

## What you can do

        
        OpenAPI Specification integration provides schema-based connectivity to help you work with custom APIs.

- **Action connector**
- 
                    Perform actions based on OpenAPI specifications. Execute API calls, manage resources, and interact with custom services through dynamically generated actions based on the provided schema. 
- **Schema-based configuration**
- 
                    Import OpenAPI specifications to automatically generate available actions and actions. Support for JSON schema validation and parameter mapping. 

## Before you begin

        
        Before you set up OpenAPI Specification integration, make sure you have the following:

- 
                OpenAPI specification (version 3.0.0 or higher) for your target API. 
- 
                API authentication credentials (API key, OAuth, or other). 
- 
                Amazon Quick Author or higher. 
- 
                API documentation and endpoint access. 

## Prepare OpenAPI specification and authentication

        
        Before setting up the integration in Amazon Quick, prepare your OpenAPI specification and authentication credentials. Your OpenAPI specification must meet specific requirements for successful integration.

### Basic requirements

Your OpenAPI specification must meet these basic requirements.

- 
                    **OpenAPI version**- Version 3.0.0 or higher is required.
- 
                    **File format**- JSON format only (application/json).
- 
                    **File size limit**- Maximum 1MB for the entire OpenAPI specification.
- 
                    **Operation limit**- Minimum 1 and maximum 100 API operations per connector.

### Required schema fields

Your OpenAPI specification must include these required sections.

- **openapi**
- 
                        The OpenAPI version being used (must be "3.0.0" or higher). 
- **info**
- 
                        Service information including title, description, and version. 
- **servers**
- 
                        Base URL and server information for API connectivity. 
- **paths**
- 
                        API endpoint definitions with HTTP methods and operations. 

### Supported authentication schemes

Prepare authentication credentials based on the supported authentication methods in OpenAPI specifications.

- **OAuth 2.0**
- 
                        Supports both Authorization Code Grant and Client Credentials Grant flows. Requires authorizationUrl, tokenUrl, and scopes definitions in the security scheme. 
- **API Key**
- 
                        API key authentication passed in query parameters or headers. 
- **No authentication**
- 
                        Default option when no security schemes are defined in the specification. 

###### Note

Unsupported authentication schemes in the OpenAPI specification will be ignored, and the connector will default to no authentication.

## Set up OpenAPI Specification integration

        
        After preparing your OpenAPI specification and authentication credentials, follow these steps to create your OpenAPI Specification integration.

- 
                In the Amazon Quick console, choose **Connectors**.
- 
                Choose the **Create for your team**tab.
- 
                Find and choose **OpenAPI Specification**.
- 
                On the Add Schema page, select **Import Schema**and choose a schema to import.
- 
                Select **Next**.
- 
                Fill in the integration details including name and description. 
- 
                Review the available actions generated from your OpenAPI specification. 
- 
                Select **Create and continue**.
- 
                Choose users to share the integration with. 
- 
                Click **Next**.

### Expected results

After successful setup, your OpenAPI Specification integration appears in the integrations list with dynamically generated actions based on your schema. The integration is available for use in Amazon Quick workflows, automations, and AI agents, with tasks corresponding to the endpoints defined in your OpenAPI specification.

## Format and pattern requirements

            
            Your OpenAPI specification must follow these format requirements.

- 
                    **Path patterns**- Must follow the pattern:`^/[^/]*(/[^/]*)*$`and begin with a forward slash (/).
- 
                    **Operation IDs**- Must follow the pattern:`^[a-zA-Z0-9_ ]{1,256}$`.
- 
                    **Descriptions**- Required for all operations and parameters, maximum 5000 characters.
- 
                    **Content type**- Only application/json is supported for request and response bodies.

## Unsupported features

            
            The following OpenAPI features are not supported and will cause validation errors.

- 
                    **Array types**- Schemas with array types (for example,`{"type": "array", "items": {"string"}}`) are not supported.
- 
                    **Composition keywords**- allOf, oneOf, anyOf, and not keywords are not supported.
- 
                    **Circular references**- Circular or cyclic references ($ref inside of $ref) are not supported.
- 
                    **Complex nested structures**- Avoid deeply nested object structures when possible.

## Schema best practices

        
        Follow these best practices when creating your OpenAPI specification.

### Write effective descriptions

Use these guidelines to write clear and helpful descriptions.

- 
                    **Operation descriptions**- Describe what the operation does, when to use it, and how it behaves.
- 
                    **Parameter descriptions**- Concisely explain the parameter's purpose and impact on operation behavior.
- 
                    **Self-contained content**- Ensure descriptions provide sufficient guidance without external references.
- 
                    **Dependency clarity**- Make dependencies between operations explicit in descriptions.
- 
                    **Operation references**- Use operationId when referring to other operations, not API paths.

### Parameter structure recommendations

Structure your parameters for optimal usability.

- 
                    **Flatten complex objects**- Instead of nested objects, use separate parameters (for example, start_date, start_time, end_date, end_time).
- 
                    **Use standard formats**- Use standard format values like "date-time" or "date" for ISO-8601 dates and times.
- 
                    **Clear parameter names**- Use descriptive parameter names that clearly indicate their purpose.
- 
                    **Required field marking**- Properly mark parameters as required or optional based on API behavior.

## Supported extensions

        
        We support custom OpenAPI extensions to enhance the user experience.

- **x-amzn-form-display-name**
- 
                    Use at the parameter level to override the default field name displayed in confirmation forms. Currently supported for request body parameters only. `"x-amzn-form-display-name": "User Name"`
- **x-amzn-operation-type**
- 
                    Define whether an operation should be treated as "read" or "write". By default, GET methods are "read" operations and all other HTTP methods are "write" operations. `"x-amzn-operation-type": "read"`

## Schema validation and error handling

        
        When you upload an OpenAPI specification, we perform comprehensive validation.

- 
                **File size validation**- Ensures the specification doesn't exceed 1MB.
- 
                **Operation count validation**- Verifies between 1-100 operations are defined.
- 
                **Schema structure validation**- Checks for required fields and proper formatting.
- 
                **Security scheme validation**- Validates supported authentication methods.
- 
                **Content type validation**- Ensures only application/json is used.

Validation errors appear below the schema editor and must be resolved before the integration can be created. Common validation issues include:

- 
                Missing required fields (openapi, info, servers, paths). 
- 
                Invalid path patterns or operation IDs. 
- 
                Unsupported schema features (arrays, composition keywords). 
- 
                Missing or overly long descriptions. 
- 
                Circular references in schema definitions. 

## Manage OpenAPI Specification integration

        
        After you create your OpenAPI Specification integration, you can manage it through several options.

### Share integration

You can share OpenAPI Specification action connectors with other users in your organization.

- 
                    From the OpenAPI integration details page, choose **Share**.
- 
                    Configure sharing options: - 
                            **Share with specific users**- Enter user names or email addresses.
- 
                            **Share with organization**- Make available to all users in your organization.
 
- 
                            
- 
                    Set permission levels for shared access. 
- 
                    Choose **Share integration**to apply the sharing settings.

### Delete integration

Follow these steps to permanently remove your OpenAPI integration.

- 
                    From the OpenAPI integration details page, choose **Delete**.
- 
                    Review the deletion impact, including any workflows or automations using this integration. 
- 
                    Type the integration name to confirm deletion. 
- 
                    Choose **Delete integration**to permanently remove it.

## Troubleshoot OpenAPI Specification integration

        
        Use these troubleshooting tips to resolve common OpenAPI Specification integration issues.

- Schema validation errors
- 
                    Ensure your OpenAPI specification follows the correct format and includes all required fields. Use an OpenAPI validator to check your schema before importing. 
- No tasks generated
- 
                    Verify that your OpenAPI specification includes path definitions with HTTP methods and operation IDs. Actions are generated based on the operations defined in your schema. 
- Authentication failures
- 
                    Check that the authentication scheme defined in your OpenAPI specification matches the actual API requirements and that credentials are properly configured. 
- Action execution failures
- 
                    Review the action parameters and ensure they match the parameter definitions in your OpenAPI specification, including required fields and data types.