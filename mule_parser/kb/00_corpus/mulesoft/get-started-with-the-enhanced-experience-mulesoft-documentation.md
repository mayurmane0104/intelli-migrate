# Get Started with the Enhanced Experience | MuleSoft Documentation

**Source:** [https://docs.mulesoft.com/general/exp-home-start](https://docs.mulesoft.com/general/exp-home-start)

---

Any of these permissions:

- 
Exchange: Exchange Viewer 
- 
Exchange: Exchange Contributor 
- 
Exchange: Exchange Administrator 

Grow and tune your AI portfolio by registering and monitoring agents, APIs, and gateways in centralized catalogs. Sign in through the entry point your organization provides, such as Anypoint Platform, or a direct URL, to access dashboards and governance strategies based on your assigned permissions. You can review live performance metrics, manage security policies, and track rule-level compliance through automated conformance reports.

These tools ensure your AI assets remain audit-ready while providing clear visibility into cost and runtime health across your organization.

Your organization determines how you access the new experience. Common options include these environments.

Anypoint Platform

In Anypoint Platform, look for the new experience banner or shortcut and choose **Go to the new experience**. Your administrator can also add a direct link in the main navigation or workspace.

Coding assistants

If your organization connects the new experience to a supported assistant, such as Claude Code, follow your internal instructions to open the new experience features from that development environment.

Direct URL

Your organization can share a standalone URL that signs you in to the new experience outside other apps. Use the address your administrator or internal documentation provides.

Custom integrations

Your organization can build access through another tool. Follow the internal access instructions for custom integrations.

| Available access points depend on how your administrators configured the new experience’s integrations with other platforms. | 

Before you rely on the new experience in production, complete these checks with your administrator. Requirements vary by entry point and how your administrator integrates the new experience with other systems.

Confirm that you have a user account for your organization’s entry path, such as Anypoint Platform, and valid credentials to log in.

Confirm that you can reach the new experience and integrated services, such as Anypoint Platform, or a connected coding assistant, from the networks and locations you use.

Confirm that your organization has the required product access for the new experience and that an administrator enabled it for your Anypoint Platform business group or organization.

If the experience isn’t available, contact your Anypoint Platform organization administrator or MuleSoft account team.

Confirm that required integrations with Anypoint Platform or your development environment work end to end.

If the new experience connects to other services, work with your administrator to configure authentication, such as API keys or OAuth tokens, to ensure successful connections.

Confirm that your administrator approved and configured required external connections, such as cloud providers under **Providers**.

The new experience uses Anypoint Platform access management. Your administrator maps jobs to roles and permissions in Access Management. Exact permission names differ by organization. Use this table with your internal access guide.

| Required Permissions | Grants the Ability to | Notes | 
|---|---|---|
| Any of these permissions: 
 | View services | View services in the portfolio and open the catalog overview in Anypoint Exchange. | 
| Any of these permissions: 
 | Create services | Register MCP servers, agents, LLMs, or APIs. | 
| API Manager: API Creator | Create instances | Create or add instances. | 
| API Manager: View APIs Configuration | View instances | View instances for services and open the  | 
| API Manager: Edit APIs Configuration | Edit instances | Edit instances for services. | 
| Any of these permissions: 
 | Create scanners | Create scanners from  To view the  | 
| Any of these permissions: 
 | View monitoring | Open the  | 
| API Manager: View Policies | View policies | View and apply policies on instances, and access policies from the  | 
| API Manager: Manage Policies | Apply policies | Edit policy configurations and add policies. | 
| These permissions: 
 | Use the  | Apply optimization strategies using policies, view policies, view Exchange assets, and query metrics. The Mule Developer Generative AI User permission is required to enable AI features. | 
| Anypoint Code Builder: Mule Developer Generative AI User | Send prompts to agent | Use the native agent. | 
| Any of these permissions: 
 | Create governance strategies | Create governance strategies. To view and create governance strategies, you need the Governance Administrator permission for  | 
| Any of these permissions: 
 | View governance reports | View governance reports at the service and governance strategy levels. To see the conformance badge and whether rulesets passed or failed, you need the Exchange Viewer permission. To view or export detailed governance reports, including violations, warnings, and rule breakdowns, you need the Governance Viewer permission. | 
| Any of these permissions: 
 | View alerts | View API alerts in API Manager and read alerts in Runtime Manager. | 
| Any of these permissions: 
 | Manage alerts | Manage API alerts in API Manager and alerts in Runtime Manager. | 

If you can’t complete an action or a page shows an authorization error, ask your Anypoint Platform organization administrator for the matching permission or role.