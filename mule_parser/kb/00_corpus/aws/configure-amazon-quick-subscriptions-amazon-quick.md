# Configure Amazon Quick subscriptions - Amazon Quick

**Source:** [https://docs.aws.amazon.com/quick/latest/userguide/managing-qbs-subscriptions.html](https://docs.aws.amazon.com/quick/latest/userguide/managing-qbs-subscriptions.html)

---

You can purchase standard user subscriptions to get discounted pricing on Amazon Quick. When you invite additional users to Quick, you're charged for those accounts on a month-by-month basis. If you have Enterprise edition, you have the option to take advantage of pay-per-session pricing for reader accounts. These are users who only view data dashboards, and don't need author or admin access.

To understand how Amazon Quick subscription names on the pricing page map to user roles in
        the admin console, see [Understanding Amazon Quick subscriptions and roles](https://docs.aws.amazon.com/quicksuite/latest/userguide/user-types.html).

When you purchase an annual subscription, you pay for a Quick user account on an annual rather than monthly basis. With an annual subscription, you receive a discounted price in return for the extended time commitment. You don't need to purchase an annual subscription to create or add users.

When you purchase a set of standard user subscriptions, you choose the number of accounts you want to cover. You also choose when to start the subscriptions (any time from the month following the current month, to one year in the future) and whether to autorenew them. All subscriptions that you purchase together must use the same values for these settings.

You can edit an existing set of user subscriptions to change whether it autorenews. If the set is not yet active, you can also change the number of subscriptions it covers, or delete it entirely.

###### Topics

## Viewing current subscriptions

        Use the following procedure to view your current user subscriptions.

###### To view your current user subscriptions

- 
                Choose your user name on the application bar and then choose **Manage Quick**.
- 
                Choose **Manage pricing**.
- 
                Use the subscription meter to see how many accounts you have and how they are billed. In the following example, the account has 21 users total: - 
                        Seven users with annual subscriptions. Only currently active subscriptions are shown here. 
- 
                        13 month-to-month users. 
 Pause over any section of the meter bar to display details about that user segment. 
- 
                        
- 
                Use the information in the subscriptions table to see what current and future subscriptions you have. 

## Purchase subscriptions

        Use the following procedure to purchase subscriptions.

###### To purchase subscriptions

- 
                Choose your user name on the application bar and then choose **Manage Quick**.
- 
                Choose **Manage pricing**.
- 
                Navigate to the **Authors and Admins**section, and then choose**Purchase plan**.
- 
                Choose or enter the number of subscriptions you want. 
- 
                Choose the month and year when the subscriptions will start. 
- 
                Choose whether the subscriptions autorenew. 
- 
                Choose **Purchase**.

## Editing a subscription

        Use the following procedure to edit subscriptions.

###### To edit subscriptions

- 
                Choose your user name on the application bar and then choose **Manage Quick**.
- 
                Choose **Manage pricing**.
- 
                Next to the set of subscriptions you want to change, choose **Manage**.
- 
                (Optional) If the subscriptions haven't started yet, change the number of subscriptions. 
- 
                Choose whether the subscriptions autorenew. 
- 
                Choose **Save changes**.

## Delete a subscription

        ###### Warning

Deleting Amazon Quick subscriptions affects user access. When you delete subscriptions:

- Users covered by deleted subscriptions may lose access to Quick features and content 
- Subscription changes affect your entire organization's access to Quick capabilities 
- Deleted subscriptions cannot be recovered - you must purchase new subscriptions to restore access 

**Before proceeding:** Verify that affected users have alternative 
                access methods and understand the implications of subscription changes.

Use the following procedure to delete subscriptions. You can only delete subscriptions that haven't started yet.

###### To delete subscriptions

- 
                Choose your user name on the application bar and then choose **Manage Quick**.
- 
                Choose **Manage pricing**.
- 
                Next to the set of subscriptions that you want to delete, choose **Edit**.
- 
                Choose **Delete Subscription**.

###### Note

If you use AWS Key Management Service or AWS Secrets Manager with Amazon Quick, you are billed for access and maintenance as described in the pricing pages for each AWS product. For more information on how these products are billed, see the following:

In your billing statement, the costs are itemized under the appropriate product and not under Amazon Quick.

## Upgrading your Amazon Quick subscription from Standard edition to Enterprise edition

        You can upgrade from Amazon Quick Standard edition to Amazon Quick Enterprise edition. In Enterprise edition, Amazon Quick supports the following additional features:

- 
                Reader role with pay-per-session pricing; for more pricing details, see following. 
- 
                Email reports for offline delivery of insights. 
- 
                Larger SPICE datasets with up to 500 million rows per SPICE dataset. 
- 
                Hourly refresh of SPICE data (using the Amazon Quick console). 
- 
                **ML Insights**to make the most of your data, including the following:- 
                        Anomaly detection that can run on billions of rows of data on a schedule. 
- 
                        Contribution analysis to help you figure out key drivers. 
- 
                        One-click forecasting. 
- 
                        Customizable natural language narratives that you can use to add business context to a dashboard. 
- 
                        SageMaker AI integration. 
 
- 
                        
- 
                **Embedded analytics**in applications and portals:- 
                        Embed dashboards with row level security. 
- 
                        Namespaces with multitenant support for creating dashboards with embedded analytics. 
- 
                        Templates for repeatable dashboard creation and management. 
- 
                        Capacity pricing for embedding. 
 
- 
                        
- 
                **Security and governance**- 
                        Row-level security. 
- 
                        Private virtual private cloud (VPC) support based on Amazon VPC. 
- 
                        Folders for organization and sharing. 
- 
                        Fine-grained access control over Amazon S3, Amazon Athena, and other AWS services and resources. 
- 
                        AWS Lake Formation support. 
 
- 
                        
- 
                **User authentication and management options**- 
                        Integration with Microsoft Active Directory with support for Active Directory groups. 
- 
                        Group support for user management. 
 
- 
                        

To see a full comparison of Standard edition with Enterprise edition, see [ Amazon Quick
                editions](https://aws.amazon.com/quicksight/resource-library/editions/).

When you upgrade your account, your administrators and authors are billed at the Amazon Quick Enterprise edition rates. For pay-per-session pricing, you can add additional users as readers. Before you reprovision existing users as readers, you transfer or delete their resources, and then delete the users from your subscription.

Users who are in the reader role can view and manipulate shared dashboards, and receive emailed updates. However, readers can't add or change data sources, datasets, analyses, visuals, or administrative settings. Billing for readers is significantly lower in cost than regular user pricing. It's based on 30-minute sessions, and it's capped at a maximum amount per month for each reader. Billing for upgrades is prorated for the month of the upgrade. Upgrades to users are also prorated. If you have an annual subscription to Standard edition, it's converted to Enterprise edition and stays in place for the remaining term.

###### Warning

Downgrading from Enterprise edition to Standard edition isn't currently possible due to the enhanced feature set available in Enterprise edition. To perform this downgrade, unsubscribe from Amazon Quick, and then start a new subscription. Also, you can't transfer users or assets between subscriptions.

Upgrading to Enterprise edition to use Active Directory connectivity isn't supported. This is because of the differences in the user identity mechanisms between Amazon Quick password-based users and existing Active Directory users. However, you can upgrade to Enterprise and still use password-based users. If you want to upgrade and change how users sign in, you can unsubscribe and start a new subscription.

Use the following procedure to upgrade to Enterprise edition. To perform the upgrade, you need administrative access to Amazon Quick, with security permissions to subscribe. The person performing the upgrade is usually an AWS administrator who is also an Amazon Quick administrator.

###### To upgrade to enterprise edition

- 
                Open the administrative settings page by clicking on your profile icon at top right. 
- 
                At top left, choose **Upgrade now**.
- 
                Be sure that you want to upgrade. ###### ImportantYou can't undo this action. Choose **Upgrade**to upgrade. The upgrade is instantaneous.Billing for the upgrade to your subscription is prorated for the month of upgrade. Upgrades to Amazon Quick users are also prorated. 
- 
                (Optional) Downgrade users to readers: - 
                        Before you start, make sure to transfer any assets your users own that you want to keep. 
- 
                        Delete the users and add them back to your subscription as readers. If you're using Active Directory, delete the authors, move them to the new reader group, then recreate them as readers in Amazon Quick. 
 When you upgrade to Enterprise edition, your admin and author users retain their roles. 
-