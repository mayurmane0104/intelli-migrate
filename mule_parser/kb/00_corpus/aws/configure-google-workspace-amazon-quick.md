# Configure Google Workspace - Amazon Quick

**Source:** [https://docs.aws.amazon.com/quick/latest/userguide/google-drive-kb-google-config.html](https://docs.aws.amazon.com/quick/latest/userguide/google-drive-kb-google-config.html)

---

To connect Amazon Quick to Google Drive, complete the following tasks in the Google Cloud console and Google Workspace Admin Console. You create a Google Cloud project, turn on the required APIs, generate service account credentials, and configure domain-wide delegation. You also create a dedicated admin user for the service account to impersonate.

###### Prerequisites

Before you begin, make sure that you have the following:

- A Google Workspace account with administrator access 
- Permission to create projects in the Google Cloud console 

## Creating a Google Cloud project

        - 
                Open the Google Cloud console. 
- 
                From the project selector at the top of the page, choose **New Project**.
- 
                Enter a project name, then choose **Create**.
- 
                After the project is created, choose **Select Project**to switch to it. This might take a few moments.

## Turning on the required APIs

        Amazon Quick requires three Google APIs. Turn on each one from the API Library.

- 
                In the navigation menu, choose **APIs & Services**, then choose**Library**.
- 
                Search for each of the following APIs and choose **Enable**:- 
                        Google Drive API 
- 
                        Google Drive Activity API 
- 
                        Admin SDK API 
 
- 
                        

## Creating the service account

        - 
                In the navigation menu, choose **APIs & Services**, then choose**Credentials**.
- 
                Choose **Create Credentials**, then choose**Service account**.
- 
                Enter a name and optional description for the service account, then choose **Done**.

## Generating a private key

        - 
                On the **Credentials**page, choose the service account you created.
- 
                Choose the **Keys**tab, then choose**Add Key**,**Create new key**.
- 
                Confirm that **JSON**is selected, then choose**Create**.

The browser downloads a JSON file containing the private key. Store this file securely. You upload it to Amazon Quick in a later step.

###### Note

If you receive an error stating that service account key creation is
                disabled by an organization policy, see
                [Resolving organization policy restrictions](#google-drive-kb-admin-troubleshooting-org-policy).

## Recording the service account unique ID

        - 
                On the service account detail page, choose the **Details**tab.
- 
                Copy the value in the **Unique ID**field. You need this value when you configure domain-wide delegation.

## Configuring domain-wide delegation

        Domain-wide delegation allows the service account to access Google Workspace data on behalf of users in your organization.

- 
                On the service account detail page, expand **Advanced settings**.
- 
                Choose **View Google Workspace Admin Console**. The admin console opens in a new tab.
- 
                In the admin console navigation pane, choose **Security**,**Access and data control**,**API controls**.
- 
                Choose **Manage Domain Wide Delegation**, then choose**Add new**.
- 
                For **Client ID**, enter the unique ID you copied earlier.
- 
                For **OAuth scopes**, enter the following comma-separated values:`https://www.googleapis.com/auth/drive.readonly,https://www.googleapis.com/auth/drive.metadata.readonly,https://www.googleapis.com/auth/admin.directory.user.readonly,https://www.googleapis.com/auth/admin.directory.group.readonly,https://www.googleapis.com/auth/cloud-platform,https://www.googleapis.com/auth/forms.body.readonly`
- 
                Choose **Authorize**.

## Creating a delegated admin user

        The service account acts on behalf of a Google Workspace admin user. Create a dedicated user for this purpose and assign the minimum required roles.

- 
                In the Google Workspace Admin Console, choose **Directory**, then choose**Users**.
- 
                Choose **Add new user**.
- 
                Enter a first name, last name, and primary email address for the new user, then choose **Add new user**.
- 
                Choose **Done**.
- 
                From the user list, choose the user you created. If the user does not appear, refresh the page. 
- 
                On the user detail page, expand the **Admin roles and privileges**section.
- 
                Under **Roles**, assign the following roles:- 
                        Groups Reader 
- 
                        User Management Admin 
- 
                        Storage Admin 
 
- 
                        
- 
                Choose **Save**.

Record the email address of this user. You need it when you create the knowledge base in Amazon Quick.

## Troubleshooting the Google Workspace configuration

         
            ### Resolving organization policy restrictions

If you receive the following error when creating a service account key:

```
The organization policy constraint iam.disableServiceAccountKeyCreation
is enforced on your organization.
```
###### Note

For Google Cloud organizations created on or after May 3, 2024, this constraint is enforced by default.

You must override the policy for your project.

- 
                    Open the Google Cloud console and confirm that the correct project is selected. 
- 
                    In the navigation menu, choose **IAM & Admin**, then choose**Organization Policies**.
- 
                    In the **Filter**field, enter`iam.disableServiceAccountKeyCreation`. Then, in the policy list, choose**Disable service account key creation**.
- 
                    Choose **Manage policy**.###### NoteIf **Manage policy**is unavailable, you need the Organization Policy Administrator role (`roles/orgpolicy.policyAdmin`) at the organization level. See[Granting the Organization Policy Administrator role](#google-drive-kb-admin-troubleshooting-org-admin-role).
- 
                    In the **Policy source**section, ensure that**Override parent's policy**is selected.
- 
                    Under **Enforcement**, turn off enforcement for this organization policy constraint.
- 
                    Choose **Set policy**.

The change can take several minutes to propagate.

### Granting the Organization Policy Administrator role

The Organization Policy Administrator role
                (`roles/orgpolicy.policyAdmin`) must be granted at the
                organization level, not the project level. It does not appear in the
                role list when assigning roles to a project.

To grant this role, select your organization (not a project) from
                the project selector in the Google Cloud console. Then, choose
                **IAM & Admin**, **IAM**, and
                assign the role to your account. For detailed instructions, see
                [Manage
                access to projects, folders, and organizations](https://cloud.google.com/iam/docs/granting-changing-revoking-access) in the Google
                Cloud documentation.

The role assignment can take several minutes to propagate.