# Designing API Specs and Fragments | MuleSoft Documentation

**Source:** [https://docs.mulesoft.com/anypoint-code-builder/des-designing-api-specs](https://docs.mulesoft.com/anypoint-code-builder/des-designing-api-specs)

---

See the RAML 1.0 specification for descriptions of these types:

- 
Trait 
- 
Resource 
- 
Library 
- 
Data Type 
- 
User Documentation 
- 
Example 

Use Anypoint Code Builder to create, design, test, and publish new API specifications to Exchange.

The process for designing API specifications is:

For source management options, see [SCM for API Design Projects](start-scm#anypoint-scm).

Supported OAS and RAML versions are:

OAS 2.0 (JSON)

OAS 2.0 (YAML)

OAS 3.0 (JSON)

OAS 3.0 (YAML)

RAML 1.0

RAML 0.8

Supported AsyncAPI versions are:

AsyncAPI 2.6 (JSON)

AsyncAPI 2.6 (YAML)

For gRPC API specifications, Anypoint Code Builder supports Protocol Buffers (Protobuf 3). See [Designing a gRPC API Specification with Anypoint Code Builder](des-design-grpc-api-spec).

Create, include, or reference API fragments within your API specification.

Supported API specification languages and syntaxes for API fragments are:

OAS 3.0

YAML

JSON

RAML 1.0

See the RAML 1.0 specification for descriptions of these types:

Trait

Resource

Library

Data Type

User Documentation

Example

JSON Schema

Avro 1.9.0 schema

gRPC fragments (Protobuf 3)

Reusable Protobuf definitions (for example, `message` or `enum` types) published as API fragment assets. See [Publish a gRPC Fragment to Exchange](des-design-grpc-api-spec#publish-a-grpc-fragment-to-exchange).

When parsing an API specification, the desktop IDE depends on your computer’s resources. To avoid issues, ensure that your computer has the following minimum resources available:

8 GB RAM

Ryzen series 5 / Intel i5 CPU or higher

To achieve optimal parser performance, keep the total project size for all files in your design project below 500 KB.

A project size that exceeds 1.5 MB severely affects validation time.

To avoid common issues, follow these guidelines:

Divide your fragments into short, reusable dependencies when possible.

Keep only one version of the same dependency.

Keep only one browser tab open at a time.

This best practice applies to the cloud IDE only.

Before designing an OAS or RAML API specification, review [OAS Specification Best Practices](#apid-best-practices-oas) or [RAML Specification Best Practices](#apid-best-practices-raml)

Use the `$ref` property to define reusable components. To improve parsing efficiency, reference each component from the API specification instead of duplicating component definitions, for example:

```
components:
  schemas:
    User:
      type: object
      properties:
        id:
          type: integer
paths:
  /users:
    get:
      responses:
        '200':
          description: Successful response
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/User'
```
Use simpler types to represent your data if possible. Avoid unnecessary nesting and complicated types, for example:

```
properties:
  age:
    type: integer  # Prefer simple types over complex types like objects
```
Use the `enum` property for fields with a fixed set of values to improve parsing efficiency:

```
properties:
  status:
    type: string
    enum: [active, inactive]
```
Use simple nesting for objects to simplify the structure and improve readability and parsing efficiency:

```
# Good
properties:
  name:
    type: string
  address:
    type: string
# Avoid
properties:
  user:
    type: object
    properties:
      profile:
        type: object
        properties:
          name:
            type: string
```
Use `response` headers instead of the response body to provide additional information, for example:

```
responses:
  '200':
    description: Successful response
    headers:
      X-Rate-Limit-Limit:
        description: The number of requests allowed in the current period
        schema:
          type: integer
```
Provide concise and short examples:

Book: type: string example: "Explain the string with as few words as possible."

When using union-type properties, use `oneOf` to represent union-type object fields, `allOf` to represent an intersection type and composite objects and fields, and `anyOf` when defining a property with multiple possible data structures.

When extracting RAML fragments, import each fragment as a local declaration first:

Create a fragment file, and before publishing the fragment to Anypoint Exchange, import the local fragment file to validate that the fragment works as expected. If the fragment works, publish the fragment to Exchange so you can reuse the fragment in your API specifications instead of duplicating it.

Reuse data types as declarations.

Use inheritance only when needed:

```
Car:
  description: This is a car
  properties:
    brand: string
    model: string
  example:
    brand: Toyota
    model: Corolla
Person:
  properties:
    owns: Car
```
Use short unions:

Person: type: Employee | Customer

Use simple traits, and avoid combining traits with resource type properties:

```
/basic:
  type: {resourceTypes.fhirResourceType: {
      postExample : !include /examples/requests/post_resource.json,
      getExample  : !include /examples/responses/get_resource.json,
      bundleName : basic.BasicBundle
    }
  }
  /_search:
    get:
      is: [ searchParams ]
    post:
      is: [ POSTSearchParams ]
```
Use source control management (SCM) to store and share your design, integration, and implementation projects. Source control options for API design projects depend on how and when you created the project:

As of the February 2024 release, design projects that you create from scratch in Anypoint Code Builder with **Design an API** (see [Create a New API Specification Project](des-create-api-specs#design-new-api-spec)) or with the command `MuleSoft: Design an API` no longer use MuleSoft VCS to store and sync changes.

API design projects [imported to Anypoint Code Builder from Design Center](des-create-api-specs#import-spec) or created in Anypoint Code Builder before the February 2024 release automatically connect to MuleSoft VCS, which enables you to sync with a corresponding design project.

If you prefer to use your own remote repository, GitHub is one option. To store your API project in a repository on GitHub, without synchronizing with the project in MuleSoft VCS, see [publish your project files to another repository](start-scm#add-extra-repo).

For source control options, see [Controlling Source Files](start-scm).