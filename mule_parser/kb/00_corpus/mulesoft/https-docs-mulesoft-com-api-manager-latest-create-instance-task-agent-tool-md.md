# https://docs.mulesoft.com/api-manager/latest/create-instance-task-agent-tool.md

**Source:** [https://docs.mulesoft.com/api-manager/latest/create-instance-task-agent-tool.md](https://docs.mulesoft.com/api-manager/latest/create-instance-task-agent-tool.md)

---

```
# Adding an Omni Gateway Agent or Tool Instance
> For the full documentation index, see: https://docs.mulesoft.com/llms.txt
Use Omni Gateway for any agent, broker, LLM, or MCP server that needs a flexible and performant
gateway that works with distributed and microservices environments and fits into your CI/CD
environments.
This diagram shows the upstream and downstream configurations of the instance. In this
configuration, the downstream service is the service making requests that are completed by the
upstream service. These terms represent the direction of dependency, not the direction of
information.
![The instance is deployed on a gateway between the upstream and downstream configuration](_images/server-upstream-downstream-config.png)
## Add a New Agent or Tool Instance
To add and manage server instances for Omni Gateway, use the **Agent and Tool Instances** section in
API Manager. These server instances can represent Agents, MCP servers, or LLM servers that extend
Omni Gateway functionality.
1.  Navigate to **Anypoint Platform** > **API Manager**.
2.  Click **Agent and Tool Instances**.
3.  Click **Add** and select the protocol: **Agent**, **MCP Server**, or **LLM**.
4.  Select an Omni Gateway to deploy the server instance to from **Select a gateway**.
    > [!NOTE] If you donâ€™t see an Omni Gateway listed, or you see an Omni Gateway but its status is
    > **Not Running**, See [Install Omni Gateway](../../gateway/latest/flex-install) and
    > [Register and Run in Connected Mode](../../gateway/latest/flex-conn-reg-run) for more
    > information.
5.  Click **Next**.
6.  Select an instance:
    - **Select asset from Exchange**: To manage an agent or tool asset shared through Exchange.
      - Select the asset from **Select asset**. You can also search for an asset.
    - **Create a new asset**: To create a new asset.
      - In **Asset name**, enter a name for the new asset.
        > [!NOTE] Your asset is published to Exchange after itâ€™s protected.
7.  Click **Next**.
8.  Configure the downstream configuration settings:
    Managed Omni Gateway
    <table><colgroup><col> <col> <col> <col></colgroup><thead><tr><th>Field Name</th><th>Description</th><th>Required</th><th>Notes</th></tr></thead><tbody><tr><td><p><strong>Base path</strong></p></td><td><p>Specifies the URL prefix for all instance paths, relative to the host root. It must start with a leading slash <code>/</code>.</p></td><td><p>Yes</p></td><td></td></tr><tr><td><p><strong>Client provider</strong></p></td><td><p>Specifies a client provider for the instance.</p></td><td><p>No</p></td><td><p>Anypoint Platform acts as the client provider by default. To configure an external client provider, see <a href="../../access-management/managing-api-clients">Client Providers</a>.</p></td></tr><tr><td><p><strong>Instance label</strong></p></td><td><p>Specifies a label for the instance.</p></td><td><p>No</p></td><td><p>If you have multiple managed instances of the same asset, add a label to differentiate each instance from the others.</p></td></tr><tr><td><p><strong>Advanced Options</strong></p></td><td></td><td></td><td></td></tr><tr><td><p><strong>Consumer endpoint</strong></p></td><td><p>Specifies a proxy applicationâ€™s address for consumers to use for sending requests.</p></td><td><p>No</p></td><td></td></tr></tbody></table>
    Self-Managed Omni Gateway (Connected Mode)
    <table><colgroup><col> <col> <col> <col></colgroup><thead><tr><th>Field Name</th><th>Description</th><th>Required</th><th>Notes</th></tr></thead><tbody><tr><td><p><strong>Protocol</strong></p></td><td><p>Specifies whether to use HTTP or HTTPS.</p></td><td><p>Yes</p></td><td><p>If you select HTTPS, specify a TLS context for inbound traffic.</p></td></tr><tr><td><p><strong>Inbound TLS</strong></p></td><td><p>TLS Context used for the inbound HTTPS traffic.</p></td><td><p>No</p></td><td><p><a href="../../gateway/latest/flex-conn-tls-config">Configure a TLS Context for Omni Gateway</a> before adding a TLS Context to your server.</p></td></tr><tr><td><p><strong>Port</strong></p></td><td><p>Specifies the number to use if the displayed port is incorrect.</p></td><td><p>No</p></td><td><p>Instances can share the same port across the same target if the <strong>Base path</strong> is different for both instances.</p></td></tr><tr><td><p><strong>Base path</strong></p></td><td><p>Specifies the URL prefix for all server paths, relative to the host root. It must start with a leading slash <code>/</code>.</p></td><td><p>Yes</p></td><td></td></tr><tr><td><p><strong>Instance label</strong></p></td><td><p>Specifies a label for the instance.</p></td><td><p>No</p></td><td><p>If you have multiple managed instances of the same asset, add a label to differentiate each instance from the others.</p></td></tr><tr><td><p><strong>Advanced Options</strong></p></td><td></td><td></td><td></td></tr><tr><td><p><strong>Consumer endpoint</strong></p></td><td><p>Specifies a proxy applicationâ€™s address for consumers to use for sending requests.</p></td><td><p>No</p></td><td></td></tr></tbody></table>
9.  Click **Next**.
10. Configure one of the server upstream configurations:
    <table><colgroup><col> <col> <col> <col></colgroup><thead><tr><th>Field Name</th><th>Description</th><th>Required</th><th>Notes</th></tr></thead><tbody><tr><td><p><strong>Upstream URL</strong></p></td><td><p>URL to access for the upstream service. This must end with a <code>/</code>.</p></td><td><p>Yes</p></td><td><p>For example, you can use the URL of your asset in Exchange.</p></td></tr><tr><td><p><strong>Outbound TLS</strong></p></td><td><p>TLS Context used for the outbound traffic to the upstream service</p></td><td><p>No</p></td><td><p><a href="../../gateway/latest/flex-conn-tls-config">Configure a TLS Context for Omni Gateway</a> before adding a TLS Context to your server.</p></td></tr></tbody></table>
11. Click **Next**.
12. Review your selections and edit them if necessary.
13. If you are ready to deploy, click **Save & Deploy**. Otherwise, you can select **Save**, to save
    the instance and deploy it at a later time.
    \== Edit Agent Network Project Instances
Some instances in **Agent and Tool Instances** can be created by supplying a YAML file in an agent
network project. For instances created with the YAML file, the YAML file is treated as the source of
truth. If you edit the instance in API Manager (for example, to add policies), the changes are
reverted to the YAML file when the instance is redeployed from the agent network project.
To ensure changes to instances created from a YAML source are present after redeployment, edit the
YAML source.
For more information, see
[Define Your Agent Network Specification](../../anypoint-code-builder/af-define-your-agent-network-specification).
## See Also
- [API Manager Overview](latest-overview-concept)
- [Define Your Agent Network Specification](../../anypoint-code-builder/af-define-your-agent-network-specification)
- [Downloading Omni Gateway](../../gateway/latest/flex-install)
- [Registering and Running Omni Gateway in Connected Mode](../../gateway/latest/flex-conn-reg-run)
```