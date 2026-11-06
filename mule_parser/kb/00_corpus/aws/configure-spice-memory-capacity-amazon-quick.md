# Configure SPICE memory capacity - Amazon Quick

**Source:** [https://docs.aws.amazon.com/quick/latest/userguide/managing-spice-capacity.html](https://docs.aws.amazon.com/quick/latest/userguide/managing-spice-capacity.html)

---

*SPICE (Super-fast, Parallel, In-memory Calculation
                Engine)* is the robust in-memory engine that Amazon Quick uses.
        It's engineered to rapidly perform advanced calculations and serve data. In Enterprise
        edition, data stored in SPICE is encrypted at rest. For more information, see
            [Data
            encryption in Quick](https://docs.aws.amazon.com/quicksight/latest/user/data-encryption.html).

SPICE capacity is allocated separately per AWS Region. For each AWS account, SPICE capacity is shared by all the people using Quick in a single AWS Region. The other AWS Regions have no SPICE capacity unless you choose to purchase some.

Quick administrators can view how much [SPICE](https://docs.aws.amazon.com/quicksight/latest/user/spice.html) capacity you
        have in each AWS Region and how much of it is currently in use. Administrators can also
        purchase additional SPICE capacity or release unused SPICE
        capacity. You can only release SPICE capacity that isn't currently used by a
        dataset. Datasets in SPICE stay there until someone remove them from
            SPICE. To change that, you can either delete the datasets or change them
        so they aren't stored in SPICE. 

Purchasing or releasing SPICE capacity only affects the capacity for the currently selected AWS Region. Each AWS account can have a separate Amazon Quick subscription and can be used in multiple AWS Regions.

Before you make any changes to SPICE capacity, make sure that you're using the correct AWS account and AWS Region. It's possible to be using different AWS accounts or AWS Regions at the same time in different contexts, as follows:

- 
            If you open Amazon Quick using the `http://quicksight.aws.amazon.com`URL, Amazon Quick automatically selects your account and AWS Region. You can't view your AWS account from Amazon Quick. We recommend using a different method to open Amazon Quick when you want to work with SPICE capacity.
- 
            If you open Amazon Quick from the AWS Management Console, Amazon Quick opens in the account that you used to sign in to that console. However, it opens in the last AWS Region that you selected in Amazon Quick. The AWS Management Console and the Amazon Quick console each have an AWS Region selector that works independently from the other. Changing the selected AWS Region in the AWS console doesn't change the AWS Region in Amazon Quick. 
- 
            If you use the AWS Command Line Interface (AWS CLI) to run Amazon Quick commands, make sure to provide the relevant AWS account for each Amazon Quick API operation you use. The AWS Region isn't always required, and if you don't provide it, the AWS CLI uses your default AWS Region from your AWS configuration. We recommend that you always explicitly provide the AWS Region, to make sure you apply the command to the correct AWS Region. 

You must be signed in as a Amazon Quick administrator to view or manage SPICE capacity.

###### Topics

## Finding your current AWS account and AWS Region

        ###### To select the correct AWS account and AWS Region (console)

- 
                Open the AWS console, using the AWS account that you want to view SPICE information for. If you have only one AWS account, you can skip this step. You can verify the account number by following these steps: - 
                        On the navigation bar at the top of the page, choose the account name or number at right. If a number displays, this might be your AWS account ID. 
- 
                        Choose **My Security Credentials**to display your credential-related information and options. Your AWS account ID displays near the top of the page.
 To return to the original page, choose the AWS logo at upper left. 
- 
                        
- 
                Open Amazon Quick by first entering " `quicksight`" into the**Find Services**search box. When the word Amazon Quick appears following the search box, choose it from the list.
- 
                In Amazon Quick, open the profile menu by choosing your profile icon at top right. The AWS name of the AWS Region that Amazon Quick is using displays in the menu. The same AWS Region also displays in the URL, for example: `https://`. If this is your URL, the profile menu displays the name N. Virginia.`us-east-1`.quicksight.aws.amazon.com/sn/adminTo switch AWS Regions, display the list of supported Regions by choosing the Region name from the profile menu. Then choose the Region that you want to use. Switching to a different AWS Region changes the SPICE usage information that you can view. It also changes the Amazon Quick assets that you can use, for example data sources and dashboards. 

## Viewing SPICE capacity and usage in an AWS Region

        ###### To view current SPICE capacity and usage (console)

- 
                Open Amazon Quick. Make sure that you're using the correct AWS account and AWS Region as described previously in [Finding your current AWS account and AWS Region](https://docs.aws.amazon.com/quicksight/latest/user/current-aws-account-and-default-aws-region.html).
- 
                Open the administration page by choosing **Manage Quick**from your profile menu.
- 
                Choose **SPICE capacity**from the left navigation pane . The following information displays:- 
                        The **Total SPICE capacity**section displays the total amount of used and unused SPICE capacity. A bar graph shows how much of this storage space is in each of the following categories for this AWS account in the AWS Region that's currently selected in Amazon Quick:- 
                                Purchased SPICE capacity – This is the additional SPICE capacity. 
- 
                                SPICE capacity bundled with Amazon Quick – This is the total default capacity associated with your paid users. 
 Hover over any section of the meter to see details on that capacity type. 
- 
                                
- 
                        The **SPICE usage**section displays the total amount of the used and unused SPICE capacity. A bar graph shows how much of this storage space is in each of the following categories for this AWS account in the AWS Region that's currently selected in Amazon Quick:- 
                                Used SPICE capacity – This is the used portion of the default SPICE capacity that you get for each user. 
- 
                                Unused SPICE capacity – This is the unused portion of the default SPICE capacity that you get for each user. 
- 
                                Releasable unused capacity – This is the purchased capacity that isn't in use, and so can be released to reduce costs. 
 
- 
                                
 
- 
                        

## Hiding SPICE capacity labels

        Amazon Quick account admins can choose to hide the account-wide SPICE
            capacity usage and remaining size labels from Amazon Quick authors. This feature is
            available to all enterprise accounts that use custom permissions. For more information
            about custom permissions in Amazon Quick, see [Customizing access to Amazon Quick capabilities](https://docs.aws.amazon.com/quicksight/latest/user/customizing-permissions-to-the-quicksight-console.html)

Use the following procedure to hide SPICE capacity usage from the Amazon Quick console.

- 
	Open the [Quick console](https://quicksight.aws.amazon.com/).
- 
                From any page in the Amazon Quick console, choose your profile name, and then choose **Manage Quick**.The **Manage Quick**menu is only available to Amazon Quick admins. If you are unable to acces this menu, contact your Amazon Quick account admin for assistance.
- 
                Choose **Manage users**, and then choose**Manage permissions**.
- 
                Edit or create a new custom permission. For **Restrict access to**, under**Datasets**, select**Viewing account SPICE capacity**.
- 
                When you are finished creating or changing the custom permission, chose **Create**or**Update**.

After you create or update a custom permission to hide SPICE capacity
            usage, assign the new permission to users with the `UpdateUser` API.

## Purchasing SPICE capacity in an AWS Region

        ###### To purchase more SPICE capacity (console)

- 
                Open Amazon Quick. Make sure that you're using the correct AWS account and AWS Region as described previously in [Finding your current AWS account and AWS Region](https://docs.aws.amazon.com/quicksight/latest/user/current-aws-account-and-default-aws-region.html).
- 
                Open the administration page by choosing **Manage Quick**from your profile menu.
- 
                Choose **SPICE capacity**from the left navigation pane .
- 
                Choose the **Purchase more capacity**button.
- 
                Enter a number of gigabytes of SPICE capacity to purchase for the AWS Region that is currently selected in Amazon Quick. 
- 
                To confirm your choice, choose **Purchase SPICE capacity**. To exit without making any changes, choose**Cancel**.

## Turning on SPICE auto capacity purchasing

        Turn on SPICE auto capacity purchasing to allow Amazon Quick to automatically manage your Amazon Quick account's SPICE capacity. When you turn auto capacity purchasing on, Amazon Quick evaluates how much capacity is needed based on your account's usage. As your account uses more SPICE storage, Amazon Quick automatically purchases SPICE capacity as needed on your behalf. This allows users to ingest data as needed without the need to estimate usage or manually purchase SPICE data. Auto capacity purchasing makes it easier for new customers, ISVs, and larger companies to directly access SPICE without needing to understand, track, or manually purchase their account's SPICE capacity. Amazon Quick admins can still purchase and release SPICE capacity manually.

Auto capacity purchasing doesn't support auto-decrement. If users want to reduce their SPICE usage, capacity release must be done manually.

By default, all new Amazon Quick accounts that are created in the Amazon Quick console
            have auto capacity purchasing turned on in the region that their capacity is located. To
            turn on auto capacity purchasing for other regions, Amazon Quick account admins can
            manually turn on auto capacity from the **SPICE capacity** management
            page.

By default, all new Amazon Quick accounts that were created with the Amazon Quick API
            and all existing Amazon Quick accounts have auto capacity purchasing turned off. To turn
            on auto capacity purchasing, Amazon Quick account admins can manually turn on auto
            capacity from the **SPICE capacity** management page.

###### To turn SPICE capacity purchasing on or off

- 
	Open the [Quick console](https://quicksight.aws.amazon.com/).
- 
                From any page in the Amazon Quick console, choose your profile name, and then choose **Manage Quick**.The **Manage Quick**menu is only available to Amazon Quick admins. If you are unable to acces this menu, contact your Amazon Quick account admin for assistance.
- 
                Choose **SPICE capacity**.
- 
                On the **SPICE Capacity**page that opens, toggle the**Auto-purchase capacity**on.

To turn auto capacity purchasing off, follow the procedure above and toggle
                **Auto-purchase capacity** off. When auto purchase capacity is
            turned off, ingestions or refreshes that exceed the account's SPICE
            capacity automatically fail.

Amazon Quick admins can turn auto capacity pricing on or off at any time. If you turn auto capacity purchasing off after it's been in use, your account's current capacity becomes your account's purchased capacity. If your account has no remaining capacity when you turn auto purchase off, the next ingestion or refresh will fail.

If your account already exceeds its SPICE capacity when you turn auto capacity purchasing on, Amazon Quick automatically matches your account's capacity to your current usage. After Amazon Quick matches your account's capacity, the auto-purchase logic starts.

## Releasing SPICE capacity in an AWS Region

        ###### To release unused SPICE capacity (console)

- 
                Open Amazon Quick. Make sure that you're using the correct AWS account and AWS Region as described previously in [Finding your current AWS account and AWS Region](https://docs.aws.amazon.com/quicksight/latest/user/current-aws-account-and-default-aws-region.html).
- 
                Open the administration page by choosing **Manage Quick**from your profile menu.
- 
                Choose **SPICE capacity**from the left navigation pane .
- 
                Choose **Release unused purchased capacity**.
- 
                Do one of the following: - 
                        To release all SPICE capacity from the AWS Region that is currently selected in Amazon Quick, choose **Release all**.
- 
                        To release some of gigabytes of SPICE capacity from the AWS Region that is currently selected in Amazon Quick, enter the number of gigabytes to release. 
 
- 
                        
- 
                To confirm your choice, choose **Release SPICE capacity**. To exit without making any changes, choose**Cancel**.