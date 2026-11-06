# IAM Access Analyzer examples using AWS CLI - AWS Command Line Interface

**Source:** [https://docs.aws.amazon.com/cli/latest/userguide/cli_accessanalyzer_code_examples.html](https://docs.aws.amazon.com/cli/latest/userguide/cli_accessanalyzer_code_examples.html)

---

The following code examples show you how to perform actions and implement common scenarios by using the AWS Command Line Interface with IAM Access Analyzer.

*Actions* are code excerpts from larger programs and must be run in context. While actions show you how to call individual service functions, you can see actions in context in their related scenarios.

Each example includes a link to the complete source code, where you can find instructions on how to set up and run the code in context.

###### Topics

## Actions

    The following code example shows how to use `apply-archive-rule`.

- **AWS CLI**
- 
            
                    **To apply an archive rule to existing findings that meet the archive rule criteria**The following `apply-archive-rule`example applies an archive rule to existing findings that meet the archive rule criteria.`aws accessanalyzer apply-archive-rule \ --analyzer-arn``arn:aws:access-analyzer:us-west-2:111122223333:analyzer/UnusedAccess-ConsoleAnalyzer-organization`\ --rule-name`MyArchiveRule`This command produces no output. For more information, see [Archive rules](https://docs.aws.amazon.com/IAM/latest/UserGuide/access-analyzer-archive-rules.html)in the*AWS IAM User Guide*.- 
                    For API details, see [ApplyArchiveRule](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/accessanalyzer/apply-archive-rule.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `cancel-policy-generation`.

- **AWS CLI**
- 
            
                    **To cancel the requested policy generation**The following `cancel-policy-generation`example cancels the requested policy generation job id.`aws accessanalyzer cancel-policy-generation \ --job-id``923a56b0-ebb8-4e80-8a3c-a11ccfbcd6f2`This command produces no output. For more information, see [IAM Access Analyzer policy generation](https://docs.aws.amazon.com/IAM/latest/UserGuide/access-analyzer-policy-generation.html)in the*AWS IAM User Guide*.- 
                    For API details, see [CancelPolicyGeneration](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/accessanalyzer/cancel-policy-generation.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `check-access-not-granted`.

- **AWS CLI**
- 
            
                    **To check whether the specified access isn't allowed by a policy**The following `check-access-not-granted`example checks whether the specified access isn't allowed by a policy.`aws accessanalyzer check-access-not-granted \ --policy-document``file://myfile.json`\ --access actions="s3:DeleteBucket","s3:GetBucketLocation" \ --policy-type`IDENTITY_POLICY`Contents of `myfile.json`:`{ "Version":"2012-10-17", "Statement": [ { "Effect": "Allow", "Action": [ "s3:GetObject", "s3:ListBucket" ], "Resource": [ "arn:aws:s3:::amzn-s3-demo-bucket", "arn:aws:s3:::amzn-s3-demo-bucket/*" ] } ] }`Output: `{ "result": "PASS", "message": "The policy document does not grant access to perform one or more of the listed actions." }`For more information, see [Previewing access with IAM Access Analyzer APIs](https://docs.aws.amazon.com/IAM/latest/UserGuide/access-analyzer-preview-access-apis.html)in the*AWS IAM User Guide*.- 
                    For API details, see [CheckAccessNotGranted](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/accessanalyzer/check-access-not-granted.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `check-no-new-access`.

- **AWS CLI**
- 
            
                    **To check whether new access is allowed for an updated policy when compared to the existing policy**The following `check-no-new-access`example checks whether new access is allowed for an updated policy when compared to the existing policy.`aws accessanalyzer check-no-new-access \ --existing-policy-document``file://existing-policy.json`\ --new-policy-document`file://new-policy.json`\ --policy-type`IDENTITY_POLICY`Contents of `existing-policy.json`:`{ "Version":"2012-10-17", "Statement": [ { "Effect": "Allow", "Action": [ "s3:GetObject", "s3:ListBucket" ], "Resource": [ "arn:aws:s3:::amzn-s3-demo-bucket", "arn:aws:s3:::amzn-s3-demo-bucket/*" ] } ] }`Contents of `new-policy.json`:`{ "Version":"2012-10-17", "Statement": [ { "Effect": "Allow", "Action": [ "s3:GetObject", "s3:GetObjectAcl", "s3:ListBucket" ], "Resource": [ "arn:aws:s3:::amzn-s3-demo-bucket", "arn:aws:s3:::amzn-s3-demo-bucket/*" ] } ] }`Output: `{ "result": "FAIL", "message": "The modified permissions grant new access compared to your existing policy.", "reasons": [ { "description": "New access in the statement with index: 0.", "statementIndex": 0 } ] }`For more information, see [Previewing access with IAM Access Analyzer APIs](https://docs.aws.amazon.com/IAM/latest/UserGuide/access-analyzer-preview-access-apis.html)in the*AWS IAM User Guide*.- 
                    For API details, see [CheckNoNewAccess](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/accessanalyzer/check-no-new-access.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `check-no-public-access`.

- **AWS CLI**
- 
            
                    **To check whether a resource policy can grant public access to the specified resource type**The following `check-no-public-access`example checks whether a resource policy can grant public access to the specified resource type.`aws accessanalyzer check-no-public-access \ --policy-document``file://check-no-public-access-myfile.json`\ --resource-type`AWS::S3::Bucket`Contents of `myfile.json`:`{ "Version":"2012-10-17", "Statement": [ { "Sid": "CheckNoPublicAccess", "Effect": "Allow", "Principal": { "AWS": "arn:aws:iam::111122223333:user/JohnDoe" }, "Action": [ "s3:GetObject" ] } ] }`Output: `{ "result": "PASS", "message": "The resource policy does not grant public access for the given resource type." }`For more information, see [Previewing access with IAM Access Analyzer APIs](https://docs.aws.amazon.com/IAM/latest/UserGuide/access-analyzer-preview-access-apis.html)in the*AWS IAM User Guide*.- 
                    For API details, see [CheckNoPublicAccess](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/accessanalyzer/check-no-public-access.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `create-access-preview`.

- **AWS CLI**
- 
            
                    **To create an access preview that allows you to preview IAM Access Analyzer findings for your resource before deploying resource permissions**The following `create-access-preview`example creates an access preview that allows you to preview IAM Access Analyzer findings for your resource before deploying resource permissions in your AWS account.`aws accessanalyzer create-access-preview \ --analyzer-arn``arn:aws:access-analyzer:us-west-2:111122223333:analyzer/ConsoleAnalyzer-account`\ --configurations`file://myfile.json`Contents of `myfile.json`:`{ "arn:aws:s3:::amzn-s3-demo-bucket": { "s3Bucket": { "bucketPolicy": "{\"Version\":\"2012-10-17\",\"Statement\":[{\"Effect\":\"Allow\",\"Principal\":{\"AWS\":[\"arn:aws:iam::111122223333:root\"]},\"Action\":[\"s3:PutObject\",\"s3:PutObjectAcl\"],\"Resource\":\"arn:aws:s3:::amzn-s3-demo-bucket/*\"}]}", "bucketPublicAccessBlock": { "ignorePublicAcls": true, "restrictPublicBuckets": true }, "bucketAclGrants": [ { "grantee": { "id": "79a59df900b949e55d96a1e698fbacedfd6e09d98eacf8f8d5218e7cd47ef2be" }, "permission": "READ" } ] } } }`Output: `{ "id": "3c65eb13-6ef9-4629-8919-a32043619e6b" }`For more information, see [Previewing access with IAM Access Analyzer APIs](https://docs.aws.amazon.com/IAM/latest/UserGuide/access-analyzer-preview-access-apis.html)in the*AWS IAM User Guide*.- 
                    For API details, see [CreateAccessPreview](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/accessanalyzer/create-access-preview.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `create-analyzer`.

- **AWS CLI**
- 
            
                    **To create an analyzer**The following `create-analyzer`example creates an analyzer in your AWS account.`aws accessanalyzer create-analyzer \ --analyzer-name``example`\ --type`ACCOUNT`Output: `{ "arn": "arn:aws:access-analyzer:us-east-2:111122223333:analyzer/example" }`For more information, see [Getting started with AWS Identity and Access Management Access Analyzer findings](https://docs.aws.amazon.com/IAM/latest/UserGuide/access-analyzer-getting-started.html)in the*AWS IAM User Guide*.- 
                    For API details, see [CreateAnalyzer](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/accessanalyzer/create-analyzer.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `create-archive-rule`.

- **AWS CLI**
- 
            
                    **To create an archive rule for the specified analyzer**The following `create-archive-rule`example creates an archive rule for the specified analyzer in your AWS account.`aws accessanalyzer create-archive-rule \ --analyzer-name``UnusedAccess-ConsoleAnalyzer-organization`\ --rule-name`MyRule`\ --filter '`{"resource": {"contains": ["Cognito"]}, "resourceType": {"eq": ["AWS::IAM::Role"]}}`'This command produces no output. For more information, see [Archive rules](https://docs.aws.amazon.com/IAM/latest/UserGuide/access-analyzer-archive-rules.html)in the*AWS IAM User Guide*.- 
                    For API details, see [CreateArchiveRule](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/accessanalyzer/create-archive-rule.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `delete-analyzer`.

- **AWS CLI**
- 
            
                    **To delete the specified analyzer**The following `delete-analyzer`example deletes the specified analyzer in your AWS account.`aws accessanalyzer delete-analyzer \ --analyzer-name``example`This command produces no output. For more information, see [Archive rules](https://docs.aws.amazon.com/IAM/latest/UserGuide/access-analyzer-archive-rules.html)in the*AWS IAM User Guide*.- 
                    For API details, see [DeleteAnalyzer](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/accessanalyzer/delete-analyzer.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `delete-archive-rule`.

- **AWS CLI**
- 
            
                    **To delete the specified archive rule**The following `delete-archive-rule`example deletes the specified archive rule in your AWS account.`aws accessanalyzer delete-archive-rule \ --analyzer-name``UnusedAccess-ConsoleAnalyzer-organization`\ --rule-name`MyRule`This command produces no output. For more information, see [Archive rules](https://docs.aws.amazon.com/IAM/latest/UserGuide/access-analyzer-archive-rules.html)in the*AWS IAM User Guide*.- 
                    For API details, see [DeleteArchiveRule](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/accessanalyzer/delete-archive-rule.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `get-access-preview`.

- **AWS CLI**
- 
            
                    **To retrieves information about an access preview for the specified analyzer**The following `get-access-preview`example retrieves information about an access preview for the specified analyzer in your AWS account.`aws accessanalyzer get-access-preview \ --access-preview-id``3c65eb13-6ef9-4629-8919-a32043619e6b`\ --analyzer-arn`arn:aws:access-analyzer:us-west-2:111122223333:analyzer/ConsoleAnalyzer-account`Output: `{ "accessPreview": { "id": "3c65eb13-6ef9-4629-8919-a32043619e6b", "analyzerArn": "arn:aws:access-analyzer:us-west-2:111122223333:analyzer/ConsoleAnalyzer-account", "configurations": { "arn:aws:s3:::amzn-s3-demo-bucket": { "s3Bucket": { "bucketPolicy": "{\"Version\":\"2012-10-17\",\"Statement\":[{\"Effect\":\"Allow\",\"Principal\":{\"AWS\":[\"arn:aws:iam::111122223333:root\"]},\"Action\":[\"s3:PutObject\",\"s3:PutObjectAcl\"],\"Resource\":\"arn:aws:s3:::amzn-s3-demo-bucket/*\"}]}", "bucketAclGrants": [ { "permission": "READ", "grantee": { "id": "79a59df900b949e55d96a1e698fbacedfd6e09d98eacf8f8d5218e7cd47ef2be" } } ], "bucketPublicAccessBlock": { "ignorePublicAcls": true, "restrictPublicBuckets": true } } } }, "createdAt": "2024-02-17T00:18:44+00:00", "status": "COMPLETED" } }`For more information, see [Previewing access with IAM Access Analyzer APIs](https://docs.aws.amazon.com/IAM/latest/UserGuide/access-analyzer-preview-access-apis.html)in the*AWS IAM User Guide*.- 
                    For API details, see [GetAccessPreview](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/accessanalyzer/get-access-preview.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `get-analyzed-resource`.

- **AWS CLI**
- 
            
                    **To retrieve information about a resource that was analyzed**The following `get-analyzed-resource`example retrieves information about a resource that was analyzed in your AWS account.`aws accessanalyzer get-analyzed-resource \ --analyzer-arn``arn:aws:access-analyzer:us-west-2:111122223333:analyzer/ConsoleAnalyzer-account`\ --resource-arn`arn:aws:s3:::amzn-s3-demo-bucket`Output: `{ "resource": { "analyzedAt": "2024-02-15T18:01:53.002000+00:00", "isPublic": false, "resourceArn": "arn:aws:s3:::amzn-s3-demo-bucket", "resourceOwnerAccount": "111122223333", "resourceType": "AWS::S3::Bucket" } }`For more information, see [Using AWS Identity and Access Management Access Analyzer](https://docs.aws.amazon.com/IAM/latest/UserGuide/what-is-access-analyzer.html)in the*AWS IAM User Guide*.- 
                    For API details, see [GetAnalyzedResource](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/accessanalyzer/get-analyzed-resource.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `get-analyzer`.

- **AWS CLI**
- 
            
                    **To retrieve information about the specified analyzer**The following `get-analyzer`example retrieves information about the specified analyzer in your AWS account.`aws accessanalyzer get-analyzer \ --analyzer-name``ConsoleAnalyzer-account`Output: `{ "analyzer": { "arn": "arn:aws:access-analyzer:us-west-2:111122223333:analyzer/ConsoleAnalyzer-account", "createdAt": "2019-12-03T07:28:17+00:00", "lastResourceAnalyzed": "arn:aws:sns:us-west-2:111122223333:config-topic", "lastResourceAnalyzedAt": "2024-02-15T18:01:53.003000+00:00", "name": "ConsoleAnalyzer-account", "status": "ACTIVE", "tags": { "auto-delete": "no" }, "type": "ACCOUNT" } }`For more information, see [Using AWS Identity and Access Management Access Analyzer](https://docs.aws.amazon.com/IAM/latest/UserGuide/what-is-access-analyzer.html)in the*AWS IAM User Guide*.- 
                    For API details, see [GetAnalyzer](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/accessanalyzer/get-analyzer.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `get-archive-rule`.

- **AWS CLI**
- 
            
                    **To retrieve information about an archive rule**The following `get-archive-rule`example retrieves information about an archive rule in your AWS account.`aws accessanalyzer get-archive-rule \ --analyzer-name``UnusedAccess-ConsoleAnalyzer-organization`\ --rule-name`MyArchiveRule`Output: `{ "archiveRule": { "createdAt": "2024-02-15T00:49:27+00:00", "filter": { "resource": { "contains": [ "Cognito" ] }, "resourceType": { "eq": [ "AWS::IAM::Role" ] } }, "ruleName": "MyArchiveRule", "updatedAt": "2024-02-15T00:49:27+00:00" } }`For more information, see [Archive rules](https://docs.aws.amazon.com/IAM/latest/UserGuide/access-analyzer-archive-rules.html)in the*AWS IAM User Guide*.- 
                    For API details, see [GetArchiveRule](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/accessanalyzer/get-archive-rule.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `get-finding-v2`.

- **AWS CLI**
- 
            
                    **To retrieve information about the specified finding**The following `get-finding-v2`example etrieves information about the specified finding in your AWS account.`aws accessanalyzer get-finding-v2 \ --analyzer-arn``arn:aws:access-analyzer:us-west-2:111122223333:analyzer/ConsoleAnalyzer-organization`\ --id`0910eedb-381e-4e95-adda-0d25c19e6e90`Output: `{ "findingDetails": [ { "externalAccessDetails": { "action": [ "sts:AssumeRoleWithWebIdentity" ], "condition": { "cognito-identity.amazonaws.com:aud": "us-west-2:EXAMPLE0-0000-0000-0000-000000000000" }, "isPublic": false, "principal": { "Federated": "cognito-identity.amazonaws.com" } } } ], "resource": "arn:aws:iam::111122223333:role/Cognito_testpoolAuth_Role", "status": "ACTIVE", "error": null, "createdAt": "2021-02-26T21:17:50.905000+00:00", "resourceType": "AWS::IAM::Role", "findingType": "ExternalAccess", "resourceOwnerAccount": "111122223333", "analyzedAt": "2024-02-16T18:17:47.888000+00:00", "id": "0910eedb-381e-4e95-adda-0d25c19e6e90", "updatedAt": "2021-02-26T21:17:50.905000+00:00" }`For more information, see [Reviewing findings](https://docs.aws.amazon.com/IAM/latest/UserGuide/access-analyzer-findings-view.html)in the*AWS IAM User Guide*.- 
                    For API details, see [GetFindingV2](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/accessanalyzer/get-finding-v2.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `get-finding`.

- **AWS CLI**
- 
            
                    **To retrieve information about the specified finding**The following `get-finding`example etrieves information about the specified finding in your AWS account.`aws accessanalyzer get-finding \ --analyzer-arn``arn:aws:access-analyzer:us-west-2:111122223333:analyzer/ConsoleAnalyzer-organization`\ --id`0910eedb-381e-4e95-adda-0d25c19e6e90`Output: `{ "finding": { "id": "0910eedb-381e-4e95-adda-0d25c19e6e90", "principal": { "Federated": "cognito-identity.amazonaws.com" }, "action": [ "sts:AssumeRoleWithWebIdentity" ], "resource": "arn:aws:iam::111122223333:role/Cognito_testpoolAuth_Role", "isPublic": false, "resourceType": "AWS::IAM::Role", "condition": { "cognito-identity.amazonaws.com:aud": "us-west-2:EXAMPLE0-0000-0000-0000-000000000000" }, "createdAt": "2021-02-26T21:17:50.905000+00:00", "analyzedAt": "2024-02-16T18:17:47.888000+00:00", "updatedAt": "2021-02-26T21:17:50.905000+00:00", "status": "ACTIVE", "resourceOwnerAccount": "111122223333" } }`For more information, see [Reviewing findings](https://docs.aws.amazon.com/IAM/latest/UserGuide/access-analyzer-findings-view.html)in the*AWS IAM User Guide*.- 
                    For API details, see [GetFinding](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/accessanalyzer/get-finding.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `get-generated-policy`.

- **AWS CLI**
- 
            
                    **To retrieve the policy that was generated using the `StartPolicyGeneration` API**The following `get-generated-policy`example retrieves the policy that was generated using the StartPolicyGeneration API in your AWS account.`aws accessanalyzer get-generated-policy \ --job-id``c557dc4a-0338-4489-95dd-739014860ff9`Output: `{ "generatedPolicyResult": { "generatedPolicies": [ { "policy": "{\"Version\":\"2012-10-17\",\"Statement\":[{\"Sid\":\"SupportedServiceSid0\",\"Effect\":\"Allow\",\"Action\":[\"access-analyzer:GetAnalyzer\",\"access-analyzer:ListAnalyzers\",\"access-analyzer:ListArchiveRules\",\"access-analyzer:ListFindings\",\"cloudtrail:DescribeTrails\",\"cloudtrail:GetEventDataStore\",\"cloudtrail:GetEventSelectors\",\"cloudtrail:GetInsightSelectors\",\"cloudtrail:GetTrailStatus\",\"cloudtrail:ListChannels\",\"cloudtrail:ListEventDataStores\",\"cloudtrail:ListQueries\",\"cloudtrail:ListTags\",\"cloudtrail:LookupEvents\",\"ec2:DescribeRegions\",\"iam:GetAccountSummary\",\"iam:GetOpenIDConnectProvider\",\"iam:GetRole\",\"iam:ListAccessKeys\",\"iam:ListAccountAliases\",\"iam:ListOpenIDConnectProviders\",\"iam:ListRoles\",\"iam:ListSAMLProviders\",\"kms:ListAliases\",\"s3:GetBucketLocation\",\"s3:ListAllMyBuckets\"],\"Resource\":\"*\"}]}" } ], "properties": { "cloudTrailProperties": { "endTime": "2024-02-14T22:44:40+00:00", "startTime": "2024-02-13T00:30:00+00:00", "trailProperties": [ { "allRegions": true, "cloudTrailArn": "arn:aws:cloudtrail:us-west-2:111122223333:trail/my-trail", "regions": [] } ] }, "isComplete": false, "principalArn": "arn:aws:iam::111122223333:role/Admin" } }, "jobDetails": { "completedOn": "2024-02-14T22:47:01+00:00", "jobId": "c557dc4a-0338-4489-95dd-739014860ff9", "startedOn": "2024-02-14T22:44:41+00:00", "status": "SUCCEEDED" } }`For more information, see [IAM Access Analyzer policy generation](https://docs.aws.amazon.com/IAM/latest/UserGuide/access-analyzer-policy-generation.html)in the*AWS IAM User Guide*.- 
                    For API details, see [GetGeneratedPolicy](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/accessanalyzer/get-generated-policy.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `list-access-preview-findings`.

- **AWS CLI**
- 
            
                    **To retrieve a list of access preview findings generated by the specified access preview**The following `list-access-preview-findings`example retrieves a list of access preview findings generated by the specified access preview in your AWS account.`aws accessanalyzer list-access-preview-findings \ --access-preview-id``3c65eb13-6ef9-4629-8919-a32043619e6b`\ --analyzer-arn`arn:aws:access-analyzer:us-west-2:111122223333:analyzer/ConsoleAnalyzer-account`Output: `{ "findings": [ { "id": "e22fc158-1c87-4c32-9464-e7f405ce8d74", "principal": { "AWS": "111122223333" }, "action": [ "s3:PutObject", "s3:PutObjectAcl" ], "condition": {}, "resource": "arn:aws:s3:::amzn-s3-demo-bucket", "isPublic": false, "resourceType": "AWS::S3::Bucket", "createdAt": "2024-02-17T00:18:46+00:00", "changeType": "NEW", "status": "ACTIVE", "resourceOwnerAccount": "111122223333", "sources": [ { "type": "POLICY" } ] } ] }`For more information, see [Previewing access with IAM Access Analyzer APIs](https://docs.aws.amazon.com/IAM/latest/UserGuide/access-analyzer-preview-access-apis.html)in the*AWS IAM User Guide*.- 
                    For API details, see [ListAccessPreviewFindings](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/accessanalyzer/list-access-preview-findings.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `list-access-previews`.

- **AWS CLI**
- 
            
                    **To retrieve a list of access previews for the specified analyzer**The following `list-access-previews`example retrieves a list of access previews for the specified analyzer in your AWS account.`aws accessanalyzer list-access-previews \ --analyzer-arn``arn:aws:access-analyzer:us-west-2:111122223333:analyzer/ConsoleAnalyzer-account`Output: `{ "accessPreviews": [ { "id": "3c65eb13-6ef9-4629-8919-a32043619e6b", "analyzerArn": "arn:aws:access-analyzer:us-west-2:111122223333:analyzer/ConsoleAnalyzer-account", "createdAt": "2024-02-17T00:18:44+00:00", "status": "COMPLETED" } ] }`For more information, see [Previewing access with IAM Access Analyzer APIs](https://docs.aws.amazon.com/IAM/latest/UserGuide/access-analyzer-preview-access-apis.html)in the*AWS IAM User Guide*.- 
                    For API details, see [ListAccessPreviews](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/accessanalyzer/list-access-previews.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `list-analyzed-resources`.

- **AWS CLI**
- 
            
                    **To list the available widgets**The following `list-analyzed-resources`example lists the available widgets in your AWS account.`aws accessanalyzer list-analyzed-resources \ --analyzer-arn``arn:aws:access-analyzer:us-west-2:111122223333:analyzer/ConsoleAnalyzer-account`\ --resource-type`AWS::IAM::Role`Output: `{ "analyzedResources": [ { "resourceArn": "arn:aws:sns:us-west-2:111122223333:Validation-Email", "resourceOwnerAccount": "111122223333", "resourceType": "AWS::SNS::Topic" }, { "resourceArn": "arn:aws:sns:us-west-2:111122223333:admin-alerts", "resourceOwnerAccount": "111122223333", "resourceType": "AWS::SNS::Topic" }, { "resourceArn": "arn:aws:sns:us-west-2:111122223333:config-topic", "resourceOwnerAccount": "111122223333", "resourceType": "AWS::SNS::Topic" }, { "resourceArn": "arn:aws:sns:us-west-2:111122223333:inspector-topic", "resourceOwnerAccount": "111122223333", "resourceType": "AWS::SNS::Topic" } ] }`For more information, see [Using AWS Identity and Access Management Access Analyzer](https://docs.aws.amazon.com/IAM/latest/UserGuide/what-is-access-analyzer.html)in the*AWS IAM User Guide*.- 
                    For API details, see [ListAnalyzedResources](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/accessanalyzer/list-analyzed-resources.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `list-analyzers`.

- **AWS CLI**
- 
            
                    **To retrieve a list of analyzers**The following `list-analyzers`example retrieves a list of analyzers in your AWS account.`aws accessanalyzer list-analyzers`Output: `{ "analyzers": [ { "arn": "arn:aws:access-analyzer:us-west-2:111122223333:analyzer/UnusedAccess-ConsoleAnalyzer-organization", "createdAt": "2024-02-15T00:46:40+00:00", "name": "UnusedAccess-ConsoleAnalyzer-organization", "status": "ACTIVE", "tags": { "auto-delete": "no" }, "type": "ORGANIZATION_UNUSED_ACCESS" }, { "arn": "arn:aws:access-analyzer:us-west-2:111122223333:analyzer/ConsoleAnalyzer-organization", "createdAt": "2020-04-25T07:43:28+00:00", "lastResourceAnalyzed": "arn:aws:s3:::amzn-s3-demo-bucket", "lastResourceAnalyzedAt": "2024-02-15T21:51:56.517000+00:00", "name": "ConsoleAnalyzer-organization", "status": "ACTIVE", "tags": { "auto-delete": "no" }, "type": "ORGANIZATION" }, { "arn": "arn:aws:access-analyzer:us-west-2:111122223333:analyzer/ConsoleAnalyzer-account", "createdAt": "2019-12-03T07:28:17+00:00", "lastResourceAnalyzed": "arn:aws:sns:us-west-2:111122223333:config-topic", "lastResourceAnalyzedAt": "2024-02-15T18:01:53.003000+00:00", "name": "ConsoleAnalyzer-account", "status": "ACTIVE", "tags": { "auto-delete": "no" }, "type": "ACCOUNT" } ] }`For more information, see [Using AWS Identity and Access Management Access Analyzer](https://docs.aws.amazon.com/IAM/latest/UserGuide/what-is-access-analyzer.html)in the*AWS IAM User Guide*.- 
                    For API details, see [ListAnalyzers](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/accessanalyzer/list-analyzers.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `list-archive-rules`.

- **AWS CLI**
- 
            
                    **To retrieve a list of archive rules created for the specified analyzer**The following `list-archive-rules`example retrieves a list of archive rules created for the specified analyzer in your AWS account.`aws accessanalyzer list-archive-rules \ --analyzer-name``UnusedAccess-ConsoleAnalyzer-organization`Output: `{ "archiveRules": [ { "createdAt": "2024-02-15T00:49:27+00:00", "filter": { "resource": { "contains": [ "Cognito" ] }, "resourceType": { "eq": [ "AWS::IAM::Role" ] } }, "ruleName": "MyArchiveRule", "updatedAt": "2024-02-15T00:49:27+00:00" }, { "createdAt": "2024-02-15T23:27:45+00:00", "filter": { "findingType": { "eq": [ "UnusedIAMUserAccessKey" ] } }, "ruleName": "ArchiveRule-56125a39-e517-4ff8-afb1-ef06f58db612", "updatedAt": "2024-02-15T23:27:45+00:00" } ] }`For more information, see [Using AWS Identity and Access Management Access Analyzer](https://docs.aws.amazon.com/IAM/latest/UserGuide/what-is-access-analyzer.html)in the*AWS IAM User Guide*.- 
                    For API details, see [ListArchiveRules](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/accessanalyzer/list-archive-rules.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `list-findings-v2`.

- **AWS CLI**
- 
            
                    **To retrieve a list of findings generated by the specified analyzer**The following `list-findings-v2`example retrieves a list of findings generated by the specified analyzer in your AWS account. This example filters the results to include only IAM roles whose name contains`Cognito`.`aws accessanalyzer list-findings-v2 \ --analyzer-arn``arn:aws:access-analyzer:us-west-2:111122223333:analyzer/ConsoleAnalyzer-account`\ --filter '`{"resource": {"contains": ["Cognito"]}, "resourceType": {"eq": ["AWS::IAM::Role"]}}`'Output: `{ "findings": [ { "analyzedAt": "2024-02-16T18:17:47.888000+00:00", "createdAt": "2021-02-26T21:17:24.710000+00:00", "id": "597f3bc2-3adc-4c18-9879-5c4b23485e46", "resource": "arn:aws:iam::111122223333:role/Cognito_testpoolUnauth_Role", "resourceType": "AWS::IAM::Role", "resourceOwnerAccount": "111122223333", "status": "ACTIVE", "updatedAt": "2021-02-26T21:17:24.710000+00:00", "findingType": "ExternalAccess" }, { "analyzedAt": "2024-02-16T18:17:47.888000+00:00", "createdAt": "2021-02-26T21:17:50.905000+00:00", "id": "ce0e221a-85b9-4d52-91ff-d7678075442f", "resource": "arn:aws:iam::111122223333:role/Cognito_testpoolAuth_Role", "resourceType": "AWS::IAM::Role", "resourceOwnerAccount": "111122223333", "status": "ACTIVE", "updatedAt": "2021-02-26T21:17:50.905000+00:00", "findingType": "ExternalAccess" } ] }`For more information, see [Using AWS Identity and Access Management Access Analyzer](https://docs.aws.amazon.com/IAM/latest/UserGuide/what-is-access-analyzer.html)in the*AWS IAM User Guide*.- 
                    For API details, see [ListFindingsV2](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/accessanalyzer/list-findings-v2.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `list-findings`.

- **AWS CLI**
- 
            
                    **To retrieve a list of findings generated by the specified analyzer**The following `list-findings`example retrieves a list of findings generated by the specified analyzer in your AWS account. This example filters the results to include only IAM roles whose name contains`Cognito`.`aws accessanalyzer list-findings \ --analyzer-arn``arn:aws:access-analyzer:us-west-2:111122223333:analyzer/ConsoleAnalyzer-account`\ --filter '`{"resource": {"contains": ["Cognito"]}, "resourceType": {"eq": ["AWS::IAM::Role"]}}`'Output: `{ "findings": [ { "id": "597f3bc2-3adc-4c18-9879-5c4b23485e46", "principal": { "Federated": "cognito-identity.amazonaws.com" }, "action": [ "sts:AssumeRoleWithWebIdentity" ], "resource": "arn:aws:iam::111122223333:role/Cognito_testpoolUnauth_Role", "isPublic": false, "resourceType": "AWS::IAM::Role", "condition": { "cognito-identity.amazonaws.com:aud": "us-west-2:EXAMPLE0-0000-0000-0000-000000000000" }, "createdAt": "2021-02-26T21:17:24.710000+00:00", "analyzedAt": "2024-02-16T18:17:47.888000+00:00", "updatedAt": "2021-02-26T21:17:24.710000+00:00", "status": "ACTIVE", "resourceOwnerAccount": "111122223333" }, { "id": "ce0e221a-85b9-4d52-91ff-d7678075442f", "principal": { "Federated": "cognito-identity.amazonaws.com" }, "action": [ "sts:AssumeRoleWithWebIdentity" ], "resource": "arn:aws:iam::111122223333:role/Cognito_testpoolAuth_Role", "isPublic": false, "resourceType": "AWS::IAM::Role", "condition": { "cognito-identity.amazonaws.com:aud": "us-west-2:EXAMPLE0-0000-0000-0000-000000000000" }, "createdAt": "2021-02-26T21:17:50.905000+00:00", "analyzedAt": "2024-02-16T18:17:47.888000+00:00", "updatedAt": "2021-02-26T21:17:50.905000+00:00", "status": "ACTIVE", "resourceOwnerAccount": "111122223333" } ] }`For more information, see [Using AWS Identity and Access Management Access Analyzer](https://docs.aws.amazon.com/IAM/latest/UserGuide/what-is-access-analyzer.html)in the*AWS IAM User Guide*.- 
                    For API details, see [ListFindings](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/accessanalyzer/list-findings.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `list-policy-generations`.

- **AWS CLI**
- 
            
                    **To list all of the policy generations requested in the last seven days**The following `list-policy-generations`example lists all of the policy generations requested in the last seven days in your AWS account.`aws accessanalyzer list-policy-generations`Output: `{ "policyGenerations": [ { "completedOn": "2024-02-14T23:43:38+00:00", "jobId": "923a56b0-ebb8-4e80-8a3c-a11ccfbcd6f2", "principalArn": "arn:aws:iam::111122223333:role/Admin", "startedOn": "2024-02-14T23:43:02+00:00", "status": "CANCELED" }, { "completedOn": "2024-02-14T22:47:01+00:00", "jobId": "c557dc4a-0338-4489-95dd-739014860ff9", "principalArn": "arn:aws:iam::111122223333:role/Admin", "startedOn": "2024-02-14T22:44:41+00:00", "status": "SUCCEEDED" } ] }`For more information, see [IAM Access Analyzer policy generation](https://docs.aws.amazon.com/IAM/latest/UserGuide/access-analyzer-policy-generation.html)in the*AWS IAM User Guide*.- 
                    For API details, see [ListPolicyGenerations](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/accessanalyzer/list-policy-generations.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `list-tags-for-resource`.

- **AWS CLI**
- 
            
                    **To retrieve a list of tags applied to the specified resource**The following `list-tags-for-resource`example retrieves a list of tags applied to the specified resource in your AWS account.`aws accessanalyzer list-tags-for-resource \ --resource-arn``arn:aws:access-analyzer:us-west-2:111122223333:analyzer/ConsoleAnalyzer-account`Output: `{ "tags": { "Zone-of-trust": "Account", "Name": "ConsoleAnalyzer" } }`For more information, see [IAM Access Analyzer policy generation](https://docs.aws.amazon.com/IAM/latest/UserGuide/access-analyzer-policy-generation.html)in the*AWS IAM User Guide*.- 
                    For API details, see [ListTagsForResource](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/accessanalyzer/list-tags-for-resource.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `start-policy-generation`.

- **AWS CLI**
- 
            
                    **To start a policy generation request**The following `start-policy-generation`example starts a policy generation request in your AWS account.`aws accessanalyzer start-policy-generation \ --policy-generation-details '``{"principalArn":"arn:aws:iam::111122223333:role/Admin"}`' \ --cloud-trail-details`file://myfile.json`Contents of `myfile.json`:`{ "accessRole": "arn:aws:iam::111122223333:role/service-role/AccessAnalyzerMonitorServiceRole", "startTime": "2024-02-13T00:30:00Z", "trails": [ { "allRegions": true, "cloudTrailArn": "arn:aws:cloudtrail:us-west-2:111122223333:trail/my-trail" } ] }`Output: `{ "jobId": "c557dc4a-0338-4489-95dd-739014860ff9" }`For more information, see [IAM Access Analyzer policy generation](https://docs.aws.amazon.com/IAM/latest/UserGuide/access-analyzer-policy-generation.html)in the*AWS IAM User Guide*.- 
                    For API details, see [StartPolicyGeneration](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/accessanalyzer/start-policy-generation.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `start-resource-scan`.

- **AWS CLI**
- 
            
                    **To immediately start a scan of the policies applied to the specified resource**The following `start-resource-scan`example mmediately starts a scan of the policies applied to the specified resource in your AWS account.`aws accessanalyzer start-resource-scan \ --analyzer-arn``arn:aws:access-analyzer:us-west-2:111122223333:analyzer/ConsoleAnalyzer-account`\ --resource-arn`arn:aws:iam::111122223333:role/Cognito_testpoolAuth_Role`This command produces no output. For more information, see [IAM Access Analyzer policy generation](https://docs.aws.amazon.com/IAM/latest/UserGuide/access-analyzer-policy-generation.html)in the*AWS IAM User Guide*.- 
                    For API details, see [StartResourceScan](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/accessanalyzer/start-resource-scan.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `tag-resource`.

- **AWS CLI**
- 
            
                    **To add a tag to the specified resource**The following `tag-resource`example adds a tag to the specified resource in your AWS account.`aws accessanalyzer tag-resource \ --resource-arn``arn:aws:access-analyzer:us-west-2:111122223333:analyzer/ConsoleAnalyzer-account`\ --tags`Environment=dev,Purpose=testing`This command produces no output. For more information, see [Using AWS Identity and Access Management Access Analyzer](https://docs.aws.amazon.com/IAM/latest/UserGuide/what-is-access-analyzer.html)in the*AWS IAM User Guide*.- 
                    For API details, see [TagResource](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/accessanalyzer/tag-resource.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `untag-resource`.

- **AWS CLI**
- 
            
                    **To remove tags from the specified resources**The following `untag-resource`example removes tags from the specified resource in your AWS account.`aws accessanalyzer untag-resource \ --resource-arn``arn:aws:access-analyzer:us-west-2:111122223333:analyzer/ConsoleAnalyzer-account`\ --tag-keys`Environment``Purpose`This command produces no output. For more information, see [Using AWS Identity and Access Management Access Analyzer](https://docs.aws.amazon.com/IAM/latest/UserGuide/what-is-access-analyzer.html)in the*AWS IAM User Guide*.- 
                    For API details, see [UntagResource](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/accessanalyzer/untag-resource.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `update-archive-rule`.

- **AWS CLI**
- 
            
                    **To update the criteria and values for the specified archive rule**The following `update-archive-rule`example updates the criteria and values for the specified archive rule in your AWS account.`aws accessanalyzer update-archive-rule \ --analyzer-name``UnusedAccess-ConsoleAnalyzer-organization`\ --rule-name`MyArchiveRule`\ --filter '`{"resource": {"contains": ["Cognito"]}, "resourceType": {"eq": ["AWS::IAM::Role"]}}`'This command produces no output. For more information, see [Archive rules](https://docs.aws.amazon.com/IAM/latest/UserGuide/access-analyzer-archive-rules.html)in the*AWS IAM User Guide*.- 
                    For API details, see [UpdateArchiveRule](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/accessanalyzer/update-archive-rule.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `update-findings`.

- **AWS CLI**
- 
            
                    **To update the status for the specified findings**The following `update-findings`example updates the status for the specified findings in your AWS account.`aws accessanalyzer update-findings \ --analyzer-arn``arn:aws:access-analyzer:us-west-2:111122223333:analyzer/UnusedAccess-ConsoleAnalyzer-organization`\ --ids`4f319ac3-2e0c-4dc4-bf51-7013a086b6ae``780d586a-2cce-4f72-aff6-359d450e7500`\ --status`ARCHIVED`This command produces no output. For more information, see [Using AWS Identity and Access Management Access Analyzer](https://docs.aws.amazon.com/IAM/latest/UserGuide/what-is-access-analyzer.html)in the*AWS IAM User Guide*.- 
                    For API details, see [UpdateFindings](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/accessanalyzer/update-findings.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `validate-policy`.

- **AWS CLI**
- 
            
                    **To request the validation of a policy and returns a list of findings**The following `validate-policy`example requests the validation of a policy and returns a list of findings. The policy in the example is a role trust policy for an Amazon Cognito role used for web identity federation. The findings generated from the trust policy relate to an empty`Sid`element value and a mismatched policy principal due to the incorrect assume role action being used,`sts:AssumeRole`. The correct assume role action for use with Cognito is`sts:AssumeRoleWithWebIdentity`.`aws accessanalyzer validate-policy \ --policy-document``file://myfile.json`\ --policy-type`RESOURCE_POLICY`Contents of `myfile.json`:`{ "Version":"2012-10-17", "Statement": [ { "Sid": "", "Effect": "Allow", "Principal": { "Federated": "cognito-identity.amazonaws.com" }, "Action": [ "sts:AssumeRole", "sts:TagSession" ], "Condition": { "StringEquals": { "cognito-identity.amazonaws.com:aud": "us-west-2_EXAMPLE" } } } ] }`Output: `{ "findings": [ { "findingDetails": "Add a value to the empty string in the Sid element.", "findingType": "SUGGESTION", "issueCode": "EMPTY_SID_VALUE", "learnMoreLink": "https://docs.aws.amazon.com/IAM/latest/UserGuide/access-analyzer-reference-policy-checks.html#access-analyzer-reference-policy-checks-suggestion-empty-sid-value", "locations": [ { "path": [ { "value": "Statement" }, { "index": 0 }, { "value": "Sid" } ], "span": { "end": { "column": 21, "line": 5, "offset": 81 }, "start": { "column": 19, "line": 5, "offset": 79 } } } ] }, { "findingDetails": "The sts:AssumeRole action is invalid with the following principal(s): cognito-identity.amazonaws.com. Use a SAML provider principal with the sts:AssumeRoleWithSAML action or use an OIDC provider principal with the sts:AssumeRoleWithWebIdentity action. Ensure the provider is Federated if you use either of the two options.", "findingType": "ERROR", "issueCode": "MISMATCHED_ACTION_FOR_PRINCIPAL", "learnMoreLink": "https://docs.aws.amazon.com/IAM/latest/UserGuide/access-analyzer-reference-policy-checks.html#access-analyzer-reference-policy-checks-error-mismatched-action-for-principal", "locations": [ { "path": [ { "value": "Statement" }, { "index": 0 }, { "value": "Action" }, { "index": 0 } ], "span": { "end": { "column": 32, "line": 11, "offset": 274 }, "start": { "column": 16, "line": 11, "offset": 258 } } }, { "path": [ { "value": "Statement" }, { "index": 0 }, { "value": "Principal" }, { "value": "Federated" } ], "span": { "end": { "column": 61, "line": 8, "offset": 202 }, "start": { "column": 29, "line": 8, "offset": 170 } } } ] }, { "findingDetails": "The following actions: sts:TagSession are not supported by the condition key cognito-identity.amazonaws.com:aud. The condition will not be evaluated for these actions. We recommend that you move these actions to a different statement without this condition key.", "findingType": "ERROR", "issueCode": "UNSUPPORTED_ACTION_FOR_CONDITION_KEY", "learnMoreLink": "https://docs.aws.amazon.com/IAM/latest/UserGuide/access-analyzer-reference-policy-checks.html#access-analyzer-reference-policy-checks-error-unsupported-action-for-condition-key", "locations": [ { "path": [ { "value": "Statement" }, { "index": 0 }, { "value": "Action" }, { "index": 1 } ], "span": { "end": { "column": 32, "line": 12, "offset": 308 }, "start": { "column": 16, "line": 12, "offset": 292 } } }, { "path": [ { "value": "Statement" }, { "index": 0 }, { "value": "Condition" }, { "value": "StringEquals" }, { "value": "cognito-identity.amazonaws.com:aud" } ], "span": { "end": { "column": 79, "line": 16, "offset": 464 }, "start": { "column": 58, "line": 16, "offset": 443 } } } ] } ] }`For more information, see [Checks for validating policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access-analyzer-checks-validating-policies.html)in the*AWS IAM User Guide*.- 
                    For API details, see [ValidatePolicy](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/accessanalyzer/validate-policy.html)in*AWS CLI Command Reference*.
 
-