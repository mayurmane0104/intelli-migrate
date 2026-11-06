# Configuring Instances | MuleSoft Documentation

**Source:** [https://docs.mulesoft.com/exchange/to-configure-api-settings](https://docs.mulesoft.com/exchange/to-configure-api-settings)

---

# Configuring Instances

Use Anypoint Exchange to configure whether instances are public or private in a private Exchange instance or in an Exchange public portal. For example, configure public or private visibility for proxies or policies associated with your asset and set in API Manager.

After you register an API or other assets from Exchange in API Manager, the instances for the asset appear in Exchange in the **Instances** list on the asset details page.

You can also verify agent instances via GoDaddy Agent Naming Service (ANS) during the registration process in API Manager. Implement GoDaddy’s trust layer to verify and secure trusted agents across Anypoint Platform. Verified agents appear in the **Agents & Tools** list and on asset details pages with a verified badge. Managed instances in Exchange show if an agent is verified in the **Instances** list on the asset details page.

Instances for brokers are created in the YAML in Anypoint Code Builder. After the agent network project is published to Exchange, the instances appear in the **Instances** list.

Exchange also declares instances for assets managed by other asset management programs besides Anypoint Platform.

Visibility for each instance is either private or public. Users can see a private instance if the asset is shared with them or if they have an Anypoint Platform permission that grants access. All users accessing an Exchange public portal can see all public instances. All instances in an Exchange public portal are read-only.

In a private Exchange instance, asset administrators have access to change the visibility of instances, and to add, edit, and delete instances.

REST APIs provide a mocking service with data to test API features. The mocking service is always public.

## Configure Non-Managed Instances

Configure assets with instances not managed by API Manager. Add, edit, and delete non-managed instances that are serving AsyncAPIs, GraphQL APIs, REST APIs, HTTP APIs, agents, MCP servers, and LLMs. Add these manually on the asset’s **Instances** page by providing a display name and base URL so developers know where the API is hosted. You can change the name, URL, and visibility of non-managed instances and services.

- 
Add a non-managed instance: - 
Select the asset. 
- 
In the navigation bar, select **Instances**.
- 
Click **Add new instance**.
- 
In the **Non-managed instances**section, enter the instance name and URL.
- 
Select a visibility option and click ![The checkmark icon.](_images/ex-checkmark-icon.png) . .
 
- 
- 
Edit a non-managed instance: - 
Click ![The pencil icon](_images/ex-pencil-icon.png) . .
- 
Make your changes and click ![The checkmark icon](_images/ex-checkmark-icon.png) . .
 
- 
- 
Delete a non-managed instance by clicking ![The trash can icon.](_images/ex-trash-can-icon.png) and then clicking and then clicking**Delete instance**.