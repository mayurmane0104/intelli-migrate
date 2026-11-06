# Publishing an Asset to a Public Portal | MuleSoft Documentation

**Source:** [https://docs.mulesoft.com/exchange/to-share-api-asset-to-portal](https://docs.mulesoft.com/exchange/to-share-api-asset-to-portal)

---

# Publishing an Asset to a Public Portal

Use your organization’s public portal to publish assets for viewing and use by developers inside and outside your organization.

A public portal is visible to anyone who has the URL of the portal. The URL for a public portal starts with `https://anypoint.mulesoft.com/exchange/portals/Domain_Name/`.

Replace `Domain_Name` with the domain name shown in Anypoint access management on the [ Organization page](../access-management/managing-business-groups#organization-page).

## Permissions to Control Asset Publishing

An organization’s Exchange administrators add assets to the public portal and remove assets from the public portal.

Grant the Exchange administrator permission to a user or revoke the permission from a user with Anypoint Access Management.

For more information see [Set User Access Permissions](to-set-permissions).

## Add an Asset to a Public Portal

Follow these steps to add an asset to a portal and make the asset public.

Adding an asset to a portal does not delete the asset. It is still available internally.

- 
Select an asset to show its details. 
- 
Click **Share**and select**Public - Publish it on the public portal**.
- 
Select the version of the asset you want to publish in the public portal. 
- 
Select **Save**.

If no action occurs, refresh your browser, log in again, and add the asset again.

## Remove an Asset from a Public Portal

Follow these steps to remove an asset from a portal and make the asset private.

Removing an asset from a portal does not delete the asset. The asset is still available internally.

- 
Select the asset in Exchange and click **Share**.
- 
Select **Public - Publish it on the public portal**.
- 
Clear the version checkbox. The version of the asset is set to **Private**.
- 
Select **Save**.
- 
In Exchange, refresh the browser screen. In the asset’s **Overview**, the**Visibility**setting is now**Private**.