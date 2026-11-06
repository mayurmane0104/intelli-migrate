# Step 1: Set up permissions - Amazon Quick

**Source:** [https://docs.aws.amazon.com/quick/latest/userguide/embedded-dashboards-for-authenticated-users-get-step-1.html](https://docs.aws.amazon.com/quick/latest/userguide/embedded-dashboards-for-authenticated-users-get-step-1.html)

---

###### Important

Amazon Quick Sight has new APIs for embedding analytics:
                        `GenerateEmbedUrlForAnonymousUser` and
                        `GenerateEmbedUrlForRegisteredUser`.

You can still use the `GetDashboardEmbedUrl` and
                        `GetSessionEmbedUrl` APIs to embed dashboards and the
                    Amazon Quick Sight console, but they do not contain the latest embedding
                    capabilities. For the latest up-to-date embedding experience, see [Embedding Amazon Quick Sight analytics into your
                    applications](https://docs.aws.amazon.com/quicksight/latest/user/embedding-overview.html).

In the following section, you can find out how to set up permissions for the backend application or web server. This task requires administrative access to IAM.

Each user who accesses a dashboard assumes a role that gives them
                Amazon Quick Sight access and permissions to the dashboard. To make this possible,
                create an IAM role in your AWS account. Associate an IAM policy with the role to
                provide permissions to any user who assumes it. The IAM role needs to provide
                permissions to retrieve dashboard URLs. For this, you add
                    `quicksight:GetDashboardEmbedUrl`.

The following sample policy provides these permissions for use with
                    `IdentityType=IAM`. 

- 
            
                
                `{ "Version":"2012-10-17", "Statement": [ { "Effect": "Allow", "Action": [ "quicksight:GetDashboardEmbedUrl" ], "Resource": "*" } ] }`

The following sample policy provides permission to retrieve a dashboard URL. You
                use the policy with `quicksight:RegisterUser` if you are creating
                first-time users who are to be Amazon Quick Sight readers. 

- 
            
                
                `{ "Version":"2012-10-17", "Statement": [ { "Action": "quicksight:RegisterUser", "Resource": "*", "Effect": "Allow" }, { "Action": "quicksight:GetDashboardEmbedUrl", "Resource": "*", "Effect": "Allow" } ] }`

If you use `QUICKSIGHT` as your `identityType` and provide
                the user's Amazon Resource Name (ARN), you also need to allow the
                    `quicksight:GetAuthCode` action in your policy. The following sample
                policy provides this permission.

- 
            
                
                `{ "Version":"2012-10-17", "Statement": [ { "Effect": "Allow", "Action": [ "quicksight:GetDashboardEmbedUrl", "quicksight:GetAuthCode" ], "Resource": "*" } ] }`

Your application's IAM identity must have a trust policy associated with it
                to allow access to the role that you just created. This means that when a user
                accesses your application, your application can assume the role on the user's
                behalf and provision the user in Amazon Quick Sight. The following example shows a
                role called `embedding_quicksight_dashboard_role`, which has the sample
                policy preceding as its resource. 

For more information regarding trust policies for OpenID Connect or SAML
                authentication, see the following sections of the *IAM User
                    Guide: *