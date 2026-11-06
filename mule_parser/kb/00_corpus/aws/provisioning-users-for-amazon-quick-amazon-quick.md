# Provisioning users for Amazon Quick - Amazon Quick

**Source:** [https://docs.aws.amazon.com/quick/latest/userguide/provisioning-users.html](https://docs.aws.amazon.com/quick/latest/userguide/provisioning-users.html)

---

| Applies
                    to:Enterprise Edition and Standard Edition | 

| Intended audience: System administrators and Amazon Quick administrators | 

## Self-provisioning an Amazon Quick administrator

            Amazon Quick administrators are users who can also manage Amazon Quick features
                such as account settings and accounts. They can also purchase additional
                Amazon Quick user subscriptions, purchase [SPICE](https://docs.aws.amazon.com/quicksight/latest/user/spice.html), and
                cancel the subscription to Amazon Quick for your AWS account.

You can use an AWS user or group policy to give users the ability to add
                themselves as administrators of Amazon Quick. Users that have been granted this
                ability can only add themselves as administrators and can't use this policy to add
                others. Their accounts become active and billable the first time that they open
                Amazon Quick. To set up self-provisioning, give these users permission to use the
                    `quicksight:CreateAdmin` action. 

Alternatively, you can use the following procedure to use the console to set or create the administrator for Amazon Quick.

###### To make a user the Amazon Quick administrator

- 
                    Create the AWS user: - 
                            Use IAM to create the user that you want to be the administrator of Amazon Quick. Alternatively, identify an existing user in IAM for the administrator role. You can also put the user inside a new group, for manageability. 
- 
                            Grant the user (or group) sufficient permissions. 
 
- 
                            
- 
                    Sign in to your AWS Management Console with the target user's credentials. 
- 
                    Go to [http://quicksight.aws.amazon.com/sn/console/get-user-email](http://quicksight.aws.amazon.com/sn/console/get-user-email), type in the target user's email address, and choose**Continue**.

On success, the target user is now an administrator in Amazon Quick.

## Self-provisioning an Amazon Quick author

            Amazon Quick authors can create data sources, datasets, analyses, and dashboards.
                They can share analyses and dashboards with other Amazon Quick users in your
                Amazon Quick account. However, they don't have access to the **Manage
                    Amazon Quick** menu. They can't change account settings, manage
                accounts, purchase additional Amazon Quick user subscriptions or [SPICE](https://docs.aws.amazon.com/quicksight/latest/user/spice.html)
                capacity, or cancel the subscription to Amazon Quick for your AWS account. Author
                Pro users can additionally create content using natural language, build knowledge
                bases, configure actions, and access advanced automation capabilities.

You can use an AWS user or group policy to give users the ability
                to create an Amazon Quick author account for themselves. Their accounts become
                active and billable the first time they open Amazon Quick. To set up
                self-provisioning, you need to give them permission to use the
                    `quicksight:CreateUser` action. 

## Self-provisioning an Amazon Quick read-only user

            Amazon Quick read-only users or *readers* can view and
                manipulate dashboards that are shared with them, but they can't make any changes or
                save a dashboard for further analysis. Amazon Quick readers can't create data
                sources, datasets, analyses, or visuals. They can't do any administrative tasks.
                Choose this role for people who are consumers of the dashboards but don't author
                their own analysis, for example, executives. Reader Pro users have access to
                advanced features including AI chat agents, collaborative spaces, flows, and
                extensions.

If you are using Microsoft Active Directory with Amazon Quick, you can manage read-only permissions by using a group. Otherwise, you can bulk-invite users to use Amazon Quick. You can also use an AWS user or group policy to give people the ability to create an Amazon Quick reader account for themselves.

Reader accounts become active and billable the first time they open Amazon Quick.
                If you decide to upgrade or downgrade a user, billing for that user is prorated for
                the month. To set up self-provisioning, you need to give them permission to use the
                    `quicksight:CreateReader` action. 

Readers that are used to automatically or programmatically refresh dashboards for near real-time use cases must choose capacity pricing. For readers under user pricing, each reader is limited to manual use by one individual only.