# Microsoft .NET Connector 3.1 | MuleSoft Documentation

**Source:** [https://docs.mulesoft.com/microsoft-dotnet-connector/latest](https://docs.mulesoft.com/microsoft-dotnet-connector/latest)

---

# Microsoft .NET Connector 3.1

Anypoint Connector for Microsoft .NET (Microsoft .NET Connector) enables you to execute native .NET code in a Mule application. Microsoft .NET Connector has a dependency on the .NET CLR, which is available only on Windows machines.

This connector executes .NET code using Java Native Interface (JNI), which provides fast interprocess communication between Java Virtual Machine (JVM) and a native application that runs in a host operating system.

The connector supports one operation, **Execute**, which enables users to select a class and method to execute, and to pass the corresponding arguments for that method.

| This connector supports standalone deployments only. This connector does not support CloudHub or Runtime Fabric deployments. | 

## Before You Begin

To use this connector, you must be familiar with:

- 
The .NET API 
- 
Anypoint Connectors 
- 
Mule runtime engine (Mule) 
- 
Elements and global elements in a Mule flow 
- 
Creating a Mule app using Anypoint Studio or Anypoint Code Builder 

Before creating an app, you must have access to:

- 
The .NET target resource 
- 
Anypoint Studio or Anypoint Code Builder 

## Common Use Cases for the Connector

Common use cases for this connector include:

- 
Executing code in an existing binary assembly (DLL) without modification 
- 
Developing new .NET code that extends the capability of your integration application 

For examples, see [Examples](microsoft-dotnet-connector-examples).

## Audience

- 
New users, read: - 
[Using Anypoint Studio to Configure the Connector](microsoft-dotnet-connector-studio)to create your Mule app
- 
[Examples](microsoft-dotnet-connector-examples), which provides one or more use cases for the connector
 
- 
- 
Advanced users, read: 
- 
[Examples](microsoft-dotnet-connector-examples), which provides one or more use cases for the connector
 

## Next Step

After you complete the prerequisites and experiment with examples, you are ready to create your own app and configure the connector using [Anypoint Studio](microsoft-dotnet-connector-studio).

## See Also

- 
[Use Exchange to Discover Connectors, Templates, and Examples](../../connectors/introduction/intro-use-exchange)
- 
[Salesforce Help](https://help.salesforce.com)