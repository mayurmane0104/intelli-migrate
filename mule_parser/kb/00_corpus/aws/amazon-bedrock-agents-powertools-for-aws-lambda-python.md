# Amazon Bedrock Agents - Powertools for AWS Lambda (Python)

**Source:** [https://docs.aws.amazon.com/powertools/python/latest/core/event_handler/bedrock_agents](https://docs.aws.amazon.com/powertools/python/latest/core/event_handler/bedrock_agents)

---

# Amazon Bedrock Agents

Create [Amazon Bedrock Agents](https://docs.aws.amazon.com/bedrock/latest/userguide/agents.html#agents-how) using event handlers with two different action groups approaches:

- OpenAPI schema
- Function details

## Key features[¶](https://docs.aws.amazon.com/powertools/python/latest/core/event_handler/bedrock_agents/#key-features)

- Minimal boilerplate to build Amazon Bedrock Agents
- Support for both OpenAPI-based and Function-based actions
- Automatic generation of [OpenAPI schemas](https://www.openapis.org/)from your business logic code
- Built-in data validation for requests and responses
- Similar experience to authoring [REST and HTTP APIs](https://docs.aws.amazon.com/powertools/python/latest/core/event_handler/api_gateway/)

## Terminology[¶](https://docs.aws.amazon.com/powertools/python/latest/core/event_handler/bedrock_agents/#terminology)

**Data validation** automatically validates the user input and the response of your AWS Lambda function against a set of constraints defined by you.

**Event handler** is a Powertools for AWS feature that processes an event, runs data parsing and validation, routes the request to a specific function, and returns a response to the caller in the proper format.

** OpenAPI schema** is an industry standard JSON-serialized string that represents the structure and parameters of your API.

**Function details** consist of a list of parameters, defined by their name, [data type](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_agent_ParameterDetail.html), and whether they are required. The agent uses these configurations to determine what information it needs to elicit from the user.

**Action group** is a collection of two resources where you define the actions that the agent should carry out when invoking your Lambda function.

**Large Language Models (LLM)** are very large deep learning models that are pre-trained on vast amounts of data, capable of extracting meanings from a sequence of text and understanding the relationship between words and phrases on it.

**Amazon Bedrock Agent** is an Amazon Bedrock feature to build and deploy conversational agents that can interact with your customers using Large Language Models (LLM) and AWS Lambda functions.

All examples shared in this documentation are available within the [project repository](https://github.com/aws-powertools/powertools-lambda-python/tree/develop/examples)

## Choose your Action Group[¶](https://docs.aws.amazon.com/powertools/python/latest/core/event_handler/bedrock_agents/#choose-your-action-group)

An action group defines actions that the agent can help the user perform. You can define action groups as OpenAPI-based or Function-based.

| Aspect | OpenAPI-based Actions | Function-based Actions | 
|---|---|---|
| Definition Style | `@app.get("/path", description="")``@app.post("/path", description="")` | `@app.tool(name="")` | 
| Parameter Handling | Path, query, and body parameters | Function parameters | 
| Use Case | REST-like APIs, complex request/response structures | Direct function calls, simpler input | 
| Response object | Via `BedrockResponse` | Via `BedrockFunctionResponse` | 
| Best For | - Complex APIs with multiple endpoints - When OpenAPI spec is required - Integration with existing REST APIs | - Simple function-based actions - Direct LLM-to-function mapping | 

## Getting started[¶](https://docs.aws.amazon.com/powertools/python/latest/core/event_handler/bedrock_agents/#getting-started)

### Install[¶](https://docs.aws.amazon.com/powertools/python/latest/core/event_handler/bedrock_agents/#install)

This is unnecessary if you're installing Powertools for AWS Lambda (Python) via [Lambda Layer/SAR](https://docs.aws.amazon.com/powertools/python/latest/#lambda-layer).

If you define the action group setting up an **OpenAPI schema**, you need to add `pydantic` as a dependency in your preferred tool *e.g., requirements.txt, pyproject.toml*. At this time, we only support Pydantic V2.

### Your first Agent[¶](https://docs.aws.amazon.com/powertools/python/latest/core/event_handler/bedrock_agents/#your-first-agent)

To create an agent, use the `BedrockAgentResolver` or the `BedrockAgentFunctionResolver` to annotate your actions.
This is similar to the way [all the other Event Handler](https://docs.aws.amazon.com/powertools/python/latest/core/event_handler/api_gateway/) resolvers work.

The resolvers used by Amazon Bedrock Agents are compatible with all Powertools for AWS Lambda [features](https://docs.aws.amazon.com/powertools/python/latest/#features).
For reference, we use [Logger](https://docs.aws.amazon.com/powertools/python/latest/core/logger/) and [Tracer](https://docs.aws.amazon.com/powertools/python/latest/core/tracer/) in this example.

**OpenAPI-based actions**

| 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 | 
 | 

Powertools for AWS Lambda [generates this automatically](https://docs.aws.amazon.com/powertools/python/latest/core/event_handler/bedrock_agents/#generating-openapi-schemas) from the Lambda handler.

| 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 50 51 52 53 54 55 56 57 58 59 60 61 62 63 64 65 66 67 68 69 70 71 72 73 74 75 76 77 78 79 80 81 82 83 84 85 86 87 88 89 90 91 92 93 94 | 
 | 

| 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 | 
 | 

| 1 2 3 4 5 6 7 8 9 10 11 12 13 14 | 
 | 

**Function-based actions**

| 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 | 
 | 

| 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 | 
 | 

| 1 2 3 4 5 6 7 8 9 10 11 12 13 14 | 
 | 

### Accessing custom request fields[¶](https://docs.aws.amazon.com/powertools/python/latest/core/event_handler/bedrock_agents/#accessing-custom-request-fields)

The event sent by Amazon Bedrock Agents into your Lambda function contains a [number of extra event fields](https://docs.aws.amazon.com/powertools/python/latest/core/event_handler/bedrock_agents/#request_fields_table), exposed in the `app.current_event` field.

## Why is this useful?

You can for instance identify new conversations (`session_id`) or store and analyze entire conversations (`input_text`).

In this example, we [append correlation data](https://docs.aws.amazon.com/powertools/python/latest/core/logger/#appending-additional-keys) to all generated logs.
This can be used to aggregate logs by `session_id` and observe the entire conversation between a user and the Agent.

| 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 | 
 | 

The input event fields available depend on your Agent's configuration (OpenAPI-based or Function-based):

| Name | Type | Description | OpenAPI | Function | 
|---|---|---|---|---|
| message_version | str | The version of the message format. Amazon Bedrock only supports version 1.0. | ✅ | ✅ | 
| agent | BedrockAgentInfo | Contains information about the name, ID, alias, and version of the agent. | ✅ | ✅ | 
| input_text | str | The user input for the conversation turn. | ✅ | ✅ | 
| session_id | str | The unique identifier of the agent session. | ✅ | ✅ | 
| action_group | str | The name of the action group. | ✅ | ✅ | 
| api_path | str | The path to the API operation, as defined in the OpenAPI schema. | ✅ | ❌ | 
| http_method | str | The method of the API operation, as defined in the OpenAPI schema. | ✅ | ❌ | 
| function | str | The name of the function being called. | ❌ | ✅ | 
| parameters | List[Parameter] | Contains parameters with name, type, and value properties. | ✅ | ✅ | 
| request_body | BedrockAgentRequestBody | Contains the request body and its properties. | ✅ | ❌ | 
| session_attributes | Dict[str, str] | Contains session attributes and their values. | ✅ | ✅ | 
| prompt_session_attributes | Dict[str, str] | Contains prompt attributes and their values. | ✅ | ✅ | 

## OpenAPI-based actions[¶](https://docs.aws.amazon.com/powertools/python/latest/core/event_handler/bedrock_agents/#openapi-based-actions)

### Generating OpenAPI schemas[¶](https://docs.aws.amazon.com/powertools/python/latest/core/event_handler/bedrock_agents/#generating-openapi-schemas)

Use the `get_openapi_json_schema` function provided by the resolver to produce a JSON-serialized string that represents your OpenAPI schema.
You can print this string or save it to a file. You'll use the file later when creating the Agent.

You'll need to regenerate the OpenAPI schema and update your Agent everytime your API changes.

| 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 | 
 | 

| 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 50 51 52 53 54 55 56 57 58 59 60 61 62 63 64 65 66 67 68 69 70 71 72 73 74 75 76 77 78 79 80 81 82 83 84 85 86 87 88 89 90 91 92 93 94 | 
 | 

To get the OpenAPI schema, run the Python script from your terminal. The script will generate the schema directly to standard output, which you can redirect to a file.

| `1` | 
 | 

### Crafting effective OpenAPI schemas[¶](https://docs.aws.amazon.com/powertools/python/latest/core/event_handler/bedrock_agents/#crafting-effective-openapi-schemas)

Working with Amazon Bedrock Agents will introduce [non-deterministic behaviour to your system](https://docs.aws.amazon.com/bedrock/latest/userguide/agents-how.html#agents-rt).

## Why is that?

Amazon Bedrock uses LLMs to understand and respond to user input. These models are trained on vast amounts of data and are capable of extracting meanings from a sequence of text and understanding the relationship between words and phrases on it. However, this means that the same input can result in different outputs, depending on the characteristics of the LLM being used.

The OpenAPI schema provides context and semantics to the Agent that will support the decision process for invoking our Lambda function. Sparse or ambiguous schemas can result in unexpected outcomes.

We recommend enriching your OpenAPI schema with as many details as possible to help the Agent understand your functions, and make correct invocations. To achieve that, keep the following suggestions in mind:

- Always describe your function behaviour using the `description`field in your annotations
- When refactoring, update your description field to match the function outcomes
- Use distinct `description`for each function to have clear separation of semantics

### Validating input and output[¶](https://docs.aws.amazon.com/powertools/python/latest/core/event_handler/bedrock_agents/#validating-input-and-output)

You can define the expected format for incoming data and responses by using type annotations.
Define constraints using standard Python types, [dataclasses](https://docs.python.org/3/library/dataclasses.html) or [Pydantic models](https://docs.pydantic.dev/latest/concepts/models/).
Pydantic is a popular library for data validation using Python type annotations.

The examples below uses [Pydantic's EmailStr](https://docs.pydantic.dev/2.0/usage/types/string_types/#emailstr) to validate the email address passed to the `schedule_meeting` function.
The function then returns a boolean indicating if the meeting was successfully scheduled.

| 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 | 
 | 

| 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 50 51 52 53 54 55 56 57 58 59 60 61 62 63 64 65 66 67 68 69 70 71 72 73 74 75 76 77 78 79 80 81 82 83 84 85 86 87 88 89 90 91 92 93 94 95 96 97 98 99 100 101 102 103 104 105 106 107 108 109 | 
 | 

| 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 | 
 | 

| 1 2 3 4 5 6 7 8 9 10 11 12 13 14 | 
 | 

#### When validation fails[¶](https://docs.aws.amazon.com/powertools/python/latest/core/event_handler/bedrock_agents/#when-validation-fails)

If the request validation fails, your event handler will not be called, and an error message is returned to Bedrock. Similarly, if the response fails validation, your handler will abort the response.

## What does this mean for my Agent?

The event handler will always return a response according to the schema (OpenAPI) or type hints (Function-based).
A validation failure in OpenAPI-based actions results in a [422 response](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/422).
For both approaches, how Amazon Bedrock interprets that failure is non-deterministic, since it depends on the characteristics of the LLM being used.

| 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 | 
 | 

| 1 2 3 4 5 6 7 8 9 10 11 12 13 14 | 
 | 

### Video walkthrough[¶](https://docs.aws.amazon.com/powertools/python/latest/core/event_handler/bedrock_agents/#video-walkthrough)

To create an Agent for Amazon Bedrock, refer to the [official documentation](https://docs.aws.amazon.com/bedrock/latest/userguide/agents-create.html) provided by AWS.

The following video demonstrates the end-to-end process:

During the creation process, you should use the schema [previously generated](https://docs.aws.amazon.com/powertools/python/latest/core/event_handler/bedrock_agents/#generating-openapi-schemas) when prompted for an OpenAPI specification.

### Advanced[¶](https://docs.aws.amazon.com/powertools/python/latest/core/event_handler/bedrock_agents/#advanced)

#### Additional metadata[¶](https://docs.aws.amazon.com/powertools/python/latest/core/event_handler/bedrock_agents/#additional-metadata)

To enrich the view that Amazon Bedrock Agents has of your Lambda functions,
use a combination of [Pydantic Models](https://docs.pydantic.dev/latest/concepts/models/) and [OpenAPI](https://www.openapis.org/) type annotations to add constraints to your APIs parameters.

## When is this useful?

Adding constraints to your function parameters can help you to enforce data validation and improve the understanding of your APIs by Amazon Bedrock.

#### Customizing OpenAPI parameters[¶](https://docs.aws.amazon.com/powertools/python/latest/core/event_handler/bedrock_agents/#customizing-openapi-parameters)

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

To implement these customizations, include extra constraints when defining your parameters:

| Customizing API parameters | |
|---|---|
| 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 | 
 | 

#### Customizing API operations[¶](https://docs.aws.amazon.com/powertools/python/latest/core/event_handler/bedrock_agents/#customizing-api-operations)

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

| Customzing API operations | |
|---|---|
| 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 | 
 | 

#### Enabling user confirmation[¶](https://docs.aws.amazon.com/powertools/python/latest/core/event_handler/bedrock_agents/#enabling-user-confirmation)

You can enable user confirmation with Bedrock Agents to have your application ask for explicit user approval before invoking an action.

| Enabling user confirmation | |
|---|---|
| 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 | 
 | 

#### OpenAPI-based Responses[¶](https://docs.aws.amazon.com/powertools/python/latest/core/event_handler/bedrock_agents/#openapi-based-responses)

## Note

The default response only includes the essential fields to keep the payload size minimal, as AWS Lambda has a maximum response size of 25 KB.

You can use `BedrockResponse` class to add additional fields as needed, such as [session attributes, prompt session attributes, and knowledge base configurations](https://docs.aws.amazon.com/bedrock/latest/userguide/agents-lambda.html#agents-lambda-response).

## Content Type Behavior

Amazon Bedrock Agents only support TEXT content type in the responseBody. All response bodies are automatically serialized as JSON strings regardless of the `content_type` parameter you provide. The `content_type` parameter exists for API consistency but does not affect the actual format sent to Bedrock Agents.
Learn more: [AWS Bedrock Lambda Integration](https://docs.aws.amazon.com/bedrock/latest/userguide/agents-lambda.html)

| Customzing your Bedrock Response | |
|---|---|
| 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 | 
 | 

#### Bedrock requests under the hood[¶](https://docs.aws.amazon.com/powertools/python/latest/core/event_handler/bedrock_agents/#bedrock-requests-under-the-hood)

Powertools handle the request from the Agent, parse, validate, and route it to the correct method in your code. The response is then validated and formatted back to the Agent.

### Testing your code[¶](https://docs.aws.amazon.com/powertools/python/latest/core/event_handler/bedrock_agents/#testing-your-code)

Test your routes by passing an [Agent for Amazon Bedrock proxy event](https://docs.aws.amazon.com/bedrock/latest/userguide/agents-lambda.html#agents-lambda-input) request:

| 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 | 
 | 

| 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 | 
 | 

## Function-based Actions[¶](https://docs.aws.amazon.com/powertools/python/latest/core/event_handler/bedrock_agents/#function-based-actions)

The `BedrockAgentFunctionResolver` streamlines agent function development through three core capabilities:

- **Register Functions**: Use the- `@app.tool()`decorator to expose your functions to Bedrock Agents

| Field | Required | Description | 
|---|---|---|
| name | No | Custom name for your function. Uses the actual function name if omitted. | 
| description | No | Explain what your function does to guide the agent's usage. | 

- **Process Parameters**: Automatically maps input parameters from the agent to your function arguments
- **Format Responses**: Transforms your function outputs into properly structured Bedrock Agent responses

### Function-based Responses[¶](https://docs.aws.amazon.com/powertools/python/latest/core/event_handler/bedrock_agents/#function-based-responses)

## Note

The default response only includes the essential fields to keep the payload size minimal, as AWS Lambda has a maximum response size of 25 KB.

You can use `BedrockFunctionResponse` class to customize your response [with additional fields](https://docs.aws.amazon.com/bedrock/latest/userguide/agents-lambda.html#agents-lambda-response). This class allows you to:

- Return a response body
- Set session and prompt session attributes
- Set knowledge bases configurations
- Control the response state ("FAILURE" or "REPROMPT")

| Customzing your Bedrock Function Response | |
|---|---|
| 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 | 
 |