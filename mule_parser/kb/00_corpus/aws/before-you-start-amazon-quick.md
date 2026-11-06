# Before you start - Amazon Quick

**Source:** [https://docs.aws.amazon.com/quick/latest/userguide/share-a-dashboard-grant-access-anyone-prerequisites.html](https://docs.aws.amazon.com/quick/latest/userguide/share-a-dashboard-grant-access-anyone-prerequisites.html)

---

Before you can share a dashboard with anyone on the internet, make sure to do the following:

- 
							Turn on session capacity pricing on your account. If you have not turned on session capacity pricing on your account, you won't be able to update your account's public sharing settings. 
- 
							Assign public sharing permissions to an administrative user in the IAM console. You can add these permissions with a new policy or you can add the new permissions to an existing user. The following sample policy provides permissions for use with `UpdatePublicSharingSettings`.- 
            
                
                `{ "Version":"2012-10-17", "Statement": [ { "Action": "quicksight:UpdatePublicSharingSettings", "Resource": "*", "Effect": "Allow" } ] }`
 Accounts that don't want users with administrator access to use this feature can add an IAM policy that denies public sharing permissions. The following sample policy denies permissions for use with `UpdatePublicSharingSettings`.- 
            
                
                `{ "Version":"2012-10-17", "Statement": [ { "Action": "quicksight:UpdatePublicSharingSettings", "Resource": "*", "Effect": "Deny" } ] }`
 For more information on using IAM with Quick Sight, see [Using Quick with IAM](./security_iam_service-with-iam.html).You can also use the "Deny" policy as a Service Control Policy (SCP) if you don't want any of the accounts in your organization to have the public sharing feature. For more information, see [Service control policies (SCPs)](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_scps.html)in the*AWS Organizations User Guide*.
- 
							Turn on public sharing on your Amazon Quick account. - 
									From the Amazon Quick start page, choose your user icon at the upper right of your browser window, and then choose **Manage Quick**.
- 
									In the page that opens, scroll down to the **Permissions**section.
- 
									Choose **Public access to dashboards**at left.
- 
									On the page that opens, choose **Anyone on the internet**.When you turn on this setting, a pop up will appear asking you to confirm your choice. Once you've confirmed your choice, you can grant the public access to specific dashboards and share those dashboards with them with a link or by embedding the dashboard in a public application, wiki, or portal. 
 
-