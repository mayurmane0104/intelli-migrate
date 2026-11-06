# https://docs.mulesoft.com/exchange/importing-agentforce-agents.md

**Source:** [https://docs.mulesoft.com/exchange/importing-agentforce-agents.md](https://docs.mulesoft.com/exchange/importing-agentforce-agents.md)

---

```
# Importing Agentforce Agents
> For the full documentation index, see: https://docs.mulesoft.com/llms.txt
Organizations can import their Agentforce agents into Exchange to include them in business groups.
Importing from the same Salesforce organization into a different business group can create duplicate
assets in Exchange.
Imported Agentforce agents appear in **Agents & Tools**.
## Before You Begin
Before importing Agentforce agents, complete these requirements:
- [Enable the connection to a Salesforce organization](../access-management/managing-connected-salesforce-orgs#enable-disable-connection)
  that has an established tenant relationship with your Anypoint Platform organization.
- [Enable Einstein in Anypoint Platform](../access-management/enabling-agentforce)
  Accept the terms and conditions and set a default organization for Einstein.
## Import Agentforce Agents
1.  Select **Settings** from the sidebar and then select the **Asset Import** tab.
2.  Click **Import Agents** and then click **Confirm**.
    Agents are imported in the current business group.
3.  Close the dialog and refresh the page after a few minutes.
4.  Verify that the Agentforce agents are listed in the Exchange catalog on the **Agents & Tools**
    page.
```