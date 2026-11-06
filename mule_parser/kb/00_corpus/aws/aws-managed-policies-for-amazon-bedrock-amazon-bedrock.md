# AWS managed policies for Amazon Bedrock - Amazon Bedrock

**Source:** [https://docs.aws.amazon.com/bedrock/latest/userguide/security-iam-awsmanpol.html](https://docs.aws.amazon.com/bedrock/latest/userguide/security-iam-awsmanpol.html)

---

[Gemma 4 E2B](https://docs.aws.amazon.com/bedrock/latest/userguide/model-card-google-gemma-4-e2b.html)

*12 June 2026*

We use essential cookies and similar tools that are necessary to provide our site and services. We use performance cookies to collect anonymous statistics, so we can understand how customers use our site and make improvements. Essential cookies cannot be deactivated, but you can choose “Customize” or “Decline” to decline performance cookies. 

 If you agree, AWS and approved third parties will also use cookies to provide useful site features, remember your preferences, and display relevant content, including relevant advertising. To accept or decline all non-essential cookies, choose “Accept” or “Decline.” To make more detailed choices, choose “Customize.”

Essential cookies are necessary to provide our site and services and cannot be deactivated. They are usually set in response to your actions on the site, such as setting your privacy preferences, signing in, or filling in forms.

Performance cookies provide anonymous statistics about how customers navigate our site so we can improve site experience and performance. Approved third parties may perform analytics on our behalf, but they cannot use the data for their own purposes.

Functional cookies help us provide useful site features, remember your preferences, and display relevant content. Approved third parties may set these cookies to provide certain site features. If you do not allow these cookies, then some or all of these services may not function properly.

Advertising cookies may be set through our site by us or our advertising partners and help us deliver relevant marketing content. If you do not allow these cookies, you will experience less relevant advertising.

Blocking some types of cookies may impact your experience of our sites. You may review and change your choices at any time by selecting Cookie preferences in the footer of this site. We and selected third-parties use cookies or similar technologies as specified in the [AWS Cookie Notice](https://aws.amazon.com/legal/cookies/).

We will only store essential cookies at this time, because we were unable to save your cookie preferences.

If you want to change your cookie preferences, try again later using the link in the AWS console footer, or contact support if the problem persists.

To add permissions to users, groups, and roles, it's easier to use AWS managed policies
      than to write policies yourself. It takes time and expertise to [create IAM customer
         managed policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_create-console.html) that provide your team with only the permissions they need. To get
      started quickly, you can use our AWS managed policies. These policies cover common use cases
      and are available in your AWS account.

For a list of AWS managed policies, see [AWS managed policies](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/policy-list.html) in the AWS managed policy referenc. For more information about AWS managed policies,
      see [AWS managed policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-vs-inline.html#aws-managed-policies) in the *IAM User Guide*.

AWS services maintain and update AWS managed policies. You can't change the permissions in AWS managed policies. Services occasionally add additional permissions to an AWS managed policy to support new features. This type of update affects all identities (users, groups, and roles) where the policy is attached. Services are most likely to update an AWS managed policy when a new feature is launched or when new operations become available. Services do not remove permissions from an AWS managed policy, so policy updates won't break your existing permissions.

Additionally, AWS supports managed policies for job functions that span multiple
      services. For example, the **ReadOnlyAccess** AWS managed
      policy provides read-only access to all AWS services and resources. When a service launches
      a new feature, AWS adds read-only permissions for new operations and resources. For a list
      and descriptions of job function policies, see [AWS managed policies for
         job functions](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_job-functions.html) in the *IAM User Guide*.

You can attach the [AmazonBedrockFullAccess](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AmazonBedrockFullAccess.html) policy 
      to your IAM identities to grant administrative permissions that allow 
         the user permission to create, read, update, and delete 
         Amazon Bedrock resources.

**Permissions details**

This policy includes the following permissions:

               `ec2` (Amazon Elastic Compute Cloud) – Allows 
               permissions to describe VPCs, subnets, and security groups.
            

               `iam` (AWS Identity and Access Management) –
               Allows principals to pass roles, but only allows IAM roles
               with "Amazon Bedrock" in them to be passed to the Amazon Bedrock service. 
               The permissions are restricted to 
               `bedrock.amazonaws.com` for Amazon Bedrock operations.
            

               `kms` (AWS Key Management Service) – 
               Allows principals to describe AWS KMS keys and aliases.
            

               `bedrock` (Amazon Bedrock) – Allows principals 
               read and write access to all actions in the Amazon Bedrock 
               control plane and runtime service.
            

                    `sagemaker` (Amazon SageMaker AI) – Allows principals to access the Amazon SageMaker AI
                    resources in the customer's account, which serves as the foundation for the
                    Amazon Bedrock Marketplace feature. 

```
{
     "Version":"2012-10-17",
     "Statement": [
         {
             "Sid": "BedrockAll",
             "Effect": "Allow",
             "Action": [
                 "bedrock:*"
             ],
             "Resource": "*"
         },
         {
             "Sid": "DescribeKey",
             "Effect": "Allow",
             "Action": [
                 "kms:DescribeKey"
             ],
             "Resource": "arn:*:kms:*:::*"
         },
         {
             "Sid": "APIsWithAllResourceAccess",
             "Effect": "Allow",
             "Action": [
                 "iam:ListRoles",
                 "ec2:DescribeVpcs",
                 "ec2:DescribeSubnets",
                 "ec2:DescribeSecurityGroups"
             ],
             "Resource": "*"
         },
         {
             "Sid": "MarketplaceModelEndpointMutatingAPIs",
             "Effect": "Allow",
             "Action": [
                 "sagemaker:CreateEndpoint",
                 "sagemaker:CreateEndpointConfig",
                 "sagemaker:CreateModel",
                 "sagemaker:DeleteEndpoint",
                 "sagemaker:UpdateEndpoint"
             ],
             "Resource": [
                 "arn:aws:sagemaker:*:*:endpoint/*",
                 "arn:aws:sagemaker:*:*:endpoint-config/*",
                 "arn:aws:sagemaker:*:*:model/*"
             ],
             "Condition": {
                 "StringEquals": {
                     "aws:CalledViaLast": "bedrock.amazonaws.com",
                     "aws:ResourceTag/sagemaker-sdk:bedrock": "compatible"
                 }
             }
         },
         {
             "Sid": "MarketplaceModelEndpointAddTagsOperations",
             "Effect": "Allow",
             "Action": [
                 "sagemaker:AddTags"
             ],
             "Resource": [
                 "arn:aws:sagemaker:*:*:endpoint/*",
                 "arn:aws:sagemaker:*:*:endpoint-config/*",
                 "arn:aws:sagemaker:*:*:model/*"
             ],
             "Condition": {
                 "ForAllValues:StringEquals": {
                     "aws:TagKeys": [
                         "sagemaker-sdk:bedrock",
                         "bedrock:marketplace-registration-status",
                         "sagemaker-studio:hub-content-arn"
                     ]
                 },
                 "StringLike": {
                     "aws:RequestTag/sagemaker-sdk:bedrock": "compatible",
                     "aws:RequestTag/bedrock:marketplace-registration-status": "registered",
                     "aws:RequestTag/sagemaker-studio:hub-content-arn": "arn:aws:sagemaker:*:aws:hub-content/SageMakerPublicHub/Model/*"
                 }
             }
         },
         {
             "Sid": "MarketplaceModelEndpointDeleteTagsOperations",
             "Effect": "Allow",
             "Action": [
                 "sagemaker:DeleteTags"
             ],
             "Resource": [
                 "arn:aws:sagemaker:*:*:endpoint/*",
                 "arn:aws:sagemaker:*:*:endpoint-config/*",
                 "arn:aws:sagemaker:*:*:model/*"
             ],
             "Condition": {
                 "ForAllValues:StringEquals": {
                     "aws:TagKeys": [
                         "sagemaker-sdk:bedrock",
                         "bedrock:marketplace-registration-status",
                         "sagemaker-studio:hub-content-arn"
                     ]
                 },
                 "StringLike": {
                     "aws:ResourceTag/sagemaker-sdk:bedrock": "compatible",
                     "aws:ResourceTag/bedrock:marketplace-registration-status": "registered",
                     "aws:ResourceTag/sagemaker-studio:hub-content-arn": "arn:aws:sagemaker:*:aws:hub-content/SageMakerPublicHub/Model/*"
                 }
             }
         },
         {
             "Sid": "MarketplaceModelEndpointNonMutatingAPIs",
             "Effect": "Allow",
             "Action": [
                 "sagemaker:DescribeEndpoint",
                 "sagemaker:DescribeEndpointConfig",
                 "sagemaker:DescribeModel",
                 "sagemaker:DescribeInferenceComponent",
                 "sagemaker:ListEndpoints",
                 "sagemaker:ListTags"
             ],
             "Resource": [
                 "arn:aws:sagemaker:*:*:endpoint/*",
                 "arn:aws:sagemaker:*:*:endpoint-config/*",
                 "arn:aws:sagemaker:*:*:model/*"
             ],
             "Condition": {
                 "StringEquals": {
                     "aws:CalledViaLast": "bedrock.amazonaws.com"
                 }
             }
         },
         {
             "Sid": "MarketplaceModelEndpointInvokingOperations",
             "Effect": "Allow",
             "Action": [
                 "sagemaker:InvokeEndpoint",
                 "sagemaker:InvokeEndpointWithResponseStream"
             ],
             "Resource": [
                 "arn:aws:sagemaker:*:*:endpoint/*"
             ],
             "Condition": {
                 "StringEquals": {
                     "aws:CalledViaLast": "bedrock.amazonaws.com",
                     "aws:ResourceTag/sagemaker-sdk:bedrock": "compatible"
                 }
             }
         },
         {
             "Sid": "DiscoveringMarketplaceModel",
             "Effect": "Allow",
             "Action": [
                 "sagemaker:DescribeHubContent"
             ],
             "Resource": [
                 "arn:aws:sagemaker:*:aws:hub-content/SageMakerPublicHub/Model/*",
                 "arn:aws:sagemaker:*:aws:hub/SageMakerPublicHub"
             ]
         },
         {
             "Sid": "AllowMarketplaceModelsListing",
             "Effect": "Allow",
             "Action": [
                 "sagemaker:ListHubContents"
             ],
             "Resource": "arn:aws:sagemaker:*:aws:hub/SageMakerPublicHub"
         },
         {
             "Sid": "PassRoleToSageMaker",
             "Effect": "Allow",
             "Action": [
                 "iam:PassRole"
             ],
             "Resource": [
                 "arn:aws:iam::*:role/*SageMaker*ForBedrock*"
             ],
             "Condition": {
                 "StringEquals": {
                     "iam:PassedToService": [
                         "sagemaker.amazonaws.com",
                         "bedrock.amazonaws.com"
                     ]
                 }
             }
         },
         {
             "Sid": "PassRoleToBedrock",
             "Effect": "Allow",
             "Action": [
                 "iam:PassRole"
             ],
             "Resource": "arn:aws:iam::*:role/*AmazonBedrock*",
             "Condition": {
                 "StringEquals": {
                     "iam:PassedToService": [
                         "bedrock.amazonaws.com"
                     ]
                 }
             }
         },
         {
             "Sid": "MarketplaceOperationsFromBedrockFor3pModels",
             "Effect": "Allow",
             "Action": [
                 "aws-marketplace:Subscribe",
                 "aws-marketplace:ViewSubscriptions",
                 "aws-marketplace:Unsubscribe"
             ],
             "Resource": "*",
             "Condition": {
                 "StringEquals": {
                     "aws:CalledViaLast": "bedrock.amazonaws.com"
                 }
             }
         }
     ]
 }
```
```
{
     "Version":"2012-10-17",
     "Statement": [
         {
             "Sid": "BedrockAll",
             "Effect": "Allow",
             "Action": [
                 "bedrock:*"
             ],
             "Resource": "*"
         },
         {
             "Sid": "DescribeKey",
             "Effect": "Allow",
             "Action": [
                 "kms:DescribeKey"
             ],
             "Resource": "arn:*:kms:*:::*"
         },
         {
             "Sid": "APIsWithAllResourceAccess",
             "Effect": "Allow",
             "Action": [
                 "iam:ListRoles",
                 "ec2:DescribeVpcs",
                 "ec2:DescribeSubnets",
                 "ec2:DescribeSecurityGroups"
             ],
             "Resource": "*"
         },
         {
             "Sid": "MarketplaceModelEndpointMutatingAPIs",
             "Effect": "Allow",
             "Action": [
                 "sagemaker:CreateEndpoint",
                 "sagemaker:CreateEndpointConfig",
                 "sagemaker:CreateModel",
                 "sagemaker:DeleteEndpoint",
                 "sagemaker:UpdateEndpoint"
             ],
             "Resource": [
                 "arn:aws:sagemaker:*:*:endpoint/*",
                 "arn:aws:sagemaker:*:*:endpoint-config/*",
                 "arn:aws:sagemaker:*:*:model/*"
             ],
             "Condition": {
                 "StringEquals": {
                     "aws:CalledViaLast": "bedrock.amazonaws.com",
                     "aws:ResourceTag/sagemaker-sdk:bedrock": "compatible"
                 }
             }
         },
         {
             "Sid": "MarketplaceModelEndpointAddTagsOperations",
             "Effect": "Allow",
             "Action": [
                 "sagemaker:AddTags"
             ],
             "Resource": [
                 "arn:aws:sagemaker:*:*:endpoint/*",
                 "arn:aws:sagemaker:*:*:endpoint-config/*",
                 "arn:aws:sagemaker:*:*:model/*"
             ],
             "Condition": {
                 "ForAllValues:StringEquals": {
                     "aws:TagKeys": [
                         "sagemaker-sdk:bedrock",
                         "bedrock:marketplace-registration-status",
                         "sagemaker-studio:hub-content-arn"
                     ]
                 },
                 "StringLike": {
                     "aws:RequestTag/sagemaker-sdk:bedrock": "compatible",
                     "aws:RequestTag/bedrock:marketplace-registration-status": "registered",
                     "aws:RequestTag/sagemaker-studio:hub-content-arn": "arn:aws:sagemaker:*:aws:hub-content/SageMakerPublicHub/Model/*"
                 }
             }
         },
         {
             "Sid": "MarketplaceModelEndpointDeleteTagsOperations",
             "Effect": "Allow",
             "Action": [
                 "sagemaker:DeleteTags"
             ],
             "Resource": [
                 "arn:aws:sagemaker:*:*:endpoint/*",
                 "arn:aws:sagemaker:*:*:endpoint-config/*",
                 "arn:aws:sagemaker:*:*:model/*"
             ],
             "Condition": {
                 "ForAllValues:StringEquals": {
                     "aws:TagKeys": [
                         "sagemaker-sdk:bedrock",
                         "bedrock:marketplace-registration-status",
                         "sagemaker-studio:hub-content-arn"
                     ]
                 },
                 "StringLike": {
                     "aws:ResourceTag/sagemaker-sdk:bedrock": "compatible",
                     "aws:ResourceTag/bedrock:marketplace-registration-status": "registered",
                     "aws:ResourceTag/sagemaker-studio:hub-content-arn": "arn:aws:sagemaker:*:aws:hub-content/SageMakerPublicHub/Model/*"
                 }
             }
         },
         {
             "Sid": "MarketplaceModelEndpointNonMutatingAPIs",
             "Effect": "Allow",
             "Action": [
                 "sagemaker:DescribeEndpoint",
                 "sagemaker:DescribeEndpointConfig",
                 "sagemaker:DescribeModel",
                 "sagemaker:DescribeInferenceComponent",
                 "sagemaker:ListEndpoints",
                 "sagemaker:ListTags"
             ],
             "Resource": [
                 "arn:aws:sagemaker:*:*:endpoint/*",
                 "arn:aws:sagemaker:*:*:endpoint-config/*",
                 "arn:aws:sagemaker:*:*:model/*"
             ],
             "Condition": {
                 "StringEquals": {
                     "aws:CalledViaLast": "bedrock.amazonaws.com"
                 }
             }
         },
         {
             "Sid": "MarketplaceModelEndpointInvokingOperations",
             "Effect": "Allow",
             "Action": [
                 "sagemaker:InvokeEndpoint",
                 "sagemaker:InvokeEndpointWithResponseStream"
             ],
             "Resource": [
                 "arn:aws:sagemaker:*:*:endpoint/*"
             ],
             "Condition": {
                 "StringEquals": {
                     "aws:CalledViaLast": "bedrock.amazonaws.com",
                     "aws:ResourceTag/sagemaker-sdk:bedrock": "compatible"
                 }
             }
         },
         {
             "Sid": "DiscoveringMarketplaceModel",
             "Effect": "Allow",
             "Action": [
                 "sagemaker:DescribeHubContent"
             ],
             "Resource": [
                 "arn:aws:sagemaker:*:aws:hub-content/SageMakerPublicHub/Model/*",
                 "arn:aws:sagemaker:*:aws:hub/SageMakerPublicHub"
             ]
         },
         {
             "Sid": "AllowMarketplaceModelsListing",
             "Effect": "Allow",
             "Action": [
                 "sagemaker:ListHubContents"
             ],
             "Resource": "arn:aws:sagemaker:*:aws:hub/SageMakerPublicHub"
         },
         {
             "Sid": "PassRoleToSageMaker",
             "Effect": "Allow",
             "Action": [
                 "iam:PassRole"
             ],
             "Resource": [
                 "arn:aws:iam::*:role/*SageMaker*ForBedrock*"
             ],
             "Condition": {
                 "StringEquals": {
                     "iam:PassedToService": [
                         "sagemaker.amazonaws.com",
                         "bedrock.amazonaws.com"
                     ]
                 }
             }
         },
         {
             "Sid": "PassRoleToBedrock",
             "Effect": "Allow",
             "Action": [
                 "iam:PassRole"
             ],
             "Resource": "arn:aws:iam::*:role/*AmazonBedrock*",
             "Condition": {
                 "StringEquals": {
                     "iam:PassedToService": [
                         "bedrock.amazonaws.com"
                     ]
                 }
             }
         },
         {
             "Sid": "MarketplaceOperationsFromBedrockFor3pModels",
             "Effect": "Allow",
             "Action": [
                 "aws-marketplace:Subscribe",
                 "aws-marketplace:ViewSubscriptions",
                 "aws-marketplace:Unsubscribe"
             ],
             "Resource": "*",
             "Condition": {
                 "StringEquals": {
                     "aws:CalledViaLast": "bedrock.amazonaws.com"
                 }
             }
         }
     ]
 }
```
You can attach the [AmazonBedrockReadOnly](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AmazonBedrockReadOnly.html)
         policy to your IAM identities to grant read-only permissions to view all resources in Amazon Bedrock.

You can attach the [AmazonBedrockLimitedAccess](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AmazonBedrockLimitedAccess.html)
            policy to your IAM identities to allow it access to Amazon Bedrock services, AWS KMS key management, networking resources, and AWS Marketplace subscriptions for third-party foundation models. The policy includes the following statements:

The `BedrockAPIs` statement allows you to perform several operations in Amazon Bedrock including:

Passing the Amazon Bedrock API key when making API requests to the Amazon Bedrock service.

Describing information about resources.

Creating resources (guardrails, models, jobs).

Creating and refining Automated Reasoning policies (create, build, refine, and test policies).

Deleting resources.

Invoking models on all resources.

The `DescribeKey` statement allows you to view information about KMS keys across all regions and accounts, as long as the policies on the keys permit you to do so.

The `APIsWithAllResourceAccess` statement allows you to:

List IAM roles.

Describe Amazon VPC resources (VPCs, subnets, and security groups) across all resources.

The `MarketplaceOperationsFromBedrockFor3pModels` statement enables you to:

Subscribe to AWS Marketplace offerings.

View subscriptions.

Unsubscribe from AWS Marketplace offerings.

The condition key `aws:CalledViaLast` restricts these actions to only when they are called through the Amazon Bedrock service.

You can attach the [AmazonBedrockMarketplaceAccess](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AmazonBedrockMarketplaceAccess.html)
            policy to your IAM identities to allow it to manage and use Amazon Bedrock marketplace model endpoints with SageMaker AI integration. The policy includes the following statements:

The `BedrockMarketplaceAPIs` statement allows you to create, delete, register, deregister, and update marketplace model endpoints in Amazon Bedrock on all resources.

The `MarketplaceModelEndpointMutatingAPIs` statement allows you to create and manage SageMaker AI endpoints, endpoint configurations, and models on specified resources.

Use the `aws:CalledViaLast` condition key to ensure that these actions are only performed when called through Bedrock.

Use the `aws:ResourceTag/sagemaker-sdk:bedrock` condition key to ensure that these actions are only performed on resources tagged as Amazon Bedrock-compatible.

The `MarketplaceModelEndpointAddTagsOperations` statement allows adding specific tags to SageMaker AI endpoints, endpoint configurations, and models on specified resources.

Use the `aws:TagKeys` condition key to restrict which tags can be added

Use the `aws:RequestTag/*` condition key to ensure tag values match specified patterns

The `MarketplaceModelEndpointDeleteTagsOperations` statement allows deleting specific tags from SageMaker AI endpoints, endpoint configurations, and models on specified resources.

Use the `aws:TagKeys` condition key to restrict which tags can be deleted

Use the `aws:ResourceTag/*` condition key to ensure deleted tags match specified patterns

The `MarketplaceModelEndpointNonMutatingAPIs` statement allows viewing and describing SageMaker AI endpoints, endpoint configurations, and models on specified resources.

Use `aws:CalledViaLast` condition key to ensure actions are only performed through the Amazon Bedrock service

The `MarketplaceModelEndpointInvokingOperations` statement allows invoking SageMaker AI endpoints on specified resources.

Use the `aws:CalledViaLast` condition key to ensure actions are only performed through the Amazon Bedrock service

Use the `aws:ResourceTag/sagemaker-sdk:bedrock` condition key to ensure actions are only performed on Bedrock-compatible resources

The `DiscoveringMarketplaceModel` statement allows decribing SageMaker AI hub content on specified resources.

The `AllowMarketplaceModelsListing` statement allows listing SageMaker AI hub contents on specified resources.

The `PassRoleToSageMaker` statement allows passing IAM roles to SageMaker AI and Amazon Bedrock on specified resources.

Use `iam:PassedToService` condition key to ensure roles are only passed to specified services.

The `PassRoleToBedrock` statement allows you to pass specific IAM roles to Amazon Bedrock on specified resources.

Use the `iam:PassedToService` condition key to ensure roles are only passed to the Amazon Bedrock service.

You can attach the [AmazonBedrockMantleFullAccess](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AmazonBedrockMantleFullAccess.html) policy to your IAM identities to grant full access to all Amazon Bedrock Mantle operations.

**Permissions details**

This policy includes the following permissions:

`bedrock-mantle` (Amazon Bedrock Mantle) – Allows principals full access to all actions in the Amazon Bedrock Mantle service.

You can attach the [AmazonBedrockMantleReadOnly](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AmazonBedrockMantleReadOnly.html) policy to your IAM identities to grant read-only permissions to view Amazon Bedrock Mantle resources and call with bearer token.

**Permissions details**

This policy includes the following permissions:

`bedrock-mantle` (Amazon Bedrock Mantle) – Allows principals to get and list Amazon Bedrock Mantle project resources, and call with bearer token for authentication.

You can attach the [AmazonBedrockMantleInferenceAccess](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AmazonBedrockMantleInferenceAccess.html) policy to your IAM identities to grant permissions to run inference on Amazon Bedrock Mantle models.

**Permissions details**

This policy includes the following permissions:

`bedrock-mantle` (Amazon Bedrock Mantle) – Allows principals to get and list Amazon Bedrock Mantle project resources, create inference requests, and call with bearer token for authentication.

View details about updates to AWS managed policies for Amazon Bedrock since this service
         began tracking these changes. For automatic alerts about changes to this page, subscribe to
         the RSS feed on the [Document history for the Amazon Bedrock User Guide](./doc-history.html).

| Change | Description | Date | 
|---|---|---|
| 
 | Amazon Bedrock added a new policy to grant full access to all Amazon Bedrock Mantle operations. | December 3, 2025 | 
| 
 | Amazon Bedrock added a new policy to grant read-only access to Amazon Bedrock Mantle resources. | December 3, 2025 | 
| 
 | Amazon Bedrock added a new policy to grant inference access to Amazon Bedrock Mantle models. | December 3, 2025 | 
| 
 | Amazon Bedrock updated the AmazonBedrockFullAccess managed policy to enable access to all serverless foundation models by default. | July 14th, 2025 | 
| 
 | Amazon Bedrock added a new policy to grant customers permissions to access Amazon Bedrock Marketplace foundation models through a SageMaker AI endpoint. | June 13, 2025 | 
| 
 | Amazon Bedrock added a new policy to grant customers basic permissions to access core actions in Amazon Bedrock. | June 13, 2025 | 
| 
 | Amazon Bedrock updated the AmazonBedrockFullAccess managed policy to grant customers the necessary permissions to create, read, update, and delete Amazon Bedrock Marketplace resources. This includes permissions to manage the underlying Amazon SageMaker AI resources, as they serve as the foundation for the Amazon Bedrock Marketplace functionality. | December 4th, 2024 | 
| 
 | Amazon Bedrock updated the AmazonBedrockReadOnly managed policy to grant customers the necessary permissions to read Amazon Bedrock Marketplace resources. This includes permissions to manage the underlying Amazon SageMaker AI resources, as they serve as the foundation for the Amazon Bedrock Marketplace functionality. | December 4th, 2024 | 
| 
 | Amazon Bedrock updated the AmazonBedrockReadOnly policy to include read-only permissions for custom model import. | October 18, 2024 | 
| 
 | Amazon Bedrock added inference profile read-only permissions. | August 27, 2024 | 
| 
 | Amazon Bedrock updated the AmazonBedrockReadOnly policy to include read-only permissions for Amazon Bedrock Guardrails, Amazon Bedrock Model evaluation, and Amazon Bedrock Batch inference. | August 21, 2024 | 
| 
 | Amazon Bedrock added batch inference (model invocation job) read-only permissions. | August 21, 2024 | 
| 
                         | Amazon Bedrock updated the AmazonBedrockReadOnly policy to include read-only permissions for Amazon Bedrock Custom Model Import. | September 3, 2024 | 
| 
 | Amazon Bedrock added a new policy to give users permissions to create, read, update, and delete resources. | December 12, 2023 | 
| 
 | Amazon Bedrock added a new policy to give users read-only permissions for all actions. | December 12, 2023 | 
| Amazon Bedrock started tracking changes | Amazon Bedrock started tracking changes for its AWS managed policies. | December 12, 2023 | 

Thanks for letting us know we're doing a good job!

If you've got a moment, please tell us what we did right so we can do more of it.

Thanks for letting us know this page needs work. We're sorry we let you down.

If you've got a moment, please tell us how we can make the documentation better.

Updates cover managed policies for DataZone, including Lake Formation permissions, SageMaker roles, cross-account sharing, lineage APIs.

Managed policy grants SageMaker AI model customization permissions, including serverless training, reinforcement learning, MLflow tracking, IAM role passing.

AWS managed policies grant Macie principals full or read-only access, enabling service-linked role creation cost estimation.

Amazon Bedrock enables generative AI development, now featuring GPT-5 agentic coding, Claude Opus 4.7, IAM cost attribution.

Optimize LLM prompts via few-shot techniques, RAG, templates, conversational API calls reduce hallucinations.

Amazon Bedrock foundation model details, IDs, Regions, modalities, inference parameters consolidated models at glance.