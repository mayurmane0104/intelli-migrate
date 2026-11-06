# SAP Connector 5.9 | MuleSoft Documentation

**Source:** [https://docs.mulesoft.com/sap-connector/latest](https://docs.mulesoft.com/sap-connector/latest)

---

# SAP Connector 5.9

Anypoint Connector for SAP (SAP Connector) enables integration of data between external systems and SAP systems based on SAP NetWeaver.

This connector requires a separate license. Contact MuleSoft to evaluate or use this connector in production.

Mule runtime engine (Mule) supports SAP integration through Anypoint Connector for SAP, which leverages the SAP Java Connector (JCo) libraries. SAP JCo facilitates communication between an SAP backend system and a Java application. It allows Java programs to connect to SAP systems and invoke Remote Function Modules. It also allows the parsing of IDocs (SAP Intermediate Documents), among other object types. The SAP configuration supports both inbound and outbound communications.

The SAP JCo libraries enable Mule apps to:

- 
Execute BAPI functions over the following types of RFC protocols: - 
Synchronous Remote Function Call RFC (sRFC) 
- 
Asynchronous Remote Function Call RFC (aRFC) 
 
- 
- 
Act as a JCo server to be called as a BAPI over sRFC and aRFC 
- 
Send IDocs over tRFC and qRFC 
- 
Receive IDocs over tRFC and qRFC 
- 
Transform SAP objects (JCo function for BAPI and IDocs) to and from XML 

See [SAP Terminology](sap-connector-terminology) to understand SAP acronyms.

## Before You Begin

To use this connector, you must be familiar with:

- 
SAP Connector’s API 
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
Credentials to access the SAP target resource 
- 
SAP libraries for IDoc, JCO, and JCO Native To download these libraries, go to the SAP website. Studio 7 can use the library formats directly without conversion. To see which libraries are compatible with the connector, see the [SAP Connector Release Notes](../../release-notes/connector/sap-connector-release-notes-mule-4).
- 
A service user with the roles or profiles that allow you to use the required RFCs, BAPIs, and IDocs 
- 
A working knowledge of the SAP business context and, in particular, the SAP R/3 Business Suite 
- 
A basic understanding of the SAP NetWeaver Platform from an administration point of view 
- 
Knowledge of the ABAP language 
- 
An SAP ID to download the required SAP libraries 
- 
Use of the RFC protocol to connect to NetWeaver Application Servers (NWAS) 
 [ECC](https://www.cipherbsc.com/sap-erp-central-component-erp-ecc/)and[CRM](https://help.sap.com/docs/r/p/SAP_CUSTOMER_RELATIONSHIP_MANAGEMENT)run on top of NWAS, as other SAP solutions do, so any customer using the connector can access those systems.
- 
Knowledge of how to create a Mule app using Anypoint Studio 

## Common Use Cases for the Connector

Common use cases for SAP Connector include:

- 
**Unified View of Enterprise Resources**Enable real-time integration of digital information across your business from financial accounting, materials management, sales and distribution, and customer service to make data-driven decisions that optimize core business processes. 
- 
**Data Synchronization**Sync SAP data with your business applications, such as Salesforce, Workday, and Marketo. For example, you can migrate a large set of accounts from SAP to Salesforce or broadcast changes in organizations from SAP to Workday in real-time. 
- 
**Sales Order Automation**Automate sales order processing between SAP ERP and a CRM, such as Salesforce. 
- 
**BAPI Support**Discover BAPIs, query BAPI/RFM enabled function modules, or execute BAPI functions. 
- 
**IDoc Integration**Send and receive IDocs from SAP, import IDocs, or transform SAP objects to and from XML. 

For examples of these use cases, refer to [SAP Connector Examples](sap-connector-examples).

## Authentication Types

SAP Connector connections use the following authentication types:

- 
Certificate Connection provider that relies on an X509 certificate to authenticate the user 
- 
Kerberos Connection provider that implements the Kerberos protocol to authenticate and authorize the user 
- 
Simple Connection Provider Connection provider that connects using a username and password 

## Exchange Templates and Examples

[Anypoint Exchange](https://www.mulesoft.com/exchange/) provides templates that you can use as starting points for your apps and examples that illustrate a complete solution:

- 
**General:**[Account System API - SAP Implementation Template](https://www.mulesoft.com/exchange/org.mule.templates/template-apiled-system-account-sap/),[Salesforce to Salesforce, Workday, SAP, and Database Account Broadcast](https://www.mulesoft.com/exchange/org.mule.templates/template-sfdc2sfdc.wday.sap.db-account-broadcast/)
- 
**Salesforce and SAP:**[Account Aggregation](https://www.mulesoft.com/exchange/org.mule.templates/template-sap2sfdc-account-aggregation/),[Account Customer Bidirectional Sync](https://www.mulesoft.com/exchange/org.mule.templates/template-sap2sfdc-customer-bidirectional-sync/),[Opportunity Aggregation](https://www.mulesoft.com/exchange/org.mule.templates/template-sfdc2sap-opportunity-aggregation/),[Product Aggregation](https://www.mulesoft.com/exchange/org.mule.templates/template-sfdc2sap-product-aggregation/),[Product Bidirectional Sync](https://www.mulesoft.com/exchange/org.mule.templates/template-sfdc2sap-product-bidirectional-sync/)
- 
**Salesforce to SAP:**[Account Broadcast](https://www.mulesoft.com/exchange/org.mule.templates/template-sfdc2sap-account-broadcast/),[Account Migration](https://www.mulesoft.com/exchange/org.mule.templates/template-sfdc2sap-account-migration/),[Opportunity Broadcast](https://www.mulesoft.com/exchange/org.mule.templates/template-sfdc2sap-opportunity-broadcast/),[Opportunity Migration](https://www.mulesoft.com/exchange/org.mule.templates/template-sfdc2sap-opportunity-migration/),[Product Broadcast](https://www.mulesoft.com/exchange/org.mule.templates/template-sfdc2sap-product-broadcast/)
- 
**SAP to Salesforce:**[Contact Broadcast](https://www.mulesoft.com/exchange/org.mule.templates/template-sap2sfdc-contact-broadcast/),[Contact Migration](https://www.mulesoft.com/exchange/org.mule.templates/template-sap2sfdc-contact-migration/),[Customer Broadcast](https://www.mulesoft.com/exchange/org.mule.templates/template-sap2sfdc-customer-broadcast/),[Customer Migration](https://www.mulesoft.com/exchange/org.mule.templates/template-sap2sfdc-customer-migration/),[Product Material Broadcast](https://www.mulesoft.com/exchange/org.mule.templates/template-sap2sfdc-product-broadcast/),[Product Material Migration](https://www.mulesoft.com/exchange/org.mule.templates/template-sap2sfdc-material-migration/)
- 
**SAP to Workday:**[Employee Migration](https://www.mulesoft.com/exchange/org.mule.templates/template-sap2wday-employee-migration/),[Organization Broadcast](https://www.mulesoft.com/exchange/org.mule.templates/template-sap2wday-organization-broadcast/),[Organization Migration](https://www.mulesoft.com/exchange/org.mule.templates/template-sap2wday-organization-migration/)
- 
**Workday and SAP:**[Organization Aggregation](https://www.mulesoft.com/exchange/org.mule.templates/template-wday2sap-organization-aggregation/),[Worker (Employee) Aggregation](https://www.mulesoft.com/exchange/org.mule.templates/template-wday2sap-worker-aggregation/)
- 
**Workday to SAP:**[Worker (Employee) Migration](https://www.mulesoft.com/exchange/org.mule.templates/template-wday2sap-worker2employee-migration/),[Worker Broadcast](https://www.mulesoft.com/exchange/org.mule.templates/template-wday2sap-worker-broadcast/)

## Next

After you complete the prerequisites and experimented with templates and examples, you are ready to create an app with
[Anypoint Studio](sap-connector-studio).

## See Also

- 
[SAP Connector in Anypoint Exchange](https://www.mulesoft.com/exchange/com.mulesoft.connectors/mule-sap-connector/)
- 
[Salesforce Help](https://help.salesforce.com)