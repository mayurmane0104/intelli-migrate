# Managing Connected Apps | MuleSoft Documentation

**Source:** [https://docs.mulesoft.com/exchange/managing-connected-apps](https://docs.mulesoft.com/exchange/managing-connected-apps)

---

# Managing Connected Apps

Connected apps are applications that allow external applications to securely interact with the Anypoint Platform APIs by providing controlled access to its resources using OAuth 2.0 authentication protocols, without the need to share user credentials directly. For more information, see [Connected Apps in Anypoint Platform](../access-management/connected-apps-overview).

When an asset is created using a connected app and is published to Exchange, the creator of the asset is automatically set as the owner of the connected app.

Control whether or not to assign owner roles when creating assets using a connected app to avoid going over the maximum role [limit](../access-management/troubleshooting-anypoint-platform-access#access-management-limits).

When enabled, when creating new assets using a connected app, roles aren’t assigned to connected app owners. When disabled, roles are assigned by default.

- 
From the navigation bar, select **Settings**and select**Asset Deletion & Connected Apps Management**.
- 
In **Connected Application Owner Configuration**, enable or disable the option.