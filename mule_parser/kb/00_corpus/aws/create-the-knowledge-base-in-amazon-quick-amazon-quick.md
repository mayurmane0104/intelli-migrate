# Create the knowledge base in Amazon Quick - Amazon Quick

**Source:** [https://docs.aws.amazon.com/quick/latest/userguide/onedrive-kb-admin-connection.html](https://docs.aws.amazon.com/quick/latest/userguide/onedrive-kb-admin-connection.html)

---

After you complete the service credentials setup, create the knowledge base in Amazon Quick and provide the credentials. Any enterprise user can complete this step. Amazon Quick administrator access is not required.

You need the following values from
        [Set up service credentials](./onedrive-kb-admin-config.html). If an administrator completed the
        setup on your behalf, collect these values before you proceed:

- 
            KMS key ARN (from Step 1) 
- 
            Certificate thumbprint in base64url format (from Step 2) 
- 
            Entra application (client) ID (from Step 3) 
- 
            Directory (tenant) ID (from Step 3) 

## Navigate to Knowledge

        - 
                In Amazon Quick, choose **Knowledge**from the left navigation pane.
- 
                Under **Set up new knowledge base**, locate**Microsoft OneDrive**and choose the**Add**icon.

## Select service credentials authentication

        The **Create OneDrive knowledge base** wizard opens on
            the **Authentication method** step. Choose
            **Have admin access? Connect with service credentials to enable
                document-level access control.**

If you have previously created a knowledge base using service credentials,
            the **Connected account** dropdown appears with your most
            recent connection pre-selected. When you select an existing connection, the
            Tenant ID and Client ID are displayed below the dropdown for verification. You
            can use an existing connection or choose **+ Add account** to
            enter new service credentials.

## Enter service credentials

        After choosing **+ Add account**, fill in the following
            fields:

| Field | Description | Example | 
|---|---|---|
| Name | A descriptive name for this OneDrive connection. You see this name when selecting a connection for future knowledge bases. | OneDrive Production | 
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

Admin-managed setup crawls the OneDrive content of every user in your
            organization. Under **All users**, Amazon Quick syncs files
            and permissions for all users. You do not select individual sites, drives, or
            paths.

Choose **Next**.

###### Note

Because admin-managed setup syncs all users' OneDrive content, the
                Entra app registration must have tenant-wide
                `Sites.Read.All` permission. For the full permission set, see
                [Permissions](./onedrive-kb-admin-config.html#onedrive-kb-admin-config-permissions).

###### Note

Folders shared with a user are not crawled in admin-managed setup.
                Shared folders are stored in SharePoint and cannot be accessed with
                application credentials. To sync shared content, create a SharePoint
                knowledge base instead. For more information, see
                [Known limitations](./onedrive-kb-admin-managed.html#onedrive-kb-admin-managed-limitations).

## Configure additional settings

        In the final step of the wizard, you can configure optional settings for the knowledge base.

###### Note

Document-level access control (ACL) is always enabled for admin-managed
                OneDrive knowledge bases and cannot be turned off. When you enable ACL by
                creating an admin-managed knowledge base, the console might display a note
                that one-time admin consent is required for real-time access
                verification. If you are a Microsoft 365 administrator, choose the
                **Grant admin consent** link to grant consent directly.
                If you are not an administrator, ask your Microsoft 365 admin to grant
                consent. For more information, see
                [Admin consent](./onedrive-kb-acl.html#onedrive-kb-acl-admin-consent).

- Filter content by date
- 
                    Limits which documents are crawled based on their last modified date in OneDrive. The start date defaults to one year before today. You can change or clear the start date, and optionally set an end date. 
- Multi-media content, file size, and file patterns
- 
                    - 
                            **Visual content in documents**– Extracts and indexes visual elements from supported document formats. Enabled by default.
- 
                            **Audio files**– Transcribes and indexes audio files.
- 
                            **Video files**– Transcribes and indexes video files.
 ###### NoteEnabling audio and video indexing increases sync time and storage usage. Enable these options only if your OneDrive content includes relevant media files. 
- 
                            

Choose **Create** to create the knowledge base.

## Initial sync

        After you choose **Create**, you are returned to the
            knowledge base list page. The knowledge base might take a few minutes to finish
            provisioning. Once creation is complete, an initial sync is automatically
            triggered. You do not need to start it manually.