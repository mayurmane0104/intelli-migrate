# https://docs.mulesoft.com/general/exp-instances-add.md

**Source:** [https://docs.mulesoft.com/general/exp-instances-add.md](https://docs.mulesoft.com/general/exp-instances-add.md)

---

```
# Creating and Managing Instances
> For the full documentation index, see: https://docs.mulesoft.com/llms.txt
Instances represent how a service runs in a specific environment, such as production or sandbox, and
how traffic reaches it through gateways or runtimes your organization manages.
Services such as APIs, agents, MCP servers, and LLM proxies can include instances. In the enhanced
experience, you manage instances from the service detail page through the **Instances** tab.
Managed paths through Anypoint Omni Gateway can provide additional policy and monitoring
integrations if your organization supports them. Unmanaged or external paths remain available when
they align with your operating model.
## Before You Begin
Before getting started, make sure you have:
- An Anypoint Platform account.
- These permissions:
  - API Manager: API Creator to create instances.
  - API Manager: View APIs Configuration to view instances.
  - API Manager: Edit APIs Configuration to edit instances.
  For more information, see [Enhanced Experience Permissions](exp-home-start#permissions).
## Open the APIs Catalog
1.  In **Portfolio**, open the catalog for the service type, such as **APIs**, **Agents**, **MCP
    Servers**, or **LLM Proxies**.
2.  Select a service to open its detail page.
3.  Open the **Instances** tab.
Field names, required metadata, and available gateway or runtime options depend on the selected
service type and your organizationâ€™s configuration.
## Create an Instance
1.  In the **Instances** tab, click **Add Instance**.
2.  Select the instance type:
    - **Managed Instance** â€“ Creates a new instance on an Omni Gateway with full support for
      authentication, monitoring, and policy enforcement.
    - **Unmanaged Target** â€“ Creates a basic record of an API endpoint. You can add management for
      this endpoint later.
3.  Complete the **Instance** fields:
    - **Environment** â€“ Select the environment where the instance runs, such as Sandbox or
      Production.
    - **Omni Gateway** â€“ Select the gateway to route traffic through. Required for managed
      instances.
    - **Version** â€“ Select the API version for this instance.
    - **Label** â€“ Optional label to identify the instance.
4.  Under **Target**, enter the **Target URL** where the instance proxies requests.
5.  Click **Create Instance**.
## After You Create or Change an Instance
After creating or updating an instance, you can continue managing the service through related areas
of the experience.
- Use the **Policies** tab to review or apply policies to the instance. If the instance uses a Kong
  gateway, applying a policy targets the gateway level and protects all services in that gateway.
- Use the **Monitoring** tab to review metrics and runtime performance when monitoring is available.
- Coordinate with platform owners if DNS, certificates, or upstream routing changes must happen
  outside the product.
## See Also
- [Adding Services to Your Portfolio](exp-services-add-to-portfolio)
- [Register Services Manually](exp-services-register-manually)
- [Create a Scanner for Provider Services](exp-services-connect-providers-to-add)
- [View Service Details](exp-services-view-details)
- [Monitoring Your Services](exp-services-monitoring)
```