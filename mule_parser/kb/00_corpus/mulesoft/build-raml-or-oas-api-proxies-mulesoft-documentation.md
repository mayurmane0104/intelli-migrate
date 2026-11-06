# Build RAML or OAS API Proxies | MuleSoft Documentation

**Source:** [https://docs.mulesoft.com/api-manager/latest/proxy-deploy-raml-oas-proxy](https://docs.mulesoft.com/api-manager/latest/proxy-deploy-raml-oas-proxy)

---

Deploying an API proxy to a self-managed server in API Manager doesn’t deploy the proxy to your on-premises server. After you deploy the proxy in API Manager, deploy the proxy to your on-premises server:
. [Download your new API proxy JAR file](download-proxy-task).
. [Deploy the JAR file to your on-premises server](../../mule-runtime/latest/deploy-on-premises).

# Build RAML or OAS API Proxies

API Manager 2.x enables you to use a RAML or OAS type of API Proxy, for all your Mule 4 based proxies.

## Configuring your RAML or OAS API Proxy

Configure your RAML or OAS API proxy by completing the following steps:

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
Select **REST API**as the**Asset type**.
- 
Upload either a RAML or OAS file for your REST API. Anypoint API Manager supports OpenAPI Specification (OAS) 3.0, with the exception of the callback feature. To work around this issue, handle the callback outside of the Mule runtime engine domain or use an OAS 3.0 specification that does not use callbacks. 
- 
Update the **Asset type**,**API version**, and**Asset version**if you are not using the latest version.For more information about versions in Exchange, see [Asset Versions](../../exchange/asset-versions).
- 
View the **Conformance Status**of the API to ensure the API is conformant. If the**Conformance Status**is nonconformant, after deployment, view the**Governance Report**to find and fix the conformance issues. For more information about the**Governance Report**, see[Governing API Instances](govern-api-instances)- 
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