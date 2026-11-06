# Enhanced MuleSoft Experience Release Notes | MuleSoft Documentation

**Source:** [https://docs.mulesoft.com/general/exp-release-notes](https://docs.mulesoft.com/general/exp-release-notes)

---

You can now deploy, edit, and delete MCP servers that share the same name.

# Enhanced MuleSoft Experience Release Notes

The enhanced MuleSoft experience is a unified workspace for managing, governing, and monitoring AI-connected integration assets, including agents, APIs, Model Context Protocol (MCP) servers, LLM proxies, and gateways. Teams use it to register services, apply governance strategies, monitor runtime health, and optimize costs from one portfolio view instead of working across disconnected tools.

## June 11, 2026

### What’s New

This release includes security updates and improvements to the enhanced MuleSoft experience.

### Fixed Issues

The release addresses these enhanced MuleSoft experience issues:

| Issue Resolution | ID | 
|---|---|
| W-22603005 | |
| Auto-generated MCP tool names no longer contain spaces, ensuring compliance with the MCP specification. | W-22816476 | 
| You can now open service detail pages from the Services catalog while viewing the root Business Group context. | W-22696491 | 
| Governance Insights reports now display policy rulesets and instances correctly. | W-22710201 | 
| The Environment filter on the Gateways catalog page now correctly filters the displayed gateways by the selected environment. | W-22778035 | 
| The Provider filter on portfolio pages (Agents, APIs, MCPs) now correctly returns services associated with the selected provider. | W-22815822 | 
| The Vitest library is upgraded to 4.1.8 to address a reported security vulnerability. | W-22777847 | 
| Automated policies configured at both organization and environment levels now display correctly without duplicated policy activity. | W-22735582 | 
| Policy direction (inbound or outbound) now displays correctly under application methods instead of showing generic instance policy labels. | W-22801826 | 
| A cross-tenant security vulnerability that allowed unauthorized access to Kong gateway plugin configurations across organizations is resolved. | W-22803601 | 
| Public MCP Server and Agent assets no longer allow unmanaged instance creation. | W-22733185 | 
| MCP server provisioning status now updates more reliably while reducing unnecessary refresh cycles. | W-22725529 | 
| Third-party libraries are updated to resolve reported security vulnerabilities. | W-22618670 | 

## May 28, 2026

### What’s New

- 
You can now manage agents, APIs, MCP servers, LLM proxies, and gateways from one portfolio experience, so teams can govern and operate AI integrations without switching between separate tools. For more information, see [Enhanced MuleSoft Experience](learning-map-exp)and[Enhanced MuleSoft Experience Overview](exp-overview).
- 
You can now add services through provider-based discovery or manual registration, so teams can onboard both cloud-managed and custom services faster. For more information, see [Adding Services to Your Portfolio](exp-services-add-to-portfolio),[Create a Scanner for Provider Services](exp-services-connect-providers-to-add), and[Register Services Manually](exp-services-register-manually).
- 
You can now create MCP servers by selecting source systems and publishing tools and resources for MCP clients, so you can more easily expose existing APIs and SaaS systems through MCP workflows. For more information, see [Create an MCP Server](exp-services-create-mcp-server).
- 
You can now add semantic services with Basic and Advanced scale models, so LLM-driven requests route with improved context awareness as traffic grows. For more information, see [Add Semantic Services](exp-services-add-semantic).
- 
You can now apply governance strategies across supported service types, so teams can enforce conformance and cost controls more consistently. For more information, see [Create Governance Strategies](exp-governance-create-strategy)and[View Service Details](exp-services-view-details).
- 
Scanner operations now support lifecycle workflows for running, pausing, editing, and deleting scanners, so provider discovery stays current with less manual overhead. For more information, see [Adding Scanners from Providers](exp-scanners-add-from-providers)and[Managing Scanners](exp-scanners-manage).
- 
Service detail pages now centralize instance creation and management workflows for supported catalogs, so teams can align deployment operations with governance and monitoring workflows. For more information, see [Creating and Managing Instances](exp-instances-add)and[View Service Details](exp-services-view-details).

- 
Monitoring guidance now connects service health, detailed metrics, and token and response analysis, so responders can triage regressions faster. For more information, see [Monitoring Your Services](exp-services-monitoring),[View Detailed Metrics for Your Services](exp-services-view-detailed-metrics), and[Viewing Cost and Token Usage](exp-governance-view-cost-and-token-usage).
- 
You can now access the experience from Anypoint Platform, direct URLs, and supported coding assistants, so teams can work from existing workflow surfaces. For more information, see [Get Started with the Enhanced Experience](exp-home-start)[Connect the Enhanced Experience to Claude Desktop](exp-claude-desktop-connect).
- 
Service detail pages now clarify tab availability by service type, so operators can more easily find instance, governance, and conformance data by catalog. For more information, see [View Service Details](exp-services-view-details).