# Testing a Connection Configuration | MuleSoft Documentation

**Source:** [https://docs.mulesoft.com/anypoint-code-builder/int-configure-components-check-connection](https://docs.mulesoft.com/anypoint-code-builder/int-configure-components-check-connection)

---

![HTTP Listener Test Connection link in the code editor](_images/http-listener-test-connection.png) 

# Testing a Connection Configuration

Most connectors provide an operation, such as the HTTP Listener operation, that triggers the flow to start. These operations typically include connection configurations that you can test.

## Test Connection from the Configuration Panel

You can test the connection from the connectors **Configuration** panel. For example, to test an HTTP Listener connection:

![Configuration panel for connectors](_images/acb-configuration-panel-test.png)


| 1 | Click the +icon on the connector to open the configuration panel. | 
| 2 | After filling in the required fields, click Test Connection. | 

The status bar shows the progress:

- 
**Verifying connection**indicates that the test is in progress.
- 
**Connection is valid**indicates a successful connection.
- 
**Invalid Connection Got status code: 500 when trying to resolve a Mule Runtime operation**indicates a connection error.

## Test Connection from the Code Editor

You can test the connection from the code editor. For example, to test an HTTP Listener connection, click **Test Connection** in the code editor:

![HTTP Listener Test Connection link in the code editor](_images/http-listener-test-connection.png) 

The status bar shows the progress:

- 
**Verifying connection inbound-request**indicates that the test is in progress.
- 
**Connection is valid**indicates a successful connection.
- 
**Invalid Connection Got status code: 500 when trying to resolve a Mule Runtime operation**indicates a connection error.A common code `500`error is`port 8081: Address already in use`. For port conflicts, configure a different port, such as`8082`, and retest the connection.

Before publishing, run your application in debug mode.