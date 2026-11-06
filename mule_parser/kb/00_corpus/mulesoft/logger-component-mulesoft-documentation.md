# Logger Component | MuleSoft Documentation

**Source:** [https://docs.mulesoft.com/mule-runtime/latest/logger-component-reference](https://docs.mulesoft.com/mule-runtime/latest/logger-component-reference)

---

![A flow of a logger component process in a Mule application including error handling in Anypoint Studio](_images/logger-flow.png) 

# Logger Component

This Core component helps you monitor and debug your Mule application by logging important information such as error messages, status notifications, payloads, and so on. You can add a Logger anywhere in a flow, and you can configure it to log a string that you specify, the output of a DataWeave expression you write, or any combination of strings and expressions.

| Keep in mind that the Logger is one of the only components that supports mixing Strings and expressions within a value. DataWeave String interpolation or concatenation within a single expression should be used elsewhere. | 

The configured messages are logged to the app’s log file, which is located in `MULE_HOME/logs/<app-name>.log` if no custom log file path is specified in the `log4j2.xml` file.

In Studio, the logs show in the Console.

The following example displays the message in Set Payload in a browser and also logs the message.

![A flow of a logger component process in a Mule application including error handling in Anypoint Studio](_images/logger-flow.png) 

```
<http:listener-config name="HTTP_Listener_Configuration" host="localhost" port="8081"/>
<flow name="logger-example-Flow">
  <http:listener config-ref="HTTP_Listener_Configuration" path="/"/>
  <set-payload value="Hello MuleSoft!"/>
  <logger message="#[payload]" level="INFO"/>
</flow>
```
xml## Logger Configuration

![A Logger general fields showing name and generic data](_images/logger.png) 

| Field | Value | Description | Example | 
|---|---|---|---|
| Message | String or DataWeave expression | Specifies the Mule log message. By default, messages are logged to the application’s log file. | 
 | 
| Level | Available options: 
 | Specifies the log level. | 
 | 
| Category | String | Optional setting that specifies a category name that it adds to  | 
 | 

## Examples

This Logger is set to monitor message processing status, mixing Strings and expressions:

`<logger category="monitoring" message="Message #[payload.id] processed successfully" level="INFO"/>`xmlThis Logger set to record the processing time of a flow, using a single expression and DataWeave’s String concatenation:

` <logger category="performance" message="#['Message ' ++ payload.id ++ ' took ' ++ vars.processingTime ++ ' milliseconds to process']" level="INFO"/>`xml