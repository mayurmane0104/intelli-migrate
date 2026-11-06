# Account details in Amazon Quick - Amazon Quick

**Source:** [https://docs.aws.amazon.com/quick/latest/userguide/manage-qs-account-settings.html](https://docs.aws.amazon.com/quick/latest/userguide/manage-qs-account-settings.html)

---

Use this section to change the account-wide settings in Amazon Quick. To open your account
        settings, choose the profile icon, and then select **Manage
            Quick**. Then, click on **Account
        settings**.

## Deleting your Amazon Quick subscription and closing your account

        ###### Warning

**Deleting your Amazon Quick subscription permanently destroys all 
                    organizational data across all AWS regions and cannot be reversed.**

This action will immediately and permanently delete:

- 
                    Every dashboard, analysis, and dataset across your entire organization in all regions 
- 
                    All user accounts and their associated work 
- 
                    Custom data sources and connections 
- 
                    All sharing permissions and folder structures 
- 
                    Historical usage data and audit logs 
- 
                    All customizations, themes, and organizational settings 

**Account deletion from any region affects your entire 
                global Quick deployment.** Even if you have Quick resources 
                in multiple AWS regions, this single action deletes everything worldwide.

**There is no recovery option.** Once deleted, this data 
                cannot be restored by AWS or recovered through any means.

**Before proceeding:** Export critical dashboards, back up 
                datasets, and ensure all stakeholders are informed of this permanent action.

The act of deleting your Amazon Quick subscription is immediate and final. Deletion
            removes every Amazon Quick asset on the AWS account you are using. It doesn't delete
            namespaces that you added. (The **Default** namespace is deleted
            automatically.) You can locate and delete namespaces by using the API operations [ListNamespaces](https://docs.aws.amazon.com/quicksight/latest/APIReference/API_ListNamespaces.html) and [DeleteNamespace](https://docs.aws.amazon.com/quicksight/latest/APIReference/API_DeleteNamespace.html).

You can terminate your Amazon Quick account from the **Manage
                Quick** menu or by using the API. To prevent someone from deleting a
            Amazon Quick user account accidentally or maliciously, Amazon Quick uses permissions, a
            switch for the **Account termination protection** setting, and a
            required confirmation word. 

After your account is deleted, you can create a new Amazon Quick account. The process doesn't take more than 15 minutes. The settings for edition and user authorization method on the new account can be the same or different.

Before you can delete your Amazon Quick account, make sure of the following:

- 
                You're signed in using the IAM account or AWS root account that was used to create your Amazon Quick account. 
- 
                You understand that your AWS account is not deleted when you terminate your Amazon Quick account. To instead close your AWS account, see [Closing an AWS account](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/close-account.html).

- 
                Terminating your account deletes all users, all uploaded data, and assets (for example, datasets, data sources, queries, dashboards, analyses, settings, and so on). 

### Permissions and access to account termination

You need the following special permissions to terminate a Amazon Quick account. Without these permissions, you won't be able to terminate a Amazon Quick user account. Contact your account administrator for help.

- 
                    You're a Amazon Quick administrator and have an `Admin`role in Amazon Quick.
- 
                    You need permissions to run the following (except if you're the root admin user (IAM ) who added Amazon Quick) - 
                            `quicksight:Unsubscribe`
- 
                            `quicksight:DeleteAccountSubscription`
- 
                            `ds:UnauthorizeApplication`
- 
                            `ds:DeleteDirectory`
- 
                            `ds:DescribeDirectories`
- 
                            `quicksight:UpdateAccountSettings`
 ###### NoteThe `DeleteAccountSubscription`Amazon Quick API requires both`quicksight:Unsubscribe`and`quicksight:DeleteAccountSubscription`IAM permissions. An explicit deny on either permission results in an`AccessDeniedException`.
- 
                            
- 
                    To remove custom namespaces, you need permission to run the following API operations: - 
                            `quicksight:ListNamespaces`
- 
                            `quicksight:DeleteNamespace`
 You don't need extra permissions to delete the default namespace. 
- 
                            

###### Warning

Terminating your account is an instant action that cannot be undone by you or by AWS.

### Deleting your account

The following sections outlines the different ways you can terminate your Amazon Quick instance.

###### To terminate your Amazon Quick account without the Amazon Quick UI

- 
                    Sign in to AWS where you want to remove Amazon Quick. 

###### To terminate your account by using the Amazon Quick UI

- 
                    Choose your profile on the application bar, and then choose **Manage Quick**.
- 
                    Use one of the following methods to open the **Account termination**screen.- 
                            Use this [direct link](https://us-east-1.quicksight.aws.amazon.com/sn/console/unsubscribe)to the screen.
- 
                            Choose **Account settings**,**Manage**.
 
- 
                            
- 
                    On the **Account termination**page, confirm that you are viewing the correct Amazon Quick account by checking the name listed for account name.
- 
                    Toggle off **Account termination protection is on**. Doing this enables the**Delete account**section.
- 
                    For **Type "confirm" to delete this account**, enter the word confirmation word shown on your screen.