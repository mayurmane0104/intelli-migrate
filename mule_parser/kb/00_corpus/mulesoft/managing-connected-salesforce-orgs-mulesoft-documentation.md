# Managing Connected Salesforce Orgs | MuleSoft Documentation

**Source:** [https://docs.mulesoft.com/access-management/managing-connected-salesforce-orgs](https://docs.mulesoft.com/access-management/managing-connected-salesforce-orgs)

---

# Managing Connected Salesforce Orgs

As an Anypoint Platform organization administrator, you can enable, remove, and repair connections, and edit the name of Salesforce organizations.

## Enable the Connection in Anypoint Platform

Enable the connection to a Salesforce organization that has an established tenant relationship with your Anypoint Platform organization.

| Tenant relationships that are automatically provisioned for your Anypoint Platform organization are disabled until you enable them. | 

You can’t publish assets from Anypoint Platform to the Salesforce organization or use any of the other features associated with the connected Salesforce organization until the connection is enabled.

- 
Sign in to Anypoint Platform using an account that has the root Organization Administrator permission. 
- 
Select **Access Management**from themenu. 
- 
Select **Salesforce**.If your organization has at least one established tenant relationship with a Salesforce organization, a list of Salesforce orgs appears, showing the name, organization ID, and status of the tenant relationship connection. 
- 
Click the **Actions**menu (**…**) in the Salesforce organization to enable and select**Enable Org**.
- 
In **Enable Salesforce Org**, click**Enable**.

## Remove the Connection Between Anypoint Platform and Salesforce Organizations

When you remove the connection between your Anypoint Platform organization and Salesforce organization, the Salesforce organization no longer appears in the list of connected organizations. The connection still exists in the Salesforce organization until it’s removed by the Salesforce organization administrator.

To reestablish the connection between Anypoint Platform and removed Salesforce organizations, administrators with the appropriate permissions in both Anypoint Platform and Salesforce organizations must recreate the connection.

### Remove a Connected Salesforce Org in Anypoint Platform

An Anypoint Platform organization administrator can remove the connection between their Anypoint Platform organization and a connected Salesforce organization.

When you remove a connection to a Salesforce organization, any capabilities associated with the Salesforce organization are removed.

To remove the connection to a Salesforce organization:

- 
Sign in to Anypoint Platform using an account that has the root Organization Administrator permission. 
- 
Select **Access Management**from themenu. 
- 
Select **Salesforce**.
- 
Click the **Actions**menu (**…**) in the Salesforce organization to remove the connection from and select**Remove Salesforce Org**.
- 
In **Remove Salesforce Org**, click**Remove Org**.

### Remove a Connected Anypoint Platform Organization in Salesforce

A Salesforce organization administrator can remove the connection between an Anypoint Platform organization and Salesforce organization using the Salesforce user interface.

To remove the connection to an Anypoint Platform organization in Salesforce:

- 
Log in to your Salesforce organization with your admin credentials. 
- 
Go to **Setup**.![Salesforce Setup menu with Setup selected](_images/salesforce-setup.png) 
- 
From **Setup**, in the Quick Find box, enter`MuleSoft`, and then select**MuleSoft > Anypoint Platform Setup**.
- 
In **Your connected Anypoint Platform Organization**, click**View Connection Info**.
- 
From **Go To Anypoint**, select**Remove connection**.
- 
In **Remove connection to Anypoint Platform**, click**OK**.

Alternatively, to temporarily prevent Anypoint Platform users from publishing assets to Salesforce from the Anypoint Platform side, you can [disable](#enable-disable-connection) the connection temporarily instead.

For more information about managing this relationship from the Salesforce user interface, see the [Salesforce documentation](https://help.salesforce.com/s/articleView?id=platform.external_services_manage_your_mulesoft_anypoint_platform_connection.htm&type=5).

## Repair the Connection to a Salesforce Organization

If the Salesforce **My Domain** is changed in the connected Salesforce organization, you can rediscover the Salesforce organization and repair the connection.

- 
Sign in to Anypoint Platform using an account that has the root Organization Administrator permission. 
- 
Select **Access Management**from themenu. 
- 
Select **Salesforce**.
- 
Click the **Actions**menu (**…**) in the Salesforce organization and select**Repair Org Info**.
- 
Click **Repair**to rediscover the Salesforce organization.

## Edit the Salesforce Organization Name

You can edit the Salesforce organization display name in your Anypoint Platform organization. The name of the Salesforce organization within Salesforce remains the same.

To edit a Salesforce organization name:

- 
Sign in to Anypoint Platform using an account that has the root Organization Administrator permission. 
- 
Select **Access Management**from themenu. 
- 
Select **Salesforce**.
- 
Click the **Actions**menu (**…**) in the Salesforce organization and select**Edit Org Name**.
- 
Enter the name for the Salesforce organization and click **Save**.The Salesforce organization name appears in Anypoint Platform anywhere the organization is referenced. 

## Copy Your Anypoint Platform Organization ID

- 
Sign in to Anypoint Platform using an account that has the root Organization Administrator permission. 
- 
Select **Access Management**from themenu. 
- 
Select **Salesforce**.
- 
Click the **Actions**menu (**…**) and select**Get Anypoint Platform Organization ID**.
- 
Click **Copy**.