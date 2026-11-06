# Data encryption in Amazon Quick - Amazon Quick

**Source:** [https://docs.aws.amazon.com/quick/latest/userguide/data-encryption.html](https://docs.aws.amazon.com/quick/latest/userguide/data-encryption.html)

---

Amazon Quick uses the following data encryption features:

- 
        Encryption at rest 
- 
        Encryption in transit 
- 
        Key management 

You can find more details about data encryption at rest and data encryption in transit in
      the following topics. For more information about key management in Amazon Quick see [Encrypting
        Amazon Quick SPICE datasets with AWS KMS customer-managed keys](https://docs.aws.amazon.com/quicksuite/latest/userguide/customer-managed-keys.html).

## Encryption at rest

      Amazon Quick securely stores your Amazon Quick metadata. This includes the following:

- 
          Amazon Quick user data, including Amazon Quick user names, email addresses, and passwords. Amazon Quick administrators can view user names and emails, but each user's password is completely private to each user. 
- 
          Minimal data necessary to coordinate user identification with your Microsoft Active Directory or identity federation implementation (Federated Single Sign-On (IAM Identity Center) through Security Assertion Markup Language 2.0 (SAML 2.0)). 
- 
          Data source connection data. 
- 
          Amazon Quick data source credentials (username and password) or OAuth tokens to establish a data source connection are encrypted with the customers default CMK when customer registers a CMK with Amazon Quick. If the customer does not register a CMK with Amazon Quick, we will continue to encrypt the information using a Amazon Quick owned AWS KMS key. 
- 
          Names of your uploaded files, data source names, and data set names. 
- 
          Statistics that Amazon Quick uses to populate machine learning (ML) insights. 
- 
          Data indexed to support Amazon Q in Quick. This includes the following: - 
              Topics 
- 
              Metadata related to your dashboards 
- 
              Your first index capacity purchase 
- 
              Your first chat 
- 
              Your first space creation 
- 
              Your first knowledge base creation 
 
- 
              

###### Note

Configure a CMK prior to creating the above. Otherwise, Q data will be encrypted by an AWS–owned key and cannot be changed later.

Amazon Quick securely stores your Amazon Quick data. This includes the following:

- 
          Data-at-rest in SPICE is encrypted using hardware block-level encryption with AWS-managed keys. 
- 
          Data-at-rest other than SPICE is encrypted using Amazon-managed KMS keys. This includes the following: - 
              Email reports 
- 
              Sample value for filters 
 
- 
              

When you delete a user, all of that user's metadata is permanently deleted. If you don't transfer that user's Amazon Quick objects to another user, all of the deleted user's Amazon Quick objects (data sources, datasets, analyses, and so on) are also deleted. When you unsubscribe from Amazon Quick, all metadata and any data you have in SPICE is completely and permanently deleted.

## Encryption in transit

      Amazon Quick supports encryption for all data transfers. This includes transfers from the data source to SPICE, or from SPICE to the user interface. However, encryption isn't mandatory. For some databases, you can choose whether transfers from the data source are encrypted or not. Amazon Quick secures all encrypted transfers by using Secure Sockets Layer (SSL).