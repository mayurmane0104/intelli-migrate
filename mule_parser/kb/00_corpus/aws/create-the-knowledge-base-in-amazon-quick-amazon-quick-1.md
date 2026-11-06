# Create the knowledge base in Amazon Quick - Amazon Quick

**Source:** [https://docs.aws.amazon.com/quick/latest/userguide/sharepoint-kb-admin-connection.html](https://docs.aws.amazon.com/quick/latest/userguide/sharepoint-kb-admin-connection.html)

---

After you complete the service credentials setup, create the knowledge base in Amazon Quick and provide the credentials. Any enterprise user can complete this step. Amazon Quick administrator access is not required.

You need the following values from
        [Set up service credentials](./sharepoint-kb-admin-config.html). If an administrator completed the
        setup on your behalf, collect these values before you proceed:

- 
            KMS key ARN (from Step 1) 
- 
            Certificate thumbprint in base64url format (from Step 2) 
- 
            Entra application (client) ID (from Step 3) 
- 
            Directory (tenant) ID (from Step 3) 
- 
            SharePoint domain URL (from your Microsoft 365 tenant) 

## Navigate to Knowledge

        - 
                In Amazon Quick, choose **Knowledge**from the left navigation pane.
- 
                Under **Set up new knowledge base**, locate**Microsoft SharePoint Online**and choose the**Add**icon.

## Select service credentials authentication

        The **Create SharePoint knowledge base** wizard opens on
            the **Authentication method** step. Choose
            **Have admin access? Connect with service credentials to enable
                document-level access control.**

If you have previously created a knowledge base using service credentials,
            the **Connected account** dropdown appears with your most
            recent connection pre-selected. When you select an existing connection, the
            SharePoint domain, Tenant ID, and Client ID are displayed below the dropdown
            for verification. You can use an existing connection or choose
            **+ Add account** to enter new service credentials.

## Enter service credentials

        After choosing **+ Add account**, fill in the following
            fields:

| Field | Description | Example | 
|---|---|---|
| Connection name | A descriptive name for this SharePoint connection. You see this name when selecting a connection for future knowledge bases. | SharePoint Production | 
| SharePoint domain | Your organization's SharePoint Online domain. | `https://contoso.sharepoint.com` | 
| Tenant ID | The Microsoft Entra (Azure AD) tenant identifier. | `34567890-1234-1234-1234-123456789012` | 
| Client ID | The Application (client) ID from your Entra app registration. | `12345678-1234-4321-4321-210987654321` | 
| KMS key ARN | The ARN of the AWS KMS asymmetric signing key. | `arn:aws:kms:us-west-2:123456789012:key/my-key-id` | 
| Certificate Thumbprint | The base64url-encoded SHA-1 thumbprint of the certificate uploaded to Entra. | `abc123DEF456ghi789EXAMPLE` | 

Fill in each field and choose **Next**.

###### Tip

Give the connection a recognizable name. This name appears in the
                **Connected account** dropdown when you create future
                knowledge bases.

## Choose content

        Enter a **Name** and optional
            **Description** for your knowledge base.

- SharePoint site URLs
- 
                    Enter the URLs of SharePoint sites or subsites you want to sync, such as `https://contoso.sharepoint.com/sites/finance`. Enter one or more site URLs separated by commas and choose**Add Site**. Do not add file or folder URLs here.You can add up to 350 entries total across both **SharePoint site URLs**and**Specific SharePoint Paths**combined.
- Specific SharePoint Paths (optional)
- 
                    Enter the paths of specific folders, files, lists, libraries, or pages within a SharePoint site. Enter one or more paths separated by commas and choose **Add Path**. The 350-entry limit is shared with**SharePoint site URLs**.If a site is already added under **SharePoint site URLs**, all content from that site is synced. Adding individual items from the same site does not limit what is synced.###### ImportantDo not use browser URLs for paths. To get the correct path, navigate to the item in SharePoint, choose the three dot menu ( **...**), select**Details**, then scroll to**Path**and choose**Copy**.Example paths: - 
                            Folder: `https://contoso.sharepoint.com/sites/finance/Shared%20Documents/Reports/Q1`
- 
                            File: `https://contoso.sharepoint.com/sites/finance/Shared%20Documents/Reports/Q1/data.docx`
 
- 
                            

After adding your content, choose **Next**.

###### Tip

Each site URL and path must be accessible by the Entra app
                registration. If you are using `Sites.Selected`, ensure
                per-site permissions have been granted. For more information, see
                [Step 3b: Grant site-level permissions (Sites.Selected only)](./sharepoint-kb-admin-config.html#sharepoint-kb-admin-sites-selected).

## Configure additional settings

        In the final step of the wizard, you can configure optional settings for the knowledge base.

- ACL management
- 
                    Access Control List (ACL) management enables document-level access control for your SharePoint knowledge base. When enabled, Amazon Quick syncs the permission metadata from SharePoint during each crawl. At query time, Quick uses this metadata with a real-time access check. This check ensures that users only see answers from documents they can access in SharePoint. ACL management is unchecked (disabled) by default. To enable, select the **Control document access with ACLs**checkbox.When you enable ACL management, the console displays a note that one-time admin consent might be required for real-time access verification. If you are a Microsoft 365 administrator, choose the **Grant admin consent**link to grant consent directly. If you are not an administrator, ask your Microsoft 365 admin to grant consent. For more information about admin consent, see[Admin consent](./sharepoint-kb-acl.html#sharepoint-kb-acl-admin-consent).###### ImportantACL management cannot be changed after the knowledge base is created. This setting is immutable. If you need to change this setting, you must create a new knowledge base. Plan your ACL requirements carefully before creating the knowledge base. ###### NoteIf you enable ACL management, ensure your Entra app has the ACL permission set ( `User.Read.All`,`GroupMember.Read.All`on Graph, and`Sites.FullControl.All`on SharePoint). Without these, the knowledge base creation might succeed but ACL enforcement fails during sync.
- Filter content by date
- 
                    Limits which documents are crawled based on their last modified date in SharePoint. The start date defaults to one year before today. You can change or clear the start date, and optionally set an end date. 
- Multi-media content, file size, and file patterns
- 
                    - 
                            **Visual content in documents**– Extracts and indexes visual elements from supported document formats. Enabled by default.
- 
                            **Audio files**– Transcribes and indexes audio files.
- 
                            **Video files**– Transcribes and indexes video files.
 ###### NoteEnabling audio and video indexing increases sync time and storage usage. Enable these options only if your SharePoint content includes relevant media files. 
- 
                            

Choose **Create** to create the knowledge base.

## Initial sync

        After you choose **Create**, you are returned to the
            knowledge base list page. The knowledge base might take a few minutes to finish
            provisioning. Once creation is complete, an initial sync is automatically
            triggered. You do not need to start it manually.