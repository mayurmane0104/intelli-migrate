# https://docs.mulesoft.com/general/exp-services-add-semantic.md

**Source:** [https://docs.mulesoft.com/general/exp-services-add-semantic.md](https://docs.mulesoft.com/general/exp-services-add-semantic.md)

---

```
# Add Semantic Services
> For the full documentation index, see: https://docs.mulesoft.com/llms.txt
Semantic services improve how the system interprets and routes LLM-driven requests across your
portfolio. They apply context-aware behavior so the system directs requests to the most relevant
tools, services, or pathways configured in your organization.
Use this capability when workflows need more than static routing. With semantic context in place,
the system supports better request matching, more consistent response behavior, and stronger control
as usage grows across agents, APIs, MCP servers, and related integrations.
To add semantic services, follow these steps:
1.  Define the semantic service your organization uses for contextual matching.
2.  Associate that semantic capability with the relevant Enhanced Experience flow (for example,
    supported LLM routing paths).
3.  Operate the service as part of your broader governance and monitoring model so behavior remains
    reliable as traffic and use cases evolve.
## Before You Begin
Before getting started, make sure you have:
- An Anypoint Platform account.
- One of these permissions:
  - Exchange: Exchange Contributor
  - Exchange: Exchange Administrator
  - Exchange: Exchange Creator
  For more information, see [Enhanced Experience Permissions](exp-home-start#permissions).
## Create a Semantic Service
1.  In the navigation, under **Portfolio**, expand **LLM Proxies**, and select **Semantic
    Services**.
2.  Select **Add Semantic Service**.
3.  Select the scale model that matches your traffic profile and operational needs.
    - **Basic scale**
      Choose **Basic scale** for smaller topic sets (up to 6 topics and 10 utterances per topic).
      This scale is managed through an internal LLM proxy configuration.
    - **Advanced scale**
      Choose **Advanced scale** for larger utterance sets per topic. This scale requires a dedicated
      external vector database connection.
## Configure Semantic Service Fields
Basic and Advanced scales use the same setup fields. Provide values for:
- **Environment**
- **Embedding service provider**
- **Service label**
- **URL**
- **Model**
- **Auth key**
For **Advanced scale**, also configure the dedicated external vector database connection required by
your selected provider.
## See Also
- [Adding Services to Your Portfolio](exp-services-add-to-portfolio)
- [View Service Details](exp-services-view-details)
- [Monitoring Your Services](exp-services-monitoring)
```