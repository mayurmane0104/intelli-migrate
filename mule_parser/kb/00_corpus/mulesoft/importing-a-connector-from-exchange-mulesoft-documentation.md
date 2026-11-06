# Importing a Connector from Exchange | MuleSoft Documentation

**Source:** [https://docs.mulesoft.com/anypoint-code-builder/int-configure-components-import-connector-exchange](https://docs.mulesoft.com/anypoint-code-builder/int-configure-components-import-connector-exchange)

---

![Add Publish operation from the Anypoint MQ Connector](_images/int-add-connector-operation.png) 

# Importing a Connector from Exchange

Anypoint Connectors provide operations for retrieving, modifying, and sending data to and from systems.
In addition to the [built-in connectors](acb-reference#builtin-connectors) that Anypoint Code Builder provides,
you can download many other connectors from Anypoint Exchange.

## Import a Connector from the Canvas

To import a connector from Exchange and add it to your configuration:

- 
{open-config-xml}, such as `my-project-name.xml`.
- 
Click ![](_images/icon-tree-view.png) ( (**Show Mule graphical mode**) in the activity bar to open the UI canvas if it doesn’t open automatically.
- 
Add the connector the same way you added other components from the canvas: - 
In the canvas, click the ![](_images/icon-plus.png) ( (**Add component**) icon.
- 
In the **Add Component**panel, click**Connectors**.
- 
Click the connector name and then click the operation to add, such as **Publish**:![Add Publish operation from the Anypoint MQ Connector](_images/int-add-connector-operation.png)  
- 
If the connector is not available locally, click the ![](_images/icon-search-exchange.png) ( (**Search in Exchange**) toggle:![Search in Exchange toggle](_images/int-connector-search-exchange.png)  **1**Search locally **2**Search in Exchange 
- 
Select the connector to add to your project. You can select from connector versions that are compatible with your Mule runtime and Java version set in Project Properties. ![Exchange connectors with valid versions for the project](_images/int-add-component-connector-version.png)  
- 
Select the operation from the **Add Component**panel.
 
- 

## Import a Connector with a Command

To import a connector from Exchange to use later in your project:

- 
{open-config-xml}, such as `my-project-name.xml`.
- 
Click ![](_images/icon-tree-view.png) ( (**Show Mule graphical mode**) in the activity bar to open the canvas if it doesn’t open automatically.
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
Select the following command: `MuleSoft: Import Asset from Exchange`command
- 
Select **Connector**.
- 
Search for the connector name to import, such as "MQ," for example: !["Import Anypoint MQ Connector from Exchange](_images/int-import-connect-exchange.png)  
- 
Select the connector. 
- 
At the prompt, select the version of the connector to import, such as `v4.0.3`.Anypoint Code Builder imports the connector and makes it available in the Components list. 

For more information about the connectors available on Exchange, see
[Connectors](../connectors/).
For more information about Exchange, see
[Exchange (US)](https://anypoint.mulesoft.com/exchange/) or
[Exchange (EU)](https://eu1.anypoint.mulesoft.com/exchange/)
and
[Anypoint Exchange Overview](../exchange/).