# Enabling or Disabling Agentforce for Anypoint Platform | MuleSoft Documentation

**Source:** [https://docs.mulesoft.com/access-management/enabling-agentforce](https://docs.mulesoft.com/access-management/enabling-agentforce)

---

# Enabling or Disabling Agentforce for Anypoint Platform

Connect a trusted Salesforce organization and enable Agentforce (formerly Einstein) for your Anypoint Platform organization. Enabling Agentforce unlocks AI assistance across supported MuleSoft products while routing tracking and billing through Salesforce. Administrators can grant user permissions and set the default Salesforce organization used by Agentforce.

As an organization administrator, you can assign permission to the users in your organization so they can use Agentforce with Anypoint Platform products that have Agentforce capabilities, including:

- 
Anypoint Code Builder 
- 
Anypoint Exchange 
- 
Intelligent Document Processing (IDP) 

## Before You Begin

Before enabling Agentforce in your Anypoint Platform organization, you must:

- 
Have administrative access to an Anypoint Platform organization that isn’t a trial organization and isn’t expired. 
- 
Have the root Organization Administrator permission and role. 
- 
Have administrative access to a Salesforce organization that [has Agentforce enabled](https://help.salesforce.com/s/articleView?id=ai.generative_ai_enable.htm&type=5).
- 
[Establish a tenant relationship](trusted-salesforce-org)between your Anypoint Platform organization and a trusted Salesforce organization.

## Enable Agentforce in the Salesforce Organization

When the Salesforce administrator enables Agentforce for the connected Anypoint Platform organization, the connected Salesforce organization routes the Agentforce requests. The Salesforce organization handles tracking and billing.

- 
Log in to your Salesforce organization. 
- 
In Salesforce Setup, enter `MuleSoft`in the**Quick Find**box, then select**MuleSoft > Anypoint Platform Setup**.
- 
In **Your connected Anypoint Platform Organization**, select**Complete Connection**.
- 
In **Connection to MuleSoft Anypoint Platform**, switch between**Enabled**or**Disabled**in**Enable Agentforce for MuleSoft Anypoint Platform**.
- 
Click **Close**.After enabling Agentforce in the Salesforce organization, you see **Enabled in Salesforce**in Anypoint Platform for the connected Salesforce organization.

## Enable Agentforce for Your Anypoint Platform Organization

When Agentforce is enabled in Anypoint Platform through a connected Salesforce organization, any Anypoint Platform feature in that organization that supports Agentforce is enabled to use it.

- 
Sign in to Anypoint Platform using an account that has the Organization Administrator permission. 
- 
Select **Access Management**from themenu. 
- 
Select **Salesforce**.
- 
In **Enable Agentforce for Anypoint Platform**, select**Accept**.
- 
Accept the terms and conditions. The **Salesforce Orgs**section shows the orgs with[established tenant relationships](connecting-salesforce-orgs)with your Anypoint Platform organization.Each Salesforce organization shows the enabled and disabled Anypoint Platform capabilities. 
- 
Select the Salesforce organization to use by default in your Anypoint Platform organization: - 
Select **Settings**in**Enhance Anypoint Platform with Agentforce**.
- 
In **Agentforce for Anypoint Platform Setting**, select the Salesforce organization and select**Save**.
 
- 

## Add the Agentforce Permissions for Users

When Agentforce is enabled for your Anypoint Platform organization, organization administrators are granted the required Agentforce permission automatically.

To enable Agentforce for users in your organization, assign the required permissions manually.

- 
Sign in to Anypoint Platform using an account that has the Organization Administrator permission. 
- 
Select **Access Management**from themenu. 
- 
[Create a team](configure-teams)for the users you are enabling to use Agentforce.
- 
Select the **Permissions**tab.
- 
In **Permissions**, select**Add permissions**.
- 
Select the **Anypoint Code Builder > Mule Developer Generative AI User**permission and select**Next**.
- 
Select the business groups to apply the permissions to. Select which environments to apply the permission to if it’s enabled for the permission. 
- 
Select **Next**.
- 
Review the permissions and the business groups and environments they apply to, and then select **Add Permissions**.

## Disable Agentforce

When you disable Agentforce for your Anypoint Platform organization, none of the users in your organization can use Agentforce in any of the features where it’s enabled.

- 
Sign in to Anypoint Platform using an account that has the Organization Administrator permission. 
- 
Select **Access Management**from themenu. 
- 
Select **Salesforce**.
- 
In the **Capabilities managed in Salesforce**section, switch Agentforce to**Disabled**.