# IAM policy examples for Quick - Amazon Quick

**Source:** [https://docs.aws.amazon.com/quick/latest/userguide/iam-policy-examples.html](https://docs.aws.amazon.com/quick/latest/userguide/iam-policy-examples.html)

---

This section provides examples of IAM policies that you can use with Quick.

## IAM identity-based policies for Quick

            This section shows examples of identity-based policies to use with Quick.

### IAM identity-based policies for Amazon Quick IAM console administration

The following example shows the IAM permissions needed for Amazon Quick IAM console administration actions.

```
{
   "Version": "2012-10-17",
   "Statement": [
       {
           "Sid": "Statement1",
           "Effect": "Allow",
           "Action": [
               "quicksight:*",
               "iam:ListAttachedRolePolicies",
               "iam:GetPolicy",
               "iam:CreatePolicyVersion",
               "iam:DeletePolicyVersion",
               "iam:GetPolicyVersion",
               "iam:ListPolicyVersions",
               "iam:DeleteRole",
               "iam:CreateRole",
               "iam:GetRole",
               "iam:ListRoles",
               "iam:CreatePolicy",
               "iam:ListEntitiesForPolicy",
               "iam:listPolicies",
               "s3:ListAllMyBuckets",
               "athena:ListDataCatalogs",
               "athena:GetDataCatalog"
           ],
           "Resource": [
               "*"
           ]
       }
    ]
}
```
## IAM identity-based policies for Quick: dashboards

            The following example shows an IAM policy that allows dashboard sharing and embedding for specific dashboards.

```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Action": "quicksight:RegisterUser",
            "Resource": "*",
            "Effect": "Allow"
        },
        {
            "Action": "quicksight:GetDashboardEmbedUrl",
            "Resource": "arn:aws:quicksight:us-west-2:
```
`111122223333`:dashboard/`1a1ac2b2-3fc3-4b44-5e5d-c6db6778df89`",
            "Effect": "Allow"
        }
    ]
}## IAM identity-based policies for Quick: namespaces

            The following examples show IAM policies that allow a Amazon Quick administrator to create or delete namespaces.

Creating namespaces

```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": [
                "ds:AuthorizeApplication",
                "ds:UnauthorizeApplication",
                "ds:DeleteDirectory",
                "ds:CreateIdentityPoolDirectory",
                "ds:DescribeDirectories",
                "quicksight:CreateNamespace"
            ],
            "Resource": "*"
        }
    ]
}
```
Deleting namespaces

```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": [
                "ds:UnauthorizeApplication",
                "ds:DeleteDirectory",
                "ds:DescribeDirectories",
                "quicksight:DeleteNamespace"
            ],
            "Resource": "*"
        }
    ]
}
```
## IAM identity-based policies for Quick: custom permissions

            The following example shows an IAM policy that allows a Amazon Quick administrator or a developer to manage custom permissions.

```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": [
                "quicksight:*CustomPermissions"
            ],
            "Resource": "*"
        }
    ]
}
```
The following example shows another way to grant the same permissions as shown in the previous example.

```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": [
                "quicksight:CreateCustomPermissions",
                "quicksight:DescribeCustomPermissions",
                "quicksight:ListCustomPermissions",
                "quicksight:UpdateCustomPermissions",
                "quicksight:DeleteCustomPermissions"
 
            ],
            "Resource": "*"
        }
    ]
}
```
## IAM identity-based policies for Quick: customizing email report templates

            The following example shows a policy that allows viewing, updating, and creating email report templates in Amazon Quick, as well as obtaining verification attributes for an Amazon Simple Email Service identity. This policy allows a Amazon Quick administrator to create and update custom email report templates, and to confirm that any custom email address they want to send email reports from is a verified identity in SES.

```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": [
                "quicksight:DescribeAccountCustomization",
                "quicksight:CreateAccountCustomization",
                "quicksight:UpdateAccountCustomization",
                "quicksight:DescribeEmailCustomizationTemplate",
                "quicksight:CreateEmailCustomizationTemplate",
                "quicksight:UpdateEmailCustomizationTemplate",
                "ses:GetIdentityVerificationAttributes"
            ],
            "Resource": "*"
        }
    ]
}
```
## IAM identity-based policies for Quick: create an Enterprise account with Amazon Quick managed users

            The following example shows a policy that allows Amazon Quick admins to create an Enterprise edition Amazon Quick account with Amazon Quick managed users.

