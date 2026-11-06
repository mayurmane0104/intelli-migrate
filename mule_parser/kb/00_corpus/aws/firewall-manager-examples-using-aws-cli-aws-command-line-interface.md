# Firewall Manager examples using AWS CLI - AWS Command Line Interface

**Source:** [https://docs.aws.amazon.com/cli/latest/userguide/cli_fms_code_examples.html](https://docs.aws.amazon.com/cli/latest/userguide/cli_fms_code_examples.html)

---

The following code examples show you how to perform actions and implement common scenarios by using the AWS Command Line Interface with Firewall Manager.

*Actions* are code excerpts from larger programs and must be run in context. While actions show you how to call individual service functions, you can see actions in context in their related scenarios.

Each example includes a link to the complete source code, where you can find instructions on how to set up and run the code in context.

###### Topics

## Actions

    The following code example shows how to use `associate-admin-account`.

- **AWS CLI**
- 
            
                    **To set the Firewall Manager administrator account**The following `associate-admin-account`example sets the administrator account for Firewall Manager.`aws fms associate-admin-account \ --admin-account``123456789012`This command produces no output. For more information, see [Set the AWS Firewall Manager Administrator Account](https://docs.aws.amazon.com/waf/latest/developerguide/enable-integration.html)in the*AWS WAF, AWS Firewall Manager, and AWS Shield Advanced Developer Guide*.- 
                    For API details, see [AssociateAdminAccount](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/fms/associate-admin-account.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `delete-notification-channel`.

- **AWS CLI**
- 
            
                    **To remove the SNS topic information for Firewall Manager logs**The following `delete-notification-channel`example removes the SNS topic information.`aws fms delete-notification-channel`This command produces no output. For more information, see [Configure Amazon SNS Notifications and Amazon CloudWatch Alarms](https://docs.aws.amazon.com/waf/latest/developerguide/get-started-fms-shield-cloudwatch.html)in the*AWS WAF, AWS Firewall Manager, and AWS Shield Advanced Developer Guide*.- 
                    For API details, see [DeleteNotificationChannel](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/fms/delete-notification-channel.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `delete-policy`.

- **AWS CLI**
- 
            
                    **To delete a Firewall Manager policy**The following `delete-policy`example removes the policy with the specified ID, along with all of its resources.`aws fms delete-policy \ --policy-id``a1b2c3d4-5678-90ab-cdef-EXAMPLE11111`\ --delete-all-policy-resourcesThis command produces no output. For more information, see [Working with AWS Firewall Manager Policies](https://docs.aws.amazon.com/waf/latest/developerguide/working-with-policies.html)in the*AWS WAF, AWS Firewall Manager, and AWS Shield Advanced Developer Guide*.- 
                    For API details, see [DeletePolicy](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/fms/delete-policy.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `disassociate-admin-account`.

- **AWS CLI**
- 
            
                    **To remove the Firewall Manager administrator account**The following `disassociate-admin-account`example removes the current administrator account association from Firewall Manager.`aws fms disassociate-admin-account`This command produces no output. For more information, see [Set the AWS Firewall Manager Administrator Account](https://docs.aws.amazon.com/waf/latest/developerguide/enable-integration.html)in the*AWS WAF, AWS Firewall Manager, and AWS Shield Advanced Developer Guide*.- 
                    For API details, see [DisassociateAdminAccount](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/fms/disassociate-admin-account.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `get-admin-account`.

- **AWS CLI**
- 
            
                    **To retrieve the Firewall Manager administrator account**The following `get-admin-account`example retrieves the administrator account.`aws fms get-admin-account`Output: `{ "AdminAccount": "123456789012", "RoleStatus": "READY" }`For more information, see [AWS Firewall Manager Prerequisites](https://docs.aws.amazon.com/waf/latest/developerguide/fms-prereq.html)in the*AWS WAF, AWS Firewall Manager, and AWS Shield Advanced Developer Guide*.- 
                    For API details, see [GetAdminAccount](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/fms/get-admin-account.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `get-compliance-detail`.

- **AWS CLI**
- 
            
                    **To retrieve the compliance information for an account**The following `get-compliance-detail`example retrieves compliance information for the specified policy and member account.`aws fms get-compliance-detail \ --policy-id``a1b2c3d4-5678-90ab-cdef-EXAMPLE11111`\ --member-account`123456789012`Output: `{ "PolicyComplianceDetail": { "EvaluationLimitExceeded": false, "IssueInfoMap": {}, "MemberAccount": "123456789012", "PolicyId": "a1b2c3d4-5678-90ab-cdef-EXAMPLE11111", "PolicyOwner": "123456789012", "Violators": [] }`For more information, see [Viewing Resource Compliance with a Policy](https://docs.aws.amazon.com/waf/latest/developerguide/fms-compliance.html)in the*AWS WAF, AWS Firewall Manager, and AWS Shield Advanced Developer Guide*.- 
                    For API details, see [GetComplianceDetail](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/fms/get-compliance-detail.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `get-notification-channel`.

- **AWS CLI**
- 
            
                    **To retrieve the SNS topic information for Firewall Manager logs**The following `get-notification-channel`example retrieves the SNS topic information.`aws fms get-notification-channel`Output: `{ "SnsTopicArn": "arn:aws:sns:us-west-2:123456789012:us-west-2-fms", "SnsRoleName": "arn:aws:iam::123456789012:role/aws-service-role/fms.amazonaws.com/AWSServiceRoleForFMS" }`For more information, see [Configure Amazon SNS Notifications and Amazon CloudWatch Alarms](https://docs.aws.amazon.com/waf/latest/developerguide/get-started-fms-shield-cloudwatch.html)in the*AWS WAF, AWS Firewall Manager, and AWS Shield Advanced Developer Guide*.- 
                    For API details, see [GetNotificationChannel](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/fms/get-notification-channel.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `get-policy`.

- **AWS CLI**
- 
            
                    **To retrieve a Firewall Manager policy**The following `get-policy`example retrieves the policy with the specified ID.`aws fms get-policy \ --policy-id``a1b2c3d4-5678-90ab-cdef-EXAMPLE11111`Output: `{ "Policy": { "PolicyId": "a1b2c3d4-5678-90ab-cdef-EXAMPLE11111", "PolicyName": "test", "PolicyUpdateToken": "1:p+2RpKR4wPFx7mcrL1UOQQ==", "SecurityServicePolicyData": { "Type": "SECURITY_GROUPS_COMMON", "ManagedServiceData": "{\"type\":\"SECURITY_GROUPS_COMMON\",\"revertManualSecurityGroupChanges\":true,\"exclusiveResourceSecurityGroupManagement\":false,\"securityGroups\":[{\"id\":\"sg-045c43ccc9724e63e\"}]}" }, "ResourceType": "AWS::EC2::Instance", "ResourceTags": [], "ExcludeResourceTags": false, "RemediationEnabled": false }, "PolicyArn": "arn:aws:fms:us-west-2:123456789012:policy/d1ac59b8-938e-42b3-b2e0-7c620422ddc2" }`For more information, see [Working with AWS Firewall Manager Policies](https://docs.aws.amazon.com/waf/latest/developerguide/working-with-policies.html)in the*AWS WAF, AWS Firewall Manager, and AWS Shield Advanced Developer Guide*.- 
                    For API details, see [GetPolicy](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/fms/get-policy.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `list-compliance-status`.

- **AWS CLI**
- 
            
                    **To retrieve the policy compliance information for member accounts**The following `list-compliance-status`example retrieves member account compliance information for the specified policy.`aws fms list-compliance-status \ --policy-id``a1b2c3d4-5678-90ab-cdef-EXAMPLE11111`Output: `{ "PolicyComplianceStatusList": [ { "PolicyOwner": "123456789012", "PolicyId": "a1b2c3d4-5678-90ab-cdef-EXAMPLE11111", "PolicyName": "test", "MemberAccount": "123456789012", "EvaluationResults": [ { "ComplianceStatus": "COMPLIANT", "ViolatorCount": 0, "EvaluationLimitExceeded": false }, { "ComplianceStatus": "NON_COMPLIANT", "ViolatorCount": 2, "EvaluationLimitExceeded": false } ], "LastUpdated": 1576283774.0, "IssueInfoMap": {} } ] }`For more information, see [Viewing Resource Compliance with a Policy](https://docs.aws.amazon.com/waf/latest/developerguide/fms-compliance.html)in the*AWS WAF, AWS Firewall Manager, and AWS Shield Advanced Developer Guide*.- 
                    For API details, see [ListComplianceStatus](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/fms/list-compliance-status.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `list-member-accounts`.

- **AWS CLI**
- 
            
                    **To retrieve the member accounts in the organization**The following `list-member-accounts`example lists all of the member accounts that are in the Firewall Manager administrator's organization.`aws fms list-member-accounts`Output: `{ "MemberAccounts": [ "222222222222", "333333333333", "444444444444" ] }`For more information, see [AWS Firewall Manager](https://docs.aws.amazon.com/waf/latest/developerguide/fms-chapter.html)in the*AWS WAF, AWS Firewall Manager, and AWS Shield Advanced Developer Guide*.- 
                    For API details, see [ListMemberAccounts](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/fms/list-member-accounts.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `list-policies`.

- **AWS CLI**
- 
            
                    **To retrieve all Firewall Manager policies**The following `list-policies`example retrieves the list of policies for the account. In this example, the output is limited to two results per request. Each call returns a`NextToken`that can be used as the value for the`--starting-token`parameter in the next`list-policies`call to get the next set of results for the list.`aws fms list-policies \ --max-items``2`Output: `{ "PolicyList": [ { "PolicyArn": "arn:aws:fms:us-west-2:123456789012:policy/a1b2c3d4-5678-90ab-cdef-EXAMPLE11111", "PolicyId": "a1b2c3d4-5678-90ab-cdef-EXAMPLE11111", "PolicyName": "test", "ResourceType": "AWS::EC2::Instance", "SecurityServiceType": "SECURITY_GROUPS_COMMON", "RemediationEnabled": false }, { "PolicyArn": "arn:aws:fms:us-west-2:123456789012:policy/a1b2c3d4-5678-90ab-cdef-EXAMPLE22222", "PolicyId": "457c9b21-fc94-406c-ae63-21217395ba72", "PolicyName": "test", "ResourceType": "AWS::EC2::Instance", "SecurityServiceType": "SECURITY_GROUPS_COMMON", "RemediationEnabled": false } ], "NextToken": "eyJOZXh0VG9rZW4iOiBudWxsLCAiYm90b190cnVuY2F0ZV9hbW91bnQiOiAyfQ==" }`For more information, see [Working with AWS Firewall Manager Policies](https://docs.aws.amazon.com/waf/latest/developerguide/working-with-policies.html)in the*AWS WAF, AWS Firewall Manager, and AWS Shield Advanced Developer Guide*.- 
                    For API details, see [ListPolicies](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/fms/list-policies.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `put-notification-channel`.

- **AWS CLI**
- 
            
                    **To set the SNS topic information for Firewall Manager logs**The following `put-notification-channel`example sets the SNS topic information.`aws fms put-notification-channel \ --sns-topic-arn``arn:aws:sns:us-west-2:123456789012:us-west-2-fms`\ --sns-role-name`arn:aws:iam::123456789012:role/aws-service-role/fms.amazonaws.com/AWSServiceRoleForFMS`This command produces no output. For more information, see [Configure Amazon SNS Notifications and Amazon CloudWatch Alarms](https://docs.aws.amazon.com/waf/latest/developerguide/get-started-fms-shield-cloudwatch.html)in the*AWS WAF, AWS Firewall Manager, and AWS Shield Advanced Developer Guide*.- 
                    For API details, see [PutNotificationChannel](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/fms/put-notification-channel.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `put-policy`.

- **AWS CLI**
- 
            
                    **To create a Firewall Manager policy**The following `put-policy`example creates a Firewall Manager security group policy.`aws fms put-policy \ --cli-input-json``file://policy.json`Contents of `policy.json`:`{ "Policy": { "PolicyName": "test", "SecurityServicePolicyData": { "Type": "SECURITY_GROUPS_USAGE_AUDIT", "ManagedServiceData": "{\"type\":\"SECURITY_GROUPS_USAGE_AUDIT\",\"deleteUnusedSecurityGroups\":false,\"coalesceRedundantSecurityGroups\":true}" }, "ResourceType": "AWS::EC2::SecurityGroup", "ResourceTags": [], "ExcludeResourceTags": false, "RemediationEnabled": false }, "TagList": [ { "Key": "foo", "Value": "foo" } ] }`Output: `{ "Policy": { "PolicyId": "a1b2c3d4-5678-90ab-cdef-EXAMPLE11111", "PolicyName": "test", "PolicyUpdateToken": "1:X9QGexP7HASDlsFp+G31Iw==", "SecurityServicePolicyData": { "Type": "SECURITY_GROUPS_USAGE_AUDIT", "ManagedServiceData": "{\"type\":\"SECURITY_GROUPS_USAGE_AUDIT\",\"deleteUnusedSecurityGroups\":false,\"coalesceRedundantSecurityGroups\":true,\"optionalDelayForUnusedInMinutes\":null}" }, "ResourceType": "AWS::EC2::SecurityGroup", "ResourceTags": [], "ExcludeResourceTags": false, "RemediationEnabled": false }, "PolicyArn": "arn:aws:fms:us-west-2:123456789012:policy/a1b2c3d4-5678-90ab-cdef-EXAMPLE11111" }`For more information, see [Working with AWS Firewall Manager Policies](https://docs.aws.amazon.com/waf/latest/developerguide/working-with-policies.html)in the*AWS WAF, AWS Firewall Manager, and AWS Shield Advanced Developer Guide*.- 
                    For API details, see [PutPolicy](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/fms/put-policy.html)in*AWS CLI Command Reference*.
 
-