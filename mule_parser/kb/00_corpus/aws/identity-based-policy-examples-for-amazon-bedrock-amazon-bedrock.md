# Identity-based policy examples for Amazon Bedrock - Amazon Bedrock

**Source:** [https://docs.aws.amazon.com/bedrock/latest/userguide/security_iam_id-based-policy-examples.html](https://docs.aws.amazon.com/bedrock/latest/userguide/security_iam_id-based-policy-examples.html)

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

By default, users and roles don't have permission to create or modify Amazon Bedrock resources. To grant users permission to perform actions on the resources that they need, an IAM administrator can create IAM policies.

To learn how to create an IAM identity-based policy by using these example JSON policy
 documents, see [Create IAM policies (console)](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_create-console.html) in the
 *IAM User Guide*.

For details about actions and resource types defined by Amazon Bedrock, including the format of the ARNs for each of the resource types, see [Actions, Resources, and Condition Keys for Amazon Bedrock ](https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazonbedrock.html) in the *Service Authorization Reference*.

Identity-based policies determine whether someone can create, access, or delete Amazon Bedrock resources in your account. These actions can incur costs for your AWS account. When you create or edit identity-based policies, follow these guidelines and recommendations:

**Get started with AWS managed policies and move toward least-privilege permissions**
            – To get started granting permissions to your users and workloads, use the *AWS
            managed policies* that grant permissions for many common use cases. They are
            available in your AWS account. We recommend that you reduce permissions further by
            defining AWS customer managed policies that are specific to your use cases. For more information, see 
            [AWS managed policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-vs-inline.html#aws-managed-policies) or [AWS managed policies for job functions](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_job-functions.html) in the *IAM User Guide*.

**Apply least-privilege permissions** – 
            When you set permissions with IAM policies, grant only the permissions required to
            perform a task. You do this by defining the actions that can be taken on specific resources
            under specific conditions, also known as *least-privilege permissions*.
            For more information about using IAM to apply permissions, see [
            Policies and permissions in IAM](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies.html) in the *IAM User Guide*.

**Use conditions in IAM policies to further restrict access**
            – You can add a condition to your policies to limit access to actions and resources. For example, you can write a policy condition to specify that all requests must
            be sent using SSL. You can also use conditions to grant access to service actions
            if they are used through a specific AWS service, such as CloudFormation. For more information, see
            [
            IAM JSON policy elements: Condition](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_elements_condition.html) in the *IAM User Guide*.

**Use IAM Access Analyzer to validate your IAM policies to ensure secure and functional permissions**
            – IAM Access Analyzer validates new and existing policies so that the policies adhere to the IAM policy language (JSON) and IAM best practices.
            IAM Access Analyzer provides more than 100 policy checks and actionable recommendations to help
            you author secure and functional policies. For more information, see [Validate policies with IAM Access Analyzer](https://docs.aws.amazon.com/IAM/latest/UserGuide/access-analyzer-policy-validation.html) in the *IAM User Guide*.

**Require multi-factor authentication (MFA)** –
            If you have a scenario that requires IAM users or a root user in your AWS account, turn on MFA for additional security. To require
            MFA when API operations are called, add MFA conditions to your policies. For
            more information, see [
            Secure API access with MFA](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_mfa_configure-api-require.html) in the *IAM User Guide*.

For more information about best practices in IAM, see [Security best practices in IAM](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html) in the *IAM User Guide*.

To access the Amazon Bedrock console, you must have a minimum set of permissions. These permissions must allow you to list and view details about the Amazon Bedrock resources in your AWS account. If you create an identity-based policy that is more restrictive than the minimum required permissions, the console won't function as intended for entities (users or roles) with that policy.

You don't need to allow minimum console permissions for users that are making calls only to the AWS CLI or the AWS API. Instead, allow access to only the actions that match the API operation that they're trying to perform.

To ensure that users and roles can still use the Amazon Bedrock console, also attach the
              Amazon Bedrock [AmazonBedrockFullAccess](./security-iam-awsmanpol.html#security-iam-awsmanpol-AmazonBedrockFullAccess) or
              [AmazonBedrockReadOnly](./security-iam-awsmanpol.html#security-iam-awsmanpol-AmazonBedrockReadOnly) AWS managed policy to the
              entities. For more information, see [Adding permissions to a user](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_users_change-permissions.html#users_change_permissions-add-console) in the
              *IAM User Guide*.

This example shows how you might create a policy that allows IAM users to view the inline and managed policies that are attached to their user identity. This policy includes permissions to complete this action on the console or programmatically using the AWS CLI or AWS API.

```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "ViewOwnUserInfo",
            "Effect": "Allow",
            "Action": [
                "iam:GetUserPolicy",
                "iam:ListGroupsForUser",
                "iam:ListAttachedUserPolicies",
                "iam:ListUserPolicies",
                "iam:GetUser"
            ],
            "Resource": ["arn:aws:iam::*:user/${aws:username}"]
        },
        {
            "Sid": "NavigateInConsole",
            "Effect": "Allow",
            "Action": [
                "iam:GetGroupPolicy",
                "iam:GetPolicyVersion",
                "iam:GetPolicy",
                "iam:ListAttachedGroupPolicies",
                "iam:ListGroupPolicies",
                "iam:ListPolicyVersions",
                "iam:ListPolicies",
                "iam:ListUsers"
            ],
            "Resource": "*"
        }
    ]
}
```
To prevent a user from invoking foundation models, you need to deny access to API actions that invoke models directly. The following example shows a identity-based policy that denies access to running inference on a specific model. This policy can be used as a service control policy (SCP) to control model access across an organization.

```
{
          "Version":"2012-10-17",
          "Statement": {
              "Sid": "DenyInference",
              "Effect": "Deny",
              "Action": [
                  "bedrock:InvokeModel",
                  "bedrock:InvokeModelWithResponseStream",
                  "bedrock:CreateModelInvocationJob"
               ],
              "Resource": "arn:aws:bedrock:*::foundation-model/
```
`model-id`"
          }
      }        
```
{
          "Version":"2012-10-17",
          "Statement": {
              "Sid": "DenyInference",
              "Effect": "Deny",
              "Action": [
                  "bedrock:InvokeModel",
                  "bedrock:InvokeModelWithResponseStream",
                  "bedrock:CreateModelInvocationJob"
               ],
              "Resource": "arn:aws:bedrock:*::foundation-model/
```
`model-id`"
          }
      }        
To deny inference access to all foundation models, use `*` for the model ID.
      Other actions, such as `Converse` and `StartAsyncInvoke`, are blocked
      automatically when `InvokeModel` is denied. If you want to explicitly deny all inference actions, you can use `bedrock:InvokeModel*` as a wildcard or add `bedrock:Converse` and `bedrock:ConverseStream` to the action list. For a list of model IDs, see [Supported foundation models in Amazon Bedrock](./models-supported.html)

The following is a sample policy that you can attach to an IAM role to allow it to use a provisioned model in model inference. For example, you could attach this policy to a role that you want to only have permissions to use a provisioned model. The role won't be able to manage or see information about the Provisioned Throughput.

```
{
    "Version":"2012-10-17",
    "Statement": [
        {
            "Sid": "
```
`ProvisionedThroughputModelInvocation`",
            "Effect": "Allow",
            "Action": [
                "bedrock:InvokeModel",
                "bedrock:InvokeModelWithResponseStream"
            ],
            "Resource": "arn:aws:bedrock:us-east-1:`123456789012`:provisioned-model/`my-provisioned-model`"
        }
    ]
}
```
{
    "Version":"2012-10-17",
    "Statement": [
        {
            "Sid": "
```
`ProvisionedThroughputModelInvocation`",
            "Effect": "Allow",
            "Action": [
                "bedrock:InvokeModel",
                "bedrock:InvokeModelWithResponseStream"
            ],
            "Resource": "arn:aws:bedrock:us-east-1:`123456789012`:provisioned-model/`my-provisioned-model`"
        }
    ]
}
The following policy grants the minimum permissions required to use the Amazon Bedrock Playground in the AWS Management Console to chat with a model. Replace `<region>`, `<account-id>`, and the model resource ARNs with your values.

