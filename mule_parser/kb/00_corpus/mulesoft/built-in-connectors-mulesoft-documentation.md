# Built-In Connectors | MuleSoft Documentation

**Source:** [https://docs.mulesoft.com/anypoint-code-builder/ref-connectors](https://docs.mulesoft.com/anypoint-code-builder/ref-connectors)

---

# Built-In Connectors

Anypoint connectors and modules are extensions to Mule runtime engine that process event data within a Mule application. Connectors, unlike modules, also provide ways to connect to external systems or services.

In Anypoint Code Builder, both integrations and implementations are Mule applications.

Anypoint connectors and modules are extensions to Mule runtime engine that process event data within a Mule application. Connectors, unlike modules, also provide ways to connect to external systems or services.

Built-in Anypoint connectors are available from the canvas and code editor for integration and implementation projects. These connectors include:

- 
[Anypoint Connector for Agent2Agent (A2A) (Beta) (<a2a:/>)](../a2a-connector/latest/)(A2A Connector)
- 
[Anypoint Connector for Agentforce (<ms-agentforce:/>)](../agentforce-connector/latest/)(Agentforce Connector)
- 
[Anypoint Connector for Database (<db:/>)](../db-connector/latest/)(Database Connector)
- 
[Anypoint Connector for Einstein AI (<ms-einstein-ai:/>)](../einstein-ai-connector/latest/)(Einstein AI Connector)
- 
[Anypoint Connector for Email (<email:/>)](../email-connector/latest/)(Email Connector)
- 
[Anypoint Connector for File (<file:/>)](../file-connector/latest/)(File Connector)
- 
[Anypoint Connector for HTTP (<http:/>)](../http-connector/latest/)(HTTP Connector)
- 
[Anypoint Connector for Salesforce (<salesforce:/>)](../salesforce-connector/latest/)(Salesforce Connector)
- 
[Anypoint Connector for Salesforce Data Cloud (<sdc:/>)](../salesforce-data-cloud-connector/latest/)(Salesforce Data Cloud Connector)
- 
[Anypoint Connector for Sockets (<sockets:/>)](../sockets-connector/latest/)(Sockets Connector)
- 
[Anypoint Connector for Workday (<workday:/>)](../workday-connector/latest/)(Workday Connector)

Connector XML tags start with a namespace followed by an operation, following the syntax `namespace:operation`, such as `<db:select/>` for a Select operation in Anypoint Connector for Database (Database Connector).
For more information, see [Using Anypoint Code Builder to Configure a Connector](../connectors/introduction/intro-config-use-acb).

Many other connectors are available from your Anypoint Code Builder IDE through Anypoint Exchange:

- 
US cloud (non-EU host): [Exchange (US)](https://anypoint.mulesoft.com/exchange/)
- 
EU cloud (EU host): [Exchange (EU)](https://eu1.anypoint.mulesoft.com/exchange/)

To find information about more connectors, see [Anypoint Connectors Overview](../connectors/introduction/introduction-to-anypoint-connectors), and find documentation on all [Anypoint connectors and modules](../connectors/).