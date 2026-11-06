# REST Connect Connector Generator | MuleSoft Documentation

**Source:** [https://docs.mulesoft.com/exchange/to-deploy-using-rest-connect](https://docs.mulesoft.com/exchange/to-deploy-using-rest-connect)

---

`#%RAML 1.0 title: Dropbox API version: 1 baseUri: https://api.dropbox.com/{version} securitySchemes: basic: description: | This API supports Basic Authentication. type: Basic Authentication`text

# REST Connect Connector Generator

The Exchange backend uses REST Connect to transparently convert a REST API specification to a Mule 4 connector. You can use this connector as you would any other in Anypoint Studio.

## Access Generated Connectors

In Exchange, download the generated connector from the **Download** menu.

| After deploying a REST asset to Exchange, refresh your screen to ensure that all download options are available. | 

Mule 4 connectors download as JAR files.

## API Specification Format Support

REST Connect supports these API specification formats:

- 
OAS 3 - JSON 
- 
OAS 3 - YAML 
- 
OAS 2 - JSON 
- 
OAS 2 - YAML 
- 
RAML 1.0 

## Security Scheme Support

REST Connect supports these security schemes:

- 
Basic Authentication 
- 
OAuth 2.0 Client Credentials 
- 
OAuth 2.0 Authorization Code 
- 
Pass Through 
- 
Digest Authentication 

If you publish an API specification with an unsupported authentication type, you receive an alert email. If this happens, update your API specification to use one of the supported security schemes.

If the operations defined in your API specification support multiple security schemes, the one that comes first in the list of supported schemes is used.

### Basic Authentication

RAML Example:

OAS Example:

`openapi: 3.0.3 info: title: Dropbox API version: "1" servers: - url: https://api.dropbox.com/{version} variables: version: default: "1" components: securitySchemes: basic: type: http scheme: basic description: This API supports Basic Authentication. security: - basic: []`text

### OAuth 2.0 Client Credentials

RAML Example:

`#%RAML 1.0 version: v1 title: Deadlines API baseUri: http://localhost/deadlines securitySchemes: oauth_2_0: description: Deadlines API supports OAuth 2.0 for authenticating all API requests. type: OAuth 2.0 describedBy: headers: Authorization: description: Sends a valid OAuth 2 access token. type: string responses: 401: description: Bad or expired token. 403: description: Bad OAuth request. settings: accessTokenUri: https://api.example.com/1/oauth2/token authorizationGrants: [ client_credentials ] /deadlines: get: securedBy: [oauth_2_0] displayName: Get deadlines. description: Get a list of all registered deadlines. responses: 200: body: application/json: example: '[ { "rest-connect": "2017-03-13" } ]'`text

OAS Example:

`openapi: 3.0.3 info: title: Deadlines API version: v1 servers: - url: http://localhost/deadlines paths: /deadlines: get: summary: Get deadlines. description: Get a list of all registered deadlines. security: - oauth_2_0: [] responses: "200": description: Successful response content: application/json: example: - rest-connect: "2017-03-13" components: securitySchemes: oauth_2_0: type: oauth2 description: Deadlines API supports OAuth 2.0 for authenticating all API requests. flows: clientCredentials: tokenUrl: https://api.example.com/1/oauth2/token`text

### OAuth 2.0 Authorization Code

RAML Example:

`#%RAML 1.0 version: v1 title: Github API baseUri: https://api.github.com securitySchemes: oauth_2_0: description: | OAuth2 is a protocol that lets external apps request authorization to private details in a user's GitHub account without getting their password. This is preferred over Basic Authentication because tokens can be limited to specific types of data, and can be revoked by users at any time. type: OAuth 2.0 describedBy: headers: Authorization: description: | Used to send a valid OAuth 2 access token. responses: 404: description: Unauthorized settings: authorizationUri: https://github.com/login/oauth/authorize accessTokenUri: https://github.com/login/oauth/access_token authorizationGrants: [ authorization_code ] scopes: - "user" - "user:email" - "user:follow" - "public_repo" - "repo" - "repo_deployment" - "repo:status" - "delete_repo" - "notifications" - "gist" - "read:repo_hook" - "write:repo_hook" - "admin:repo_hook" - "admin:org_hook" - "read:org" - "write:org" - "admin:org" - "read:public_key" - "write:public_key" - "admin:public_key"`text

OAS Example:

`openapi: 3.0.3 info: title: Github API version: v1 servers: - url: https://api.github.com components: securitySchemes: oauth_2_0: type: oauth2 description: | OAuth2 is a protocol that lets external apps request authorization to private details in a user's GitHub account without getting their password. This is preferred over Basic Authentication because tokens can be limited to specific types of data, and can be revoked by users at any time. flows: authorizationCode: authorizationUrl: https://github.com/login/oauth/authorize tokenUrl: https://github.com/login/oauth/access_token scopes: user: "" user:email: "" user:follow: "" public_repo: "" repo: "" repo_deployment: "" repo:status: "" delete_repo: "" notifications: "" gist: "" read:repo_hook: "" write:repo_hook: "" admin:repo_hook: "" admin:org_hook: "" read:org: "" write:org: "" admin:org: "" read:public_key: "" write:public_key: "" admin:public_key: ""`text

### Pass-through

RAML Example:

`#%RAML 1.0 title: Customer API version: 1 baseUri: https://api.customer.com/v2 securitySchemes: passthrough: description: | This API supports Pass Through Authentication. type: Pass Through describedBy: headers: api_key: type: string`text

OAS Example:

`openapi: 3.0.3 info: title: Customer API version: "1" servers: - url: https://api.customer.com/v2 components: securitySchemes: passthrough: type: apiKey in: header name: api_key description: | This API supports Pass Through Authentication.`text

## Change an Auto-Generated Connector’s Name

REST Connect generates the names of operations based on the `operationName`, `displayName`, and `endpoint` attributes, in that order.

To modify a generated connector name using RAML, change the text in `displayName`, for example:

`#%RAML 1.0 title: Sample API baseUri: https://jsonplaceholder.typicode.com version: 0.1 mediaType: application/json ... /{postId}: uriParameters: postId: integer get: displayName: Get a post by ID. responses: 200: body: type: Post`text

To modify a generated connector name using OAS, change the text in `summary`, for example:

`openapi: 3.0.3 info: title: Sample API version: "0.1" servers: - url: https://jsonplaceholder.typicode.com paths: /{postId}: parameters: - name: postId in: path required: true schema: type: integer get: summary: Get a post by ID. responses: "200": description: Successful response content: application/json: schema: $ref: "#/components/schemas/Post" components: schemas: Post: {}`text

You can also modify a generated connector name by pointing to the REST Connect library and using the `operationName` annotation (RAML) or `x-rest-connect-operationName` extension (OAS) from a method such as GET, POST, and DELETE.

RAML Example using `operationName`:

`#%RAML 1.0 title: Sample API baseUri: https://jsonplaceholder.typicode.com version: 0.1 mediaType: application/json uses: rest-connect: exchange_modules/org.mule.connectivity/rest-connect-library/1.0.0/rest-connect-library.raml ... /{postId}: uriParameters: postId: integer get: (rest-connect.operationName): Retrieve a post by id displayName: Get a post by ID. responses: 200: body: type: Post`text

OAS Example using `x-rest-connect-operationName`:

`openapi: 3.0.3 info: title: Sample API version: "0.1" servers: - url: https://jsonplaceholder.typicode.com paths: /{postId}: parameters: - name: postId in: path required: true schema: type: integer get: summary: Get a post by ID. x-rest-connect-operationName: Retrieve a post by id responses: '200': description: Successful response content: application/json: schema: $ref: '#/components/schemas/Post' components: schemas: Post: type: object additionalProperties: true`text

## Metadata Limitations

REST Connect generates metadata for each operation based on your schema definition in the request and response for each method in your API specification. REST Connect cannot generate metadata based on examples in the specification.

REST Connect supports only one input/output type and uses the first one declared in the API specification. You can change this behavior by using the default property from the REST Connect library.

The following examples uses the REST Connect library:

RAML Example:

`#%RAML 1.0 title: Sample API baseUri: https://jsonplaceholder.typicode.com version: 0.1 mediaType: application/json uses: rest-connect: exchange_modules/org.mule.connectivity/rest-connect-library/1.0.0/rest-connect-library.raml ... /{postId}: uriParameters: postId: integer get: displayName: Get a post by ID. responses: 200: body: application/json: type: string application/xml: (rest-connect.default): //this sets application/xml response by default type: string`text

OAS Example:

`openapi: 3.0.3 info: title: Sample API version: "0.1" servers: - url: https://jsonplaceholder.typicode.com paths: /{postId}: parameters: - name: postId in: path required: true schema: type: integer get: summary: Get a post by ID. responses: '200': description: Successful response content: application/json: schema: type: string application/xml: x-rest-connect-default: true # indicates XML is the default schema: type: string`text

## Reserved Keywords

Valid identifiers for REST Connect must not use any reserved Java or Mule keywords.

The following list shows the reserved Java keywords to avoid when naming valid identifiers for REST Connect:

- 
`abstract`
- 
`assert`
- 
`boolean`
- 
`break`
- 
`byte`
- 
`case`
- 
`catch`
- 
`char`
- 
`class`
- 
`const`
- 
`continue`
- 
`default`
- 
`do`
- 
`double`
- 
`else`
- 
`extends`
- 
`false`
- 
`final`
- 
`finally`
- 
`float`
- 
`for`
- 
`goto`
- 
`if`
- 
`implements`
- 
`import`
- 
`instanceof`
- 
`int`
- 
`interface`
- 
`long`
- 
`native`
- 
`new`
- 
`null`
- 
`package`
- 
`private`
- 
`protected`
- 
`public`
- 
`return`
- 
`short`
- 
`static`
- 
`strictfp`
- 
`super`
- 
`switch`
- 
`synchronized`
- 
`this`
- 
`throw`
- 
`throws`
- 
`transient`
- 
`true`
- 
`try`
- 
`void`
- 
`volatile`
- 
`while`

The following list shows the reserved Mule keywords to avoid when naming valid identifiers for REST Connect:

- 
`friendlyName`
- 
`name`
- 
`operationName`
- 
`target`
- 
`targetValue`

## Generating Connectors With TLS Support

Mule 4 (SmartConnector) connectors support Transport Layer Security (TLS).

When you enable TLS support and generate a connector:

- 
The connector is upgraded to run on Mule runtime 4.6. 
- 
TLS is enabled, so that Anypoint Studio displays a form for collecting the connector’s required TLS connection configuration information. To see the connection configuration properties, select **Edit inline**or**Global reference**from the**Tls context**field.![The form for TLS connection configuration information](_images/rest-connect-tls-configuration.png)  

To enable TLS, add a `properties.json` file to the root directory of the Design Center API project for your app:

- 
In Design Center, Select **Files +**>**New file**.
- 
In the **Add new file**window, select**API format > other**, name the file`properties.json`, and then click**Create**.
- 
In the new file, add `"tlsEnabled": true`.Add the `properties.json`file only if you want to enable TLS support or explicitly opt out of it. If you don’t add a`properties.json`file to your API project, the REST Connect Service generates the standard connector artifacts without TLS support.

After you add the `properties.json` file and enable TLS, Anypoint Studio displays the TLS configuration form for the connector.

When you add a `properties.json` file to your project, ensure that the `tlsEnabled` property is set correctly with a valid boolean value of either `true` to enable TLS or `false` to explicitly disable TLS. If the `properties.json` file is invalid or the property is incorrectly set, the connector generation is aborted.

## View Mule Runtime Version and Compatible Java Version

To view the minimum Mule runtime version or the compatible Java versions for the patch versions of a connector:

- 
From Exchange, select a connector. 
- 
In the asset details page, click **View versions**.![The asset version showing the minimum runtime version and compatible Java versions](_images/ex-connector-java-compatibility.png)  

## Upgrading a REST Connect Generated Connector

To update your REST-Connect-generated connector to use the latest version of Mule runtime and to be compatible with Java 17:

- 
In Design Center, open your API project. 
- 
Click **Publish**.The connector is regenerated. 

If you want to add [TLS support](#tls-support) to your application, add it before re-generating the connector so that you only have to test your app once.

## Known Limitations

- 
Anypoint Platform, including REST Connect, does not support API fragments for OAS. 
- 
Chinese characters are not supported in API specs or their dependencies. Japanese characters are supported in the `description`and`example`tags.