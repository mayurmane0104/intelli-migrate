# Passing IAM roles to Quick - Amazon Quick

**Source:** [https://docs.aws.amazon.com/quick/latest/userguide/security-create-iam-role.html](https://docs.aws.amazon.com/quick/latest/userguide/security-create-iam-role.html)

---

| Applies
                    to:Enterprise Edition | 

When your IAM users sign up for Quick, they can choose to use the Amazon Quick-managed role (this is the default role). Or they can pass an existing IAM role to Amazon Quick.

Use the sections below to pass existing IAM roles to Amazon Quick

## Prerequisites

            For your users to pass IAM roles to Amazon Quick, your administrator needs to complete the following tasks:

- 
                    **Create an IAM role**. For more information about creating IAM roles, see[Creating IAM roles](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_create.html)in the*IAM User Guide*.
- 
                    **Attach a trust policy to your IAM role that allows Amazon Quick to assume the role**. Use the following example to create a trust policy for the role. The following example trust policy allows the Quick principal to assume the IAM role that it's attached to.For more information about creating IAM trust policies and attaching them to roles, see [Modifying a Role (Console)](https://docs.aws.amazon.com/IAM/latest/UserGuide/roles-managingrole-editing-console.html#roles-managingrole_edit-trust-policy.html)in the*IAM User Guide*.`{ "Version": "2012-10-17", "Statement": [ { "Effect": "Allow", "Principal": { "Service": "quicksight.amazonaws.com" }, "Action": "sts:AssumeRole" } ] }`
- 
                    **Assign the following IAM permissions to your administrator (IAM users or roles)**:- 
                            `quicksight:UpdateResourcePermissions`– This grants IAM users who are Amazon Quick administrators the permission to update resource-level permissions in Amazon Quick. For more information about resource types defined by Amazon Quick, see[Actions, resources, and condition keys for Quick](https://docs.aws.amazon.com/IAM/latest/UserGuide/list_amazonquicksight.html)in the*IAM User Guide*.
- 
                            `iam:PassRole`– This grants users permission to pass roles to Amazon Quick. For more information, see[Granting a user permissions to pass a role to an AWS service](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)in the*IAM User Guide*.
- 
                            `iam:ListRoles`– (Optional) This grants users permission to see a list of existing roles in Amazon Quick. If this permission is not provided, they can use an ARN to use existing IAM roles.
 Following is an example IAM permissions policy that allows managing resource-level permissions, listing IAM roles, and passing IAM roles in Quick. `{ "Version": "2012-10-17", "Statement": [ { "Effect": "Allow", "Action": "iam:ListRoles", "Resource": "arn:aws:iam::``account-id`:role:*" }, { "Effect": "Allow", "Action": "iam:PassRole", "Resource": "arn:aws:iam::`account-id`:role/`path`/`role-name`", "Condition": { "StringEquals": { "iam:PassedToService": [ "quicksight.amazonaws.com" ] } } }, { "Effect": "Allow", "Action": "quicksight:UpdateResourcePermissions", "Resource": "*" } ] }For more examples of IAM policies that you can use with Amazon Quick, see [IAM policy examples for Amazon Quick](https://docs.aws.amazon.com/quicksight/latest/user/iam-policy-examples.html).
- 
                            

For more information about assigning permissions policies to users or user groups,
                see [Changing permissions
                    for an IAM user](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_users_change-permissions.html) in the *IAM User Guide*.

## Attaching additional policies

            If you're using another AWS service, such as Amazon Athena or Amazon S3, you can create a permissions policy that grants Amazon Quick permission to perform specific actions. You can then attach the policy to the IAM roles that you later pass to Amazon Quick. The following are examples of how you can set up and attach additional permissions policies to your IAM roles.

For an example managed policy for Amazon Quick in Athena, see [AWSQuicksightAthenaAccess Managed Policy](https://docs.aws.amazon.com/athena/latest/ug/awsquicksightathenaaccess-managed-policy.html) in the
                    *Amazon Athena User Guide*. IAM users can access this role in
                Amazon Quick using the following ARN:
                    `arn:aws:iam::aws:policy/service-role/AWSQuicksightAthenaAccess`.

The following is an example of a permissions policy for Amazon Quick in Amazon S3. For
                more information about using IAM with Amazon S3, see [Identity and access
                    management in Amazon S3](https://docs.aws.amazon.com/AmazonS3/latest/userguide/s3-access-control.html) in the *Amazon S3 User
                Guide*.

For information on how to create cross-account access from Amazon Quick to an Amazon S3
                bucket in another account, see [How do I set
                    up cross-account access from Quick to an Amazon S3 bucket in another
                    account?](https://aws.amazon.com/premiumsupport/knowledge-center/quicksight-cross-account-s3/) in the AWS Knowledge Center.

```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": "s3:ListAllMyBuckets",
            "Resource": "arn:aws:s3:::*"
        },
        {
            "Action": [
                "s3:ListBucket"
            ],
            "Effect": "Allow",
            "Resource": [
                "arn:aws:s3:::aws-athena-query-results-us-west-2-123456789"
            ]
        },
        {
            "Action": [
                "s3:GetObject",
                "s3:GetObjectVersion"
            ],
            "Effect": "Allow",
            "Resource": [
                "arn:aws:s3:::aws-athena-query-results-us-west-2-123456789/*"
            ]
        },
        {
            "Action": [
                "s3:ListBucketMultipartUploads",
                "s3:GetBucketLocation"
            ],
            "Effect": "Allow",
            "Resource": [
                "arn:aws:s3:::aws-athena-query-results-us-west-2-123456789"
            ]
        },
        {
            "Effect": "Allow",
            "Action": [
                "s3:PutObject",
                "s3:AbortMultipartUpload",
                "s3:ListMultipartUploadParts"
            ],
            "Resource": [
                "arn:aws:s3:::aws-athena-query-results-us-west-2-123456789/*"
            ]
        }
    ]
}
```
## Using existing IAM roles in Quick

            If you're a Amazon Quick administrator and have permissions to update Amazon Quick
                resources and pass IAM roles, you can use existing IAM roles in Amazon Quick. To
                learn more about the prerequisites for passing IAM roles in Amazon Quick, see the
                    [Prerequisites](https://docs.aws.amazon.com/quicksight/latest/user/security-create-iam-role-prerequisites.html#byor-prereq) outlined in the previous list.

Use the following procedure to learn how to pass IAM roles in Amazon Quick.

###### To use an existing IAM role in Amazon Quick

- 
                    In Amazon Quick, choose your account name in the navigation bar at top right and choose **Manage QuickSight**.
- 
                    On the **Manage Amazon Quick**page that opens, choose**Security & Permissions**in the menu at left.
- 
                    In the **Security & Permissions**page that opens, under**Amazon Quick access to AWS services**, choose**Manage**.
- 
                    For **IAM role**, choose**Use an existing role**, and then do one of the following:- 
                            Choose the role that you want to use from the list. 
- 
                            Or, if you don't see a list of existing IAM roles, you can enter the IAM ARN for the role in the following format: `arn:aws:iam::`.`account-id`:role/`path`/`role-name`
 
- 
                            
- 
                    Choose **Save**.