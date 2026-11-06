# Amazon RDS Connector 1.4 | MuleSoft Documentation

**Source:** [https://docs.mulesoft.com/amazon-rds-connector/latest](https://docs.mulesoft.com/amazon-rds-connector/latest)

---

```
<dependency>
  <groupId>com.mulesoft.connectors</groupId>
  <artifactId>mule-amazon-rds-connector</artifactId>
  <version>x.x.x</version>
  <classifier>mule-plugin</classifier>
</dependency>
```
xml# Amazon RDS Connector 1.4

| Where possible, we changed noninclusive terms to align with our company value of Equality. We maintained certain terms to avoid any effect on customer implementations. | 

Anypoint Connector for Amazon RDS (Amazon RDS Connector) provides connectivity to the Amazon Relational Database Service (Amazon RDS) API. Amazon RDS Connector enables you to interface with Amazon RDS, which provides cost-efficient and resizable capacity and automation of time-consuming administration tasks such as hardware provisioning, database setup, patching, and backups.

## Before You Begin

To use the Amazon RDS Connector, you must have the following:

- 
Access to Amazon Web Services - RDS 
- 
AWS Identity and Access Management (IAM) user account credentials to access AWS with the connector 

## POM File Information

## Add the Connector to Your Project

Anypoint Studio provides two ways to add the connector to your Studio project:

- 
From the Exchange button in the Studio taskbar 
- 
From the Mule Palette view 

### Add the Connector Using Exchange

- 
In Studio, create a Mule project. 
- 
Click the Exchange icon **(X)**in the upper-left of the Studio task bar.
- 
In Exchange, click **Login**and supply your Anypoint Platform username and password.
- 
In Exchange, search for "rds". 
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
In **Add Modules to Project**, type "rds" in the search field.
- 
Click this connector’s name in **Available modules**.
- 
Click **Add**.
- 
Click **Finish**.

## Configure the Connector Global Element

To use Amazon RDS Connector in your Mule application, configure a global Amazon RDS element that all the Amazon RDS connectors in your project can use.

- 
Click the **Global Elements**tab at the bottom of the canvas.
- 
On the Global Configuration Elements screen, click **Create**.
 The following window displays:![Global Configuration Elements Wizard](_images/amazon-rds-config-global-wizard.png)  
- 
In the Choose Global Type wizard, expand **Connector Configuration**, select**Amazon RDS Configuration**, and click**Ok**.
 The following window displays:![Create DB Instance Configure](_images/amazon-rds-create-db-instance-config.png)  
- 
Configure the parameters according to instructions below: Parameter Description **Name**Enter a name for the configuration for the connector to reference. **Session Token**Enter the session token provided by AWS Security Token Service (STS). **Access Key**Enter an alphanumeric text string that uniquely identifies the user who owns the account. **Secret Key**Enter the key that is used as a password. **Try Default AWS Credentials Provider Chain**Select the checkbox to use temporary credentials. **Region Endpoint**Select the region to use for the Amazon RDS client. When you do not select a region, it defaults to 'us-east-1'. Placeholder values refer to a configuration file `mule-artifact.properties`placed in the`src/main/resources`folder of your project. You can either enter your credentials into the global configuration properties, or reference a configuration file that contains these values. For simpler maintenance and better reusability of your project, MuleSoft recommends that you use a configuration file. Keeping these values in a separate file is useful if you need to deploy to different environments, such as production, development, and QA, where your access credentials differ.
- 
On the Advanced tab, keep the Reconnection strategy default entries. 
- 
Click **Test Connection**to confirm that the parameters of your global configuration are accurate, and that Mule is able to successfully connect to Amazon RDS.
- 
Click **OK**to save the global connector configurations.

### Configure With the XML Editor or Standalone

Ensure that you include the Amazon RDS namespaces in your configuration file.

```
<?xml version="1.0" encoding="UTF-8"?>
<mule xmlns:ee="http://www.mulesoft.org/schema/mule/ee/core"
	xmlns:rds="http://www.mulesoft.org/schema/mule/rds"
	xmlns:http="http://www.mulesoft.org/schema/mule/http"
	xmlns="http://www.mulesoft.org/schema/mule/core"
	xmlns:doc="http://www.mulesoft.org/schema/mule/documentation"
	xmlns:spring="http://www.springframework.org/schema/beans"
	xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
	xsi:schemaLocation="http://www.springframework.org/schema/beans
	http://www.springframework.org/schema/beans/spring-beans-current.xsd
	http://www.mulesoft.org/schema/mule/core
	http://www.mulesoft.org/schema/mule/core/current/mule.xsd
	http://www.mulesoft.org/schema/mule/http
	http://www.mulesoft.org/schema/mule/http/current/mule-http.xsd
	http://www.mulesoft.org/schema/mule/rds
	http://www.mulesoft.org/schema/mule/rds/current/mule-rds.xsd
	http://www.mulesoft.org/schema/mule/ee/core
	http://www.mulesoft.org/schema/mule/ee/core/current/mule-ee.xsd">
<!-- Put your flows and configuration elements here -->
</mule>
```
xmlTo configure Amazon RDS Connector in your application, create a global Amazon RDS configuration outside and above your flows, using the following global configuration code:

```
<rds:config name="Amazon_RDS_Configuration">
	<rds:basic-connection
		accessKey="${config.accessKey}"
		secretKey="${config.secretKey}"
		region="${config.region}"/>
</rds:config>
```
xmlIf you or your Amazon Identity and Access Management users forget or lose the secret access key, you can create a new access key.

## Use the Connector

Amazon RDS connector is an operation-based connector, which means that when you add the connector to your flow, you need to configure a specific web service operation for the connector to perform.

## Connector Namespace and Schema

When designing your application in Studio, the act of dragging the connector operation from the palette onto the Anypoint Studio canvas should automatically populate the XML code with the connector namespace and schema location.

Namespace: `http://www.mulesoft.org/schema/mule/rds`

Schema Location: `http://www.mulesoft.org/schema/mule/rds/current/mule-rds.xsd`

If you are manually coding the Mule application in the Studio XML editor or other text editor, paste the namespace and schema location into the header of your Configuration XML, inside the `<mule>` tag.

```
<mule xmlns:rds="http://www.mulesoft.org/schema/mule/rds"
	xmlns="http://www.mulesoft.org/schema/mule/core"
	xmlns:doc="http://www.mulesoft.org/schema/mule/documentation"
	xmlns:spring="http://www.springframework.org/schema/beans"
	xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
	xsi:schemaLocation="http://www.springframework.org/schema/beans
	http://www.springframework.org/schema/beans/spring-beans-current.xsd
	http://www.mulesoft.org/schema/mule/core
	http://www.mulesoft.org/schema/mule/core/current/mule.xsd
	http://www.mulesoft.org/schema/mule/rds
	http://www.mulesoft.org/schema/mule/rds/current/mule-rds.xsd">
      <!-- here it goes your global configuration elements and flows -->
</mule>
```
xml## Use Cases and Demos

- 
Create a DB instance of your choice over all the Amazon supported databases. 
- 
Stop a DB instance that is available or in a running state. 
- 
Start a DB instance that is in a stopped state. 
- 
Retrieve information on one or all available DB instances. 
- 
Create a DB snapshot for a DB instance. 
- 
Retrieve information on one or all available DB snapshots. 
- 
Delete a DB snapshot. 

## Use the Connector in a Mule App in Studio

If you are developing a Mule application in Anypoint Studio 7.x, use this XML snippet in your pom.xml file:

```
<dependency>
    <groupId>com.mulesoft.connectors</groupId>
    <artifactId>mule-amazon-rds-connector</artifactId>
    <version>x.x.x</version>
    <classifier>mule-plugin</classifier>
</dependency>
```
xmlReplace `x.x.x` with the version that corresponds to the connector you are using.

### Create a Database Instance

This demo Mule application creates a DB instance.

![Creating a DB instance](_images/amazon-rds-create-db-instance-use-case-flow.png) 

- 
Create a new Mule Project in Anypoint Studio. 
- 
Add the following properties to the `mule-artifact.properties`file for your Amazon RDS credentials and place it in the project’s`src/main/resources`directory.`config.accesskey=<Access Key> config.secretkey=<Secret Key> config.region=<Region>`text
- 
Drag an HTTP Listener operation onto the canvas and configure the following parameters: ![RDS HTTP config props](_images/amazon-rds-http-props.png)  Parameter Value **Display Name**Listener **Extension Configuration**If no HTTP element has been created yet, click the plus sign to add a new HTTP Listener Configuration and click OK (leave the values to its defaults). **Path**`/create-db-instance`
- 
Drag a Transform Message component after the HTTP connector to retrieve the HTTP query parameters and set the payload. 
- 
Click the component to open its properties editor. 
 The DataWeave script should look similar to the following:`%dw 2.0 output application/java --- { dbInstanceClass : attributes.queryParams.dbInstanceClass, dbInstanceIdentifier : attributes.queryParams.dbInstanceIdentifier, engine : attributes.queryParams.engine, allocatedStorage : attributes.queryParams.allocatedStorage, masterUsername : attributes.queryParams.masterUsername, masterUserPassword : attributes.queryParams.masterUserPassword }`dataweave
- 
Add a Logger component after the Transform Message component to print the payload data that was set in the previous processor to the Mule Console. 
- 
Configure the Logger according to the table below: Parameter Value **Display Name**Logger (or any other name you prefer) **Message**`#[payload]`**Level**INFO 
- 
Drag the Amazon RDS Connector next to the Logger component. 
- 
Configure the RDS connector by adding a new Amazon RDS Global Element: - 
Click the plus sign next to the Extension Configuration field. 
- 
Configure the global element according to the table below: Parameter Description **Value**Name **Enter a name for the configuration for the connector to reference.**<Configuration_Name> **Session Token**Session token provided by AWS Security Token Service (STS) `${config.sessiontoken}`Access Key **Alphanumeric text string that uniquely identifies the user who owns the account**`${config.accesskey}`**Secret Key**Key that plays the role of a password `${config.secretkey}`Region Endpoint **Region to set for the Amazon RDS Client**When not selected from the drop down list, it defaults to 'us-east-1'. 
- 
Your configuration should look like this: ![RDS use case config](_images/amazon-rds-create-db-instance-config.png)  
- 
The corresponding XML configuration should be as follows: `<rds:config name="Amazon_RDS_Configuration"> <rds:basic-connection accessKey="${config.accessKey}" secretKey="${config.secretKey}"/> </rds:config>`xml
 
- 
- 
Click **Test Connection**to confirm that Mule can connect with the Amazon RDS instance.
- 
If the connection is successful, click **OK**to save the configurations. Otherwise, review or correct any incorrect parameters, then test again.
- 
Back in the properties editor of the Amazon RDS connector, configure the parameters for the createDbInstance operation: Parameter Value **General****Display Name**Enter a the name to display for the Create DB instance. **Extension Configuration**Enter the reference name to the global element you created. **Db instance class**`#[payload.dbInstanceClass]`**Db instance identifier**Enter a valid identifier to uniquely identify the DB instance. **Engine**Choose from among the six DB engines that Amazon RDS supports. **Security****Master username**Enter a valid user name for the database. **Master user password**Enter the password for the database user. **Storage and Maintenance****Allocated storage**A number representing the storage in GB. ![Create DB instance parameter props](_images/amazon-rds-create-db-instance-param-config.png)  
- 
Verify that your XML looks like this: `<rds:create-db-instance config-ref="Amazon_RDS_Configuration" dbInstanceClass="#[payload.dbInstanceClass]" dbInstanceIdentifier="#[payload.dbInstanceIdentifier]" engine="#[payload.engine]" allocatedStorage="#[payload.allocatedStorage]" doc:name="Create db instance" masterUsername="#[payload.masterUsername]" masterUserPassword="#[payload.masterUserPassword]"/>`xml
- 
Add a Logger component after the RDS connector to print the payload data that was output from the Create DB instance processor to the Mule Console. Configure the Logger according to the table below. Parameter Value **Display Name**Logger (or any other name you prefer) **Message**`#[payload]`**Level**INFO 
- 
Drag a Transform Message component after the Logger component to set the payload that would be transferred to the browser. 
- 
Click the component to open its properties editor. The DataWeave script should look similar to the following: `%dw 2.0 output application/json --- { success: true, info: payload }`dataweave
- 
Save and Run the project as a Mule Application: 
 In Package Explorer, right-click the project and click**Run As > Mule Application**.
- 
Open a browser and check the response after entering the URL `http://localhost:8081/create-db-instance`.
 You should see the generated DB instance ID in the browser and its information in the console.

### Demo XML Code

Paste this code into your XML Editor to load the flow for this example use case into your Mule application.

```
<?xml version="1.0" encoding="UTF-8"?>
<mule xmlns:ee="http://www.mulesoft.org/schema/mule/ee/core"
	xmlns:rds="http://www.mulesoft.org/schema/mule/rds"
	xmlns:http="http://www.mulesoft.org/schema/mule/http"
	xmlns="http://www.mulesoft.org/schema/mule/core"
	xmlns:doc="http://www.mulesoft.org/schema/mule/documentation"
	xmlns:spring="http://www.springframework.org/schema/beans"
	xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
	xsi:schemaLocation="http://www.springframework.org/schema/beans
	http://www.springframework.org/schema/beans/spring-beans-current.xsd
	http://www.mulesoft.org/schema/mule/core
	http://www.mulesoft.org/schema/mule/core/current/mule.xsd
	http://www.mulesoft.org/schema/mule/http
	http://www.mulesoft.org/schema/mule/http/current/mule-http.xsd
	http://www.mulesoft.org/schema/mule/rds
	http://www.mulesoft.org/schema/mule/rds/current/mule-rds.xsd
	http://www.mulesoft.org/schema/mule/ee/core
	http://www.mulesoft.org/schema/mule/ee/core/current/mule-ee.xsd">
	<http:listener-config
		name="HTTP_Listener_config"
		doc:name="HTTP Listener config">
		<http:listener-connection
			host="127.0.0.1"
			port="8081" />
	</http:listener-config>
	<rds:config
		name="Amazon_RDS_Configuration"
		doc:name="Amazon RDS Configuration">
		<rds:basic-connection
			accessKey="${config.accessKey}"
			secretKey="${config.secretKey}" />
	</rds:config>
	<flow name="create-db-instance-flow">
		<http:listener
			config-ref="HTTP_Listener_config"
			path="/create-db-instance"
			doc:name="Listener"/>
		<ee:transform doc:name="Transform Message">
			<ee:message >
				<ee:set-payload ><![CDATA[%dw 2.0
output application/java
---
{
	dbInstanceClass : attributes.queryParams.dbInstanceClass,
	dbInstanceIdentifier : attributes.queryParams.dbInstanceIdentifier,
	engine : attributes.queryParams.engine,
	allocatedStorage : attributes.queryParams.allocatedStorage,
	masterUsername : attributes.queryParams.masterUsername,
	masterUserPassword : attributes.queryParams.masterUserPassword
}]]></ee:set-payload>
			</ee:message>
		</ee:transform>
		<logger level="INFO" doc:name="Logger" message="#[payload]"/>
		<rds:create-db-instance
			config-ref="Amazon_RDS_Configuration"
			dbInstanceClass="#[payload.dbInstanceClass]"
			dbInstanceIdentifier="#[payload.dbInstanceIdentifier]"
			engine="#[payload.engine]"
			allocatedStorage="#[payload.allocatedStorage]"
			doc:name="Create db instance"
		 	masterUsername="#[payload.masterUsername]"
			masterUserPassword="#[payload.masterUserPassword]"/>
		 <logger level="INFO" doc:name="Logger" message="#[payload]"/>
		<ee:transform doc:name="Transform Message">
			<ee:message >
				<ee:set-payload ><![CDATA[%dw 2.0
output application/json
---
{
	success: true,
    info: payload
}]]></ee:set-payload>
			</ee:message>
		</ee:transform>
	</flow>
</mule>
```
xml## See Also

- 
[Amazon RDS Connector](https://www.mulesoft.com/exchange/com.mulesoft.connectors/mule-amazon-rds-connector/)
- 
[Salesforce Help](https://help.salesforce.com)