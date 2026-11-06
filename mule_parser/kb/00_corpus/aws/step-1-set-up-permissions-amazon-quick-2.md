# Step 1: Set up permissions - Amazon Quick

**Source:** [https://docs.aws.amazon.com/quick/latest/userguide/embedded-analytics-full-console-for-authenticated-users-get-step-1.html](https://docs.aws.amazon.com/quick/latest/userguide/embedded-analytics-full-console-for-authenticated-users-get-step-1.html)

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

Each user who accesses a Amazon Quick Sight assumes a role that gives them
                Amazon Quick Sight access and permissions to the console session. To make this
                possible, create an IAM role in your AWS account. Associate an IAM policy with the
                role to provide permissions to any user who assumes it. Add
                    `quicksight:RegisterUser` permissions to ensure that the reader can
                access Amazon Quick Sight in a read-only fashion, and not have access to any other
                data or creation capability. The IAM role also needs to provide permissions to
                retrieve console session URLs. For this, you add
                    `quicksight:GetSessionEmbedUrl`.

The following sample policy provides these permissions for use with
                    `IdentityType=IAM`. 

- 
            
                
                `{ "Version":"2012-10-17", "Statement": [ { "Action": "quicksight:RegisterUser", "Resource": "*", "Effect": "Allow" }, { "Action": "quicksight:GetSessionEmbedUrl", "Resource": "*", "Effect": "Allow" } ] }`

The following sample policy provides permission to retrieve a console session URL.
                You use the policy without `quicksight:RegisterUser` if you are creating
                users before they access an embedded session.

- 
            
                
                `{ "Version":"2012-10-17", "Statement": [ { "Effect": "Allow", "Action": [ "quicksight:GetSessionEmbedUrl" ], "Resource": "*" } ] }`

If you use `QUICKSIGHT` as your `identityType` and provide
                the user's Amazon Resource Name (ARN), you also need to allow the
                    `quicksight:GetAuthCode` action in your policy. The following sample
                policy provides this permission.

- 
            
                
                `{ "Version":"2012-10-17", "Statement": [ { "Effect": "Allow", "Action": [ "quicksight:GetSessionEmbedUrl", "quicksight:GetAuthCode" ], "Resource": "*" } ] }`

Your application's IAM identity must have a trust policy associated with it
                to allow access to the role that you just created. This means that when a user
                accesses your application, your application can assume the role on the user's
                behalf and provision the user in Amazon Quick Sight. The following example shows a
                role called `embedding_quicksight_console_session_role`, which has the
                sample policy preceding as its resource. 

For more information regarding trust policies for OpenID Connect or SAML
                authentication, see the following sections of the *IAM User
                    Guide: *