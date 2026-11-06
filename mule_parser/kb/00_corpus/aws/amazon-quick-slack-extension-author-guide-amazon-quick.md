# Amazon Quick Slack extension author guide - Amazon Quick

**Source:** [https://docs.aws.amazon.com/quick/latest/userguide/slack-extension-author-guide.html](https://docs.aws.amazon.com/quick/latest/userguide/slack-extension-author-guide.html)

---

As an Amazon Quick author, you can deploy Quick Slack extensions after your admin establishes the foundational connection to your organization's Slack workspace. Your capabilities depend on the permission level granted by your administrator.

With **limited permissions** (view, share, delete
                only), you can manage basic extension operations through the landing page after
                admin completes all setup. With **full permissions**
                (deploy, view, share, delete, edit), you can complete the Slack OAuth
                application deployment, rename extensions, and access all editing features.

Author capabilities for Slack extensions:

- 
                    Deploy extensions to your organization's Slack workspace using OAuth (requires full permissions). 
- 
                    Customize extension settings - names, descriptions (requires full permissions). 
- 
                    Manage sharing and access permissions (available with limited or full permissions). 

###### Note

Before you deploy a Slack extension as an author, your
                    Quick admin must [configure Amazon Quick access to Slack](https://docs.aws.amazon.com/quicksuite/latest/userguide/slack-extension.html).

## Deploy a Slack extension

                Deploy a new Slack extension instance in the Quick console. This process establishes the foundation for connecting AI-powered assistance to your Slack workspace.

###### Note

This action requires full author permissions.

- 
                        Sign in to the Amazon Quick console. 
- 
                        In the left navigation, under **CONNECTIONS**, select**Extensions**.
- 
                        Select **Create extension**.
- 
                        Select **Slack**. Then, select**Next**.
- 
                        Configure the following fields: - 
                                **Name**- A name for your extension is pre-filled for you. You can edit this and enter a descriptive name for the Slack extension.
- 
                                **Description**(optional) - A description for your extension is pre-filled for you. You can edit this and enter a new description to provide additional context about this extension configuration.
- 
                                **Installation**type - Your Slack extension supports OAuth installation by default.
 
- 
                                
- 
                        Select **Next**to save your configuration.
- 
                        From the **Extension**summary page, navigate to the extension you just configured.
- 
                        Then, from the **Actions**menu, navigate to the extension you just configured.
- 
                        Select **Install**. Then, from the**Complete installation for Slack assistant**dialog box that opens, select**Install**.A success message will open up on the top right of your screen. 
- 
                        From the success message, select **Install extension**to finish installing your extension.###### NoteYou can also navigate to the extensions summary page and deploy your extension from the **Actions**menu.
- 
                        The link will open to a Slack login page where after you login (as admin) you will need to find and be asked to install the Amazon Quick app within your Slack workspace. ###### NoteYou may see a "This app is not approved by Slack banner." This message can be ignored. 
- 
                        Choose **Allow**to install your Amazon Quick App for Slack.
- 
                        Once the installation is complete, you will see the page confirming that the **Congratulations! Your Slack App has been successfully installed.**
- 
                        Choose **Open the Amazon Quick App in Slack**.
- 
                        This will open your Slack workspace where all users will be required to sign-in. 

Your Slack extension has now been successfully deployed and is available for users.

## Edit Slack extension

                ###### Note

This action requires full author permissions.

As an author, you can edit the extensions you deploy to your users. Modify extension settings to update names, descriptions, or configuration options. Changes take effect immediately and apply to all users with access to the extension.

- 
                        Sign in to the Amazon Quick console. 
- 
                        In the left navigation, under **CONNECTIONS**, select**Extensions**.
- 
                        Select the three dot menu icon for the Slack extension you need to edit. 
- 
                        Select **Edit**.
- 
                        Edit the configuration as required and select **Save**to confirm the changes.

## Share Slack extension

                Share ownership and management permissions with specific users and groups, enabling multiple users to manage extensions and assist with installation. You can assign different permission levels and manage access as needed.

- 
                        Sign in to the Amazon Quick console. 
- 
                        In the left navigation, under **CONNECTIONS**, select**Extensions**.
- 
                        Select the three dot menu icon for the Slack extension you need to share. 
- 
                        Select **Share**.
- 
                        Enter the users and groups you would like to share the extension with. 
- 
                        Select **Share**to send the access email to each group and user.
- 
                        From the drop-down next to each name, you can edit their access levels ( **Viewer**or**Owner**).
- 
                        **Optional:**You could select**Remove access**to delete the access for the selected group or user.

## Delete Slack extension

                As an author, you can delete the extensions you deploy to your users. Permanently remove a extension from your Quick console and revoke access for all users. This action cannot be undone and requires confirmation.

- 
                        Sign in to Amazon Quick console. 
- 
                        In the left navigation, under **CONNECTIONS**, select**Extensions**.
- 
                        Select the three dot menu icon for the Slack extension you need to delete. 
- 
                        Select **Delete**.
- 
                        Enter the word, "confirm", and select **DELETE**.