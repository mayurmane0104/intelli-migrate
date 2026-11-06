# NetSuite Restlet Connector 1.0 | MuleSoft Documentation

**Source:** [https://docs.mulesoft.com/netsuite-restlet-connector/latest](https://docs.mulesoft.com/netsuite-restlet-connector/latest)

---

# NetSuite Restlet Connector 1.0

Anypoint Connector for NetSuite Restlet (NetSuite Restlet Connector) synchronizes data and automates business processes between NetSuite and third-party applications, either on-premises or in the cloud. NetSuite provides cloud-based business management software that helps companies manage core business processes, ERP financials, CRM, e-commerce, inventory, and more.

NetSuite Restlet Connector provides the following features:

- 
Generation of NetSuite business objects 
- 
Different authentication levels 
- 
Error-handling support 
- 
Access to NetSuite using REST calls to RESTlets that expose APIs created with SuiteScript 

For compatibility information and fixed issues, see the NetSuite Restlet Connector Release Notes.

## Before You Begin

To use this connector, you must be familiar with:

- 
The NetSuite API 
- 
Anypoint connectors 
- 
Mule runtime engine (Mule) 
- 
Elements in a Mule flow 
- 
Global elements 
- 
How to create a Mule app using Anypoint Studio 

You must also have a NetSuite account with the Web Services features enabled.

## Connection Types

| NetSuite Restlet Connector supports OAuth 1.0 only. | 

NetSuite Restlet connections use the following authentication types:

- 
Restlet Login Authenticates to NetSuite by invoking login 
- 
Restlet Token Authenticates to NetSuite by using either a consumer and token key or secret pairs, which are established within the NetSuite environment 

For information about configuring authentication types, refer to [Configure a Global Element for the Connector](netsuite-restlet-studio-configure#configure-global-element).

## See Also

- 
[Use Exchange to Discover Connectors, Templates, and Examples](../../connectors/introduction/intro-use-exchange)
- 
[Salesforce Help](https://help.salesforce.com)