# Shield examples using AWS CLI - AWS Command Line Interface

**Source:** [https://docs.aws.amazon.com/cli/latest/userguide/cli_shield_code_examples.html](https://docs.aws.amazon.com/cli/latest/userguide/cli_shield_code_examples.html)

---

The following code examples show you how to perform actions and implement common scenarios by using the AWS Command Line Interface with Shield.

*Actions* are code excerpts from larger programs and must be run in context. While actions show you how to call individual service functions, you can see actions in context in their related scenarios.

Each example includes a link to the complete source code, where you can find instructions on how to set up and run the code in context.

###### Topics

## Actions

    The following code example shows how to use `associate-drt-log-bucket`.

- **AWS CLI**
- 
            
                    **To authorize the DRT to access an Amazon S3 bucket**The following `associate-drt-log-bucket`example creates an association between the DRT and the specified S3 bucket. This permits the DRT to access the bucket on behalf of the account.:`aws shield associate-drt-log-bucket \ --log-bucket``flow-logs-for-website-lb`This command produces no output. For more information, see [Authorize the DDoS Response Team](https://docs.aws.amazon.com/waf/latest/developerguide/authorize-DRT.html)in the*AWS Shield Advanced Developer Guide*.- 
                    For API details, see [AssociateDrtLogBucket](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/shield/associate-drt-log-bucket.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `associate-drt-role`.

- **AWS CLI**
- 
            
                    **To authorize the DRT to mitigate potential attacks on your behalf**The following `associate-drt-role`example creates an association between the DRT and the specified role. The DRT can use the role to access and manage the account.`aws shield associate-drt-role \ --role-arn``arn:aws:iam::123456789012:role/service-role/DrtRole`This command produces no output. For more information, see [Authorize the DDoS Response Team](https://docs.aws.amazon.com/waf/latest/developerguide/authorize-DRT.html)in the*AWS Shield Advanced Developer Guide*.- 
                    For API details, see [AssociateDrtRole](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/shield/associate-drt-role.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `create-protection`.

- **AWS CLI**
- 
            
                    **To enable AWS Shield Advanced protection for a single AWS resource**The following `create-protection`example enables Shield Advanced protection for the specified AWS CloudFront distribution.`aws shield create-protection \ --name``"Protection for CloudFront distribution"`\ --resource-arn`arn:aws:cloudfront::123456789012:distribution/E198WC25FXOWY8`Output: `{ "ProtectionId": "a1b2c3d4-5678-90ab-cdef-EXAMPLE11111" }`For more information, see [Specify Your Resources to Protect](https://docs.aws.amazon.com/waf/latest/developerguide/ddos-choose-resources.html)in the*AWS Shield Advanced Developer Guide*.- 
                    For API details, see [CreateProtection](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/shield/create-protection.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `create-subscription`.

- **AWS CLI**
- 
            
                    **To enable AWS Shield Advanced protection for an account**The following `create-subscription`example enables Shield Advanced protection for the account.`aws shield create-subscription`This command produces no output. For more information, see [Getting Started with AWS Shield Advanced](https://docs.aws.amazon.com/waf/latest/developerguide/getting-started-ddos.html)in the*AWS Shield Advanced Developer Guide*.- 
                    For API details, see [CreateSubscription](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/shield/create-subscription.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `delete-protection`.

- **AWS CLI**
- 
            
                    **To remove AWS Shield Advanced protection from an AWS resource**The following `delete-protection`example removes the specified AWS Shield Advanced protection.`aws shield delete-protection \ --protection-id``a1b2c3d4-5678-90ab-cdef-EXAMPLE11111`This command produces no output. For more information, see [Removing AWS Shield Advanced from an AWS Resource](https://docs.aws.amazon.com/waf/latest/developerguide/remove-protection.html)in the*AWS Shield Advanced Developer Guide*.- 
                    For API details, see [DeleteProtection](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/shield/delete-protection.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `describe-attack`.

- **AWS CLI**
- 
            
                    **To retrieve a detailed description of an attack**The following `describe-attack`example displays details about the DDoS attack with the specified attack ID. You can obtain attack IDs by running the`list-attacks`command.`aws shield describe-attack --attack-id``a1b2c3d4-5678-90ab-cdef-EXAMPLE22222`Output: `{ "Attack": { "AttackId": "a1b2c3d4-5678-90ab-cdef-EXAMPLE22222", "ResourceArn": "arn:aws:elasticloadbalancing:us-west-2:123456789012:loadbalancer/testElb", "SubResources": [ { "Type": "IP", "Id": "192.0.2.2", "AttackVectors": [ { "VectorType": "SYN_FLOOD", "VectorCounters": [ { "Name": "SYN_FLOOD_BPS", "Max": 982184.0, "Average": 982184.0, "Sum": 11786208.0, "N": 12, "Unit": "BPS" } ] } ], "Counters": [] }, { "Type": "IP", "Id": "192.0.2.3", "AttackVectors": [ { "VectorType": "SYN_FLOOD", "VectorCounters": [ { "Name": "SYN_FLOOD_BPS", "Max": 982184.0, "Average": 982184.0, "Sum": 9821840.0, "N": 10, "Unit": "BPS" } ] } ], "Counters": [] }, { "Type": "IP", "Id": "192.0.2.4", "AttackVectors": [ { "VectorType": "SYN_FLOOD", "VectorCounters": [ { "Name": "SYN_FLOOD_BPS", "Max": 982184.0, "Average": 982184.0, "Sum": 7857472.0, "N": 8, "Unit": "BPS" } ] } ], "Counters": [] }, { "Type": "IP", "Id": "192.0.2.5", "AttackVectors": [ { "VectorType": "SYN_FLOOD", "VectorCounters": [ { "Name": "SYN_FLOOD_BPS", "Max": 982184.0, "Average": 982184.0, "Sum": 1964368.0, "N": 2, "Unit": "BPS" } ] } ], "Counters": [] }, { "Type": "IP", "Id": "2001:DB8::bcde:4321:8765:0:0", "AttackVectors": [ { "VectorType": "SYN_FLOOD", "VectorCounters": [ { "Name": "SYN_FLOOD_BPS", "Max": 982184.0, "Average": 982184.0, "Sum": 1964368.0, "N": 2, "Unit": "BPS" } ] } ], "Counters": [] }, { "Type": "IP", "Id": "192.0.2.6", "AttackVectors": [ { "VectorType": "SYN_FLOOD", "VectorCounters": [ { "Name": "SYN_FLOOD_BPS", "Max": 982184.0, "Average": 982184.0, "Sum": 1964368.0, "N": 2, "Unit": "BPS" } ] } ], "Counters": [] } ], "StartTime": 1576024927.457, "EndTime": 1576025647.457, "AttackCounters": [], "AttackProperties": [ { "AttackLayer": "NETWORK", "AttackPropertyIdentifier": "SOURCE_IP_ADDRESS", "TopContributors": [ { "Name": "198.51.100.5", "Value": 2024475682 }, { "Name": "198.51.100.8", "Value": 1311380863 }, { "Name": "203.0.113.4", "Value": 900599855 }, { "Name": "198.51.100.4", "Value": 769417366 }, { "Name": "203.1.113.13", "Value": 757992847 } ], "Unit": "BYTES", "Total": 92773354841 }, { "AttackLayer": "NETWORK", "AttackPropertyIdentifier": "SOURCE_COUNTRY", "TopContributors": [ { "Name": "United States", "Value": 80938161764 }, { "Name": "Brazil", "Value": 9929864330 }, { "Name": "Netherlands", "Value": 1635009446 }, { "Name": "Mexico", "Value": 144832971 }, { "Name": "Japan", "Value": 45369000 } ], "Unit": "BYTES", "Total": 92773354841 }, { "AttackLayer": "NETWORK", "AttackPropertyIdentifier": "SOURCE_ASN", "TopContributors": [ { "Name": "12345", "Value": 74953625841 }, { "Name": "12346", "Value": 4440087595 }, { "Name": "12347", "Value": 1635009446 }, { "Name": "12348", "Value": 1221230000 }, { "Name": "12349", "Value": 1199425294 } ], "Unit": "BYTES", "Total": 92755479921 } ], "Mitigations": [] } }`For more information, see [Reviewing DDoS Incidents](https://docs.aws.amazon.com/waf/latest/developerguide/using-ddos-reports.html)in the*AWS Shield Advanced Developer Guide*.- 
                    For API details, see [DescribeAttack](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/shield/describe-attack.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `describe-drt-access`.

- **AWS CLI**
- 
            
                    **To retrieve a description of the authorizations the DRT has to mitigate attacks on your behalf**The following `describe-drt-access`example retrieves the role and S3 bucket authorizations that the DRT has, which allow it to respond to potential attacks on your behalf.`aws shield describe-drt-access`Output: `{ "RoleArn": "arn:aws:iam::123456789012:role/service-role/DrtRole", "LogBucketList": [ "flow-logs-for-website-lb" ] }`For more information, see [Authorize the DDoS Response Team](https://docs.aws.amazon.com/waf/latest/developerguide/authorize-DRT.html)in the*AWS Shield Advanced Developer Guide*.- 
                    For API details, see [DescribeDrtAccess](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/shield/describe-drt-access.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `describe-emergency-contact-settings`.

- **AWS CLI**
- 
            
                    **To retrieve emergency e-mail addresses that you have on file with the DRT**The following `describe-emergency-contact-settings`example retrieves the e-mail addresses that are on file with the DRT for the account. These are the addresses the DRT should contact when it's responding to a suspected attack.`aws shield describe-emergency-contact-settings`Output: `{ "EmergencyContactList": [ { "EmailAddress": "ops@example.com" }, { "EmailAddress": "ddos-notifications@example.com" } ] }`For more information, see How AWS Shield Works<https://docs.aws.amazon.com/waf/latest/developerguide/ddos-overview.html> in the *AWS Shield Advanced Developer Guide*.- 
                    For API details, see [DescribeEmergencyContactSettings](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/shield/describe-emergency-contact-settings.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `describe-protection`.

- **AWS CLI**
- 
            
                    **To retrieve the details for an AWS Shield Advanced protection**The following `describe-protection`example displays details about the Shield Advanced protection with the specified ID. You can obtain protection IDs by running the`list-protections`command.`aws shield describe-protection \ --protection-id``a1b2c3d4-5678-90ab-cdef-EXAMPLE11111`Output: `{ "Protection": { "Id": "a1b2c3d4-5678-90ab-cdef-EXAMPLE11111", "Name": "1.2.3.4", "ResourceArn": "arn:aws:ec2:us-west-2:123456789012:eip-allocation/eipalloc-0ac1537af40742a6d" } }`For more information, see [Specify Your Resources to Protect](https://docs.aws.amazon.com/waf/latest/developerguide/ddos-choose-resources.html)in the*AWS Shield Advanced Developer Guide*.- 
                    For API details, see [DescribeProtection](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/shield/describe-protection.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `describe-subscription`.

- **AWS CLI**
- 
            
                    **To retrieve the details of the AWS Shield Advanced protection for the account**The following `describe-subscription`example displays details about the Shield Advanced protection provided for the account.:`aws shield describe-subscription`Output: `{ "Subscription": { "StartTime": 1534368978.0, "EndTime": 1597613778.0, "TimeCommitmentInSeconds": 63244800, "AutoRenew": "ENABLED", "Limits": [ { "Type": "GLOBAL_ACCELERATOR", "Max": 1000 }, { "Type": "ROUTE53_HOSTED_ZONE", "Max": 1000 }, { "Type": "CF_DISTRIBUTION", "Max": 1000 }, { "Type": "ELB_LOAD_BALANCER", "Max": 1000 }, { "Type": "EC2_ELASTIC_IP_ALLOCATION", "Max": 1000 } ] } }`For more information, see [How AWS Shield Works](https://docs.aws.amazon.com/waf/latest/developerguide/ddos-overview.html)in the*AWS Shield Advanced Developer Guide*.- 
                    For API details, see [DescribeSubscription](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/shield/describe-subscription.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `disassociate-drt-log-bucket`.

- **AWS CLI**
- 
            
                    **To remove the authorization for DRT to access an Amazon S3 bucket on your behalf**The following `disassociate-drt-log-bucket`example removes the association between the DRT and the specified S3 bucket. After this command completes, the DRT can no longer access the bucket on behalf of the account.`aws shield disassociate-drt-log-bucket \ --log-bucket``flow-logs-for-website-lb`This command produces no output. For more information, see [Authorize the DDoS Response Team](https://docs.aws.amazon.com/waf/latest/developerguide/authorize-DRT.html)in the*AWS Shield Advanced Developer Guide*.- 
                    For API details, see [DisassociateDrtLogBucket](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/shield/disassociate-drt-log-bucket.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `disassociate-drt-role`.

- **AWS CLI**
- 
            
                    **To remove the authorization for DRT to mitigate potential attacks on your behalf**The following `disassociate-drt-role`example removes the association between the DRT and the account. After this call, the DRT can no longer access or manage your account.`aws shield disassociate-drt-role`This command produces no output. For more information, see [Authorize the DDoS Response Team](https://docs.aws.amazon.com/waf/latest/developerguide/authorize-DRT.html)in the*AWS Shield Advanced Developer Guide*.- 
                    For API details, see [DisassociateDrtRole](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/shield/disassociate-drt-role.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `get-subscription-state`.

- **AWS CLI**
- 
            
                    **To retrieve the current state of the account's AWS Shield Advanced subscription**The following `get-subscription-state`example retrieves the state of the Shield Advanced protection for the account.`aws shield get-subscription-state`Output: `{ "SubscriptionState": "ACTIVE" }`For more information, see [How AWS Shield Works](https://docs.aws.amazon.com/waf/latest/developerguide/ddos-overview.html)in the*AWS Shield Advanced Developer Guide*.- 
                    For API details, see [GetSubscriptionState](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/shield/get-subscription-state.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `list-attacks`.

- **AWS CLI**
- 
            
                    **To retrieve attack summaries from AWS Shield Advanced**The following `list-attacks`example retrieves summaries of attacks for the specified AWS CloudFront distribution during the specified time period. The response includes attack IDs that you can provide to the`describe-attack`command for detailed information on an attack.`aws shield list-attacks \ --resource-arns``arn:aws:cloudfront::12345678910:distribution/E1PXMP22ZVFAOR`\ --start-time`FromInclusive=1529280000,ToExclusive=1529300000`Output: `{ "AttackSummaries": [ { "AttackId": "a1b2c3d4-5678-90ab-cdef-EXAMPLE11111", "ResourceArn": "arn:aws:cloudfront::123456789012:distribution/E1PXMP22ZVFAOR", "StartTime": 1529280000.0, "EndTime": 1529449200.0, "AttackVectors": [ { "VectorType": "SYN_FLOOD" } ] } ] }`For more information, see [Reviewing DDoS Incidents](https://docs.aws.amazon.com/waf/latest/developerguide/using-ddos-reports.html)in the*AWS Shield Advanced Developer Guide*.- 
                    For API details, see [ListAttacks](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/shield/list-attacks.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `list-protections`.

- **AWS CLI**
- 
            
                    **To retrieve protection summaries from AWS Shield Advanced**The following `list-protections`example retrieves summaries of the protections that are enabled for the account.`aws shield list-protections`Output: `{ "Protections": [ { "Id": "a1b2c3d4-5678-90ab-cdef-EXAMPLE11111", "Name": "Protection for CloudFront distribution", "ResourceArn": "arn:aws:cloudfront::123456789012:distribution/E198WC25FXOWY8" } ] }`For more information, see [Specify Your Resources to Protect](https://docs.aws.amazon.com/waf/latest/developerguide/ddos-choose-resources.html)in the*AWS Shield Advanced Developer Guide*.- 
                    For API details, see [ListProtections](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/shield/list-protections.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `update-emergency-contact-settings`.

- **AWS CLI**
- 
            
                    **To define the emergency e-mail addresses that are on file with the DRT**The following `update-emergency-contact-settings`example defines two e-mail addresses that the DRT should contact when it's responding to a suspected attack.`aws shield update-emergency-contact-settings \ --emergency-contact-list``EmailAddress=ops@example.com``EmailAddress=ddos-notifications@example.com`This command produces no output. For more information, see [How AWS Shield Works](https://docs.aws.amazon.com/waf/latest/developerguide/ddos-overview.html)in the*AWS Shield Advanced Developer Guide*.- 
                    For API details, see [UpdateEmergencyContactSettings](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/shield/update-emergency-contact-settings.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `update-subscription`.

- **AWS CLI**
- 
            
                    **To modify the account's AWS Shield Advanced subscription**The following `update-subscription`example enables auto-renewal of the AWS Shield Advanced subscription for the account.`aws shield update-subscription \ --auto-renew``ENABLED`This command produces no output. For more information, see [How AWS Shield Works](https://docs.aws.amazon.com/waf/latest/developerguide/ddos-overview.html)in the*AWS Shield Advanced Developer Guide*.- 
                    For API details, see [UpdateSubscription](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/shield/update-subscription.html)in*AWS CLI Command Reference*.
 
-