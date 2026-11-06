# Creating a custom permissions profile in Amazon Quick - Amazon Quick

**Source:** [https://docs.aws.amazon.com/quick/latest/userguide/create-custom-permissions-profile.html](https://docs.aws.amazon.com/quick/latest/userguide/create-custom-permissions-profile.html)

---

| Applies
                    to:Enterprise Edition | 

| Intended audience: Administrators and Amazon Quick developers | 

In Enterprise edition, you can restrict the functionality that people can access in
        Amazon Quick. You can configure custom permissions at the account, role (admin, author,
        reader), and user levels for all identity types in Quick. *User level
            custom permissions* override a role's existing default or custom role
        level permissions for the specified user. *User level custom permissions*
        and *role level custom permissions* override *account level
            custom permissions*.

The following limitations apply to custom permissions.

- 
            You can't grant permissions that are above a user's default role. For example, if a user has reader access, you can't grant permissions for that user to edit dashboards. 
- 
            To customize user or role permissions, you need to be a Amazon Quick administrator with the following IAM permissions: - 
                    `quicksight:CreateCustomPermissions`
- 
                    `quicksight:DeleteCustomPermissions`
- 
                    `quicksight:DescribeCustomPermissions`
- 
                    `quicksight:ListCustomPermissions`
- 
                    `quicksight:UpdateCustomPermissions`
- 
                    `quicksight:DescribeAccountCustomPermissions`
- 
                    `quicksight:UpdateAccountCustomPermissions`
- 
                    `quicksight:DeleteAccountCustomPermissions`
 
- 
                    

You can create custom permission profiles to restrict access to any combination of the following features. Parent capabilities can be used to restrict access to an entire asset's feature sets. When parent capabilities are disabled, all associated child features will also be disabled.

Features with no parent capabilities cannot be turned off with this mechanism. Instead, they must be restricted as individual features.

## Quick parent capabilities

        
        | Parent capability | Functionality | 
|---|---|
| Analyses | Restricts all Analysis-related features | 
| Apps | Restricts all Apps-related features | 
| Dashboards | Restricts all Dashboards-related features | 
| Actions | Restricts all Actions-related features | 
| Automate | Restricts all Automation-related features | 
| Chat Agents | Restricts all Chat Agent-related features | 
| Extensions | Restricts all Extensions-related features | 
| Flows | Restricts all Flows-related features | 
| Knowledge Base | Restricts all Knowledge Base-related features | 
| Research | Restricts all Research-related features | 
| Scenarios | Restricts all Scenarios-related features | 
| Spaces | Restricts all Spaces-related features | 
| Stories | Restricts all Stories-related features | 
| Topics | Restricts all Topics-related features | 

## Quick features

        
        | Feature | Amazon Quick behavior | Parent capability | 
|---|---|---|
| Create Chat Agents | 
 | Chat Agents | 
| Share Chat Agents | 
 | Chat Agents | 
| Allow creators to share without approval | 
 | Flows | 
| Use Bedrock models for output refinement | 
 | Flows | 
| Enable UI agent to perform browser tasks | 
 | Flows | 
| All eligible users can review and approve Flows sharing requests | 
 | Flows | 
| Create Spaces | 
 | Spaces | 
| Share Spaces | 
 | Spaces | 
| Use internet to enhance results | 
 | -- | 
| Sharing analyses | 
 | Analyses | 
| Adding or running anomaly detection | 
 | Analyses | 
| Print Sheet | 
 | -- | 
| Export sheet to PDF | 
 | -- | 
| Creating or updating themes | 
 | -- | 
| Sharing dashboards | 
 | Dashboard | 
| Export visual to CSV | 
 | -- | 
| Export visual to Excel | 
 | -- | 
| Creating or updating all datasets | 
 | -- | 
| Creating or updating only SPICE datasets | 
 | -- | 
| Sharing datasets | 
 | -- | 
| Viewing account SPICE capacity | 
 | -- | 
| Creating or updating all data sources | 
 | -- | 
| Sharing data sources | 
 | -- | 
| Managing shared folders | 
 | -- | 
| Creating shared folders | 
 | Managing shared folders | 
| Renaming shared folders | 
 | Managing shared folders | 
| Creating or updating scheduled email reports | 
 | -- | 
| Subscribing to scheduled email reports | 
 | Dashboard | 
| CSV attachments in scheduled email reports | 
 | -- | 
| Excel attachments in scheduled email reports | 
 | -- | 
| PDF attachments in scheduled email reports | 
 | -- | 
| Content within scheduled email reports | 
 | -- | 
| Creating or updating threshold alerts | 
 | -- | 
| Edit Visual with AI | 
 | Analyses | 
| Build Calculation with AI | 
 | Analyses | 
| Create Executive Summary | 
 | Dashboards | 
| Creating or updating all knowledge bases | 
 | Knowledge Base | 
| Share all knowledge bases | 
 | Knowledge Base | 
| Create and update apps | 
 | Apps | 
| Share apps | 
 | Apps | 
| Invoke apps AI inference | 
 | Apps | 
| Access apps native data store | 
 | Apps | 

## Action connector features

        
        In addition to the features listed in the preceding sections, you can restrict access to individual action connectors. Each action connector supports the following permissions:

- 
                **Create and Update action**– Restricts the ability to create or update actions for the connector.
- 
                **Share action**– Restricts the ability to share actions for the connector.
- 
                **Use action**– Restricts the ability to use actions for the connector.

These permissions are available on the **Action Connectors** tab of
            the custom permissions profile. For a list of available action connectors, see [Action connectors](https://docs.aws.amazon.com/quick/latest/userguide/action-integrations.html).

Custom permissions profiles can be created for Amazon Quick accounts that are integrated with IAM Identity Center, Active Directory, or for Amazon Quick accounts that have Amazon Quick managed users. The identity type that an Amazon Quick account uses determines the way an Amazon Quick admin configures a custom permissions profile.

The following procedure shows you how to control access to Amazon Quick capabilities and respective features.

###### To control access to Amazon Quick capabilities and features

- 
            Log in to the Amazon Quick console. 
- 
            Select **Manage Quick**.
- 
            From the admin console left navigation menu, select **Permissions**, and then select**Custom permissions**.
- 
            In **Custom permissions**, from**Profiles**, select**New profile**or choose to edit the default profile.
- 
            In **New profile**, do the following:- 
                    In **Restrict capabilities**– Choose whether to allow specific capabilities for your system by checking or unchecking the appropriate options.
- 
                    In **Restrict features**– Choose whether to allow specific features by checking or unchecking the appropriate options.
 
- 
                    

## Creating a custom permissions profile for a Amazon Quick account that is integrated with IAM Identity Center or Active Directory

        Amazon Quick account admins can use the following procedure to create a custom permissions profile for a Amazon Quick account that is integrated with IAM Identity Center or Active Directory.

###### To create a custom permissions profile for a Amazon Quick account that is integrated with IAM Identity Center or Active Directory

- 
                Sign in to the [AWS Management Console](https://aws.amazon.com//console).
- 
                Open Amazon Quick. 
- 
                The Amazon Quick Admin console opens. Choose **Custom Permissions**.
- 
                The **Manage custom permissions**page opens. Choose one of the following options.- 
                        To create a new custom permissions profile, choose **Create**.
- 
                        To edit or view an existing custom permissions profile, choose the ellipsis (three dots) next to the profile that you want, and then choose **Edit**.
 
- 
                        
- 
                If you want to create or update a custom permissions profile, make selections for the following items. - 
                        For **Name**, enter a name for the custom permissions profile.
- 
                        For **Restrictions**, choose the options that you want to deny. Any option that you don't choose is allowed. For example, if you don't want users to create or update data sources, but you want them to be able to do everything else, choose only**Creating or updating data sources**.
 
- 
                        
- 
                Choose **Create**or**Update**to confirm your choices. To go back without making any changes, choose**Back**.
- 
                Once you are done making changes, record the name of the custom permissions profile. Provide the name of the custom permissions profile to API users so that they can apply the custom permissions profile to roles or users. 

## Creating a custom permissions profile for a Amazon Quick account that uses Amazon Quick managed users

        Amazon Quick account admins can use the following procedure to create a custom permissions profile for a Amazon Quick account that uses Amazon Quick managed users.

###### To create a custom permissions profile for Amazon Quick managed users

- 
	Open the [Quick console](https://quicksight.aws.amazon.com/).
- 
                From any page in the Amazon Quick console, choose **Manage Quick**at the top right corner.Only Amazon Quick administrators have access to the **Manage Quick**menu option. If you don't have access to the**Manage Quick**menu, contact your Amazon Quick administrator for assistance.
- 
                Choose **Custom permissions**. You can also choose the**Manage users**section, and then choose**Manage custom permissions**.
- 
                The **Manage custom permissions**page opens. Choose one of the following options.- 
                        To create a new custom permissions profile, choose **Create**.
- 
                        To edit or view an existing custom permissions profile, choose the ellipsis (three dots) next to the profile that you want, and then choose **Edit**.
 
- 
                        
- 
                If you want to create or update a custom permissions profile, make selections for the following items. - 
                        For **Name**, enter a name for the custom permissions profile.
- 
                        For **Restrictions**, choose the options that you want to deny. Any option that you don't choose is allowed. For example, if you don't want users to create or update data sources, but you want them t be able to do everything else, choose only**Creating or updating data sources**.
 
- 
                        
- 
                Choose **Create**or**Update**to confirm your choices. To go back without making any changes, choose**Back**.
- 
                Once you are done making changes, record the name of the custom permissions profile. Provide the name of the custom permissions profile to API users so that they can apply the custom permissions profile to roles or users. 

After you create a custom permissions profile, use Amazon Quick APIs to add or
            change the custom permissions profile that is assigned to a user, role, or account. Users with
            sufficient permissions can also use the [ AWS::QuickSight::CustomPermissions](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-quicksight-custompermissions.html) CloudFormation resource to
            manage Amazon Quick custom permissions profiles. Use the following topics to learn more
            about managing custom permissions profiles with the Amazon Quick APIs.

## Apply a custom permissions profile to a Amazon Quick role with the Amazon Quick API

        After you create a custom permissions profile, use the Amazon Quick APIs to add or change the custom permissions profile that is assigned to a role.

Before you begin, you need to set up and configure the AWS CLI. For more information
            about installing the AWS CLI, see [Install or update the latest
                version of the AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html) and [Configure the AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-configure.html)
            in the AWS Command Line Interface User guide. You also need permissions to use the Amazon Quick
            API.

The following example calls the `UpdateRoleCustomPermission` API to update
            the custom permissions that are assigned to a role.

`aws quicksight update-role-custom-permission \ --role``ROLE`\ --aws-account-id`AWSACCOUNTID`\ --namespace default \ --custom-permissions-name`PERMISSIONNAME`\ --region`REGION`

The following example returns the custom permissions profile that is assigned to a role.

`aws quicksight describe-role-custom-permission \ --role``ROLE`\ --aws-account-id`AWSACCOUNTID`\ --namespace default \ --region`REGION`

The following example deletes a custom permissions profile from a role.

`aws quicksight delete-role-custom-permission \ --role``ROLE`\ --aws-account-id`AWSACCOUNTID`\ --namespace default \ --region`REGION`

## Apply a custom permissions profile to a user with the Amazon Quick API

        The following example applies a custom permissions profile to a user.

`aws quicksight update-user-custom-permission \ --aws-account-id``AWSACCOUNTID`\ --namespace`default`\ --user-name`USER_NAME`\ --custom-permissions-name`myCustomPermission`

The following example deletes a custom permissions profile from a user.

`aws quicksight delete-user-custom-permission \ --aws-account-id``AWSACCOUNTID`\ --namespace`default`

The following example adds custom permissions to a new Amazon Quick IAM user.

`aws quicksight register-user \ --iam-arn arn:aws:iam::``AWSACCOUNTID`:user/`USER`\ --identity-type IAM \ --user-role AUTHOR \ --custom-permissions-name`custom-permissions-profile-name`\ --email`AWSACCOUNTID`\ --namespace default \

You can also associate an existing IAM user with a new permissions profile. The following example updated the custom permissions profile of an existing IAM user.

`aws quicksight update-user \ --user-name``USERNAME`\ --role AUTHOR \ --custom-permissions-name`custom-permissions-profile-name`\ --email`AWSACCOUNTID`\ --namespace default \

The example below removes an existing user from a permissions profile.

`aws quicksight update-user \ --user-name``USERNAME`\ --role AUTHOR \ --unapply-custom-permissions \ --email`AWSACCOUNTID`\ --namespace default

To test the custom permissions that are applied to a role or user, log in to the
            user's account. When a user logs into Amazon Quick, they are granted the highest
            privilege role that they have access to. The highest privileged role a user can be
            granted is Admin. The lowest privileged role that a user can be granted is Reader. For
            more information about roles in Amazon Quick, see [Managing user
                access inside Amazon Quick](https://docs.aws.amazon.com/quicksight/latest/user/managing-users.html).

If you assign a custom permissions profile that restricts data source sharing to the author's role, that author is no longer able to access the controls that allow data source sharing. Instead, the affected author has view-only permissions to the data source.

## Apply a custom permissions profile to an account

        ###### To apply a custom permissions profile to an account

- 
	Open the [Quick console](https://quicksight.aws.amazon.com/).
- 
                From the top right, choose the profile icon. 
- 
                Choose **Manage Quick**. Only Amazon Quick administrators will be able to view this page.
- 
                Choose **Custom permissions**. You can also choose the**Manage users**section, and then choose**Manage Custom Permissions**if your Quick account uses Quick managed users.
- 
                Locate the desired account custom permission. In the options menu under **Actions**, choose**Set as account profile**.

### Apply a custom permissions profile to an account using the Quick APIs

After you have created a custom permissions profile, use the Quick API to add or change the custom permissions profile that is assigned to an account.

Before you begin, you will need to set up and configure the AWS CLI. For more
                information about installing the AWS CLI, see see [Install or update the
                    latest version of the AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html) and [Configure the AWS
                    CLI](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-configure.html) in the AWS Command Line Interface user guide. You also need the
                following IAM permissions: `quicksight:UpdateAccountPermission`,
                    `quicksight:DescribeAccountPermission`, and
                    `quicksight:DeleteAccountCustomPermission`.

The following example calls the `UpdateAccountPermission` API to update
                the custom permissions that are assigned to an account.

`aws quicksight update-account-custom-permission \ --aws-account-id``AWSACCOUNTID`\ --custom-permissions-name`PERMISSIONNAME`\ --region`REGION`

The following example returns the custom permissions profile that is assigned to an account.

`aws quicksight describe-account-custom-permission \ --aws-account-id``AWSACCOUNTID`\ --region`REGION`

The following example unapplies a custom permissions profile from an account.

`aws quicksight delete-account-custom-permission \ --aws-account-id``AWSACCOUNTID`\ --region`REGION`