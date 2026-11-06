# OpenAPI - Powertools for AWS Lambda (Python)

**Source:** [https://docs.aws.amazon.com/powertools/python/latest/core/event_handler/openapi](https://docs.aws.amazon.com/powertools/python/latest/core/event_handler/openapi)

---

# OpenAPI

Powertools for AWS Lambda supports automatic OpenAPI schema generation from your route definitions and type annotations. This includes Swagger UI integration, schema customization, and OpenAPI Merge for micro-functions architectures.

## Key features[¶](https://docs.aws.amazon.com/powertools/python/latest/core/event_handler/openapi/#key-features)

- **Automatic schema generation**from Pydantic models and type annotations
- **Swagger UI**for interactive API documentation
- **OpenAPI Merge**for generating unified schemas from multiple Lambda handlers
- **Security schemes**support (OAuth2, API Key, HTTP auth, etc.)
- **Customizable**metadata, operations, and parameters

## Swagger UI[¶](https://docs.aws.amazon.com/powertools/python/latest/core/event_handler/openapi/#swagger-ui)

Behind the scenes, the [data validation](https://docs.aws.amazon.com/powertools/python/latest/core/event_handler/api_gateway/#data-validation) feature auto-generates an OpenAPI specification from your routes and type annotations. You can use [Swagger UI](https://swagger.io/tools/swagger-ui/) to visualize and interact with your API.

This feature requires [data validation](https://docs.aws.amazon.com/powertools/python/latest/core/event_handler/api_gateway/#data-validation) to be enabled.

## Important caveats

| Caveat | Description | 
|---|---|
| Swagger UI is publicly accessible by default | Implement a [custom middleware](https://docs.aws.amazon.com/powertools/python/latest/core/event_handler/openapi/#customizing-swagger-ui)for authorization | 
| You need to expose a new route | Expose `/swagger`path to Lambda | 
| JS and CSS files are embedded within Swagger HTML | Consider enabling `compress`option for better performance | 
| Authorization data is loston browser close/refresh | Use `enable_swagger(persist_authorization=True)`to persist | 

| 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 | 
 | 

Here's an example of what it looks like by default:

![Swagger UI picture](https://docs.aws.amazon.com/powertools/python/latest/media/swagger.png)


### Customizing Swagger UI[¶](https://docs.aws.amazon.com/powertools/python/latest/core/event_handler/openapi/#customizing-swagger-ui)

The Swagger UI appears by default at the `/swagger` path, but you can customize this to serve the documentation from another path and specify the source for Swagger UI assets.

| 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 | 
 | 

Use middleware for security headers, authentication, or other request processing.

| 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 | 
 | 

## Customization[¶](https://docs.aws.amazon.com/powertools/python/latest/core/event_handler/openapi/#customization)

### Customizing parameters[¶](https://docs.aws.amazon.com/powertools/python/latest/core/event_handler/openapi/#customizing-parameters)

Whenever you use OpenAPI parameters to validate [query strings](https://docs.aws.amazon.com/powertools/python/latest/core/event_handler/api_gateway/#validating-query-strings) or [path parameters](https://docs.aws.amazon.com/powertools/python/latest/core/event_handler/api_gateway/#validating-path-parameters), you can enhance validation and OpenAPI documentation by using any of these parameters:

| Field name | Type | Description | 
|---|---|---|
| `alias` | `str` | Alternative name for a field, used when serializing and deserializing data | 
| `validation_alias` | `str` | Alternative name for a field during validation (but not serialization) | 
| `serialization_alias` | `str` | Alternative name for a field during serialization (but not during validation) | 
| `description` | `str` | Human-readable description | 
| `gt` | `float` | Greater than. If set, value must be greater than this. Only applicable to numbers | 
| `ge` | `float` | Greater than or equal. If set, value must be greater than or equal to this. Only applicable to numbers | 
| `lt` | `float` | Less than. If set, value must be less than this. Only applicable to numbers | 
| `le` | `float` | Less than or equal. If set, value must be less than or equal to this. Only applicable to numbers | 
| `min_length` | `int` | Minimum length for strings | 
| `max_length` | `int` | Maximum length for strings | 
| `pattern` | `string` | A regular expression that the string must match. | 
| `strict` | `bool` | If `True`, strict validation is applied to the field. See[Strict Mode](https://docs.pydantic.dev/latest/concepts/strict_mode/)for details | 
| `multiple_of` | `float` | Value must be a multiple of this. Only applicable to numbers | 
| `allow_inf_nan` | `bool` | Allow `inf`,`-inf`,`nan`. Only applicable to numbers | 
| `max_digits` | `int` | Maximum number of allow digits for strings | 
| `decimal_places` | `int` | Maximum number of decimal places allowed for numbers | 
| `openapi_examples` | `dict[str, Example]` | A list of examples to be displayed in the SwaggerUI interface. Avoid using the `examples`field for this purpose. | 
| `deprecated` | `bool` | Marks the field as deprecated | 
| `include_in_schema` | `bool` | If `False`the field will not be part of the exported OpenAPI schema | 
| `json_schema_extra` | `JsonDict` | Any additional JSON schema data for the schema property | 

### Customizing operations[¶](https://docs.aws.amazon.com/powertools/python/latest/core/event_handler/openapi/#customizing-operations)

Customize your API endpoints by adding metadata to endpoint definitions.

Here's a breakdown of various customizable fields:

| Field Name | Type | Description | 
|---|---|---|
| `summary` | `str` | A concise overview of the main functionality of the endpoint. This brief introduction is usually displayed in autogenerated API documentation and helps consumers quickly understand what the endpoint does. | 
| `description` | `str` | A more detailed explanation of the endpoint, which can include information about the operation's behavior, including side effects, error states, and other operational guidelines. | 
| `responses` | `Dict[int, Dict[str, OpenAPIResponse]]` | A dictionary that maps each HTTP status code to a Response Object as defined by the [OpenAPI Specification](https://swagger.io/specification/#response-object). This allows you to describe expected responses, including default or error messages, and their corresponding schemas or models for different status codes. | 
| `response_description` | `str` | Provides the default textual description of the response sent by the endpoint when the operation is successful. It is intended to give a human-readable understanding of the result. | 
| `tags` | `List[str]` | Tags are a way to categorize and group endpoints within the API documentation. They can help organize the operations by resources or other heuristic. | 
| `operation_id` | `str` | A unique identifier for the operation, which can be used for referencing this operation in documentation or code. This ID must be unique across all operations described in the API. | 
| `include_in_schema` | `bool` | A boolean value that determines whether or not this operation should be included in the OpenAPI schema. Setting it to `False`can hide the endpoint from generated documentation and schema exports, which might be useful for private or experimental endpoints. | 
| `deprecated` | `bool` | A boolean value that determines whether or not this operation should be marked as deprecated in the OpenAPI schema. | 
| `status_code` | `int` | The default HTTP status code for successful responses. Defaults to `200`. This value is used both in the OpenAPI schema and as the actual response status code when the handler returns a dictionary or plain value (not a`Response`object or tuple). | 

To implement these customizations, include extra parameters when defining your routes:

| 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 | 
 | 

### Customizing metadata[¶](https://docs.aws.amazon.com/powertools/python/latest/core/event_handler/openapi/#customizing-metadata)

Defining and customizing OpenAPI metadata gives detailed, top-level information about your API. Use the method `app.configure_openapi` to set and tailor this metadata:

| Field Name | Type | Description | 
|---|---|---|
| `title` | `str` | The title for your API. It should be a concise, specific name that can be used to identify the API in documentation or listings. | 
| `version` | `str` | The version of the API you are documenting. This could reflect the release iteration of the API and helps clients understand the evolution of the API. | 
| `openapi_version` | `str` | Specifies the version of the OpenAPI Specification on which your API is based. When using Pydantic v1 it defaults to 3.0.3, and when using Pydantic v2, it defaults to 3.1.0. | 
| `summary` | `str` | A short and informative summary that can provide an overview of what the API does. This can be the same as or different from the title but should add context or information. | 
| `description` | `str` | A verbose description that can include Markdown formatting, providing a full explanation of the API's purpose, functionalities, and general usage instructions. | 
| `tags` | `List[str]` | A collection of tags that categorize endpoints for better organization and navigation within the documentation. This can group endpoints by their functionality or other criteria. | 
| `servers` | `List[Server]` | An array of Server objects, which specify the URL to the server and a description for its environment (production, staging, development, etc.), providing connectivity information. | 
| `terms_of_service` | `str` | A URL that points to the terms of service for your API. This could provide legal information and user responsibilities related to the usage of the API. | 
| `contact` | `Contact` | A Contact object containing contact details of the organization or individuals maintaining the API. This may include fields such as name, URL, and email. | 
| `license_info` | `License` | A License object providing the license details for the API, typically including the name of the license and the URL to the full license text. | 

Include extra parameters when exporting your OpenAPI specification:

| 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 | 
 | 

### Security schemes[¶](https://docs.aws.amazon.com/powertools/python/latest/core/event_handler/openapi/#security-schemes)

## Does Powertools implement any of the security schemes?

No. Powertools adds support for generating OpenAPI documentation with [security schemes](https://swagger.io/docs/specification/authentication/), but you must implement the security mechanisms separately.

Security schemes are declared at the top-level first, then referenced globally or per operation.

| 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 | 
 | 

| 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 | 
 | 

- Using the oauth security scheme scoped to the "admin" role.

| 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 | 
 | 

- An empty security requirement ({}) makes security optional for this route.

OpenAPI 3 supports these security schemes:

| Security Scheme | Type | Description | 
|---|---|---|
| [HTTP auth](https://www.iana.org/assignments/http-authschemes/http-authschemes.xhtml) | `HTTPBase` | HTTP authentication (Basic, Bearer) | 
| [API keys](https://swagger.io/docs/specification/authentication/api-keys/) | `APIKey` | API keys in headers, query strings or cookies | 
| [OAuth 2](https://swagger.io/docs/specification/authentication/oauth2/) | `OAuth2` | OAuth 2.0 authorization | 
| [OpenID Connect](https://swagger.io/docs/specification/authentication/openid-connect-discovery/) | `OpenIdConnect` | OpenID Connect Discovery | 
| [Mutual TLS](https://swagger.io/specification/#security-scheme-object) | `MutualTLS` | Client/server certificate authentication | 

## Using OAuth2 with Swagger UI?

Use `OAuth2Config` to configure a default OAuth2 app:

| 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 | 
 | 

### OpenAPI extensions[¶](https://docs.aws.amazon.com/powertools/python/latest/core/event_handler/openapi/#openapi-extensions)

Define extensions using `openapi_extensions` parameter at Root, Servers, Operation, and Security Schemes levels.

## Warning

We do not support `x-amazon-apigateway-any-method` and `x-amazon-apigateway-integrations` extensions.

| 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 | 
 | 

## OpenAPI Merge[¶](https://docs.aws.amazon.com/powertools/python/latest/core/event_handler/openapi/#openapi-merge)

OpenAPI Merge generates a unified OpenAPI schema from multiple Lambda handlers. This is designed for micro-functions architectures where each Lambda has its own resolver.

### Why OpenAPI Merge?[¶](https://docs.aws.amazon.com/powertools/python/latest/core/event_handler/openapi/#why-openapi-merge)

In a micro-functions architecture, each Lambda function handles a specific domain (users, orders, payments). Each has its own resolver with routes, but you need a single OpenAPI specification for documentation and API Gateway imports.

### How it works[¶](https://docs.aws.amazon.com/powertools/python/latest/core/event_handler/openapi/#how-it-works)

OpenAPI Merge uses AST (Abstract Syntax Tree) analysis to detect resolver instances in your handler files. **No code is executed during discovery** - it's pure static analysis. This means:

- No side effects from importing handler code
- No Lambda cold starts
- No security concerns from arbitrary code execution
- Fast discovery across many files

## Handler modules must be side-effect-free at import time

While discovery uses static analysis (AST), **schema generation requires importing your handler modules** to extract route definitions. If a handler module runs code at import time - such as validating environment variables, opening database connections, or calling external services — the import will fail silently and its routes will be missing from the final schema.

If your schema is unexpectedly empty, check whether your handler files have decorators or top-level code that depends on runtime state. Move these to the handler function body or guard them with `if __name__ == "__main__"`.

### Discovery parameters[¶](https://docs.aws.amazon.com/powertools/python/latest/core/event_handler/openapi/#discovery-parameters)

The `discover()` method accepts the following parameters:

| Parameter | Type | Default | Description | 
|---|---|---|---|
| `path` | `str`or`Path` | required | Root directory to search for handler files | 
| `pattern` | `str`or`list[str]` | `"handler.py"` | Glob pattern(s) to match handler files | 
| `exclude` | `list[str]` | `["**/tests/**", "**/__pycache__/**", "**/.venv/**"]` | Patterns to exclude from discovery | 
| `resolver_name` | `str` | `"app"` | Variable name of the resolver instance in handler files | 
| `recursive` | `bool` | `False` | Whether to search recursively in subdirectories | 
| `project_root` | `str`or`Path` | Same as `path` | Root directory for resolving Python imports | 

#### Pattern examples[¶](https://docs.aws.amazon.com/powertools/python/latest/core/event_handler/openapi/#pattern-examples)

Patterns use glob syntax:

| Pattern | Matches | 
|---|---|
| `handler.py` | Files named exactly `handler.py`in the root directory | 
| `*_handler.py` | Files ending with `_handler.py`(e.g.,`users_handler.py`) | 
| `**/*.py` | All Python files recursively (requires `recursive=True`) | 
| `["handler.py", "api.py"]` | Multiple patterns | 

#### Recursive search[¶](https://docs.aws.amazon.com/powertools/python/latest/core/event_handler/openapi/#recursive-search)

By default, `recursive=False` searches only in the specified `path` directory. Set `recursive=True` to search subdirectories:

| 1 2 3 4 5 6 7 8 | 
 | 

#### Project root for imports[¶](https://docs.aws.amazon.com/powertools/python/latest/core/event_handler/openapi/#project-root-for-imports)

When handler files use absolute imports (e.g., `from myapp.utils.resolver import app`), set `project_root` to the directory that serves as the Python package root:

| 1 2 3 4 5 | 
 | 

### Getting started example[¶](https://docs.aws.amazon.com/powertools/python/latest/core/event_handler/openapi/#getting-started-example)

Here's a typical micro-functions project structure and how to configure OpenAPI Merge:

| 1 2 3 4 5 6 7 8 9 10 11 12 13 | 
 | 

Each handler file defines its own resolver with domain-specific routes:

| 1 2 3 4 5 6 7 8 9 10 11 12 13 14 | 
 | 

| 1 2 3 4 5 6 7 8 9 10 11 12 13 14 | 
 | 

To generate a unified OpenAPI schema, you have two options:

Generate `openapi.json` at build time:

| 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 | 
 | 

Serve Swagger UI from a dedicated Lambda:

| 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 | 
 | 

### Standalone class[¶](https://docs.aws.amazon.com/powertools/python/latest/core/event_handler/openapi/#standalone-class)

Use `OpenAPIMerge` class to generate schemas. This is pure Python code where you control the paths and output.

| 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 | 
 | 

| 1 2 3 4 5 6 7 8 9 10 | 
 | 

| 1 2 3 4 5 6 7 8 9 | 
 | 

### Resolver integration[¶](https://docs.aws.amazon.com/powertools/python/latest/core/event_handler/openapi/#resolver-integration)

Use `configure_openapi_merge()` on any resolver to serve merged schemas via Swagger UI. This is useful when you want a dedicated Lambda to serve the unified documentation.

| 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 | 
 | 

## Routes from other Lambdas are documentation only

The merged schema includes routes from all discovered handlers for documentation purposes. However, only routes defined in the current Lambda are actually executable. Other routes exist only in the OpenAPI spec - unless you configure API Gateway to route them to their respective Lambdas.

### Shared resolver pattern[¶](https://docs.aws.amazon.com/powertools/python/latest/core/event_handler/openapi/#shared-resolver-pattern)

In some architectures, instead of each handler file defining its own resolver, you have a central resolver file that is imported by multiple route files. Each route file registers its routes on the shared resolver instance.

| 1 2 3 4 5 6 | 
 | 

OpenAPI Merge automatically detects this pattern. When you point `discover()` to the resolver file, it finds all files that import from it and loads them to ensure all routes are registered before extracting the schema.

| 1 2 3 4 | 
 | 

| 1 2 3 4 5 6 7 8 9 10 11 12 | 
 | 

| 1 2 3 4 5 6 7 | 
 | 

| 1 2 3 4 5 6 7 8 9 10 11 12 13 | 
 | 

### Conflict handling[¶](https://docs.aws.amazon.com/powertools/python/latest/core/event_handler/openapi/#conflict-handling)

When the same path+method is defined in multiple handlers, use `on_conflict` to control behavior:

| Strategy | Behavior | 
|---|---|
| `warn`(default) | Log warning, keep first definition | 
| `error` | Raise `OpenAPIMergeError` | 
| `first` | Silently keep first definition | 
| `last` | Use last definition (override) | 

| 1 2 3 4 5 6 7 8 9 | 
 | 

### Full configuration[¶](https://docs.aws.amazon.com/powertools/python/latest/core/event_handler/openapi/#full-configuration)

| 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 | 
 |