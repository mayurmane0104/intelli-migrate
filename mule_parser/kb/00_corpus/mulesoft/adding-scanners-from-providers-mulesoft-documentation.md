# Adding Scanners from Providers | MuleSoft Documentation

**Source:** [https://docs.mulesoft.com/general/exp-scanners-add-from-providers](https://docs.mulesoft.com/general/exp-scanners-add-from-providers)

---

- 
Exchange: Exchange Administrator 
- 
Exchange: Exchange Contributor 
- 
API Manager: API Creator 
- 
API Manager: Manage Policies 

# Adding Scanners from Providers

A scanner is the configured link between the system and a supported cloud provider that lets discovery jobs find services—such as APIs, agents, and MCP servers—and register them in the right **Portfolio** catalogs. Scanners enable automated discovery so your catalogs stay current without manual registration. Configure a scanner once to turn on discovery for a provider, then extend it as your organization adds catalogs or enabled features.

For how provider connection and catalogs fit together, see [Create a Scanner for Provider Services](exp-services-connect-providers-to-add) and [Adding Services to Your Portfolio](exp-services-add-to-portfolio).

## Before You Begin

Before getting started, make sure you have:

- 
An Anypoint Platform account. 
- 
Any of these permissions: For more information, see [Enhanced Experience Permissions](exp-home-start#permissions).

## Benefits of Provider Scanners

- 
Keep catalogs current New and changed services in the provider appear in the system without manually re-entering each registration. 
- 
Centralize visibility Discovered services appear in **Portfolio**where teams can govern, monitor, and deploy from one place.
- 
Stay aligned with the provider Scheduled or on-demand scans pick up releases and configuration drift according to the options your administrator allows. 

## Workflow Entry Points for Adding a Scanner

The system exposes the same underlying connect-and-configure wizard from more than one place; the label depends on context:

- 
**Home**Start from the general **Add Services**area and choose the path that connects a provider and defines a scanner (**Connect to Provider**).
- 
**Providers**Use the area dedicated to provider and scanner management if your navigation includes it. Add or refine scanners alongside other provider work. 
- 
**Portfolio**Open the catalog that matches the service type you want ( **Agents**,**APIs**,**MCP Servers**, and others your tenant supports). Use that catalog’s add control—the label indicates the type (for example**Add API**)—then choose provider connection to scan and discover services to add to that catalog.

Navigation labels can vary by catalog, enabled features, and release.

## Scanner Configuration Overview

Regardless of entry point, adding a scanner establishes trust and scope. You specify which provider platform to reach, how the system authenticates, and how you validate connectivity. You also name and schedule the scanner—or configure another trigger—so discovery runs on the cadence your team expects. Saving the configuration activates the scanner for the catalogs and features your administrator enabled.

## After the Scanner Runs

When the scanner is active, it applies discovery results according to its settings and your organization’s rules. You review outcomes on the **Providers** page and on scanner detail pages, and you manage discovered services from the relevant **Portfolio** catalogs.

For ongoing operations (pause, edit, or delete), see [Managing Scanners](exp-scanners-manage).