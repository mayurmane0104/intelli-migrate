# Supporting multitenancy with isolated namespaces - Amazon Quick

**Source:** [https://docs.aws.amazon.com/quick/latest/userguide/namespaces.html](https://docs.aws.amazon.com/quick/latest/userguide/namespaces.html)

---

Amazon Quick Enterprise edition supports multitenancy through namespaces. An
        Amazon Quick *namespace* is a logical container that you
        can use to organize clients, subsidiaries, teams, and so on. Namespaces can help you achieve
        the following goals:
        

- 
            Your Amazon Quick subscription allows users to discover shared content and share with other users. At the same time, in the Amazon Quick end-user console experience, users in one namespace can't see or interact with users in another namespace. The Amazon Quick administrative console uses a different permission model. For more information, see the following important note. 
- 
            You can securely isolate data and also support diverse workloads without adding additional AWS accounts. Access to data is still strictly controlled by AWS security features. Users can see assets (like data and dashboards) only if they have the correct resource permissions. Also, users who have permissions can't inadvertently expose content to people who outside of their namespace. For more information, see [Supporting multitenancy with isolated namespaces](https://docs.aws.amazon.com/quicksight/latest/user/namespaces.html).
- 
            You can monitor data flows and usage reports, neatly partitioned by namespace. Categorizing data and reports by namespace can help simplify cost and security analysis. 
- 
            After you've registered users into your namespace, there's no additional administrative complexity or overhead. 
- 
            Namespaces are designed to span AWS Regions, so the use containment doesn't change even if a person signs in to a different AWS Region. 

###### Namespace isolation and the administrative console

Amazon Quick uses two different permission models depending on the console experience. In the Amazon Quick end-user console, namespace-level isolation is enforced. Each user's Amazon Quick role determines the actions that they can perform, and their namespace determines which users and groups they can interact with.

In the Amazon Quick administrative console, only AWS Identity and Access Management (IAM) permissions are enforced. Users operate outside of the namespace context, and the user's IAM policies determine access, not their namespace membership.

Users can operate under both permission models. When they use the end-user console, their Amazon Quick role and namespace determine their access. When they use the administrative console, their IAM permissions determine their access. For example, an IAM administrator with the appropriate permissions can view and manage users and groups across namespaces from the administrative console.

Namespaces currently have the following limitations:

- 
            Custom namespaces—those that are not the default namespace—are only accessible to IAM Federated Single-Sign On users. 
- 
            Use default namespaces instead of custom namespaces if you need to support the following: - 
                    Integrating your Amazon Quick account with IAM Identity Center. For more information on integrating your Amazon Quick account with IAM Identity Center, see [AWS security in Amazon Quick](https://docs.aws.amazon.com/quicksight/latest/user/security.html).
- 
                    Password-based logins. 
- 
                    Credential-based Active Directory logins. 
 
- 
                    
- 
            You can't transfer users directly from one namespace to another. You can choose to do some or all of this work programmatically. For more information, see the [Quick API reference](https://docs.aws.amazon.com/quicksight/latest/APIReference/Welcome.html). At the bottom of the page of each API operation, there's a list of links to the same operation in the SDKs for other languages. To see what SDKs are available, see[SDKs and toolkits](aws.amazon.comgetting-started/tools-sdks/)in the[AWS getting started resource center](aws.amazon.comgetting-started/).
- 
            Namespaces are useful for isolating users and permissions, but not for sharing assets. Dashboards, datasets, and analyses can be shared with users in different namespaces. By default, users can't access items that exist in the same namespace by default, but gain access to specific assets when the asset is shared with them. 

If you don't have an existing AWS account or you need to sign up for Amazon Quick, read
        the following guidelines, then follow the applicable instructions in [Signing up for an Amazon Quick
            subscription](https://docs.aws.amazon.com/quicksight/latest/user/signing-up.html):

- 
            Sign up for Enterprise edition. 
- 
            When asked which method you want to connect with, choose **Role Based Federation (IAM)**. Currently, namespaces support only customers who use an AWS Identity and Access Management (IAM) role with a web identity federation. For more information, see[Creating a role for a third-party Identity Provider (federation)](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_create_for-idp.html)
- 
            Complete the process of signing up. 
- 
            Use the Amazon Quick [CreateNamespace](https://docs.aws.amazon.com/quicksight/latest/APIReference/API_CreateNamespace.html)API operation to create one or more namespaces.
- 
            To start adding users, first follow the instructions in [Setting up IdP federation using IAM and Amazon Quick](https://docs.aws.amazon.com//quicksight/latest/user/external-identity-providers-setting-up-saml.html). Then use the[RegisterUser](https://docs.aws.amazon.com/quicksight/latest/APIReference/API_RegisterUser.html)API operation to add users to the appropriate namespace.

If you already signed up for Standard edition, you can easily upgrade your subscription to
        Enterprise edition. The person performing the upgrade must be a Amazon Quick user with
        administrator privileges. For more information, see [Upgrading
            your Amazon Quick subscription](https://docs.aws.amazon.com/quicksight/latest/user/upgrading-subscription.html).

If you have an Enterprise edition subscription that you've been using for some time, it's also possible to migrate your users into namespaces. When you sign up for Amazon Quick and add users, all of them reside in the default namespace. All of the users can interact directly with each other and share data and dashboards with each other. To isolate your users from each other, you can create one or more additional namespaces.

###### Important

Amazon Quick assets and resources, including datasets, data sources, dashboards, analyses, and so on, exist outside of any namespace. They're visible only to users who have resource permissions granted to them.

To implement namespaces, you use the following Amazon Quick API operations:

Namespaces are not supported in the Regions listed below:

- 
            `af-south-1`Africa (Cape Town)
- 
            `ap-southeast-3`Asia Pacific (Jakarta)
- 
            `ap-southeast-5`Asia Pacific (Malaysia)
- 
            `eu-south-1`Europe (Milan)
- 
            `eu-central-2`Europe (Zurich)

###### Note

If you need to install the AWS CLI, see [Installing the AWS
                CLI version 2](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html) in the *AWS Command Line Interface User Guide.*

To add users to a namespace, you use the [RegisterUser](https://docs.aws.amazon.com/quicksight/latest/APIReference/API_RegisterUser.html) API operation. Each namespace has a completely independent set of
        users.
         The user ARNs include the namespace qualifier to
        distinguish them, as shown in the following examples:

- 
            Amazon Quick considers these two entities to be different persons: - 
                    `arn:aws:quicksight:us-east-1:111122223333:user/`**namespace-123**/username123
- 
                    `arn:aws:quicksight:us-east-1:111122223333:user/`**namespace-456**/username123
 
- 
                    
- 
            Amazon Quick considers these two entities to be the same person: - 
                    `arn:aws:quicksight:`**us-east-1**:111122223333:user/**namespace-123**/username123
- 
                    `arn:aws:quicksight:`**us-west-2**:111122223333:user/**namespace-123**/username123
 
- 
                    

When you use [RegisterUser](https://docs.aws.amazon.com/quicksight/latest/APIReference/API_RegisterUser.html), you select an access level for each user. After a person's user
        name is assigned to one of the security cohorts, their access to the console and API is
        restricted. People using Amazon Quick can have a single access level, as follows:

- 
            Reader access, for read-only subscribers of a dashboard 
- 
            Author access, for analysts and dashboard designers 
- 
            Admin access, for Amazon Quick administrators 

## To migrate existing users in one namespace to a different namespace

        Follow the procedure below to migrate existing users from one namespace to a different namespace.

- 
                Identify the users that you want to transfer to a different namespace by using the Amazon Quick user and group API operations. For more information, see [API operations for controlling access](https://docs.aws.amazon.com/quicksight/latest/APIReference/controlling-access.html#quicksight-groups)in the[Quick API reference](https://docs.aws.amazon.com/quicksight/latest/APIReference/Welcome.html).
- 
                Create users in the new namespace by using the [RegisterUser](https://docs.aws.amazon.com/quicksight/latest/APIReference/API_RegisterUser.html)API operation. Within a namespace, user names are unique.If a namespace user starts using the Amazon Quick console or API in a new AWS Region, that user is still constrained to the namespace that you added them to. Each namespace represents a user directory of an identity provider. As such, it originates in the primary AWS Region where Amazon Quick is set up. However, because the user directory is propagated globally in your AWS account, the namespace is accessible from any AWS Region where your users are using Amazon Quick. 
- 
                To identify the asset and resource permissions that the new namespace users need, use the Amazon Quick API operations associated with each type of asset (dashboards, datasets, and so on). For more information, see [QuickSight API operations to control assets](https://docs.aws.amazon.com/quicksight/latest/APIReference/qs-assets.html)in the[Quick API reference](https://docs.aws.amazon.com/quicksight/latest/APIReference/Welcome.html).For example, let's say you are focusing on dashboards. You can use `ListDashboards`to list all the dashboard IDs in your AWS account. Then, to determine which users or groups can access these dashboards, you can use`DescribeDashboardPermissions`on the result set generated by`ListDashboards`. If you need to identify specific versions of a dashboard, you can`ListDashboardVersions`for that. You can also collect information about the location of the data that's used in the dashboard with the data source and dataset API operations. For more information, see[QuickSight API operations to control data resources](https://docs.aws.amazon.com/quicksight/latest/APIReference/qs-data.html)in the[Quick API reference](https://docs.aws.amazon.com/quicksight/latest/APIReference/Welcome.html).For more information about filtering API response output, see the SDK documentation for the language you're using. For information relating to the AWS Command Line Interface (AWS CLI), see [Controlling command output from the AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/cli-usage-output.html#cli-usage-output-filter)in the[AWS Command Line Interface User Guide](https://docs.aws.amazon.com/cli/latest/userguide/).
- 
                For Amazon Quick assets and resources, copy the permissions that the source namespace user has for each asset. Then use, for example, `UpdateDashboardPermissions`to apply the same permissions to the target namespace user. Each asset type has its own separate set of API operations for controlling the permissions that users have to use it. For more information, see[QuickSight API operations for asset and resource permissions](https://docs.aws.amazon.com/quicksight/latest/APIReference/controlling-access.html#asset-permissions)in the[Quick API reference](https://docs.aws.amazon.com/quicksight/latest/APIReference/Welcome.html).
- 
                When you are finished adding users and permissions, it's a good practice to allow some time for user acceptance testing. Doing this ensures that everyone is successfully using the new namespace. It also ensures that all assets and resources are accessible in the new namespace. After you're certain that you no longer need the original user names, you can begin to deprecate their permissions in the original namespace. Finally, when the users are ready, you can remove the unused group and user names in the source namespace. Do this in each AWS Region where your users were previously active.