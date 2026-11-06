# Logging and Debugging | MuleSoft Documentation

**Source:** [https://docs.mulesoft.com/mule-runtime/latest/logging-and-debugging](https://docs.mulesoft.com/mule-runtime/latest/logging-and-debugging)

---

# Logging and Debugging

MuleSoft provides a variety of logging and debugging options for Mule apps.

Application logs and a runtime log help you monitor and troubleshoot your apps and the Mule server. For details, see [Configuring Logging](logging-in-mule).

You can [enable verbose logging](enable-verbose-logging) for connectors and modules to record debug level information in the logs.

The Logger component can help you monitor or even debug your Mule app by logging important information such as error messages, status notifications, payloads, and so on. You can add a Logger anywhere in a flow, and you can configure it to log a string that you specify, the output of a DataWeave expression you write, or any combination of strings and expressions. For details, see [Logger Component](logger-component-reference) in the Core component documentation.

To control the display of Mule stack traces, you can use command-line arguments or set properties in Anypoint Studio. For details, see [Configuring Mule Stack Traces](configuring-mule-stacktraces).

To troubleshoot a Mule app in Anypoint Studio, you can use the [Studio Visual Debugger](../../studio/visual-debugger-concept), which lets you set breakpoints to stop execution and check events. If you are creating your Mule app outside of Studio, you can either use MUnit to test your app, or you can activate remote debugging. For details, see [Debugging Outside Studio](debugging-outside-studio).

If you are running your Mule application in CloudHub, see [View Log Data](../../cloudhub/viewing-log-data) for additional information about log data and persistence.