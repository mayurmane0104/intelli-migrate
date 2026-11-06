# Creating and Importing AsyncAPI Specifications | MuleSoft Documentation

**Source:** [https://docs.mulesoft.com/anypoint-code-builder/des-create-asyncapi-api-specs](https://docs.mulesoft.com/anypoint-code-builder/des-create-asyncapi-api-specs)

---

![Anypoint Code Builder icon highlighted in the activity bar](_images/anypoint-code-builder-view.png) 

# Creating and Importing AsyncAPI Specifications

Use Anypoint Code Builder to design, import, govern, and test AsyncAPI specs before publishing to Anypoint Exchange:

- 
Create and design an AsyncAPI spec project in Anypoint Code Builder from the IDE or by importing the spec from MuleSoft VCS: 

Use the [ asyncapi-example](#example-asyncapi-api-spec) API spec to explore the functionality of Anypoint Code Builder.

## Before You Begin

- 
Understand the basics of designing AsyncAPI specs. 
- 
Have some familiarity with [business groups](../access-management/business-groups).When you publish your API spec to Exchange from Anypoint Code Builder, the IDE requests the name of the business group. See [Anypoint Platform Business Groups](../access-management/business-groups).

## Create and Design a New AsyncAPI Specification Project

To create and design an AsyncAPI spec project in Anypoint Code Builder:

- 
In the activity bar of the IDE, click the ![](_images/icon-ms-logo.png) ( (**Anypoint Code Builder**) icon.![Anypoint Code Builder icon highlighted in the activity bar](_images/anypoint-code-builder-view.png)  
- 
From **Create**, click**Design an API**:![*Design an API* link highlighted in the *Create* section](_images/design-api-1.png)  
- 
Complete the **API Specification**form:Field Name Field Value **Project Name**Unique name for your project. This name is used as the AsyncAPI spec title in Exchange, the name of the spec file, and the name of the project’s root directory. For example, if the project name is *AsyncAPI Example*, the spec file name is`asyncapi-example`.To reuse an existing project name, you must delete the project that is already using the name first. See [Deleting API Specs and Fragments](des-delete-api-projects).**Project Location**Your home directory or another directory you create. Don’t create the project within another project directory. **API Type**The type of API spec to create. Available options are **REST API**and**AsyncAPI**.Select **AsyncAPI**to use the[example](#example-asyncapi-api-spec)in this procedure.**API Specification Language**Select **AsyncAPI 2.6 (YAML)**to use the[example](#example-asyncapi-api-spec)in this procedure.
- 
Click **Create Project**.If prompted, trust the authors of the files in the folder. When the project is ready for editing, the API project opens the spec in the Editor view, for example, this AsyncAPI 2.6 (YAML) spec: ![New AsyncAPI 2.6 (YAML) API project](_images/des-asyncapi-create.png)  
- 
Continue designing your API spec. As you enter elements, use [auto-complete](start-discover-ui#auto-complete)(Ctrl+Space) to display available options within the context.

## Import an AsyncAPI Specification from MuleSoft VCS

Import an AsyncAPI spec from MuleSoft VCS and use Git or another source-control management system compatible with VS Code in the desktop or cloud IDE to keep your project in sync. For more information, see [Source Control for API Design Projects](des-designing-api-specs#anypoint-scm).

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
Provide the following command: `MuleSoft: Import API Specification from MuleSoft VCS`command
- 
If prompted, log in to Anypoint Platform through the IDE. 
- 
Complete the import process: - 
Select your business group from the **Select a Business Group**popup.
- 
Search for the API spec in the **APIs from MuleSoft VCS**field.
- 
Navigate to or create a folder for the spec, and click **Select target folder**.If you receive an error that the import failed ( **Importing project**), check your target folder for a project with the same name. To address a duplicate naming issue before importing, you can import the design project to a different target folder or delete the project from your IDE (see*a_project_name*has failed[Deleting API Specs and Fragments](des-delete-api-projects)).
 
- 
- 
Edit or continue designing your spec, as needed. As you enter elements, use [auto-complete](start-discover-ui#auto-complete)(Ctrl+Space) to display available options within the context.
- 
Optionally, sync your changes by using MuleSoft VCS. This feature is available only for API projects that you import from MuleSoft VCS. You can also store your work in another SCM. For SCM options, see [Controlling Source Files](start-scm).

## Track Progress in the Output Panel

To track the progress of internal processing as you design your API:

- 
Open the Output panel. ## Show me how- 
Use the keyboard shortcuts: - 
Mac: Cmd+Shift+u 
- 
Windows: Ctrl+Shift+u 
 
- 
- 
In the desktop IDE, select **View**>**Output**.
- 
In the cloud IDE, click the ![](_images/icon-menu.png) (menu) icon, and select (menu) icon, and select**View**>**Output**.
 
- 
- 
Select **Mule DX Server**from the dropdown:![Mule DX Server in the output pane](_images/des-output-panel.png)  

## Review Your Spec in the API Console

To display your spec in the console:

- 
Click your spec file in the editor. 
- 
Click the ![](_images/icon-api-console.png) ( (**API Console**) icon.Alternatively, you can provide the command `MuleSoft: API Console`from the[Command Palette](start-use-command-palette).
- 
Wait for the channels to render in the API Console. The API Console show the channels for the spec, for example: ![AsyncAPI spec in the API Console](_images/des-asyncapi-api-console.png)  **1**Click a channel to view details. **2**Display the console menu. 
- 
Click channels in the console or select items from the menu to view different parts of your spec. For example, click **PUBLISH**:![API Console with Publish details](_images/des-asyncapi-api-console-detail.png)  

## Example AsyncAPI (YAML) API Specification

If you created an AsyncAPI 2.6 (YAML) project, you can replace the initial spec with this example code:

## Example AsyncAPI 2.6 (YAML) Specification

`asyncapi: '2.6.0' `**(1)**
info:
  title: Orders AsyncAPI
  version: '1.0.0'
  description: Orders API
  license:
    name: Anypoint MQ
    url: https://license.com
  contact:
    name: Max Muley
    email: max@salesforce.com
    url: http://salesforce.com
defaultContentType: application/json
tags:
  - name: Orders API
    description: API for orders
servers: **(2)**
  AMQ-prod:
    url: https:://your_MQ_server_URL_here
    protocol: anypointmq
    protocolVersion: v1
    description: Anypoint MQ broker
  kafka-prod:
    url: your_kafka_URL_here
    protocol: kafka
    description: kafka broker
  sfpubsub-prod:
      protocol: salesforcepubsub
      protocolVersion: v1
      url: api.pubsub.salesforce.com
      description: Salesforce pub sub for Platform events production
  solace-server:
    protocol: solace
    variables:
      port:
        enum:
        - '1000'
    bindings:
      solace:
        msgVpn: your_solace_vpn_here
        bindingVersion: 0.4.0
    protocolVersion: 1.0.0
    url: mySolaceURL
channels: **(3)**
  order-placed:
    description: new orders channel
    servers:
      - AMQ-prod
    publish:
      operationId: listen-order-placed
      description: listen for new order events
      summary: Order Placed Event
      message:
        $ref: '#/components/messages/OrderPlaced'
    subscribe:
      operationId: publish-order-placed
      description: publish new order events
      summary: Order Placed Event
      message:
        $ref: '#/components/messages/OrderPlaced'
  order-updated:
    description: updated orders channel
    servers:
      - solace-server
    publish:
      operationId: listen-order-updated
      description: listen for updated order events
      summary: Order updated Event
      bindings:
        solace:
          bindingVersion: 0.3.0
          destinations:
          - destinationType: queue
            queue:
              name: listen-order-updated
              topicSubscriptions:
              - acmeretail/onlineservices/order/updated/v1/*/*
              - acmeretail/onlineservices/order/updated/v2/*/*
      message:
        $ref: '#/components/messages/OrderUpdated'
    subscribe:
      operationId: publish-order-updated
      description: publish updated order events
      summary: Order updated Event
      bindings:
        solace:
          bindingVersion: 0.3.0
          destinations:
          - destinationType: queue
            queue:
              name: C360.CUSTOMERS
              topicSubscriptions:
              - acmeretail/onlineservices/order/updated/v1/*/*
              - acmeretail/onlineservices/order/updated/v2/*/*
      message:
        $ref: '#/components/messages/OrderUpdated'
  order-cancelled:
    description: orders cancelled channel
    servers:
      - AMQ-prod
    publish:
      operationId: listen-order-cancellations
      description: listen for order cancellation events
      summary: Order Cancelled Event
      message:
        $ref: '#/components/messages/OrderCancelled'
    subscribe:
      operationId: publish-order-cancellations
      description: publish order cancellation events
      summary: Order Cancelled Event
      message:
        $ref: '#/components/messages/OrderCancelled'
  order-confirmed:
    description: orders confirmed channel
    servers:
      - sfpubsub-prod
    publish:
      operationId: listen-order-confirmations
      description: listen for order confirmation events
      summary: Order Confirmed Event
      message:
        $ref: '#/components/messages/OrderConfirmedSub'
    subscribe:
      operationId: publish-order-confirmations
      description: publish order confirmation events
      summary: Order Confirmed Event
      message:
        $ref: '#/components/messages/OrderConfirmedPub'
  order-backordered:
    servers:
      - kafka-prod
    description: orders backordered channel
    publish:
      operationId: listen-order-backordered
      description: listen for backorder events
      summary: Backorder Event
      message:
        $ref: '#/components/messages/BackOrder'
    subscribe:
      operationId: publish-order-backordered
      description: publish backorder events
      summary: Backorder Event
      message:
        $ref: '#/components/messages/BackOrder'
components: **(4)**
  messages:
    OrderPlaced:
      payload:
        type: object
        properties:
          orderId:
            type: string
          customerName:
            type: string
          email:
            type: string
          items:
            type: array
            items:
              type: object
              properties:
                productId:
                  type: string
                productName:
                  type: string
                quantity:
                  type: integer
                price:
                  type: number
              required: [productId, productName, quantity, price]
              additionalProperties: false
        required: [orderId, customerName, email, items]
        additionalProperties: false
    OrderConfirmedPub:
      summary: order message pub
      contentType: application/json
      payload:
        type: array
        orderconfirmation:
          type: object
          properties:
            orderId__c:
              type: string
            email__c:
              type: string
            required: [orderId, email]
            additionalProperties: false
    OrderConfirmedSub:
      summary: order message sub
      contentType: application/json
      payload:
        type: object
        properties:
          event:
            type: object
            properties:
              orderId__c:
                type: string
              email__c:
                type: string
        required: [orderId, email]
        additionalProperties: false
    OrderCancelled:
      payload:
        type: object
        properties:
          orderId:
            type: string
          email:
            type: string
          reason:
            type: string
        required: [orderId, email, reason]
        additionalProperties: false
    BackOrder:
      payload:
        type: object
        properties:
          orderId:
            type: string
          email:
            type: string
        required: [orderId, email]
        additionalProperties: false
    OrderUpdated:
      contentType: application/json
      description: Shows changes to customer information including name, address and
        loyalty status
      payload:
        "$ref": "#/components/schemas/Order_JSON"
      schemaFormat: application/vnd.aai.asyncapi+json;version=2.0.0
      x-ep-application-domain-id: p4oo2ehrcpf
      x-ep-application-domain-name: OnlineServices
      x-ep-custom-attr-confidential: 'true'
      x-ep-event-id: 66gdcid5pht
      x-ep-event-name: Customer Created
      x-ep-event-state-id: '2'
      x-ep-event-state-name: RELEASED
      x-ep-event-version: 2.0.2
      x-ep-event-version-displayname: ''
      x-ep-event-version-id: 29btjydowi0
      x-ep-shared: 'true'
  schemas:
    Order_JSON:
      "$schema": http://json-schema.org/draft-07/schema#
      properties:
        customer_id:
          description: The unique identifier of the customer
          type: string
        insight_description:
          description: A brief description of the insight
          type: string
        insight_type:
          description: The type of insight (e.g., demographic, behavioral, transactional)
          type: string
        insight_value:
          description: The value or result of the insight
          type: string
        timestamp:
          description: The timestamp when the insight was generated
          format: date-time
          type: string
      required:
      - customer_id
      - insight_type
      - insight_description
      - insight_value
      - timestamp
      title: CustomerInsight
      type: object
      x-ep-application-domain-id: a3hbbd7unz2
      x-ep-application-domain-name: Customer360
      x-ep-schema-id: 6dqkacw0k70
      x-ep-schema-name: Customer Insight
      x-ep-schema-state-id: '1'
      x-ep-schema-state-name: DRAFT
      x-ep-schema-version: 0.1.0
      x-ep-schema-version-displayname: ''
      x-ep-schema-version-id: u15ylfss2qx
      x-ep-shared: 'false'YAML| 1 | AsyncAPI Identifies the API model as AsyncAPI and specifies the title and version of the API spec | 
| 2 | Servers Defines message brokers that determine the connectors to use (indirectly) when publishing events or subscribing to events through operations in the AsyncAPI module: 
 | 
| 3 | Channels Defines the bindings: 
 | 
| 4 | Components Defines the structure of messages for the different types of orders, which include  |