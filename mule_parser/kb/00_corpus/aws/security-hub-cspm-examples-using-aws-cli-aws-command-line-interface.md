# Security Hub CSPM examples using AWS CLI - AWS Command Line Interface

**Source:** [https://docs.aws.amazon.com/cli/latest/userguide/cli_securityhub_code_examples.html](https://docs.aws.amazon.com/cli/latest/userguide/cli_securityhub_code_examples.html)

---

The following code examples show you how to perform actions and implement common scenarios by using the AWS Command Line Interface with Security Hub CSPM.

*Actions* are code excerpts from larger programs and must be run in context. While actions show you how to call individual service functions, you can see actions in context in their related scenarios.

Each example includes a link to the complete source code, where you can find instructions on how to set up and run the code in context.

###### Topics

## Actions

    The following code example shows how to use `accept-administrator-invitation`.

- **AWS CLI**
- 
            
                    **To accept an invitation from an administrator account**The following `accept-administrator-invitation`example accepts the specified invitation from the specified administrator account.`aws securityhub accept-administrator-invitation \ --administrator-id``123456789012`\ --invitation-id`7ab938c5d52d7904ad09f9e7c20cc4eb`This command produces no output. For more information, see [Managing administrator and member accounts](https://docs.aws.amazon.com/securityhub/latest/userguide/securityhub-accounts.html)in the*AWS Security Hub User Guide*.- 
                    For API details, see [AcceptAdministratorInvitation](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/securityhub/accept-administrator-invitation.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `accept-invitation`.

- **AWS CLI**
- 
            
                    **To accept an invitation from an administrator account**The following `accept-invitation`example accepts the specified invitation from the specified administrator account.`aws securityhub accept-invitation \ --master-id``123456789012`\ --invitation-id`7ab938c5d52d7904ad09f9e7c20cc4eb`This command produces no output. For more information, see [Managing administrator and member accounts](https://docs.aws.amazon.com/securityhub/latest/userguide/securityhub-accounts.html)in the*AWS Security Hub User Guide*.- 
                    For API details, see [AcceptInvitation](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/securityhub/accept-invitation.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `batch-delete-automation-rules`.

- **AWS CLI**
- 
            
                    **To delete automation rules**The following `batch-delete-automation-rules`example deletes the specified automation rule. You can delete one or more rules with a single command. Only the Security Hub administrator account can run this command.`aws securityhub batch-delete-automation-rules \ --automation-rules-arns '``["arn:aws:securityhub:us-east-1:123456789012:automation-rule/a1b2c3d4-5678-90ab-cdef-EXAMPLE11111"]`'Output: `{ "ProcessedAutomationRules": [ "arn:aws:securityhub:us-east-1:123456789012:automation-rule/a1b2c3d4-5678-90ab-cdef-EXAMPLE11111" ], "UnprocessedAutomationRules": [] }`For more information, see [Deleting automation rules](https://docs.aws.amazon.com/securityhub/latest/userguide/automation-rules.html#delete-automation-rules)in the*AWS Security Hub User Guide*.- 
                    For API details, see [BatchDeleteAutomationRules](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/securityhub/batch-delete-automation-rules.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `batch-disable-standards`.

- **AWS CLI**
- 
            
                    **To disable a standard**The following `batch-disable-standards`example disables the standard associated with the specified subscription ARN.`aws securityhub batch-disable-standards \ --standards-subscription-arns``"arn:aws:securityhub:us-west-1:123456789012:subscription/pci-dss/v/3.2.1"`Output: `{ "StandardsSubscriptions": [ { "StandardsArn": "arn:aws:securityhub:eu-central-1::standards/pci-dss/v/3.2.1", "StandardsInput": { }, "StandardsStatus": "DELETING", "StandardsSubscriptionArn": "arn:aws:securityhub:us-west-1:123456789012:subscription/pci-dss/v/3.2.1" } ] }`For more information, see [Disabling or enabling a security standard](https://docs.aws.amazon.com/securityhub/latest/userguide/securityhub-standards-enable-disable.html)in the*AWS Security Hub User Guide*.- 
                    For API details, see [BatchDisableStandards](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/securityhub/batch-disable-standards.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `batch-enable-standards`.

- **AWS CLI**
- 
            
                    **To enable a standard**The following `batch-enable-standards`example enables the PCI DSS standard for the requesting account.`aws securityhub batch-enable-standards \ --standards-subscription-requests '``{"StandardsArn":"arn:aws:securityhub:us-west-1::standards/pci-dss/v/3.2.1"}`'Output: `{ "StandardsSubscriptions": [ { "StandardsArn": "arn:aws:securityhub:us-west-1::standards/pci-dss/v/3.2.1", "StandardsInput": { }, "StandardsStatus": "PENDING", "StandardsSubscriptionArn": "arn:aws:securityhub:us-west-1:123456789012:subscription/pci-dss/v/3.2.1" } ] }`For more information, see [Disabling or enabling a security standard](https://docs.aws.amazon.com/securityhub/latest/userguide/securityhub-standards-enable-disable.html)in the*AWS Security Hub User Guide*.- 
                    For API details, see [BatchEnableStandards](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/securityhub/batch-enable-standards.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `batch-get-automation-rules`.

- **AWS CLI**
- 
            
                    **To get details for automation rules**The following `batch-get-automation-rules`example gets details for the specified automation rule. You can get details for one or more automation rules with a single command.`aws securityhub batch-get-automation-rules \ --automation-rules-arns '``["arn:aws:securityhub:us-east-1:123456789012:automation-rule/a1b2c3d4-5678-90ab-cdef-EXAMPLE11111"]`'Output: `{ "Rules": [ { "RuleArn": "arn:aws:securityhub:us-east-1:123456789012:automation-rule/a1b2c3d4-5678-90ab-cdef-EXAMPLE11111", "RuleStatus": "ENABLED", "RuleOrder": 1, "RuleName": "Suppress informational findings", "Description": "Suppress GuardDuty findings with Informational severity", "IsTerminal": false, "Criteria": { "ProductName": [ { "Value": "GuardDuty", "Comparison": "EQUALS" } ], "SeverityLabel": [ { "Value": "INFORMATIONAL", "Comparison": "EQUALS" } ], "WorkflowStatus": [ { "Value": "NEW", "Comparison": "EQUALS" } ], "RecordState": [ { "Value": "ACTIVE", "Comparison": "EQUALS" } ] }, "Actions": [ { "Type": "FINDING_FIELDS_UPDATE", "FindingFieldsUpdate": { "Note": { "Text": "Automatically suppress GuardDuty findings with Informational severity", "UpdatedBy": "sechub-automation" }, "Workflow": { "Status": "SUPPRESSED" } } } ], "CreatedAt": "2023-05-31T17:56:14.837000+00:00", "UpdatedAt": "2023-05-31T17:59:38.466000+00:00", "CreatedBy": "arn:aws:iam::123456789012:role/Admin" } ], "UnprocessedAutomationRules": [] }`For more information, see [Viewing automation rules](https://docs.aws.amazon.com/securityhub/latest/userguide/automation-rules.html#view-automation-rules)in the*AWS Security Hub User Guide*.- 
                    For API details, see [BatchGetAutomationRules](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/securityhub/batch-get-automation-rules.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `batch-get-configuration-policy-associations`.

- **AWS CLI**
- 
            
                    **To get configuration association details for a batch of targets**The following `batch-get-configuration-policy-associations`example retrieves association details for the specified targets. You can provide account IDs, organizational unit IDs, or the root ID for the target.`aws securityhub batch-get-configuration-policy-associations \ --configuration-policy-association-identifiers '``{"OrganizationalUnitId": "ou-6hi7-8j91kl2m"}`'Output: `{ "ConfigurationPolicyId": "a1b2c3d4-5678-90ab-cdef-EXAMPLE33333", "TargetId": "ou-6hi7-8j91kl2m", "TargetType": "ORGANIZATIONAL_UNIT", "AssociationType": "APPLIED", "UpdatedAt": "2023-09-26T21:13:01.816000+00:00", "AssociationStatus": "SUCCESS", "AssociationStatusMessage": "Association applied successfully on this target." }`For more information, see [Viewing Security Hub configuration policies](https://docs.aws.amazon.com/securityhub/latest/userguide/view-policy.html)in the*AWS Security Hub User Guide*.- 
                    For API details, see [BatchGetConfigurationPolicyAssociations](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/securityhub/batch-get-configuration-policy-associations.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `batch-get-security-controls`.

- **AWS CLI**
- 
            
                    **To get security control details**The following `batch-get-security-controls`example gets details for the security controls ACM.1 and IAM.1 in the current AWS account and AWS Region.`aws securityhub batch-get-security-controls \ --security-control-ids '``["ACM.1", "IAM.1"]`'Output: `{ "SecurityControls": [ { "SecurityControlId": "ACM.1", "SecurityControlArn": "arn:aws:securityhub:us-east-2:123456789012:security-control/ACM.1", "Title": "Imported and ACM-issued certificates should be renewed after a specified time period", "Description": "This control checks whether an AWS Certificate Manager (ACM) certificate is renewed within the specified time period. It checks both imported certificates and certificates provided by ACM. The control fails if the certificate isn't renewed within the specified time period. Unless you provide a custom parameter value for the renewal period, Security Hub uses a default value of 30 days.", "RemediationUrl": "https://docs.aws.amazon.com/console/securityhub/ACM.1/remediation", "SeverityRating": "MEDIUM", "SecurityControlStatus": "ENABLED" "UpdateStatus": "READY", "Parameters": { "daysToExpiration": { "ValueType": CUSTOM, "Value": { "Integer": 15 } } }, "LastUpdateReason": "Updated control parameter" }, { "SecurityControlId": "IAM.1", "SecurityControlArn": "arn:aws:securityhub:us-east-2:123456789012:security-control/IAM.1", "Title": "IAM policies should not allow full \"*\" administrative privileges", "Description": "This AWS control checks whether the default version of AWS Identity and Access Management (IAM) policies (also known as customer managed policies) do not have administrator access with a statement that has \"Effect\": \"Allow\" with \"Action\": \"*\" over \"Resource\": \"*\". It only checks for the Customer Managed Policies that you created, but not inline and AWS Managed Policies.", "RemediationUrl": "https://docs.aws.amazon.com/console/securityhub/IAM.1/remediation", "SeverityRating": "HIGH", "SecurityControlStatus": "ENABLED" "UpdateStatus": "READY", "Parameters": {} } ] }`For more information, see [Viewing details for a control](https://docs.aws.amazon.com/securityhub/latest/userguide/securityhub-standards-control-details.html)in the*AWS Security Hub User Guide*.- 
                    For API details, see [BatchGetSecurityControls](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/securityhub/batch-get-security-controls.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `batch-get-standards-control-associations`.

- **AWS CLI**
- 
            
                    **To get the enablement status of a control**The following `batch-get-standards-control-associations`example identifies whether the specified controls are enabled in the specified standards.`aws securityhub batch-get-standards-control-associations \ --standards-control-association-ids '``[{"SecurityControlId": "Config.1","StandardsArn": "arn:aws:securityhub:us-east-1:123456789012:ruleset/cis-aws-foundations-benchmark/v/1.2.0"}, {"SecurityControlId": "IAM.6","StandardsArn": "arn:aws:securityhub:us-east-1:123456789012:standards/aws-foundational-security-best-practices/v/1.0.0"}]`'Output: `{ "StandardsControlAssociationDetails": [ { "StandardsArn": "arn:aws:securityhub:::ruleset/cis-aws-foundations-benchmark/v/1.2.0", "SecurityControlId": "Config.1", "SecurityControlArn": "arn:aws:securityhub:us-east-1:068873283051:security-control/Config.1", "AssociationStatus": "ENABLED", "RelatedRequirements": [ "CIS AWS Foundations 2.5" ], "UpdatedAt": "2022-10-27T16:07:12.960000+00:00", "StandardsControlTitle": "Ensure AWS Config is enabled", "StandardsControlDescription": "AWS Config is a web service that performs configuration management of supported AWS resources within your account and delivers log files to you. The recorded information includes the configuration item (AWS resource), relationships between configuration items (AWS resources), and any configuration changes between resources. It is recommended to enable AWS Config in all regions.", "StandardsControlArns": [ "arn:aws:securityhub:us-east-1:068873283051:control/cis-aws-foundations-benchmark/v/1.2.0/2.5" ] }, { "StandardsArn": "arn:aws:securityhub:us-east-1::standards/aws-foundational-security-best-practices/v/1.0.0", "SecurityControlId": "IAM.6", "SecurityControlArn": "arn:aws:securityhub:us-east-1:068873283051:security-control/IAM.6", "AssociationStatus": "DISABLED", "RelatedRequirements": [], "UpdatedAt": "2022-11-22T21:30:35.080000+00:00", "UpdatedReason": "test", "StandardsControlTitle": "Hardware MFA should be enabled for the root user", "StandardsControlDescription": "This AWS control checks whether your AWS account is enabled to use a hardware multi-factor authentication (MFA) device to sign in with root user credentials.", "StandardsControlArns": [ "arn:aws:securityhub:us-east-1:068873283051:control/aws-foundational-security-best-practices/v/1.0.0/IAM.6" ] } ] }`For more information, see [Enabling and disabling controls in specific standards](https://docs.aws.amazon.com/securityhub/latest/userguide/controls-configure.html)in the*AWS Security Hub User Guide*.- 
                    For API details, see [BatchGetStandardsControlAssociations](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/securityhub/batch-get-standards-control-associations.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `batch-import-findings`.

- **AWS CLI**
- 
            
                    **To update a finding**The following `batch-import-findings`example updates a finding.`aws securityhub batch-import-findings \ --findings '``[{ "AwsAccountId": "123456789012", "CreatedAt": "2020-05-27T17:05:54.832Z", "Description": "Vulnerability in a CloudTrail trail", "FindingProviderFields": { "Severity": { "Label": "LOW", "Original": "10" }, "Types": [ "Software and Configuration Checks/Vulnerabilities/CVE" ] }, "GeneratorId": "TestGeneratorId", "Id": "Id1", "ProductArn": "arn:aws:securityhub:us-west-1:123456789012:product/123456789012/default", "Resources": [ { "Id": "arn:aws:cloudtrail:us-west-1:123456789012:trail/TrailName", "Partition": "aws", "Region": "us-west-1", "Type": "AwsCloudTrailTrail" } ], "SchemaVersion": "2018-10-08", "Title": "CloudTrail trail vulnerability", "UpdatedAt": "2020-06-02T16:05:54.832Z" }]`'Output: `{ "FailedCount": 0, "SuccessCount": 1, "FailedFindings": [] }`For more information, see [Using BatchImportFindings to create and update findings](https://docs.aws.amazon.com/securityhub/latest/userguide/finding-update-batchimportfindings.html)in the*AWS Security Hub User Guide*.- 
                    For API details, see [BatchImportFindings](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/securityhub/batch-import-findings.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `batch-update-automation-rules`.

- **AWS CLI**
- 
            
                    **To update automation rules**The following `batch-update-automation-rules`example updates the specified automation rule. You can update one or more rules with a single command. Only the Security Hub administrator account can run this command.`aws securityhub batch-update-automation-rules \ --update-automation-rules-request-items '``[ \ { \ "Actions": [{ \ "Type": "FINDING_FIELDS_UPDATE", \ "FindingFieldsUpdate": { \ "Note": { \ "Text": "Known issue that is a risk", \ "UpdatedBy": "sechub-automation" \ }, \ "Workflow": { \ "Status": "NEW" \ } \ } \ }], \ "Criteria": { \ "SeverityLabel": [{ \ "Value": "LOW", \ "Comparison": "EQUALS" \ }] \ }, \ "RuleArn": "arn:aws:securityhub:us-east-1:123456789012:automation-rule/a1b2c3d4-5678-90ab-cdef-EXAMPLE11111", \ "RuleOrder": 1, \ "RuleStatus": "DISABLED" \ } \ ]`'Output: `{ "ProcessedAutomationRules": [ "arn:aws:securityhub:us-east-1:123456789012:automation-rule/a1b2c3d4-5678-90ab-cdef-EXAMPLE11111" ], "UnprocessedAutomationRules": [] }`For more information, see [Editing automation rules](https://docs.aws.amazon.com/securityhub/latest/userguide/automation-rules.html#edit-automation-rules)in the*AWS Security Hub User Guide*.- 
                    For API details, see [BatchUpdateAutomationRules](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/securityhub/batch-update-automation-rules.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `batch-update-findings`.

- **AWS CLI**
- 
            
                    **Example 1: To update a finding**The following `batch-update-findings`example updates two findings to add a note, change the severity label, and resolve it.`aws securityhub batch-update-findings \ --finding-identifiers '``[{"Id": "arn:aws:securityhub:us-west-1:123456789012:subscription/pci-dss/v/3.2.1/PCI.Lambda.2/finding/a1b2c3d4-5678-90ab-cdef-EXAMPLE11111", "ProductArn": "arn:aws:securityhub:us-west-1::product/aws/securityhub"}, {"Id": "arn:aws:securityhub:us-west-1:123456789012:subscription/pci-dss/v/3.2.1/PCI.Lambda.2/finding/a1b2c3d4-5678-90ab-cdef-EXAMPLE22222", "ProductArn": "arn:aws:securityhub:us-west-1::product/aws/securityhub"}]`' \ --note '`{"Text": "Known issue that is not a risk.", "UpdatedBy": "user1"}`' \ --severity '`{"Label": "LOW"}`' \ --workflow '`{"Status": "RESOLVED"}`'Output: `{ "ProcessedFindings": [ { "Id": "arn:aws:securityhub:us-west-1:123456789012:subscription/pci-dss/v/3.2.1/PCI.Lambda.2/finding/a1b2c3d4-5678-90ab-cdef-EXAMPLE11111", "ProductArn": "arn:aws:securityhub:us-west-1::product/aws/securityhub" }, { "Id": "arn:aws:securityhub:us-west-1:123456789012:subscription/pci-dss/v/3.2.1/PCI.Lambda.2/finding/a1b2c3d4-5678-90ab-cdef-EXAMPLE22222", "ProductArn": "arn:aws:securityhub:us-west-1::product/aws/securityhub" } ], "UnprocessedFindings": [] }`For more information, see [Using BatchUpdateFindings to update a finding](https://docs.aws.amazon.com/securityhub/latest/userguide/finding-update-batchupdatefindings.html)in the*AWS Security Hub User Guide*.**Example 2: To update a finding using shorthand syntax**The following `batch-update-findings`example updates two findings to add a note, change the severity label, and resolve it using shorthand syntax.`aws securityhub batch-update-findings \ --finding-identifiers Id="arn:aws:securityhub:us-west-1:123456789012:subscription/pci-dss/v/3.2.1/PCI.Lambda.2/finding/a1b2c3d4-5678-90ab-cdef-EXAMPLE11111",ProductArn="arn:aws:securityhub:us-west-1::product/aws/securityhub" Id="arn:aws:securityhub:us-west-1:123456789012:subscription/pci-dss/v/3.2.1/PCI.Lambda.2/finding/a1b2c3d4-5678-90ab-cdef-EXAMPLE22222",ProductArn="arn:aws:securityhub:us-west-1::product/aws/securityhub" \ --note Text="Known issue that is not a risk.",UpdatedBy="user1" \ --severity Label="LOW" \ --workflow Status="RESOLVED"`Output: `{ "ProcessedFindings": [ { "Id": "arn:aws:securityhub:us-west-1:123456789012:subscription/pci-dss/v/3.2.1/PCI.Lambda.2/finding/a1b2c3d4-5678-90ab-cdef-EXAMPLE11111", "ProductArn": "arn:aws:securityhub:us-west-1::product/aws/securityhub" }, { "Id": "arn:aws:securityhub:us-west-1:123456789012:subscription/pci-dss/v/3.2.1/PCI.Lambda.2/finding/a1b2c3d4-5678-90ab-cdef-EXAMPLE22222", "ProductArn": "arn:aws:securityhub:us-west-1::product/aws/securityhub" } ], "UnprocessedFindings": [] }`For more information, see [Using BatchUpdateFindings to update a finding](https://docs.aws.amazon.com/securityhub/latest/userguide/finding-update-batchupdatefindings.html)in the*AWS Security Hub User Guide*.- 
                    For API details, see [BatchUpdateFindings](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/securityhub/batch-update-findings.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `batch-update-standards-control-associations`.

- **AWS CLI**
- 
            
                    **To update the enablement status of a control in enabled standards**The following `batch-update-standards-control-associations`example disables CloudTrail.1 in the specified standards.`aws securityhub batch-update-standards-control-associations \ --standards-control-association-updates '``[{"SecurityControlId": "CloudTrail.1", "StandardsArn": "arn:aws:securityhub:::ruleset/cis-aws-foundations-benchmark/v/1.2.0", "AssociationStatus": "DISABLED", "UpdatedReason": "Not applicable to environment"}, {"SecurityControlId": "CloudTrail.1", "StandardsArn": "arn:aws:securityhub:::standards/cis-aws-foundations-benchmark/v/1.4.0", "AssociationStatus": "DISABLED", "UpdatedReason": "Not applicable to environment"}]`'This command produces no output when successful. For more information, see [Enabling and disabling controls in specific standards](https://docs.aws.amazon.com/securityhub/latest/userguide/controls-configure.html)and[Enabling and disabling controls in all standards](https://docs.aws.amazon.com/securityhub/latest/userguide/securityhub-standards-enable-disable-controls.html)in the*AWS Security Hub User Guide*.- 
                    For API details, see [BatchUpdateStandardsControlAssociations](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/securityhub/batch-update-standards-control-associations.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `create-action-target`.

- **AWS CLI**
- 
            
                    **To create a custom action**The following `create-action-target`example creates a custom action. It provides the name, description, and identifier for the action.`aws securityhub create-action-target \ --name``"Send to remediation"`\ --description`"Action to send the finding for remediation tracking"`\ --id`"Remediation"`Output: `{ "ActionTargetArn": "arn:aws:securityhub:us-west-1:123456789012:action/custom/Remediation" }`For more information, see [Creating a custom action and associating it with a CloudWatch Events rule](https://docs.aws.amazon.com/securityhub/latest/userguide/securityhub-cloudwatch-events.html#securityhub-cwe-configure)in the*AWS Security Hub User Guide*.- 
                    For API details, see [CreateActionTarget](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/securityhub/create-action-target.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `create-automation-rule`.

- **AWS CLI**
- 
            
                    **To create an automation rule**The following `create-automation-rule`example creates an automation rule in the current AWS account and AWS Region. Security Hub filters your findings based on the specified criteria and applies the actions to matching findings. Only the Security Hub administrator account can run this command.`aws securityhub create-automation-rule \ --actions '``[{ \ "Type": "FINDING_FIELDS_UPDATE", \ "FindingFieldsUpdate": { \ "Severity": { \ "Label": "HIGH" \ }, \ "Note": { \ "Text": "Known issue that is a risk. Updated by automation rules", \ "UpdatedBy": "sechub-automation" \ } \ } \ }]`' \ --criteria '`{ \ "SeverityLabel": [{ \ "Value": "INFORMATIONAL", \ "Comparison": "EQUALS" \ }] \ }`' \ --description`"A sample rule"`\ --no-is-terminal \ --rule-name`"sample rule"`\ --rule-order`1`\ --rule-status`"ENABLED"`Output: `{ "RuleArn": "arn:aws:securityhub:us-east-1:123456789012:automation-rule/a1b2c3d4-5678-90ab-cdef-EXAMPLE11111" }`For more information, see [Creating automation rules](https://docs.aws.amazon.com/securityhub/latest/userguide/automation-rules.html#create-automation-rules)in the*AWS Security Hub User Guide*.- 
                    For API details, see [CreateAutomationRule](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/securityhub/create-automation-rule.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `create-configuration-policy`.

- **AWS CLI**
- 
            
                    **To create a configuration policy**The following `create-configuration-policy`example creates a configuration policy with the specified settings.`aws securityhub create-configuration-policy \ --name``"SampleConfigurationPolicy"`\ --description`"SampleDescription"`\ --configuration-policy '`{"SecurityHub": {"ServiceEnabled": true, "EnabledStandardIdentifiers": ["arn:aws:securityhub:eu-central-1::standards/aws-foundational-security-best-practices/v/1.0.0","arn:aws:securityhub:::ruleset/cis-aws-foundations-benchmark/v/1.2.0"],"SecurityControlsConfiguration":{"DisabledSecurityControlIdentifiers": ["CloudTrail.2"], "SecurityControlCustomParameters": [{"SecurityControlId": "ACM.1", "Parameters": {"daysToExpiration": {"ValueType": "CUSTOM", "Value": {"Integer": 15}}}}]}}}`' \ --tags '`{"Environment": "Prod"}`'Output: `{ "Arn": "arn:aws:securityhub:eu-central-1:123456789012:configuration-policy/a1b2c3d4-5678-90ab-cdef-EXAMPLE11111", "Id": "a1b2c3d4-5678-90ab-cdef-EXAMPLE11111", "Name": "SampleConfigurationPolicy", "Description": "SampleDescription", "UpdatedAt": "2023-11-28T20:28:04.494000+00:00", "CreatedAt": "2023-11-28T20:28:04.494000+00:00", "ConfigurationPolicy": { "SecurityHub": { "ServiceEnabled": true, "EnabledStandardIdentifiers": [ "arn:aws:securityhub:eu-central-1::standards/aws-foundational-security-best-practices/v/1.0.0", "arn:aws:securityhub:::ruleset/cis-aws-foundations-benchmark/v/1.2.0" ], "SecurityControlsConfiguration": { "DisabledSecurityControlIdentifiers": [ "CloudTrail.2" ], "SecurityControlCustomParameters": [ { "SecurityControlId": "ACM.1", "Parameters": { "daysToExpiration": { "ValueType": "CUSTOM", "Value": { "Integer": 15 } } } } ] } } } }`For more information, see [Creating and associating Security Hub configuration policies](https://docs.aws.amazon.com/securityhub/latest/userguide/create-associate-policy.html)in the*AWS Security Hub User Guide*.- 
                    For API details, see [CreateConfigurationPolicy](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/securityhub/create-configuration-policy.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `create-finding-aggregator`.

- **AWS CLI**
- 
            
                    **To enable finding aggregation**The following `create-finding-aggregator`example configures finding aggregation. It is run from US East (Virginia), which designates US East (Virginia) as the aggregation Region. It indicates to only link specified Regions, and to not automatically link new Regions. It selects US West (N. California) and US West (Oregon) as the linked Regions.`aws securityhub create-finding-aggregator \ --region``us-east-1`\ --region-linking-mode`SPECIFIED_REGIONS`\ --regions`us-west-1,us-west-2`Output: `{ "FindingAggregatorArn": "arn:aws:securityhub:us-east-1:222222222222:finding-aggregator/123e4567-e89b-12d3-a456-426652340000", "FindingAggregationRegion": "us-east-1", "RegionLinkingMode": "SPECIFIED_REGIONS", "Regions": "us-west-1,us-west-2" }`For more information, see [Enabling finding aggregation](https://docs.aws.amazon.com/securityhub/latest/userguide/finding-aggregation-enable.html)in the*AWS Security Hub User Guide*.- 
                    For API details, see [CreateFindingAggregator](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/securityhub/create-finding-aggregator.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `create-insight`.

- **AWS CLI**
- 
            
                    **To create a custom insight**The following `create-insight`example creates a custom insight named Critical role findings that returns critical findings that are related to AWS roles.`aws securityhub create-insight \ --filters '``{"ResourceType": [{ "Comparison": "EQUALS", "Value": "AwsIamRole"}], "SeverityLabel": [{"Comparison": "EQUALS", "Value": "CRITICAL"}]}`' \ --group-by-attribute`"ResourceId"`\ --name`"Critical role findings"`Output: `{ "InsightArn": "arn:aws:securityhub:us-west-1:123456789012:insight/123456789012/custom/a1b2c3d4-5678-90ab-cdef-EXAMPLE11111" }`For more information, see [Managing custom insights](https://docs.aws.amazon.com/securityhub/latest/userguide/securityhub-custom-insights.html)in the*AWS Security Hub User Guide*.- 
                    For API details, see [CreateInsight](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/securityhub/create-insight.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `create-members`.

- **AWS CLI**
- 
            
                    **To add accounts as member accounts**The following `create-members`example adds two accounts as member accounts to the requesting administrator account.`aws securityhub create-members \ --account-details '``[{"AccountId": "123456789111"}, {"AccountId": "123456789222"}]`'Output: `{ "UnprocessedAccounts": [] }`For more information, see [Managing administrator and member accounts](https://docs.aws.amazon.com/securityhub/latest/userguide/securityhub-accounts.html)in the*AWS Security Hub User Guide*.- 
                    For API details, see [CreateMembers](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/securityhub/create-members.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `decline-invitations`.

- **AWS CLI**
- 
            
                    **To decline an invitation to be a member account**The following `decline-invitations`example declines an invitation to be a member account of the specified administrator account. The member account is the requesting account.`aws securityhub decline-invitations \ --account-ids``"123456789012"`Output: `{ "UnprocessedAccounts": [] }`For more information, see [Managing administrator and member accounts](https://docs.aws.amazon.com/securityhub/latest/userguide/securityhub-accounts.html)in the*AWS Security Hub User Guide*.- 
                    For API details, see [DeclineInvitations](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/securityhub/decline-invitations.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `delete-action-target`.

- **AWS CLI**
- 
            
                    **To delete a custom action**The following `delete-action-target`example deletes the custom action identified by the specified ARN.`aws securityhub delete-action-target \ --action-target-arn``"arn:aws:securityhub:us-west-1:123456789012:action/custom/Remediation"`Output: `{ "ActionTargetArn": "arn:aws:securityhub:us-west-1:123456789012:action/custom/Remediation" }`For more information, see [Creating a custom action and associating it with a CloudWatch Events rule](https://docs.aws.amazon.com/securityhub/latest/userguide/securityhub-cloudwatch-events.html#securityhub-cwe-configure)in the*AWS Security Hub User Guide*.- 
                    For API details, see [DeleteActionTarget](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/securityhub/delete-action-target.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `delete-configuration-policy`.

- **AWS CLI**
- 
            
                    **To delete a configuration policy**The following `delete-configuration-policy`example deletes the specified configuration policy.`aws securityhub delete-configuration-policy \ --identifier``"arn:aws:securityhub:eu-central-1:123456789012:configuration-policy/a1b2c3d4-5678-90ab-cdef-EXAMPLE11111"`This command produces no output. For more information, see [Deleting and disassociating Security Hub configuration policies](https://docs.aws.amazon.com/securityhub/latest/userguide/delete-disassociate-policy.html)in the*AWS Security Hub User Guide*.- 
                    For API details, see [DeleteConfigurationPolicy](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/securityhub/delete-configuration-policy.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `delete-finding-aggregator`.

- **AWS CLI**
- 
            
                    **To stop finding aggregation**The following `delete-finding-aggregator`example stops finding aggregation. It is run from US East (Virginia), which is the aggregation Region.`aws securityhub delete-finding-aggregator \ --region``us-east-1`\ --finding-aggregator-arn`arn:aws:securityhub:us-east-1:222222222222:finding-aggregator/123e4567-e89b-12d3-a456-426652340000`This command produces no output. For more information, see [Stopping finding aggregation](https://docs.aws.amazon.com/securityhub/latest/userguide/finding-aggregation-stop.html)in the*AWS Security Hub User Guide*.- 
                    For API details, see [DeleteFindingAggregator](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/securityhub/delete-finding-aggregator.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `delete-insight`.

- **AWS CLI**
- 
            
                    **To delete a custom insight**The following `delete-insight`example deletes the custom insight with the specified ARN.`aws securityhub delete-insight \ --insight-arn``"arn:aws:securityhub:us-west-1:123456789012:insight/123456789012/custom/a1b2c3d4-5678-90ab-cdef-EXAMPLE11111"`Output: `{ "InsightArn": "arn:aws:securityhub:eu-central-1:123456789012:insight/123456789012/custom/a1b2c3d4-5678-90ab-cdef-EXAMPLE11111" }`For more information, see [Managing custom insights](https://docs.aws.amazon.com/securityhub/latest/userguide/securityhub-custom-insights.html)in the*AWS Security Hub User Guide*.- 
                    For API details, see [DeleteInsight](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/securityhub/delete-insight.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `delete-invitations`.

- **AWS CLI**
- 
            
                    **To delete an invitation to be a member account**The following `delete-invitations`example deletes an invitation to be a member account for the specified administrator account. The member account is the requesting account.`aws securityhub delete-invitations \ --account-ids``"123456789012"`Output: `{ "UnprocessedAccounts": [] }`For more information, see [Managing administrator and member accounts](https://docs.aws.amazon.com/securityhub/latest/userguide/securityhub-accounts.html)in the*AWS Security Hub User Guide*.- 
                    For API details, see [DeleteInvitations](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/securityhub/delete-invitations.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `delete-members`.

- **AWS CLI**
- 
            
                    **To delete member accounts**The following `delete-members`example deletes the specified member accounts from the requesting administrator account.`aws securityhub delete-members \ --account-ids``"123456789111"``"123456789222"`Output: `{ "UnprocessedAccounts": [] }`For more information, see [Managing administrator and member accounts](https://docs.aws.amazon.com/securityhub/latest/userguide/securityhub-accounts.html)in the*AWS Security Hub User Guide*.- 
                    For API details, see [DeleteMembers](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/securityhub/delete-members.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `describe-action-targets`.

- **AWS CLI**
- 
            
                    **To retrieve details about custom actions**The following `describe-action-targets`example retrieves information about the custom action identified by the specified ARN.`aws securityhub describe-action-targets \ --action-target-arns``"arn:aws:securityhub:us-west-1:123456789012:action/custom/Remediation"`Output: `{ "ActionTargets": [ { "ActionTargetArn": "arn:aws:securityhub:us-west-1:123456789012:action/custom/Remediation", "Description": "Action to send the finding for remediation tracking", "Name": "Send to remediation" } ] }`For more information, see [Creating a custom action and associating it with a CloudWatch Events rule](https://docs.aws.amazon.com/securityhub/latest/userguide/securityhub-cloudwatch-events.html#securityhub-cwe-configure)in the*AWS Security Hub User Guide*.- 
                    For API details, see [DescribeActionTargets](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/securityhub/describe-action-targets.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `describe-hub`.

- **AWS CLI**
- 
            
                    **To get information about a hub resource**The following `describe-hub`example returns the subscription date and other configuration settings for the specified hub resource. The hub resource is identified by its ARN.`aws securityhub describe-hub \ --hub-arn``"arn:aws:securityhub:us-west-1:123456789012:hub/default"`Output: `{ "HubArn": "arn:aws:securityhub:us-west-1:123456789012:hub/default", "SubscribedAt": "2019-11-19T23:15:10.046Z", "AutoEnableControls": true, "ControlFindingGenerator": "SECURITY_CONTROL" }`For more information, see [AWS::SecurityHub::Hub](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-securityhub-hub.html)in the*AWS CloudFormation User Guide*.- 
                    For API details, see [DescribeHub](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/securityhub/describe-hub.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `describe-organization-configuration`.

- **AWS CLI**
- 
            
                    **To view how Security Hub is configured for an organization**The following `describe-organization-configuration`example returns information about the way an organization is configured in Security Hub. In this example, the organization uses central configuration. Only the Security Hub administrator account can run this command.`aws securityhub describe-organization-configuration`Output: `{ "AutoEnable": false, "MemberAccountLimitReached": false, "AutoEnableStandards": "NONE", "OrganizationConfiguration": { "ConfigurationType": "LOCAL", "Status": "ENABLED", "StatusMessage": "Central configuration has been enabled successfully" } }`For more information, see [Managing accounts with AWS Organizations](https://docs.aws.amazon.com/securityhub/latest/userguide/securityhub-accounts-orgs.html)in the*AWS Security Hub User Guide*.- 
                    For API details, see [DescribeOrganizationConfiguration](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/securityhub/describe-organization-configuration.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `describe-products`.

- **AWS CLI**
- 
            
                    **To return information about available product integrations**The following `describe-products`example returns the available product integrations one at a time.`aws securityhub describe-products \ --max-results``1`Output: `{ "NextToken": "U2FsdGVkX18vvPlOqb7RDrWRWVFBJI46MOIAb+nZmRJmR15NoRi2gm13sdQEn3O/pq/78dGs+bKpgA+7HMPHO0qX33/zoRI+uIG/F9yLNhcOrOWzFUdy36JcXLQji3Rpnn/cD1SVkGA98qI3zPOSDg==", "Products": [ { "ProductArn": "arn:aws:securityhub:us-west-1:123456789333:product/crowdstrike/crowdstrike-falcon", "ProductName": "CrowdStrike Falcon", "CompanyName": "CrowdStrike", "Description": "CrowdStrike Falcon's single lightweight sensor unifies next-gen antivirus, endpoint detection and response, and 24/7 managed hunting, via the cloud.", "Categories": [ "Endpoint Detection and Response (EDR)", "AV Scanning and Sandboxing", "Threat Intelligence Feeds and Reports", "Endpoint Forensics", "Network Forensics" ], "IntegrationTypes": [ "SEND_FINDINGS_TO_SECURITY_HUB" ], "MarketplaceUrl": "https://aws.amazon.com/marketplace/seller-profile?id=a1b2c3d4-5678-90ab-cdef-EXAMPLE11111", "ActivationUrl": "https://falcon.crowdstrike.com/support/documentation", "ProductSubscriptionResourcePolicy": "{\"Version\":\"2012-10-17\",\"Statement\":[{\"Effect\":\"Allow\",\"Principal\":{\"AWS\":\"123456789333\"},\"Action\":[\"securityhub:BatchImportFindings\"],\"Resource\":\"arn:aws:securityhub:us-west-1:123456789012:product-subscription/crowdstrike/crowdstrike-falcon\",\"Condition\":{\"StringEquals\":{\"securityhub:TargetAccount\":\"123456789012\"}}},{\"Effect\":\"Allow\",\"Principal\":{\"AWS\":\"123456789012\"},\"Action\":[\"securityhub:BatchImportFindings\"],\"Resource\":\"arn:aws:securityhub:us-west-1:123456789333:product/crowdstrike/crowdstrike-falcon\",\"Condition\":{\"StringEquals\":{\"securityhub:TargetAccount\":\"123456789012\"}}}]}" } ] }`For more information, see [Managing product integrations](https://docs.aws.amazon.com/securityhub/latest/userguide/securityhub-integrations-managing.html)in the*AWS Security Hub User Guide*.- 
                    For API details, see [DescribeProducts](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/securityhub/describe-products.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `describe-standards-controls`.

- **AWS CLI**
- 
            
                    **To request the list of controls in an enabled standard**The following `describe-standards-controls`example requests the list of controls in the requester account's subscription to the PCI DSS standard. The request returns two controls at a time.`aws securityhub describe-standards-controls \ --standards-subscription-arn``"arn:aws:securityhub:us-west-1:123456789012:subscription/pci-dss/v/3.2.1"`\ --max-results`2`Output: `{ "Controls": [ { "StandardsControlArn": "arn:aws:securityhub:us-west-1:123456789012:control/pci-dss/v/3.2.1/PCI.AutoScaling.1", "ControlStatus": "ENABLED", "ControlStatusUpdatedAt": "2020-05-15T18:49:04.473000+00:00", "ControlId": "PCI.AutoScaling.1", "Title": "Auto scaling groups associated with a load balancer should use health checks", "Description": "This AWS control checks whether your Auto Scaling groups that are associated with a load balancer are using Elastic Load Balancing health checks.", "RemediationUrl": "https://docs.aws.amazon.com/console/securityhub/PCI.AutoScaling.1/remediation", "SeverityRating": "LOW", "RelatedRequirements": [ "PCI DSS 2.2" ] }, { "StandardsControlArn": "arn:aws:securityhub:us-west-1:123456789012:control/pci-dss/v/3.2.1/PCI.CW.1", "ControlStatus": "ENABLED", "ControlStatusUpdatedAt": "2020-05-15T18:49:04.498000+00:00", "ControlId": "PCI.CW.1", "Title": "A log metric filter and alarm should exist for usage of the \"root\" user", "Description": "This control checks for the CloudWatch metric filters using the following pattern { $.userIdentity.type = \"Root\" && $.userIdentity.invokedBy NOT EXISTS && $.eventType != \"AwsServiceEvent\" } It checks that the log group name is configured for use with active multi-region CloudTrail, that there is at least one Event Selector for a Trail with IncludeManagementEvents set to true and ReadWriteType set to All, and that there is at least one active subscriber to an SNS topic associated with the alarm.", "RemediationUrl": "https://docs.aws.amazon.com/console/securityhub/PCI.CW.1/remediation", "SeverityRating": "MEDIUM", "RelatedRequirements": [ "PCI DSS 7.2.1" ] } ], "NextToken": "U2FsdGVkX1+eNkPoZHVl11ip5HUYQPWSWZGmftcmJiHL8JoKEsCDuaKayiPDyLK+LiTkShveoOdvfxXCkOBaGhohIXhsIedN+LSjQV/l7kfCfJcq4PziNC1N9xe9aq2pjlLVZnznTfSImrodT5bRNHe4fELCQq/z+5ka+5Lzmc11axcwTd5lKgQyQqmUVoeriHZhyIiBgWKf7oNYdBVG8OEortVWvSkoUTt+B2ThcnC7l43kI0UNxlkZ6sc64AsW" }`For more information, see [Viewing details for controls](https://docs.aws.amazon.com/securityhub/latest/userguide/securityhub-standards-view-controls.html)in the*AWS Security Hub User Guide*.- 
                    For API details, see [DescribeStandardsControls](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/securityhub/describe-standards-controls.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `describe-standards`.

- **AWS CLI**
- 
            
                    **To return a list of available standards**The following `describe-standards`example returns the list of available standards.`aws securityhub describe-standards`Output: `{ "Standards": [ { "StandardsArn": "arn:aws:securityhub:us-west-1::standards/aws-foundational-security-best-practices/v/1.0.0", "Name": "AWS Foundational Security Best Practices v1.0.0", "Description": "The AWS Foundational Security Best Practices standard is a set of automated security checks that detect when AWS accounts and deployed resources do not align to security best practices. The standard is defined by AWS security experts. This curated set of controls helps improve your security posture in AWS, and cover AWS's most popular and foundational services.", "EnabledByDefault": true }, { "StandardsArn": "arn:aws:securityhub:::ruleset/cis-aws-foundations-benchmark/v/1.2.0", "Name": "CIS AWS Foundations Benchmark v1.2.0", "Description": "The Center for Internet Security (CIS) AWS Foundations Benchmark v1.2.0 is a set of security configuration best practices for AWS. This Security Hub standard automatically checks for your compliance readiness against a subset of CIS requirements.", "EnabledByDefault": true }, { "StandardsArn": "arn:aws:securityhub:us-west-1::standards/pci-dss/v/3.2.1", "Name": "PCI DSS v3.2.1", "Description": "The Payment Card Industry Data Security Standard (PCI DSS) v3.2.1 is an information security standard for entities that store, process, and/or transmit cardholder data. This Security Hub standard automatically checks for your compliance readiness against a subset of PCI DSS requirements.", "EnabledByDefault": false } ] }`For more information, see [Security standards in AWS Security Hub](https://docs.aws.amazon.com/securityhub/latest/userguide/securityhub-standards.html)in the*AWS Security Hub User Guide*.- 
                    For API details, see [DescribeStandards](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/securityhub/describe-standards.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `disable-import-findings-for-product`.

- **AWS CLI**
- 
            
                    **To stop receiving findings from a product integration**The following `disable-import-findings-for-product`example disables the flow of findings for the specified subscription to a product integration.`aws securityhub disable-import-findings-for-product \ --product-subscription-arn``"arn:aws:securityhub:us-west-1:123456789012:product-subscription/crowdstrike/crowdstrike-falcon"`This command produces no output. For more information, see [Managing product integrations](https://docs.aws.amazon.com/securityhub/latest/userguide/securityhub-integrations-managing.html)in the*AWS Security Hub User Guide*.- 
                    For API details, see [DisableImportFindingsForProduct](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/securityhub/disable-import-findings-for-product.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `disable-organization-admin-account`.

- **AWS CLI**
- 
            
                    **To remove a Security Hub administrator account**The following `disable-organization-admin-account`example revokes the specified account's assignment as a Security Hub administrator account for AWS Organizations.`aws securityhub disable-organization-admin-account \ --admin-account-id``777788889999`This command produces no output. For more information, see [Designating a Security Hub administrator account](https://docs.aws.amazon.com/securityhub/latest/userguide/designate-orgs-admin-account.html)in the*AWS Security Hub User Guide*.- 
                    For API details, see [DisableOrganizationAdminAccount](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/securityhub/disable-organization-admin-account.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `disable-security-hub`.

- **AWS CLI**
- 
            
                    **To disable AWS Security Hub**The following `disable-security-hub`example disables AWS Security Hub for the requesting account.`aws securityhub disable-security-hub`This command produces no output. For more information, see [Disabling AWS Security Hub](https://docs.aws.amazon.com/securityhub/latest/userguide/securityhub-disable.html)in the*AWS Security Hub User Guide*.- 
                    For API details, see [DisableSecurityHub](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/securityhub/disable-security-hub.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `disassociate-from-administrator-account`.

- **AWS CLI**
- 
            
                    **To disassociate from an administrator account**The following `disassociate-from-administrator-account`example disassociates the requesting account from its current administrator account.`aws securityhub disassociate-from-administrator-account`This command produces no output. For more information, see [Managing administrator and member accounts](https://docs.aws.amazon.com/securityhub/latest/userguide/securityhub-accounts.html)in the*AWS Security Hub User Guide*.- 
                    For API details, see [DisassociateFromAdministratorAccount](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/securityhub/disassociate-from-administrator-account.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `disassociate-from-master-account`.

- **AWS CLI**
- 
            
                    **To disassociate from an administrator account**The following `disassociate-from-master-account`example disassociates the requesting account from its current administrator account.`aws securityhub disassociate-from-master-account`This command produces no output. For more information, see [Managing administrator and member accounts](https://docs.aws.amazon.com/securityhub/latest/userguide/securityhub-accounts.html)in the*AWS Security Hub User Guide*.- 
                    For API details, see [DisassociateFromMasterAccount](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/securityhub/disassociate-from-master-account.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `disassociate-members`.

- **AWS CLI**
- 
            
                    **To disassociate member accounts**The following `disassociate-members`example disassociates the specified member accounts from the requesting administrator account.`aws securityhub disassociate-members \ --account-ids``"123456789111"``"123456789222"`This command produces no output. For more information, see [Managing administrator and member accounts](https://docs.aws.amazon.com/securityhub/latest/userguide/securityhub-accounts.html)in the*AWS Security Hub User Guide*.- 
                    For API details, see [DisassociateMembers](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/securityhub/disassociate-members.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `enable-import-findings-for-product`.

- **AWS CLI**
- 
            
                    **To start receiving findings from a product integration**The following `enable-import-findings-for-product`example enables the flow of findings from the specified product integration.`aws securityhub enable-import-findings-for-product \ --product-arn``"arn:aws:securityhub:us-east-1:123456789333:product/crowdstrike/crowdstrike-falcon"`Output: `{ "ProductSubscriptionArn": "arn:aws:securityhub:us-east-1:123456789012:product-subscription/crowdstrike/crowdstrike-falcon" }`For more information, see [Managing product integrations](https://docs.aws.amazon.com/securityhub/latest/userguide/securityhub-integrations-managing.html)in the*AWS Security Hub User Guide*.- 
                    For API details, see [EnableImportFindingsForProduct](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/securityhub/enable-import-findings-for-product.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `enable-organization-admin-account`.

- **AWS CLI**
- 
            
                    **To designate an organization account as a Security Hub administrator account**The following `enable-organization-admin-account`example designates the specified account as a Security Hub administrator account.`aws securityhub enable-organization-admin-account \ --admin-account-id``777788889999`This command produces no output. For more information, see [Designating a Security Hub administrator account](https://docs.aws.amazon.com/securityhub/latest/userguide/designate-orgs-admin-account.html)in the*AWS Security Hub User Guide*.- 
                    For API details, see [EnableOrganizationAdminAccount](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/securityhub/enable-organization-admin-account.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `enable-security-hub`.

- **AWS CLI**
- 
            
                    **To enable AWS Security Hub**The following `enable-security-hub`example enables AWS Security Hub for the requesting account. It configures Security Hub to enable the default standards. For the hub resource, it assigns the value`Security`to the tag`Department`.`aws securityhub enable-security-hub \ --enable-default-standards \ --tags '``{"Department": "Security"}`'This command produces no output. For more information, see [Enabling Security Hub](https://docs.aws.amazon.com/securityhub/latest/userguide/securityhub-settingup.html#securityhub-enable)in the*AWS Security Hub User Guide*.- 
                    For API details, see [EnableSecurityHub](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/securityhub/enable-security-hub.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `get-administrator-account`.

- **AWS CLI**
- 
            
                    **To retrieve information about an administrator account**The following `get-administrator-account`example retrieves information about the administrator account for the requesting account.`aws securityhub get-administrator-account`Output: `{ "Master": { "AccountId": "123456789012", "InvitationId": "7ab938c5d52d7904ad09f9e7c20cc4eb", "InvitedAt": 2020-06-01T20:21:18.042000+00:00, "MemberStatus": "ASSOCIATED" } }`For more information, see [Managing administrator and member accounts](https://docs.aws.amazon.com/securityhub/latest/userguide/securityhub-accounts.html)in the*AWS Security Hub User Guide*.- 
                    For API details, see [GetAdministratorAccount](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/securityhub/get-administrator-account.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `get-configuration-policy-association`.

- **AWS CLI**
- 
            
                    **To get configuration association details for a target**The following `get-configuration-policy-association`example retrieves association details for the specified target. You can provide an account ID, organizational unit ID, or the root ID for the target.`aws securityhub get-configuration-policy-association \ --target '``{"OrganizationalUnitId": "ou-6hi7-8j91kl2m"}`'Output: `{ "ConfigurationPolicyId": "a1b2c3d4-5678-90ab-cdef-EXAMPLE33333", "TargetId": "ou-6hi7-8j91kl2m", "TargetType": "ORGANIZATIONAL_UNIT", "AssociationType": "APPLIED", "UpdatedAt": "2023-09-26T21:13:01.816000+00:00", "AssociationStatus": "SUCCESS", "AssociationStatusMessage": "Association applied successfully on this target." }`For more information, see [Viewing Security Hub configuration policies](https://docs.aws.amazon.com/securityhub/latest/userguide/view-policy.html)in the*AWS Security Hub User Guide*.- 
                    For API details, see [GetConfigurationPolicyAssociation](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/securityhub/get-configuration-policy-association.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `get-configuration-policy`.

- **AWS CLI**
- 
            
                    **To view configuration policy details**The following `get-configuration-policy`example retrieves details about the specified configuration policy.`aws securityhub get-configuration-policy \ --identifier``"arn:aws:securityhub:eu-central-1:123456789012:configuration-policy/a1b2c3d4-5678-90ab-cdef-EXAMPLE11111"`Output: `{ "Arn": "arn:aws:securityhub:eu-central-1:123456789012:configuration-policy/a1b2c3d4-5678-90ab-cdef-EXAMPLE11111", "Id": "ce5ed1e7-9639-4e2f-9313-fa87fcef944b", "Name": "SampleConfigurationPolicy", "Description": "SampleDescription", "UpdatedAt": "2023-11-28T20:28:04.494000+00:00", "CreatedAt": "2023-11-28T20:28:04.494000+00:00", "ConfigurationPolicy": { "SecurityHub": { "ServiceEnabled": true, "EnabledStandardIdentifiers": [ "arn:aws:securityhub:eu-central-1::standards/aws-foundational-security-best-practices/v/1.0.0", "arn:aws:securityhub:::ruleset/cis-aws-foundations-benchmark/v/1.2.0" ], "SecurityControlsConfiguration": { "DisabledSecurityControlIdentifiers": [ "CloudTrail.2" ], "SecurityControlCustomParameters": [ { "SecurityControlId": "ACM.1", "Parameters": { "daysToExpiration": { "ValueType": "CUSTOM", "Value": { "Integer": 15 } } } } ] } } } }`For more information, see [Viewing Security Hub configuration policies](https://docs.aws.amazon.com/securityhub/latest/userguide/view-policy.html)in the*AWS Security Hub User Guide*.- 
                    For API details, see [GetConfigurationPolicy](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/securityhub/get-configuration-policy.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `get-enabled-standards`.

- **AWS CLI**
- 
            
                    **To retrieve information about an enabled standard**The following `get-enabled-standards`example retrieves information about the PCI DSS standard.`aws securityhub get-enabled-standards \ --standards-subscription-arn``"arn:aws:securityhub:us-west-1:123456789012:subscription/pci-dss/v/3.2.1"`Output: `{ "StandardsSubscriptions": [ { "StandardsArn": "arn:aws:securityhub:us-west-1::standards/pci-dss/v/3.2.1", "StandardsInput": { }, "StandardsStatus": "READY", "StandardsSubscriptionArn": "arn:aws:securityhub:us-west-1:123456789012:subscription/pci-dss/v/3.2.1" } ] }`For more information, see [Security standards in AWS Security Hub](https://docs.aws.amazon.com/securityhub/latest/userguide/securityhub-standards.html)in the*AWS Security Hub User Guide*.- 
                    For API details, see [GetEnabledStandards](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/securityhub/get-enabled-standards.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `get-finding-aggregator`.

- **AWS CLI**
- 
            
                    **To retrieve the current finding aggregation configuration**The following `get-finding-aggregator`example retrieves the current finding aggregation configuration.`aws securityhub get-finding-aggregator \ --finding-aggregator-arn``arn:aws:securityhub:us-east-1:222222222222:finding-aggregator/123e4567-e89b-12d3-a456-426652340000`Output: `{ "FindingAggregatorArn": "arn:aws:securityhub:us-east-1:222222222222:finding-aggregator/123e4567-e89b-12d3-a456-426652340000", "FindingAggregationRegion": "us-east-1", "RegionLinkingMode": "SPECIFIED_REGIONS", "Regions": "us-west-1,us-west-2" }`For more information, see [Viewing the current finding aggregation configuration](https://docs.aws.amazon.com/securityhub/latest/userguide/finding-aggregation-view-config.html)in the*AWS Security Hub User Guide*.- 
                    For API details, see [GetFindingAggregator](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/securityhub/get-finding-aggregator.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `get-finding-history`.

- **AWS CLI**
- 
            
                    **To get finding history**The following `get-finding-history`example gets up to the last 90 days of history for the specified finding. In this example, the results are limited to two records of finding history.`aws securityhub get-finding-history \ --finding-identifier Id="arn:aws:securityhub:us-east-1:123456789012:security-control/S3.17/finding/a1b2c3d4-5678-90ab-cdef-EXAMPLE11111",ProductArn="arn:aws:securityhub:us-east-1::product/aws/securityhub"`Output: `{ "Records": [ { "FindingIdentifier": { "Id": "arn:aws:securityhub:us-east-1:123456789012:security-control/S3.17/finding/a1b2c3d4-5678-90ab-cdef-EXAMPLE11111", "ProductArn": "arn:aws:securityhub:us-east-1::product/aws/securityhub" }, "UpdateTime": "2023-06-02T03:15:25.685000+00:00", "FindingCreated": false, "UpdateSource": { "Type": "BATCH_IMPORT_FINDINGS", "Identity": "arn:aws:securityhub:us-east-1::product/aws/securityhub" }, "Updates": [ { "UpdatedField": "Compliance.RelatedRequirements", "OldValue": "[\"NIST.800-53.r5 SC-12(2)\",\"NIST.800-53.r5 SC-12(3)\",\"NIST.800-53.r5 SC-12(6)\",\"NIST.800-53.r5 CM-3(6)\",\"NIST.800-53.r5 SC-13\",\"NIST.800-53.r5 SC-28\",\"NIST.800-53.r5 SC-28(1)\",\"NIST.800-53.r5 SC-7(10)\"]", "NewValue": "[\"NIST.800-53.r5 SC-12(2)\",\"NIST.800-53.r5 CM-3(6)\",\"NIST.800-53.r5 SC-13\",\"NIST.800-53.r5 SC-28\",\"NIST.800-53.r5 SC-28(1)\",\"NIST.800-53.r5 SC-7(10)\",\"NIST.800-53.r5 CA-9(1)\",\"NIST.800-53.r5 SI-7(6)\",\"NIST.800-53.r5 AU-9\"]" }, { "UpdatedField": "LastObservedAt", "OldValue": "2023-06-01T09:15:38.587Z", "NewValue": "2023-06-02T03:15:22.946Z" }, { "UpdatedField": "UpdatedAt", "OldValue": "2023-06-01T09:15:31.049Z", "NewValue": "2023-06-02T03:15:14.861Z" }, { "UpdatedField": "ProcessedAt", "OldValue": "2023-06-01T09:15:41.058Z", "NewValue": "2023-06-02T03:15:25.685Z" } ] }, { "FindingIdentifier": { "Id": "arn:aws:securityhub:us-east-1:123456789012:security-control/S3.17/finding/a1b2c3d4-5678-90ab-cdef-EXAMPLE11111", "ProductArn": "arn:aws:securityhub:us-east-1::product/aws/securityhub" }, "UpdateTime": "2023-05-23T02:06:51.518000+00:00", "FindingCreated": "true", "UpdateSource": { "Type": "BATCH_IMPORT_FINDINGS", "Identity": "arn:aws:securityhub:us-east-1::product/aws/securityhub" }, "Updates": [] } ] }`For more information, see [Finding history](https://docs.aws.amazon.com/securityhub/latest/userguide/finding-view-details.html#finding-history)in the*AWS Security Hub User Guide*.- 
                    For API details, see [GetFindingHistory](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/securityhub/get-finding-history.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `get-findings`.

- **AWS CLI**
- 
            
                    **Example 1: To return findings generated for a specific standard**The following `get-findings`example returns findings for the PCI DSS standard.`aws securityhub get-findings \ --filters '``{"GeneratorId":[{"Value": "pci-dss","Comparison":"PREFIX"}]}`' \ --max-items`1`Output: `{ "Findings": [ { "SchemaVersion": "2018-10-08", "Id": "arn:aws:securityhub:eu-central-1:123456789012:subscription/pci-dss/v/3.2.1/PCI.Lambda.2/finding/a1b2c3d4-5678-90ab-cdef-EXAMPLE11111", "ProductArn": "arn:aws:securityhub:us-west-1::product/aws/securityhub", "GeneratorId": "pci-dss/v/3.2.1/PCI.Lambda.2", "AwsAccountId": "123456789012", "Types": [ "Software and Configuration Checks/Industry and Regulatory Standards/PCI-DSS" ], "FindingProviderFields": { "Severity": { "Original": 0, "Label": "INFORMATIONAL" }, "Types": [ "Software and Configuration Checks/Industry and Regulatory Standards/PCI-DSS" ] }, "FirstObservedAt": "2020-06-02T14:02:49.159Z", "LastObservedAt": "2020-06-02T14:02:52.397Z", "CreatedAt": "2020-06-02T14:02:49.159Z", "UpdatedAt": "2020-06-02T14:02:52.397Z", "Severity": { "Original": 0, "Label": "INFORMATIONAL", "Normalized": 0 }, "Title": "PCI.Lambda.2 Lambda functions should be in a VPC", "Description": "This AWS control checks whether a Lambda function is in a VPC.", "Remediation": { "Recommendation": { "Text": "For directions on how to fix this issue, please consult the AWS Security Hub PCI DSS documentation.", "Url": "https://docs.aws.amazon.com/console/securityhub/PCI.Lambda.2/remediation" } }, "ProductFields": { "StandardsArn": "arn:aws:securityhub:::standards/pci-dss/v/3.2.1", "StandardsSubscriptionArn": "arn:aws:securityhub:us-west-1:123456789012:subscription/pci-dss/v/3.2.1", "ControlId": "PCI.Lambda.2", "RecommendationUrl": "https://docs.aws.amazon.com/console/securityhub/PCI.Lambda.2/remediation", "RelatedAWSResources:0/name": "securityhub-lambda-inside-vpc-0e904a3b", "RelatedAWSResources:0/type": "AWS::Config::ConfigRule", "StandardsControlArn": "arn:aws:securityhub:us-west-1:123456789012:control/pci-dss/v/3.2.1/PCI.Lambda.2", "aws/securityhub/SeverityLabel": "INFORMATIONAL", "aws/securityhub/ProductName": "Security Hub", "aws/securityhub/CompanyName": "AWS", "aws/securityhub/FindingId": "arn:aws:securityhub:eu-central-1::product/aws/securityhub/arn:aws:securityhub:eu-central-1:123456789012:subscription/pci-dss/v/3.2.1/PCI.Lambda.2/finding/a1b2c3d4-5678-90ab-cdef-EXAMPLE11111" }, "Resources": [ { "Type": "AwsAccount", "Id": "AWS::::Account:123456789012", "Partition": "aws", "Region": "us-west-1" } ], "Compliance": { "Status": "PASSED", "RelatedRequirements": [ "PCI DSS 1.2.1", "PCI DSS 1.3.1", "PCI DSS 1.3.2", "PCI DSS 1.3.4" ] }, "WorkflowState": "NEW", "Workflow": { "Status": "NEW" }, "RecordState": "ARCHIVED" } ], "NextToken": "eyJOZXh0VG9rZW4iOiBudWxsLCAiYm90b190cnVuY2F0ZV9hbW91bnQiOiAxfQ==" }`**Example 2: To return critical-severity findings that have a workflow status of NOTIFIED**The following `get-findings`example returns findings that have a severity label value of CRITICAL and a workflow status of NOTIFIED. The results are sorted in descending order by the value of Confidence.`aws securityhub get-findings \ --filters '``{"SeverityLabel":[{"Value": "CRITICAL","Comparison":"EQUALS"}],"WorkflowStatus": [{"Value":"NOTIFIED","Comparison":"EQUALS"}]}`' \ --sort-criteria '`{ "Field": "Confidence", "SortOrder": "desc"}`' \ --max-items`1`Output: `{ "Findings": [ { "SchemaVersion": "2018-10-08", "Id": "arn:aws:securityhub:us-west-1: 123456789012:subscription/cis-aws-foundations-benchmark/v/1.2.0/1.13/finding/a1b2c3d4-5678-90ab-cdef-EXAMPLE11111", "ProductArn": "arn:aws:securityhub:us-west-2::product/aws/securityhub", "GeneratorId": "arn:aws:securityhub:::ruleset/cis-aws-foundations-benchmark/v/1.2.0/rule/1.13", "AwsAccountId": "123456789012", "Types": [ "Software and Configuration Checks/Industry and Regulatory Standards/CIS AWS Foundations Benchmark" ], "FindingProviderFields" { "Severity": { "Original": 90, "Label": "CRITICAL" }, "Types": [ "Software and Configuration Checks/Industry and Regulatory Standards/CIS AWS Foundations Benchmark" ] }, "FirstObservedAt": "2020-05-21T20:16:34.752Z", "LastObservedAt": "2020-06-09T08:16:37.171Z", "CreatedAt": "2020-05-21T20:16:34.752Z", "UpdatedAt": "2020-06-09T08:16:36.430Z", "Severity": { "Original": 90, "Label": "CRITICAL", "Normalized": 90 }, "Title": "1.13 Ensure MFA is enabled for the \"root\" account", "Description": "The root account is the most privileged user in an AWS account. MFA adds an extra layer of protection on top of a user name and password. With MFA enabled, when a user signs in to an AWS website, they will be prompted for their user name and password as well as for an authentication code from their AWS MFA device.", "Remediation": { "Recommendation": { "Text": "For directions on how to fix this issue, please consult the AWS Security Hub CIS documentation.", "Url": "https://docs.aws.amazon.com/console/securityhub/standards-cis-1.13/remediation" } }, "ProductFields": { "StandardsGuideArn": "arn:aws:securityhub:::ruleset/cis-aws-foundations-benchmark/v/1.2.0", "StandardsGuideSubscriptionArn": "arn:aws:securityhub:us-west-1:123456789012:subscription/cis-aws-foundations-benchmark/v/1.2.0", "RuleId": "1.13", "RecommendationUrl": "https://docs.aws.amazon.com/console/securityhub/standards-cis-1.13/remediation", "RelatedAWSResources:0/name": "securityhub-root-account-mfa-enabled-5pftha", "RelatedAWSResources:0/type": "AWS::Config::ConfigRule", "StandardsControlArn": "arn:aws:securityhub:us-west-1:123456789012:control/cis-aws-foundations-benchmark/v/1.2.0/1.13", "aws/securityhub/SeverityLabel": "CRITICAL", "aws/securityhub/ProductName": "Security Hub", "aws/securityhub/CompanyName": "AWS", "aws/securityhub/FindingId": "arn:aws:securityhub:us-west-1::product/aws/securityhub/arn:aws:securityhub:us-west-1:123456789012:subscription/cis-aws-foundations-benchmark/v/1.2.0/1.13/finding/a1b2c3d4-5678-90ab-cdef-EXAMPLE11111" }, "Resources": [ { "Type": "AwsAccount", "Id": "AWS::::Account:123456789012", "Partition": "aws", "Region": "us-west-1" } ], "Compliance": { "Status": "FAILED" }, "WorkflowState": "NEW", "Workflow": { "Status": "NOTIFIED" }, "RecordState": "ACTIVE" } ] }`For more information, see [Filtering and grouping findings](https://docs.aws.amazon.com/securityhub/latest/userguide/findings-filtering-grouping.html)in the*AWS Security Hub User Guide*.- 
                    For API details, see [GetFindings](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/securityhub/get-findings.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `get-insight-results`.

- **AWS CLI**
- 
            
                    **To retrieve the results for an insight**The following `get-insight-results`example returns the list of insight results for the insight with the specified ARN.`aws securityhub get-insight-results \ --insight-arn``"arn:aws:securityhub:us-west-1:123456789012:insight/123456789012/custom/a1b2c3d4-5678-90ab-cdef-EXAMPLE11111"`Output: `{ "InsightResults": { "GroupByAttribute": "ResourceId", "InsightArn": "arn:aws:securityhub:us-west-1:123456789012:insight/123456789012/custom/a1b2c3d4-5678-90ab-cdef-EXAMPLE11111", "ResultValues": [ { "Count": 10, "GroupByAttributeValue": "AWS::::Account:123456789111" }, { "Count": 3, "GroupByAttributeValue": "AWS::::Account:123456789222" } ] } }`For more information, see [Viewing and taking action on insight results and findings](https://docs.aws.amazon.com/securityhub/latest/userguide/securityhub-insights-view-take-action.html)in the*AWS Security Hub User Guide*.- 
                    For API details, see [GetInsightResults](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/securityhub/get-insight-results.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `get-insights`.

- **AWS CLI**
- 
            
                    **To retrieve details about an insight**The following `get-insights`example retrieves the configuration details for the insight with the specified ARN.`aws securityhub get-insights \ --insight-arns``"arn:aws:securityhub:us-west-1:123456789012:insight/123456789012/custom/a1b2c3d4-5678-90ab-cdef-EXAMPLE11111"`Output: `{ "Insights": [ { "Filters": { "ResourceType": [ { "Comparison": "EQUALS", "Value": "AwsIamRole" } ], "SeverityLabel": [ { "Comparison": "EQUALS", "Value": "CRITICAL" } ], }, "GroupByAttribute": "ResourceId", "InsightArn": "arn:aws:securityhub:us-west-1:123456789012:insight/123456789012/custom/a1b2c3d4-5678-90ab-cdef-EXAMPLE11111", "Name": "Critical role findings" } ] }`For more information, see [Insights in AWS Security Hub](https://docs.aws.amazon.com/securityhub/latest/userguide/securityhub-insights.html)in the*AWS Security Hub User Guide*.- 
                    For API details, see [GetInsights](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/securityhub/get-insights.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `get-invitations-count`.

- **AWS CLI**
- 
            
                    **To retrieve the number of invitations that were not accepted**The following `get-invitations-count`example retrieves the number of invitations that the requesting account declined or did not respond to.`aws securityhub get-invitations-count`Output: `{ "InvitationsCount": 3 }`For more information, see [Managing administrator and member accounts](https://docs.aws.amazon.com/securityhub/latest/userguide/securityhub-accounts.html)in the*AWS Security Hub User Guide*.- 
                    For API details, see [GetInvitationsCount](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/securityhub/get-invitations-count.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `get-master-account`.

- **AWS CLI**
- 
            
                    **To retrieve information about an administrator account**The following `get-master-account`example retrieves information about the administrator account for the requesting account.`aws securityhub get-master-account`Output: `{ "Master": { "AccountId": "123456789012", "InvitationId": "7ab938c5d52d7904ad09f9e7c20cc4eb", "InvitedAt": 2020-06-01T20:21:18.042000+00:00, "MemberStatus": "ASSOCIATED" } }`For more information, see [Managing administrator and member accounts](https://docs.aws.amazon.com/securityhub/latest/userguide/securityhub-accounts.html)in the*AWS Security Hub User Guide*.- 
                    For API details, see [GetMasterAccount](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/securityhub/get-master-account.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `get-members`.

- **AWS CLI**
- 
            
                    **To retrieve information about selected member accounts**The following `get-members`example retrieves information about the specified member accounts.`aws securityhub get-members \ --account-ids``"444455556666"``"777788889999"`Output: `{ "Members": [ { "AccountId": "123456789111", "AdministratorId": "123456789012", "InvitedAt": 2020-06-01T20:15:15.289000+00:00, "MasterId": "123456789012", "MemberStatus": "ASSOCIATED", "UpdatedAt": 2020-06-01T20:15:15.289000+00:00 }, { "AccountId": "123456789222", "AdministratorId": "123456789012", "InvitedAt": 2020-06-01T20:15:15.289000+00:00, "MasterId": "123456789012", "MemberStatus": "ASSOCIATED", "UpdatedAt": 2020-06-01T20:15:15.289000+00:00 } ], "UnprocessedAccounts": [ ] }`For more information, see [Managing administrator and member accounts](https://docs.aws.amazon.com/securityhub/latest/userguide/securityhub-accounts.html)in the*AWS Security Hub User Guide*.- 
                    For API details, see [GetMembers](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/securityhub/get-members.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `get-security-control-definition`.

- **AWS CLI**
- 
            
                    **To get security control definition details**The following `get-security-control-definition`example retrieves definition details for a Security Hub security control. Details include the control title, description, Region availability, parameters, and other information.`aws securityhub get-security-control-definition \ --security-control-id``ACM.1`Output: `{ "SecurityControlDefinition": { "SecurityControlId": "ACM.1", "Title": "Imported and ACM-issued certificates should be renewed after a specified time period", "Description": "This control checks whether an AWS Certificate Manager (ACM) certificate is renewed within the specified time period. It checks both imported certificates and certificates provided by ACM. The control fails if the certificate isn't renewed within the specified time period. Unless you provide a custom parameter value for the renewal period, Security Hub uses a default value of 30 days.", "RemediationUrl": "https://docs.aws.amazon.com/console/securityhub/ACM.1/remediation", "SeverityRating": "MEDIUM", "CurrentRegionAvailability": "AVAILABLE", "ParameterDefinitions": { "daysToExpiration": { "Description": "Number of days within which the ACM certificate must be renewed", "ConfigurationOptions": { "Integer": { "DefaultValue": 30, "Min": 14, "Max": 365 } } } } } }`For more information, see [Custom control parameters](https://docs.aws.amazon.com/securityhub/latest/userguide/custom-control-parameters.html)in the*AWS Security Hub User Guide*.- 
                    For API details, see [GetSecurityControlDefinition](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/securityhub/get-security-control-definition.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `invite-members`.

- **AWS CLI**
- 
            
                    **To send invitations to member accounts**The following `invite-members`example sends invitations to the specified member accounts.`aws securityhub invite-members \ --account-ids``"123456789111"``"123456789222"`Output: `{ "UnprocessedAccounts": [] }`For more information, see [Managing administrator and member accounts](https://docs.aws.amazon.com/securityhub/latest/userguide/securityhub-accounts.html)in the*AWS Security Hub User Guide*.- 
                    For API details, see [InviteMembers](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/securityhub/invite-members.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `list-automation-rules`.

- **AWS CLI**
- 
            
                    **To view a list of automation rules**The following `list-automation-rules`example lists the automation rules for an AWS account. Only the Security Hub administrator account can run this command.`aws securityhub list-automation-rules \ --max-results``3`\ --next-token`NULL`Output: `{ "AutomationRulesMetadata": [ { "RuleArn": "arn:aws:securityhub:us-east-1:123456789012:automation-rule/a1b2c3d4-5678-90ab-cdef-EXAMPLE11111", "RuleStatus": "ENABLED", "RuleOrder": 1, "RuleName": "Suppress informational findings", "Description": "Suppress GuardDuty findings with Informational severity", "IsTerminal": false, "CreatedAt": "2023-05-31T17:56:14.837000+00:00", "UpdatedAt": "2023-05-31T17:59:38.466000+00:00", "CreatedBy": "arn:aws:iam::123456789012:role/Admin" }, { "RuleArn": "arn:aws:securityhub:us-east-1:123456789012:automation-rule/a1b2c3d4-5678-90ab-cdef-EXAMPLE22222", "RuleStatus": "ENABLED", "RuleOrder": 1, "RuleName": "sample rule", "Description": "A sample rule", "IsTerminal": false, "CreatedAt": "2023-07-15T23:37:20.223000+00:00", "UpdatedAt": "2023-07-15T23:37:20.223000+00:00", "CreatedBy": "arn:aws:iam::123456789012:role/Admin" }, { "RuleArn": "arn:aws:securityhub:us-east-1:123456789012:automation-rule/a1b2c3d4-5678-90ab-cdef-EXAMPLE33333", "RuleStatus": "ENABLED", "RuleOrder": 1, "RuleName": "sample rule", "Description": "A sample rule", "IsTerminal": false, "CreatedAt": "2023-07-15T23:45:25.126000+00:00", "UpdatedAt": "2023-07-15T23:45:25.126000+00:00", "CreatedBy": "arn:aws:iam::123456789012:role/Admin" } ] }`For more information, see [Viewing automation rules](https://docs.aws.amazon.com/securityhub/latest/userguide/automation-rules.html#view-automation-rules)in the*AWS Security Hub User Guide*.- 
                    For API details, see [ListAutomationRules](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/securityhub/list-automation-rules.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `list-configuration-policies`.

- **AWS CLI**
- 
            
                    **To list configuration policy summaries**The following `list-configuration-policies`example lists a summary of configuration policies for the organization.`aws securityhub list-configuration-policies \ --max-items``3`Output: `{ "ConfigurationPolicySummaries": [ { "Arn": "arn:aws:securityhub:eu-central-1:123456789012:configuration-policy/a1b2c3d4-5678-90ab-cdef-EXAMPLE11111", "Id": "a1b2c3d4-5678-90ab-cdef-EXAMPLE11111", "Name": "SampleConfigurationPolicy1", "Description": "SampleDescription1", "UpdatedAt": "2023-09-26T21:08:36.214000+00:00", "ServiceEnabled": true }, { "Arn": "arn:aws:securityhub:eu-central-1:123456789012:configuration-policy/a1b2c3d4-5678-90ab-cdef-EXAMPLE22222", "Id": "a1b2c3d4-5678-90ab-cdef-EXAMPLE22222", "Name": "SampleConfigurationPolicy2", "Description": "SampleDescription2" "UpdatedAt": "2023-11-28T19:26:25.207000+00:00", "ServiceEnabled": true }, { "Arn": "arn:aws:securityhub:eu-central-1:123456789012:configuration-policy/a1b2c3d4-5678-90ab-cdef-EXAMPLE33333", "Id": "a1b2c3d4-5678-90ab-cdef-EXAMPLE33333", "Name": "SampleConfigurationPolicy3", "Description": "SampleDescription3", "UpdatedAt": "2023-11-28T20:28:04.494000+00:00", "ServiceEnabled": true } }`For more information, see [Viewing Security Hub configuration policies](https://docs.aws.amazon.com/securityhub/latest/userguide/view-policy.html)in the*AWS Security Hub User Guide*.- 
                    For API details, see [ListConfigurationPolicies](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/securityhub/list-configuration-policies.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `list-configuration-policy-associations`.

- **AWS CLI**
- 
            
                    **To list configuration associations**The following `list-configuration-policy-associations`example lists a summary of configuration associations for the organization. The response include associations with configuration policies and self-managed behavior.`aws securityhub list-configuration-policy-associations \ --filters '``{"AssociationType": "APPLIED"}`' \ --max-items`4`Output: `{ "ConfigurationPolicyAssociationSummaries": [ { "ConfigurationPolicyId": "a1b2c3d4-5678-90ab-cdef-EXAMPLE11111", "TargetId": "r-1ab2", "TargetType": "ROOT", "AssociationType": "APPLIED", "UpdatedAt": "2023-11-28T19:26:49.417000+00:00", "AssociationStatus": "FAILED", "AssociationStatusMessage": "Policy association failed because 2 organizational units or accounts under this root failed." }, { "ConfigurationPolicyId": "a1b2c3d4-5678-90ab-cdef-EXAMPLE22222", "TargetId": "ou-1ab2-c3de4f5g", "TargetType": "ORGANIZATIONAL_UNIT", "AssociationType": "APPLIED", "UpdatedAt": "2023-09-26T21:14:05.283000+00:00", "AssociationStatus": "FAILED", "AssociationStatusMessage": "One or more children under this target failed association." }, { "ConfigurationPolicyId": "a1b2c3d4-5678-90ab-cdef-EXAMPLE33333", "TargetId": "ou-6hi7-8j91kl2m", "TargetType": "ORGANIZATIONAL_UNIT", "AssociationType": "APPLIED", "UpdatedAt": "2023-09-26T21:13:01.816000+00:00", "AssociationStatus": "SUCCESS", "AssociationStatusMessage": "Association applied successfully on this target." }, { "ConfigurationPolicyId": "SELF_MANAGED_SECURITY_HUB", "TargetId": "111122223333", "TargetType": "ACCOUNT", "AssociationType": "APPLIED", "UpdatedAt": "2023-11-28T22:01:26.409000+00:00", "AssociationStatus": "SUCCESS" } }`For more information, see [Viewing configuration policy status and details](https://docs.aws.amazon.com/securityhub/latest/userguide/view-policy.html)in the*AWS Security Hub User Guide*.- 
                    For API details, see [ListConfigurationPolicyAssociations](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/securityhub/list-configuration-policy-associations.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `list-enabled-products-for-import`.

- **AWS CLI**
- 
            
                    **To return the list of enabled product integrations**The following `list-enabled-products-for-import`example returns the list of subscription ARNS for the currently enabled product integrations.`aws securityhub list-enabled-products-for-import`Output: `{ "ProductSubscriptions": [ "arn:aws:securityhub:us-west-1:123456789012:product-subscription/crowdstrike/crowdstrike-falcon", "arn:aws:securityhub:us-west-1:123456789012:product-subscription/aws/securityhub" ] }`For more information, see [Managing product integrations](https://docs.aws.amazon.com/securityhub/latest/userguide/securityhub-integrations-managing.html)in the*AWS Security Hub User Guide*.- 
                    For API details, see [ListEnabledProductsForImport](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/securityhub/list-enabled-products-for-import.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `list-finding-aggregators`.

- **AWS CLI**
- 
            
                    **To list the available widgets**The following `list-finding-aggregators`example returns the ARN of the finding aggregation configuration.`aws securityhub list-finding-aggregators`Output: `{ "FindingAggregatorArn": "arn:aws:securityhub:us-east-1:222222222222:finding-aggregator/123e4567-e89b-12d3-a456-426652340000" }`For more information, see [Viewing the current finding aggregation configuration](https://docs.aws.amazon.com/securityhub/latest/userguide/finding-aggregation-view-config.html)in the*AWS Security Hub User Guide*.- 
                    For API details, see [ListFindingAggregators](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/securityhub/list-finding-aggregators.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `list-invitations`.

- **AWS CLI**
- 
            
                    **To display a list of invitations**The following `list-invitations`example retrieves the list of invitations sent to the requesting account.`aws securityhub list-invitations`Output: `{ "Invitations": [ { "AccountId": "123456789012", "InvitationId": "7ab938c5d52d7904ad09f9e7c20cc4eb", "InvitedAt": 2020-06-01T20:21:18.042000+00:00, "MemberStatus": "ASSOCIATED" } ], }`For more information, see [Managing administrator and member accounts](https://docs.aws.amazon.com/securityhub/latest/userguide/securityhub-accounts.html)in the*AWS Security Hub User Guide*.- 
                    For API details, see [ListInvitations](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/securityhub/list-invitations.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `list-members`.

- **AWS CLI**
- 
            
                    **To retrieve a list of member accounts**The following `list-members`example returns the list of member accounts for the requesting administrator account.`aws securityhub list-members`Output: `{ "Members": [ { "AccountId": "123456789111", "AdministratorId": "123456789012", "InvitedAt": 2020-06-01T20:15:15.289000+00:00, "MasterId": "123456789012", "MemberStatus": "ASSOCIATED", "UpdatedAt": 2020-06-01T20:15:15.289000+00:00 }, { "AccountId": "123456789222", "AdministratorId": "123456789012", "InvitedAt": 2020-06-01T20:15:15.289000+00:00, "MasterId": "123456789012", "MemberStatus": "ASSOCIATED", "UpdatedAt": 2020-06-01T20:15:15.289000+00:00 } ], }`For more information, see [Managing administrator and member accounts](https://docs.aws.amazon.com/securityhub/latest/userguide/securityhub-accounts.html)in the*AWS Security Hub User Guide*.- 
                    For API details, see [ListMembers](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/securityhub/list-members.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `list-organization-admin-accounts`.

- **AWS CLI**
- 
            
                    **To list the designated Security Hub administrator accounts**The following `list-organization-admin-accounts`example lists the Security Hub administrator accounts for an organization.`aws securityhub list-organization-admin-accounts`Output: `{ AdminAccounts": [ { "AccountId": "777788889999" }, { "Status": "ENABLED" } ] }`For more information, see [Designating a Security Hub administrator account](https://docs.aws.amazon.com/securityhub/latest/userguide/designate-orgs-admin-account.html)in the*AWS Security Hub User Guide*.- 
                    For API details, see [ListOrganizationAdminAccounts](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/securityhub/list-organization-admin-accounts.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `list-security-control-definitions`.

- **AWS CLI**
- 
            
                    **Example 1: To list all available security controls**The following `list-security-control-definitions`example lists the available security controls across all Security Hub standards. This example limits the results to three controls.`aws securityhub list-security-control-definitions \ --max-items``3`Output: `{ "SecurityControlDefinitions": [ { "SecurityControlId": "ACM.1", "Title": "Imported and ACM-issued certificates should be renewed after a specified time period", "Description": "This control checks whether an AWS Certificate Manager (ACM) certificate is renewed within the specified time period. It checks both imported certificates and certificates provided by ACM. The control fails if the certificate isn't renewed within the specified time period. Unless you provide a custom parameter value for the renewal period, Security Hub uses a default value of 30 days.", "RemediationUrl": "https://docs.aws.amazon.com/console/securityhub/ACM.1/remediation", "SeverityRating": "MEDIUM", "CurrentRegionAvailability": "AVAILABLE", "CustomizableProperties": [ "Parameters" ] }, { "SecurityControlId": "ACM.2", "Title": "RSA certificates managed by ACM should use a key length of at least 2,048 bits", "Description": "This control checks whether RSA certificates managed by AWS Certificate Manager use a key length of at least 2,048 bits. The control fails if the key length is smaller than 2,048 bits.", "RemediationUrl": "https://docs.aws.amazon.com/console/securityhub/ACM.2/remediation", "SeverityRating": "HIGH", "CurrentRegionAvailability": "AVAILABLE", "CustomizableProperties": [] }, { "SecurityControlId": "APIGateway.1", "Title": "API Gateway REST and WebSocket API execution logging should be enabled", "Description": "This control checks whether all stages of an Amazon API Gateway REST or WebSocket API have logging enabled. The control fails if the 'loggingLevel' isn't 'ERROR' or 'INFO' for all stages of the API. Unless you provide custom parameter values to indicate that a specific log type should be enabled, Security Hub produces a passed finding if the logging level is either 'ERROR' or 'INFO'.", "RemediationUrl": "https://docs.aws.amazon.com/console/securityhub/APIGateway.1/remediation", "SeverityRating": "MEDIUM", "CurrentRegionAvailability": "AVAILABLE", "CustomizableProperties": [ "Parameters" ] } ], "NextToken": "U2FsdGVkX1/UprCPzxVbkDeHikDXbDxfgJZ1w2RG1XWsFPTMTIQPVE0m/FduIGxS7ObRtAbaUt/8/RCQcg2PU0YXI20hH/GrhoOTgv+TSm0qvQVFhkJepWmqh+NYawjocVBeos6xzn/8qnbF9IuwGg==" }`For more information, see [Viewing details for a standard](https://docs.aws.amazon.com/securityhub/latest/userguide/securityhub-standards-view-controls.html)in the*AWS Security Hub User Guide*.**Example 2: To list available security controls for a specific standard**The following `list-security-control-definitions`example lists the available security controls for the CIS AWS Foundations Benchmark v1.4.0. This example limits the results to three controls.`aws securityhub list-security-control-definitions \ --standards-arn``"arn:aws:securityhub:us-east-1::standards/cis-aws-foundations-benchmark/v/1.4.0"`\ --max-items`3`Output: `{ "SecurityControlDefinitions": [ { "SecurityControlId": "CloudTrail.1", "Title": "CloudTrail should be enabled and configured with at least one multi-Region trail that includes read and write management events", "Description": "This AWS control checks that there is at least one multi-region AWS CloudTrail trail includes read and write management events.", "RemediationUrl": "https://docs.aws.amazon.com/console/securityhub/CloudTrail.1/remediation", "SeverityRating": "HIGH", "CurrentRegionAvailability": "AVAILABLE", "CustomizableProperties": [] }, { "SecurityControlId": "CloudTrail.2", "Title": "CloudTrail should have encryption at-rest enabled", "Description": "This AWS control checks whether AWS CloudTrail is configured to use the server side encryption (SSE) AWS Key Management Service (AWS KMS) customer master key (CMK) encryption. The check will pass if the KmsKeyId is defined.", "RemediationUrl": "https://docs.aws.amazon.com/console/securityhub/CloudTrail.2/remediation", "SeverityRating": "MEDIUM", "CurrentRegionAvailability": "AVAILABLE", "CustomizableProperties": [] }, { "SecurityControlId": "CloudTrail.4", "Title": "CloudTrail log file validation should be enabled", "Description": "This AWS control checks whether CloudTrail log file validation is enabled.", "RemediationUrl": "https://docs.aws.amazon.com/console/securityhub/CloudTrail.4/remediation", "SeverityRating": "MEDIUM", "CurrentRegionAvailability": "AVAILABLE", "CustomizableProperties": [] } ], "NextToken": "eyJOZXh0VG9rZW4iOiBudWxsLCAiYm90b190cnVuY2F0ZV9hbW91bnQiOiAzfQ==" }`For more information, see [Viewing details for a standard](https://docs.aws.amazon.com/securityhub/latest/userguide/securityhub-standards-view-controls.html)in the*AWS Security Hub User Guide*.- 
                    For API details, see [ListSecurityControlDefinitions](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/securityhub/list-security-control-definitions.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `list-standards-control-associations`.

- **AWS CLI**
- 
            
                    **To get the enablement status of a control in each enabled standard**The following `list-standards-control-associations`example lists the enablement status of CloudTrail.1 in each enabled standard.`aws securityhub list-standards-control-associations \ --security-control-id``CloudTrail.1`Output: `{ "StandardsControlAssociationSummaries": [ { "StandardsArn": "arn:aws:securityhub:us-east-2::standards/nist-800-53/v/5.0.0", "SecurityControlId": "CloudTrail.1", "SecurityControlArn": "arn:aws:securityhub:us-east-2:123456789012:security-control/CloudTrail.1", "AssociationStatus": "ENABLED", "RelatedRequirements": [ "NIST.800-53.r5 AC-2(4)", "NIST.800-53.r5 AC-4(26)", "NIST.800-53.r5 AC-6(9)", "NIST.800-53.r5 AU-10", "NIST.800-53.r5 AU-12", "NIST.800-53.r5 AU-2", "NIST.800-53.r5 AU-3", "NIST.800-53.r5 AU-6(3)", "NIST.800-53.r5 AU-6(4)", "NIST.800-53.r5 AU-14(1)", "NIST.800-53.r5 CA-7", "NIST.800-53.r5 SC-7(9)", "NIST.800-53.r5 SI-3(8)", "NIST.800-53.r5 SI-4(20)", "NIST.800-53.r5 SI-7(8)", "NIST.800-53.r5 SA-8(22)" ], "UpdatedAt": "2023-05-15T17:52:21.304000+00:00", "StandardsControlTitle": "CloudTrail should be enabled and configured with at least one multi-Region trail that includes read and write management events", "StandardsControlDescription": "This AWS control checks that there is at least one multi-region AWS CloudTrail trail includes read and write management events." }, { "StandardsArn": "arn:aws:securityhub:::ruleset/cis-aws-foundations-benchmark/v/1.2.0", "SecurityControlId": "CloudTrail.1", "SecurityControlArn": "arn:aws:securityhub:us-east-2:123456789012:security-control/CloudTrail.1", "AssociationStatus": "ENABLED", "RelatedRequirements": [ "CIS AWS Foundations 2.1" ], "UpdatedAt": "2020-02-10T21:22:53.998000+00:00", "StandardsControlTitle": "Ensure CloudTrail is enabled in all regions", "StandardsControlDescription": "AWS CloudTrail is a web service that records AWS API calls for your account and delivers log files to you. The recorded information includes the identity of the API caller, the time of the API call, the source IP address of the API caller, the request parameters, and the response elements returned by the AWS service." }, { "StandardsArn": "arn:aws:securityhub:us-east-2::standards/aws-foundational-security-best-practices/v/1.0.0", "SecurityControlId": "CloudTrail.1", "SecurityControlArn": "arn:aws:securityhub:us-east-2:123456789012:security-control/CloudTrail.1", "AssociationStatus": "DISABLED", "RelatedRequirements": [], "UpdatedAt": "2023-05-15T19:31:52.671000+00:00", "UpdatedReason": "Alternative compensating controls are in place", "StandardsControlTitle": "CloudTrail should be enabled and configured with at least one multi-Region trail that includes read and write management events", "StandardsControlDescription": "This AWS control checks that there is at least one multi-region AWS CloudTrail trail includes read and write management events." }, { "StandardsArn": "arn:aws:securityhub:us-east-2::standards/cis-aws-foundations-benchmark/v/1.4.0", "SecurityControlId": "CloudTrail.1", "SecurityControlArn": "arn:aws:securityhub:us-east-2:123456789012:security-control/CloudTrail.1", "AssociationStatus": "ENABLED", "RelatedRequirements": [ "CIS AWS Foundations Benchmark v1.4.0/3.1" ], "UpdatedAt": "2022-11-10T15:40:36.021000+00:00", "StandardsControlTitle": "Ensure CloudTrail is enabled in all regions", "StandardsControlDescription": "AWS CloudTrail is a web service that records AWS API calls for your account and delivers log files to you. The recorded information includes the identity of the API caller, the time of the API call, the source IP address of the API caller, the request parameters, and the response elements returned by the AWS service. CloudTrail provides a history of AWS API calls for an account, including API calls made via the Management Console, SDKs, command line tools, and higher-level AWS services (such as CloudFormation)." } ] }`For more information, see [Enabling and disabling controls in specific standards](https://docs.aws.amazon.com/securityhub/latest/userguide/controls-configure.html)in the*AWS Security Hub User Guide*.- 
                    For API details, see [ListStandardsControlAssociations](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/securityhub/list-standards-control-associations.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `list-tags-for-resource`.

- **AWS CLI**
- 
            
                    **To retrieve the tags assigned to a resource**The following `list-tags-for-resource`example returns the tags assigned to the specified hub resource.`aws securityhub list-tags-for-resource \ --resource-arn``"arn:aws:securityhub:us-west-1:123456789012:hub/default"`Output: `{ "Tags": { "Department" : "Operations", "Area" : "USMidwest" } }`For more information, see [AWS::SecurityHub::Hub](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-securityhub-hub.html)in the*AWS CloudFormation User Guide*.- 
                    For API details, see [ListTagsForResource](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/securityhub/list-tags-for-resource.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `start-configuration-policy-association`.

- **AWS CLI**
- 
            
                    **Example 1: To associate a configuration policy**The following `start-configuration-policy-association`example associates the specified configuration policy with the specified organizational unit. A configuration may be associated with a target account, organizational unit, or the root.`aws securityhub start-configuration-policy-association \ --configuration-policy-identifier``"arn:aws:securityhub:eu-central-1:123456789012:configuration-policy/a1b2c3d4-5678-90ab-cdef-EXAMPLE33333"`\ --target '`{"OrganizationalUnitId": "ou-6hi7-8j91kl2m"}`'Output: `{ "ConfigurationPolicyId": "a1b2c3d4-5678-90ab-cdef-EXAMPLE33333", "TargetId": "ou-6hi7-8j91kl2m", "TargetType": "ORGANIZATIONAL_UNIT", "AssociationType": "APPLIED", "UpdatedAt": "2023-11-29T17:40:52.468000+00:00", "AssociationStatus": "PENDING" }`For more information, see [Creating and associating Security Hub configuration policies](https://docs.aws.amazon.com/securityhub/latest/userguide/create-associate-policy.html)in the*AWS Security Hub User Guide*.**Example 2: To associate a self-managed configuration**The following `start-configuration-policy-association`example associates a self-managed configuration with the specified account.`aws securityhub start-configuration-policy-association \ --configuration-policy-identifier``"SELF_MANAGED_SECURITY_HUB"`\ --target '`{"OrganizationalUnitId": "123456789012"}`'Output: `{ "ConfigurationPolicyId": "SELF_MANAGED_SECURITY_HUB", "TargetId": "123456789012", "TargetType": "ACCOUNT", "AssociationType": "APPLIED", "UpdatedAt": "2023-11-29T17:40:52.468000+00:00", "AssociationStatus": "PENDING" }`For more information, see [Creating and associating Security Hub configuration policies](https://docs.aws.amazon.com/securityhub/latest/userguide/create-associate-policy.html)in the*AWS Security Hub User Guide*.- 
                    For API details, see [StartConfigurationPolicyAssociation](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/securityhub/start-configuration-policy-association.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `start-configuration-policy-disassociation`.

- **AWS CLI**
- 
            
                    **Example 1: To disassociate a configuration policy**The following `start-configuration-policy-disassociation`example disassociates a configuration policy from the specified organizational unit. A configuration may be disassociated from a target account, organizational unit, or the root.`aws securityhub start-configuration-policy-disassociation \ --configuration-policy-identifier``"arn:aws:securityhub:eu-central-1:123456789012:configuration-policy/a1b2c3d4-5678-90ab-cdef-EXAMPLE33333"`\ --target '`{"OrganizationalUnitId": "ou-6hi7-8j91kl2m"}`'This command produces no output. For more information, see [Disassociating a configuration from accounts and OUs](https://docs.aws.amazon.com/securityhub/latest/userguide/delete-disassociate-policy.html#disassociate-policy)in the*AWS Security Hub User Guide*.**Example 2: To disassociate a self-managed configuration**The following `start-configuration-policy-disassociation`example disassociates a self-managed configuration from the specified account.`aws securityhub start-configuration-policy-disassociation \ --configuration-policy-identifier``"SELF_MANAGED_SECURITY_HUB"`\ --target '`{"AccountId": "123456789012"}`'This command produces no output. For more information, see [Disassociating a configuration from accounts and OUs](https://docs.aws.amazon.com/securityhub/latest/userguide/delete-disassociate-policy.html#disassociate-policy)in the*AWS Security Hub User Guide*.- 
                    For API details, see [StartConfigurationPolicyDisassociation](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/securityhub/start-configuration-policy-disassociation.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `tag-resource`.

- **AWS CLI**
- 
            
                    **To assign a tag to a resource**The following `tag-resource`example assigns values for the Department and Area tags to the specified hub resource.`aws securityhub tag-resource \ --resource-arn``"arn:aws:securityhub:us-west-1:123456789012:hub/default"`\ --tags '`{"Department":"Operations", "Area":"USMidwest"}`'This command produces no output. For more information, see [AWS::SecurityHub::Hub](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-securityhub-hub.html)in the*AWS CloudFormation User Guide*.- 
                    For API details, see [TagResource](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/securityhub/tag-resource.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `untag-resource`.

- **AWS CLI**
- 
            
                    **To remove a tag value from a resource**The following `untag-resource`example removes the Department tag from the specified hub resource.`aws securityhub untag-resource \ --resource-arn``"arn:aws:securityhub:us-west-1:123456789012:hub/default"`\ --tag-keys`"Department"`This command produces no output. For more information, see [AWS::SecurityHub::Hub](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-securityhub-hub.html)in the*AWS CloudFormation User Guide*.- 
                    For API details, see [UntagResource](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/securityhub/untag-resource.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `update-action-target`.

- **AWS CLI**
- 
            
                    **To update a custom action**The following `update-action-target`example updates the name of the custom action identified by the specified ARN.`aws securityhub update-action-target \ --action-target-arn``"arn:aws:securityhub:us-west-1:123456789012:action/custom/Remediation"`\ --name`"Send to remediation"`This command produces no output. For more information, see [Creating a custom action and associating it with a CloudWatch Events rule](https://docs.aws.amazon.com/securityhub/latest/userguide/securityhub-cloudwatch-events.html#securityhub-cwe-configure)in the*AWS Security Hub User Guide*.- 
                    For API details, see [UpdateActionTarget](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/securityhub/update-action-target.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `update-configuration-policy`.

- **AWS CLI**
- 
            
                    **To update a configuration policy**The following `update-configuration-policy`example updates an existing configuration policy to use the specified settings.`aws securityhub update-configuration-policy \ --identifier``"arn:aws:securityhub:eu-central-1:508236694226:configuration-policy/09f37766-57d8-4ede-9d33-5d8b0fecf70e"`\ --name`"SampleConfigurationPolicyUpdated"`\ --description`"SampleDescriptionUpdated"`\ --configuration-policy '`{"SecurityHub": {"ServiceEnabled": true, "EnabledStandardIdentifiers": ["arn:aws:securityhub:eu-central-1::standards/aws-foundational-security-best-practices/v/1.0.0","arn:aws:securityhub:::ruleset/cis-aws-foundations-benchmark/v/1.2.0"],"SecurityControlsConfiguration":{"DisabledSecurityControlIdentifiers": ["CloudWatch.1"], "SecurityControlCustomParameters": [{"SecurityControlId": "ACM.1", "Parameters": {"daysToExpiration": {"ValueType": "CUSTOM", "Value": {"Integer": 21}}}}]}}}`' \ --updated-reason`"Disabling CloudWatch.1 and changing parameter value"`Output: `{ "Arn": "arn:aws:securityhub:eu-central-1:123456789012:configuration-policy/a1b2c3d4-5678-90ab-cdef-EXAMPLE11111", "Id": "a1b2c3d4-5678-90ab-cdef-EXAMPLE11111", "Name": "SampleConfigurationPolicyUpdated", "Description": "SampleDescriptionUpdated", "UpdatedAt": "2023-11-28T20:28:04.494000+00:00", "CreatedAt": "2023-11-28T20:28:04.494000+00:00", "ConfigurationPolicy": { "SecurityHub": { "ServiceEnabled": true, "EnabledStandardIdentifiers": [ "arn:aws:securityhub:eu-central-1::standards/aws-foundational-security-best-practices/v/1.0.0", "arn:aws:securityhub:::ruleset/cis-aws-foundations-benchmark/v/1.2.0" ], "SecurityControlsConfiguration": { "DisabledSecurityControlIdentifiers": [ "CloudWatch.1" ], "SecurityControlCustomParameters": [ { "SecurityControlId": "ACM.1", "Parameters": { "daysToExpiration": { "ValueType": "CUSTOM", "Value": { "Integer": 21 } } } } ] } } } }`For more information, see [Updating Security Hub configuration policies](https://docs.aws.amazon.com/securityhub/latest/userguide/update-policy.html)in the*AWS Security Hub User Guide*.- 
                    For API details, see [UpdateConfigurationPolicy](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/securityhub/update-configuration-policy.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `update-finding-aggregator`.

- **AWS CLI**
- 
            
                    **To update the current finding aggregation configuration**The following `update-finding-aggregator`example changes the finding aggregation configuration to link from selected Regions. It is run from US East (Virginia), which is the aggregation Region. It selects US West (N. California) and US West (Oregon) as the linked Regions.`aws securityhub update-finding-aggregator \ --region``us-east-1`\ --finding-aggregator-arn`arn:aws:securityhub:us-east-1:222222222222:finding-aggregator/123e4567-e89b-12d3-a456-426652340000`\ --region-linking-mode`SPECIFIED_REGIONS`\ --regions`us-west-1,us-west-2`This command produces no output. For more information, see [Updating the finding aggregation configuration](https://docs.aws.amazon.com/securityhub/latest/userguide/finding-aggregation-update.html)in the*AWS Security Hub User Guide*.- 
                    For API details, see [UpdateFindingAggregator](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/securityhub/update-finding-aggregator.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `update-insight`.

- **AWS CLI**
- 
            
                    **Example 1: To change the filter for a custom insight**The following `update-insight`example changes the filters for a custom insight. The updated insight looks for findings with a high severity that are related to AWS roles.`aws securityhub update-insight \ --insight-arn``"arn:aws:securityhub:us-west-1:123456789012:insight/123456789012/custom/a1b2c3d4-5678-90ab-cdef-EXAMPLE11111"`\ --filters '`{"ResourceType": [{ "Comparison": "EQUALS", "Value": "AwsIamRole"}], "SeverityLabel": [{"Comparison": "EQUALS", "Value": "HIGH"}]}`' \ --name`"High severity role findings"`**Example 2: To change the grouping attribute for a custom insight**The following `update-insight`example changes the grouping attribute for the custom insight with the specified ARN. The new grouping attribute is the resource ID.`aws securityhub update-insight \ --insight-arn``"arn:aws:securityhub:us-west-1:123456789012:insight/123456789012/custom/a1b2c3d4-5678-90ab-cdef-EXAMPLE11111"`\ --group-by-attribute`"ResourceId"`\ --name`"Critical role findings"`Output: `{ "Insights": [ { "InsightArn": "arn:aws:securityhub:us-west-1:123456789012:insight/123456789012/custom/a1b2c3d4-5678-90ab-cdef-EXAMPLE11111", "Name": "Critical role findings", "Filters": { "SeverityLabel": [ { "Value": "CRITICAL", "Comparison": "EQUALS" } ], "ResourceType": [ { "Value": "AwsIamRole", "Comparison": "EQUALS" } ] }, "GroupByAttribute": "ResourceId" } ] }`For more information, see [Managing custom insights](https://docs.aws.amazon.com/securityhub/latest/userguide/securityhub-custom-insights.html)in the*AWS Security Hub User Guide*.- 
                    For API details, see [UpdateInsight](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/securityhub/update-insight.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `update-organization-configuration`.

- **AWS CLI**
- 
            
                    **To update how Security Hub is configured for an organization**The following `update-organization-configuration`example specifies that Security Hub should use central configuration to configure an organization. After running this command, the delegated Security Hub administrator can create and manage configuration policies to configure the organization. The delegated administrator can also use this command to switch from central to local configuration. If local configuration is the configuration type, the delegated administrator can choose whether to automatically enable Security Hub and default security standards in new organization accounts.`aws securityhub update-organization-configuration \ --no-auto-enable \ --organization-configuration '``{"ConfigurationType": "CENTRAL"}`'This command produces no output. For more information, see [Managing accounts with AWS Organizations](https://docs.aws.amazon.com/securityhub/latest/userguide/securityhub-accounts-orgs.html)in the*AWS Security Hub User Guide*.- 
                    For API details, see [UpdateOrganizationConfiguration](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/securityhub/update-organization-configuration.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `update-security-control`.

- **AWS CLI**
- 
            
                    **To update security control properties**The following `update-security-control`example specifies custom values for a Security Hub security control parameter.`aws securityhub update-security-control \ --security-control-id``ACM.1`\ --parameters '`{"daysToExpiration": {"ValueType": "CUSTOM", "Value": {"Integer": 15}}}`' \ --last-update-reason`"Internal compliance requirement"`This command produces no output. For more information, see [Custom control parameters](https://docs.aws.amazon.com/securityhub/latest/userguide/custom-control-parameters.html)in the*AWS Security Hub User Guide*.- 
                    For API details, see [UpdateSecurityControl](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/securityhub/update-security-control.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `update-security-hub-configuration`.

- **AWS CLI**
- 
            
                    **To update Security Hub configuration**The following `update-security-hub-configuration`example configures Security Hub to automatically enable new controls for enabled standards.`aws securityhub update-security-hub-configuration \ --auto-enable-controls`This command produces no output. For more information, see [Enabling new controls automatically](https://docs.aws.amazon.com/securityhub/latest/userguide/controls-auto-enable.html)in the*AWS Security Hub User Guide*.- 
                    For API details, see [UpdateSecurityHubConfiguration](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/securityhub/update-security-hub-configuration.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `update-standards-control`.

- **AWS CLI**
- 
            
                    **Example 1: To disable a control**The following `update-standards-control`example disables the PCI.AutoScaling.1 control.`aws securityhub update-standards-control \ --standards-control-arn``"arn:aws:securityhub:us-west-1:123456789012:control/pci-dss/v/3.2.1/PCI.AutoScaling.1"`\ --control-status`"DISABLED"`\ --disabled-reason`"Not applicable for my service"`This command produces no output. **Example 2: To enable a control**The following `update-standards-control`example enables the PCI.AutoScaling.1 control.`aws securityhub update-standards-control \ --standards-control-arn``"arn:aws:securityhub:us-west-1:123456789012:control/pci-dss/v/3.2.1/PCI.AutoScaling.1"`\ --control-status`"ENABLED"`This command produces no output. For more information, see [Disabling and enabling individual controls](https://docs.aws.amazon.com/securityhub/latest/userguide/securityhub-standards-enable-disable-controls.html)in the*AWS Security Hub User Guide*.- 
                    For API details, see [UpdateStandardsControl](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/securityhub/update-standards-control.html)in*AWS CLI Command Reference*.
 
-