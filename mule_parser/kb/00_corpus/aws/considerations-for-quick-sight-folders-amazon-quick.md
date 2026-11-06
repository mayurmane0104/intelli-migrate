# Considerations for Quick Sight folders - Amazon Quick

**Source:** [https://docs.aws.amazon.com/quick/latest/userguide/folders-limitations.html](https://docs.aws.amazon.com/quick/latest/userguide/folders-limitations.html)

---

Before you get started creating and modifying folders in Amazon Quick Sight, review the following limitations that apply to Quick Sight folders.

- 
                You can't share folders in your AWS account with people in other AWS accounts. 
- 
                For people who have Quick reader permissions, the following limitations apply: - 
                        Readers can't own a personal or shared folder. 
- 
                        Readers can't create or manage folders or folder content. 
- 
                        Readers can't have the *contributor*access level.
- 
                        In shared folders, readers can only see dashboard assets. 
 
- 
                        

In addition, these limitations apply specifically to shared folders:

- 
                The name of a shared folder (at the top level of the tree) must be unique in your AWS account. 
- 
                In a single folder, multiple assets can't have the same name. For example, in your top-level folder, you can't create two subfolders with the same name. In the same folder, you can't add two assets with the same name, even if they have different asset IDs. The path to each asset behaves like an Amazon S3 key name. It must be unique in your AWS account. 
- 
                Restricted shared folders can only be created with the Quick Sight CLI. 

See [Overview of Quick Sight folders](./folders-functionality.html) to
            learn more about the different types of folder available in Amazon Quick Sight.