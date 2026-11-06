# Microsoft Dynamics GP Connector | MuleSoft Documentation

**Source:** [https://docs.mulesoft.com/microsoft-dynamics-gp-connector/latest](https://docs.mulesoft.com/microsoft-dynamics-gp-connector/latest)

---

```
<dependency>
  <groupId>com.mulesoft.connectors</groupId>
  <artifactId>mule-microsoft-dynamics-gp-connector</artifactId>
  <version>x.x.x</version>
  <classifier>mule-plugin</classifier>
</dependency>
```
xml# Microsoft Dynamics GP Connector

Microsoft Dynamics GP Connector v2.1

Anypoint Connector for Microsoft Dynamics GP enables Mule applications to interact with the Microsoft Dynamics Great Plains (GP) Web Services.

Release Notes: [Microsoft Dynamics GP Connector Release Notes](../../release-notes/connector/microsoft-dynamics-gp-connector-release-notes-mule-4)

Exchange: [Microsoft Dynamics GP Connector](https://www.mulesoft.com/exchange/com.mulesoft.connectors/mule-microsoft-dynamics-gp-connector/)

## Before You Begin

To use this information, you should be familiar with Microsoft Dynamics GP, Mule runtime engine (Mule), Anypoint Connectors, Anypoint Studio, Mule concepts, elements in a Mule flow, and Global Elements.

To use this connector, you need:

- 
Microsoft Dynamics GP instance. 
- 
Valid credentials for a Kerberos connection. 
- 
MuleSoft Enterprise License. 

## POM File Information

Replace `x.x.x` with the version that corresponds to the connector you are using.

To obtain the most up-to-date `pom.xml` file information, access the connector in [Anypoint Exchange](https://www.mulesoft.com/exchange/) and click **Dependency Snippets**.

## Add the Connector to a Studio Project

Anypoint Studio provides two ways to add the connector to your Studio project: from the Exchange button in the Studio taskbar or from the Mule Palette view.

### Add the Connector Using Exchange

- 
In Studio, create a Mule project. 
- 
Click the Exchange icon **(X)**in the upper-left of the Studio task bar.
- 
In Exchange, click **Login**and supply your Anypoint Platform username and password.
- 
In Exchange, search for "gp". 
- 
Select the connector and click **Add to project**.
- 
Follow the prompts to install the connector. 

### Add the Connector in Studio

- 
In Studio, create a Mule project. 
- 
In the Mule Palette view, click **(X) Search in Exchange**.
- 
In **Add Modules to Project**, type "gp" in the search field.
- 
Click this connector’s name in **Available modules**.
- 
Click **Add**.
- 
Click **Finish**.

### Configure in Studio

- 
Drag the connector operation to the Studio canvas. 
- 
Configure the global element for the connector. ![Microsoft Dynamics GP global elements properties config window](_images/ms-dynamics-gp-anypoint-config.png)  

## Use Case: Studio

### Create Customer

![Create customer use case flow](_images/ms-dynamics-gp-create-customer.png) 

- 
From the Mule Palette drag an HTTP Listener element to the canvas and use the default configuration but with the path set to /createCustomer. 
- 
Drag a Transform Message element next to the HTTP Listener and add: `%dw 2.0 output application/xml ns ns0 http://schemas.microsoft.com/dynamics/gp/2010/01 ns ns01 http://schemas.datacontract.org/2004/07/Microsoft.Dynamics.Common ns ns02 http://schemas.datacontract.org/2004/07/Microsoft.Dynamics.GP ns xsi http://www.w3.org/2001/XMLSchema-instance --- { ns0#CreateCustomer: { ns0#customer: { ns02#Key: { ns02#Id: attributes.queryParams.customerKeyID }, ns02#Name: attributes.queryParams.customerName }, ns0#context: { ns01#OrganizationKey @(xsi#"type": "ns01:CompanyKey") : { ns01#Id: attributes.queryParams.companyKeyID } } } }`dataweave
- 
Drag a Microsoft Dynamics GP connector next to the Transform Message. 
- 
Set its configuration and fill in the required fields, this applies to any other Dynamics GP connectors that are dragged into the flows. 
- 
Select the operation Create Entity. Pick the Customer entity from the drop-down list. Leave the Input Reference as it is. 
- 
Drag a Set Payload element next to the Connector and set its value to `Success`.

### Get Customer

![Get customer use case flow](_images/ms-dynamics-gp-get-customer.png) 

- 
From the Mule Palette, drag an HTTP Listener element to the canvas and use the default configuration but with the path set to /getCustomer. 
- 
Drag a Transform Message element next to the HTTP Listener and add: `%dw 2.0 output application/xml ns ns0 http://schemas.microsoft.com/dynamics/gp/2010/01 ns ns01 http://schemas.datacontract.org/2004/07/Microsoft.Dynamics.GP ns ns02 http://schemas.datacontract.org/2004/07/Microsoft.Dynamics.Common ns xsi http://www.w3.org/2001/XMLSchema-instance --- { ns0#GetCustomerByKey: { ns0#key: { ns01#Id: attributes.queryParams.customerKeyID }, ns0#context: { ns02#OrganizationKey @(xsi#"type": "ns02:CompanyKey") : { ns02#Id: attributes.queryParams.companyKeyID } } } }`dataweave
- 
Drag a Microsoft Dynamics GP connector next to the Transform Message. 
- 
Select the operation Get Entity By Key. Pick the Customer entity from the drop-down list. Leave the Input Reference as it is. 
- 
Drag a Transform Message next to the connector and add: `%dw 2.0 output application/json --- payload`dataweave

### Update Customer

![Update customer use case flow](_images/ms-dynamics-gp-update-customer.png) 

- 
From the Mule Palette, drag an HTTP Listener element to the canvas and use the default configuration but with the path set to /updateCustomer. 
- 
Drag a Transform Message element next to the HTTP Listener and add: `%dw 2.0 output application/xml ns ns0 http://schemas.microsoft.com/dynamics/gp/2010/01 ns ns01 http://schemas.datacontract.org/2004/07/Microsoft.Dynamics.Common ns ns02 http://schemas.datacontract.org/2004/07/Microsoft.Dynamics.GP ns xsi http://www.w3.org/2001/XMLSchema-instance --- { ns0#GetCustomerByKey: { ns0#key: { ns02#Id: attributes.queryParams.keyId }, ns0#context: { ns01#OrganizationKey @(xsi#"type": "ns01:CompanyKey") : { ns01#Id: attributes.queryParams.companyKeyID } } } }`dataweave
- 
Create a variable called 'updatedComment' on this Transform Message with this value: `%dw 2.0 output application/java --- { comment1: payload.customer.comment1 }`dataweave
- 
Drag a Microsoft Dynamics GP connector next to the Transform Message. 
- 
Select the Get Entity By Key operation. Pick the Customer entity from the drop-down list. Leave the Input Reference as it is. 
- 
Drag a Transform Message element next to the Connector and add: `%dw 2.0 output application/java --- %dw 2.0 output application/xml ns ns0 http://schemas.microsoft.com/dynamics/gp/2010/01 ns ns01 http://schemas.datacontract.org/2004/07/Microsoft.Dynamics.Common ns ns02 http://schemas.datacontract.org/2004/07/Microsoft.Dynamics.GP ns xsi http://www.w3.org/2001/XMLSchema-instance --- { ns0#UpdateCustomer: { ns0#customer: { ns02#Comment1: vars.comment1, ns02#Key: { ns02#Id: payload.key.id }, ns02#Name: payload.name }, ns0#context: { ns01#OrganizationKey @(xsi#"type": "ns01:CompanyKey") : { ns01#Id: attributes.queryParams.companyKeyID } } } }`dataweave
- 
Drag a Microsoft Dynamics GP connector next to the Transform Message. 
- 
Select the Update Entity operation. Pick the Customer entity from the drop-down list. Leave the Input Reference as it is. 
- 
Drag a Set Payload element next to the connector and set its value to `Success`.

### Delete Customer

![Delete customer use case flow](_images/ms-dynamics-gp-delete-customer.png) 

- 
From the Mule Palette, drag an HTTP Listener element to the canvas and use the default configuration but with the path set to /deleteCustomer. 
- 
Drag a Transform Message element next to the HTTP Listener and add: `%dw 2.0 output application/xml ns ns0 http://schemas.microsoft.com/dynamics/gp/2010/01 ns ns01 http://schemas.datacontract.org/2004/07/Microsoft.Dynamics.GP ns ns02 http://schemas.datacontract.org/2004/07/Microsoft.Dynamics.Common ns xsi http://www.w3.org/2001/XMLSchema-instance --- { ns0#DeleteCustomer: { ns0#key: { ns01#Id: attributes.queryParams.customerKeyID }, ns0#context: { ns02#OrganizationKey @(xsi#"type": "ns02:CompanyKey") : { ns02#Id: attributes.queryParams.companyKeyID } } } }`dataweave
- 
Drag a Microsoft Dynamics GP connector next to the Transform Message. 
- 
Select the Delete Entity. Pick the Customer entity from the drop-down list. Leave the Input Reference as it is. 
- 
Drag a Set Payload element next to the connector and set its value to `Success`.

### Get Customer List

![Get customer list use case flow](_images/ms-dynamics-gp-get-customer-list.png) 

- 
From the Mule Palette, drag an HTTP Listener element to the canvas and use the default configuration but with the path set to /getCustomerList. 
- 
Drag a Transform Message element next to the HTTP Listener and add: `%dw 2.0 output application/xml ns ns0 http://schemas.microsoft.com/dynamics/gp/2010/01 ns ns01 http://schemas.datacontract.org/2004/07/Microsoft.Dynamics.Common ns ns02 http://schemas.datacontract.org/2004/07/Microsoft.Dynamics.GP ns xsi http://www.w3.org/2001/XMLSchema-instance --- { ns0#GetCustomerList: { ns0#criteria: { ns02#Name: { ns01#Like: attributes.queryParams.like } }, ns0#context: { ns01#OrganizationKey @(xsi#"type": "ns01:CompanyKey") : { ns01#Id: attributes.queryParams.companyKeyID } } } }`dataweave
- 
Drag a Microsoft Dynamics GP connector next to the Transform Message. 
- 
Select the Get Entity List. Pick the Customer entity from the drop-down list. Leave the Input Reference as it is. 
- 
Drag a Transform Message next to the connector and add: `%dw 2.0 output application/json --- payload`dataweave

## See Also

[Salesforce Help](https://help.salesforce.com)