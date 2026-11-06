# Salesforce Connector 11.4 | MuleSoft Documentation

**Source:** [https://docs.mulesoft.com/salesforce-connector/latest](https://docs.mulesoft.com/salesforce-connector/latest)

---

# Salesforce Connector 11.4

Anypoint Connector for Salesforce (Salesforce Connector) enables you to create apps that react to Salesforce events such as adding, changing, or deleting objects, topics, documents, and channels.

Salesforce Connector enables you to connect to the Salesforce APIs. This connector exposes methods for accessing Salesforce, including working with the [Salesforce Apex classes](https://developer.salesforce.com/docs/atlas.en-us.apexcode.meta/apexcode/apex_dev_process_chapter.htm).

This connector works with the Salesforce SOAP API, REST API, Bulk API, and Streaming API, depending on the operation you configure. Each API call uses a request/response pattern over an HTTPS connection. All required request headers, error handling, and HTTPS connection configurations are built into the connector.

For compatibility information and fixed issues, see the Salesforce Connector release notes.

## Before You Begin

To use this connector, you must be familiar with:

- 
The Salesforce SOAP, REST, Bulk, and Streaming APIs 
- 
Anypoint Connectors 
- 
Mule runtime engine (Mule) 
- 
Elements and global elements in a Mule flow 
- 
Creating a Mule app using Anypoint Studio or Anypoint Code Builder 

Before creating an app, you must have:

- 
Access to the Salesforce target resource, which requires a [Salesforce developer account](https://developer.salesforce.com)and[Salesforce security token](https://help.salesforce.com/s/articleView?language=en_US&id=user_security_token.htm).You can receive a new security token by email if you run **Reset Security Token**through**My Personal Information**from the Salesforce Setup pages.
- 
A consumer key and secret (available in your Salesforce developer account) 
- 
The namespace and schema location, if you are using OAuth authentication. If you plan to create the XML for your Mule app, include the correct namespace and schema location in your XML file. Studio adds this information to the XML file automatically when you add Salesforce Connector to a flow in a Mule app. 

## Limitations

- 
Salesforce Connector does not expose all possible operations of the Salesforce APIs. 
- 
Salesforce Connector does not provide access to the Chatter API or Tooling API. 

## Audience

- 
New users Read this document and create your Mule app in [Anypoint Studio](salesforce-connector-studio).The [Additional Configuration Information](salesforce-connector-config-topics)topic helps you extend your understanding of the connector.
- 
Advanced users Read [XML and Maven Support](salesforce-connector-xml-maven), the[Additional Configuration Information](salesforce-connector-config-topics)topic, and[Examples](salesforce-connector-examples).

## Common Use Cases for the Connector

Common use cases for Salesforce Connector include:

- 
**ERP Integration**Give your sales team access to all relevant customer data from one system via real-time synchronization of data between Salesforce and your ERP & finance applications. For example, use Anypoint Connector for SAP (SAP Connector) to sync data between Salesforce and SAP and Anypoint Connector for NetSuite (NetSuite Connector) to sync data between Salesforce and NetSuite. 
- 
**Data Aggregation**Collect data from multiple Salesforce orgs, other CRMs, ERP systems, and databases into one Salesforce instance or use that information to generate reports. 
- 
**Legacy Modernization**Easily manage data post-acquisition, move off of a legacy CRM system, or migrate ERP data into Salesforce by automatically moving your data into Salesforce. 
- 
**Customer Experience**Deliver a consistent, connected customer experience across channels, increase customer satisfaction, and drive revenue growth by integrating Salesforce to applications such as ServiceNow, Marketo, and others. 

For examples of these use cases, refer to [Salesforce Connector Examples](salesforce-connector-examples).

## Authentication Types

Salesforce Connector connections use the following authentication types:

- 
Basic authentication Uses a username and password for authentication 
- 
OAuth 2.0 Delegates user authentication to the service hosting the user account 
- 
OAuth JWT Uses OAuth 2.0 with a JSON Web token (JWT) request for user authentication 
- 
OAuth Client Credentials Uses a client ID and client secret for authentication 
- 
OAuth SAML Uses OAuth 2.0 with a signed SAML 2.0 assertion to request an access token 
- 
OAuth Username password Uses OAuth 2.0 with a user and password for authentication 

For information about configuring these authentication types, see [Using Anypoint Studio to Configure Salesforce Connector](salesforce-connector-studio).

## Salesforce Connector Configurations and Examples

The following table provides links to specific Salesforce Connector information:

| Subject | Description | 
|---|---|
| Accept and transform data from Salesforce example | |
| Configure for APEX SOAP API and APEX REST API | |
| List of Salesforce APIs that this connector can access | |
| Process order and integration patterns | |
| Batch data using the Salesforce Bulk API | |
| Specify a lead ID using DataWeave | |
| Create and update parent and child relationships example | |
| Simplify Salesforce Connector development with a template or example | |
| Subscribe to a Salesforce topic | |
| Subscribe to a Salesforce streaming channel | |
| Replay events from a Topic | |
| Replay Events from a Salesforce streaming channel | |
| Get custom event notifications over a streaming channel | |
| Push Events to a Streaming Channel | |
| Object Store usage and limitations | 

## Develop an Application

To build an app, perform the following tasks:

- 
Configure the connector. 
- 
Test the connection. 
- 
Build the rest of your flow. 
- 
Add and configure DataWeave. 

When developing an app, Salesforce Connector provides these integration patterns you can use with the Salesforce APIs:

- 
Batch Data Synchronization An external system accesses, changes, deletes, or adds data in Salesforce in batches, and vice versa (Salesforce to external system). 
- 
Remote Call-In An external system accesses, changes, deletes, or adds data in Salesforce, and vice versa (Salesforce to external system). 
- 
Fire and Forget Remote Process Invocation Salesforce initiates a process in a third-party system and receives an acknowledgment that the process has started. The third-party system continues processing independent of Salesforce. 
- 
Request-Reply Remote Process Invocation Salesforce initiates a process in a remote system, waits for the remote system to finish processing, and accepts control returned from the remote system. 
- 
User Interface Update Based on Data Changes The Salesforce UI updates in response to a change in a third-party system. 

## Salesforce APIs

Salesforce Connector works with the Salesforce Apex SOAP API, Apex REST API, Bulk API, Metadata API, and Streaming API, but does not provide access to the Chatter API or the Tooling API. Each API call uses a request/response pattern over an HTTPS connection. All required request headers, error handling, and HTTPS connection configurations are built into the connector.

- 
Apex SOAP API Salesforce [Apex SOAP API](https://developer.salesforce.com/docs/atlas.en-us.apexcode.meta/apexcode/apex_api.htm?search_text=soap)exposes Apex class methods as custom SOAP web service calls. This allows an external app to invoke an Apex web service to perform an action in Salesforce.
- 
Apex REST API Salesforce [Apex REST API](https://developer.salesforce.com/docs/atlas.en-us.apexcode.meta/apexcode/apex_rest.htm)creates your own REST-based web services using Apex. This API has all of the advantages of the REST architecture, while adding the ability to define custom logic and including automatic argument or object mapping.
- 
Bulk API Salesforce [Bulk API](https://developer.salesforce.com/docs/atlas.en-us.api_asynch.meta/api_asynch/asynch_api_intro.htm)quickly and securely loads batches of your organization’s data into Salesforce. See also[Load Data in Batches](salesforce-connector-config-topics#batchdata).
- 
Metadata API Salesforce [Metadata API](https://developer.salesforce.com/docs/atlas.en-us.api_meta.meta/api_meta/meta_intro.htm)manages customizations and build tools that work with the metadata model, not the data itself.
- 
SOAP API Salesforce [SOAP API](https://developer.salesforce.com/docs/atlas.en-us.api.meta/api/sforce_api_quickstart_intro.htm)provides secure access to your organization’s information on Salesforce. Most of the operations that Salesforce Connector performs map to this API.All the Salesforce operations performed through the SOAP API have an optional parameter called `Headers`that can take any of the[Salesforce SOAP headers](https://developer.salesforce.com/docs/atlas.en-us.api.meta/api/soap_headers.htm).
- 
Streaming API Salesforce [Streaming API](https://developer.salesforce.com/docs/atlas.en-us.api_streaming.meta/api_streaming/intro_stream.htm)securely receives notifications about changes to your organization’s information in Salesforce. See[Create a Streaming Channel to Receive Data from Salesforce](salesforce-connector-processing-events#createchannel)for more information about the use of the Streaming API.

## Anypoint Exchange Templates and Examples

[Anypoint Exchange](https://www.mulesoft.com/exchange/) provides templates
you can use as a starting point for your app, as well as examples that illustrate a complete solution.

### Salesforce Connector Templates in Exchange

[Anypoint Exchange templates](https://www.mulesoft.com/exchange/?search=salesforce&type=template) provide starting points for Studio projects such as:

- 
Account Broadcast template [Salesforce to Salesforce, Workday, SAP, and database account broadcast](https://www.mulesoft.com/exchange/org.mule.templates/template-sfdc2sfdc.wday.sap.db-account-broadcast/)
- 
Aggregation [contacts](https://www.mulesoft.com/exchange/org.mule.templates/template-sfdc2sfdc-contact-aggregation/),[opportunity](https://www.mulesoft.com/exchange/org.mule.templates/template-sfdc2sfdc-opportunity-aggregation/),[user](https://www.mulesoft.com/exchange/org.mule.templates/template-sfdc2sfdc-user-aggregation/)
- 
Bidirectional Sync template - 
Between Salesforce organizations [accounts](https://www.mulesoft.com/exchange/org.mule.templates/template-sfdc2sfdc-account-bidirectional-sync/),[contacts](https://www.mulesoft.com/exchange/org.mule.templates/template-sfdc2sfdc-contact-bidirectional-sync/),[custom objects](https://www.mulesoft.com/exchange/org.mule.templates/template-sfdc2sfdc-casecustomobject-bidirectional-sync/),[opportunities](https://www.mulesoft.com/exchange/org.mule.templates/template-sfdc2sfdc-opportunity-bidirectional-sync/),[users](https://www.mulesoft.com/exchange/org.mule.templates/template-sfdc2sfdc-user-bidirectional-sync/)
- 
Other sources [database](https://www.mulesoft.com/exchange/org.mule.templates/template-sfdc2db-account-bidirectional-sync/),[Microsoft Dynamics CRM](https://www.mulesoft.com/exchange/org.mule.templates/template-sfdc2msdyn-account-bidirectional-sync/),[Siebel](https://www.mulesoft.com/exchange/org.mule.templates/template-sfdc2sieb-account-bidirectional-sync/)
 
- 
- 
Migration [accounts](https://www.mulesoft.com/exchange/org.mule.templates/template-sfdc2sap-account-migration/),[contacts](https://www.mulesoft.com/exchange/org.mule.templates/template-sap2sfdc-contact-migration/),[opportunities](https://www.mulesoft.com/exchange/org.mule.templates/template-sfdc2sfdc-opportunity-migration/)

### Salesforce Connector Examples in Exchange

[Anypoint Exchange examples](https://www.mulesoft.com/exchange/?search=salesforce&type=example) enable you to create complete Studio projects such as:

- 
Batch processing [database](https://www.mulesoft.com/exchange/org.mule.examples/salesforce-to-MySQL-DB-using-Batch-Processing/)and[import leads](https://www.mulesoft.com/exchange/org.mule.examples/import-leads-into-salesforce/)
- 
[Contacts](https://www.mulesoft.com/exchange/org.mule.examples/cache-scope-with-salesforce-contacts/)
- 
[Data retrieval](https://www.mulesoft.com/exchange/org.mule.examples/salesforce-data-retrieval/)
- 
[DataWeave](https://www.mulesoft.com/exchange/org.mule.examples/dataweave-with-flowreflookup/)

## Next Steps

After you complete the prerequisites and experiment with templates and examples, you are ready to create an app with [Anypoint Studio](salesforce-connector-studio).

## See Also

- 
[Use Exchange to Discover Connectors, Templates, and Examples](../../connectors/introduction/intro-use-exchange)
- 
[Salesforce APIs: What they are and when to use them](https://developer.salesforce.com/)
- 
[Which Salesforce API should I use?](https://help.salesforce.com/s/articleView?id=integrate_what_is_api.htm&language=en_US&type=5)
- 
[Salesforce Connector in Exchange](https://www.mulesoft.com/exchange/com.mulesoft.connectors/mule-salesforce-connector/)
- 
[Salesforce Help](https://help.salesforce.com)