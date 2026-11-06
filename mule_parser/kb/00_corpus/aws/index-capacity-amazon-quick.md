# Index capacity - Amazon Quick

**Source:** [https://docs.aws.amazon.com/quick/latest/userguide/manage-data-capacity.html](https://docs.aws.amazon.com/quick/latest/userguide/manage-data-capacity.html)

---

An index is a structured corpus of documents that allows for efficient searching, sorting, and data access. Amazon Quick uses an index to store, prepare, sync any files you upload to your Quick spaces. It then uses this indexed data to generate agent-driven responses during chat conversations.

###### Topics

## Storage allocation

        You get index capacity measured as the original file size of documents at their source
            location (such as SharePoint, S3, Confluence) before any processing by
            Quick. Quick automatically creates an index when you sign up in
            your home region with auto-scaling enabled (a mechanism where your index capacity is
            adjusted automatically based on usage). Your Quick Index storage allocation
            is based on your user count and subscription tier. **Professional
            users** get 25 GB of storage per user and **Enterprise
            users** get 50 GB per user. Overages are billed at $5 per GB per month.
            Allocated storage and overages are pooled on a payer account level. This replaces the
            previously auto-provisioned 50 MB (extracted text) default index capability.

## Regional allocation

        Your Quick Index storage allocation is billed as a discount to your home region, the region you selected during your Quick subscription setup. If you provision Quick Index capacity in additional regions beyond your home region, that storage counts as overage and is billed at $5 per GB per month.

## Manual scaling & autoscaling

        You can purchase additional capacity via the Quick console in two ways. First, auto-purchase is enabled by default for all accounts. When your usage approaches your organizational allocation, the system automatically purchases additional capacity in 0.25 GB increments up to a maximum of 2 TB. Second, you can manually purchase capacity from 0.25 GB, up to 2 TB in 0.25 GB increments. The pre-populated auto-purchase limit is set to 2 TB, which you can adjust in the console. The default manual purchase amount is set to 0.25 GB. For manual purchase mode, you will be billed based on the storage capacity you have purchased, while in auto scale mode you will be billed based on 0.25 GB increment bundles, depending on how much you have consumed.

Quick Index has an auto-scaling limit currently set at 2 TB of storage per account, replacing the previous limit of 60 GB of extracted text. If you need to index more than 2 TB, please open a ticket with AWS support to extend this limit.

## Total index capacity

        You must purchase data storage capacity for your Amazon Quick index to ingest data
            from knowledge bases and upload files to spaces. In the index capacity page, the first
            horizontal bar shows your total index capacity. This is the current capacity available
            in your index to support file uploads and knowledge bases. You can switch between manual
            and auto-scaled index capacity modes as per your needs. When auto-scaling mode is
                **ON**, this capacity automatically adjusts to reflect the
            latest available capacity based on your ingestion needs. When manual mode is
                **ON**, this total capacity represents the actual capacity you have
            purchased for your account based on your estimate of the ingestion needs.

If you previously purchased Index capacity measured in extracted MBs of storage, your existing purchased capacity will be converted to the new Raw Storage dimension automatically. When buying capacity manually, you can also release unused capacity. If you want to release all provisioned index capacity, you can do so after deleting corresponding data—like file uploads in spaces and knowledge bases—in your Amazon Quick instance.

###### Note

With auto-scaling enabled, Amazon Quick may temporarily provision capacity above your maximum purchase limit during periods of high concurrent usage to maintain performance. However, you are only charged for capacity up to your configured maximum purchase limit, not for any temporary over-provisioning that occurs.

###### To manage purchase options

- 
                Log in to the Amazon Quick console. 
- 
                Select **Manage Quick**.
- 
                From the admin console left navigation menu, select **Subscriptions**, and then select**Index capacity**.
- 
                In **Index capacity**, from**Total index capacity**select**Manage capacity**, and do the following:- 
                        In **Manage purchase options**, do one of the following:- 
                                To automatically scale index capacity as per usage, select **Auto-scale (Recommended)**. This automatically adjusts index capacity in 0.25 GB increments based on your usage, purchasing or releasing as needed. Then, in**Maximum purchase limit**set the limit at which auto-purchase stops. The value of the maximum purchase limit must be 2 TB. Maximum purchase limit cannot be lower that current used capacity.
- 
                                To manually purchase capacity, select **Manual**. Then, in**Index capacity**, set the total capacity you want your index to hold. The capacity must be between 0.25 GB-2 TB and you can increase it in 0.25 GB increments. When you want to lower the current capacity held by the index, it can't be lowered below the used capacity. Since capacity is managed in 0.25 GB increments, you can only decrease to the next 0.25 GB unit above your current usage. For example, if your index has 2 GB capacity with 1.1 GB consumed, you can reduce capacity to 1.25 GB but not to 1 GB since part of the 1-1.25 GB unit is already in use.
 
- 
                                
- 
                        Select **Confirm**.
 
- 
                        

## To view index capacity usage

        The Amazon Quick admin console displays both your purchased index capacity and your index capacity usage. The following procedure shows you how to view them.

###### To view index data capacity usage

- 
                Log in to the Amazon Quick console. 
- 
                Select **Manage Quick**.
- 
                From the left navigation menu, select **Subscriptions**, and then select**Index capacity**.
- 
                In **Index capacity**, you'll find your capacity usage under**Index capacity usage**. First bar shows you total purchased capacity and second bar shows you index capacity usage.

## Release unused index capacity

        The Amazon Quick admin console displays both your purchased index capacity and your index capacity usage. If you've manually provisioned capacity, you can choose to release unused index capacity. If you've enabled auto-scaling for your index, you don't need to release index capacity as Amazon Quick automatically scales index capacity to your usage. The following procedure shows you how to release unused index capacity.

###### Note

To release any provisioned index capacity, you must delete all datasets and files uploaded to spaces. Then, follow the steps to release unused index capacity.

###### To release index data capacity

- 
                Log in to the Amazon Quick console. 
- 
                Select **Manage Quick**.
- 
                From the left navigation menu, select **Subscriptions**, and then select**Index capacity**.
- 
                In **Index capacity**, select**Manage capacity**.
- 
                In **Manage index capacity**, reduce the**Index capacity**to your desired value.

## Switch between capacity modes

        You can switch between manual and auto-scale index capacity modes at any time. When switching from auto-scale to manual, your current capacity becomes your fixed manual capacity. When switching from manual to auto-scale, you set a maximum purchase limit and Amazon Quick automatically adjusts capacity based on usage.

- 
                            Log in to the Amazon Quick console. 
- 
                            Select **Manage Quick**.
- 
                            From the admin console left navigation menu, select **Subscriptions**, and then select**Index capacity**.
- 
                            In **Index capacity**, from**Total index capacity**select**Manage capacity**.
- 
                            In **Manage index capacity**, select**Manual**.
- 
                            In **Index capacity**, set your desired manual capacity. The value must be between 0.25 GB-2 TB in 0.25 GB increments and can't be less than current usage.
- 
                            Select **Confirm**.