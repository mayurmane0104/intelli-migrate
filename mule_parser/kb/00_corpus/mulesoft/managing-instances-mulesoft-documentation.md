# Managing Instances | MuleSoft Documentation

**Source:** [https://docs.mulesoft.com/api-manager/latest/api-instance-landing-page](https://docs.mulesoft.com/api-manager/latest/api-instance-landing-page)

---

# Managing Instances

An instance is the instantiation of a definition, such as an API or another component. It is an object that shares data between gateways and the control plane. Depending on its type, an instance can represent a proxy that serves upstream traffic, a Mule application endpoint, or another managed component (for example, a broker, agent, or LLM).

You can create, import, and deprecate instances using API Manager. You can use instances in multiple environments, and you can also have multiple instances of the same asset in one environment.

For example, you can create one instance of an API version that serves as a proxy and another to directly manage it as an endpoint. You can apply policies based on how the instance is configured — proxy or endpoint. For example, you can apply caching policies to a proxy instance, and throttling or security policies to an endpoint instance. Additionally, you can promote an instance to another environment.

To manage instances in API Manager:

- 
Add an instance for your relevant gateway: 
- 
View an instance’s summary for information or to export it: - 
[Determining API Instance ID on API Manager](find-api-id-task)- API Manager generates the`apiId`of new APIs managed by API Manager for use with Mule 4.
- 
[Exporting an API Instance on API Manager](export-api-latest-task)- After creating an instance, you can export it. This exports the instance configuration and Exchange asset relationship. You can then import it into another environment in the same business group to create a new instance.
- 
[Access Asset and Developer Portals](access-developer-portal-task)- Open the API in Anypoint Exchange from API Manager or from the organization’s public portal to review resources, methods, publish dates, and mocking for the asset.
 
- 
- 
Modify an instance when you no longer need it or when you need to update it: - 
[Editing an API Instance](edit-api-endpoint-task)- Edit the instance’s configuration settings to update its base path, port, TLS context, and more.
- 
[Deprecating an API instance on API Manager](deprecate-api-latest-task)- While transitioning consumers to an updated instance, you can prevent developers from signing up for access to the old instance.
- 
[Delete API Instances](delete-api-task)- You can delete an instance and its version if you no longer need to manage it from API Manager.
- 
[Managing API Instance Versions](manage-versions-instances-concept)- After you create an asset in Anypoint Platform, you configure the version details and publish it to Anypoint Exchange (Exchange). The version resides in Exchange, and not in API Manager. However, you then manage this version from API Manager.
 
- 
- 
Explore advanced use cases for instances: - 
[Configure Multiple Client Providers for Client Management](configure-multiple-credential-providers)- You can use multiple client providers, such as OpenAM and PingFederate, to help enforce security and regulations in your business organization. These client providers enable you to secure your operational data, including client credentials and access tokens.
- 
[Governing API Instances](govern-api-instances)- You can govern instances using Anypoint API Governance. View the governance validation report for governed instances to identify conformance issues and take action to fix them.
 
-