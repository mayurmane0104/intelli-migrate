# Web Service Consumer Connector 2.2 | MuleSoft Documentation

**Source:** [https://docs.mulesoft.com/web-service-consumer-connector/latest](https://docs.mulesoft.com/web-service-consumer-connector/latest)

---

# Web Service Consumer Connector 2.2

Anypoint Connector for Web Service Consumer (Web Service Consumer Connector) consumes a SOAP web service from a Mule app to acquire data from an external source. In many cases, you can use Anypoint Connector for Workday (Workday Connector) or Anypoint Connector for ServiceNow (ServiceNow Connector) to connect to a service provider, however, when no connector is available for a specific web service, the easiest way to consume the service is to use the Web Service Consumer Connector.

The main features of the connector include:

- 
Ability to consume DOC literal web services 
- 
Use of SOAP multipart messages 
- 
Use of SOAP headers 
- 
Support for a DataSense for SOAP headers, SOAP body, and attachments 
- 
Use of embedded DataWeave transformations inside the operation 
- 
Support for a unified experience for SOAP with attachments and MTOM handling 
- 
Custom HTTP configuration as a transport 
- 
Support for Web Service Security (WS Security) 

| Web Service Consumer Connector doesn’t support RPC WSDLs (Remote procedure call Web Service Descripting Language). | 

## Before You Begin

To use this connector, you must be familiar with:

- 
SOAP and WSDLs 
- 
Anypoint Connectors 
- 
Mule runtime engine (Mule) 
- 
Elements in a Mule flow 
- 
Global elements 
- 
DataWeave 
- 
Creating a Mule app using Anypoint Studio 

Before creating an app, you must have access to Anypoint Studio.

## Next Step

After you complete the prerequisites, you are ready to create an app and configure the connector using [Anypoint Studio](web-service-consumer-studio).

## See Also

- 
[Use Exchange to Discover Connectors, Templates, and Examples](../../connectors/introduction/intro-use-exchange)
- 
[Web Service Consumer in Exchange](https://anypoint.mulesoft.com/exchange/org.mule.connectors/mule-wsc-connector/)
- 
[Salesforce Help](https://help.salesforce.com)