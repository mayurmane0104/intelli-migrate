# Adding a Mule Gateway API Instance | MuleSoft Documentation

**Source:** [https://docs.mulesoft.com/api-manager/latest/create-instance-task-mule](https://docs.mulesoft.com/api-manager/latest/create-instance-task-mule)

---

Deploying an API proxy to a self-managed server in API Manager doesn’t deploy the proxy to your on-premises server. After you deploy the proxy in API Manager, deploy the proxy to your on-premises server:
. [Download your new API proxy JAR file](download-proxy-task).
. [Deploy the JAR file to your on-premises server](../../mule-runtime/latest/deploy-on-premises).

# Adding a Mule Gateway API Instance

After you have created an API using Design Center or any other application, you can then manage that API in API Manager by adding an API instance. API instances remain under management until you delete them.

Use Mule Gateway if you have APIs on Mule Runtime that need an API gateway to manage, observe, and secure your APIs.

There are three options for adding an API instance:

- 
**Add a new API:**
- 
**Promote API from environment:**
- 
**Import API from zip file:**

When you are promoting or importing an API instance, you do not have options to alter the configuration. However, when you add a new API instance, you need to the downstream and the upstream configuration settings.

The following diagram shows the relationship of the upstream and downstream configurations settings to your upstream service and the downstream consumer application. In this configuration, the downstream service is the service making API requests that are completed by the upstream service. These terms represent the direction of dependency, not the direction of information. A downstream service could make a `POST` request where it provides information to the upstream service. However, the downstream service is still dependent on the upstream service to complete the request.

![The API instance is deployed on a gateway between the upstream and downstream configuration](_images/api-upstream-downstream-config.png)


## Add a New API

- 
Navigate to **Anypoint Platform**>**API Manager**.
- 
In **API Administration**, click**Add**and select**Add new API**.
- 
Select **Mule Gateway**.
- 
Select the **Proxy type**from the following options:- Connect to existing application (basic endpoint)
- 
Use this option to directly interact with a Mule runtime Engine (Mule) application when your application is configured with API gateway autodiscovery. See [API Autodiscovery](../../mule-gateway/mule-gateway-autodiscovery-overview)for more information.Select the **Mule version**.
- Deploy a proxy application
- 
Use this option to interact by proxy with an application, either because it is a Mule application not configured with API gateway autodiscovery or because it is not a Mule application. See [Configure Proxies for your APIs](api-proxy-landing-page)for more information.
 
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
Configure the downstream configuration settings relevant to your proxy type: ## Connect to existing application (basic endpoint)Field Name Description Required Notes **Instance label**Specifies a label for the API. No If you have multiple managed instances of the same API, add a label to differentiate each instance from the others. **Advanced Options****Consumer endpoint**Specifies a proxy application’s address for consumers to use for sending requests. No **Client provider**Specifies a client provider for the API. Yes Anypoint Platform acts as the client provider by default. To configure an external client provider, see [Client Providers](../../access-management/managing-api-clients).**Manual Approval**Enables manual approval for API Requests. No After submitting the instance, you must go to **Contracts**to approve or revoke the request.## Deploy a proxy applicationField Name Description Required Notes **Protocol**Specifies whether to use HTTP or HTTPS for the validations. Yes If you select HTTPS, specify a TLS context for inbound traffic. **Inbound TLS**Specifies the TLS context to secure inbound traffic. No If you can’t see a context, ensure that you have the correct permissions. **Port**Specifies the number to use if the displayed port is incorrect. Yes **Base path**Specifies the URL prefix for all API paths, relative to the host root. It must start and end with a leading slash `/`.
 If the final slash is not provided, the system adds it automatically.Yes **Instance label**Specifies a label for the API. No If you have multiple managed instances of the same API, add a label to differentiate each instance from the others. **Advanced Options****Consumer endpoint**Specifies a proxy application’s address for consumers to use for sending requests. No **Client provider**Specifies a client provider for the API. Yes Anypoint Platform acts as the client provider by default. To configure an external client provider, see [Client Providers](../../access-management/managing-api-clients).**Request timeout**Specifies the duration after which a request times out. No **Proxy Version**Specifies the version of the proxy to use for the endpoint. No **Service Name**Name of your WSDL service. Yes Only avaliable for WSDL APIs. **Service Port**Port for your WSDL your service. Yes Only avaliable for WSDL APIs. **Service Namespace**Namespace of your WSDL service. Yes Only avaliable for WSDL APIs. **Enable Console**Specifies whether you can expose and test your API specification. No You can specify a different path in **Console Path**, for example,`/spec/*`. Only available if you have an attached API definition.**Validations**Specifies whether to validate inbound requests against a provided specification. No Only available if you have an attached API definition. **Strict validations (optional)**Specifies whether to validate inbound requests against query parameters. No Only available if you have an attached API definition. **User Domain**Specifies whether to use an API gateway domain. No If you chose **Hybrid**as the proxy deployment target previously in the configuration, ensure that you select this option.
- 
Click **Next**.
- 
Configure the upstream configuration settings relevant to your proxy type: ## Connect to existing application (basic endpoint)Field Name Description Required Notes **Upstream URL**The URL to access for the proxy or the API. No For example, you can use the URL of your API asset in Exchange. ## Deploy a proxy applicationField Name Description Required Notes **Upstream URL**The URL to access for the proxy or the API. Yes For example, you can use the URL of your API asset in Exchange. **Outbound TLS**Specifies the TLS context to secure outbound traffic. No If you can’t see a context, ensure that you have the correct permissions. 
- 
Click **Next**.
- 
Review your selections and edit them if necessary. 
- 
If you are ready to deploy, click **Save & Deploy**. Otherwise, you can select**Save**, to save the instance and deploy it at a later time.== Create New API Asset 
 
- 
 
- 

| This feature is only available on GovCloud environments. If you want to create an API asset in other environments, refer to [exchange::to-create-an-asset.adoc#create-an-api-asset](../../exchange/to-create-an-asset#create-an-api-asset) | 

An API asset specifies an interface completely, including its functions, descriptions, how to handle return codes, and dependencies.

Creating an asset sets the asset type, which cannot be changed. All versions of an asset always have the same type.

To create an API asset:

- 
In API Manager, click **Add API**.
- 
From the dropdown list, select **Create new API asset**
- 
Enter a name for the asset. 
- 
Select the asset type from the drop-down list: - 
REST API - RAML: Provide a RAML API specification file. RAML specifications must be a RAML file (.raml). 
- 
REST API - OAS: Provide an OAS API specification file. OAS specifications can be either a YAML (.yaml) or JSON (.json) file. Exchange supports OAS 2.0 and OAS 3.0 specifications. 
- 
SOAP API - WSDL: Provide a WSDL API specification file. SOAP specifications file can be either a WSDL (.wsdl) or XML (.xml) file. 
- 
AsyncAPI: Provide an AsyncAPI specification file in a YAML (.yaml) or JSON (.json) file. 
- 
AsyncAPI with Avro schemas: Provide an Avro fragment in an AVSC (.avsc) file. 
- 
API Spec Fragment - RAML: Provide an API Fragment RAML specification file. Fragment specifications must be a RAML file (.raml). 
- 
API Spec Fragment - JSON: Provide an API Fragment JSON specification (.json) file. 
- 
API Spec Fragment - OpenAPI Specification (OAS): Provide an API Fragment OpenAPI specification file either JSON or YAML. 
- 
HTTP API: This asset does not require a file. This asset type provides an API endpoint that is defined by API Manager. 
 
- 
- 
For assets that require a file: - 
Click **Choose File**to locate the API specification file.
- 
Select the main file of the API. 
 If the file is a ZIP, the selected main file must be in the root directory of the ZIP file. If the file is not a ZIP or if the file is a ZIP file with only one main file, then the main file is selected automatically.
 
- 
- 
If you want to edit the **GroupId**,**AssetId**,**Version**, and**API version**(GAV), click**Advanced**.
 Exchange generates the group ID, asset ID, and version (GAV) for you, and you can change these values as needed. You can change an API’s asset version and version separately. Use the advanced settings to change the asset version.
- 
Choose an option for **Lifecycle state**. The default is Stable.
- 
Click **Publish**.

## Promote an API Instance from Another Environment

- 
Navigate to **Anypoint Platform**>**API Manager**.
- 
In **API Administration**, click**Add API**and select**Promote API from environment**.
- 
Select the **Source Environment**.
- 
Select the **API**by entering the name of the API into the search field.
- 
Select the **API Version**.
- 
Select the **API instance label**.
- 
Optionally, uncheck any of the **Include in Promotion**options you want to exclude.
- 
Click **Promote**.
- 
Review and update the Runtime & Endpoint Configuration details as needed and click **Save**.

## Import API from Zip File

- 
Navigate to **Anypoint Platform**>**API Manager**.
- 
From **API Administration**, click**Add API**and select**Import API from zip file**.
- 
Click **Choose file**and select your API instance configuration zip file.
- 
Click **Next**.
- 
Review and update the API Configuration details as needed and click **Save**.

## Notes

- 
Although OpenAPI Specification (OAS) 3.0 is supported, the callback feature is not. To work around this issue, either handle the callback outside of the Mule runtime engine domain or use an OAS 3.0 specification that does not use callbacks.