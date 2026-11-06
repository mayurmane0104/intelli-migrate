# Amazon Quick Microsoft PowerPoint extension (Preview) - Amazon Quick

**Source:** [https://docs.aws.amazon.com/quick/latest/userguide/powerpoint-extension.html](https://docs.aws.amazon.com/quick/latest/userguide/powerpoint-extension.html)

---

###### Note

This extension is currently available as a preview. During the preview period, the extension is fully functional for end users and production workloads. Administrative features such as centralized deployment controls and usage monitoring are being developed and will be available when the extension becomes generally available. Functionality and features may change during the preview period.

The Amazon Quick extension for PowerPoint integrates AI-powered assistance directly in your slide deck. Users can leverage Quick within PowerPoint to create presentations, add new slides, and make formatted edits to slides using their Quick enterprise data and apps.

The PowerPoint extension enables users to:

- 
                Create visually appealing and formatted templates using their own templates and brand guidelines. 
- 
                Create and edit slides and visuals within PowerPoint using natural language and their Quick enterprise data and apps. 
- 
                Make decks presentation ready by streamlining operations such as restructuring presentations, applying transitions, and more. 

The Quick PowerPoint extension is available within
            Amazon Quick to all eligible users by default and requires no administrative setup for
            user access if users can access the Microsoft PowerPoint app store.
            Users can search for Amazon Quick in the Microsoft PowerPoint app store
            or visit the [Quick
                for PowerPoint Microsoft store page](https://marketplace.microsoft.com/en-us/product/WA200010606) to add the extension.

###### Important

- 
                    The Amazon Quick PowerPoint extension uses generative AI to create and execute code within your PowerPoint application sandbox to help you perform tasks within PowerPoint. AI can make mistakes and perform inaccurate actions within your PowerPoint slide deck. 
- 
                    Amazon Quick does not use your user data for service improvement or for training its underlying large language models (LLMs). 

The following procedures are for IT administrators who want to automatically deploy the Amazon Quick PowerPoint extension across their organization on behalf of their users.

###### Topics

## Prerequisites for deploying the Microsoft PowerPoint extension to your organization

            Before configuring access to the Amazon Quick extension to Microsoft PowerPoint, administrators must complete the following steps:

- 
                    Have a Microsoft 365 Business subscription and be a Global Admin or have administrative permissions (specifically `AppCatalog.ReadWrite.All`).
- 
                    Have an Amazon Quick instance. 

## Deploying the Microsoft PowerPoint extension to your organization

            Follow these steps to deploy the extension to your users:

- 
                    Login to M365 admin center. 
- 
                    Select **Settings**>**Integrated apps**in the left navigation menu.
- 
                    Click on **Get apps**.
- 
                    Search for "Amazon Quick". 
- 
                    Locate the tile for the Amazon Quick in PowerPoint and click on **Get it now**.
- 
                    Confirm that you want to add the app. 
- 
                    Under **Assign users**, you can choose**Entire organization**or**Specific users/groups**depending on your needs.
- 
                    After selecting the users, review the app's requested permissions and capabilities and click **Next**.
- 
                    Click **Finish Deployment**.

## Microsoft PowerPoint extension permissions

            The Amazon Quick PowerPoint extension uses the
                `ReadWriteDocument` Office JavaScript API permission level. This is an
                Office add-in manifest permission, not a Microsoft Graph API scope.
                No Graph API permissions are needed during deployment.

The default app capabilities for the PowerPoint add-in are:

- 
                    Can read and make changes to your document 
- 
                    Access your profile information such as your name, email address, company name, and preferred language 
- 
                    Can send data over the Internet 

Administrators should review the permissions listed during the consent step of deployment through the M365 admin center integrated apps portal.