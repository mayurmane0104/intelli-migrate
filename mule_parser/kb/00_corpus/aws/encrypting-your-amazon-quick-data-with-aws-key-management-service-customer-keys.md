# Encrypting your Amazon Quick data with AWS Key Management Service customer-managed keys - Amazon Quick

**Source:** [https://docs.aws.amazon.com/quick/latest/userguide/customer-managed-keys.html](https://docs.aws.amazon.com/quick/latest/userguide/customer-managed-keys.html)

---

Amazon Quick enables you to encrypt your Amazon Quick data with the keys you have stored in AWS Key Management Service. This provides you with the tools to audit access to data and satisfy regulatory security requirements. If you need to do so, you have the option to immediately lock down access to your data by revoking access to AWS KMS keys. All data access to encrypted resources in Amazon Quick is logged in AWS CloudTrail. Administrators or auditors can trace data access in CloudTrail to identify when and where data was accessed.

To create customer-managed keys (CMKs), you use AWS Key Management Service (AWS KMS) in the same AWS account and AWS Region as the Amazon Quick resource. A Amazon Quick administrator can then use a CMK to encrypt your Amazon Quick data and control access.

You can create and manage CMKs in the Amazon Quick console or with the Amazon Quick APIs. For
        more information about creating and managing CMKs with the Amazon Quick APIs, see [Key
            management operations](https://docs.aws.amazon.com/quicksight/latest/developerguide/cmk-operations.html).

The following rules apply to using CMKs with Amazon Quick resources:

- 
            Amazon Quick doesn't support asymmetric AWS KMS keys. 
- 
            You can have multiple CMKs and one default CMK per AWS account per AWS Region. 
- 
            By default, Amazon Quick resources are encrypted with Amazon Quick–native encryption strategies. 
- 
            Data currently encrypted by a CMK key will stay encrypted by the key. 

###### Note

If you use AWS Key Management Service with Amazon Quick, you are billed for access and maintenance as
            described in the [AWS Key Management Service Pricing
                page](https://aws.amazon.com/kms/pricing). In your billing statement, the costs are itemized under AWS KMS and not
            under Amazon Quick.

###### Note

Amazon Q data is encrypted by an AWS managed key, not the default AWS KMS key.

The key that is currently the default CMK is automatically used to encrypt the following:

- 
            New SPICE datasets. Existing datasets need to be fully refreshed to be encrypted by the new default key. 
- 
            New report artifacts generated through the dashboard snapshot API, scheduled reports and exports, or dashboards. 

All non-customer managed keys associated with Amazon Quick are managed by AWS.

Database server certificates that are not managed by AWS are the responsibility of the
        customer and should be signed by a trusted CA. For more information, see [Network and
            database configuration requirements](https://docs.aws.amazon.com/quicksuite/latest/userguide/configure-access.html).

Use the following topics to learn more about using CMKs with Amazon Quick. To learn more
        about data encryption in Amazon Quick see [Data
            protection in Amazon Quick](https://docs.aws.amazon.com/quicksuite/latest/userguide/sec-data-protection.html).

###### Topics

## Add a CMK to your account

        Before you begin, make sure that you have an IAM role that grants the admin user
            access to the Amazon Quick admin key management console. For more information on the
            required permissions, see [IAM identity-based policies for Amazon Quick: using the admin
                key management console](https://docs.aws.amazon.com/quicksight/latest/user/iam-policy-examples.html#security_iam_id-based-policy-examples-admin-key-management-console).

You can add keys that already exist in AWS KMS to your Amazon Quick account, so that you can encrypt your Amazon Quick data.

To learn more about how you can create a key to use in Amazon Quick, see the [AWS Key
                Management Service Developer Guide](https://docs.aws.amazon.com//kms/latest/developerguide/overview.html).

###### To add a new CMK to your Amazon Quick account.

- 
                On the Amazon Quick start page, choose **Manage Amazon Quick**, and then choose**KMS keys**.
- 
                On the **KMS keys**page, choose**Manage**. The**KMS keys**dashboard opens.
- 
                On the **KMS Keys**dashboard, choose**Select key**.
- 
                On the **Select key**pop-up box, choose**Key**to open the list. Then, select the key that you want to add.If your key isn't in the list, you can manually enter the key's ARN. 
- 
                (Optional) Select the **Use as default encryption key for all new data in the current region of this Amazon Quick account**to set the selected key as your default key. A badge appears next to the default key to indicate its status.When you choose a default key, all new data that is created in the region that hosts your Amazon Quick account is encrypted with the default key. 
- 
                (Optional) Add more keys by repeating the previous steps in this procedure. While you can add as many keys as you want, you can only have one default key at one time. 

## Verify the key used by Amazon Quick

        When a key is used, an audit log is created in AWS CloudTrail. You can use the log to track the key's usage. If you need to know which key the Amazon Quick data is encrypted by, you can find this information in CloudTrail.

To learn more about which data can be managed with the key, see [Encrypting your Amazon Quick data with AWS Key Management Service customer-managed keys](./customer-managed-keys.html).

###### Verify the CMK that's currently used by a SPICE dataset

- 
                Navigate to your CloudTrail log. For more information, see [Logging Amazon Quick information with CloudTrail](https://docs.aws.amazon.com/quicksight/latest/user/logging-using-cloudtrail.html).
- 
                Locate the most recent grant events for the SPICE dataset, using the following search arguments: - 
                        The event name ( `eventName`) contains`Grant`.
- 
                        The request parameters `requestParameters`contain the Amazon Quick ARN for the dataset.
 `{ "eventVersion": "1.08", "userIdentity": { "type": "AWSService", "invokedBy": "quicksight.amazonaws.com" }, "eventTime": "2022-10-26T00:11:08Z", "eventSource": "kms.amazonaws.com", "eventName": "``CreateGrant`", "awsRegion": "us-west-2", "sourceIPAddress": "quicksight.amazonaws.com", "userAgent": "quicksight.amazonaws.com", "requestParameters": { "constraints": { "encryptionContextSubset": { "aws:quicksight:arn": "arn:aws:quicksight:us-west-2:111122223333:`dataset/12345678-1234-1234-1234-123456789012`" } }, "retiringPrincipal": "quicksight.amazonaws.com", "keyId": "arn:aws:kms:us-west-2:111122223333:`key/87654321-4321-4321-4321-210987654321`", "granteePrincipal": "quicksight.amazonaws.com", "operations": [ "Encrypt", "Decrypt", "DescribeKey", "GenerateDataKey" ] }, .... }
- 
                        
- 
                Depending on the event type, one of the following applies: `CreateGrant`– You can find the most recently used CMK in the key ID (`keyID`) for the last`CreateGrant`event for the SPICE dataset.`RetireGrant`– If latest CloudTrail event of the SPICE datasets is`RetireGrant`, there is no key ID and the resource is no longer CMK encrypted.

###### Verify the CMK that's currently used when generating report artifacts

- 
                Navigate to your CloudTrail log. For more information, see [Logging Amazon Quick Sight information with AWS CloudTrail](./incident-response-logging-and-monitoring-qs.html#logging-using-cloudtrail).
- 
                Locate the most recent `GenerateDataKey`events for the report execution, using the following search arguments:- 
                        The event name ( `eventName`) contains`GenerateDataKey`or`Decrypt`.
- 
                        The request parameters ( `requestParameters`) contain the Amazon Quick ARN for the analysis or dashboard the report was generated for.
 `{ "eventVersion": "1.11", "userIdentity": { "type": "AWSService", "invokedBy": "quicksight.amazonaws.com" }, "eventTime": "2025-07-23T23:33:46Z", "eventSource": "kms.amazonaws.com", "eventName": "``GenerateDataKey`", "awsRegion": "us-west-2", "sourceIPAddress": "quicksight.amazonaws.com", "userAgent": "quicksight.amazonaws.com", "requestParameters": { "keyId": "arn:aws:kms:us-west-2:111122223333`:key/87654321-4321-4321-4321-210987654321`", "keySpec": "AES_256", "encryptionContext": { "aws:quicksight:arn": "arn:aws:quicksight:us-west-2:111122223333:`dashboard/1ca456fe-eb34-4250-805c-b1b9350bd164`", "aws:s3:arn": "arn:aws:s3:::sn-imagegen.prod.us-west-2" } }, ... }
- 
                        
- 
                `aws:s3:arn`is the Amazon Quick owned S3 bucket where your report artifacts are stored.
- 
                If you no longer see `GenerateDataKey`, then new report executions are no longer CMK encrypted. Exisiting report artifacts will remain encrypted.

## Changing the default CMK

        You can change the default key to another key that already exists in the
                **KMS keys** dashboard. When you change the default key, all new
            Amazon Quick data is encrypted on the new key. The new default key changes how new
            Amazon Quick data is encrypted. However, existing Amazon Quick data will continue to use the
            previous default key.

To learn more about which data can be managed with the key, see [Encrypting your Amazon Quick data with AWS Key Management Service customer-managed keys](./customer-managed-keys.html).

###### To change the default key to an existing key

- 
                On the Amazon Quick start page, choose **Manage Amazon Quick**, and then choose**KMS keys**.
- 
                Choose **MANAGE**to open the**KMS keys**dashboard.
- 
                Navigate to the key that you want to set as your new default. Choose **Actions**(three dots) on the row of the key that you want to open the key's menu.
- 
                Choose **Set as default**, and then choose**Set**.

###### Note

The Q data key cannot be changed. Q data will remain encrypted with the current
                default key. In the event that this key is compromised, you can [revoke access to it](#customer-managed-key-revoke-access).

The selected key is now your default key.

## Removing CMK encryption on your Amazon Quick account

        You can remove the default key to disable data encryption in your Amazon Quick account. Removing the key prevents new resources from encrypting on a CMK.

###### To remove CMK encryption for new Amazon Quick data

- 
                On the Amazon Quick start page, choose **Manage Amazon Quick**, and then choose**KMS keys**.
- 
                On the **KMS keys**page, choose**Manage**to open the**KMS keys**dashboard.
- 
                Choose **Actions**(three dots) on the row of the default key, and then choose**Delete**.
- 
                In the pop-up box that appears, choose **Remove**.

After you delete the default key from your account, Amazon Quick stops
            encrypting new Amazon Quick data. Any existing encrypted data will remain encrypted. Q data
            remains encrypted because the Q data key cannot be changed. In the event that the
            deleted key is compromised, you can [revoke access to it](#customer-managed-key-revoke-access).

## Auditing CMK usage in CloudTrail

        You can audit your account's CMK usage in AWS CloudTrail. To audit your key usage, log in to
            your AWS account, open CloudTrail, and choose **Event history**.

## Revoking access to a CMK

        You can revoke access to your CMKs. When you revoke access to a key that is used to encrypt your Amazon Quick data, access to it is denied until you undo the revoke. The following methods are examples of how you can revoke access:

- 
                Turn off the key in AWS KMS. 
- 
                Add a `Deny`policy to your Amazon Quick AWS KMS policy in IAM.

To learn more about which data can be managed with the key, see [Encrypting your Amazon Quick data with AWS Key Management Service customer-managed keys](./customer-managed-keys.html).

Use the following procedure to revoke access to your CMKs in AWS KMS.

###### To turn off a CMK in AWS Key Management Service

- 
                Log in to your AWS account, open AWS KMS, and choose **Customer managed keys**.
- 
                Select the key that you want to turn off. 
- 
                Open the **Key actions**menu and choose**Disable**.

To prevent further use of the CMK, you could add a `Deny` policy in
            AWS Identity and Access Management (IAM). Use `"Service": "quicksight.amazonaws.com"` as the
            principal and the ARN of the key as the resource. Deny the following actions:
                ```
"kms:Encrypt", "kms:Decrypt", "kms:ReEncrypt*", "kms:GenerateDataKey*",
                "kms:DescribeKey"
```
.

###### Important

After you revoke access by using any method, it can take up to 15 minutes for the data to become inaccessible.

## Recovering encrypted Amazon Quick data

        ###### To recover Amazon Quick data while its access is revoked

- 
                Restore access to the CMK. Usually, this is enough to recover the Amazon Quick data. 
- 
                Test the Amazon Quick data to check if you can see it. 
- 
                (Optional) If the data is not fully recovered, even after you restored its access to the CMK, perform a full refresh on the data. 

To learn more about which data can be managed with the key, see [Encrypting your Amazon Quick data with AWS Key Management Service customer-managed keys](./customer-managed-keys.html).