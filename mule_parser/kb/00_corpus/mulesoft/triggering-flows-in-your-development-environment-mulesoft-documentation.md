# Triggering Flows in Your Development Environment | MuleSoft Documentation

**Source:** [https://docs.mulesoft.com/anypoint-code-builder/int-trigger-flows](https://docs.mulesoft.com/anypoint-code-builder/int-trigger-flows)

---

http://localhost:8081/mypath

# Triggering Flows in Your Development Environment

When your integration or implementation builds successfully within the Anypoint Code Builder IDE, the application deploys to your local development environment, whether you use the desktop or cloud IDE.

Configure the **HTTP Listener** from [Anypoint Connector for HTTP](../http-connector/latest/) (HTTP Connector) to trigger the execution of a flow in a deployed application. Or trigger the flow locally from the built-in terminal in Anypoint Code Builder, or from a VS Code extension like Thunder Client.

A **Scheduler**, a **Flow Ref**, or any connector trigger or message source can initiate a flow execution. These components serve as entry points that listen for specific events or time intervals to start the flow logic.

## Before You Begin

- 
Complete [Getting Started with Anypoint Code Builder](start-acb)for your IDE.
- 
Make sure an integration or implementation project with an HTTP Listener ( `<http:listener/>`) is available from the cloud or desktop IDE.To create a project, see [Creating Integrations](int-create-integrations)or[Implementing APIs](imp-implementing-apis), or follow[Take Your API Specification from Design Through Deployment](tutorials#modular-learning-paths).

## URLs for Triggering a Flow from an HTTP Listener

For integrations and implementations that you build and deploy within your IDE during the development process, the URL to use for triggering an HTTP Listener differs depending on whether the listener is within the configuration XML for a scaffolded interface that is generated from an API specification or within a configuration XML file that does not implement a scaffolded interface.

Typically, for apps that use an HTTP Listener, you configure the host to `0.0.0.0` and the port to `8081`. If port `8081` is in use by another application, you can use a similar port, such as `8082`.

- 
Trigger a flow within a configuration XML that *does not*contain a scaffolded interface by using a URL similar to this one from your IDE’s terminal:The port and host are defined in the `<http:listener-connection/>`element, and the endpoint is defined by the`path`attribute in the`<http:listener/>`element:`<http:listener-config name="inbound-request" doc:name="Listener Config" doc:id="b5c62f"> <http:listener-connection host="0.0.0.0" port="8081"/> </http:listener-config> <flow name="myFlow"> <http:listener path="mypath" config-ref="inbound-request" doc:name="HTTP /flights" /> ... </flow>`xml

- 
Trigger a flow from the listener within a scaffolded interface by using a URL similar to this one from your IDE’s terminal: http://localhost:8081/api/my-endpoint Notice `/api/my-endpoint`in the example. For this case, the endpoint is defined within the`name`attribute of a`<flow/>`element in the interface, and`api`is defined in an HTTP Listener in the interface.For example, assume that a flow in a scaffolded interface references a flow ( `getFlights`):`<flow name="get:\flights:american-flights-api-config"> <flow-ref name="getFlights"/> <logger level="INFO" message="get:\flights:american-flights-api-config" /> </flow>`xmlAlso assume that the `getFlights`flow resides in an XML configuration file for the implementation:`<flow name="getFlights" > <set-payload value="Hello Flights!" doc:name="Set payload" doc:id="gwdsmi" /> <logger doc:name="Logger" doc:id="dnitvb" message="#[payload]"/> </flow>`xmlThe URL to trigger this flow uses `flights`as the endpoint:http://localhost:8081/api/flights The URL adds `/api`before the`/flights`endpoint to make the request through the`<http:listener/>`in the interface. Generally, a listener is located before the router, as in this example:`<apikit:config name="american-flight-api-config" api="resource::bc64acc7-41ad-43b7-9e0a-092182b03271:American-Flight-API:1.0.0:raml:zip:american-flight-api.raml" outboundHeadersMapName="outboundHeaders" httpStatusVarName="httpStatus" /> <flow name="american-flight-api-main"> <http:listener config-ref="inbound-request" path="/api/*">`**(1)**<http:response statusCode="#[vars.httpStatus default 200]"> <http:headers>#[vars.outboundHeaders default {}]</http:headers> </http:response> <http:error-response statusCode="#[vars.httpStatus default 500]"> <http:body>#[payload]</http:body> <http:headers>#[vars.outboundHeaders default {}]</http:headers> </http:error-response> </http:listener> <apikit:router config-ref="american-flight-api-config" />**(2)**... </flow>xml**1**Within the listener ( `<http:listener/>`), the attribute`path="/api/*"`is set automatically during the scaffolding process.**2**The router ( `<apikit:router/>`) is located after the listener in the scaffolded interface within the configuration XML.

## Trigger a Flow

Use the terminal in Anypoint Code Builder to trigger a flow through an HTTP Listener in an integration or implementation project that is deployed locally, within your IDE. This procedure is for Mule apps within the desktop or cloud IDE.

| The examples in this procedure show how to trigger the flow with a `curl`command from the IDE’s terminal. You can also use Thunder Client, a third-party extension for VS Code, to trigger a flow with the same URLs. For security reasons, external REST clients, such as Advanced REST Client and Postman, are not allowed to send requests to projects deployed in the cloud IDE. | 

Before attempting to trigger a flow, review [URLs for Triggering a Flow from an HTTP Listener](#trigger-urls), and verify that you meet the prerequisites in [Before You Begin](#before-you-begin).

- 
Before starting your Mule app, confirm that the connection to the listener is successful: From the code editor, above the HTTP Listener configuration ( `<http:listener-config/>`), click**Test Connection**.- 
If the test succeeds, you see a **Connection is valid**message.
- 
If the connection fails, an error message indicates that the connection was unsuccessful. If the app is running when you click **Test Connection**, this error message appears:`Invalid Connection Got status code: 500 when trying to resolve a Mule Runtime operation. Reason: 'Internal Server Error.`
 
- 
- 
Open the Run and Debug panel. ## Show me how- 
Click the ![](_images/icon-run-debug.png) ( (**Run and Debug**) icon in the activity bar.
- 
Use the keyboard shortcuts: - 
Mac: Cmd+Shift+d 
- 
Windows: Ctrl+Shift+d 
 
- 
- 
In the desktop IDE, select **View**>**Run**.
- 
In the cloud IDE, click the ![](_images/icon-menu.png) (menu) icon, and select (menu) icon, and select**View**>**Run**.
 
- 
- 
Click the ![](_images/icon-start-debug.png) ( (**Start Debugging (F5)**) icon for**Debug Mule Application**.Alternatively, if the **Start Debugging (F5)**icon is not present:- 
Click **Run and Debug**.
- 
If a **Select debugger**dropdown menu appears, select**Mule Xml Debugger**to initiate the debugging session:![Run and Debug button and Mule XML Debugger menu item](_images/run-debug-imported-folder.png) When the application deploys successfully, you see a `DEPLOYED`log message in the output panel:********************************************************************** * - - + DOMAIN + - - * - - + STATUS + - - * ********************************************************************** * default * DEPLOYED * ********************************************************************** 
 
- 
- 
From your IDE, open the Terminal window in the console: - 
In the desktop IDE, select **View**>**Terminal**.
- 
In the cloud IDE, click the ![](_images/icon-menu.png) (menu) icon, and select (menu) icon, and select**Terminal**>**New Terminal**.
- 
For either IDE: Press Ctrl and then press the backtick key (`). 
 
- 
- 
In the IDE’s terminal, click the name of the shell to use, such as PowerShell (for Windows), Bash ( `bash`), or Z shell (`zsh`for Mac).Alternatively, click the **+**icon in the terminal to open a new command prompt.
- 
At the command prompt, provide a `curl`command to trigger the flow.- 
To trigger a flow from an HTTP Listener that doesn’t reside within an interface, use `curl`with a URL similar to this one:$ curl localhost:8081/mypath Use `localhost`instead of`0.0.0.0`. Get[more information](#trigger-url-no-interface)about triggering the endpoint.If successful, the command returns a response. 
- 
To trigger a flow from an HTTP Listener that resides in a scaffolded interface, use `curl`with a URL similar to this one:$ curl http://localhost:8081/api/mypath2 Use `localhost`instead of`0.0.0.0`, and add the listener`path`for before the router (such as`api`for most scaffolded interfaces) and the endpoint (such as`mypath2`) to the URL. Get[more information](#trigger-url-interface)about triggering the endpoint.
 
-