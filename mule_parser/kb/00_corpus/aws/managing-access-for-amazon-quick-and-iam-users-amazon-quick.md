# Managing access for Amazon Quick and IAM users - Amazon Quick

**Source:** [https://docs.aws.amazon.com/quick/latest/userguide/managing-user-access-qs-iam.html](https://docs.aws.amazon.com/quick/latest/userguide/managing-user-access-qs-iam.html)

---

Amazon Quick account administrators can use this topic to learn more about managing accounts that use IAM or Quick for identity federation.

To manage Quick users, you must have administrative privileges in
            Quick and also the appropriate AWS permissions. For more information about
            the necessary AWS permissions, see [IAM
                policy examples for Quick](https://docs.aws.amazon.com/quicksight/latest/user/iam-policy-examples.html).

Each Quick Enterprise edition account can have an unlimited number of
            users. User names that contain a semicolon (`;` ) aren't supported.

Use the topics below to learn more about managing access for Quick and IAM users.

###### Topics

## Inviting users to access Amazon Quick

            | Applies
                    to:Enterprise Edition and Standard Edition | 

| Intended audience: Amazon Quick administrators | 

Use the following procedure to invite a user to access Quick.

- 
                    Choose your user name on the application bar and then choose **Manage Quick**.
- 
                    Choose **Manage Users**. On this screen, you can manage users who already exist in your account.
- 
                    Choose **Invite users**.
- 
                    In the **Invite users to this account**table, enter a new user name for a person to whom you want to grant access to Quick. If the user is an IAM user, enter their IAM username. Then press`+`. A user's IAM username can be the same as their email address.Repeat this step until you have entered everyone who you want to invite. Then go to the next step to enter details. 
- 
                    For **Email**, enter an email address for the account.###### NoteCurrently, email addresses are case-sensitive. 
- 
                    For **Role**, choose the role to assign to each person you're inviting. A*role*determines the permission level to grant to that account.- 
                            **ADMIN roles**:- 
                                    **ADMIN**– The user is able to both use Amazon Quick for authoring and for performing administrative tasks like managing users or purchasing[SPICE](https://docs.aws.amazon.com/quicksight/latest/user/spice.html)capacity.
- 
                                    **ADMIN PRO**– The user is able to perform all actions of a Amazon Quick Admin and utilize applicable Amazon Quick Generative BI capabilities. For more information about Pro roles in Amazon Quick, see[Get started with Generative BI](https://docs.aws.amazon.com/quicksight/latest/user/generative-bi-get-started.html).
 There are some differences in the administrative tasks that IAM users and Amazon Quick administrators can perform. These differences occur because some administrative tasks require permissions in AWS, which Amazon Quick–only users lack. The differences are these: - 
                                    Amazon Quick administrators can manage users, SPICE capacity, and subscriptions. 
- 
                                    IAM users with administrative permissions can also manage users, SPICE capacity, and subscriptions. In addition, they can manage Amazon Quick permissions to AWS resources, upgrade to Enterprise edition, and unsubscribe from Amazon Quick. 
 If you want to create a user with administrator permissions with IAM access, check with your AWS administrator. Make sure that the IAM user has the all necessary statements in their IAM permissions policy to work with Amazon Quick resources. For more information about what statements are required, see [IAM policy examples for Amazon Quick](https://docs.aws.amazon.com/quicksight/latest/user/iam-policy-examples.html).
- 
                                    
- 
                            **AUTHOR roles**:- 
                                    **AUTHOR**– The user is able to author analyses and dashboards in Amazon Quick but not perform any administrative tasks in Amazon Quick.
- 
                                    **AUTHOR PRO**– The user is able to perform all actions of a Amazon Quick Author and utilize applicable Amazon Quick Generative BI capabilities. For more information about Pro roles in Amazon Quick, see[Get started with Generative BI](https://docs.aws.amazon.com/quicksight/latest/user/generative-bi-get-started.html).
 
- 
                                    
- 
                            **READER roles (Enterprise only)**:- 
                                    **READER**– Users are able to interact with shared dashboards, but not author analyses or dashboards or perform any administrative tasks.
- 
                                    **READER PRO**– The user is able to perform all actions of a Amazon Quick Reader and utilize applicable Amazon Quick Generative BI capabilities. For more information about Pro roles in Amazon Quick, see[Get started with Generative BI](https://docs.aws.amazon.com/quicksight/latest/user/generative-bi-get-started.html).
 
- 
                                    
 
- 
                            
- 
                    For **IAM User**, verify that it says**Yes**for accounts that are associated with IAM users, and**No**for those that are Amazon Quick-only.
- 
                    (Optional) To delete a user, choose the delete icon at the end of the relevant row. 
- 
                    Choose **Invite**.

## Viewing Amazon Quick account details

            | Intended audience: Amazon Quick administrators | 

You can view Amazon Quick accounts on the **Manage Users** page.
                To view a Amazon Quick user account, use the following procedure. 

- 
                    Choose your user name on the application bar and then choose **Manage Quick**.
- 
                    Choose **Manage Users**to view details about people who are Amazon Quick users. The information that displays includes:- 
                            Username – The person's user name. 
- 
                            Email – The email associated with this user name. 
- 
                            Role – The security cohort that the person's user name belongs to: **ADMIN**,**ADMIN PRO**,**AUTHOR**,**AUTHOR PRO**,**READER**, or**READER PRO**.
- 
                            Last active – The last date and time that this person accessed the Amazon Quick console. Anyone who isn't an active user has a **Last active**status of`User has no activity`.
 You can also see deleted or inactive users in this screen. 
- 
                            
- 
                    To find a user name, enter a part or all of a user's name or email the search box. Search is case-insensitive and wildcards aren't supported. To clear the search results and view all user names, delete your search entry. 

## Deleting a Amazon Quick user account

            | Intended audience: Amazon Quick administrators | 

###### Warning

**Deleting user accounts has permanent, organization-wide 
                    consequences.** When you delete a user account:

- 
                        All user-owned resources are permanently removed unless explicitly transferred to another user before deletion 
- 
                        Shared dashboards and analyses become inaccessible to other users if the deleted user was the owner 
- 
                        Data sources and datasets owned by the user are deleted, potentially breaking dependent analyses across your organization 
- 
                        **This action cannot be undone - deleted resources cannot be recovered**

Always transfer critical resources to another user before deleting an account. Review all user-owned assets using the asset management console before proceeding with any account deletion.

Accounts can be deleted by either an AWS administrator or an Amazon Quick administrator. Deleting a Amazon Quick user account works the same in both the Standard and Enterprise editions of Amazon Quick.

Deleting a Amazon Quick user account removes or transfers their resources. In
                Enterprise edition, the network administrator can temporarily deactivate a
                Amazon Quick user account by removing it from the network group that has access to
                Amazon Quick. If a user is deleted, but not deactivated, that user can still access
                Amazon Quick as a new user. For more information about deactivating an Enterprise
                account, see [Deactivating user accounts](https://docs.aws.amazon.com/quicksight/latest/user/deactivate-user-groups-enterprise.html).

Use the following procedure to delete a Amazon Quick user account.

- 
                    Choose your user name on the application bar and then choose **Manage Quick**.
- 
                    Choose **Manage Users**.
- 
                    Locate the account you want to delete and then choose the delete icon at the end of that row. 
- 
                    Choose to either delete or transfer any resources owned by the user and then choose **OK**.
- 
                    Do one of the following: - 
                            If you chose to transfer user resources, enter the user name of the account to transfer them to and then choose **Delete and transfer resources**.
- 
                            If you chose to delete user resources, choose **Delete**. You can't undo this action.
 
-