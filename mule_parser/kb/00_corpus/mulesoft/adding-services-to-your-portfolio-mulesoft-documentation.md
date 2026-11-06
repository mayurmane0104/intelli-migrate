# Adding Services to Your Portfolio | MuleSoft Documentation

**Source:** [https://docs.mulesoft.com/general/exp-services-add-to-portfolio](https://docs.mulesoft.com/general/exp-services-add-to-portfolio)

---

- 
Exchange: Exchange Contributor 
- 
Exchange: Exchange Administrator 
- 
Exchange: Exchange Creator 

# Adding Services to Your Portfolio

Your **Portfolio** is organized into catalogs: **Agents**, **MCP Servers**, **LLM Proxies**, **APIs**, and **Gateways**. Each catalog holds the services (or gateway entries) your organization registered or imported for governance, monitoring, and deployment. Services enter a catalog through automated provider discovery or manual registration. For procedures, use the topics linked in each section.

| Approach | What Happens | 
|---|---|
| You add a provider scanner from  | |
| You start an  | 

Gateway creation starts in Anypoint Platform, which you can open from the Enhanced Experience.

## Before You Begin

Before getting started, make sure you have:

- 
An Anypoint Platform account. 
- 
One of these permissions: For more information, see [Enhanced Experience Permissions](exp-home-start#permissions).

## Workflow Entry Points

- 
**Home**Use **Add Services**to open provider connection or manual registration, then select the service type.
- 
**Portfolio**Open the **Agents**,**MCP Servers**,**LLM Proxies**,**APIs**, or**Gateways**catalog. Use the add control for that type (for example,**Add API**or**Add Agent**), then select the available flow. For gateways,**Add Gateway**opens gateway creation in Anypoint Platform.

Navigation labels can vary by catalog, enabled features, and release.

## Service Type Registration Options

- **Agents**
- 
Register by uploading an agent card or connect an agent provider scanner for discovery. 
- **MCP Servers**
- 
Register with an MCP URL or a schema file, or connect an MCP server provider. 
- **LLM Proxies**
- 
Register manually by creating an LLM proxy with a routing strategy that routes requests by provider or semantically. 
- **APIs**
- 
Register with an API specification, or connect an API provider so scans import APIs into the **APIs**catalog.
- **Gateways**
- 
Create gateways in Anypoint Platform. In Enhanced Experience, select **Add Gateway**to open the Anypoint gateway creation flow.

For more information about registering any of these types, see [Register Services Manually](exp-services-register-manually) and [Create a Scanner for Provider Services](exp-services-connect-providers-to-add).