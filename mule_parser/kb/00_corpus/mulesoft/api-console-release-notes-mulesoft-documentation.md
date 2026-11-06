# API Console Release Notes | MuleSoft Documentation

**Source:** [https://docs.mulesoft.com/release-notes/api-console/api-console-release-notes](https://docs.mulesoft.com/release-notes/api-console/api-console-release-notes)

---

Imported schemas and XML examples now display in the **Documentation** panel.

# API Console Release Notes

API Console automatically generates documentation for an API project. An interactive component, API Console shows information about your REST APIs and their methods, and enables you to test the methods by sending requests. API Console is embedded in multiple MuleSoft platform products including API Designer, Exchange, and Studio.

## 6.6.40

February 9, 2024

### Fixed Issues

| Issue Resolution | ID | 
|---|---|
| W-14846319 | |
| In Design Center and Exchange, Swaqgger JSON now displays valid examples in the response. | W-14874965 | 

## 6.6.39

January 15, 2024

### Fixed Issues

| Issue Resolution | ID | 
|---|---|
| Design Center now generates JSON with nested objects for OAS 3.0. | W-14278539 | 
| AsyncAPI examples now appear in the API Console. | W-14588829 | 
| XML examples now show in REST APIs for OAS. | W-14651311 | 

## 6.6.38

November 11, 2023

### Fixed Issues

| Issue Resolution | ID | 
|---|---|
| Header names are no longer showing in code examples. | W-14454298 | 
| When editing an example, the mocking service URL no longer changes and causes the request to fail. | W-14071465 | 
| The example names are no longer missing when defining the XML schema definition. | W-12646073 | 

## 6.6.37

October 23, 2023

### Fixed Issues

| Issue Resolution | ID | 
|---|---|
| The example for an API is no longer missing. | W-14102462 | 
| An unexpected  | W-13959789 | 

## 6.6.36

September 25, 2023

### Fixed Issues

| Issue Resolution | ID | 
|---|---|
| The cookie authentication value is now sent in the  | W-13832170 | 
| The  | W-14015302 | 

## 6.6.35

August 28, 2023

### Fixed Issues

| Issue Resolution | ID | 
|---|---|
| The child property no longer displays mandatory fields. | W-13772034 | 
| The query parameters are now rendering properly and the parameter value box is no longer hidden. | W-13813608 | 
| A new error message now displays for error code 0. | W-13957966 | 

## 6.6.34

July 31, 2023

### Fixed Issues

| Issue Resolution | ID | 
|---|---|
| A field error no longer overlaps with other inputs. | W-13463891 | 
| Query parameters now list all options. | W-13599882 | 

## 6.6.33

July 3, 2023

### Fixed Issues

| Issue Resolution | ID | 
|---|---|
| The oauth-popup.html no longer causes an access vulnerability. | W-1358830 | 
| The  | W-13547158 | 
| All fields no longer display as required. | W-13536254 | 
| Fields are now rending in the request panel. | W-13524893 | 
| The content for schema types now displays in the API specification. | W-13207777 | 
| An error no longer displays when the  | W-13079436 | 

## 6.6.32

June 5, 2023

### Fixed Issues

| Issue Resolution | ID | 
|---|---|
| The URL protocol is no longer missing when making a request. | W-112688568 | 

## 6.6.31

May 12, 2023

### Fixed Issues

| Issue Resolution | ID | 
|---|---|
| When an OAS API specification scheme is not defined, HTTPS is now the default for the URL protocol. | W-12598786 | 
| For AsyncAPIs, the Kafka key element and its datatype now display in the documentation panel. | W-12528949 | 

## 6.6.30

April 24, 2023

### Fixed Issues

| Issue Resolution | ID | 
|---|---|
| For AsyncAPIs, the Kafka key element and its datatype now display in the documentation panel. | W-12528949 | 

## 6.6.29

March 27, 2023

### Fixed Issues

| Issue Resolution | ID | 
|---|---|
| OAuth 2.0 token generation now populates after the request. | W-12119152 | 
| DIN fonts are now deprecated. | W-12726752 | 

## 6.6.28

February 17

### Fixed Issues

| Issue Resolution | ID | 
|---|---|
| Data type values now display correctly in the documentation panel. | W-12137562 | 
| The request access token is now working as expected with the OAuth 2.0 implicit flow. | W-12227877 | 
| Types now render as expected in the documentation panel when called from other libraries. | W-12276910 | 
| Properties are no longer missing in generated examples when merging  | W-1248170 | 
| The value for  | W-12428173 | 

## 6.6.27

February 1, 2023

### Fixed Issues

| Issue Resolution | ID | 
|---|---|
| Boundary is no longer missing in multipart content-type headers. | W-12465439 | 

## 6.6.26

January 6, 2023

### Fixed Issues

| Issue Resolution | ID | 
|---|---|
| Information is no longer missing when merging  | W-12142859 | 
| The mocking service now receives the correct  | W-12146715 | 
| The information for the  | W-12183115 | 

## 6.6.25

December 19, 2022

### Fixed Issues

| Issue Resolution | ID | 
|---|---|
| The documentation for type is no longer missing when properties are defined as  | W-12065773 | 

## 6.6.24

November 17, 2022

### Fixed Issues

| Issue Resolution | ID | 
| The custom query parameters are no longer reset when the server value is set in the Request panel. | W-12030452 | 

## 6.6.23

October 28. 2022

### Fixed Issues

| Issue Resolution | ID | 
| The request URL now populates correctly. | W-11386481 | 
| The example for string arrays now generate correctly. | W-11798608 | 
| The example for enum types in parameters section are no longer missing. | W-11836777 | 
| The correct value now displays for the header when making requests. | W-11843862 | 
| The  | W-11858334 | 
| You now can allow the OAuth2 Token requests to be prevented. | W-11921592 | 
| The names for security fields now display correctly. | W-11939928 | 

## 6.6.22

October 11, 2022

### Fixed Issues

| Issue Resolution | ID | 
| Parameters are now sent on request. | W-11517665 | 

## 6.6.21

September 16, 2022

### What’s New

- 
For an AsyncAPI with multiple messages for an operation, you can now choose a message from the drop-down menu. 

## 6.6.20

August 26, 2022

### Fixed Issues

| Issue | ID | 
| Optional headers are now shown in the Documentation panel. | W-11429833 | 
| The input fields in the Try it panel now display properly. | W-11486959 | 
| The input fields in the Try it panel no longer display as missing information once rendered. | W-11486967 | 
| The labels of multiple API keys now render correctly in the Documentation panel and in the Request panel. | W-11541233 | 

## 6.6.19

August 5, 2022

### Fixed Issues

| Issue | ID | 
| In OpenAPI, deprecated endpoints are now displaying in the documentation panel. | W-11383870 | 
| Examples in OAS 3.0.0 for content-type application/xml are now displaying tags with a prefix. | W-11423667 | 

## 6.6.18

July 15, 2022

### Fixed Issues

| Issue | ID | 
| An array now displays an element in the API documentation preview. | W-11117349 | 
| The miniItems and maxItems information is now displaying in the data type documentation. | W-11209734 | 

## 6.6.17

June 24, 2022

### Fixed Issues

| Issue | ID | 
| All messages render correctly when there are multiple AsyncAPI messages. | W-11105366 | 
| XML responses render correctly in the response viewer. | W-11196904 | 
| Operation headers for AsyncAPIs render correctly. | W-11308473 | 

## 6.6.16

May 27, 2022

### Fixed Issues

| Issue | ID | 
| Namespace is no longer missing from the body example. | W-11084386 | 

## 6.6.15

May 19, 2022

### Fixed Issues

| Issue | ID | 
| Request responses for images, SVG, and XML no longer cause an XSS vulnerability. | W-11031948 | 

## 6.6.14

May 6, 2022

### Fixed Issues

| Issue | ID | 
| When navigating to the method documentation, the console browser no longer displays an error. | W-10914362 | 
| To increase accessibility, this release adds alt text for icons in the request panel. | W-11083487 | 

## 6.6.13

April 18, 2022

### Fixed Issues

| Issue | ID | 
| The API server description no longer causes an XSS vulnerability. | W-10881270 | 

## 6.6.12

April 7, 2022

### Fixed Issues

| Issue | ID | 
| This release removes non-inclusive language. | W-10921614 | 
| XML name can now override type name. | W-10743611 | 
| OAuth 2.0 token request events now dispatch properly. | W-10749540 | 
| The properties of the data type  | W-10928298 | 
| When the  | W-10839261 | 

## 6.6.11

March 3, 2022

### Fixed Issues

The Code icon is no longer missing in the response example.

## 6.6.10

February 25, 2022

### Fixed Issues

- 
A long XML schema example is not duplicated. 
- 
Saving response does not generate an empty .HAR file. 
- 
Headers are reset when navigating to another operation without headers. 
- 
Adding a new custom header changes focus to the newly added field properly. * Icon for saving .HAR response is no longer missing. 
- 
An array response collapse button displays properly. 

## 6.6.9

January 28, 2022

### What’s New

- 
Added request body description to documentation. 
- 
Added test for overwriting `Content-Type`header with`multipart`body.
- 
Added functional tests for flattened model. 
- 
Added test for sending request with a file attachment as body. 

## 6.6.8

January 10, 2022

### What’s New

- 
Added documentation support for allOf types in OAS 3.0 APIs. - 
Added functional tests for responses. 
- 
Added functional tests for AsyncAPIs. 
- 
Added functional tests for OAS 3.0 APIs. 
- 
Set up visual tests to run as part of GitHub actions. 
 
- 

### Fixed Issues

- 
The request panel renders correctly. 
- 
Multipart body has the correct type stored internally when initializing. 
- 
OAuth scopes renders correctly. 

## 6.6.7

December 20, 2021

### Fixed Issues

- 
Populating credentials after removing a header does not throw an error. 
- 
Modifying a header does not clear the previous changes after populating credentials. 

## 6.6.6

November 30, 2021

### New Features

- 
Added documentation panel tests for security and types. 
- 
Added documentation panel tests for endpoints and methods. 
- 
Added request panel tests for query parameters. 
- 
Added basic visual tests. 

### Fixed Issues

- 
The anypoint-web-components that use an API are available in FF. 
- 
Request panel fields are updated after credentials population event. 
- 
Annotations display correctly in partial models. 
- 
Empty headers are not removed from request editor if body was present in request. 
- 
Headers are updated in the model when input is changed.* Request with a file attachment in the body is sent. 

## 6.6.5

October 19, 2021

### New Features

- 
Increase timeout for request test (921794bf) 
- 
Authorization in request panel (ce15b4eb) 
- 
Request panel tests (07f9a5f3) 
- 
Increase timeout (d988c6f3) 
- 
Increase timeout (10e49c5b) 
- 
Basic documentation panel tests (76200b0e) 

### Fixed Issues

Use timeout to avoid using many nextframes.

## 6.6.4

September 24, 2021

### New Features

- 
Added support for populating parameters with custom domain properties in the request editor through the `populate_annotated_fields`event.
- 
Added multiple component tests to request panel (Headers & Body, Authorization) and documentation. 

## 6.6.3

### New Features

- 
Added `--api-responses-method-padding-left`and`--api-responses-method-padding-right`CSS variables.
- 
Added listener for `securitysettingsinfochanged`to populate security settings fields in request panel.

### Fixed Issues

- 
Fixed visual bug in code selector divider in responses documentation. 
- 
Fixed bug where summary would not clear when changing AMF model to a library. 
- 
Removed `force-resolutions`package to avoid sub-dependency clashes.

## 6.6.2

August 27, 2021

### New Features

- 
Multiple new `data-`attributes across components enable testing.

### Fixed Issues

- 
Request URLs include optional query parameters. 
- 
XML examples correctly render `application/xml`bodies.
- 
Header autocomplete opens on focus. 
- 
Selecting the previously selected item closes the drop-down menu. 
- 
The newly added `force-resolutions`dependency resolves specific component versions in sub-dependencies.

## 6.6.1

August 11, 2021

### Fixed Issues

- 
`arc-response`renders responses correctly.

## 6.6.0

August 6, 2021

### New Features

- 
The `persistCache`property prevents cache clearing in the request panel after an AMF property change.
- 
API Console renders the description for named examples. 

### Fixed Issues

- 
API Console correctly generates and shows nullable properties examples. 
- 
XML generated examples consider a defined XML name. 
- 
The response time has the correct number of digits after the decimal place. 
- 
Scalar types show generated examples without duplication. 

## 6.5.2

July 26, 2021

### New Features

- 
Added `oneOf`types to the available types displayed in type documentation.
- 
Added the option to disable required parameters in the request panel. 

### Fixed Issues

- 
Media type names in the selector display correctly. 
- 
The `Content-Type`header is sent in the request correctly.
- 
Application authorization flow is processed correctly. 

## 6.5.1

July 12, 2021

### Fixed Issues

- 
Fixed bug where request panel was allowing user to encode payload multiple times, creating a breaking payload in most cases 
- 
Fixed bug with rendering examples when wrapped property was set 
- 
Fixed bug where tabs in Code Examples would flicker endlessly 
- 
Fixed bug where decimal numbers would always show as invalid in input 

## 6.5.0

June 25, 2021

### New Features

- 
Added support for OAS 3 `deprecated`property
- 
Added support for flattened AMF model 
- 
Added `renderFullPaths`property to render endpoints as their full paths, without indentation
- 
`rearrangeEndpoints`now sorts endpoints alphabetically by path

### Fixed Issues

- 
Fixed OAuth grant type issue for OAS 2 APIs 
- 
Fixed bug where navigating between some endpoints caused incorrect URI parameters to appear 
- 
Fixed bug in enum array properties where the enums where not being rendered 
- 
Fixed missing application/xml media types in body 
- 
Fixed API-asset showing incomplete description of JSON-schema 

## 6.4.12

June 11, 2021

### Fixed Issues

- 
Add Optional Content Type for File upload Multipart 
- 
When "Query Parameters" or "Query Strings" is added, it is not displayed in "Try it" panel 
- 
Missing server description in summary 
- 
Change toggle button to checkbox for "enable/disable header" option and other minor correction 

## 6.4.11

May 26, 2021

### Fixed Issues

- 
Arrows in responses tabs were not rendering correctly 
- 
Toggling optional parameters was changing the values of the parameters 

## 6.4.10

May 14, 2021

### New Features

- 
Convert multiline headers to single line when parsing 

### Fixed Issues

- 
It is not possible to add a new Field in the multipart-payload-editor, it gets removed after adding it 
- 
Missing "anyOf" details for types 
- 
Union type examples of arrays not displaying as arrays 
- 
The title of a property, defined as a union of arrays, appears as "undefined" 
- 
Array type title appears as "undefined" 
- 
Wrong title for a property defined as an array of numbers 
- 
Code example curl shows undefined 
- 
Use description from Parameter over schema if available 
- 
Query parameter input value can hardly be seen 
- 
Example section showing extra spaces 
- 
Tabs flicker in Code Examples 

## 6.4.9

April 23, 2021

### New Features

- 
Added multiple new CSS variables for further fine tuning of styling 

### Fixed Issues

- 
"Show optional parameters" has been re-added 
- 
When adding multiple headers with the same name, the first instance would not reflect the correct value of the header 
- 
Example names are now ignored if they match the media type + a numerical iteration (e.g. `application/json2`)
- 
Hide type name for inline types (if the type name is `default`)
- 
Mintor styling fixes 

## 6.4.8

March 29, 2021

### Fixed Issues

- 
Fix `content-type`header not being sent in requests
- 
Add warning messages to body form items in request 
- 
Fix styling for request panel subheaders 
- 
Fix warning messages spacing in query parameters 

## 6.4.7

March 25, 2021

### Fixed Issues

- 
Missing examples for parameters, types and headers 
- 
When a query parameter is defined as optional, the checkbox "Show optional parameters" is not displayed 
- 
Content type not being set on requests 
- 
Font labels for URI parameters and Query parameter sections are large and labels are indented 

## 6.4.6

March 25, 2021

### Fixed Issues

- 
Content type being sent when sending requests 
- 
Warning messages overlapping with multiple required headers 
- 
Header schemas are now copied from original AMF model ones when switching between source and form editors 
- 
Fixed version URI parameter being replaced with API version 
- 
Fixed example generation with tracked elements for partial models 
- 
Fixed autocomplete not closing when clicking outside of overlay 
- 
Fixed headers being added/removed incorrectly 
- 
Disable copy button when there are no headers 

## 6.4.5

March 9, 2021

### New Features

- 
For required fields that have no other restrictions, do not show as invalid. Instead, show an info message under the field 
- 
Added `noOverview`property to remove`Overview`items from navigation. If enabled, clicking on the endpoint name will select it, and the arrow will toggle the collapsible element
- 
Added `operationsOpened`property to toggle all operations opened/closed
- 
Added `credentialsSource`to optionally populate credentials in the request editor

### Fixed Issues

- 
Server selection for slotted servers was not changing the request URL 
- 
Copy button in Headers is now disabled if there are no headers 
- 
Response headers are hidden until deliberately shown 
- 
Response body was not being formatted 
- 
Response body was not being rendered with error responses 
- 
Re-add CSS variable to style form titles in request panel, and fix indenting in the titles 

## 6.3.7

February 22, 2021

### Fixed Issues

- 
Show message object schema in documentation view for `subscribe`operations

## 6.4.4

February 17, 2021

### Fixed Issues

- 
Message schema was not being shown in api-method-documentation view 

## 6.4.3

February 5, 2021

### Fixed Issues

- 
Boundary missing when content-type is multipart 

## 6.3.6

January 7, 2021

### New Features

- 
Add PKCE OAuth flow in advanced settings in request panel. Enabled by default if declared in specificartion, can be enabled/disabled manually 

### Fixed Issues

- 
Fixed bug where the `Content-Type`header inferred from the payload was not being added in the Request Panel
- 
Fixed bug where client_secret was not being sent alongside thee rest of the information for the OAuth2 Password Grant 
- 
Fixed visual bug where channel and url were too compressed if channel was too long 
- 
`anyOf`in body payload now appears correctly
- 
Changed an instance of "endpoints" to "channels" for AsyncAPIs 
- 
Do not prefix AsyncAPI url with `http`in summary view
- 
Fixed operation label styling in summary and endpoint documentation views 
- 
Add styling to Publish and Subscribe operations in endpoint documentation 

## 6.3.5

December 9, 2020

### Fixed Issues

- 
Fixed bug where changing the server would not immediately update the URL in the method documentation and endpoint documentation 
- 
Fixed bug where selecting Custom URI would make selector disappear if only one other server option was present 

## 6.3.4

December 4, 2020

### Fixed Issues

- 
Bug UI bug where Summary and Endpoint views showed a small gray box where method would be 
- 
Fixed example generation bug for compact model where the value for a number would sometimes generate empty string instead of `0`

## 6.3.3

December 3, 2020

### Fixed Issues

- 
Fixed bug where endpoints with closely related named may cause one of them to appear blank in navigation 
- 
Fixed bug where multiple, fully expressed endpoints which could be nested, would appear blank 
- 
Fixed bug in URL handling where, if the url did not have examples for a query param, an error would be thrown and nothing would render 

## 6.3.2

December 2, 2020

### New Features

- 
`api-request-panel`does not return empty content if model does not belong to a WebAPI. This behavior is expected of whoever renders it
- 
`api-console`and`api-console-app`check if AMF belongs to a non WebAPI, and hide the request panel & propagate the`noTryIt`accordingly

### Fixed Issues

- 
Fixed bug where `baseUri`on`api-method-documentation`was not propagating the change to`api-url`

## 6.3.1

December 1, 2020

### Fixed Issues

- 
Fixed regression in `api-navigation`that caused an error to happen when the first endpoint in a specification had a URI parameter in it

## 6.3.0

November 30, 2020

### New Features

- 
Annotation name is now rendered with the annotation 
- 
AsyncAPI 2.0 - 
Support for non HTTP protocols in documentation 
- 
`api-request-panel`is hidden when present model is from an AsyncAPI
- 
`Endpoints`renamed to`Channels`
- 
Operation URL is displayed differently for non-HTTP protocols 
- 
Example and snippets are hidden for non-HTTP protocols 
 
- 

### Fixed Issues

- 
Required query parameters are now added to code snippets 
- 
Fixed bug with URL persisting after being removed from the spec 
- 
Fixed password grant type in Authorization where client secret was not being passed into the grant 
- 
Fixed bug where unordered endpoints would cause a endpoint path name to be shortened when it shouldn’t be 
- 
WCAG - 
Navigation collapse/expand was not being properly read by screen reader 
- 
Query parameters input box was not associated with any form label 
- 
Code Examples and Body collapse/expand were not being properly read by screen reader 
- 
Server selector dropdown was not properly associated with form label 
 
- 

## 6.2.6

September 28, 2020

### Fixed Issues

- 
Fixed bug example generation for partial models where some properties would not appear in rendered example if their values were empty strings, false boolean values or 0 integer values 
- 
Fixed bug in type documentation where enum array properties weren’t being rendered correctly 
- 
Fixed bug where the queryString node was defined on an operation, but the query parameters didn’t render in the try it panel 
- 
Fixed bug where XML example structures did not match the definition in the RAML type 
- 
Fixed bug where JSON schemas in RAML did not render completely 

## 6.2.5

August 31, 2020

### New Features

- 
New css variable for text wrapping for navigation items 

### Fixed Issues

- 
Changing RAML baseUri made query parameters section disappear 
- 
Duplicated examples in type documentation 
- 
Query string documentation was missing 
- 
Media types selector was missing when multiple media types defined in spec 
- 
Increase space between input and selectors and their labels 
- 
Table view was not displaying string examples 
- 
When setting no-auto-encoding annotation to URL elements, components were still being encoded 

## 6.0.4

July 23, 2020

### Fixed Issues

- 
Client secret missing on request when authorizing for client_credentials authorizationGrants 

## 6.2.4

July 21, 2020

### New Features

- 
Add rearrangeEndpoints property to api-documentation component, so it will be passed down to the api-summary if present 
- 
Pass down rearrangeEndpoints value to api-documentation as well 

### Fixed Issues

- 
Add scrolling to response codes in documentation to be able to see all possible response code options 
- 
Example generation for partial models now accounts for arrays with only 1 item appearing as a single object in partial model 
- 
Fix issue where documentation pages were listed in navigation with its description content rather than its title 

## 6.2.3

July 7, 2020

### New Features

- 
Implement oneOf, anyOf from OAS3 

### Fixed Issues

- 
When a library is applied, documentation is blank for types 
- 
Server menu list width should fit dropdown width 
- 
URI in api-documentation and api-request-panel component does not update when servers in model change 
- 
Duplicate headers and headers from other methods shown in request panel 
- 
API Console do not understand readOnly fields when generating examples for OAS3 APIs 
- 
A property of type Object is rendered as a String 
- 
Library type documentation is blank 
- 
Missing response examples 

## 6.0.3

June 25, 2020

### Fixed Issues

- 
Client Id and Client secret fields missing for client_credentials authorizationGrants 

## 6.2.2

June 12, 2020

### Fixed Issues

- 
XML example with missing "e" at the end 
- 
Response body type not rendering 

## 6.2.1

May 27, 2020

### Fixed Issues

- 
Examples generation after AMF model changes 
- 
Auto selection of a custom server when no servers are defined in an API 
- 
Support for the partial AMF model when querying for servers 
- 
api-request event listener is now registered on the request panel instead of the eventsTarget 
- 
Duplicated content-type header on the request editor 
- 
XSS via authorization URI 
- 
Authorization method styling issue 
- 
Restored support for partial model when getting servers 
- 
Additional model support when computing servers 
- 
Operation and endpoint servers override base servers when switching to Try It panel 
- 
Fix display of enum values for array type document 
- 
Added OAS' external documentation support in the navigation 

## 6.2.0

April 27, 2020

### New Features

- 
OAS 3 support 
- 
Support for multi-server definitions 
- 
Custom servers 
- 
OAS multi-authorization 
- 
OAS links and callbacks 
- 
Support for `no-auto-encoding`annotation

## 6.1.1

March 31, 2020

### New Features

- 
fixed issues with multiple security scheme names in the navigation by adding name of the scheme to the type 
- 
upgrading AMF processor helper to better support OAS 3 features and build background for OAS 3 full support 
- 
upgraded `lit-html`and`lit-element`libraries to the latest version
- 
upgraded dev dependencies 

## 6.0.1

February 6, 2020

### New Features

- 
cleared dependencies 
- 
updated api-summary component with sanitization enabled for license URLs 

## 6.0.0

January 16, 2020

### New Features

- 
Upgrade to final web components specification: replacing HTML imports with JavaScript modules 
- 
Replacing Polymer with super lightweight, almost native, `LitElement`. This triggers a series of changes:- 
All dash-case attributes are now "no-dash", lowercase, web style attributes. For example old `redirect-uri`is now`redirecturi`. This is true for all properties used as HTML attribute. Properties names are the same.
- 
New templating engine. API Console now uses `lit-html`which is performant HTML templating system.
- 
Build process is completely different. See documentation at [https://docs.api-console.io](https://docs.api-console.io).
 
- 
- 
Redesigned base input controls. API console now uses own, material design based, basic UI input controls. It comes with 3 predefined styles: - 
Default - Material design filled style 
- 
Outlined - Material design outlined state controlled by `outlined`attribute
- 
Anypoint - Compatibility layer with the Anypoint platform. Controlled by `compatibility`attribute
 
- 
- 
The request panel (aka try it) now only renders editors that corresponds to the API data model. This means that, for example, if headers are not defined for given operation then headers panel is not rendered. 
- 
Dropped support for tabs view for the editors in the request panel and they are stacked now. 
- 
Code mirror dependency requires some additional libraries that won’t work inside JavaScript module. This means that those libraries have to be included into the web application before initializing the element. See the documentation or readme file for details. 
- 
API Console is now WCAG compliant. All components used to build the console passed axe-core tests and therefore are fully accessible. 
- 
The application and the component are now split into separate components. Use `api-console`custom element for embedding the console inside existing web application and`api-console-app`to create stand alone application.
- 
New demo pages. Preview the console with `npm start`command (run inside cloned repository) to see API console with various scenarios and configuration options.
- 
Removed any reference to CSS mixins (the `@apply`function). All styling options are now defined via CSS variables. Any styles defined for previous version of API console won’t work.
- 
Minimised use of icons in favour of regular buttons with labels. 
- 
This release contains tones of bug fixes and improvements reported by the community and our customers ❤ 
- 
The Chrome proxy extension banner is not rendered by default. Set `allowExtensionBanner`property to initialize the console with the extension support.
- 
Added configuration option to set a static OAuth 2 client ID and secret for the application. This way it is easier to demo an API by providing demo client id. 
- 
Added markdown sanitization 
- 
Now XML schemas and examples are propertly rendered. 
- 
Huge XML schemas are now not syntax highlighted (above 10K characters) as it causes the browser to hang. 
- 
XML examples are now properly formatted and RAML type name is properly resolved (instead of `<model>`element)

## 3.0.34

August 30, 2019

### New Features

- 
New headers for mocking service requests 

## 3.0.33

June 26, 2019

### Fixed Issues

- 
Various fixed issues. 

## 5.0.2

May 29, 2019

### New Features

- 
Updated AMF parser version and support for new model structure 
- 
Fixed examples rendering in the type documentation 
- 
Now type documentation renders generated JSON/XML schema when RAML’s `mediaTypes`/ OAS'`produces`property is set
- 
Examples now have default values for boolean, number, and null values when default value and example is missing 

## 3.0.32

May 6, 2019

### New Features

- 
Bump parser to version v1.1.50 

## 5.0.1

March 13, 2019

### Fixed Issues

- 
Fixed vulnerability issues. 

## 6.0.0-preview.1

March 1, 2019

### New Features

- 
Preview of ES6 modules version of API Console. This is an early preview, not targeted for production. Try it and give us your feedback. 

## 5.0.0

January 15, 2019

### New Features

- 
Support for AMF data model instead of RAML parser allows to render a documentation for RAML and OAS specification and enables the console to read even more API types 
- 
Users can now define new properties (headers, query parameters) in the request editor that are not defined in the API spec. 
- 
API console now works with web components specification version 1. This allows to target all browsers with native support for web components spec and those with polyfill support. 
- 
Build process to create separate bundles for ES5 and ES6 enabled browsers so modern browsers can run the console with minimal required setup 
- 
Redesigned styling API to enable consumers to apply corporate theme using CSS variables 
- 
Build tools for the console now are based on AMF library to generate new data model 
- 
Redesign of the documentation part to deliver best in class documentation tool for APIs 
- 
Redesign of navigation for faster recognition of the API structure and to search for an endpoint 
- 
Added documentation for security schemes 
- 
Added code examples in the method documentation 
- 
Updated how union types are rendered - now it renders type name in the type selector instead of “Variant” 

### Fixed Issues

- 
Feedback from our customers and the open source community was applied to this version resolving tens of issues regarding performance, stability and design 

## 5.0.0-rc.2

January 12, 2019

### Fixed Issues

- 
Fixing CORS extension banner behavior. 

## 5.0.0-rc.1

January 11, 2019

### New Features

- 
Support for AMF data model instead of RAML parser allows to render a documentation for RAML and OAS specification and enables the console to read even more API types 
- 
Users can now define new properties (headers, query parameters) in the request editor that are not defined in the API spec. 
- 
API console now works with web components specification version 1. This allows to target all browsers with native support for web components spec and those with polyfill support. 
- 
Build process to create separate bundles for ES5 and ES6 enabled browsers so modern browsers can run the console with minimal required setup 
- 
Redesigned styling API to enable consumers to apply corporate theme using CSS variables 
- 
Build tools for the console now are based on AMF library to generate new data model 
- 
Redesign of the documentation part to deliver best in class documentation tool for APIs 
- 
Redesign of navigation for faster recognition of the API structure and to search for an endpoint 
- 
Added documentation for security schemes 
- 
Added code examples in the method documentation 
- 
Updated how union types are rendered - now it renders type name in the type selector instead of “Variant” 

### Fixed Issues

- 
Feedback from our customers and the open source community was applied to this version resolving tens of issues regarding performance, stability and design 

## 5.0.0-preview.3

January 2, 2019

### New Features

- 
Updated styles to enable theming 
- 
Added demo page with dark theme 

## 5.0.0-preview-1

October 31, 2018

### New Features

- 
It is fully functional 
- 
Has working demo pages 
- 
Documentation for the HTML component 
- 
Documentation for building application 
- 
Build tools (which is the reason of creating the release) 
- 
Build documentation 
- 
Styling documentation 

## 3.0.31

September 26, 2018

### New Features

- 
Bump parser to version v1.1.48 

### Fixed Issues

- 
Bug fixing 

## 4.2.3

September 21, 2018

### Fixed Issues

- 
Forcing "marked" library update due to security vulnerability 

## 4.2.2

September 20, 2018

### New Features

- 
Updating dev dependencies 
- 
Bumping version 
- 
Removing silent bower installation 
- 
Updating tests configuration 

### Fixed Issues

- 
Fixing bower configuration 

## 3.0.30

July 20, 2018

### New Features

- 
Bump parser to version v1.1.45 

## 5.0.0-preview-0

July 1, 2018

### New Features

- 
It is fully functional 
- 
Has working demo pages 
- 
Build tools (which is the reason of creating the release) 
- 
Build documentation 

## 3.0.29

June 7, 2018

### New Features

- 
Bump parser to version v1.1.43 

## 3.0.28

May 10, 2018

### New Features

- 
Bump parser to version v1.1.42 

## 3.0.27

April 21, 2018

This release includes the following enhancement and resolves a number of issues:

### Enhancements

- 
Bumped RAML Parser to version to [1.1.41](https://github.com/raml-org/raml-js-parser-2/releases/tag/1.1.41).

### Fixed Issues

- 
Properties defined in the **items**facet were not displayed.
- 
Values in optional headers were required to be specified. 
- 
Properties defined in response bodies for custom data types were not displayed in the console. 
- 
The error message “Cannot read property 'type' of undefined” appeared when a type was defined as an array and the array did not contain any elements. 

## 3.0.26

February 24, 2018

This release includes the following enhancements and resolves a number of issues:

### Enhancements

- 
Bumped RAML Parser to version to [1.1.40](https://github.com/raml-org/raml-js-parser-2/releases/tag/1.1.40).
- 
Because API Manager 1.x does not support digest authentication, the error message has been changed for Digest Authentication as follows: *Digest Authentication is not supported in Try it.*

### Fixed Issues

- 
When including a data type, the invalid error in IE *Object doesn’t support property or method `include`*appeared.
- 
When selecting the Try It option, if the Request section is expanded and has the details, the Response section remained collapsed. 
- 
The problem declaring Arrays using defining items. 
- 
Partially blocked visibility of the tooltip for traits help. 
- 
A problem with the example defined for the query parameter. 

## 3.0.25

January 13, 2018

This release resolves a number of issues.

### Resolved Issues

- 
Fixed an issue that caused a missing description and examples when using a security scheme. 
- 
Body extending from a type defined at a library is now displayed correctly. 
- 
Fixed the issue that required you to scroll to the right to see an example having many attibutes. 
- 
Fixed the issue causing API Console to throw "Custom Security Schemes are not supported in Try It”. 
- 
Fixed an issue related to using inline !include in query param rendering. 

## 3.0.21

November 4, 2017

This release introduces improvements and bug fixes.

### Improvements

Bump JS RAML Parser to [v1.1.31](https://github.com/raml-org/raml-js-parser-2/releases/tag/1.1.31)

### Resolved Issues

Display descriptions in sub-level resources.

## 3.0.20

August 26, 2017

This release focuses on a few RAML 1.0-related improvements and bug fixes.

### Resolved Issues

- 
The description of types was not being displayed when defined using libraries. 
- 
Types were not displayed correctly at Types section. 
- 
Description of inner resources (those defined at sublevels) were not displayed. 
- 
API Console would not parse Raml files when using IE 11. 
- 
API Console was not rendered in IE. 

### Improvements

Bumped RAML Parser to version to [1.1.29](https://github.com/raml-org/raml-js-parser-2/releases/tag/1.1.29)

## 3.0.19

July 15, 2017

This release focuses on a few RAML 1.0-related improvements and bug fixes.

### Resolved Issues

- 
Fixed an issue causing types defined in libraries to display incorrect information. 
- 
Fixed an issue preventing libraries from expanding and causing a display problem with the console library preview. 

### Improvements

- 
Bumped RAML Parser to version [1.1.24](https://github.com/raml-org/raml-js-parser-2/releases/tag/1.1.24).
- 
Added support for the file type to the Try It view. 

## 3.0.18

June 17, 2017

This release focuses on a few RAML 1.0 related improvements and bug fixes.

### Resolved Issues

- 
Fixed an issue preventing the console from showing schemas that contain patterns that used `|`.
- 
Fixed an issue preventing body parameters of type 'application/x-www-form-urlencoded' from being rendered in the Try It view. 

### Improvements

- 
Bumped the RAML Parser to version [1.1.24](https://github.com/raml-org/raml-js-parser-2/releases/tag/1.1.24)
- 
Added showing the request URL in the Try It view even before you send out the request. 

## 3.0.17

June 3, 2017

This release focuses on a few RAML 1.0 related improvements and bug fixes.

### Resolved Issues

- 
API Console was not accurately displaying enum values defined in a library. 
- 
Arrays defined using type expression shortcut were not displayed correctly. 
- 
The order of query parameters and types properties were not preserved when navigating to a resource. 
- 
API Console was not showing DataTypes examples when using inheritance. 
- 
API Console returned an Invalid Type error inside the TryIt panel when using RAML 1.0 array types. 
- 
API Console renders example information twice. 
- 
Parameter examples were not shown when defined in a response. 
- 
The description and examples of Pass Through security scheme were missing from API console. 
- 
Validation of uriParameters failed when using a custom type. 
- 
API Console did not entirely show examples when provided in type definitions (either for the entire type or single properties). 
- 
Rendering issues occurred when a type extends from another type declaration. 
- 
A validation issue occurred when the type is a number and has a related enum. 

### Improvements

- 
Bumped RAML Parser to version [1.1.20](https://github.com/raml-org/raml-js-parser-2/releases/tag/1.1.20)
- 
Enhanced performance when rendering large projects. 

## 3.0.16

April 8, 2017

This release focuses on minor bug fixes.

### Resolved Issues

- 
Fixed an issue preventing API documentation from being displayed at the Portal due to incorrect url resolution after library expansion. 
- 
Fixed an issue preventing error feedback from being displayed (white page or greyed page was displayed instead, depending on implementation). 
- 
Fixed an issue that prevented response type and examples from being refreshed accurately when changing methods. 
- 
Fixed an issue causing multiple inheritance types to be incompletely rendered in the method response. 

### Improvements

- 
Bumped RAML Parser to version to [1.1.19](https://github.com/raml-org/raml-js-parser-2/releases/tag/1.1.19)
- 
Added an improvement for rendering the root description of an API on the top of the page. 

## 3.0.14

March 11, 2017

This release includes a JS parser update.

### Improvements

Bumped JS parser version to [1.1.14](https://github.com/raml-org/raml-js-parser-2/releases/tag/1.1.14).

## 3.0.13

February 3, 2017

This release includes a JS parser update.

### Improvements

Bumped JS parser version to 1.1.13.

## 3.0.12

January 14, 2017

This release includes a JS parser update.

### Improvements

Bumped JS parser version to 1.1.12.

## 3.0.11

December 3, 2016

This release includes several fixes for rendering information as well as fixes for issues around RAML 1.0.

### Resolved Issues

- 
Add support for Pass Through to reflect the complete set of security schemes defined in RAML 1.0. 
- 
In the previous version, the error output was not correctly handled and had to be updated. 
- 
Several other smaller bug fixes. 

### Improvements

- 
Bumped JS parser version to 1.1.8. 
- 
Several other smaller improvements. 

## 3.0.9

November 19, 2016

### Improvements

Bumped JS parser version to 1.1.6.