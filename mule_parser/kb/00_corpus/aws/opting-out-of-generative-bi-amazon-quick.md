# Opting out of Generative BI - Amazon Quick

**Source:** [https://docs.aws.amazon.com/quick/latest/userguide/generative-bi-opt-out.html](https://docs.aws.amazon.com/quick/latest/userguide/generative-bi-opt-out.html)

---

Quick accounts are charged if Generative BI is active in the account. Generative BI is considered active if your account uses any of the following capabilities:

- 
                Pro users 
- 
                Topics 
- 
                Dashboard and visual indexing 
- 
                Dashboard Q&A 

To avoid being charged for Generative BI by completely deactivating it, perform the following steps.

###### Warning

Opting out of Generative BI will disable AI-powered features and stop related charges. This process involves:

- Removing or changing Pro user roles to standard roles 
- Deleting all topics in your account 
- Disabling dashboard indexing and Q&A features 

**Before proceeding:** Review the steps carefully and ensure 
                you understand which features will be disabled.

###### To opt out of Generative BI

- 
                Ensure there are no Pro users or user groups mapped to Pro roles in the account by performing the following steps: - 
                        To update or remove Pro users using APIs: - 
                                If you use Quick identity (with or without IAM federation): - 
                                        Find users that have Pro roles using the [ListUsers](https://docs.aws.amazon.com/quicksight/latest/APIReference/API_ListUsers.html)API.
- 
                                        Either change the users' roles using the [UpdateUser](https://docs.aws.amazon.com/quicksight/latest/APIReference/API_UpdateUser.html)API, or remove the users from the account using the[DeleteUser](https://docs.aws.amazon.com/quicksight/latest/APIReference/API_DeleteUser.html)API.
 
- 
                                        
- 
                                If you use IAM Identity Center or Microsoft Active Directory: - 
                                        Find group of users mapped to Pro roles using the [ListRoleMemberships](https://docs.aws.amazon.com/quicksight/latest/APIReference/API_ListRoleMemberships.html)API.
- 
                                        Create new user groups with the same users, but mapped to different roles, using the [CreateRoleMemberships](https://docs.aws.amazon.com/quicksight/latest/APIReference/API_CreateRoleMemberships.html)API.
- 
                                        Delete the previous user groups mapped to Pro roles using the [DeleteRoleMemberships](https://docs.aws.amazon.com/quicksight/latest/APIReference/API_DeleteRoleMemberships.html)API.
 
- 
                                        
 
- 
                                
- 
                        To update or remove Pro users using the Quick console: - 
	Open the [Quick console](https://quicksight.aws.amazon.com/).
- 
                                Choose the profile icon, then choose **Manage Quick**.
- 
                                If necessary, in the left navigation pane, choose **Manage users**.- 
                                        If you use Quick identity (with or without IAM federation), update user roles or delete users using the steps in [Viewing Amazon Quick account details](./managing-user-access-qs-iam.html#view-user-accounts)or[Deleting a Amazon Quick user account](./managing-user-access-qs-iam.html#delete-a-user-account).
- 
                                        If you use IAM Identity Center or Microsoft Active Directory, update group and role mappings or delete user groups using the steps in [Managing user access](./managing-user-access-idc.html#view-user-accounts-enterprise).
 
- 
                                        
 
- 
	
 
- 
                        
- 
                Ensure there are no topics in the account by performing the following steps: - 
                        Use the [ListTopics](https://docs.aws.amazon.com/quicksight/latest/APIReference/API_ListTopics.html)API to list all topics in the account for each AWS Region where topics are used.
- 
                        For each topic, do one of the following: - 
                                If you are an owner or co-owner of the topics, delete the topics using the [DeleteTopic](https://docs.aws.amazon.com/quicksight/latest/APIReference/API_DeleteTopic.html)API.
- 
                                If you're not an owner or co-owner of the topics: - 
                                        Identify the owners of each topic using the [DescribeTopicPermissions](https://docs.aws.amazon.com/quicksight/latest/APIReference/API_DescribeTopicPermissions.html)API, then ask them to delete their topics using the[DeleteTopic](https://docs.aws.amazon.com/quicksight/latest/APIReference/API_DeleteTopic.html)API.
- 
                                        Make yourself a co-owner of the topics using the [UpdateTopicPermissions](https://docs.aws.amazon.com/quicksight/latest/APIReference/API_UpdateTopicPermissions.html)API , then delete the topics using the[DeleteTopic](https://docs.aws.amazon.com/quicksight/latest/APIReference/API_DeleteTopic.html)API.
 
- 
                                        
 
- 
                                
 
- 
                        
- 
                Ensure that dashboard and visual indexing and Dashboard Q&A are disabled by performing the following steps: - 
                        To disable dashboard and visual indexing and Dashboard Q&A using APIs: - 
                                Disable dashboard and visual indexing using the [UpdateQuickSightQSearchConfiguration](https://docs.aws.amazon.com/quicksight/latest/APIReference/API_UpdateQuickSightQSearchConfiguration.html)API.
- 
                                Disable Dashboard Q&A using the [UpdateDashboardsQAConfiguration](https://docs.aws.amazon.com/quicksight/latest/APIReference/API_UpdateDashboardsQAConfiguration.html)API.
 
- 
                                
- 
                        To disable dashboard and visual indexing and Dashboard Q&A using the Quick console: - 
	Open the [Quick console](https://quicksight.aws.amazon.com/).
- 
                                Choose the profile icon, then choose **Manage Quick**.
- 
                                Under the **Account**section, choose**Amazon Q**.
- 
                                Disable each of the options. 
 
- 
	
 
-