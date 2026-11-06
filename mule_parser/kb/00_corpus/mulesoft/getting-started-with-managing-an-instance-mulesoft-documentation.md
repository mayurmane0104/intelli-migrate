# Getting Started with Managing an Instance | MuleSoft Documentation

**Source:** [https://docs.mulesoft.com/api-manager/latest/getting-started-proxy](https://docs.mulesoft.com/api-manager/latest/getting-started-proxy)

---

# Getting Started with Managing an Instance

You can use API Manager to apply policies and to add contracts, alerts, and SLA tiers to your API instance. Additionally, you can configure a runtime for your API that runs in CloudHub or CloudHub 2.0. Although you can also deploy your API runtime using Mule runtime engine (Mule) and Hybrid, deploying your API proxy directly to CloudHub is the fastest and easiest.

| If you are running an API with a standalone server, use the [classic API creation flows](create-instance-task-mule)to manage your API. | 

You can manage your instance using the following steps:

- 
[Create an API asset in Exchange](../../exchange/to-create-an-asset#create-an-api-asset)You can create a REST, HTTP (including the WebSocket subtype), AsyncAPI, SOAP, gRPC, or GraphQL API asset in Exchange and manage it as an API instance in API Manager. 
- 
[Add an API Instance in API Manager](api-instance-landing-page)An instance represents a proxy or component that serves an upstream. API instances support the application of policies and can be deployed to an API gateway. 
- 
A policy extends the functionality of an instance and enforces certain capabilities such as security. A policy can control access and traffic. For example, a policy can generally control authentication, access, allotted consumption, and service level access (SLA).