```
{
    "Version": "2012-10-17", 
    "Statement": [
        {
            "Sid": "BedrockConsoleRead",
            "Effect": "Allow",
            "Action": [
                "bedrock:ListFoundationModels",
                "bedrock:ListInferenceProfiles",
                "bedrock:ListProvisionedModelThroughputs",
                "bedrock:ListCustomModels",
                "bedrock:ListGuardrails",
                "bedrock:ListFoundationModelAgreementOffers",
                "bedrock:ListMarketplaceModelEndpoints",
                "bedrock:ListImportedModels",
                "bedrock:ListPromptRouters",
                "bedrock:GetFoundationModel",
                "bedrock:GetFoundationModelAvailability",
                "bedrock:GetInferenceProfile",
                "bedrock:GetUseCaseForModelAccess",
                "bedrock:PutUseCaseForModelAccess"
            ],
            "Resource": "*"
        },
        {
            "Sid": "SageMakerHubRead",
            "Effect": "Allow",
            "Action": [
                "sagemaker:ListHubContents"
            ],
            "Resource": "arn:aws:sagemaker:*:aws:hub/SageMakerPublicHub"
        },
        {
            "Sid": "InvokeModel",
            "Effect": "Allow",
            "Action": [
                "bedrock:InvokeModel",
                "bedrock:InvokeModelWithResponseStream"
            ],
            "Resource": [
                "arn:aws:bedrock:*::foundation-model/*",
                "arn:aws:bedrock:
```
`<region>`:`<account-id>`:inference-profile/*"
            ]
        },
        {
            "Sid": "MarketplaceSubscription",
            "Effect": "Allow",
            "Action": [
                "aws-marketplace:ViewSubscriptions",
                "aws-marketplace:Subscribe"
            ],
            "Resource": "*",
            "Condition": {
                "StringEquals": {
                    "aws:CalledViaLast": "bedrock.amazonaws.com"
                }
            }
        }
    ]
}To restrict access to a specific model, replace the `InvokeModel` statement's `Resource` with the specific model and inference profile ARNs.

Thanks for letting us know we're doing a good job!

If you've got a moment, please tell us what we did right so we can do more of it.

Thanks for letting us know this page needs work. We're sorry we let you down.

If you've got a moment, please tell us how we can make the documentation better.

IAM policies grant least-privilege access, enabling job submission, license endpoints, console use, farm queue monitoring.

IAM policies grant least-privilege App Studio access using MFA conditions, Access Analyzer validation, managed policies.

IAM policies grant least-privilege permissions, restrict access via conditions, validate with Access Analyzer, require MFA API operations.

Amazon Bedrock enables generative AI development, now featuring GPT-5 agentic coding, Claude Opus 4.7, IAM cost attribution.

Optimize LLM prompts via few-shot techniques, RAG, templates, conversational API calls reduce hallucinations.

Amazon Bedrock foundation model details, IDs, Regions, modalities, inference parameters consolidated models at glance.