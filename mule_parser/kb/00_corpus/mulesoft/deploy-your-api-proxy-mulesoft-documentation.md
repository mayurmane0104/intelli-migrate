# Deploy Your API Proxy | MuleSoft Documentation

**Source:** [https://docs.mulesoft.com/api-manager/latest/proxy-latest-concept](https://docs.mulesoft.com/api-manager/latest/proxy-latest-concept)

---

Deploying an API proxy to a self-managed server in API Manager doesn’t deploy the proxy to your on-premises server. After you deploy the proxy in API Manager, deploy the proxy to your on-premises server:
. [Download your new API proxy JAR file](download-proxy-task).
. [Deploy the JAR file to your on-premises server](../../mule-runtime/latest/deploy-on-premises).

# Deploy Your API Proxy

You can deploy your API proxy to CloudHub, Runtime Fabric, or a hybrid cloud environment. The resources allocated to the proxy application varies based on the type of proxy you are using. For example, the CloudHub proxy includes a CPU with 0.1 vCores and a memory of 500 MB, by default.

If required, modify the resource allocation from [Runtime Manager](../../cloudhub/deploying-to-cloudhub#change-settings-of-a-deployed-application.adoc).

## Prerequisites

Before you deploy your API proxy, complete the following requirements if you work in a Runtime Fabric or hybrid cloud environment:

- 
Runtime Fabric - 
Obtain the Manage APIs Configuration and Deploy API Proxies permissions on your account. 
- 
Use Mule version 4.1.2 or later. 
 
- 
- 
Hybrid: - 
For private servers, obtain access to a Mule runtime engine (Mule) instance configured for your organization. For information about how to configure a Mule instance as a server, see [register a server in Runtime Manager](../../runtime-manager/servers-create).
- 
Register your private server with a Mule agent that is compatible with your Mule instance. Use the Mule Agent specified in the release notes. 
 
- 

## Deploy Your API Proxy

Deploy your proxy by completing the following steps:

- 
Navigate to **Anypoint Platform**>**API Manager**.
- 
In **API Administration**, click**Add API**and select**Add new API**.
- 
Select **Mule Gateway**as your runtime.
- 
Select **Deploy a proxy application**for**Proxy type**.
- 
If you selected to deploy a proxy application, select the **Target type**from the following options:- 
**CloudHub 2.0**: Select this option if you want to use the Mule runtime hosted by MuleSoft in a container-based cloud infrastructure. The CloudHub 2.0 proxy includes a CPU with 0.1 vCores by default.- 
Select a space. To learn more about spaces, see [Shared Spaces](../../cloudhub-2/ch2-shared-space-about)and[Private Spaces](../../cloudhub-2/ch2-private-space-about).
- 
In **Runtime version**:- 
Select the **Runtime Channel**.
- 
Select the **Version**for Mule runtime.
- 
Select the **Java version**.
 
- 
- 
Enter a **Proxy app name**.
 
- 
- 
**CloudHub**: Select this option if you want to use the Mule runtime hosted on the cloud by MuleSoft. The CloudHub proxy includes a CPU with 0.1 vCores and a memory of 500 MB, by default.- 
In **Runtime version**:- 
Select the **Runtime Channel**.
- 
Select the **Version**for Mule runtime.
- 
Select the **Java version**.
 
- 
- 
Enter a **Proxy app name**.
 
- 
- 
**Hybrid:**Select this option if you want to use a Mule runtime instance running on an on-premises server that is registered in Runtime Manager.See [Register a server in Runtime Manager](../../runtime-manager/servers-create)for more information.- 
Select a target from the list or click **Add server**.
- 
Enter a **Proxy app name**.
 
- 
- 
**Self-managed Server:**Select this option if you want to create a JAR file to deploy an API proxy to a Mule runtime instance running on an on-premises server that is not registered in Runtime Manager. For more information, see[On-Premises Deployment Model](../../mule-runtime/latest/mule-deployment-model).
 
- 

- 
**Runtime Fabric:**Select Runtime Fabric if you want to deploy API Proxies to a Mule runtime engine that is managed on Runtime Fabric. See[Deploying API Proxies to Runtime Fabric](../../runtime-fabric/latest/proxy-deploy-runtime-fabric)for more information.- 
Select a target from the list. 
- 
In **Runtime version**:- 
Select the **Runtime Channel**.
- 
Select the **Version**for Mule runtime.
- 
Select the **Java version**.
 
- 
- 
Enter a **Proxy app name**.- 
Select an API from the following options: 
 
- 
 
- 
- 
Click **Select API from Exchange**if you have an API shared with you through Exchange that you want to manage.- 
Click the API from the list under **Select API**. You can search for a specific API if needed.
- 
Update the **Asset type**,**API version**, and**Asset version**if you are not using the latest version.For more information about versions in Exchange, see [Asset Versions](../../exchange/asset-versions).
- 
If you chose a **RAML/OAS**asset type, view the**Conformance Status**of the API to ensure the API is conformant. If the**Conformance Status**is nonconformant, after deployment, view the**Governance Report**to find and fix the conformance issues. For more information about the**Governance Report**, see[Governing API Instances](govern-api-instances).
 
- 
- 
Click **Create new API**:- 
Enter a **Name**for the new API asset.
- 
Select the **Asset type**from the following options:- 
**REST API:**Select this option if you have a RAML or OAS API definition file you want to include for your asset.Upload either a RAML or OAS file for your REST API. Versions 2.0.0 and later are the recommended versions for OAS or RAML specs, because these versions add native OAS support. If you upload an OAS API specification to an API proxy version 1.0 or earlier, your API specification is translated to RAML. 
- 
**HTTP API:**Select this option if you do not have an API definition file you want to include for your asset. For WebSocket APIs, select HTTP and then choose the WebSocket subtype when selecting the API from Exchange. WebSocket instances can use HTTP or AsyncAPI assets from Exchange.
- 
**SOAP API:**Select this option if you have a WSDL API definition file or an external link to the file.Upload a WSDL file for your SOAP API or add the link to the file. 
- 
**GraphQL API:**Select this option if you have a GraphQL schema definition file you want to include for your asset.Upload the GraphQL schema definition for your GraphQL API. 
 
- 
- 
Update the **Asset type**,**API version**, and**Asset version**if you are not using the latest version.For more information about versions in Exchange, see [Asset Versions](../../exchange/asset-versions).
- 
If you chose a **RAML/OAS**asset type, view the**Conformance Status**of the API to ensure the API is conformant. If the**Conformance Status**is nonconformant, after deployment, view the**Governance Report**to find and fix the conformance issues. For more information about the**Governance Report**, see[Governing API Instances](govern-api-instances).- 
Click **Next**.
- 
Configure the downstream configuration settings: ## Expand for configuration settings.Field Name Description Required Notes **Protocol**Specifies whether to use HTTP or HTTPS for the validations. Yes If you select HTTPS, specify a TLS context for inbound traffic. **Inbound TLS**Specifies the TLS context to secure inbound traffic. No If you can’t see a context, ensure that you have the correct permissions. **Port**Specifies the number to use if the displayed port is incorrect. Yes **Base path**Specifies the URL prefix for all API paths, relative to the host root. It must start and end with a leading slash `/`.
 If the final slash is not provided, the system adds it automatically.Yes **Instance label**Specifies a label for the API. No If you have multiple managed instances of the same API, add a label to differentiate each instance from the others. **Advanced Options****Consumer endpoint**Specifies a proxy application’s address for consumers to use for sending requests. No **Client provider**Specifies a client provider for the API. Yes Anypoint Platform acts as the client provider by default. To configure an external client provider, see [Client Providers](../../access-management/managing-api-clients).**Request timeout**Specifies the duration after which a request times out. No **Proxy Version**Specifies the version of the proxy to use for the endpoint. No **Service Name**Name of your WSDL service. Yes Only avaliable for WSDL APIs. **Service Port**Port for your WSDL your service. Yes Only avaliable for WSDL APIs. **Service Namespace**Namespace of your WSDL service. Yes Only avaliable for WSDL APIs. **Enable Console**Specifies whether you can expose and test your API specification. No You can specify a different path in **Console Path**, for example,`/spec/*`. Only available if you have an attached API definition.**Validations**Specifies whether to validate inbound requests against a provided specification. No Only available if you have an attached API definition. **Strict validations (optional)**Specifies whether to validate inbound requests against query parameters. No Only available if you have an attached API definition. **User Domain**Specifies whether to use an API gateway domain. No If you chose **Hybrid**as the proxy deployment target previously in the configuration, ensure that you select this option.
- 
Click **Next**.
- 
Configure the upstream configuration settings: ## Expand for configuration settings.Field Name Description Required Notes **Upstream URL**The URL to access for the proxy or the API. Yes For example, you can use the URL of your API asset in Exchange. **Outbound TLS**Specifies the TLS context to secure outbound traffic. No If you can’t see a context, ensure that you have the correct permissions. 
- 
Click **Next**.
- 
Review your selections and edit them if necessary. 
- 
If you are ready to deploy, click **Save & Deploy**. Otherwise, you can select**Save**, to save the instance and deploy it at a later time.
 
- 
 
-