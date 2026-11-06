# Allowlisting Amazon Quick domains - Amazon Quick

**Source:** [https://docs.aws.amazon.com/quick/latest/userguide/allowlist-domains.html](https://docs.aws.amazon.com/quick/latest/userguide/allowlist-domains.html)

---

If your end users are signing in to Amazon Quick using AWS root (not recommended), AWS Identity and Access Management (IAM), corporate Active Directory, or native Quick credentials, make sure to allow-list the following domains within your organization's network.

| User type | Domain or domains to allow-list | 
|---|---|
| Users who sign in directly through Amazon Quick and Active Directory users | 
 | 
| AWS root user | 
 | 
| IAM users | 
 | 

###### Important

We strongly recommend that you don't use the AWS root user for your everyday tasks,
            even the administrative ones. Instead, adhere to the best practice of using the root
            user only to create your first IAM user. Then securely lock away the root user
            credentials and use them to perform only a few account and service management tasks. For
            more information, see [AWS account root user](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_root-user.html) in the
                *IAM User Guide*.