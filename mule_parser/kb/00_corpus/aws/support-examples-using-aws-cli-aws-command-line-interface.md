# Support examples using AWS CLI - AWS Command Line Interface

**Source:** [https://docs.aws.amazon.com/cli/latest/userguide/cli_support_code_examples.html](https://docs.aws.amazon.com/cli/latest/userguide/cli_support_code_examples.html)

---

The following code examples show you how to perform actions and implement common scenarios by using the AWS Command Line Interface with Support.

*Actions* are code excerpts from larger programs and must be run in context. While actions show you how to call individual service functions, you can see actions in context in their related scenarios.

Each example includes a link to the complete source code, where you can find instructions on how to set up and run the code in context.

###### Topics

## Actions

    The following code example shows how to use `add-attachments-to-set`.

- **AWS CLI**
- 
            
                    **To add an attachment to a set**The following `add-attachments-to-set`example adds an image to a set that you can then specify for a support case in your AWS account.`aws support add-attachments-to-set \ --attachment-set-id``"as-2f5a6faa2a4a1e600-mu-nk5xQlBr70-G1cUos5LZkd38KOAHZa9BMDVzNEXAMPLE"`\ --attachments`fileName=troubleshoot-screenshot.png,data=base64-encoded-string`Output: `{ "attachmentSetId": "as-2f5a6faa2a4a1e600-mu-nk5xQlBr70-G1cUos5LZkd38KOAHZa9BMDVzNEXAMPLE", "expiryTime": "2020-05-14T17:04:40.790+0000" }`For more information, see [Case management](https://docs.aws.amazon.com/awssupport/latest/user/case-management.html)in the*AWS Support User Guide*.- 
                    For API details, see [AddAttachmentsToSet](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/support/add-attachments-to-set.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `add-communication-to-case`.

- **AWS CLI**
- 
            
                    **To add communication to a case**The following `add-communication-to-case`example adds communications to a support case in your AWS account.`aws support add-communication-to-case \ --case-id``"case-12345678910-2013-c4c1d2bf33c5cf47"`\ --communication-body`"I'm attaching a set of images to this case."`\ --cc-email-addresses`"myemail@example.com"`\ --attachment-set-id`"as-2f5a6faa2a4a1e600-mu-nk5xQlBr70-G1cUos5LZkd38KOAHZa9BMDVzNEXAMPLE"`Output: `{ "result": true }`For more information, see [Case management](https://docs.aws.amazon.com/awssupport/latest/user/case-management.html)in the*AWS Support User Guide*.- 
                    For API details, see [AddCommunicationToCase](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/support/add-communication-to-case.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `create-case`.

- **AWS CLI**
- 
            
                    **To create a case**The following `create-case`example creates a support case for your AWS account.`aws support create-case \ --category-code``"using-aws"`\ --cc-email-addresses`"myemail@example.com"`\ --communication-body`"I want to learn more about an AWS service."`\ --issue-type`"technical"`\ --language`"en"`\ --service-code`"general-info"`\ --severity-code`"low"`\ --subject`"Question about my account"`Output: `{ "caseId": "case-12345678910-2013-c4c1d2bf33c5cf47" }`For more information, see [Case management](https://docs.aws.amazon.com/awssupport/latest/user/case-management.html)in the*AWS Support User Guide*.- 
                    For API details, see [CreateCase](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/support/create-case.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `describe-attachment`.

- **AWS CLI**
- 
            
                    **To describe an attachment**The following `describe-attachment`example returns information about the attachment with the specified ID.`aws support describe-attachment \ --attachment-id``"attachment-KBnjRNrePd9D6Jx0-Mm00xZuDEaL2JAj_0-gJv9qqDooTipsz3V1Nb19rCfkZneeQeDPgp8X1iVJyHH7UuhZDdNeqGoduZsPrAhyMakqlc60-iJjL5HqyYGiT1FG8EXAMPLE"`Output: `{ "attachment": { "fileName": "troubleshoot-screenshot.png", "data": "base64-blob" } }`For more information, see [Case management](https://docs.aws.amazon.com/awssupport/latest/user/case-management.html)in the*AWS Support User Guide*.- 
                    For API details, see [DescribeAttachment](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/support/describe-attachment.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `describe-cases`.

- **AWS CLI**
- 
            
                    **To describe a case**The following `describe-cases`example returns information about the specified support case in your AWS account.`aws support describe-cases \ --display-id``"1234567890"`\ --after-time`"2020-03-23T21:31:47.774Z"`\ --include-resolved-cases \ --language`"en"`\ --no-include-communications \ --max-item`1`Output: `{ "cases": [ { "status": "resolved", "ccEmailAddresses": [], "timeCreated": "2020-03-23T21:31:47.774Z", "caseId": "case-12345678910-2013-c4c1d2bf33c5cf47", "severityCode": "low", "language": "en", "categoryCode": "using-aws", "serviceCode": "general-info", "submittedBy": "myemail@example.com", "displayId": "1234567890", "subject": "Question about my account" } ] }`For more information, see [Case management](https://docs.aws.amazon.com/awssupport/latest/user/case-management.html)in the*AWS Support User Guide*.- 
                    For API details, see [DescribeCases](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/support/describe-cases.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `describe-communications`.

- **AWS CLI**
- 
            
                    **To describe the latest communication for a case**The following `describe-communications`example returns the latest communication for the specified support case in your AWS account.`aws support describe-communications \ --case-id``"case-12345678910-2013-c4c1d2bf33c5cf47"`\ --after-time`"2020-03-23T21:31:47.774Z"`\ --max-item`1`Output: `{ "communications": [ { "body": "I want to learn more about an AWS service.", "attachmentSet": [], "caseId": "case-12345678910-2013-c4c1d2bf33c5cf47", "timeCreated": "2020-05-12T23:12:35.000Z", "submittedBy": "Amazon Web Services" } ], "NextToken": "eyJuZXh0VG9rZW4iOiBudWxsLCAiYm90b190cnVuY2F0ZV9hbW91bnQEXAMPLE==" }`For more information, see [Case management](https://docs.aws.amazon.com/awssupport/latest/user/case-management.html)in the*AWS Support User Guide*.- 
                    For API details, see [DescribeCommunications](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/support/describe-communications.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `describe-services`.

- **AWS CLI**
- 
            
                    **To list AWS services and service categories**The following `describe-services`example lists the available service categories for requesting general information.`aws support describe-services \ --service-code-list``"general-info"`Output: `{ "services": [ { "code": "general-info", "name": "General Info and Getting Started", "categories": [ { "code": "charges", "name": "How Will I Be Charged?" }, { "code": "gdpr-queries", "name": "Data Privacy Query" }, { "code": "reserved-instances", "name": "Reserved Instances" }, { "code": "resource", "name": "Where is my Resource?" }, { "code": "using-aws", "name": "Using AWS & Services" }, { "code": "free-tier", "name": "Free Tier" }, { "code": "security-and-compliance", "name": "Security & Compliance" }, { "code": "account-structure", "name": "Account Structure" } ] } ] }`For more information, see [Case management](https://docs.aws.amazon.com/awssupport/latest/user/case-management.html)in the*AWS Support User Guide*.- 
                    For API details, see [DescribeServices](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/support/describe-services.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `describe-severity-levels`.

- **AWS CLI**
- 
            
                    **To list the available severity levels**The following `describe-severity-levels`example lists the available severity levels for a support case.`aws support describe-severity-levels`Output: `{ "severityLevels": [ { "code": "low", "name": "Low" }, { "code": "normal", "name": "Normal" }, { "code": "high", "name": "High" }, { "code": "urgent", "name": "Urgent" }, { "code": "critical", "name": "Critical" } ] }`For more information, see [Choosing a severity](https://docs.aws.amazon.com/awssupport/latest/user/case-management.html#choosing-severity)in the*AWS Support User Guide*.- 
                    For API details, see [DescribeSeverityLevels](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/support/describe-severity-levels.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `describe-trusted-advisor-check-refresh-statuses`.

- **AWS CLI**
- 
            
                    **To list the refresh statuses of AWS Trusted Advisor checks**The following `describe-trusted-advisor-check-refresh-statuses`example lists the refresh statuses for two Trusted Advisor checks: Amazon S3 Bucket Permissions and IAM Use.`aws support describe-trusted-advisor-check-refresh-statuses \ --check-id``"Pfx0RwqBli"``"zXCkfM1nI3"`Output: `{ "statuses": [ { "checkId": "Pfx0RwqBli", "status": "none", "millisUntilNextRefreshable": 0 }, { "checkId": "zXCkfM1nI3", "status": "none", "millisUntilNextRefreshable": 0 } ] }`For more information, see [AWS Trusted Advisor](https://docs.aws.amazon.com/awssupport/latest/user/trusted-advisor.html)in the*AWS Support User Guide*.- 
                    For API details, see [DescribeTrustedAdvisorCheckRefreshStatuses](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/support/describe-trusted-advisor-check-refresh-statuses.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `describe-trusted-advisor-check-result`.

- **AWS CLI**
- 
            
                    **To list the results of an AWS Trusted Advisor check**The following `describe-trusted-advisor-check-result`example lists the results of the IAM Use check.`aws support describe-trusted-advisor-check-result \ --check-id``"zXCkfM1nI3"`Output: `{ "result": { "checkId": "zXCkfM1nI3", "timestamp": "2020-05-13T21:38:05Z", "status": "ok", "resourcesSummary": { "resourcesProcessed": 1, "resourcesFlagged": 0, "resourcesIgnored": 0, "resourcesSuppressed": 0 }, "categorySpecificSummary": { "costOptimizing": { "estimatedMonthlySavings": 0.0, "estimatedPercentMonthlySavings": 0.0 } }, "flaggedResources": [ { "status": "ok", "resourceId": "47DEQpj8HBSa-_TImW-5JCeuQeRkm5NMpJWZEXAMPLE", "isSuppressed": false } ] } }`For more information, see [AWS Trusted Advisor](https://docs.aws.amazon.com/awssupport/latest/user/trusted-advisor.html)in the*AWS Support User Guide*.- 
                    For API details, see [DescribeTrustedAdvisorCheckResult](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/support/describe-trusted-advisor-check-result.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `describe-trusted-advisor-check-summaries`.

- **AWS CLI**
- 
            
                    **To list the summaries of AWS Trusted Advisor checks**The following `describe-trusted-advisor-check-summaries`example lists the results for two Trusted Advisor checks: Amazon S3 Bucket Permissions and IAM Use.`aws support describe-trusted-advisor-check-summaries \ --check-ids``"Pfx0RwqBli"``"zXCkfM1nI3"`Output: `{ "summaries": [ { "checkId": "Pfx0RwqBli", "timestamp": "2020-05-13T21:38:12Z", "status": "ok", "hasFlaggedResources": true, "resourcesSummary": { "resourcesProcessed": 44, "resourcesFlagged": 0, "resourcesIgnored": 0, "resourcesSuppressed": 0 }, "categorySpecificSummary": { "costOptimizing": { "estimatedMonthlySavings": 0.0, "estimatedPercentMonthlySavings": 0.0 } } }, { "checkId": "zXCkfM1nI3", "timestamp": "2020-05-13T21:38:05Z", "status": "ok", "hasFlaggedResources": true, "resourcesSummary": { "resourcesProcessed": 1, "resourcesFlagged": 0, "resourcesIgnored": 0, "resourcesSuppressed": 0 }, "categorySpecificSummary": { "costOptimizing": { "estimatedMonthlySavings": 0.0, "estimatedPercentMonthlySavings": 0.0 } } } ] }`For more information, see [AWS Trusted Advisor](https://docs.aws.amazon.com/awssupport/latest/user/trusted-advisor.html)in the*AWS Support User Guide*.- 
                    For API details, see [DescribeTrustedAdvisorCheckSummaries](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/support/describe-trusted-advisor-check-summaries.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `describe-trusted-advisor-checks`.

- **AWS CLI**
- 
            
                    **To list the available AWS Trusted Advisor checks**The following `describe-trusted-advisor-checks`example lists the available Trusted Advisor checks in your AWS account. This information includes the check name, ID, description, category, and metadata. Note that the output is shortened for readability.`aws support describe-trusted-advisor-checks \ --language``"en"`Output: `{ "checks": [ { "id": "zXCkfM1nI3", "name": "IAM Use", "description": "Checks for your use of AWS Identity and Access Management (IAM). You can use IAM to create users, groups, and roles in AWS, and you can use permissions to control access to AWS resources. \n<br>\n<br>\n<b>Alert Criteria</b><br>\nYellow: No IAM users have been created for this account.\n<br>\n<br>\n<b>Recommended Action</b><br>\nCreate one or more IAM users and groups in your account. You can then create additional users whose permissions are limited to perform specific tasks in your AWS environment. For more information, see <a href=\"https://docs.aws.amazon.com/IAM/latest/UserGuide/IAMGettingStarted.html\" target=\"_blank\">Getting Started</a>. \n<br><br>\n<b>Additional Resources</b><br>\n<a href=\"https://docs.aws.amazon.com/IAM/latest/UserGuide/IAM_Introduction.html\" target=\"_blank\">What Is IAM?</a>", "category": "security", "metadata": [] } ] }`For more information, see [AWS Trusted Advisor](https://docs.aws.amazon.com/awssupport/latest/user/trusted-advisor.html)in the*AWS Support User Guide*.- 
                    For API details, see [DescribeTrustedAdvisorChecks](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/support/describe-trusted-advisor-checks.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `refresh-trusted-advisor-check`.

- **AWS CLI**
- 
            
                    **To refresh an AWS Trusted Advisor check**The following `refresh-trusted-advisor-check`example refreshes the Amazon S3 Bucket Permissions Trusted Advisor check in your AWS account.`aws support refresh-trusted-advisor-check \ --check-id``"Pfx0RwqBli"`Output: `{ "status": { "checkId": "Pfx0RwqBli", "status": "enqueued", "millisUntilNextRefreshable": 3599992 } }`For more information, see [AWS Trusted Advisor](https://docs.aws.amazon.com/awssupport/latest/user/trusted-advisor.html)in the*AWS Support User Guide*.- 
                    For API details, see [RefreshTrustedAdvisorCheck](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/support/refresh-trusted-advisor-check.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `resolve-case`.

- **AWS CLI**
- 
            
                    **To resolve a support case**The following `resolve-case`example resolves a support case in your AWS account.`aws support resolve-case \ --case-id``"case-12345678910-2013-c4c1d2bf33c5cf47"`Output: `{ "finalCaseStatus": "resolved", "initialCaseStatus": "work-in-progress" }`For more information, see [Case management](https://docs.aws.amazon.com/awssupport/latest/user/case-management.html)in the*AWS Support User Guide*.- 
                    For API details, see [ResolveCase](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/support/resolve-case.html)in*AWS CLI Command Reference*.
 
-