# Anypoint Connector Configuration | MuleSoft Documentation

**Source:** [https://docs.mulesoft.com/connectors/introduction/intro-connector-configuration-overview](https://docs.mulesoft.com/connectors/introduction/intro-connector-configuration-overview)

---

![Configuring property placeholders](../_images/intro-config-overview-properties.png) 

# Anypoint Connector Configuration

You can configure a connector using [Anypoint Studio](intro-config-use-studio) or [XML](intro-config-xml-maven).

You should understand connector configuration requirements and best practices before configuring a connector.

## Connector Configuration Requirements

Because a connector is a component in a Mule app, you should know how to configure a Mule app before you try to configure a connector. For information, see [Mule Application Development](../../mule-runtime/latest/mule-app-dev).

Every connector has specific configuration requirements, which are described in the reference guide for that connector. Although connectors have different configuration requirements, most connector configurations require that you configure:

- 
A source to initiate the app flow 
- 
The authorization credentials needed to connect to the connector’s data source, for example, to the Salesforce Marketing Cloud, Amazon S3, or SAP Concur APIs. Most connectors use the Basic (username and password), OAuth, or OAuth2 authentication schemes. 
- 
A connector operation to perform the desired action 

### Configure a Source

To configure a source for a connector, select a source associated with the connector you are configuring, or select the HTTP Listener operation or Scheduler endpoint. Not all connectors have associated sources.

For more information, see:

To determine whether the connector you are working with has its own sources, see the reference guide for that connector.

### Authorization Credentials

Connectors that connect to external APIs use the Basic (username and password), OAuth, or OAuth2 authentication scheme.

To configure authorization credentials for a connector, create a [global element](#global-element), which enables you to reuse the configuration for other connector instances.

### Connector Operations

Connector operations are calls to external APIs or other connectivity-related actions that a connector can perform. You can use connector operations anywhere in a flow.

Each connector has different supported operations. To view a list of supported operations for a specific connector, see the reference guide for that connector.

## Best Practices for Configuring Connectors

The following best practices apply to configuring connectors:

- 
Use a global element to define configuration details that can be shared with other instances of the connector in the flow. 
- 
Use property-value placeholders to configure a connector in Anypoint Studio or to configure the connector using XML outside the Studio editor. 
- 
Configure a reconnection strategy to set the number of reconnection attempts to try after an initial failure. 
- 
When you finish the configuration, test the connectivity before you deploy it. 

### Use a Global Element to Define Configuration Details

Global elements act as reusable objects. When you configure a global element for a connector, other instances of that connector in the flow can share that global element.

Create one global element to configure your connection, configuration, or transport details for the connector. Reference the global element from other instances of the connector in the flow to ensure consistency across flow elements.

In addition creating reusability and consistency, global elements make connector maintenance easier. If you must change a connector’s configuration, you can change the configuration in the global element, to apply that change to all connector instances that reference that global element.

Most connectors support the use of a global element for authentication and other functions. For information about configuring a global element for a specific connector, see the user guide for that connector.

### Use Property Placeholders for Property Values

Instead of using static values for a connector configuration in Studio, you can use [Ant-style](https://ant.apache.org/) property placeholders, as shown in this Studio example:

![Configuring property placeholders](../_images/intro-config-overview-properties.png) 

- 
The first item is a placeholder for the Anypoint Connector for Amazon SQS (Amazon SQS) access key. 
- 
The second item is a placeholder for the Amazon SQS secret key. 

Using property placeholders improves the maintainability of your applications because they enable you to change configuration values in one place. If you don’t use property placeholders and configuration parameter values change, you must search for changed parameters in the connector configuration screens or configuration XML.

To make the values for the placeholders available, create a YAML file or properties file to contain the values, place the file in `src/main/resources` in the Mule project, and then reference the file from the connector configuration.

To reference a file that stores property values in Studio:

- 
Open the **Global Elements**tab and click**Create**.
- 
Search for the element called **Configuration properties**.
- 
Select **Configuration properties**.
- 
Click **OK**.
- 
Click **…**to the right of the**File**field and navigate to your YAML or properties file.

To reference a file that stores property values when configuring a connector using XML:

- 
Include a `<configuration-properties>`element inside the`<mule>`element.
- 
Set the `file`parameter with your properties file name:

```
<mule>
  <configuration-properties
    file="myConfiguration.yaml"
    doc:name="Configuration properties"
    />`
  ...
</mule>
```
xmlFor more information about using property placeholders, see [Configure Property Placeholders](../../mule-runtime/latest/mule-app-properties-to-configure).

### Test the Connectivity of the Connector

Studio enables you to test the connection between a connector and its data source by clicking a button.

In Studio, after you configure the required connection values in the **Global Element Properties** screen, click **Test Connection**:

![Test the connection button in Studio](../_images/intro-config-overview-studio-test.png) 

**Test Connection**button in Studio to test the connection

### Configure a Reconnection Strategy for the Connector

When a Mule app starts, a connectivity test runs on connectors that must connect to an external server. If the test fails, the default behavior is to log a warning message and continue with the deployment of the app, instead of blocking the deployment.

You can modify this behavior by setting the number of reconnection attempts to try after an initial failure and forcing the deployment to fail when all connection attempts fail.

To configure a reconnection strategy for a connector using Studio, use the **Advanced** tab in the global element configuration **General** tab. The following example configures a reconnection strategy that:

- 
Forces the deployment to fail if the connection fails and configured reconnection attempts are exhausted 
- 
Limits the number of reconnection attempts to five at a frequency of every 4000 milliseconds (ms) 

![Reconnection strategy example using Studio](../_images/intro-config-overview-reconnection-strategy-studio.png) 

To determine whether a specific connector supports a reconnection strategy and to obtain information about reconnection strategy settings, see the reference guide for that connector.

## See Also

- 
[Salesforce Help](https://help.salesforce.com)