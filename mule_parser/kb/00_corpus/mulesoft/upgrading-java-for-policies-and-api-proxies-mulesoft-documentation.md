# Upgrading Java for Policies and API Proxies | MuleSoft Documentation

**Source:** [https://docs.mulesoft.com/general/upgrade-policies-proxies](https://docs.mulesoft.com/general/upgrade-policies-proxies)

---

# Upgrading Java for Policies and API Proxies

Upgrade your policies and API proxies to be compatible with Java 17.

## Upgrading Automated Policies

Upgrade your automated policies (included and custom) to Java 17.

### Upgrading Included Automated Policies

To upgrade automated [MuleSoft included policies](../mule-gateway/policies-included-directory) to Java 17:

- 
In API Manager, go to **Automated Policies**.
- 
In **Policy version**, select the latest version of the included policy.
- 
In **Rule of application**:- 
If your policy is on the latest version: - 
To apply included policies to all Mule runtimes, select **All runtimes**and click**Apply**.
- 
To apply the included policies to Omni Gateways only, select **Omni gateways only**and click**Apply**.
- 
To apply the included policies to Mule Gateways only: - 
Select **Mule gateways only**.
- 
In **From version**and**To**, enter the Mule version range.
- 
In **Java Versions**, select**All Java versions**or**Choose specific Java versions**.
- 
Click **Apply**.
 
- 
 
- 
- 
If your policy is not on the latest version: - 
To apply included policies to all Mule runtimes, select **All runtimes**and click**Apply**.
- 
To apply the included policies to Omni Gateways only, select **Omni gateways only**and click**Apply**. Note that the**Rule of application**section must be the same as the**Rule of application**section in the latest version or else you might have unprotected APIs.
- 
To apply the included policies to Mule Gateways only: - 
Select **Mule gateways only**.
- 
In **From version**and**To**, enter the Mule version range.
- 
In **Java versions**, select**Choose specific Java versions**and select Java 8 and Java 11.
- 
Click **Apply**.
- 
Click **Add automated policy**and add the same automated policy.
- 
Click **Advanced options**.
- 
Select **Mule gateways only**.
- 
In **From version**and**To**, enter the Mule version range.
- 
In **Java versions**, select**Choose specific Java versions**and select Java 17.
- 
Click **Apply**.
 
- 
 
- 
 
- 

### Upgrading Custom Automated Policies

To upgrade custom automated policies to Java 17:

- 
In API Manager, go to **Automated Policies**.
- 
Upgrade the required extensions and connectors to Java 17. - 
If your custom policy has Anypoint Connectors, see [Upgrading Anypoint Connectors and Modules](java-support#anypoint-connectors-and-modules).
- 
If your custom policy has custom connectors, see [Upgrading Custom Connectors](java-support#custom-connectors).
 
- 
- 
Configure Java 17 locally to make custom policies compatible with Java 17. 
- 
Apply the new version of the custom policy that is compatible with Java 17 to the API instance: - 
Go to **Policies**.
- 
In **Applied policy status**, verify that the latest definition is applied.- 
If the latest definition is applied, click on the More (…) menu and select **Check for implementation updates**.
- 
If the latest definition is not applied, update to the latest definition. 
 
- 
 
- 

## Upgrading API-Level Policies

Upgrade your API-level policies (included and custom) to Java 17.

### Upgrading Included API-Level Policies

To upgrade API-level [MuleSoft included policies](../mule-gateway/policies-included-directory) to Java 17:

- 
In API Manager, go to **API Administration**>**{API Name}**>**Policies**>**Add a policy**to[apply policies](../mule-gateway/policies-included-apply)at the individual API level.
- 
Upgrade each of your API-level policies: - 
In **Policy version**, select the latest version of the included policy.
- 
In **Method & resource conditions**, select either**Apply configuration to all API method & resources**or**Apply configuration to specific API method & resources**.
- 
Click **Apply**.
 
- 

### Upgrading Custom API-level Policies

To upgrade custom API-level policies to Java 17:

- 
In API Manager, go to **API Administration**>**{API Name}**>**Policies**>**Add a policy**to[apply policies](../mule-gateway/policies-included-apply)at the individual API level.
- 
Upgrade the required extensions and connectors to Java 17. - 
If your custom policy has Anypoint Connectors, see [Upgrading Anypoint Connectors and Modules](java-support#anypoint-connectors-and-modules).
- 
If your custom policy has custom connectors, see [Upgrading Custom Connectors](java-support#custom-connectors).
 
- 
- 
Configure Java 17 locally to make custom policies compatible with Java 17. 
- 
Apply the new version of the custom policy that is compatible with Java 17 to the API instance: - 
Go to **Policies**.
- 
In **Applied policy status**, verify that the latest definition is applied.- 
If the latest definition is applied, click on the More (…) menu and select **Check for implementation updates**.
- 
If the latest definition is not applied, update to the latest definition. 
 
- 
 
- 

## Upgrading API Proxies

| To ensure your API proxies or Mule apps are protected when upgrading, upgrade your API policies beforeupgrading your API proxies or Mule apps. | 

The steps to upgrade are a little different, depending on your **Proxy type**:

- 
Basic endpoint: - 
If you use Basic endpoint, deploy the adapted application to the server from Mule runtime and connect it to API Manager using autodiscovery. For more information, see [Configuring Mule Gateway API Autodiscovery in a Mule 4 Application](../mule-gateway/mule-gateway-config-autodiscovery-mule4).
- 
If you use a Basic endpoint API instance to update your instance, update the Mule application connecting to your API instance. 
 
- 
- 
If you use a proxy application, see the following sections for deployment type: 

### CloudHub and CloudHub 2.0 Deployments

Before following these steps, ensure your policies are updated. For more information, see [Upgrading Automated Policies](#upgrading-automated-policies) and [Upgrading API-Level Policies](#upgrading-api-level-policies).

- 
In API Manager, go to **API Administration > Settings**.
- 
[Edit the API instance’s configuration settings](../api-manager/latest/edit-api-endpoint-task):- 
In **Runtime Channel**, select the runtime channel to use.
- 
In **Version**, select**4.6.0**or later.
- 
In **Java version**, select**Java 17**.
 
- 
- 
Click **Save & Apply**.

### Hybrid Deployments

Before following these steps, ensure your policies are updated. For more information, see [Upgrading Automated Policies](#upgrading-automated-policies) and [Upgrading API-Level Policies](#upgrading-api-level-policies).

- 
Deploy Mule runtime engine 4.6.x in a new server running on Java 17 and start the server. For more information, see [Add Servers to Runtime Manager](../runtime-manager/servers-create).
- 
Select the new target you created running on Java 17 and, in API Manager, go to **API Administration > Settings**.
- 
[Edit the API instance’s configuration settings](../api-manager/latest/edit-api-endpoint-task):- 
In **Select target**, select the server running on Java 17 as the target.
 
- 
- 
Click **Save & Apply**.
- 
After the server successfully runs on Java 17, shift your traffic gradually to the new server using a load balancer and turn off the old server after all of its apps are migrated. 

### Runtime Fabric Deployments

Before following these steps, ensure your policies are updated. For more information, see [Upgrading Automated Policies](#upgrading-automated-policies) and [Upgrading API-Level Policies](#upgrading-api-level-policies).

- 
Deploy Mule runtime engine 4.6.x in a new server running on Java 17 and start the server. For more information, see [Deploying API Proxies to Runtime Fabric](../runtime-fabric/latest/proxy-deploy-runtime-fabric).
- 
Select the new target you created running on Java 17 and, in API Manager, go to **API Administration > Settings**.
- 
[Edit the API instance’s configuration settings](../api-manager/latest/edit-api-endpoint-task):- 
In **Runtime Channel**, select the runtime channel to use.
- 
In **Version**, select**4.6.0**or later.
- 
In **Java version**, select**Java 17**.
 
- 
- 
Click **Save & Apply**.
- 
After the server successfully runs on Java 17, shift your traffic gradually to the new server using a load balancer and turn off the old server after all of its apps are migrated.