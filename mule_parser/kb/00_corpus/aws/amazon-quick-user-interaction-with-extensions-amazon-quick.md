# Amazon Quick user interaction with extensions - Amazon Quick

**Source:** [https://docs.aws.amazon.com/quick/latest/userguide/extension-roles-overview.html](https://docs.aws.amazon.com/quick/latest/userguide/extension-roles-overview.html)

---

Amazon Quick extensions enable different user roles to collaborate effectively in creating, managing, and utilizing AI-powered analytics tools. Each role—administrators, authors, and end users—has distinct responsibilities and capabilities when working with extensions. Understanding these role-based interactions ensures proper governance, security, and optimal user experience across your organization's Amazon Quick deployment.

###### Topics

## User capabilities and permissions

            Amazon Quick implements a hierarchical permission model for extensions that balances organizational control with user productivity. Administrators establish the foundational policies and infrastructure, authors manage the deployment and configuration of specific extension instances, and readers benefit from the AI-powered assistance within their authorized scope. The following table shows how each user type in Amazon Quick interacts with extensions.

| User Type | Capabilities | 
|---|---|
| Administrators | 
 | 
| Authors | 
 | 
| Readers (Reader Pro only) | 
 | 

Beyond the broad user type categories, Amazon Quick implements granular permission controls that determine specific actions users can perform with individual extensions. These permissions operate independently of user types, allowing administrators to fine-tune access based on organizational needs and security requirements. The following table outlines how user permissions determine what you can do with a extension:

| Permissions Type | Permissions | 
|---|---|
| Owners | 
 | 
| Viewers | 
 | 

###### Important

The Amazon Quick browser extension extension doesn't need any admin setup to install and use.

These permission structures ensure that extension access aligns with your organization's security requirements while enabling appropriate levels of functionality for each user role. Administrators maintain control over extension availability and initial setup, authors handle deployment and configuration, and all users can benefit from the AI-powered assistance once extensions are properly configured.

## Amazon Quick administrator responsibilities

            Amazon Quick administrators, or users granted admin privileges, establish the foundational infrastructure that enables extension functionality across the organization. They handle the critical setup and security configurations that allow Amazon Quick authors to deploy extensions and end users to access them safely.

###### Note

Creating and adjusting extension access requires IAM administrator
                    privileges. All administrators will see the extension links, but if not [signed in with IAM credentials](https://docs.aws.amazon.com/quicksuite/latest/userguide/iam-credentials.html), you will need to sign in with
                    appropriate IAM permissions to manage extension access. This must be an IAM
                    user who is an Amazon Quick administrator and not non-IAM admin users.

| Responsibility area | Administrator capabilities | 
|---|---|
| Infrastructure setup | 
 | 
| Security and compliance | 
 | 

## Amazon Quick author capabilities

            Authors bridge the gap between administrative infrastructure and end-user access by creating, configuring, and deploying specific extension instances. They manage the day-to-day operational aspects of extension deployment and maintenance.

Author capabilities depend on the permission level granted by administrators. There are two permission types that determine what authors can do:

- 
                    **Viewers:**Can view extension name and description, access links to open extensions, and use the extensions.
- 
                    **Owners:**Can edit extension name and description, install extensions in workspaces or organizations, and share ownership permissions with users and groups.

This translates to two main setup flows:

- 
                    **Limited permissions (view, share, delete only):**Authors can only use the basic landing page functionality to view, share, and delete extensions after admin completes all setup.
- 
                    **Full permissions (deploy, view, share, delete, edit):**Authors can download manifests or use OAuth deployments to complete app setup, rename extensions, and access editing features.

| Capability area | Author functions | 
|---|---|
| Configuration and deployment | 
 | 
| Management and sharing | 
 | 

## Amazon Quick end user access

            End users represent the primary beneficiaries of extension functionality, accessing AI-powered assistance directly within their existing workflow applications. Their interaction with extensions focuses on daily productivity and seamless integration with organizational knowledge.

| Access level | User capabilities | 
|---|---|
| Daily usage and productivity | 
 | 
| Knowledge and actions | 
 | 

The following table shows how each user type in Amazon Quick interacts with extensions.

| User Type | Capabilities | 
|---|---|
| Administrators | 
 | 
| Authors | 
 | 
| Readers (Reader Pro only) | 
 | 

The following table outlines how user permissions determine what you can do with a extension:

| Permissions Type | Permissions | 
|---|---|
| Owners | 
 | 
| Viewers | 
 | 

###### Important

The Amazon Quick browser extension extension doesn't need any admin setup to install and use.

## Extension access troubleshooting

            If you encounter issues accessing or creating extensions:

- 
                    **Cannot create extensions:**Your IAM user who is a Amazon Quick administrator must first configure extension access for the extension type you want to use. Other administrators will not be able to create/edit/delete extension access.
- 
                    **Cannot find my extensions:**Check that extension access has been configured by your administrator and that you have the appropriate permissions to view extensions.
- 
                    **Extensions appear but cannot edit:**You have view-only access. Ask your administrator or extension owner to share edit permissions with you.
- 
                    **No extensions visible:**Contact your administrator to set up extension access and create default extensions for your organization.