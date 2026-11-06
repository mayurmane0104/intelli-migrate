# Creating and Managing Instances | MuleSoft Documentation

**Source:** [https://docs.mulesoft.com/general/exp-instances-add](https://docs.mulesoft.com/general/exp-instances-add)

---

- 
API Manager: API Creator to create instances. 
- 
API Manager: View APIs Configuration to view instances. 
- 
API Manager: Edit APIs Configuration to edit instances. 

# Creating and Managing Instances

Instances represent how a service runs in a specific environment, such as production or sandbox, and how traffic reaches it through gateways or runtimes your organization manages.

Services such as APIs, agents, MCP servers, and LLM proxies can include instances. In the enhanced experience, you manage instances from the service detail page through the **Instances** tab.

Managed paths through Anypoint Omni Gateway can provide additional policy and monitoring integrations if your organization supports them. Unmanaged or external paths remain available when they align with your operating model.

## Before You Begin

Before getting started, make sure you have:

- 
An Anypoint Platform account. 
- 
These permissions: For more information, see [Enhanced Experience Permissions](exp-home-start#permissions).

## Open the APIs Catalog

- 
In **Portfolio**, open the catalog for the service type, such as**APIs**,**Agents**,**MCP Servers**, or**LLM Proxies**.
- 
Select a service to open its detail page. 
- 
Open the **Instances**tab.

Field names, required metadata, and available gateway or runtime options depend on the selected service type and your organization’s configuration.

## Create an Instance

- 
In the **Instances**tab, click**Add Instance**.
- 
Select the instance type: - 
**Managed Instance**– Creates a new instance on an Omni Gateway with full support for authentication, monitoring, and policy enforcement.
- 
**Unmanaged Target**– Creates a basic record of an API endpoint. You can add management for this endpoint later.
 
- 
- 
Complete the **Instance**fields:- 
**Environment**– Select the environment where the instance runs, such as Sandbox or Production.
- 
**Omni Gateway**– Select the gateway to route traffic through. Required for managed instances.
- 
**Version**– Select the API version for this instance.
- 
**Label**– Optional label to identify the instance.
 
- 
- 
Under **Target**, enter the**Target URL**where the instance proxies requests.
- 
Click **Create Instance**.

## After You Create or Change an Instance

After creating or updating an instance, you can continue managing the service through related areas of the experience.

- 
Use the **Policies**tab to review or apply policies to the instance. If the instance uses a Kong gateway, applying a policy targets the gateway level and protects all services in that gateway.
- 
Use the **Monitoring**tab to review metrics and runtime performance when monitoring is available.
- 
Coordinate with platform owners if DNS, certificates, or upstream routing changes must happen outside the product.