```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "Statement1",
            "Effect": "Allow",
            "Action": [
                "quicksight:*",
                "iam:ListAttachedRolePolicies",
                "iam:GetPolicy",
                "iam:CreatePolicyVersion",
                "iam:DeletePolicyVersion",
                "iam:GetPolicyVersion",
                "iam:ListPolicyVersions",
                "iam:DeleteRole",
                "iam:CreateRole",
                "iam:GetRole",
                "iam:ListRoles",
                "iam:CreatePolicy",
                "iam:ListEntitiesForPolicy",
                "iam:listPolicies",
                "s3:ListAllMyBuckets",
                "athena:ListDataCatalogs",
                "athena:GetDataCatalog",
                "ds:AuthorizeApplication",
                "ds:UnauthorizeApplication",
                "ds:CheckAlias",
                "ds:CreateAlias",
                "ds:DescribeDirectories",
                "ds:DescribeTrusts",
                "ds:DeleteDirectory",
                "ds:CreateIdentityPoolDirectory"
            ],
            "Resource": [
                "*"
            ]
        }
    ]
}
```
## IAM identity-based policies for Quick: creating users

            The following example shows a policy that allows creating Amazon Quick users only.
                For `quicksight:CreateReader`, `quicksight:CreateUser`, and
                    `quicksight:CreateAdmin`, you can limit the permissions to
                    ```
"Resource":
                        "arn:aws:quicksight::
```
.
                For all other permissions described in this guide, use `<YOUR_AWS_ACCOUNTID>`:user/${aws:userid}"```
"Resource":
                    "*"
```
. The resource you specify limits the scope of the permissions to
                the specified resource.

```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Action": [
                "quicksight:CreateUser"
            ],
            "Effect": "Allow",
            "Resource": "arn:aws:quicksight::<
