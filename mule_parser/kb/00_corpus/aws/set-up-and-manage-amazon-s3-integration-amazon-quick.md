# Set up and manage Amazon S3 integration - Amazon Quick

**Source:** [https://docs.aws.amazon.com/quick/latest/userguide/s3-setup-manage.html](https://docs.aws.amazon.com/quick/latest/userguide/s3-setup-manage.html)

---

## Set up Amazon S3 integration

        After your administrator has completed the setup tasks, follow these steps to create your Amazon S3 knowledge base.

- 
                In the Amazon Quick console, choose **Knowledge**.
- 
                Under **Amazon S3**, choose**Add**(the plus**+**button).
- 
                On the **Connect S3 bucket**page, choose your data source:- 
                        To reuse an existing Amazon S3 data source, select it from the dropdown. Then choose **Next**to skip to the knowledge base details step.
- 
                        To connect a new Amazon S3 bucket, choose **+ Add account**from the dropdown.
 
- 
                        
- 
                If you are connecting a new bucket, fill in the connection details: - 
                        **Name**– A descriptive name for your Amazon S3 integration.
- 
                        **S3 bucket location**– Choose**Quick Suite instance account**to access Amazon S3 buckets in the same AWS account where Amazon Quick is enabled, or choose**Other AWS account**to access buckets in a different account.
- 
                        **S3 bucket URL**– The Amazon S3 bucket path containing your documents. Your Amazon S3 bucket must be in the same region as your Amazon Quick region.
 Choose **Next**. The system validates your configuration. If errors occur, review the error message for specific remediation steps.###### NoteIf you receive an access error, contact your administrator to verify that your user has the required permissions for the Amazon S3 bucket. 
- 
                        
- 
                On the **Create knowledge base**page, complete the following:- 
                        **Name**– Enter a descriptive name for your knowledge base.
- 
                        **Description**– Describe the purpose of this knowledge base (optional).
- 
                        **Content**– Choose**Add all content**to sync everything from the bucket, or choose**Add specific content**to specify S3 prefixes for the folders and files you want to include. Filters are case-sensitive.
 
- 
                        
- 
                Choose **Next: Additional settings**to configure ACL and metadata options, or choose**Create**to create the knowledge base with default settings.
- 
                On the **Additional settings**page, configure ACL management and metadata:###### ImportantThe decision to enable or disable ACLs must be made during knowledge base creation. You cannot change this option after this step. For more information about ACLs, see [Document-level ACLs](./s3-acl.html).- 
                        To enable document-level ACLs, select **Control document access with ACLs**. When enabled, the following options appear:- 
                                **Global ACL file location**– Enter the Amazon S3 path to your global ACL file (e.g. acl.json) if you are using a global ACL configuration file for centralized access control management at the folder level.
- 
                                **Metadata files folder location**– Enter the Amazon S3 path to your metadata folder if you are using document-level metadata files that include ACL entries.
- 
                                If your metadata files use the sidecar method (stored in the same folder as the original documents), you can leave both fields blank. 
 
- 
                                
- 
                        You can optionally specify a **Metadata files folder location**even without ACLs enabled.
 
- 
                        
- 
                Choose **Create**.

After you choose create, the data sync starts automatically.

## Manage knowledge bases

        
        After setting up your Amazon S3 integration, you can create and manage knowledge bases from your Amazon S3 content.

### Edit existing knowledge bases

You can modify your existing Amazon S3 knowledge bases:

- 
                    In the Amazon Quick console, choose **Knowledge bases**.
- 
                    Select your Amazon S3 knowledge base from the list. 
- 
                    Choose the three-dot icon under **Actions**, then choose**Edit knowledge base**.
- 
                    Update your configuration settings as needed and choose **Save**.

### Create additional knowledge bases

You can create multiple knowledge bases from the same Amazon S3 integration:

- 
                    In the Amazon Quick console, choose **Knowledge**.
- 
                    Choose your existing Amazon S3 integration from the list. 
- 
                    Choose the three-dot icon under **Actions**, then choose**Create knowledge base**.
- 
                    Configure your knowledge base settings and choose **Create**.

For detailed information about knowledge base configuration options, see [Common configuration settings](./knowledge-base-integrations.html#common-configuration-settings).

###### Note

When you create a knowledge base in Amazon Quick, by default only you can get
                insights from the knowledge base. For shared content, you can provide access to
                different users and groups by updating the knowledge base permissions. To control
                document-level access within a knowledge base, see
                [Document-level ACLs](./s3-acl.html).