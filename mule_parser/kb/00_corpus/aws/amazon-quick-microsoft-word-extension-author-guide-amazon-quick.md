# Amazon Quick Microsoft Word extension author guide - Amazon Quick

**Source:** [https://docs.aws.amazon.com/quick/latest/userguide/legacy-word-extension-author-guide.html](https://docs.aws.amazon.com/quick/latest/userguide/legacy-word-extension-author-guide.html)

---

As an Amazon Quick author, you can deploy Quick Microsoft Word extensions after your admin establishes the foundational connection to your organization's Microsoft 365 tenant. Your capabilities depend on the permission level granted by your administrator.

With **limited permissions** (view, share, delete
                only), you can manage basic extension operations through the landing page after
                admin completes all setup. With **full permissions**
                (deploy, view, share, delete, edit), you can download manifests for deployment in
                the M365 admin center, rename extensions, and access all editing
                features.

Author capabilities for Microsoft Word extensions include:

- 
                    Configure extension connections (requires access to M365 Admin Center portal). 
- 
                    Deploy extensions to your organization's Microsoft 365 tenant (requires full permissions). 
- 
                    Customize extension settings - names, descriptions (requires full permissions). 
- 
                    Download manifest files for advanced Microsoft 365 deployment (requires full permissions). 
- 
                    Manage sharing and access permissions (available with limited or full permissions). 

###### Note

Before you deploy a Microsoft Word extension as an author, your
                    Quick admin must [configure Amazon Quick access to Microsoft
                    Word](https://docs.aws.amazon.com/quicksuite/latest/userguide/legacy-word-extension.html).

###### Topics

## Deploy Microsoft Word extension

                Deploy a new Microsoft Word extension instance in the Amazon Quick console. This process establishes the foundation for connecting AI-powered assistance to your Microsoft Word environment.

###### Note

This action requires full author permissions.

Use this procedure to create and configure a new Microsoft Word extension for your organization.

- 
                        Sign in to the Amazon Quick console. 
- 
                        In the left navigation, under **CONNECTIONS**, select**Extensions**.
- 
                        Select **Create extension**.
- 
                        Select **Microsoft Word**. Then, select**Next**.
- 
                        Configure the following fields: - 
                                **Name**- A name for your extension is pre-filled for you. You can edit this and enter a descriptive name for the Microsoft Word extension.
- 
                                **Description**(optional) - A description for your extension is pre-filled for you. You can edit this and enter a new description to provide additional context about this extension configuration.
- 
                                **Installation**type - Your Microsoft Word extension uses manifest-only installation by default.
 
- 
                                
- 
                        Select **Next**to save the details and download the manifest file to your computer.

###### Note

You will now continue the remainder of this procedure within the Microsoft 365 admin center.

- 
                        In the Microsoft 365 admin center, choose **Integrated apps**from the left navigation and choose**Upload custom apps**. This will open the**Deploy New App**page.
- 
                        Choose **Office Add-in**as your App type.
- 
                        Choose **Upload manifest file (.xml) from device**, select**Choose from file**, select the downloaded manifest xml file and choose**Next**.
- 
                        Choose the users you want to add in the **Add users**section.
- 
                        Choose **Accept permissions**in the**Accept permissions requests**section and deploy the Add-in. Once deployment is completed, your users will be able to install the Amazon Quick Add-in in their Microsoft Word.

Your Microsoft Word extension is now created and ready for deployment to users in your organization.

## Edit Microsoft Word extension

                ###### Note

This action requires full author permissions.

As an author, you can edit the extensions you deploy to your users. Modify existing Microsoft Word extension configurations to update settings, change descriptions, or adjust deployment parameters as your organizational needs evolve.

Use this procedure to modify settings and configuration for an existing Microsoft Word extension.

- 
                        Sign in to the Amazon Quick console. 
- 
                        In the left navigation, under **CONNECTIONS**, select**Extensions**.
- 
                        Select the three dot menu icon for the Microsoft Word extension you need to edit. 
- 
                        Select **Edit**.
- 
                        Enter your changes and select **Save**to confirm the new configuration.

Your changes are now applied and will be reflected in the extension configuration for all users.

## Share Microsoft Word extensions

                Share ownership and management permissions with specific users and groups, enabling multiple users to manage extensions and assist with installation. You can assign different permission levels and manage access as needed.

Use this procedure to share your Microsoft Word extension with other users and manage their access permissions.

- 
                        Sign in to Amazon Quick console. 
- 
                        In the left navigation, under **CONNECTIONS**, select**Extensions**.
- 
                        Select the three dot menu icon for the Microsoft Word extension you need to share. 
- 
                        Select **Share**.
- 
                        Enter the users and groups you would like to share the extension with. 
- 
                        Select **Share**to send the access email to each group and user.
- 
                        From the drop-down next to each name, you can edit their access levels ( **Viewer**or**Owner**).
- 
                        **Optional**You could select,**Remove access**to delete the access for the selected group or user.

The specified users and groups now have access to your Microsoft Word extension with the permissions you assigned.

## Delete Microsoft Word Extensions

                As an author, you can delete the extensions you deploy to your users.

Use this procedure to permanently remove a Microsoft Word extension from your organization.

- 
                        Sign in to Amazon Quick console 
- 
                        In the left navigation, under **CONNECTIONS**, select**Extensions**
- 
                        Select the three dot menu icon for the Microsoft Word extension you need to delete 
- 
                        Select **Delete**
- 
                        Enter, confirm and **DELETE**to delete the Extension

The Microsoft Word extension has been permanently removed and is no longer accessible to users in your organization.