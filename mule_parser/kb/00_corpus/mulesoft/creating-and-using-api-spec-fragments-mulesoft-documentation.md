# Creating and Using API Spec Fragments | MuleSoft Documentation

**Source:** [https://docs.mulesoft.com/anypoint-code-builder/des-create-api-fragments](https://docs.mulesoft.com/anypoint-code-builder/des-create-api-fragments)

---

![Anypoint Code Builder icon highlighted in the activity bar](_images/anypoint-code-builder-view.png) 

# Creating and Using API Spec Fragments

Using Anypoint Code Builder, you can create your own API fragments and publish them to Anypoint Exchange to share with other people, add fragments from Exchange to your API specification, or create fragments in your project to add directly to your API specification. Alternatively, you can create and add a fragment directly in your project without publishing it to Exchange.

Anypoint Code Builder supports scaffolding these schema fragment files if they’re referenced from API specs:

| Avro | JSON | RAML | |
|---|---|---|---|
| 
 | Yes | Yes | No | 
| 
 | No | No | Yes | 
| 
 | No | No | Yes | 
| 
 | No | No | Yes | 
| 
 | No | No | Yes | 

If you add a fragment that isn’t supported, the scaffolder doesn’t add these fragments as project dependencies when you import the spec from Exchange. However, you can scaffold schemas that are specified inline within the spec.

The process for adding a fragment from Exchange is:

- 
[Add the API fragment from Exchange](#add-fragment-to-project)to your API spec project as a dependency.
- 
[Add the API fragment to your API spec](#add-fragments-to-spec)using the`$ref`(OAS and AsyncAPI) or`!include`(RAML) directives.

The process for adding a fragment without publishing it to Exchange is:

- 
[Create and add a fragment directly in your project](#create-add-fragment-directly)without publishing it to Exchange.

Use these examples to explore the functionality of Anypoint Code Builder:

- 
`example-oas-fragment`
- 
`example-oas-api-spec`
- 
`example-asyncapi-avro-fragment`
- 
`example-asyncapi-spec`
- 
`example-asyncapi-spec-inline-avro`

## Before You Begin

Before adding fragments:

- 
Understand the basics of designing API specifications. To see where adding fragments fits in the journey from API design through deployment, see [Take Your API Specification from Design Through Deployment in Mule](tutorials#modular-learning-paths).
- 
Have some familiarity with [business groups](../access-management/business-groups).When you publish your API fragment to Exchange from Anypoint Code Builder, the IDE requests the name of the business group. See [Anypoint Platform Business Groups](../access-management/business-groups).

## Create an API Fragment and Publish it to Exchange

The process for creating and publishing API spec fragments is similar to the process for API specs.

To create an API spec fragment:

- 
In the activity bar of the IDE, click the ![](_images/icon-ms-logo.png) ( (**Anypoint Code Builder**) icon.![Anypoint Code Builder icon highlighted in the activity bar](_images/anypoint-code-builder-view.png)  
- 
From **Create**, click**Design an API**:![*Design an API* link highlighted in the *Create* section](_images/design-api-1.png)  
- 
In **Design an API**, click the**API Fragment**tab:![API Fragment tab on the Design an API page](_images/des-api-fragment.png) Ensure that you select the **API Fragment**tab.
- 
Complete the **API Fragment**form:Field Name Field Value **Project Name**Unique name for your fragment. This name is used as the fragment title in Exchange and name of the fragment file. For example, if the project name is *Example OAS Fragment*, the specification file name is`example-oas-fragment`.To reuse an existing project name, you must delete the project that is already using the name first. See [Deleting API Specs and Fragments](des-delete-api-projects).**Project Location**Your home directory or another directory you create. Don’t create the project within another project directory. **API Specification Language**Select **OAS 3.0 (YAML)**to use the[example](#example-oas-api-frag)in this procedure.**<Language> Syntax**The syntax for the selected language. Select **YAML**to use the[example](#example-oas-api-frag)in this procedure.
- 
Click **Create Project**.If prompted, trust the authors of the files in the folder. When the project is ready for editing, the API fragment project opens in the Explorer view. For example, this OAS 3.0 (YAML) API fragment: ![API Fragment tab on the Design an API page](_images/des-api-fragment-new.png) 
- 
Continue designing your API fragment. As you enter elements, use [auto-complete](start-discover-ui#use-autocomplete)(or press Ctrl+Space) to display available options within the context.If you created an OAS 3.0 (YAML) fragment project, you can replace the initial API fragment with the [example](#example-oas-api-frag)code to test adding fragments to a spec.
- 
[Publish your fragment to Exchange](des-publish-api-spec-to-exchange).The status bar shows the progress. When complete, you see a message that the API fragment successfully published to Exchange. 
- 
Navigate to Anypoint Platform and log in using your credentials. ## Show me how- 
US cloud (non-EU host): [Anypoint Platform (US)](https://anypoint.mulesoft.com/login/)
- 
EU cloud (EU host): [Anypoint Platform (EU)](https://eu1.anypoint.mulesoft.com/login/)
 
- 
- 
Navigate to Anypoint Exchange. ## Show me how- 
US cloud (non-EU host): [Exchange (US)](https://anypoint.mulesoft.com/exchange/)
- 
EU cloud (EU host): [Exchange (EU)](https://eu1.anypoint.mulesoft.com/exchange/)
 Your API specification appears as an API spec fragment type asset in your organization, for example: ![API Spec Fragment in Exchange](_images/des-api-frag-exchange.png)  If your API spec appears on Exchange as a REST API rather than an API spec fragment, check that the `classifier`attribute in the`exchange.json`file in the project folder in your IDE is set to one of the following, depending on the language:- 
OAS: `oas-components`
- 
RAML: `raml-fragment`
- 
JSON Schema: `json-schema`
 If the attribute is set to one of the following, the project is an API spec rather than a fragment: - 
OAS: `oas`
- 
RAML: `raml`
 
- 

## Add a Fragment from Exchange to Your Project

To add an API spec fragment from Exchange to the project directory so that you can include the fragment in your spec:

- 
Open your API spec project file, for example, `example-oas-spec`
- 
Open the Command Palette. ## Show me how- 
Use the keyboard shortcuts: - 
Mac: Cmd+Shift+p 
- 
Windows: Ctrl+Shift+p 
 
- 
- 
In the desktop IDE, select **View**>**Command Palette**.
- 
In the cloud IDE, click the ![](_images/icon-menu.png) (menu) icon, and select (menu) icon, and select**View**>**Command Palette**.
 
- 
- 
Enter `mulesoft`and select the following command:`MuleSoft: Add Fragment dependency from Exchange`command
- 
If prompted, log in to Anypoint Platform. 
- 
In the **Search for Asset**field, provide the name of the data type asset to add.To search for assets, type the search term and press Enter, for example: ![Search for fragment in Assets from Exchange dropdown](_images/des-add-frag-from-exchange.png)  
- 
Select the fragment from the **Assets From Exchange**menu.
- 
Select a version of the fragment. The status bar shows the progress. When complete, you see a message that the selected API fragment was successfully added to the project. 
- 
Verify that the fragment dependency was added by checking the `dependencies`section of the`exchange.json`file, for example:![Verify the fragment dependency in the exchange.json file](_images/des-verify-frag-from-exchange.png)  You can also see the fragment in the Explorer view under Project Dependencies, for example: ![API fragment in the Explorer view](_images/des-api-frag-dependencies.png)  The fragment files are located in your home directory on your system in the `.exchange_modules`directory, for example,`~/.exchange_modules`(Mac).

## Add an API Fragment to Your API Spec

To add an API spec fragment to a spec:

- 
Open your API spec project file, for example, `example-oas-spec`
- 
Place the cursor where you want to add the fragment. 
- 
Depending on the API spec language, select the directive to add the fragment to your specification. - 
OAS and AsyncAPI specs: Use the `$ref`directive.
- 
RAML specs: Use the `!include`directive.
 - 
OAS Example 
- 
RAML Example 
- 
AsyncAPI Example 
 This `$ref`directive adds the`AmericanFlightDataType`from`example-oas-fragment`as a data type:`schema: $ref: exchange_modules/e91cab06-650b-4634-9c6f-5bc4f4fc4d17/example-oas-fragment/1.0.0/example-oas-fragment.yaml#/components/schemas/AmericanFlightDataType`YAMLThis `!include`directive adds the`AmericanFlight`object from`AmericanFlightDataType.raml`as a data type:`types: AmericanFlight: !include exchange_modules/68ef9520-24e9-4cf2-b2f5-620025690913/training-american-flight-data-type/1.0.1/AmericanFlightDataType.raml`RAMLThis `$ref`directive adds the`AmericanFlightDataType`from`example-asyncapi-fragment`as a data type:`payload: $ref: exchange_modules/e91cab06-650b-4634-9c6f-5bc4f4fc4d17/example-asyncapi-fragment/1.0.0/example-asyncapi-fragment.json#/components/schemas/AmericanFlightDataType`YAML
- 
- 
Use [auto-complete](start-discover-ui#use-autocomplete)(or press Ctrl+Space) to display available options within each context, for example:![Add the fragment to your API spec](_images/des-add-frag-to-spec.png)  
- 
To reference an element within a component defined in the fragment file: - 
Select the fragment file name. 
- 
Enter `#/`.
- 
Press Ctrl+Space. 
- 
Select the element from the options, for example: ![Reference an element in the fragment](_images/des-api-frag-ref-element.png) 
 
- 

After adding the fragment to your spec, you can:

- 
Navigate to the dependency: Place the cursor on the fragment reference and press Command+Click. For example: ![Navigate to the fragment dependency](_images/des-api-frag-goto-dependencies.png) 
- 
View the dependency in the API Console: Place the cursor on the fragment reference and click the ![](_images/icon-api-console.png) ( (**API Console**) icon to open the fragment in the console.For more information, see [Review Your Spec in the API Console](des-create-api-specs#review-spec-console).

## Create and Add a Fragment Directly in Your Spec

To create a fragment in your project and include it in your specification:

- 
Open your API spec project file, for example, `example-oas-spec`
- 
In the Explorer view, right-click on an empty space, and create a folder for your fragments, such as `fragments`.
- 
In the `fragments`folder, create a new file, such as`my-fragment`and add your fragment code.
- 
Place the cursor where you want to add the fragment. 
- 
Depending on the API spec language, select the directive to add the fragment from the folder to your spec: - 
OAS and AsyncAPI specs: Use the `$ref`directive.
- 
RAML specs: Use the `!include`directive.
 - 
OAS Example 
- 
RAML Example 
- 
AsyncAPI Example 
 This `$ref`directive adds the`api_key`object from the`my-fragment.yaml`file:`api-key: $ref: fragments/my-fragment.yaml#/components/securitySchemes/api_key`YAMLThis `!include`directive adds the`AmericanFlightsExample.raml`example:`examples: output: !include examples/AmericanFlightExample.raml`RAMLThis `$ref`directive adds the`fragments/my-fragment`example:`payload: $ref: fragments/my-fragment`YAML
- 
- 
Use [auto-complete](start-discover-ui#use-autocomplete)(or press Ctrl+Space) to display available options within each context, for example:![Add the fragment from a folder to your API spec](_images/des-add-frag-from-folder-to-spec.png)  
- 
To reference an element within a component defined in the fragment file: - 
Select the fragment file name. 
- 
Enter `#/`.
- 
Press Ctrl+Space. 
- 
Select the element from the options, for example: ![Reference an element in the fragment](_images/des-api-frag-ref-element.png) 
 
- 

After adding the fragment to your spec, you can:

- 
Navigate to the dependency: Place the cursor on the fragment reference and press Command+Click. For example: ![Navigate to the fragment dependency](_images/des-api-frag-goto-dependencies.png) 
- 
View the dependency in the API Console: Place the cursor on the fragment reference and click the ![](_images/icon-api-console.png) ( (**API Console**) icon to open the fragment in the console.For more information, see [Review Your Spec in the API Console](des-create-api-specs#review-spec-console).

## Example OAS 3.0 (YAML) API Spec Fragment

If you created an OAS 3.0 (YAML) fragment project, you can replace the initial API fragment with following example code:

## Example OAS 3.0 (YAML) API Spec Fragment

```
openapi: "3.0.0"
info:
  version: 1.0.0
  title: ExampleComponents
paths: {}
components:
  schemas:
    AmericanFlightDataType:
      type: object
      description: American Flight Data Type
      properties:
        ID:
          type: number
        code:
          type: string
        price:
          type: number
        departureDate:
          type: string
        origin:
          type: string
        destination:
          type: string
        emptySeats:
          type: number
        plane:
          type: object
          properties:
            type:
              type: string
            totalSeats:
              type: number
      example:
        ID: 1
        code: ER38sd
        price: 400
        departureDate: 2017/07/26
        origin: CLE
        destination: SFO
        emptySeats: 0
        plane:
          type: Boeing 737
          totalSeats: 150
```
YAML## Example OAS 3.0 (YAML) API Spec

If you created an OAS 3.0 (YAML) API spec project, you can replace the initial API spec with following example code to test adding the API spec fragments:

## Example OAS 3.0 (YAML) API Spec

```
openapi: "3.0.0"
info:
  version: 1.0.0
  title: Example OAS Spec
paths:
  /flights/{ID}:
    get:
      parameters:
        -
          name: ID
          required: true
          in: path
          schema:
            type: string
      responses:
        "200":
          description: "Flight with ID"
          content:
            application/json:
              schema:
```
YAML## Example AsyncAPI Spec Avro Schema Fragment

If you created an Avro schema fragment, you can replace the initial API fragment with following example code:

## Example AsyncAPI Spec Avro Schema Fragment

```
{
  "name": "AmericanFlightDataType",
  "type": "record",
  "fields": [
    {"name": "ID", "type": "int", "example": 1},
    {"name": "code", "type": "string", "example": "ER38sd"},
    {"name": "price", "type": "int", "example": 400},
    {"name": "departureDate", "type": "string", "example": "2017/07/26"},
    {"name": "origin", "type": "string", "example": "CLE"},
    {"name": "destination", "type": "string", "example": "SFO"},
    {"name": "emptySeats", "type": "int", "example": 0},
    {
      "name": "plane",
      "type": {
        "name": "Plane",
        "type": "record",
        "fields": [
          {"name": "type", "type": "string"},
          {"name": "totalSeats", "type": "int"}
        ]
      }
    }
  ]
}
```
JSON## Example AsyncAPI Spec

If you created an AsyncAPI spec project, you can replace the initial API spec with following example code to test adding the API spec fragments:

## Example AsyncAPI Spec

```
asyncapi: 2.6.0
info:
  title: Example AsyncAPI Spec
  version: '1.0.0'
channels:
  myChannel:
    publish:
      message:
        schemaFormat: application/vnd.apache.avro;version=1.9.0
        payload:
          $ref: exchange_modules/e91cab06-650b-4634-9c6f-5bc4f4fc4d17/example-asyncapi-fragment/1.0.0/example-asyncapi-fragment.json
```
YAML## Example AsyncAPI Spec (Inline Avro)

If you created an AsyncAPI spec project, you can replace the initial API spec with following example code to test inlining the API spec fragments:

## Example AsyncAPI Spec (Inline Avro)

```
asyncapi: 2.6.0
info:
  title: Example AsyncAPI Spec (Inline Avro)
  version: '1.0.0'
channels:
  myChannel:
    publish:
      message:
        schemaFormat: 'application/vnd.apache.avro;version=1.9.0'
        payload:
          name: AmericanFlightDataType
          type: record
          fields:
            - name: ID
              type: int
              example: 1
            - name: code
              type: string
              example: ER38sd
            - name: price
              type: int
              example: 400
            - name: departureDate
              type: string
              example: 2017/07/26
            - name: origin
              type: string
              example: CLE
            - name: destination
              type: string
              example: SFO
            - name: emptySeats
              type: int
              example: 0
            - name: plane
              type:
                name: Plane
                type: record
                fields:
                  - name: type
                    type: string
                  - name: totalSeats
                    type: int
```
YAML