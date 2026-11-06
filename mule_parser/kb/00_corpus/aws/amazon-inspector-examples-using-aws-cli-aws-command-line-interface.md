# Amazon Inspector examples using AWS CLI - AWS Command Line Interface

**Source:** [https://docs.aws.amazon.com/cli/latest/userguide/cli_inspector2_code_examples.html](https://docs.aws.amazon.com/cli/latest/userguide/cli_inspector2_code_examples.html)

---

The following code examples show you how to perform actions and implement common scenarios by using the AWS Command Line Interface with Amazon Inspector.

*Actions* are code excerpts from larger programs and must be run in context. While actions show you how to call individual service functions, you can see actions in context in their related scenarios.

Each example includes a link to the complete source code, where you can find instructions on how to set up and run the code in context.

###### Topics

## Actions

    The following code example shows how to use `add-attributes-to-findings`.

- **AWS CLI**
- 
            
                    **To add attributes to findings**The following `add-attribute-to-finding`command assigns an attribute with the key of`Example`and value of`example`to the finding with the ARN of`arn:aws:inspector:us-west-2:123456789012:target/0-0kFIPusq/template/0-8l1VIE0D/run/0-Z02cjjug/finding/0-T8yM9mEU`:`aws inspector add-attributes-to-findings --finding-arns``arn:aws:inspector:us-west-2:123456789012:target/0-0kFIPusq/template/0-8l1VIE0D/run/0-Z02cjjug/finding/0-T8yM9mEU`--attributes`key=Example,value=example`Output: `{ "failedItems": {} }`For more information, see Amazon Inspector Findings in the *Amazon Inspector*guide.- 
                    For API details, see [AddAttributesToFindings](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/inspector/add-attributes-to-findings.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `associate-member`.

- **AWS CLI**
- 
            
                    **Example: To associate an AWS account with an Amazon Inspector delegated administrator**The following `associate-member`example associates an AWS account with an Amazon Inspector delegated administrator.`aws inspector2 associate-member \ --account-id``123456789012`Output: `{ "accountId": "123456789012" }`For more information, see [Managing multiple accounts in Amazon Inspector with AWS Organizations](https://docs.aws.amazon.com/inspector/latest/user/managing-multiple-accounts.html)in the*Amazon Inspector User Guide*.- 
                    For API details, see [AssociateMember](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/inspector2/associate-member.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `create-assessment-target`.

- **AWS CLI**
- 
            
                    **To create an assessment target**The following `create-assessment-target`command creates an assessment target named`ExampleAssessmentTarget`using the resource group with the ARN of`arn:aws:inspector:us-west-2:123456789012:resourcegroup/0-AB6DMKnv`:`aws inspector create-assessment-target --assessment-target-name``ExampleAssessmentTarget`--resource-group-arn`arn:aws:inspector:us-west-2:123456789012:resourcegroup/0-AB6DMKnv`Output: `{ "assessmentTargetArn": "arn:aws:inspector:us-west-2:123456789012:target/0-nvgVhaxX" }`For more information, see Amazon Inspector Assessment Targets in the *Amazon Inspector*guide.- 
                    For API details, see [CreateAssessmentTarget](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/inspector/create-assessment-target.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `create-assessment-template`.

- **AWS CLI**
- 
            
                    **To create an assessment template**The following `create-assessment-template`command creates an assessment template called`ExampleAssessmentTemplate`for the assessment target with the ARN of`arn:aws:inspector:us-west-2:123456789012:target/0-nvgVhaxX`:`aws inspector create-assessment-template --assessment-target-arn``arn:aws:inspector:us-west-2:123456789012:target/0-nvgVhaxX`--assessment-template-name`ExampleAssessmentTemplate`--duration-in-seconds`180`--rules-package-arns`arn:aws:inspector:us-west-2:758058086616:rulespackage/0-9hgA516p`--user-attributes-for-findings`key=ExampleTag,value=examplevalue`Output: `{ "assessmentTemplateArn": "arn:aws:inspector:us-west-2:123456789012:target/0-nvgVhaxX/template/0-it5r2S4T" }`For more information, see Amazon Inspector Assessment Templates and Assessment Runs in the *Amazon Inspector*guide.- 
                    For API details, see [CreateAssessmentTemplate](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/inspector/create-assessment-template.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `create-filter`.

- **AWS CLI**
- 
            
                    **To create a filter**The following `create-filter`example creates a suppression rule that omits ECR instance type findings.`aws inspector2 create-filter \ --name``"ExampleSuppressionRuleECR"`\ --description`"This suppression rule omits ECR instance type findings"`\ --action`SUPPRESS`\ --filter-criteria '`resourceType=[{comparison="EQUALS", value="AWS_ECR_INSTANCE"}]`'Output: `{ "arn": "arn:aws:inspector2:us-west-2:123456789012:owner/o-EXAMPLE222/filter/EXAMPLE444444444" }`For more information, see [Filtering Amazon Inspector findings](https://docs.aws.amazon.com/inspector/latest/user/findings-managing-filtering.html)in the*Amazon Inspector User Guide*.- 
                    For API details, see [CreateFilter](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/inspector2/create-filter.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `create-findings-report`.

- **AWS CLI**
- 
            
                    **To create a findings report**The following `create-findings-report`example creates a finding report.`aws inspector2 create-findings-report \ --report-format``CSV`\ --s3-destination`bucketName=inspector-sbom-123456789012,keyPrefix=sbom-key,kmsKeyArn=arn:aws:kms:us-west-2:123456789012:key/a1b2c3d4-5678-90ab-cdef-EXAMPLE33333`\ --filter-criteria '`{"ecrImageRepositoryName":[{"comparison":"EQUALS","value":"debian"}]}`'Output: `{ "reportId": "a1b2c3d4-5678-90ab-cdef-EXAMPLE33333" }`For more information, see [Managing findings in Amazon Inspector](https://docs.aws.amazon.com/inspector/latest/user/findings-managing.html)in the*Amazon Inspector User Guide*.- 
                    For API details, see [CreateFindingsReport](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/inspector2/create-findings-report.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `create-resource-group`.

- **AWS CLI**
- 
            
                    **To create a resource group**The following `create-resource-group`command creates a resource group using the tag key of`Name`and value of`example`:`aws inspector create-resource-group --resource-group-tags``key=Name,value=example`Output: `{ "resourceGroupArn": "arn:aws:inspector:us-west-2:123456789012:resourcegroup/0-AB6DMKnv" }`For more information, see Amazon Inspector Assessment Targets in the *Amazon Inspector*guide.- 
                    For API details, see [CreateResourceGroup](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/inspector/create-resource-group.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `create-sbom-export`.

- **AWS CLI**
- 
            
                    **To create a software bill of materials (SBOM) report**The following `create-sbom-export`example creates a software bill of materials (SBOM) report.`aws inspector2 create-sbom-export \ --report-format``SPDX_2_3`\ --resource-filter-criteria '`ecrRepositoryName=[{comparison="EQUALS",value="debian"}]`' \ --s3-destination`bucketName=inspector-sbom-123456789012,keyPrefix=sbom-key,kmsKeyArn=arn:aws:kms:us-west-2:123456789012:key/a1b2c3d4-5678-90ab-cdef-EXAMPLE33333`Output: `{ "reportId": "a1b2c3d4-5678-90ab-cdef-EXAMPLE33333" }`For more information, see [Exporting SBOMs with Amazon Inspector](https://docs.aws.amazon.com/inspector/latest/user/sbom-export.html)in the*Amazon Inspector User Guide*.- 
                    For API details, see [CreateSbomExport](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/inspector2/create-sbom-export.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `delete-assessment-run`.

- **AWS CLI**
- 
            
                    **To delete an assessment run**The following `delete-assessment-run`command deletes the assessment run with the ARN of`arn:aws:inspector:us-west-2:123456789012:target/0-nvgVhaxX/template/0-it5r2S4T/run/0-11LMTAVe`:`aws inspector delete-assessment-run --assessment-run-arn``arn:aws:inspector:us-west-2:123456789012:target/0-nvgVhaxX/template/0-it5r2S4T/run/0-11LMTAVe`For more information, see Amazon Inspector Assessment Templates and Assessment Runs in the *Amazon Inspector*guide.- 
                    For API details, see [DeleteAssessmentRun](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/inspector/delete-assessment-run.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `delete-assessment-target`.

- **AWS CLI**
- 
            
                    **To delete an assessment target**The following `delete-assessment-target`command deletes the assessment target with the ARN of`arn:aws:inspector:us-west-2:123456789012:target/0-0kFIPusq`:`aws inspector delete-assessment-target --assessment-target-arn``arn:aws:inspector:us-west-2:123456789012:target/0-0kFIPusq`For more information, see Amazon Inspector Assessment Targets in the *Amazon Inspector*guide.- 
                    For API details, see [DeleteAssessmentTarget](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/inspector/delete-assessment-target.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `delete-assessment-template`.

- **AWS CLI**
- 
            
                    **To delete an assessment template**The following `delete-assessment-template`command deletes the assessment template with the ARN of`arn:aws:inspector:us-west-2:123456789012:target/0-nvgVhaxX/template/0-it5r2S4T`:`aws inspector delete-assessment-template --assessment-template-arn``arn:aws:inspector:us-west-2:123456789012:target/0-nvgVhaxX/template/0-it5r2S4T`For more information, see Amazon Inspector Assessment Templates and Assessment Runs in the *Amazon Inspector*guide.- 
                    For API details, see [DeleteAssessmentTemplate](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/inspector/delete-assessment-template.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `delete-filter`.

- **AWS CLI**
- 
            
                    **To delete a filter**The following `delete-filter`example deletes a filter.`aws inspector2 delete-filter \ --arn``"arn:aws:inspector2:us-west-2:123456789012:owner/o-EXAMPLE222/filter/EXAMPLE444444444"`Output: `{ "arn": "arn:aws:inspector2:us-west-2:123456789012:owner/o-EXAMPLE222/filter/EXAMPLE444444444" }`For more information, see [Filtering Amazon Inspector findings](https://docs.aws.amazon.com/inspector/latest/user/findings-managing-filtering.html)in the*Amazon Inspector User Guide*.- 
                    For API details, see [DeleteFilter](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/inspector2/delete-filter.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `describe-assessment-runs`.

- **AWS CLI**
- 
            
                    **To describe assessment runs**The following `describe-assessment-run`command describes an assessment run with the ARN of`arn:aws:inspector:us-west-2:123456789012:target/0-0kFIPusq/template/0-4r1V2mAw/run/0-MKkpXXPE`:`aws inspector describe-assessment-runs --assessment-run-arns``arn:aws:inspector:us-west-2:123456789012:target/0-0kFIPusq/template/0-4r1V2mAw/run/0-MKkpXXPE`Output: `{ "assessmentRuns": [ { "arn": "arn:aws:inspector:us-west-2:123456789012:target/0-0kFIPusq/template/0-4r1V2mAw/run/0-MKkpXXPE", "assessmentTemplateArn": "arn:aws:inspector:us-west-2:123456789012:target/0-0kFIPusq/template/0-4r1V2mAw", "completedAt": 1458680301.4, "createdAt": 1458680170.035, "dataCollected": true, "durationInSeconds": 3600, "name": "Run 1 for ExampleAssessmentTemplate", "notifications": [], "rulesPackageArns": [ "arn:aws:inspector:us-west-2:758058086616:rulespackage/0-X1KXtawP" ], "startedAt": 1458680170.161, "state": "COMPLETED", "stateChangedAt": 1458680301.4, "stateChanges": [ { "state": "CREATED", "stateChangedAt": 1458680170.035 }, { "state": "START_DATA_COLLECTION_PENDING", "stateChangedAt": 1458680170.065 }, { "state": "START_DATA_COLLECTION_IN_PROGRESS", "stateChangedAt": 1458680170.096 }, { "state": "COLLECTING_DATA", "stateChangedAt": 1458680170.161 }, { "state": "STOP_DATA_COLLECTION_PENDING", "stateChangedAt": 1458680239.883 }, { "state": "DATA_COLLECTED", "stateChangedAt": 1458680299.847 }, { "state": "EVALUATING_RULES", "stateChangedAt": 1458680300.099 }, { "state": "COMPLETED", "stateChangedAt": 1458680301.4 } ], "userAttributesForFindings": [] } ], "failedItems": {} }`For more information, see Amazon Inspector Assessment Templates and Assessment Runs in the *Amazon Inspector*guide.- 
                    For API details, see [DescribeAssessmentRuns](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/inspector/describe-assessment-runs.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `describe-assessment-targets`.

- **AWS CLI**
- 
            
                    **To describe assessment targets**The following `describe-assessment-targets`command describes the assessment target with the ARN of`arn:aws:inspector:us-west-2:123456789012:target/0-0kFIPusq`:`aws inspector describe-assessment-targets --assessment-target-arns``arn:aws:inspector:us-west-2:123456789012:target/0-0kFIPusq`Output: `{ "assessmentTargets": [ { "arn": "arn:aws:inspector:us-west-2:123456789012:target/0-0kFIPusq", "createdAt": 1458074191.459, "name": "ExampleAssessmentTarget", "resourceGroupArn": "arn:aws:inspector:us-west-2:123456789012:resourcegroup/0-PyGXopAI", "updatedAt": 1458074191.459 } ], "failedItems": {} }`For more information, see Amazon Inspector Assessment Targets in the *Amazon Inspector*guide.- 
                    For API details, see [DescribeAssessmentTargets](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/inspector/describe-assessment-targets.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `describe-assessment-templates`.

- **AWS CLI**
- 
            
                    **To describe assessment templates**The following `describe-assessment-templates`command describes the assessment template with the ARN of`arn:aws:inspector:us-west-2:123456789012:target/0-0kFIPusq/template/0-4r1V2mAw`:`aws inspector describe-assessment-templates --assessment-template-arns``arn:aws:inspector:us-west-2:123456789012:target/0-0kFIPusq/template/0-4r1V2mAw`Output: `{ "assessmentTemplates": [ { "arn": "arn:aws:inspector:us-west-2:123456789012:target/0-0kFIPusq/template/0-4r1V2mAw", "assessmentTargetArn": "arn:aws:inspector:us-west-2:123456789012:target/0-0kFIPusq", "createdAt": 1458074191.844, "durationInSeconds": 3600, "name": "ExampleAssessmentTemplate", "rulesPackageArns": [ "arn:aws:inspector:us-west-2:758058086616:rulespackage/0-X1KXtawP" ], "userAttributesForFindings": [] } ], "failedItems": {} }`For more information, see Amazon Inspector Assessment Templates and Assessment Runs in the *Amazon Inspector*guide.- 
                    For API details, see [DescribeAssessmentTemplates](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/inspector/describe-assessment-templates.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `describe-cross-account-access-role`.

- **AWS CLI**
- 
            
                    **To describe the cross account access role**The following `describe-cross-account-access-role`command describes the IAM role that enables Amazon Inspector to access your AWS account:`aws inspector describe-cross-account-access-role`Output: `{ "registeredAt": 1458069182.826, "roleArn": "arn:aws:iam::123456789012:role/inspector", "valid": true }`For more information, see Setting up Amazon Inspector in the *Amazon Inspector*guide.- 
                    For API details, see [DescribeCrossAccountAccessRole](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/inspector/describe-cross-account-access-role.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `describe-findings`.

- **AWS CLI**
- 
            
                    **To describe findings**The following `describe-findings`command describes the finding with the ARN of`arn:aws:inspector:us-west-2:123456789012:target/0-0kFIPusq/template/0-4r1V2mAw/run/0-MKkpXXPE/finding/0-HwPnsDm4`:`aws inspector describe-findings --finding-arns``arn:aws:inspector:us-west-2:123456789012:target/0-0kFIPusq/template/0-4r1V2mAw/run/0-MKkpXXPE/finding/0-HwPnsDm4`Output: `{ "failedItems": {}, "findings": [ { "arn": "arn:aws:inspector:us-west-2:123456789012:target/0-0kFIPusq/template/0-4r1V2mAw/run/0-MKkpXXPE/finding/0-HwPnsDm4", "assetAttributes": { "ipv4Addresses": [], "schemaVersion": 1 }, "assetType": "ec2-instance", "attributes": [], "confidence": 10, "createdAt": 1458680301.37, "description": "Amazon Inspector did not find any potential security issues during this assessment.", "indicatorOfCompromise": false, "numericSeverity": 0, "recommendation": "No remediation needed.", "schemaVersion": 1, "service": "Inspector", "serviceAttributes": { "assessmentRunArn": "arn:aws:inspector:us-west-2:123456789012:target/0-0kFIPusq/template/0-4r1V2mAw/run/0-MKkpXXPE", "rulesPackageArn": "arn:aws:inspector:us-west-2:758058086616:rulespackage/0-X1KXtawP", "schemaVersion": 1 }, "severity": "Informational", "title": "No potential security issues found", "updatedAt": 1458680301.37, "userAttributes": [] } ] }`For more information, see Amazon Inspector Findings in the *Amazon Inspector*guide.- 
                    For API details, see [DescribeFindings](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/inspector/describe-findings.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `describe-resource-groups`.

- **AWS CLI**
- 
            
                    **To describe resource groups**The following `describe-resource-groups`command describes the resource group with the ARN of`arn:aws:inspector:us-west-2:123456789012:resourcegroup/0-PyGXopAI`:`aws inspector describe-resource-groups --resource-group-arns``arn:aws:inspector:us-west-2:123456789012:resourcegroup/0-PyGXopAI`Output: `{ "failedItems": {}, "resourceGroups": [ { "arn": "arn:aws:inspector:us-west-2:123456789012:resourcegroup/0-PyGXopAI", "createdAt": 1458074191.098, "tags": [ { "key": "Name", "value": "example" } ] } ] }`For more information, see Amazon Inspector Assessment Targets in the *Amazon Inspector*guide.- 
                    For API details, see [DescribeResourceGroups](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/inspector/describe-resource-groups.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `describe-rules-packages`.

- **AWS CLI**
- 
            
                    **To describe rules packages**The following `describe-rules-packages`command describes the rules package with the ARN of`arn:aws:inspector:us-west-2:758058086616:rulespackage/0-9hgA516p`:`aws inspector describe-rules-packages --rules-package-arns``arn:aws:inspector:us-west-2:758058086616:rulespackage/0-9hgA516p`Output: `{ "failedItems": {}, "rulesPackages": [ { "arn": "arn:aws:inspector:us-west-2:758058086616:rulespackage/0-9hgA516p", "description": "The rules in this package help verify whether the EC2 instances in your application are exposed to Common Vulnerabilities and Exposures (CVEs). Attacks can exploit unpatched vulnerabilities to compromise the confidentiality, integrity, or availability of your service or data. The CVE system provides a reference for publicly known information security vulnerabilities and exposures. For more information, see [https://cve.mitre.org/](https://cve.mitre.org/). If a particular CVE appears in one of the produced Findings at the end of a completed Inspector assessment, you can search [https://cve.mitre.org/](https://cve.mitre.org/) using the CVE's ID (for example, \"CVE-2009-0021\") to find detailed information about this CVE, its severity, and how to mitigate it. ", "name": "Common Vulnerabilities and Exposures", "provider": "Amazon Web Services, Inc.", "version": "1.1" } ] }`For more information, see Amazon Inspector Rules Packages and Rules in the *Amazon Inspector*guide.- 
                    For API details, see [DescribeRulesPackages](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/inspector/describe-rules-packages.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `disassociate-member`.

- **AWS CLI**
- 
            
                    **Example: To disassociate a member account from an Amazon Inspector delegated administrator**The following `disassociate-member`example disassociates an AWS account from an Amazon Inspector delegated administrator.`aws inspector2 disassociate-member \ --account-id``123456789012`Output: `{ "accountId": "123456789012" }`For more information, see [Managing multiple accounts in Amazon Inspector with AWS Organizations](https://docs.aws.amazon.com/inspector/latest/user/managing-multiple-accounts.html)in the*Amazon Inspector User Guide*.- 
                    For API details, see [DisassociateMember](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/inspector2/disassociate-member.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `get-configuration`.

- **AWS CLI**
- 
            
                    **To get the setting configuration for Inspector scans**The following `get-configuration`example gets the setting configuration for Inspector scans.`aws inspector2 get-configuration`Output: `{ "ec2Configuration": { "scanModeState": { "scanMode": "EC2_HYBRID", "scanModeStatus": "SUCCESS" } }, "ecrConfiguration": { "rescanDurationState": { "pullDateRescanDuration": "DAYS_90", "rescanDuration": "DAYS_30", "status": "SUCCESS", "updatedAt": "2024-05-14T21:16:20.237000+00:00" } } }`For more information, see [Automated resource scanning with Amazon Inspector](https://docs.aws.amazon.com/inspector/latest/user/scanning-resources.html)in the*Amazon Inspector User Guide*.- 
                    For API details, see [GetConfiguration](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/inspector2/get-configuration.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `get-member`.

- **AWS CLI**
- 
            
                    **Example: To get member information for your organization**aws inspector2 get-member --account-id 123456789012 Output: `{ "member": { "accountId": "123456789012", "delegatedAdminAccountId": "123456789012", "relationshipStatus": "ENABLED", "updatedAt": "2023-09-11T09:57:20.520000-07:00" } }`For more information, see [Managing multiple accounts in Amazon Inspector with AWS Organizations](https://docs.aws.amazon.com/inspector/latest/user/managing-multiple-accounts.html)in the*Amazon Inspector User Guide*.- 
                    For API details, see [GetMember](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/inspector2/get-member.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `get-telemetry-metadata`.

- **AWS CLI**
- 
            
                    **To get the telemetry metadata**The following `get-telemetry-metadata`command generates information about the data that is collected for the assessment run with the ARN of`arn:aws:inspector:us-west-2:123456789012:target/0-0kFIPusq/template/0-4r1V2mAw/run/0-MKkpXXPE`:`aws inspector get-telemetry-metadata --assessment-run-arn``arn:aws:inspector:us-west-2:123456789012:target/0-0kFIPusq/template/0-4r1V2mAw/run/0-MKkpXXPE`Output: `{ "telemetryMetadata": [ { "count": 2, "dataSize": 345, "messageType": "InspectorDuplicateProcess" }, { "count": 3, "dataSize": 255, "messageType": "InspectorTimeEventMsg" }, { "count": 4, "dataSize": 1082, "messageType": "InspectorNetworkInterface" }, { "count": 2, "dataSize": 349, "messageType": "InspectorDnsEntry" }, { "count": 11, "dataSize": 2514, "messageType": "InspectorDirectoryInfoMsg" }, { "count": 1, "dataSize": 179, "messageType": "InspectorTcpV6ListeningPort" }, { "count": 101, "dataSize": 10949, "messageType": "InspectorTerminal" }, { "count": 26, "dataSize": 5916, "messageType": "InspectorUser" }, { "count": 282, "dataSize": 32148, "messageType": "InspectorDynamicallyLoadedCodeModule" }, { "count": 18, "dataSize": 10172, "messageType": "InspectorCreateProcess" }, { "count": 3, "dataSize": 8001, "messageType": "InspectorProcessPerformance" }, { "count": 1, "dataSize": 360, "messageType": "InspectorOperatingSystem" }, { "count": 6, "dataSize": 546, "messageType": "InspectorStopProcess" }, { "count": 1, "dataSize": 1553, "messageType": "InspectorInstanceMetaData" }, { "count": 2, "dataSize": 434, "messageType": "InspectorTcpV4Connection" }, { "count": 474, "dataSize": 2960322, "messageType": "InspectorPackageInfo" }, { "count": 3, "dataSize": 2235, "messageType": "InspectorSystemPerformance" }, { "count": 105, "dataSize": 46048, "messageType": "InspectorCodeModule" }, { "count": 1, "dataSize": 182, "messageType": "InspectorUdpV6ListeningPort" }, { "count": 2, "dataSize": 371, "messageType": "InspectorUdpV4ListeningPort" }, { "count": 18, "dataSize": 8362, "messageType": "InspectorKernelModule" }, { "count": 29, "dataSize": 48788, "messageType": "InspectorConfigurationInfo" }, { "count": 1, "dataSize": 79, "messageType": "InspectorMonitoringStart" }, { "count": 5, "dataSize": 0, "messageType": "InspectorSplitMsgBegin" }, { "count": 51, "dataSize": 4593, "messageType": "InspectorGroup" }, { "count": 1, "dataSize": 184, "messageType": "InspectorTcpV4ListeningPort" }, { "count": 1159, "dataSize": 3146579, "messageType": "Total" }, { "count": 5, "dataSize": 0, "messageType": "InspectorSplitMsgEnd" }, { "count": 1, "dataSize": 612, "messageType": "InspectorLoadImageInProcess" } ] }`- 
                    For API details, see [GetTelemetryMetadata](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/inspector/get-telemetry-metadata.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `list-account-permissions`.

- **AWS CLI**
- 
            
                    **To list account permissions**The following `list-account-permissions`example lists your account permissions.`aws inspector2 list-account-permissions`Output: `{ "permissions": [ { "operation": "ENABLE_SCANNING", "service": "ECR" }, { "operation": "DISABLE_SCANNING", "service": "ECR" }, { "operation": "ENABLE_REPOSITORY", "service": "ECR" }, { "operation": "DISABLE_REPOSITORY", "service": "ECR" }, { "operation": "ENABLE_SCANNING", "service": "EC2" }, { "operation": "DISABLE_SCANNING", "service": "EC2" }, { "operation": "ENABLE_SCANNING", "service": "LAMBDA" }, { "operation": "DISABLE_SCANNING", "service": "LAMBDA" } ] }`For more information, see [Identity and Access Management for Amazon Inspector](https://docs.aws.amazon.com/inspector/latest/user/security-iam.html)in the*Amazon Inspector User Guide*.- 
                    For API details, see [ListAccountPermissions](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/inspector2/list-account-permissions.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `list-assessment-run-agents`.

- **AWS CLI**
- 
            
                    **To list assessment run agents**The following `list-assessment-run-agents`command lists the agents of the assessment run with the specified ARN.`aws inspector list-assessment-run-agents \ --assessment-run-arn``arn:aws:inspector:us-west-2:123456789012:target/0-0kFIPusq/template/0-4r1V2mAw/run/0-MKkpXXPE`Output: `{ "assessmentRunAgents": [ { "agentHealth": "HEALTHY", "agentHealthCode": "HEALTHY", "agentId": "i-49113b93", "assessmentRunArn": "arn:aws:inspector:us-west-2:123456789012:target/0-0kFIPusq/template/0-4r1V2mAw/run/0-MKkpXXPE", "telemetryMetadata": [ { "count": 2, "dataSize": 345, "messageType": "InspectorDuplicateProcess" }, { "count": 3, "dataSize": 255, "messageType": "InspectorTimeEventMsg" }, { "count": 4, "dataSize": 1082, "messageType": "InspectorNetworkInterface" }, { "count": 2, "dataSize": 349, "messageType": "InspectorDnsEntry" }, { "count": 11, "dataSize": 2514, "messageType": "InspectorDirectoryInfoMsg" }, { "count": 1, "dataSize": 179, "messageType": "InspectorTcpV6ListeningPort" }, { "count": 101, "dataSize": 10949, "messageType": "InspectorTerminal" }, { "count": 26, "dataSize": 5916, "messageType": "InspectorUser" }, { "count": 282, "dataSize": 32148, "messageType": "InspectorDynamicallyLoadedCodeModule" }, { "count": 18, "dataSize": 10172, "messageType": "InspectorCreateProcess" }, { "count": 3, "dataSize": 8001, "messageType": "InspectorProcessPerformance" }, { "count": 1, "dataSize": 360, "messageType": "InspectorOperatingSystem" }, { "count": 6, "dataSize": 546, "messageType": "InspectorStopProcess" }, { "count": 1, "dataSize": 1553, "messageType": "InspectorInstanceMetaData" }, { "count": 2, "dataSize": 434, "messageType": "InspectorTcpV4Connection" }, { "count": 474, "dataSize": 2960322, "messageType": "InspectorPackageInfo" }, { "count": 3, "dataSize": 2235, "messageType": "InspectorSystemPerformance" }, { "count": 105, "dataSize": 46048, "messageType": "InspectorCodeModule" }, { "count": 1, "dataSize": 182, "messageType": "InspectorUdpV6ListeningPort" }, { "count": 2, "dataSize": 371, "messageType": "InspectorUdpV4ListeningPort" }, { "count": 18, "dataSize": 8362, "messageType": "InspectorKernelModule" }, { "count": 29, "dataSize": 48788, "messageType": "InspectorConfigurationInfo" }, { "count": 1, "dataSize": 79, "messageType": "InspectorMonitoringStart" }, { "count": 5, "dataSize": 0, "messageType": "InspectorSplitMsgBegin" }, { "count": 51, "dataSize": 4593, "messageType": "InspectorGroup" }, { "count": 1, "dataSize": 184, "messageType": "InspectorTcpV4ListeningPort" }, { "count": 1159, "dataSize": 3146579, "messageType": "Total" }, { "count": 5, "dataSize": 0, "messageType": "InspectorSplitMsgEnd" }, { "count": 1, "dataSize": 612, "messageType": "InspectorLoadImageInProcess" } ] } ] }`For more information, see [AWS Agents](https://docs.aws.amazon.com/inspector/latest/userguide/inspector_agents.html)in the*Amazon Inspector User Guide*.- 
                    For API details, see [ListAssessmentRunAgents](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/inspector/list-assessment-run-agents.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `list-assessment-runs`.

- **AWS CLI**
- 
            
                    **To list assessment runs**The following `list-assessment-runs`command lists all existing assessment runs.`aws inspector list-assessment-runs`Output: `{ "assessmentRunArns": [ "arn:aws:inspector:us-west-2:123456789012:target/0-0kFIPusq/template/0-4r1V2mAw/run/0-MKkpXXPE", "arn:aws:inspector:us-west-2:123456789012:target/0-0kFIPusq/template/0-4r1V2mAw/run/0-v5D6fI3v" ] }`For more information, see [Amazon Inspector Assessment Templates and Assessment Runs](https://docs.aws.amazon.com/inspector/latest/userguide/inspector_assessments.html)in the*Amazon Inspector User Guide*.- 
                    For API details, see [ListAssessmentRuns](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/inspector/list-assessment-runs.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `list-assessment-targets`.

- **AWS CLI**
- 
            
                    **To list assessment targets**The following `list-assessment-targets`command lists all existing assessment targets:`aws inspector list-assessment-targets`Output: `{ "assessmentTargetArns": [ "arn:aws:inspector:us-west-2:123456789012:target/0-0kFIPusq" ] }`For more information, see Amazon Inspector Assessment Targets in the *Amazon Inspector*guide.- 
                    For API details, see [ListAssessmentTargets](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/inspector/list-assessment-targets.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `list-assessment-templates`.

- **AWS CLI**
- 
            
                    **To list assessment templates**The following `list-assessment-templates`command lists all existing assessment templates:`aws inspector list-assessment-templates`Output: `{ "assessmentTemplateArns": [ "arn:aws:inspector:us-west-2:123456789012:target/0-0kFIPusq/template/0-4r1V2mAw", "arn:aws:inspector:us-west-2:123456789012:target/0-0kFIPusq/template/0-Uza6ihLh" ] }`For more information, see Amazon Inspector Assessment Templates and Assessment Runs in the *Amazon Inspector*guide.- 
                    For API details, see [ListAssessmentTemplates](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/inspector/list-assessment-templates.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `list-coverage-statistics`.

- **AWS CLI**
- 
            
                    **Example 1: To list coverage statistics by groups**The following `list-coverage-statistics`example lists the coverage statistics of your AWS environment by groups.`aws inspector2 list-coverage-statistics \ --group-by``RESOURCE_TYPE`Output: `{ "countsByGroup": [ { "count": 56, "groupKey": "AWS_LAMBDA_FUNCTION" }, { "count": 27, "groupKey": "AWS_ECR_REPOSITORY" }, { "count": 18, "groupKey": "AWS_EC2_INSTANCE" }, { "count": 3, "groupKey": "AWS_ECR_CONTAINER_IMAGE" }, { "count": 1, "groupKey": "AWS_ACCOUNT" } ], "totalCounts": 105 }`For more information, see [Assessing Amazon Inspector coverage of your AWS environment](https://docs.aws.amazon.com/inspector/latest/user/assessing-coverage.html)in the*Amazon Inspector User Guide*.**Example 2: To list coverage statistics by resource type**The following `list-coverage-statistics`example lists the coverage statistics of your AWS environment by resource type.`aws inspector2 list-coverage-statistics --filter-criteria '``{"resourceType":[{"comparison":"EQUALS","value":"AWS_ECR_REPOSITORY"}]}`' --group-by`SCAN_STATUS_REASON`Output: `{ "countsByGroup": [ { "count": 27, "groupKey": "SUCCESSFUL" } ], "totalCounts": 27 }`For more information, see [Assessing Amazon Inspector coverage of your AWS environment](https://docs.aws.amazon.com/inspector/latest/user/assessing-coverage.html)in the*Amazon Inspector User Guide*.**Example 3: To list coverage statistics by ECR repository name**The following `list-coverage-statistics`example lists the coverage statistics of your AWS environment by ECR repository name.`aws inspector2 list-coverage-statistics --filter-criteria '``{"ecrRepositoryName":[{"comparison":"EQUALS","value":"debian"}]}`' --group-by`SCAN_STATUS_REASON`Output: `{ "countsByGroup": [ { "count": 3, "groupKey": "SUCCESSFUL" } ], "totalCounts": 3 }`For more information, see [Assessing Amazon Inspector coverage of your AWS environment](https://docs.aws.amazon.com/inspector/latest/user/assessing-coverage.html)in the*Amazon Inspector User Guide*.- 
                    For API details, see [ListCoverageStatistics](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/inspector2/list-coverage-statistics.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `list-coverage`.

- **AWS CLI**
- 
            
                    **Example 1: To list coverage details about your environment**The following `list-coverage`example lists your environment's coverage details.`aws inspector2 list-coverage`Output: `{ "coveredResources": [ { "accountId": "123456789012", "lastScannedAt": "2024-05-20T16:23:20-07:00", "resourceId": "i-EXAMPLE55555555555", "resourceMetadata": { "ec2": { "amiId": "ami-EXAMPLE6666666666", "platform": "LINUX" } }, "resourceType": "AWS_EC2_INSTANCE", "scanStatus": { "reason": "SUCCESSFUL", "statusCode": "ACTIVE" }, "scanType": "PACKAGE" } ] }`**Example 2: To list coverage details about the Lambda function resource type**The following `list-coverage`example lists your Lambda function resource type details.`aws inspector2 list-coverage --filter-criteria '``{"resourceType":[{"comparison":"EQUALS","value":"AWS_LAMBDA_FUNCTION"}]}`'Output: `{ "coveredResources": [ { "accountId": "123456789012", "resourceId": "arn:aws:lambda:us-west-2:123456789012:function:Eval-container-scan-results:$LATEST", "resourceMetadata": { "lambdaFunction": { "functionName": "Eval-container-scan-results", "functionTags": {}, "layers": [], "runtime": "PYTHON_3_7" } }, "resourceType": "AWS_LAMBDA_FUNCTION", "scanStatus": { "reason": "SUCCESSFUL", "statusCode": "ACTIVE" }, "scanType": "CODE" } ] }`- 
                    For API details, see [ListCoverage](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/inspector2/list-coverage.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `list-delegated-admin-accounts`.

- **AWS CLI**
- 
            
                    **To list information about the delegated administrator account of your organization**The following `list-delegated-admin-accounts`example lists information about the delegated administrator account of your organization.`aws inspector2 list-delegated-admin-accounts`Output: `{ "delegatedAdminAccounts": [ { "accountId": "123456789012", "status": "ENABLED" } ] }`For more information, see [Designating a delegated administrator for Amazon Inspector](https://docs.aws.amazon.com/inspector/latest/user/admin-member-relationship.html)in the*Amazon Inspector User Guide*.- 
                    For API details, see [ListDelegatedAdminAccounts](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/inspector2/list-delegated-admin-accounts.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `list-event-subscriptions`.

- **AWS CLI**
- 
            
                    **To list event subscriptions**The following `list-event-subscriptions`command lists all the event subscriptions for the assessment template with the ARN of`arn:aws:inspector:us-west-2:123456789012:target/0-nvgVhaxX/template/0-7sbz2Kz0`:`aws inspector list-event-subscriptions --resource-arn``arn:aws:inspector:us-west-2:123456789012:target/0-nvgVhaxX/template/0-7sbz2Kz0`Output: `{ "subscriptions": [ { "eventSubscriptions": [ { "event": "ASSESSMENT_RUN_COMPLETED", "subscribedAt": 1459455440.867 } ], "resourceArn": "arn:aws:inspector:us-west-2:123456789012:target/0-nvgVhaxX/template/0-7sbz2Kz0", "topicArn": "arn:aws:sns:us-west-2:123456789012:exampletopic" } ] }`For more information, see Amazon Inspector Assessment Templates and Assessment Runs in the *Amazon Inspector*guide.- 
                    For API details, see [ListEventSubscriptions](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/inspector/list-event-subscriptions.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `list-filters`.

- **AWS CLI**
- 
            
                    **To list filters associated with the account that you used to activated Amazon Inspector**The following `list-filters`examples lists filters associated with the account that you used to activated Amazon Inspector.`aws inspector2 list-filters`Output: `{ "filters": [ { "action": "SUPPRESS", "arn": "arn:aws:inspector2:us-west-2:123456789012:owner/o-EXAMPLE222/filter/EXAMPLE444444444", "createdAt": "2024-05-15T21:11:08.602000+00:00", "criteria": { "resourceType": [ { "comparison": "EQUALS", "value": "AWS_EC2_INSTANCE" }, ] }, "description": "This suppression rule omits EC2 instance type findings", "name": "ExampleSuppressionRuleEC2", "ownerId": "o-EXAMPLE222", "tags": {}, "updatedAt": "2024-05-15T21:11:08.602000+00:00" }, { "action": "SUPPRESS", "arn": "arn:aws:inspector2:us-east-1:813737243517:owner/o-EXAMPLE222/filter/EXAMPLE444444444", "createdAt": "2024-05-15T21:28:27.054000+00:00", "criteria": { "resourceType": [ { "comparison": "EQUALS", "value": "AWS_ECR_INSTANCE" } ] }, "description": "This suppression rule omits ECR instance type findings", "name": "ExampleSuppressionRuleECR", "ownerId": "o-EXAMPLE222", "tags": {}, "updatedAt": "2024-05-15T21:28:27.054000+00:00" } ] }`For more information, see [Filtering Amazon Inspector findings](https://docs.aws.amazon.com/inspector/latest/user/findings-managing-filtering.html)in the*Amazon Inspector User Guide*.- 
                    For API details, see [ListFilters](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/inspector2/list-filters.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `list-findings`.

- **AWS CLI**
- 
            
                    **To list findings**The following `list-findings`command lists all of the generated findings:`aws inspector list-findings`Output: `{ "findingArns": [ "arn:aws:inspector:us-west-2:123456789012:target/0-0kFIPusq/template/0-4r1V2mAw/run/0-MKkpXXPE/finding/0-HwPnsDm4", "arn:aws:inspector:us-west-2:123456789012:target/0-0kFIPusq/template/0-4r1V2mAw/run/0-v5D6fI3v/finding/0-tyvmqBLy" ] }`For more information, see Amazon Inspector Findings in the *Amazon Inspector*guide.- 
                    For API details, see [ListFindings](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/inspector/list-findings.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `list-members`.

- **AWS CLI**
- 
            
                    **Example 1: To list all member accounts associated with the Amazon Inspector delegated administrator for your organization**aws inspector2 list-members --only-associated Output: `{ { "members": [ { "accountId": "123456789012", "delegatedAdminAccountId": "123456789012", "relationshipStatus": "ENABLED", "updatedAt": "2023-09-11T09:57:20.520000-07:00" }, { "accountId": "123456789012", "delegatedAdminAccountId": "123456789012", "relationshipStatus": "ENABLED", "updatedAt": "2024-08-12T10:13:01.472000-07:00" }, { "accountId": "625032911453", "delegatedAdminAccountId": "123456789012", "relationshipStatus": "ENABLED", "updatedAt": "2023-09-11T09:57:20.438000-07:00" }, { "accountId": "715411239211", "delegatedAdminAccountId": "123456789012", "relationshipStatus": "ENABLED", "updatedAt": "2024-04-24T09:14:57.471000-07:00" } ] }`For more information, see [Managing multiple accounts in Amazon Inspector with AWS Organizations](https://docs.aws.amazon.com/inspector/latest/user/managing-multiple-accounts.html)in the*Amazon Inspector User Guide*.**Example 2: To list all member accounts associated with and disassociated from the Amazon Inspector delegated administrator for your organization**aws inspector2 list-members --no-only-associated Output: `{ { "members": [ { "accountId": "123456789012", "delegatedAdminAccountId": "123456789012", "relationshipStatus": "REMOVED", "updatedAt": "2024-05-15T11:34:53.326000-07:00" }, { "accountId": "123456789012", "delegatedAdminAccountId": "123456789012", "relationshipStatus": "ENABLED", "updatedAt": "2023-09-11T09:57:20.520000-07:00" }, { "accountId": "123456789012", "delegatedAdminAccountId": "123456789012", "relationshipStatus": "ENABLED", "updatedAt": "2024-08-12T10:13:01.472000-07:00" }, { "accountId": "123456789012", "delegatedAdminAccountId": "123456789012", "relationshipStatus": "ENABLED", "updatedAt": "2023-09-11T09:57:20.438000-07:00" }, { "accountId": "123456789012", "delegatedAdminAccountId": "123456789012", "relationshipStatus": "ENABLED", "updatedAt": "2024-04-24T09:14:57.471000-07:00" } ] }`For more information, see [Managing multiple accounts in Amazon Inspector with AWS Organizations](https://docs.aws.amazon.com/inspector/latest/user/managing-multiple-accounts.html)in the*Amazon Inspector User Guide*.- 
                    For API details, see [ListMembers](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/inspector2/list-members.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `list-rules-packages`.

- **AWS CLI**
- 
            
                    **To list rules packages**The following `list-rules-packages`command lists all available Inspector rules packages:`aws inspector list-rules-packages`Output: `{ "rulesPackageArns": [ "arn:aws:inspector:us-west-2:758058086616:rulespackage/0-9hgA516p", "arn:aws:inspector:us-west-2:758058086616:rulespackage/0-H5hpSawc", "arn:aws:inspector:us-west-2:758058086616:rulespackage/0-JJOtZiqQ", "arn:aws:inspector:us-west-2:758058086616:rulespackage/0-vg5GGHSD" ] }`For more information, see Amazon Inspector Rules Packages and Rules in the *Amazon Inspector*guide.- 
                    For API details, see [ListRulesPackages](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/inspector/list-rules-packages.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `list-tags-for-resource`.

- **AWS CLI**
- 
            
                    **To list tags for resource**The following `list-tags-for-resource`command lists all tags associated with the assessment template with the ARN of`arn:aws:inspector:us-west-2:123456789012:target/0-0kFIPusq/template/0-gcwFliYu`:`aws inspector list-tags-for-resource --resource-arn``arn:aws:inspector:us-west-2:123456789012:target/0-0kFIPusq/template/0-gcwFliYu`Output: `{ "tags": [ { "key": "Name", "value": "Example" } ] }`For more information, see Amazon Inspector Assessment Templates and Assessment Runs in the *Amazon Inspector*guide.- 
                    For API details, see [ListTagsForResource](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/inspector/list-tags-for-resource.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `list-usage-totals`.

- **AWS CLI**
- 
            
                    **To list usage totals over the last 30 days**The following `list-usage-totals`examples lists usage totals over the last 30 days.`aws inspector2 list-usage-totals`Output: `{ "totals": [ { "accountId": "123456789012", "usage": [ { "currency": "USD", "estimatedMonthlyCost": 4.6022044647, "total": 1893.4784083333334, "type": "EC2_AGENTLESS_INSTANCE_HOURS" }, { "currency": "USD", "estimatedMonthlyCost": 18.892449279, "total": 10882.050784722222, "type": "EC2_INSTANCE_HOURS" }, { "currency": "USD", "estimatedMonthlyCost": 5.4525363736, "total": 6543.043648333333, "type": "LAMBDA_FUNCTION_CODE_HOURS" }, { "currency": "USD", "estimatedMonthlyCost": 3.9064080309, "total": 9375.379274166668, "type": "LAMBDA_FUNCTION_HOURS" }, { "currency": "USD", "estimatedMonthlyCost": 0.06, "total": 6.0, "type": "ECR_RESCAN" }, { "currency": "USD", "estimatedMonthlyCost": 0.09, "total": 1.0, "type": "ECR_INITIAL_SCAN" } ] } ] }`For more information, see [Monitoring usage and cost in Amazon Inspector](https://docs.aws.amazon.com/inspector/latest/user/usage.html)in the*Amazon Inspector User Guide*.- 
                    For API details, see [ListUsageTotals](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/inspector2/list-usage-totals.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `preview-agents`.

- **AWS CLI**
- 
            
                    **To preview agents**The following `preview-agents`command previews the agents installed on the EC2 instances that are part of the assessment target with the ARN of`arn:aws:inspector:us-west-2:123456789012:target/0-0kFIPusq`:`aws inspector preview-agents --preview-agents-arn``arn:aws:inspector:us-west-2:123456789012:target/0-0kFIPusq`Output: `{ "agentPreviews": [ { "agentId": "i-49113b93" } ] }`For more information, see Amazon Inspector Assessment Targets in the *Amazon Inspector*guide.- 
                    For API details, see [PreviewAgents](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/inspector/preview-agents.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `register-cross-account-access-role`.

- **AWS CLI**
- 
            
                    **To register the cross account access role**The following `register-cross-account-access-role`command registers the IAM role with the ARN of`arn:aws:iam::123456789012:role/inspector`that Amazon Inspector uses to list your EC2 instances at the start of the assessment run of when you call the preview-agents command:`aws inspector register-cross-account-access-role --role-arn``arn:aws:iam::123456789012:role/inspector`For more information, see Setting up Amazon Inspector in the *Amazon Inspector*guide.- 
                    For API details, see [RegisterCrossAccountAccessRole](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/inspector/register-cross-account-access-role.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `remove-attributes-from-findings`.

- **AWS CLI**
- 
            
                    **To remove attributes from findings**The following `remove-attributes-from-finding`command removes the attribute with the key of`Example`and value of`example`from the finding with the ARN of`arn:aws:inspector:us-west-2:123456789012:target/0-0kFIPusq/template/0-8l1VIE0D/run/0-Z02cjjug/finding/0-T8yM9mEU`:`aws inspector remove-attributes-from-findings --finding-arns``arn:aws:inspector:us-west-2:123456789012:target/0-0kFIPusq/template/0-8l1VIE0D/run/0-Z02cjjug/finding/0-T8yM9mEU`--attribute-keys`key=Example,value=example`Output: `{ "failedItems": {} }`For more information, see Amazon Inspector Findings in the *Amazon Inspector*guide.- 
                    For API details, see [RemoveAttributesFromFindings](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/inspector/remove-attributes-from-findings.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `set-tags-for-resource`.

- **AWS CLI**
- 
            
                    **To set tags for a resource**The following `set-tags-for-resource`command sets the tag with the key of`Example`and value of`example`to the assessment template with the ARN of`arn:aws:inspector:us-west-2:123456789012:target/0-nvgVhaxX/template/0-7sbz2Kz0`:`aws inspector set-tags-for-resource --resource-arn``arn:aws:inspector:us-west-2:123456789012:target/0-nvgVhaxX/template/0-7sbz2Kz0`--tags`key=Example,value=example`For more information, see Amazon Inspector Assessment Templates and Assessment Runs in the *Amazon Inspector*guide.- 
                    For API details, see [SetTagsForResource](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/inspector/set-tags-for-resource.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `start-assessment-run`.

- **AWS CLI**
- 
            
                    **To start an assessment run**The following `start-assessment-run`command starts the assessment run named`examplerun`using the assessment template with the ARN of`arn:aws:inspector:us-west-2:123456789012:target/0-nvgVhaxX/template/0-it5r2S4T`:`aws inspector start-assessment-run --assessment-run-name``examplerun`--assessment-template-arn`arn:aws:inspector:us-west-2:123456789012:target/0-nvgVhaxX/template/0-it5r2S4T`Output: `{ "assessmentRunArn": "arn:aws:inspector:us-west-2:123456789012:target/0-nvgVhaxX/template/0-it5r2S4T/run/0-jOoroxyY" }`For more information, see Amazon Inspector Assessment Templates and Assessment Runs in the *Amazon Inspector*guide.- 
                    For API details, see [StartAssessmentRun](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/inspector/start-assessment-run.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `stop-assessment-run`.

- **AWS CLI**
- 
            
                    **To stop an assessment run**The following `stop-assessment-run`command stops the assessment run with the ARN of`arn:aws:inspector:us-west-2:123456789012:target/0-nvgVhaxX/template/0-it5r2S4T/run/0-jOoroxyY`:`aws inspector stop-assessment-run --assessment-run-arn``arn:aws:inspector:us-west-2:123456789012:target/0-nvgVhaxX/template/0-it5r2S4T/run/0-jOoroxyY`For more information, see Amazon Inspector Assessment Templates and Assessment Runs in the *Amazon Inspector*guide.- 
                    For API details, see [StopAssessmentRun](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/inspector/stop-assessment-run.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `subscribe-to-event`.

- **AWS CLI**
- 
            
                    **To subscribe to an event**The following example enables the process of sending Amazon SNS notifications about the `ASSESSMENT_RUN_COMPLETED`event to the topic with the ARN of`arn:aws:sns:us-west-2:123456789012:exampletopic``aws inspector subscribe-to-event \ --event``ASSESSMENT_RUN_COMPLETED`\ --resource-arn`arn:aws:inspector:us-west-2:123456789012:target/0-nvgVhaxX/template/0-7sbz2Kz0`\ --topic-arn`arn:aws:sns:us-west-2:123456789012:exampletopic`This command produces no output. For more information, see [Amazon Inspector Assessment Templates and Assessment Runs](https://docs.aws.amazon.com/inspector/latest/userguide/inspector_assessments.html)in the*Amazon Inspector*guide.- 
                    For API details, see [SubscribeToEvent](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/inspector/subscribe-to-event.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `unsubscribe-from-event`.

- **AWS CLI**
- 
            
                    **To unsubscribe from an event**The following `unsubscribe-from-event`command disables the process of sending Amazon SNS notifications about the`ASSESSMENT_RUN_COMPLETED`event to the topic with the ARN of`arn:aws:sns:us-west-2:123456789012:exampletopic`:`aws inspector unsubscribe-from-event --event``ASSESSMENT_RUN_COMPLETED`--resource-arn`arn:aws:inspector:us-west-2:123456789012:target/0-nvgVhaxX/template/0-7sbz2Kz0`--topic`arn:aws:sns:us-west-2:123456789012:exampletopic`For more information, see Amazon Inspector Assessment Templates and Assessment Runs in the *Amazon Inspector*guide.- 
                    For API details, see [UnsubscribeFromEvent](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/inspector/unsubscribe-from-event.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `update-assessment-target`.

- **AWS CLI**
- 
            
                    **To update an assessment target**The following `update-assessment-target`command updates the assessment target with the ARN of`arn:aws:inspector:us-west-2:123456789012:target/0-nvgVhaxX`and the name of`Example`, and the resource group with the ARN of`arn:aws:inspector:us-west-2:123456789012:resourcegroup/0-yNbgL5Pt`:`aws inspector update-assessment-target --assessment-target-arn``arn:aws:inspector:us-west-2:123456789012:target/0-nvgVhaxX`--assessment-target-name`Example`--resource-group-arn`arn:aws:inspector:us-west-2:123456789012:resourcegroup/0-yNbgL5Pt`For more information, see Amazon Inspector Assessment Targets in the *Amazon Inspector*guide.- 
                    For API details, see [UpdateAssessmentTarget](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/inspector/update-assessment-target.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `update-filter`.

- **AWS CLI**
- 
            
                    **To update a filter**The following `update-filter`example updates a filter to omit Lambda findings instead of ECR instance findings.`aws inspector2 update-filter \ --filter-arn``"arn:aws:inspector2:us-west-2:123456789012:owner/o-EXAMPLE222/filter/EXAMPLE444444444"`\ --name`"ExampleSuppressionRuleLambda"`\ --description`"This suppression rule omits Lambda instance findings"`\ --reason`"Updating filter to omit Lambda instance findings instead of ECR instance findings"`Output: `{ "filters": [ { "action": "SUPPRESS", "arn": "arn:aws:inspector2:us-west-2:123456789012:owner/o-EXAMPLE222/filter/EXAMPLE444444444", "createdAt": "2024-05-15T21:28:27.054000+00:00", "criteria": { "resourceType": [ { "comparison": "EQUALS", "value": "AWS_ECR_INSTANCE" } ] }, "description": "This suppression rule omits Lambda instance findings", "name": "ExampleSuppressionRuleLambda", "ownerId": "o-EXAMPLE222", "reason": "Updating filter to omit Lambda instance findings instead of ECR instance findings", "tags": {}, "updatedAt": "2024-05-15T22:23:13.665000+00:00" } ] }`For more information, see [Managing findings in Amazon Inspector](https://docs.aws.amazon.com/inspector/latest/user/findings-managing.html)in the*Amazon Inspector User Guide*.- 
                    For API details, see [UpdateFilter](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/inspector2/update-filter.html)in*AWS CLI Command Reference*.
 
-