```
`YOUR_AWS_ACCOUNTID`>:user/${aws:userid}"
        }
    ]
}## IAM identity-based policies for Quick: creating and managing groups

            The following example shows a policy that allows Amazon Quick administrators and developers to create and manage groups.

```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": [
                "quicksight:ListGroups",
                "quicksight:CreateGroup",
                "quicksight:SearchGroups",
                "quicksight:ListGroupMemberships",
                "quicksight:CreateGroupMembership",
                "quicksight:DeleteGroupMembership",
                "quicksight:DescribeGroupMembership",
                "quicksight:ListUsers"
            ],
            "Resource": "*"
        }
    ]
}
```
## IAM identity-based policies for Quick: All access for Standard edition

            The following example for Amazon Quick Standard edition shows a policy that allows subscribing and creating authors and readers. This example explicitly denies permission to unsubscribe from Amazon Quick.

```
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": [
        "ds:AuthorizeApplication",
        "ds:UnauthorizeApplication",
        "ds:CheckAlias",
        "ds:CreateAlias",
        "ds:DescribeDirectories",
        "ds:DescribeTrusts",
        "ds:DeleteDirectory",
        "ds:CreateIdentityPoolDirectory",
        "iam:ListAccountAliases",
        "quicksight:CreateUser",
        "quicksight:DescribeAccountSubscription",
        "quicksight:Subscribe"
      ],
      "Resource": "*"
    },
    {
      "Effect": "Deny",
      "Action": [
        "quicksight:Unsubscribe",
        "quicksight:DeleteAccountSubscription"
      ],
      "Resource": "*"
    }
  ]
}
```
## IAM identity-based policies for Quick: All access for Enterprise edition with IAM Identity Center (Pro roles)

            The following example for Amazon Quick Enterprise edition shows a policy that allows a Amazon Quick user to subscribe to Amazon Quick, create users, and manage Active Directory in a Amazon Quick account that is integrated with IAM Identity Center.

This policy also allows users to subscribe to Amazon Quick Pro roles that grant
                access to Amazon Q in Quick Generative BI capabilities. For more information about Pro roles in
                Amazon Quick, see [Get started with Generative BI](https://docs.aws.amazon.com/quicksight/latest/user/generative-bi-get-started.html).

This example explicitly denies permission to unsubscribe from Amazon Quick.

```
{
    "Statement": [
        {
            "Sid": "Statement1",
            "Effect": "Allow",
            "Action": [
                "quicksight:*",
                "iam:ListAttachedRolePolicies",
                "iam:GetPolicy",
                "iam:CreatePolicyVersion",
                "iam:DeletePolicyVersion",
                "iam:GetPolicyVersion",
                "iam:ListPolicyVersions",
                "iam:DeleteRole",
                "iam:CreateRole",
                "iam:GetRole",
                "iam:ListRoles",
                "iam:CreatePolicy",
                "iam:ListEntitiesForPolicy",
                "iam:listPolicies",
                "iam:CreateServiceLinkedRole",
                "s3:ListAllMyBuckets",
                "athena:ListDataCatalogs",
                "athena:GetDataCatalog",
                "sso:DescribeApplication",
                "sso:DescribeInstance",
                "sso:CreateApplication",
                "sso:PutApplicationAuthenticationMethod",
                "sso:PutApplicationGrant",
                "sso:DeleteApplication",
                "sso:SearchGroups",
                "sso:GetProfile",
                "sso:CreateApplicationAssignment",
                "sso:DeleteApplicationAssignment",
                "sso:ListInstances",
                "sso:DescribeRegisteredRegions",
                "organizations:DescribeOrganization",
                "user-subscriptions:CreateClaim",
                "user-subscriptions:UpdateClaim",
                "sso-directory:DescribeUser",
                "sso:ListApplicationAssignments",
                "sso-directory:DescribeGroup",
                "organizations:ListAWSServiceAccessForOrganization",
                "identitystore:DescribeUser",
                "identitystore:DescribeGroup"
            ],
            "Resource": [
                "*"
            ]
        }
    ]
}
```
## IAM identity-based policies for Quick: All access for Enterprise edition with IAM Identity Center

            The following example for Amazon Quick Enterprise edition shows a policy that allows subscribing, creating users, and managing Active Directory in a Amazon Quick account that is integrated with IAM Identity Center.

This policy does not grant permissions to create Pro roles in Amazon Quick. To
                create a policy that grants permission to subscribe to Pro roles in Amazon Quick,
                see [IAM identity-based policies for Amazon Quick: All access
                    for Enterprise edition with IAM Identity Center (Pro roles)](https://docs.aws.amazon.com/quicksight/latest/user/iam-policy-examples.html#security_iam_id-based-policy-examples-all-access-enterprise-edition-sso-pro).

This example explicitly denies permission to unsubscribe from Amazon Quick.

```
{
    "Statement": [
        {
            "Sid": "Statement1",
            "Effect": "Allow",
            "Action": [
                "quicksight:*",
                "iam:ListAttachedRolePolicies",
                "iam:GetPolicy",
                "iam:CreatePolicyVersion",
                "iam:DeletePolicyVersion",
                "iam:GetPolicyVersion",
                "iam:ListPolicyVersions",
                "iam:DeleteRole",
                "iam:CreateRole",
                "iam:GetRole",
                "iam:ListRoles",
                "iam:CreatePolicy",
                "iam:ListEntitiesForPolicy",
                "iam:listPolicies",
                "s3:ListAllMyBuckets",
                "athena:ListDataCatalogs",
                "athena:GetDataCatalog",
                "sso:DescribeApplication",
                "sso:DescribeInstance",
                "sso:CreateApplication",
                "sso:PutApplicationAuthenticationMethod",
                "sso:PutApplicationGrant",
                "sso:DeleteApplication",
                "sso:SearchGroups",
                "sso:GetProfile",
                "sso:CreateApplicationAssignment",
                "sso:DeleteApplicationAssignment",
                "sso:ListInstances",
                "sso:DescribeRegisteredRegions",
                "organizations:DescribeOrganization" 
            ],
            "Resource": [
                "*"
            ]
        }
    ]
}
```
## IAM identity-based policies for Quick: all access for Enterprise edition with Active Directory

            The following example for Amazon Quick Enterprise edition shows a policy that allows subscribing, creating users, and managing Active Directory in a Amazon Quick account that uses Active Directory for identity management. This example explicitly denies permission to unsubscribe from Amazon Quick.

```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": [
                "ds:AuthorizeApplication",
                "ds:UnauthorizeApplication",
                "ds:CheckAlias",
                "ds:CreateAlias",
                "ds:DescribeDirectories",
                "ds:DescribeTrusts",
                "ds:DeleteDirectory",
                "ds:CreateIdentityPoolDirectory",
                "iam:ListAccountAliases",
                "quicksight:CreateAdmin",
                "quicksight:Subscribe",
                "quicksight:GetGroupMapping",
                "quicksight:SearchDirectoryGroups",
                "quicksight:SetGroupMapping"
            ],
            "Resource": "*"
        },
        {
            "Effect": "Deny",
            "Action": [
                "quicksight:Unsubscribe",
                "quicksight:DeleteAccountSubscription"
            ],
            "Resource": "*"
        }
    ]
}
```
## IAM identity-based policies for Quick: active directory groups

            The following example shows an IAM policy that allows Active Directory group management for an Amazon Quick Enterprise edition account.

```
{
    "Statement": [
        {
            "Action": [
                "ds:DescribeTrusts",
                "quicksight:GetGroupMapping",
                "quicksight:SearchDirectoryGroups",
                "quicksight:SetGroupMapping"
            ],
            "Effect": "Allow",
            "Resource": "*"
        }
    ],
    "Version": "2012-10-17"
}
```
## IAM identity-based policies for Quick: using the admin asset management console

            The following example shows an IAM policy that allows access to the admin asset management console.

```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": [          
                "quicksight:SearchGroups",
                "quicksight:SearchUsers",              
                "quicksight:ListNamespaces",            
                "quicksight:DescribeAnalysisPermissions",
                "quicksight:DescribeDashboardPermissions",
                "quicksight:DescribeDataSetPermissions",
                "quicksight:DescribeDataSourcePermissions",
                "quicksight:DescribeFolderPermissions",
                "quicksight:ListAnalyses",
                "quicksight:ListDashboards",
                "quicksight:ListDataSets",
                "quicksight:ListDataSources",
                "quicksight:ListFolders",
                "quicksight:SearchAnalyses",
                "quicksight:SearchDashboards",
                "quicksight:SearchFolders",
                "quicksight:SearchDatasets",
                "quicksight:SearchDatasources",               
                "quicksight:UpdateAnalysisPermissions",
                "quicksight:UpdateDashboardPermissions",
                "quicksight:UpdateDataSetPermissions",
                "quicksight:UpdateDataSourcePermissions",
                "quicksight:UpdateFolderPermissions"
            ],
            "Resource": "*"
        }
    ]
}
```
## IAM identity-based policies for Quick: using the admin key management console

            The following example shows an IAM policy that allows access to the admin key management console.

```
{
   "Version":"2012-10-17",
   "Statement":[
      {
         "Effect":"Allow",
         "Action":[
            "quicksight:DescribeKeyRegistration",
            "quicksight:UpdateKeyRegistration",
            "quicksight:ListKMSKeysForUser",
            "kms:CreateGrant",
            "kms:ListGrants",
            "kms:ListAliases"
         ],
         "Resource":"*"
      }
   ]
}
```
The `"quicksight:ListKMSKeysForUser"` and
                    `"kms:ListAliases"` permissions are required to access customer
                managed keys from the Amazon Quick console.
                    `"quicksight:ListKMSKeysForUser"` and `"kms:ListAliases"`
                are not required to use the Amazon Quick key management APIs.

To specify which keys you want a user to be able to access, add the ARNs of the
                keys that you want the user to access to the `UpdateKeyRegistration`
                condition with the `quicksight:KmsKeyArns` condition key. Users can only
                access the keys specified in `UpdateKeyRegistration`. For more
                information about supported condition keys for Amazon Quick, see [Condition keys for Amazon Quick](https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazonquicksight.html#amazonquicksight-policy-keys).

The example below grants `Describe` permissions for all CMKs that are
                registered to a Amazon Quick account and `Update` permissons to specific
                CMKs that are registered to the Amazon Quick account.

```
{
   "Version":"2012-10-17",
   "Statement":[
      {
         "Effect":"Allow",
         "Action":[
            "quicksight:DescribeKeyRegistration"
         ],
         "Resource":"
```
`arn:aws:quicksight:us-west-2:123456789012:*`"
      },
      {
         "Effect":"Allow",
         "Action":[
            "quicksight:UpdateKeyRegistration"
         ],
         "Resource":"`arn:aws:quicksight:us-west-2:123456789012:*`",
         "Condition":{
            "ForAllValues:StringEquals":{
               "quicksight:KmsKeyArns":[
                  "`arn:aws:kms:us-west-2:123456789012:key/key-id-of-key1`",
                  "`arn:aws:kms:us-west-2:123456789012:key/key-id-of-key2`",
                  "..."
               ]
            }
         }
      },
      {
         "Effect":"Allow",
         "Action":[
            "kms:CreateGrant",
            "kms:ListGrants"
         ],
         "Resource":"`arn:aws:kms:us-west-2:123456789012:key/*`"
      }
   ]
}## AWS resources Quick: scoping policies in Enterprise edition

            The following example for Amazon Quick Enterprise edition shows a policy that allows setting default access to AWS resources and scoping policies for permissions to AWS resources.

```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Action": [
                "quicksight:*IAMPolicyAssignment*",
                "quicksight:AccountConfigurations"
            ],
            "Effect": "Allow",
            "Resource": "*"
        }
    ]
}
```