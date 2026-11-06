# Sharing knowledge bases and data sources - Amazon Quick

**Source:** [https://docs.aws.amazon.com/quick/latest/userguide/sharing-kb-datasources.html](https://docs.aws.amazon.com/quick/latest/userguide/sharing-kb-datasources.html)

---

Amazon Quick enables you to share knowledge bases and data source connections with other users in your account. You can collaborate with multiple users on knowledge bases or reuse existing data source connections without re-entering credentials.

###### Note

All knowledge bases can be shared with the Viewer role, which allows users to query the knowledge base. The Owner role (co-owner sharing) is available only for admin-managed Microsoft SharePoint Online and Google Drive knowledge bases. Data source sharing is also limited to admin-managed SharePoint and Google Drive connections.

## Sharing knowledge bases

        Knowledge base owners can share their knowledge bases with other users and assign one of two roles:

| Role | Permissions | 
|---|---|
| Owner | View all tabs (Summary, Sync History, Settings, Permissions). Edit knowledge base details. Trigger manual syncs. Update the sync schedule. Share the knowledge base with others. Delete the knowledge base. Owners cannot edit the underlying data source connection unless they are also an Owner of the data source. | 
| Viewer | View the knowledge base in the list and access the Summary tab only. Viewers cannot edit, share, delete, or trigger syncs. | 

Before you share, note the following:

- 
                All knowledge bases support sharing with the Viewer role. Viewers can query the knowledge base. 
- 
                Any owner of the knowledge base can share it, not only the original creator. 
- 
                Co-owner sharing (the Owner role) is available only for admin-managed SharePoint and Google Drive knowledge bases. All other knowledge base types can be shared only with the Viewer role. 
- 
                The original creator of a knowledge base always retains the Owner role and cannot be removed. 

### Sharing a knowledge base

You can access the sharing permissions from either of the following locations:

- 
                    From the knowledge base list, choose the actions menu ( **⋮**) next to the knowledge base and choose**Share knowledge base**.
- 
                    From within a knowledge base, choose the **Permissions**tab.

To add a user:

- 
                    Choose **Add users & groups**.
- 
                    In the search field, enter the user's name or email. Choose the user from the results, and then choose **Add**.
- 
                    The user appears in the permissions list with a default role of **Viewer**. To change the role, open the**Permissions**dropdown next to the user's name and choose**Owner**or**Viewer**.

### Changing or revoking knowledge base access

To change or remove a user's access to a knowledge base, complete the following steps.

- 
                    Open the knowledge base and choose the **Permissions**tab.
- 
                    Locate the user in the permissions list. 
- 
                    To change their role, open the **Permissions**dropdown and choose**Owner**or**Viewer**.
- 
                    To remove access, choose **Revoke access**in the**Actions**column.

## Sharing data source connections

        Amazon Quick administrators can share data source connections with other users in their account. This enables multiple users to create knowledge bases using the same connection without re-entering credentials.

Before you share, note the following:

- 
                Only users with Amazon Quick administrator privileges can share data source connections. 
- 
                Data source sharing is available only for admin-managed (service credentials) connections. User-managed connections that are created through single sign-on cannot be shared. 
- 
                If you revoke a user's access to a data source, the user's existing knowledge bases continue to sync. Knowledge bases that were previously created with the shared data source continue to sync normally. 
- 
                If an administrator deletes a data source, then existing knowledge bases that are linked to it remain visible. However, syncs fail with an error that indicates the underlying data source was deleted. 
- 
                Unlike knowledge bases, the original creator of a data source can be removed or have their role changed. 

| Role | Permissions | 
|---|---|
| Owner | Use the shared data source to create knowledge bases and edit the connection details (such as App ID or App Secret). | 
| Viewer | Use the shared data source to create knowledge bases but cannot edit the connection details. | 

### Sharing a data source connection

To share a data source connection with other users, complete the following steps.

- 
                    In Amazon Quick, choose **Manage account**from the left navigation pane.
- 
                    Choose **Manage assets**.
- 
                    Under **Browse assets**, choose**Data sources**.
- 
                    Select the checkbox next to the data source that you want to share. 
- 
                    Choose **Share**.
- 
                    In the **Share assets**dialog, choose a**Permissions**level (**Owner**or**Viewer**).
- 
                    In the **User or Group**field, enter the user's name or email and choose the user from the results.
- 
                    Choose **Share**.

The user now sees the shared data source in the
                **Connected account** dropdown when the user creates a new
                knowledge base.

### Editing a data source connection

Data source Owners can edit the connection details from the knowledge base list:

- 
                    In the knowledge base list, choose the actions menu ( **⋮**) next to a knowledge base that uses the data source.
- 
                    Choose **Edit integration**.
- 
                    Update the connection details and choose **Save**.

###### Important

If you edit a shared data source connection, then all knowledge bases that use it are updated. Review the impact before you save changes.

### Changing or revoking data source access

To view or manage permissions for a data source, complete the following steps.

- 
                    Choose **Manage account**, then choose**Manage assets**, and then choose**Data sources**.
- 
                    Choose the data source name to open its details page. 
- 
                    Under **User & Groups Permissions**, locate the user and change their role or remove their access.