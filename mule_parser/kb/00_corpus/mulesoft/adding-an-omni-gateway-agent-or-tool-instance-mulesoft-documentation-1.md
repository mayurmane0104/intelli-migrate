# Adding an Omni Gateway Agent or Tool Instance | MuleSoft Documentation

**Source:** [https://docs.mulesoft.com/api-manager/latest/create-instance-task-agent-tool](https://docs.mulesoft.com/api-manager/latest/create-instance-task-agent-tool)

---

| Field Name | Description | Required | Notes | 
|---|---|---|---|
| 
 | Specifies the URL prefix for all instance paths, relative to the host root. It must start with a leading slash  | Yes | |
| 
 | Specifies a client provider for the instance. | No | Anypoint Platform acts as the client provider by default. To configure an external client provider, see  | 
| 
 | Specifies a label for the instance. | No | If you have multiple managed instances of the same asset, add a label to differentiate each instance from the others. | 
| 
 | |||
| 
 | Specifies a proxy application’s address for consumers to use for sending requests. | No | 

# Adding an Omni Gateway Agent or Tool Instance

Use Omni Gateway for any agent, broker, LLM, or MCP server that needs a flexible and performant gateway that works with distributed and microservices environments and fits into your CI/CD environments.

This diagram shows the upstream and downstream configurations of the instance. In this configuration, the downstream service is the service making requests that are completed by the upstream service. These terms represent the direction of dependency, not the direction of information.

![The instance is deployed on a gateway between the upstream and downstream configuration](_images/server-upstream-downstream-config.png)


## Add a New Agent or Tool Instance

To add and manage server instances for Omni Gateway, use the **Agent and Tool Instances** section in API Manager.
These server instances can represent Agents, MCP servers, or LLM servers that extend Omni Gateway functionality.

- 
Navigate to **Anypoint Platform**>**API Manager**.
- 
Click **Agent and Tool Instances**.
- 
Click **Add**and select the protocol:**Agent**,**MCP Server**, or**LLM**.
- 
Select an Omni Gateway to deploy the server instance to from **Select a gateway**.If you don’t see an Omni Gateway listed, or you see an Omni Gateway but its status is **Not Running**, See[Install Omni Gateway](../../gateway/latest/flex-install)and[Register and Run in Connected Mode](../../gateway/latest/flex-conn-reg-run)for more information.
- 
Click **Next**.
- 
Select an instance: - 
**Select asset from Exchange**: To manage an agent or tool asset shared through Exchange.- 
Select the asset from **Select asset**. You can also search for an asset.
 
- 
- 
**Create a new asset**: To create a new asset.- 
In **Asset name**, enter a name for the new asset.Your asset is published to Exchange after it’s protected. 
 
- 
 
- 
- 
Click **Next**.
- 
Configure the downstream configuration settings: ## Managed Omni Gateway## Self-Managed Omni Gateway (Connected Mode)Field Name Description Required Notes **Protocol**Specifies whether to use HTTP or HTTPS. Yes If you select HTTPS, specify a TLS context for inbound traffic. **Inbound TLS**TLS Context used for the inbound HTTPS traffic. No [Configure a TLS Context for Omni Gateway](../../gateway/latest/flex-conn-tls-config)before adding a TLS Context to your server.**Port**Specifies the number to use if the displayed port is incorrect. No Instances can share the same port across the same target if the **Base path**is different for both instances.**Base path**Specifies the URL prefix for all server paths, relative to the host root. It must start with a leading slash `/`.Yes **Instance label**Specifies a label for the instance. No If you have multiple managed instances of the same asset, add a label to differentiate each instance from the others. **Advanced Options****Consumer endpoint**Specifies a proxy application’s address for consumers to use for sending requests. No 
- 
Click **Next**.
- 
Configure one of the server upstream configurations: Field Name Description Required Notes **Upstream URL**URL to access for the upstream service. This must end with a `/`.Yes For example, you can use the URL of your asset in Exchange. **Outbound TLS**TLS Context used for the outbound traffic to the upstream service No [Configure a TLS Context for Omni Gateway](../../gateway/latest/flex-conn-tls-config)before adding a TLS Context to your server.
- 
Click **Next**.
- 
Review your selections and edit them if necessary. 
- 
If you are ready to deploy, click **Save & Deploy**. Otherwise, you can select**Save**, to save the instance and deploy it at a later time.== Edit Agent Network Project Instances 

Some instances in **Agent and Tool Instances** can be created by supplying a YAML file in an agent network project. For instances created with the YAML file, the YAML file is treated as the source of truth. If you edit the instance in API Manager (for example, to add policies), the changes are reverted to the YAML file when the instance is redeployed from the agent network project.

To ensure changes to instances created from a YAML source are present after redeployment, edit the YAML source.

For more information, see [Define Your Agent Network Specification](../../anypoint-code-builder/af-define-your-agent-network-specification).