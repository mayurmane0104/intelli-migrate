# API Mocking Service Release Notes | MuleSoft Documentation

**Source:** [https://docs.mulesoft.com/release-notes/api-mocking-service/api-mocking-service-release-notes](https://docs.mulesoft.com/release-notes/api-mocking-service/api-mocking-service-release-notes)

---

Status Code: 404 Not Found

# API Mocking Service Release Notes

## 2.71.0

**September 28, 2024**

### Fixed Issues

| Issue Resolution | ID | 
|---|---|
| You now get the correct response when simulating a request on an endpoint. | W-15150842 | 

## 2.67.0

**June 24, 2024**

### Fixed Issues

| Issue Resolution | ID | 
|---|---|
| You can now use PKCE to test API specifications without defining the  | W-15759980 | 

## 2.65.0

**April 27, 2024**

### Fixed Issues

| Issue Resolution | ID | 
|---|---|
| You can now change the  | W-14845230 | 

## 2.62.0

**February 3, 2024**

### What’s New

- 
You can now change the server URL without the make public toggle automatically unchecking. 
- 
The `/link`endpoint was replaced by the new`/links`endpoint. For more information, refer to[Mocking Service 2 API Endpoints](https://anypoint.mulesoft.com/exchange/org.mule.examples/mocking-service-2-api/minor/1.3/?status=published).

## 2.60.0

**December 9, 2023**

### What’s New

- 
The mocking service is now permanently enabled and you no longer need to define a mocking service URI in your specifications. 
- 
You can now open your projects without getting a warning to update to remove the mocking service URI. 

## 2.59.0

**November 11, 2023**

### What’s New

- 
You can now successfully test dependencies using the Mocking Service. 

### Fixed Issues

| Issue Resolution | ID | 
|---|---|
| You can now use   | W-13896554 | 

## 2.58.0

**October 13, 2023**

### Fixed Issues

| Issue Resolution | ID | 
|---|---|
| You can now see the name of the field that contains multipart data in the error message. | W-13802993 | 
| You now see the correct status codes when using the API Console. | W-13590915 | 
| You can now use the  | W-13602285 | 

## 2.56.0

**August 19, 2023**

### What’s New

- 
You can now use the `cookie`query parameter when defining an`apiKey`security scheme.

### Fixed Issues

| Issue Resolution | ID | 
|---|---|
| Now, when defining a URL, the mocking service URL is successfully removed. | W-13498665 | 

## 2.54.0

**June 24, 2023**

### Fixed Issues

| Issue Resolution | ID | 
|---|---|
| You can now successfully use URLs as selected servers without getting an error message. | W-12613109 | 

## 2.53.0

**May 29, 2023**

### Fixed Issues

| Issue Resolution | ID | 
|---|---|
| The mocking service now displays a 400 bad request error message when you don’t include an authorization header when using the OAuth 2.0 security scheme type. | W-12740857 | 

## 2.52.0

**April 29, 2023**

### Fixed Issues

| Issue Resolution | ID | 
|---|---|
| Your session no longer expires with an error when you switch to branches with  | W-12708537 / W-12613956 / W-12986979 | 

## 2.50.0

**March 4, 2023**

### Fixed Issues

| Fixed resolution | ID | 
|---|---|
| You can now use the  | W-12219253 | 

## 2.47.0

**December 10, 2022**

### Fixed Issues

| Fixed resolution | ID | 
|---|---|
| You can now use the  | W-11491070 | 

## 2.46.0

**November 12, 2022**

### What’s New

- 
You now see the correct header values when sending a request. 

### Fixed Issues

| Fixed resolution | ID | 
|---|---|
| You can now successfully send a request with an array with a single string (for example:  | W-11790087 | 
| You now get a response when defining nullable properties in return types. | W-11789702 | 
| Mocking service now automatically generates examples when given a type that only contains optional fields and the MS2-Randomize behavior header is set as  | W-11569372 | 
| You can now successfully send HTTP headers. | W-11491118 | 

## 2.45.4

**October 29, 2022**

### New Features

- 
Added a security layer to the API console, so that only registered domains are reachable. 
 For more information, see the[Allowlisting Trusted Domains documentation.](../../access-management/allowlisting-trusted-domains)

## 2.44.0

**September 13, 2022**

### Fixed Issues

| Issue | ID | 
|---|---|
| You can now use  | W-11491130 | 

## 2.43.0

**August 20, 2022**

### Fixed Issues

| Issue | ID | 
|---|---|
| When simulating a Spec API using the Mocking service, you can now add XML tags in JSON string values without them being removed in the response body. | W-11394026 | 
| When clicking  | W-11329433 | 

## 2.42.0

**July 23, 2022**

### Fixed Issues

| Issue | ID | 
|---|---|
| When the  | W-11240933 | 

## 2.41.0

**June 25, 2022**

### Fixed Issues

| Issue | ID | 
|---|---|
| When using the  | W-11141216 | 
| Trying to retrieve a PDF file no longer returns the encoded content of the file. | W-10747573 | 

## 2.40.0

**May 28, 2022**

### Fixed Issues

| Issue | ID | 
|---|---|
| When you test an API that has main and nested fragments that are Exchange dependencies, the mocking service now returns valid responses for  | W-10673086 | 
| When you use  | W-10803321 | 

## 2.39.0

**April 30, 2022**

### Fixed Issues

| Issue | ID | 
|---|---|
| The mocking service now properly handles a zero value in  | W-10764024 | 

## 2.38.0

**April 2, 2022**

### Fixed Issues

| Issue | ID | 
|---|---|
| The mocking service now properly renders examples in OAS 3.0 that use the  | W-10647695 | 
| The web UI no longer collapses when the mocking service expiration date is deleted. | W-10819894 | 

## 2.37.0

**March 5, 2022**

### Fixed Issues

| Issue | ID | 
|---|---|
| Endpoints are now properly parsed for RAML specifications that were created from OAS specifications that have path parameters. | W-10647958 | 
| RAML maximum value validation for  | W-10647957 | 

## 2.36.0

**February 5, 2022**

### Fixed Issues

| Issue | ID | 
|---|---|
| If a resource name contains an unsupported character such as  | SE-23187 | 
| When an OAS API specification is tested, the mocking service now handles the header correctly by accepting the value of the header name rather than the header name itself. | SE-23664 | 

## 2.35.0

**January 8, 2022**

### Fixed Issues

| Issue | ID | 
|---|---|
| Defining identical paths for the endpoint and  | SE-23447 | 
| The  | MSERV-1172 | 

## 2.32.0

**October 16, 2021**

### Fixed Issues

| Issue | ID | 
|---|---|
| Headers defined as  | SE-22132 | 

## 2.31.0

**September 18, 2021**

### Fixed Issues

| Issue | ID | 
|---|---|
| Publishing a RAML asset to Exchange and calling the asset’s endpoint via the mocking service no longer results in a  | SE-21215 | 
| RAML 0.8 API specifications containing URI parameters no longer result in the following parsing error: 
 | MSERV-1271 | 

## 2.30.0

**August 21, 2021**

### Fixed Issues

| Issue | ID | 
|---|---|
| The mocking service now correctly renders examples when the OAS 3  | SE-21983 | 
| In API Console, a toggle now enables you to select between query parameters that use the  | SE-21709 | 
| The mocking service no longer incorrectly returns  | SE-20620 | 

## 2.29.0

**July 24, 2021**

### Fixed Issues

- 
Request URLs that included RAML `baseUriParameters`with a value of`/v1`resulted in the following error:

## 2.28.0

**June 26, 2021**

### Fixed Issues

- 
When using the mocking function for an OAS 3 API array object, the response contained extra brackets in the array object. The response now returns array objects with the correct number of brackets. 

- 
The mocking service responded with an empty payload when a union type was defined as the response in an endpoint condition. The response now contains the correct payload. For example, the following RAML snippet would return an empty payload: `responses: 200: body: application/json: type: test1Response | test2Response`Now, the payload is not empty and contains the union of the two responses. 

## 2.26.0

**May 1, 2021**

### New Feature

- 
The mocking service now supports template URIs. A *template URI*is a URI parameter enclosed in curly brackets inside a relative URI of a resource.The following RAML snippet demonstrates using a reserved expansion template URI (callout 1). The addition operator ( `+`) allows for expanded values that include reserved URI characters.`#%RAML 1.0 title: reserved expansion mediaType: application/json /reserved/{+hello}:`**(1)**get: responses: 200: body: application/json: type: object properties: type: string example: type: helloSimilarly, the following RAML snippet demonstrates using a fragment expansion template URI (callout 2). The crosshatch ( `#`) operator allows for expanded values that include fragment identifiers.`#%RAML 1.0 title: fragment expansion mediaType: application/json /fragment/{#hello}:`**(2)**get: responses: 200: body: application/json: type: object properties: type: string example: type: helloFor additional information on using reserved expansion and fragment expansion to resolve URI templates, refer to RFC 6570. 

### Fixed Issues

- 
The mocking service returned `HTTP 400 - INVALID_PARAMETER`in scenarios such as the following.An `example_code`parameter was defined with the`^\d{2}$`pattern:`uriParameters: example_code: type: string pattern: ^\d{2}$`Specifying `12`as the value of`example_code`and sending a request to the mocking service resulted in:`{ "code": "INVALID_PARAMETER", "message": "Could not apply any validation" }`The mocking service now returns the correct `200 OK`status code.

## 2.25.0

**April 3, 2021**

### Fixed Issues

- 
Sending payloads with characters after the end tag of a JSON array resulted in no parsing errors. The mocking service now returns: HTTP 400 - Bad Request 

- 
The mocking service returned an empty response if the response content type was `application/vnd.api+json`.The response now includes the body payload as defined in the example node. 

- 
Requests with a required string type parameter could include a zero-length string for the parameter. These requests resulted in errors. The mocking service now displays the following warning when sending requests with empty strings: Value is required but currently empty Instead of sending an empty string, you can disable a parameter, which causes the mocking service to return an expected `400 - Bad Request`response. To enable or disable a parameter, toggle the button next to the parameter’s text field.

- 
The mocking service detected incorrect endpoints when the endpoints were defined with a trailing `/`, as demonstrated in the following example:`/messaging/v1/email/definitions/ /messaging/v1/email/definitions/{definitionKey}/`

## 2.24.0

**March 6, 2021**

### Fixed Issues

- 
Calling the mocking service with a value whose size was greater than 16 (the maximum) incorrectly resulted in a status code of `200 OK`.The following is now returned: `{"code": "REQUEST_VALIDATION_ERROR","message": "Invalid schema for content type application/json. Errors: /16digits 10000000000000000 is not less or equal to 1.0E16. "}`

## 2.23.0

**February 6, 2021**

### Fixed Issues

- 
Accessing endpoints with numerous nested resources resulted in the following `400 Bad Request`error:`{ "code": "INVALID_PARAMETER", "message": "Could not apply any validation" }`

- 
Under **Mocking Service Configuration**, toggling the**Make Public**button (creating or deleting a Public Mocking Service Link) was not output to the audit logs.

- 
Enabling the **Set expiration date for public link**checkbox option (under**Mocking Service Configuration**) caused the following error:Status Code: 404 Not Found 

- 
An API that redirected could have forwarded the request (including the authentication header) to a malicious server. To prevent attacks, the mocking service no longer redirects to the URL indicated in the `Location`header.The following `302 Found`message is now displayed:Details are not exposed due to browser security policies. 

## 2.20.0

**November 14, 2020**

### New Feature

- 
The mocking service now runs automatically and no longer needs to be enabled. When you open an existing API specification or fragment, API Designer safely removes the baseURI property from your specification since this property is no longer needed. API Designer now allows you to create a public link that you can share with users outside of Anypoint Platform. 

## 2.19.0

**October 29, 2020**

- 
Added support for the MS2-Example behavioral headers. MS2-Example allows you to choose a specific response example if your endpoint defines more than one example for the same status code. 

- 
Fixed an issue in the mocking service where URI parameters were not working correctly in RAML. 

## 2.18.0

**September 19, 2020**

This release includes one fix: the mocking service could parse query strings incorrectly.

## 2.17.0

**August 22, 2020**

This release includes this fix: the mocking service could, in some cases, treat optional headers as required parameters.

## 2.16.0

**July 25, 2020**

- 
If an API specification written in OAS 3.0 uses an OAuth 2.0 security scheme, the mocking service requires an authorization header in each request. If a request does not include an authorization header, the mocking service returns this error message: 

"code": "REQUEST_VALIDATION_ERROR", "message": "Error validating Oauth 2.0 Flows. Required header Authorization is missing."

- 
The MS2-Delay behavioral header now takes a maximum value of 10000 milliseconds (ms), and now follows this behavior: - 
If the value is set to fewer than 10000 ms, the mocking service adds a delay of ~5000 ms. 
- 
If the value is set to more than 10000 ms, the mocking service adds a delay of ~10000 ms. 
 Examples: - 
If the value is set to a range of 5000 - 9000 ms, the mocking service adds a delay of ~5000 - ~9000 ms. 
- 
If the value is set to a range of 9000 - 20000 ms, the mocking service adds a delay of ~9000 - ~10000 ms. 
- 
If the value is set to a range of 20000 - 30000 ms, the mocking service returns this error message: 
 
- 

```
{
  "code": "INVALID_HEADER_VALUE",
  "message": "Invalid value for header MS2-Delay. Requested range is higher than the max value allowed: 10000 ms"
}
```
## 2.15.0

**June 27, 2020**

This release includes minor bug fixes.

## 2.14.0

**May 30, 2020**

This release includes minor bug fixes.

## 2.13.0

**May 2, 2020**

- 
The mocking service returned an `Invalid schema for content type application/xml`error message for POST methods when these two conditions were met:- 
The value for a string in the request matched a regex pattern. 
- 
The media type for the specification was `application/xml`.
 For example, mocking a POST request for the following specification would cause the error: + `#%RAML 1.0 title: Regex-Test mediaType: application/xml types: xml: properties: zip: type: string pattern: (\d{5}) /test: post: body: application/xml: type: xml responses: 200:`
- 

- 
The mocking service would fail to start if a project contained any files with filenames that contained characters not allowed in URLs. 

- 
The mocking service was not validating file types when files in mock POST requests were uploaded. 

- 
The mocking service returned an `Invalid schema for content type application/xml`message when an enum was used in POST requests for which the response body was declared as`application/xml`.

- 
The mocking service returned an `Invalid schema for content type text/xml`message when the content type for an XSD file in the body of a POST request was declared as`text/xml`.

## 2.12.0

**April 4, 2020**

- 
The mocking service returned the wrong example in cases such as the following: in an API specification written in RAML, a type is defined with an example, but a response that uses the type overrides the example with an `!include`directive. Rather than use the included example in the response, the mocking service used the example from the type definition.For example, the following simple specification defines the type `ExampleRoot`. The definition includes the example`Internal Example`. For the endpoint`/tmp`, the specification defines a response that uses`ExampleRoot`, but provides a different example, which is referred to with an`!include`directive.`#%RAML 1.0 title: Example API with types and resources to showcase how examples look. mediaType: - application/json types: ExampleRoot: properties: string: type: string example: Internal Example /foo/example: get: responses: 200: body: type: ExampleRoot /tmp: get: responses: 200: body: type: ExampleRoot examples: !include external-example.raml`If a request was made on `/tmp`before the fix, the response that the mocking service sent incorrectly contained`Internal Example`as the example for`ExampleRoot`.
- 
The mocking service was not validating an example-array header that was of `type: string`and not an array. Now, you can use valid strings in these headers.

## 2.11.0

- 
March 7, 2020* 

This release of the mocking service fixes the following issues:

- 
The mocking service was not validating DataType fragments that were referenced by a Library fragment that was in trun referenced by the root file in an API-specification project. 
- 
The mocking service did not return an error message if a required query parameter was missing or the value was empty. 
- 
In a particular case, the mocking service was not returning an example in responses, even though the example was defined. 
- 
It was not possible to import an XSD schema into API Designer in Anypoint Design Center through the mocking service. The mocking service failed with the message `Invalid schema for content type application/xml. Errors: key not found:`[http://www.w3.org/2001/xml.xsd](http://www.w3.org/2001/xml.xsd).

## 2.9.0

**January 11, 2020**

This release of the mocking service fixes the following issues.

- 
If you set the authentication type to "Client Credentials" and then set a scope, the scope was not saved. 
- 
The mocking service returned empty responses instead of expected JSON responses in some cases, both in API Designer and in Exchange. 

- 
When the mocking service validated XML against an XSD schema that imported a namespace, it returned the following error message: `Invalid schema for content type application/xml. Errors: URI has an authority component.`.

- 
XML payloads in requests were not considered valid when a Union data type was used for XML schemas. 

- 
When the behavioral header MS2-Status-Code was used and set to `400`, the mocking service returned the example that was defined for status code 200.

- 
In API Console, the names of query parameters were being populated from parameter identifiers in parameter definitions, not from the parameter names. This problem occurred for API specifications written in OAS 2.0. 

### Deprecation of Version 1 of the Mocking Service

As of December 1, 2019, Version 1 of the mocking service is deprecated. MuleSoft recommends that you upgrade your API-specification projects in API Designer to use Version 2 of the mocking service.

You can continue to use Version 1 until February 1, 2020. By default, however, Version 1 now returns the following response to every request:

Status Code: 410 Gone Response headers: deprecation: date="Fri, 29 Nov 2019 23:59:59 GMT" link: https://docs.mulesoft.com/design-center/design-migrating-ms

For Version 1 to respond with a status code that is defined in an API specification, you must add the following header to requests:

name: x-deprecation-acknowledgement value: I understand that version 1 of the mocking service is deprecated and that I need to upgrade before February 1, 2020.

Here is an example of this header used in a specification that is written in RAML:

```
#%RAML 1.0
baseUri: https://mocksvc.devx.anypoint.mulesoft.com/mocks/d25ddb9c-ad20-4e80-af96-60217cc9f0b6/
version: v1
title: MS-TEST
/test:
  get:
    headers:
      x-deprecation-acknowledgement:
        type: string
        required: false
        example: I understand that version 1 of the mocking service is deprecated and that I need to upgrade before February 1, 2020.
      Cache-Control:
        type: string
        required: true
        example: no-cache
    responses:
      200:
        body:
          application/json:
            example:
              "OK"
```
## 2.6.0

**October 5, 2019**

DateTime elements appeared with null values in responses from the mocking service, even when API specifications provided example responses that contained values for these elements.

## 2.5.0

**September 7, 2019**

### Announcement

Version 2 of the mocking service is replacing Version 1. You must migrate any API-specification project that meets *both* of these conditions:

- 
The mocking service was switched on for the project before January 10, 2019. 
- 
The mocking service has been running continuously since it was switched on. 

#### Dates for the Deprecation and End of Life of Version 1

- 
**On November 29, 2019**, Version 1 of the mocking service will be deprecated. Starting on that date, third-party tools must include this header in requests that they send to the mocking service to test endpoints in API specifications being developed in API Designer:`x-deprecation-acknowledgement`The header must have this value: `I understand that version 1 of the mocking service is deprecated and that I need to upgrade before February 1, 2020.`
- 
**Starting February 1, 2020**, Version 1 of the mocking service will no longer send responses to requests. If you have not migrated your projects to use Version 2 of the mocking service by this date, the mocking service will return the HTTP status code 301 and provide a link to this document.

### New Feature

The new behavioral header `MS2-Status-Code-Selection` gives you two options for controlling how the mocking service selects a status code for responses to requests. See [Add Behavioral Headers to Simulated API Calls](../../design-center/apid-behavioral-headers) for details.

## 2.4.0

**August 10, 2019**

This release includes minor bug fixes.

## 2.3.0

**July 13, 2019**

### Fixed Issues

- 
Executing the Get command in RAML produces an empty response in the example data. 

- 
Request and response are not showing up in the mocking service. 

## 2.2.0

**June 15, 2019**

This release contains one new feature and two fixes.

### New Feature

- 
Use behavioral headers with the mocking service to modify in various ways how the mocking service behaves. See [Add Behavioral Headers to Simulated API Calls](../../design-center/apid-behavioral-headers).
- 
Now, the mocking service supports XML serialization facets, such as `wrapped`,`attribute`, and`name`, when generating an XML response that is based on a RAML example.

### Fixed Issues

- 
The mocking service included invalid tags in returned XML when the data type contained an array. 
- 
The mocking service converted null values to string "null" values. 

## 2.1.8

**May 18, 2019**

- 
The API Console and the mocking service were adding invalid tags to XML examples. 
- 
Though multiple examples were defined for an endpoint, the mocking service always used the same example, rather than randomly selecting one to use. 
- 
When an OAS API specification did not define any consuming media type for a specific endpoint, the mocking service failed. 

## 2.1.0

**February 23, 2019**

The following issues were resolved in this release:
* For an API specification written in RAML, the mocking service returned content that was in YAML, although the returned content should have been in XML.
* The mocking service returned a misleading error message when `baseURI` was invalid.

## 2.1.0

**January 10, 2019**

The following issues were resolved in this release:

- 
[SE-8276] - Issues with Design Center 
- 
[SE-8614] - Request header 'Accept' failing when application/xml is present before application/json 
- 
[SE-8666] - Mocking service for OAuth 2.0 requires users to provide both authorization header and access token 
- 
[SE-8745] - Mocking service required parameters are allowed to be left out 
- 
[SE-8790] - Mocking Server Validation on Message Body 
- 
[SE-8999] - RAML in Design Center: Unexpected token A in JSON at position 1 
- 
[SE-9588] - Mock Service returns 404 for paths with hyphens in 3rd level resource name 
- 
[SE-9830] - Mock service api always return 400 
- 
[SE-9990] - JSON Schema defined inline in Design Center RAML gives error, OK on Studio 
- 
[SE-10045] - Incorrect Datetime-only format error when trying on mocking service from design center 
- 
[SE-10194] - RAML issue with optional enum type headers 
- 
[SE-10222] - additionalProperties=false in RAML are ignored by Design Center and exchange Mocking services. 

## 1.1.11

**August 21, 2018**

This release fixes the following issue:

- 
The mocking service did not return messages for the 400 response in the correct styling. 

## 1.1.10

**June 30, 2018**

This release fixes the following issue:

- 
TLS 1.0 and 1.1 were still supported. Now, only 1.2 is supported. 

## 1.1.9

**May 19, 2018**

The parser is now at version 1.1.42.

## 1.1.8

**April 21, 2018**

- 
Invoking a resource that required the `uriParameter`(e.g., “/main/{attname}”) returned the example response for root instead of the defined example.
- 
Invoking a resource that required a `uriParameter`and then using the example parameter in a GET or PUT method resulted in a response containing the complete API specification.

## 1.1.7

**March 24, 2018**

This release bumps the parser and includes bug fixes.

### Improvements

Bumped parser to 1.1.41.

### Fixed Issues

- 
Parsing no longer returns an Error for XML and Schema valid. 
- 
Fixed an issue with getting validation errors while building RAML for XML with Attributes and Inner text. 
- 
Fixed an issue that prevented some methods that return an Array from correctly showing the response example. 

## 1.1.6

**February 24, 2018**

This release fixes several bugs.

### Fixed Issues

- 
A problem that prevented validation datetime query parameters with format RFC3339. 
- 
The issue causing RAML with a null response to return "message": in the HTTP response with 0 length. 
- 
The `multipleOf`facet validation issue.

## 1.1.5

**January 13, 2018**

This release resolves a few issues:

### Resolved Issues

- 
Fixed a problem related to a URI parameter name containing a hyphen (-) character. 
- 
Fixed an issue with making a request that has a empty body of type application/json. 
- 
Fixed a bug that returned a 400 "body: unknown type any" when using a body with an example that has no type definition. 

## 1.1.4

**December 16, 2017**

This release introduces the following improvements and resolved issues:

### Improvements

- 
Using the mocking service from a proxy application overrides the mocking service of the API itself. 
- 
The Authorization header check for path simulation has been removed. 
- 
When you don’t specify the main example for a DataType, the mocking service provides the examples defined for each property. 

### Resolved Issues

- 
Using a proxy application, the mocking service now validates the Body of the method when you try to POST it. 
- 
Using a base URI ending with / no longer causes a 404 error. 
- 
The mocking service now recognizes object type as an enum in a URI parameter. 
- 
Enforcement of a required data type has been fixed. An absent data type or one that does not include all required fields is rejected. 
- 
The problem related to using the RAML anonymous security scheme has been fixed. 

## 1.1.3

**October 21, 2017**

This release focuses on bug fixes.

### Improvements

- 
Enhanced the Mocking Server to respond with random examples if more than one is available. 
- 
A successful mock creation POST request now returns a 201 response status code instead of 200. 

### Resolved Issues

Fixed to work properly when the RAML has URI parameters.

## 1.1.2

**August 26, 2017**

This release focuses on bug fixes.

### Resolved Issues

- 
Examples defined in datatypes were not displayed properly. 
- 
Mocking server was returning 404 for calls with query parameters. 

## 1.1.1

**July 15, 2017**

This release focuses on bug fixes and closing gaps for RAML 1.0 support.

### Resolved Issues

Fixed an issue preventing API Notebook text from expanding properly.