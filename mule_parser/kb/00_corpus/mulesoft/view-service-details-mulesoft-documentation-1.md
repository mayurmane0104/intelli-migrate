# View Service Details | MuleSoft Documentation

**Source:** [https://docs.mulesoft.com/general/exp-services-view-details](https://docs.mulesoft.com/general/exp-services-view-details)

---

- 
Exchange: Exchange Viewer 
- 
Exchange: Exchange Contributor 
- 
Exchange: Exchange Administrator 

# View Service Details

Open a catalog entry in **Portfolio** to see its service detail page: a single view of one service, such as an agent, MCP server, LLM proxy, API, or gateway. From this page, review status and cost, relationships to other services, deployments, policies, monitoring, conformance, and change history without switching contexts.

## Before You Begin

Before getting started, make sure you have:

- 
An Anypoint Platform account. 
- 
One of these permissions: For more information, see [Enhanced Experience Permissions](exp-home-start#permissions).

## Service Detail Tabs

The page is organized into tabs. The following table lists each tab, what it shows, and whether that tab appears on the detail page for each catalog type. **Yes** means the tab is shown in typical configurations; **No** means it is omitted or you use another area of the experience for the same job (see the note after the table). Labels and fields inside a tab can differ by service type and release. For end-to-end portfolio tasks that reference these tabs, see [Enhanced MuleSoft Experience Overview](exp-overview).

| Tab | What You See | API | Agent | MCP Server | LLM Proxy | Gateway | 
|---|---|---|---|---|---|---|
| 
 | Short summary of what the service does and its specification. | Yes | Yes | Yes | Yes | Yes | 
| 
 | Deployed instances, environments (for example production or sandbox), and gateways when that catalog type supports instances. | Yes | Yes | Yes | Each LLM Proxy is exactly one instance so there is no  | No | 
| 
 | Governance policies attached to the service or its instances (access, data, performance, compliance, and related domains your organization uses). If the instance uses a Kong gateway, the listed policies are gateway-level policies (plugins). Other service-level policies (plugins) can also apply. | Yes | Yes | Yes | Yes | No | 
| 
 | Runtime metrics and analytics for health and usage when the system surfaces them for the service or gateway you are viewing. | Yes | Yes | Yes | Yes | No | 
| 
 | Compliance score and rule-level analysis for conformance reporting where that tab is available. | Yes | Yes | Yes | No | No | 

| 
 | 

## Open a Service Detail Page

- 
In **Portfolio**, open the catalog for the service type (for example**APIs**or**Agents**).
- 
Use the search box to find the service by name or description, or scan the list or grid. 
- 
Select the service card to open its detail page.