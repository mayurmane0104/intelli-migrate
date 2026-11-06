# AWS WAFV2 examples using AWS CLI - AWS Command Line Interface

**Source:** [https://docs.aws.amazon.com/cli/latest/userguide/cli_wafv2_code_examples.html](https://docs.aws.amazon.com/cli/latest/userguide/cli_wafv2_code_examples.html)

---

The following code examples show you how to perform actions and implement common scenarios by using the AWS Command Line Interface with AWS WAFV2.

*Actions* are code excerpts from larger programs and must be run in context. While actions show you how to call individual service functions, you can see actions in context in their related scenarios.

Each example includes a link to the complete source code, where you can find instructions on how to set up and run the code in context.

###### Topics

## Actions

    The following code example shows how to use `associate-web-acl`.

- **AWS CLI**
- 
            
                    **To associate a web ACL with a regional AWS resource**The following `associate-web-acl`example associates the specified web ACL with an Application Load Balancer.`aws wafv2 associate-web-acl \ --web-acl-arn``arn:aws:wafv2:us-west-2:123456789012:regional/webacl/test-cli/a1b2c3d4-5678-90ab-cdef-EXAMPLE11111`\ --resource-arn`arn:aws:elasticloadbalancing:us-west-2:123456789012:loadbalancer/app/waf-cli-alb/1ea17125f8b25a2a`\ --region`us-west-2`This command produces no output. For more information, see [Associating or Disassociating a Web ACL with an AWS Resource](https://docs.aws.amazon.com/waf/latest/developerguide/web-acl-associating-aws-resource.html)in the*AWS WAF, AWS Firewall Manager, and AWS Shield Advanced Developer Guide*.- 
                    For API details, see [AssociateWebAcl](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/wafv2/associate-web-acl.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `check-capacity`.

- **AWS CLI**
- 
            
                    **To obtain the capacity used by a set of rules**The following `check-capacity`retrieves the capacity requirements for a rule set that contains a rate-based rule statement, and an AND rule statement that contains nested rules.`aws wafv2 check-capacity \ --scope``REGIONAL`\ --rules`file://waf-rule-list.json`\ --region`us-west-2`Contents of file://waf-rule-list.json: `[ { "Name":"basic-rule", "Priority":0, "Statement":{ "AndStatement":{ "Statements":[ { "ByteMatchStatement":{ "SearchString":"example.com", "FieldToMatch":{ "SingleHeader":{ "Name":"host" } }, "TextTransformations":[ { "Priority":0, "Type":"LOWERCASE" } ], "PositionalConstraint":"EXACTLY" } }, { "GeoMatchStatement":{ "CountryCodes":[ "US", "IN" ] } } ] } }, "Action":{ "Allow":{ } }, "VisibilityConfig":{ "SampledRequestsEnabled":true, "CloudWatchMetricsEnabled":true, "MetricName":"basic-rule" } }, { "Name":"rate-rule", "Priority":1, "Statement":{ "RateBasedStatement":{ "Limit":1000, "AggregateKeyType":"IP" } }, "Action":{ "Block":{ } }, "VisibilityConfig":{ "SampledRequestsEnabled":true, "CloudWatchMetricsEnabled":true, "MetricName":"rate-rule" } } ]`Output: `{ "Capacity":15 }`For more information, see [AWS WAF Web ACL Capacity Units (WCU)](https://docs.aws.amazon.com/waf/latest/developerguide/how-aws-waf-works.html#aws-waf-capacity-units)in the*AWS WAF, AWS Firewall Manager, and AWS Shield Advanced Developer Guide*.- 
                    For API details, see [CheckCapacity](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/wafv2/check-capacity.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `create-ip-set`.

- **AWS CLI**
- 
            
                    **To create an IP set for use in your web ACLs and rule groups**The following `create-ip-set`command creates an IP set with a single address range specification.`aws wafv2 create-ip-set \ --name``testip`\ --scope`REGIONAL`\ --ip-address-version`IPV4`\ --addresses`198.51.100.0/16`Output: `{ "Summary":{ "ARN":"arn:aws:wafv2:us-west-2:123456789012:regional/ipset/testip/a1b2c3d4-5678-90ab-cdef-EXAMPLE11111", "Description":"", "Name":"testip", "LockToken":"447e55ac-0000-0000-0000-86b67c17f8b5", "Id":"a1b2c3d4-5678-90ab-cdef-EXAMPLE11111" } }`For more information, see [IP Sets and Regex Pattern Sets](https://docs.aws.amazon.com/waf/latest/developerguide/waf-referenced-set-managing.html)in the*AWS WAF, AWS Firewall Manager, and AWS Shield Advanced Developer Guide*.- 
                    For API details, see [CreateIpSet](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/wafv2/create-ip-set.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `create-regex-pattern-set`.

- **AWS CLI**
- 
            
                    **To create a regex pattern set for use in your web ACLs and rule groups**The following `create-regex-pattern-set`command creates a regex pattern set with two regex patterns specified.`aws wafv2 create-regex-pattern-set \ --name``regexPatterSet01`\ --scope`REGIONAL`\ --description '`Test web-acl`' \ --regular-expression-list '`[{"RegexString": "/[0-9]*/"},{"RegexString": "/[a-z]*/"}]`'Output: `{ "Summary":{ "ARN":"arn:aws:wafv2:us-west-2:123456789012:regional/regexpatternset/regexPatterSet01/a1b2c3d4-5678-90ab-cdef-EXAMPLE11111", "Description":"Test web-acl", "Name":"regexPatterSet01", "LockToken":"0bc01e21-03c9-4b98-9433-6229cbf1ef1c", "Id":"a1b2c3d4-5678-90ab-cdef-EXAMPLE11111" } }`For more information, see [IP Sets and Regex Pattern Sets](https://docs.aws.amazon.com/waf/latest/developerguide/waf-referenced-set-managing.html)in the*AWS WAF, AWS Firewall Manager, and AWS Shield Advanced Developer Guide*.- 
                    For API details, see [CreateRegexPatternSet](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/wafv2/create-regex-pattern-set.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `create-rule-group`.

- **AWS CLI**
- 
            
                    **To create a custom rule group for use in your web ACLs**The following `create-rule-group`command creates a custom rule group for regional use. The rule statements for the group are provided in a JSON-formatted file.`aws wafv2 create-rule-group \ --name``"TestRuleGroup"`\ --scope`REGIONAL`\ --capacity`250`\ --rules`file://waf-rule.json`\ --visibility-config`SampledRequestsEnabled=true,CloudWatchMetricsEnabled=true,MetricName=TestRuleGroupMetrics`\ --region`us-west-2`Contents of file://waf-rule.json: `[ { "Name":"basic-rule", "Priority":0, "Statement":{ "AndStatement":{ "Statements":[ { "ByteMatchStatement":{ "SearchString":"example.com", "FieldToMatch":{ "SingleHeader":{ "Name":"host" } }, "TextTransformations":[ { "Priority":0, "Type":"LOWERCASE" } ], "PositionalConstraint":"EXACTLY" } }, { "GeoMatchStatement":{ "CountryCodes":[ "US", "IN" ] } } ] } }, "Action":{ "Allow":{ } }, "VisibilityConfig":{ "SampledRequestsEnabled":true, "CloudWatchMetricsEnabled":true, "MetricName":"basic-rule" } } ]`Output: `{ "Summary":{ "ARN":"arn:aws:wafv2:us-west-2:123456789012:regional/rulegroup/TestRuleGroup/a1b2c3d4-5678-90ab-cdef-EXAMPLE11111", "Description":"", "Name":"TestRuleGroup", "LockToken":"7b3bcec2-374e-4c5a-b2b9-563bf47249f0", "Id":"a1b2c3d4-5678-90ab-cdef-EXAMPLE11111" } }`For more information, see [Managing Your Own Rule Groups](https://docs.aws.amazon.com/waf/latest/developerguide/waf-user-created-rule-groups.html)in the*AWS WAF, AWS Firewall Manager, and AWS Shield Advanced Developer Guide*.- 
                    For API details, see [CreateRuleGroup](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/wafv2/create-rule-group.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `create-web-acl`.

- **AWS CLI**
- 
            
                    **To create a web ACL**The following `create-web-acl`command creates a web ACL for regional use. The rule statements for the web ACL are provided in a JSON-formatted file.`aws wafv2 create-web-acl \ --name``TestWebAcl`\ --scope`REGIONAL`\ --default-action`Allow={}`\ --visibility-config`SampledRequestsEnabled=true,CloudWatchMetricsEnabled=true,MetricName=TestWebAclMetrics`\ --rules`file://waf-rule.json`\ --region`us-west-2`Contents of file://waf-rule.json: `[ { "Name":"basic-rule", "Priority":0, "Statement":{ "AndStatement":{ "Statements":[ { "ByteMatchStatement":{ "SearchString":"example.com", "FieldToMatch":{ "SingleHeader":{ "Name":"host" } }, "TextTransformations":[ { "Priority":0, "Type":"LOWERCASE" } ], "PositionalConstraint":"EXACTLY" } }, { "GeoMatchStatement":{ "CountryCodes":[ "US", "IN" ] } } ] } }, "Action":{ "Allow":{ } }, "VisibilityConfig":{ "SampledRequestsEnabled":true, "CloudWatchMetricsEnabled":true, "MetricName":"basic-rule" } } ]`Output: `{ "Summary":{ "ARN":"arn:aws:wafv2:us-west-2:123456789012:regional/webacl/TestWebAcl/a1b2c3d4-5678-90ab-cdef-EXAMPLE11111", "Description":"", "Name":"TestWebAcl", "LockToken":"2294b3a1-eb60-4aa0-a86f-a3ae04329de9", "Id":"a1b2c3d4-5678-90ab-cdef-EXAMPLE11111" } }`For more information, see [Managing and Using a Web Access Control List (Web ACL)](https://docs.aws.amazon.com/waf/latest/developerguide/web-acl.html)in the*AWS WAF, AWS Firewall Manager, and AWS Shield Advanced Developer Guide*.- 
                    For API details, see [CreateWebAcl](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/wafv2/create-web-acl.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `delete-ip-set`.

- **AWS CLI**
- 
            
                    **To delete an IP set**The following `delete-ip-set`deletes the specified IP set. This call requires an ID, which you can obtain from the call,`list-ip-sets`, and a lock token, which you can obtain from the calls,`list-ip-sets`and`get-ip-set`.`aws wafv2 delete-ip-set \ --name``test1`\ --scope`REGIONAL`\ --id`a1b2c3d4-5678-90ab-cdef-EXAMPLE11111`\ --lock-token`46851772-db6f-459d-9385-49428812e357`This command produces no output. For more information, see [IP Sets and Regex Pattern Sets](https://docs.aws.amazon.com/waf/latest/developerguide/waf-referenced-set-managing.html)in the*AWS WAF, AWS Firewall Manager, and AWS Shield Advanced Developer Guide*.- 
                    For API details, see [DeleteIpSet](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/wafv2/delete-ip-set.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `delete-logging-configuration`.

- **AWS CLI**
- 
            
                    **To disable logging for a web ACL**The following `delete-logging-configuration`removes any logging configuration from the specified web ACL.`aws wafv2 delete-logging-configuration \ --resource-arn``arn:aws:wafv2:us-west-2:123456789012:regional/webacl/test/a1b2c3d4-5678-90ab-cdef-EXAMPLE22222`This command produces no output. For more information, see [Logging Web ACL Traffic Information](https://docs.aws.amazon.com/waf/latest/developerguide/logging.html)in the*AWS WAF, AWS Firewall Manager, and AWS Shield Advanced Developer Guide*.- 
                    For API details, see [DeleteLoggingConfiguration](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/wafv2/delete-logging-configuration.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `delete-regex-pattern-set`.

- **AWS CLI**
- 
            
                    **To delete a regex pattern set**The following `delete-regex-pattern-set`updates the settings for the specified regex pattern set. This call requires an ID, which you can obtain from the call,`list-regex-pattern-sets`, and a lock token, which you can obtain from the call`list-regex-pattern-sets`or the call`get-regex-pattern-set`.`aws wafv2 delete-regex-pattern-set \ --name``regexPatterSet01`\ --scope`REGIONAL`\ --id`a1b2c3d4-5678-90ab-cdef-EXAMPLE11111`\ --lock-token`0bc01e21-03c9-4b98-9433-6229cbf1ef1c`This command produces no output. For more information, see [IP Sets and Regex Pattern Sets](https://docs.aws.amazon.com/waf/latest/developerguide/waf-referenced-set-managing.html)in the*AWS WAF, AWS Firewall Manager, and AWS Shield Advanced Developer Guide*.- 
                    For API details, see [DeleteRegexPatternSet](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/wafv2/delete-regex-pattern-set.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `delete-rule-group`.

- **AWS CLI**
- 
            
                    **To delete a custom rule group**The following `delete-rule-group`deletes the specified custom rule group. This call requires an ID, which you can obtain from the call,`list-rule-groups`, and a lock token, which you can obtain from the call`list-rule-groups`or the call`get-rule-group`.`aws wafv2 delete-rule-group \ --name``TestRuleGroup`\ --scope`REGIONAL`\ --id`a1b2c3d4-5678-90ab-cdef-EXAMPLE11111`\ --lock-token`7b3bcec2-0000-0000-0000-563bf47249f0`This command produces no output. For more information, see [Managing Your Own Rule Groups](https://docs.aws.amazon.com/waf/latest/developerguide/waf-user-created-rule-groups.html)in the*AWS WAF, AWS Firewall Manager, and AWS Shield Advanced Developer Guide*.- 
                    For API details, see [DeleteRuleGroup](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/wafv2/delete-rule-group.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `delete-web-acl`.

- **AWS CLI**
- 
            
                    **To delete a web ACL**The following `delete-web-acl`deletes the specified web ACL from your account. A web ACL can only be deleted when it's not associated with any resources. This call requires an ID, which you can obtain from the call,`list-web-acls`, and a lock token, which you can obtain from the call`list-web-acls`or the call`get-web-acl`.`aws wafv2 delete-web-acl \ --name``test`\ --scope`REGIONAL`\ --id`a1b2c3d4-5678-90ab-cdef-EXAMPLE11111`\ --lock-token`ebab4ed2-155e-4c9a-9efb-e4c45665b1f5`This command produces no output. For more information, see [Managing and Using a Web Access Control List (Web ACL)](https://docs.aws.amazon.com/waf/latest/developerguide/web-acl.html)in the*AWS WAF, AWS Firewall Manager, and AWS Shield Advanced Developer Guide*.- 
                    For API details, see [DeleteWebAcl](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/wafv2/delete-web-acl.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `describe-managed-rule-group`.

- **AWS CLI**
- 
            
                    **To retrieve the description for a managed rule group**The following `describe-managed-rule-group`retrieves the description for an AWS managed rule group.`aws wafv2 describe-managed-rule-group \ --vendor-name``AWS`\ --name`AWSManagedRulesCommonRuleSet`\ --scope`REGIONAL`Output: `{ "Capacity": 700, "Rules": [ { "Name": "NoUserAgent_HEADER", "Action": { "Block": {} } }, { "Name": "UserAgent_BadBots_HEADER", "Action": { "Block": {} } }, { "Name": "SizeRestrictions_QUERYSTRING", "Action": { "Block": {} } }, { "Name": "SizeRestrictions_Cookie_HEADER", "Action": { "Block": {} } }, { "Name": "SizeRestrictions_BODY", "Action": { "Block": {} } }, { "Name": "SizeRestrictions_URIPATH", "Action": { "Block": {} } }, { "Name": "EC2MetaDataSSRF_BODY", "Action": { "Block": {} } }, { "Name": "EC2MetaDataSSRF_COOKIE", "Action": { "Block": {} } }, { "Name": "EC2MetaDataSSRF_URIPATH", "Action": { "Block": {} } }, { "Name": "EC2MetaDataSSRF_QUERYARGUMENTS", "Action": { "Block": {} } }, { "Name": "GenericLFI_QUERYARGUMENTS", "Action": { "Block": {} } }, { } "Name": "GenericLFI_URIPATH", "Action": { "Block": {} } }, { "Name": "GenericLFI_BODY", "Action": { "Block": {} } }, { "Name": "RestrictedExtensions_URIPATH", "Action": { "Block": {} } }, { "Name": "RestrictedExtensions_QUERYARGUMENTS", "Action": { "Block": {} } }, { "Name": "GenericRFI_QUERYARGUMENTS", "Action": { "Block": {} } }, { "Name": "GenericRFI_BODY", "Action": { "Block": {} } }, { "Name": "GenericRFI_URIPATH", "Action": { "Block": {} } }, { "Name": "CrossSiteScripting_COOKIE", "Action": { "Block": {} } }, { "Name": "CrossSiteScripting_QUERYARGUMENTS", "Action": { "Block": {} } }, { "Name": "CrossSiteScripting_BODY", "Action": { "Block": {} } }, { "Name": "CrossSiteScripting_URIPATH", "Action": { "Block": {} } } ] }`For more information, see [Managed Rule Groups](https://docs.aws.amazon.com/waf/latest/developerguide/waf-managed-rule-groups.html)in the*AWS WAF, AWS Firewall Manager, and AWS Shield Advanced Developer Guide*.- 
                    For API details, see [DescribeManagedRuleGroup](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/wafv2/describe-managed-rule-group.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `disassociate-web-acl`.

- **AWS CLI**
- 
            
                    **To disassociate a web ACL from a regional AWS resource**The following `disassociate-web-acl`example removes any existing web ACL association from the specified Application Load Balancer.`aws wafv2 disassociate-web-acl \ --resource-arn``arn:aws:elasticloadbalancing:us-west-2:123456789012:loadbalancer/app/waf-cli-alb/1ea17125f8b25a2a`\ --region`us-west-2`This command produces no output. For more information, see [Associating or Disassociating a Web ACL with an AWS Resource](https://docs.aws.amazon.com/waf/latest/developerguide/web-acl-associating-aws-resource.html)in the*AWS WAF, AWS Firewall Manager, and AWS Shield Advanced Developer Guide*.- 
                    For API details, see [DisassociateWebAcl](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/wafv2/disassociate-web-acl.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `get-ip-set`.

- **AWS CLI**
- 
            
                    **To retrieve a specific IP set**The following `get-ip-set`retrieves the IP set with the specified name, scope, and ID. You can get the ID for an IP set from the commands`create-ip-set`and`list-ip-sets`.`aws wafv2 get-ip-set \ --name``testip`\ --scope`REGIONAL`\ --id`a1b2c3d4-5678-90ab-cdef-EXAMPLE11111`Output: `{ "IPSet":{ "Description":"", "Name":"testip", "IPAddressVersion":"IPV4", "Id":"a1b2c3d4-5678-90ab-cdef-EXAMPLE1111", "ARN":"arn:aws:wafv2:us-west-2:123456789012:regional/ipset/testip/a1b2c3d4-5678-90ab-cdef-EXAMPLE1111", "Addresses":[ "192.0.2.0/16" ] }, "LockToken":"447e55ac-2396-4c6d-b9f9-86b67c17f8b5" }`For more information, see [IP Sets and Regex Pattern Sets](https://docs.aws.amazon.com/waf/latest/developerguide/waf-referenced-set-managing.html)in the*AWS WAF, AWS Firewall Manager, and AWS Shield Advanced Developer Guide*.- 
                    For API details, see [GetIpSet](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/wafv2/get-ip-set.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `get-logging-configuration`.

- **AWS CLI**
- 
            
                    **To retrieve the logging configurations for a web ACL**The following `get-logging-configuration`retrieves the logging configuration for the specified web ACL.`aws wafv2 get-logging-configuration \ --resource-arn``arn:aws:wafv2:us-west-2:123456789012:regional/webacl/test/a1b2c3d4-5678-90ab-cdef-EXAMPLE22222`\ --region`us-west-2`Output: `{ "LoggingConfiguration":{ "ResourceArn":"arn:aws:wafv2:us-west-2:123456789012:regional/webacl/test/a1b2c3d4-5678-90ab-cdef-EXAMPLE22222", "RedactedFields":[ { "Method":{ } } ], "LogDestinationConfigs":[ "arn:aws:firehose:us-west-2:123456789012:deliverystream/aws-waf-logs-custom-transformation" ] } }`For more information, see [Logging Web ACL Traffic Information](https://docs.aws.amazon.com/waf/latest/developerguide/logging.html)in the*AWS WAF, AWS Firewall Manager, and AWS Shield Advanced Developer Guide*.- 
                    For API details, see [GetLoggingConfiguration](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/wafv2/get-logging-configuration.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `get-rate-based-statement-managed-keys`.

- **AWS CLI**
- 
            
                    **To retrieve a list of IP addresses that are blocked by a rate-based rule**The following `get-rate-based-statement-managed-keys`retrieves the IP addresses currently blocked by a rate-based rule that's being used for a regional application.`aws wafv2 get-rate-based-statement-managed-keys \ --scope``REGIONAL`\ --web-acl-name`testwebacl2`\ --web-acl-id`a1b2c3d4-5678-90ab-cdef-EXAMPLE11111`\ --rule-name`ratebasedtest`Output: `{ "ManagedKeysIPV4":{ "IPAddressVersion":"IPV4", "Addresses":[ "198.51.100.0/32" ] }, "ManagedKeysIPV6":{ "IPAddressVersion":"IPV6", "Addresses":[ ] } }`For more information, see [Rate-Based Rule Statement](https://docs.aws.amazon.com/waf/latest/developerguide/waf-rule-statement-type-rate-based.html)in the*AWS WAF, AWS Firewall Manager, and AWS Shield Advanced Developer Guide*.- 
                    For API details, see [GetRateBasedStatementManagedKeys](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/wafv2/get-rate-based-statement-managed-keys.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `get-regex-pattern-set`.

- **AWS CLI**
- 
            
                    **To retrieve a specific regex pattern set**The following `get-regex-pattern-set`retrieves the regex pattern set with the specified name, scope, region, and ID. You can get the ID for a regex pattern set from the commands`create-regex-pattern-set`and`list-regex-pattern-sets`.`aws wafv2 get-regex-pattern-set \ --name``regexPatterSet01`\ --scope`REGIONAL`\ --id`a1b2c3d4-5678-90ab-cdef-EXAMPLE11111`\ --region`us-west-2`Output: `{ "RegexPatternSet":{ "Description":"Test web-acl", "RegularExpressionList":[ { "RegexString":"/[0-9]*/" }, { "RegexString":"/[a-z]*/" } ], "Name":"regexPatterSet01", "ARN":"arn:aws:wafv2:us-west-2:123456789012:regional/regexpatternset/regexPatterSet01/a1b2c3d4-5678-90ab-cdef-EXAMPLE11111", "Id":"a1b2c3d4-5678-90ab-cdef-EXAMPLE11111" }, "LockToken":"c8abf33f-b6fc-46ae-846e-42f994d57b29" }`For more information, see [IP Sets and Regex Pattern Sets](https://docs.aws.amazon.com/waf/latest/developerguide/waf-referenced-set-managing.html)in the*AWS WAF, AWS Firewall Manager, and AWS Shield Advanced Developer Guide*.- 
                    For API details, see [GetRegexPatternSet](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/wafv2/get-regex-pattern-set.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `get-rule-group`.

- **AWS CLI**
- 
            
                    **To retrieve a specific custom rule group**The following `get-rule-group`retrieves the custom rule group with the specified name, scope, and ID. You can get the ID for a rule group from the commands`create-rule-group`and`list-rule-groups`.`aws wafv2 get-rule-group \ --name``ff`\ --scope`REGIONAL`\ --id`a1b2c3d4-5678-90ab-cdef-EXAMPLE11111`Output: `{ "RuleGroup":{ "Capacity":1, "Description":"", "Rules":[ { "Priority":0, "Action":{ "Block":{ } }, "VisibilityConfig":{ "SampledRequestsEnabled":true, "CloudWatchMetricsEnabled":true, "MetricName":"jj" }, "Name":"jj", "Statement":{ "SizeConstraintStatement":{ "ComparisonOperator":"LE", "TextTransformations":[ { "Priority":0, "Type":"NONE" } ], "FieldToMatch":{ "UriPath":{ } }, "Size":7 } } } ], "VisibilityConfig":{ "SampledRequestsEnabled":true, "CloudWatchMetricsEnabled":true, "MetricName":"ff" }, "Id":"a1b2c3d4-5678-90ab-cdef-EXAMPLE11111", "ARN":"arn:aws:wafv2:us-west-2:123456789012:regional/rulegroup/ff/a1b2c3d4-5678-90ab-cdef-EXAMPLE11111", "Name":"ff" }, "LockToken":"485458c9-1830-4234-af31-ec4d52ced1b3" }`For more information, see [Managing Your Own Rule Groups](https://docs.aws.amazon.com/waf/latest/developerguide/waf-user-created-rule-groups.html)in the*AWS WAF, AWS Firewall Manager, and AWS Shield Advanced Developer Guide*.- 
                    For API details, see [GetRuleGroup](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/wafv2/get-rule-group.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `get-sampled-requests`.

- **AWS CLI**
- 
            
                    **To retrieve a sample of web requests for a web ACL**The following `get-sampled-requests`retrieves the sampled web requests for the specified web ACL, rule metric, and time frame.`aws wafv2 get-sampled-requests \ --web-acl-arn``arn:aws:wafv2:us-west-2:123456789012:regional/webacl/test-cli/a1b2c3d4-5678-90ab-cdef-EXAMPLE11111`\ --rule-metric-name`AWS-AWSManagedRulesSQLiRuleSet`\ --scope=REGIONAL \ --time-window`StartTime=2020-02-12T20:00Z,EndTime=2020-02-12T21:10Z`\ --max-items`100`Output: `{ "TimeWindow": { "EndTime": 1581541800.0, "StartTime": 1581537600.0 }, "SampledRequests": [ { "Action": "BLOCK", "Timestamp": 1581541799.564, "RuleNameWithinRuleGroup": "AWS#AWSManagedRulesSQLiRuleSet#SQLi_BODY", "Request": { "Country": "US", "URI": "/", "Headers": [ { "Name": "Host", "Value": "alb-test-1EXAMPLE1.us-east-1.elb.amazonaws.com" }, { "Name": "Content-Length", "Value": "7456" }, { "Name": "User-Agent", "Value": "curl/7.53.1" }, { "Name": "Accept", "Value": "/" }, { "Name": "Content-Type", "Value": "application/x-www-form-urlencoded" } ], "ClientIP": "198.51.100.08", "Method": "POST", "HTTPVersion": "HTTP/1.1" }, "Weight": 1 }, { "Action": "BLOCK", "Timestamp": 1581541799.988, "RuleNameWithinRuleGroup": "AWS#AWSManagedRulesSQLiRuleSet#SQLi_BODY", "Request": { "Country": "US", "URI": "/", "Headers": [ { "Name": "Host", "Value": "alb-test-1EXAMPLE1.us-east-1.elb.amazonaws.com" }, { "Name": "Content-Length", "Value": "7456" }, { "Name": "User-Agent", "Value": "curl/7.53.1" }, { "Name": "Accept", "Value": "/" }, { "Name": "Content-Type", "Value": "application/x-www-form-urlencoded" } ], "ClientIP": "198.51.100.08", "Method": "POST", "HTTPVersion": "HTTP/1.1" }, "Weight": 3 }, { "Action": "BLOCK", "Timestamp": 1581541799.846, "RuleNameWithinRuleGroup": "AWS#AWSManagedRulesSQLiRuleSet#SQLi_BODY", "Request": { "Country": "US", "URI": "/", "Headers": [ { "Name": "Host", "Value": "alb-test-1EXAMPLE1.us-east-1.elb.amazonaws.com" }, { "Name": "Content-Length", "Value": "7456" }, { "Name": "User-Agent", "Value": "curl/7.53.1" }, { "Name": "Accept", "Value": "/" }, { "Name": "Content-Type", "Value": "application/x-www-form-urlencoded" } ], "ClientIP": "198.51.100.08", "Method": "POST", "HTTPVersion": "HTTP/1.1" }, "Weight": 1 }, { "Action": "BLOCK", "Timestamp": 1581541799.4, "RuleNameWithinRuleGroup": "AWS#AWSManagedRulesSQLiRuleSet#SQLi_BODY", "Request": { "Country": "US", "URI": "/", "Headers": [ { "Name": "Host", "Value": "alb-test-1EXAMPLE1.us-east-1.elb.amazonaws.com" }, { "Name": "Content-Length", "Value": "7456" }, { "Name": "User-Agent", "Value": "curl/7.53.1" }, { "Name": "Accept", "Value": "/" }, { "Name": "Content-Type", "Value": "application/x-www-form-urlencoded" } ], "ClientIP": "198.51.100.08", "Method": "POST", "HTTPVersion": "HTTP/1.1" }, "Weight": 1 } ], "PopulationSize": 4 }`For more information, see [Viewing a Sample of Web Requests](https://docs.aws.amazon.com/waf/latest/developerguide/web-acl-testing.html#web-acl-testing-view-sample)in the*AWS WAF, AWS Firewall Manager, and AWS Shield Advanced Developer Guide*.- 
                    For API details, see [GetSampledRequests](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/wafv2/get-sampled-requests.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `get-web-acl-for-resource`.

- **AWS CLI**
- 
            
                    **To retrieve the web ACL that's associated with an AWS resource**The following `get-web-acl-for-resource`retrieves the JSON for the web ACL that's associated with the specified resource.`aws wafv2 get-web-acl-for-resource \ --resource-arn``arn:aws:elasticloadbalancing:us-west-2:123456789012:loadbalancer/app/waf-cli-alb/1ea17125f8b25a2a`Output: `{ "WebACL":{ "Capacity":3, "Description":"", "Rules":[ { "Priority":1, "Action":{ "Block":{ } }, "VisibilityConfig":{ "SampledRequestsEnabled":true, "CloudWatchMetricsEnabled":true, "MetricName":"testrule01" }, "Name":"testrule01", "Statement":{ "AndStatement":{ "Statements":[ { "ByteMatchStatement":{ "PositionalConstraint":"EXACTLY", "TextTransformations":[ { "Priority":0, "Type":"NONE" } ], "SearchString":"dGVzdHN0cmluZw==", "FieldToMatch":{ "UriPath":{ } } } }, { "SizeConstraintStatement":{ "ComparisonOperator":"EQ", "TextTransformations":[ { "Priority":0, "Type":"NONE" } ], "FieldToMatch":{ "QueryString":{ } }, "Size":0 } } ] } } } ], "VisibilityConfig":{ "SampledRequestsEnabled":true, "CloudWatchMetricsEnabled":true, "MetricName":"test01" }, "DefaultAction":{ "Allow":{ } }, "Id":"9a1b2c3d4-5678-90ab-cdef-EXAMPLE11111 ", "ARN":"arn:aws:wafv2:us-west-2:123456789012:regional/webacl/test01/a1b2c3d4-5678-90ab-cdef-EXAMPLE11111 ", "Name":"test01" } }`For more information, see [Associating or Disassociating a Web ACL with an AWS Resource](https://docs.aws.amazon.com/waf/latest/developerguide/web-acl-associating-aws-resource.html)in the*AWS WAF, AWS Firewall Manager, and AWS Shield Advanced Developer Guide*.- 
                    For API details, see [GetWebAclForResource](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/wafv2/get-web-acl-for-resource.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `get-web-acl`.

- **AWS CLI**
- 
            
                    **To retrieve a web ACL**The following `get-web-acl`retrieves the web ACL with the specified name, scope, and ID. You can get the ID for a web ACL from the commands`create-web-acl`and`list-web-acls`.`aws wafv2 get-web-acl \ --name``test01`\ --scope`REGIONAL`\ --id`a1b2c3d4-5678-90ab-cdef-EXAMPLE11111`Output: `{ "WebACL":{ "Capacity":3, "Description":"", "Rules":[ { "Priority":1, "Action":{ "Block":{ } }, "VisibilityConfig":{ "SampledRequestsEnabled":true, "CloudWatchMetricsEnabled":true, "MetricName":"testrule01" }, "Name":"testrule01", "Statement":{ "AndStatement":{ "Statements":[ { "ByteMatchStatement":{ "PositionalConstraint":"EXACTLY", "TextTransformations":[ { "Priority":0, "Type":"NONE" } ], "SearchString":"dGVzdHN0cmluZw==", "FieldToMatch":{ "UriPath":{ } } } }, { "SizeConstraintStatement":{ "ComparisonOperator":"EQ", "TextTransformations":[ { "Priority":0, "Type":"NONE" } ], "FieldToMatch":{ "QueryString":{ } }, "Size":0 } } ] } } } ], "VisibilityConfig":{ "SampledRequestsEnabled":true, "CloudWatchMetricsEnabled":true, "MetricName":"test01" }, "DefaultAction":{ "Allow":{ } }, "Id":"a1b2c3d4-5678-90ab-cdef-EXAMPLE11111", "ARN":"arn:aws:wafv2:us-west-2:123456789012:regional/webacl/test01/a1b2c3d4-5678-90ab-cdef-EXAMPLE11111", "Name":"test01" }, "LockToken":"e3db7e2c-d58b-4ee6-8346-6aec5511c6fb" }`For more information, see [Managing and Using a Web Access Control List (Web ACL)](https://docs.aws.amazon.com/waf/latest/developerguide/web-acl.html)in the*AWS WAF, AWS Firewall Manager, and AWS Shield Advanced Developer Guide*.- 
                    For API details, see [GetWebAcl](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/wafv2/get-web-acl.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `list-available-managed-rule-groups`.

- **AWS CLI**
- 
            
                    **To retrieve the managed rule groups**The following `list-available-managed-rule-groups`returns the list of all managed rule groups that are currently available for use in your web ACLs.`aws wafv2 list-available-managed-rule-groups \ --scope``REGIONAL`Output: `{ "ManagedRuleGroups": [ { "VendorName": "AWS", "Name": "AWSManagedRulesCommonRuleSet", "Description": "Contains rules that are generally applicable to web applications. This provides protection against exploitation of a wide range of vulnerabilities, including those described in OWASP publications and common Common Vulnerabilities and Exposures (CVE)." }, { "VendorName": "AWS", "Name": "AWSManagedRulesAdminProtectionRuleSet", "Description": "Contains rules that allow you to block external access to exposed admin pages. This may be useful if you are running third-party software or would like to reduce the risk of a malicious actor gaining administrative access to your application." }, { "VendorName": "AWS", "Name": "AWSManagedRulesKnownBadInputsRuleSet", "Description": "Contains rules that allow you to block request patterns that are known to be invalid and are associated with exploitation or discovery of vulnerabilities. This can help reduce the risk of a malicious actor discovering a vulnerable application." }, { "VendorName": "AWS", "Name": "AWSManagedRulesSQLiRuleSet", "Description": "Contains rules that allow you to block request patterns associated with exploitation of SQL databases, like SQL injection attacks. This can help prevent remote injection of unauthorized queries." }, { "VendorName": "AWS", "Name": "AWSManagedRulesLinuxRuleSet", "Description": "Contains rules that block request patterns associated with exploitation of vulnerabilities specific to Linux, including LFI attacks. This can help prevent attacks that expose file contents or execute code for which the attacker should not have had access." }, { "VendorName": "AWS", "Name": "AWSManagedRulesUnixRuleSet", "Description": "Contains rules that block request patterns associated with exploiting vulnerabilities specific to POSIX/POSIX-like OS, including LFI attacks. This can help prevent attacks that expose file contents or execute code for which access should not been allowed." }, { "VendorName": "AWS", "Name": "AWSManagedRulesWindowsRuleSet", "Description": "Contains rules that block request patterns associated with exploiting vulnerabilities specific to Windows, (e.g., PowerShell commands). This can help prevent exploits that allow attacker to run unauthorized commands or execute malicious code." }, { "VendorName": "AWS", "Name": "AWSManagedRulesPHPRuleSet", "Description": "Contains rules that block request patterns associated with exploiting vulnerabilities specific to the use of the PHP, including injection of unsafe PHP functions. This can help prevent exploits that allow an attacker to remotely execute code or commands." }, { "VendorName": "AWS", "Name": "AWSManagedRulesWordPressRuleSet", "Description": "The WordPress Applications group contains rules that block request patterns associated with the exploitation of vulnerabilities specific to WordPress sites." }, { "VendorName": "AWS", "Name": "AWSManagedRulesAmazonIpReputationList", "Description": "This group contains rules that are based on Amazon threat intelligence. This is useful if you would like to block sources associated with bots or other threats." } ] }`For more information, see [Managed Rule Groups](https://docs.aws.amazon.com/waf/latest/developerguide/waf-managed-rule-groups.html)in the*AWS WAF, AWS Firewall Manager, and AWS Shield Advanced Developer Guide*.- 
                    For API details, see [ListAvailableManagedRuleGroups](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/wafv2/list-available-managed-rule-groups.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `list-ip-sets`.

- **AWS CLI**
- 
            
                    **To retrieve a list of IP sets**The following `list-ip-sets`retrieves all IP sets for the account that have regional scope.`aws wafv2 list-ip-sets \ --scope``REGIONAL`Output: `{ "IPSets":[ { "ARN":"arn:aws:wafv2:us-west-2:123456789012:regional/ipset/testip/a1b2c3d4-5678-90ab-cdef-EXAMPLE11111", "Description":"", "Name":"testip", "LockToken":"0674c84b-0304-47fe-8728-c6bff46af8fc", "Id":"a1b2c3d4-5678-90ab-cdef-EXAMPLE11111 " } ], "NextMarker":"testip" }`For more information, see [IP Sets and Regex Pattern Sets](https://docs.aws.amazon.com/waf/latest/developerguide/waf-referenced-set-managing.html)in the*AWS WAF, AWS Firewall Manager, and AWS Shield Advanced Developer Guide*.- 
                    For API details, see [ListIpSets](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/wafv2/list-ip-sets.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `list-logging-configurations`.

- **AWS CLI**
- 
            
                    **To retrieve a list of all logging configurations for a region**The following `list-logging-configurations`retrieves the all logging configurations for web ACLs that are scoped for regional use in the`us-west-2`region.`aws wafv2 list-logging-configurations \ --scope``REGIONAL`\ --region`us-west-2`Output: `{ "LoggingConfigurations":[ { "ResourceArn":"arn:aws:wafv2:us-west-2:123456789012:regional/webacl/test-2/a1b2c3d4-5678-90ab-cdef-EXAMPLE11111", "RedactedFields":[ { "QueryString":{ } } ], "LogDestinationConfigs":[ "arn:aws:firehose:us-west-2:123456789012:deliverystream/aws-waf-logs-test" ] }, { "ResourceArn":"arn:aws:wafv2:us-west-2:123456789012:regional/webacl/test/a1b2c3d4-5678-90ab-cdef-EXAMPLE22222", "RedactedFields":[ { "Method":{ } } ], "LogDestinationConfigs":[ "arn:aws:firehose:us-west-2:123456789012:deliverystream/aws-waf-logs-custom-transformation" ] } ] }`For more information, see [Logging Web ACL Traffic Information](https://docs.aws.amazon.com/waf/latest/developerguide/logging.html)in the*AWS WAF, AWS Firewall Manager, and AWS Shield Advanced Developer Guide*.- 
                    For API details, see [ListLoggingConfigurations](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/wafv2/list-logging-configurations.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `list-regex-pattern-sets`.

- **AWS CLI**
- 
            
                    **To retrieve a list of regex pattern sets**The following `list-regex-pattern-sets`retrieves all regex pattern sets for the account that are defined in the region`us-west-2`.`aws wafv2 list-regex-pattern-sets \ --scope``REGIONAL`\ --region`us-west-2`Output: `{ "NextMarker":"regexPatterSet01", "RegexPatternSets":[ { "ARN":"arn:aws:wafv2:us-west-2:123456789012:regional/regexpatternset/regexPatterSet01/a1b2c3d4-5678-90ab-cdef-EXAMPLE11111", "Description":"Test web-acl", "Name":"regexPatterSet01", "LockToken":"f17743f7-0000-0000-0000-19a8b93bfb01", "Id":"a1b2c3d4-5678-90ab-cdef-EXAMPLE11111" } ] }`For more information, see [IP Sets and Regex Pattern Sets](https://docs.aws.amazon.com/waf/latest/developerguide/waf-referenced-set-managing.html)in the*AWS WAF, AWS Firewall Manager, and AWS Shield Advanced Developer Guide*.- 
                    For API details, see [ListRegexPatternSets](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/wafv2/list-regex-pattern-sets.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `list-resources-for-web-acl`.

- **AWS CLI**
- 
            
                    **To retrieve the resources associated with a web ACL**The following `list-resources-for-web-acl`retrieves the API Gateway REST API resources that are currently associated with the specified web ACL in the region`us-west-2`.`aws wafv2 list-resources-for-web-acl \ --web-acl-arn``arn:aws:wafv2:us-west-2:123456789012:regional/webacl/TestWebAcl/a1b2c3d4-5678-90ab-cdef-EXAMPLE11111`\ --resource-type`API_GATEWAY`\ --region`us-west-2`Output: `{ "ResourceArns": [ "arn:aws:apigateway:us-west-2::/restapis/EXAMPLE111/stages/testing" ] }`For more information, see [Associating or Disassociating a Web ACL with an AWS Resource](https://docs.aws.amazon.com/waf/latest/developerguide/web-acl-associating-aws-resource.html)in the*AWS WAF, AWS Firewall Manager, and AWS Shield Advanced Developer Guide*.- 
                    For API details, see [ListResourcesForWebAcl](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/wafv2/list-resources-for-web-acl.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `list-rule-groups`.

- **AWS CLI**
- 
            
                    **To retrieve a list of custom rule groups**The following `list-rule-groups`retrieves all custom rule groups that are defined for the account for the specified scope and region location.`aws wafv2 list-rule-groups \ --scope``REGIONAL`\ --region`us-west-2`Output: `{ "RuleGroups":[ { "ARN":"arn:aws:wafv2:us-west-2:123456789012:regional/rulegroup/TestRuleGroup/a1b2c3d4-5678-90ab-cdef-EXAMPLE11111", "Description":"", "Name":"TestRuleGroup", "LockToken":"1eb5ec48-0000-0000-0000-ee9b906c541e", "Id":"a1b2c3d4-5678-90ab-cdef-EXAMPLE11111" }, { "ARN":"arn:aws:wafv2:us-west-2:123456789012:regional/rulegroup/test/a1b2c3d4-5678-90ab-cdef-EXAMPLE22222", "Description":"", "Name":"test", "LockToken":"b0f4583e-998b-4880-9069-3fbe45738b43", "Id":"a1b2c3d4-5678-90ab-cdef-EXAMPLE22222" } ], "NextMarker":"test" }`For more information, see [Managing Your Own Rule Groups](https://docs.aws.amazon.com/waf/latest/developerguide/waf-user-created-rule-groups.html)in the*AWS WAF, AWS Firewall Manager, and AWS Shield Advanced Developer Guide*.- 
                    For API details, see [ListRuleGroups](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/wafv2/list-rule-groups.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `list-tags-for-resource`.

- **AWS CLI**
- 
            
                    **To retrieve all tags for an AWS WAF resource**The following `list-tags-for-resource`retrieves the list of all tag key, value pairs for the specified web ACL.`aws wafv2 list-tags-for-resource \ --resource-arn``arn:aws:wafv2:us-west-2:123456789012:regional/webacl/testwebacl2/a1b2c3d4-5678-90ab-cdef-EXAMPLE11111`Output: `{ "NextMarker":"", "TagInfoForResource":{ "ResourceARN":"arn:aws:wafv2:us-west-2:123456789012:regional/webacl/testwebacl2/a1b2c3d4-5678-90ab-cdef-EXAMPLE11111", "TagList":[ ] } }`For more information, see [Getting Started with AWS WAF](https://docs.aws.amazon.com/waf/latest/developerguide/getting-started.html)in the*AWS WAF, AWS Firewall Manager, and AWS Shield Advanced Developer Guide*.- 
                    For API details, see [ListTagsForResource](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/wafv2/list-tags-for-resource.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `list-web-acls`.

- **AWS CLI**
- 
            
                    **To retrieve the web ACLs for a scope**The following `list-web-acls`retrieves all web ACLs that are defined for the account for the specified scope.`aws wafv2 list-web-acls \ --scope``REGIONAL`Output: `{ "NextMarker":"Testt", "WebACLs":[ { "ARN":"arn:aws:wafv2:us-west-2:123456789012:regional/webacl/Testt/a1b2c3d4-5678-90ab-cdef-EXAMPLE11111", "Description":"sssss", "Name":"Testt", "LockToken":"7f36cb30-74ef-4cff-8cd4-a77e1aba1746", "Id":"a1b2c3d4-5678-90ab-cdef-EXAMPLE11111" } ] }`For more information, see [Managing and Using a Web Access Control List (Web ACL)](https://docs.aws.amazon.com/waf/latest/developerguide/web-acl.html)in the*AWS WAF, AWS Firewall Manager, and AWS Shield Advanced Developer Guide*.- 
                    For API details, see [ListWebAcls](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/wafv2/list-web-acls.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `put-logging-configuration`.

- **AWS CLI**
- 
            
                    **To add a logging configuration to a web ACL**The following `put-logging-configuration`adds the Amazon Kinesis Data Firehose logging configuration`aws-waf-logs-custom-transformation`to the specified web ACL, with no fields redacted from the logs.`aws wafv2 put-logging-configuration \ --logging-configuration``ResourceArn=arn:aws:wafv2:us-west-2:123456789012:regional/webacl/test-cli/a1b2c3d4-5678-90ab-cdef-EXAMPLE11111,LogDestinationConfigs=arn:aws:firehose:us-west-2:123456789012:deliverystream/aws-waf-logs-custom-transformation`\ --region`us-west-2`Output: `{ "LoggingConfiguration":{ "ResourceArn":"arn:aws:wafv2:us-west-2:123456789012:regional/webacl/test-cli/a1b2c3d4-5678-90ab-cdef-EXAMPLE11111", "LogDestinationConfigs":[ "arn:aws:firehose:us-west-2:123456789012:deliverystream/aws-waf-logs-custom-transformation" ] } }`For more information, see [Logging Web ACL Traffic Information](https://docs.aws.amazon.com/waf/latest/developerguide/logging.html)in the*AWS WAF, AWS Firewall Manager, and AWS Shield Advanced Developer Guide*.- 
                    For API details, see [PutLoggingConfiguration](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/wafv2/put-logging-configuration.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `tag-resource`.

- **AWS CLI**
- 
            
                    **To add tags to an AWS WAF resource**The following `tag-resource`example adds a tag with a key of`Name`and value set to`AWSWAF`to the specified web ACL.`aws wafv2 tag-resource \ --resource-arn``arn:aws:wafv2:us-west-2:123456789012:regional/webacl/apiGatewayWebAcl/a1b2c3d4-5678-90ab-cdef-EXAMPLE11111`\ --tags`Key=Name,Value=AWSWAF`This command produces no output. For more information, see [Getting Started with AWS WAF](https://docs.aws.amazon.com/waf/latest/developerguide/getting-started.html)in the*AWS WAF, AWS Firewall Manager, and AWS Shield Advanced Developer Guide*.- 
                    For API details, see [TagResource](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/wafv2/tag-resource.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `untag-resource`.

- **AWS CLI**
- 
            
                    **To remove tags from an AWS WAF resource**The following `untag-resource`example removes the tag with the key`KeyName`from the specified web ACL.`aws wafv2 untag-resource \ --resource-arn``arn:aws:wafv2:us-west-2:123456789012:regional/webacl/apiGatewayWebAcl/a1b2c3d4-5678-90ab-cdef-EXAMPLE11111`\ --tag-keys`"KeyName"`This command produces no output. For more information, see [Getting Started with AWS WAF](https://docs.aws.amazon.com/waf/latest/developerguide/getting-started.html)in the*AWS WAF, AWS Firewall Manager, and AWS Shield Advanced Developer Guide*.- 
                    For API details, see [UntagResource](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/wafv2/untag-resource.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `update-ip-set`.

- **AWS CLI**
- 
            
                    **To modify the settings for an existing IP set**The following `update-ip-set`updates the settings for the specified IP set. This call requires an ID, which you can obtain from the call,`list-ip-sets`, and a lock token which you can obtain from the calls,`list-ip-sets`and`get-ip-set`. This call also returns a lock token that you can use for a subsequent update.`aws wafv2 update-ip-set \ --name``testip`\ --scope`REGIONAL`\ --id`a1b2c3d4-5678-90ab-cdef-EXAMPLE11111`\ --addresses`198.51.100.0/16`\ --lock-token`447e55ac-2396-4c6d-b9f9-86b67c17f8b5`Output: `{ "NextLockToken": "0674c84b-0304-47fe-8728-c6bff46af8fc" }`For more information, see [IP Sets and Regex Pattern Sets](https://docs.aws.amazon.com/waf/latest/developerguide/waf-referenced-set-managing.html)in the*AWS WAF, AWS Firewall Manager, and AWS Shield Advanced Developer Guide*.- 
                    For API details, see [UpdateIpSet](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/wafv2/update-ip-set.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `update-regex-pattern-set`.

- **AWS CLI**
- 
            
                    **To modify the settings for an existing regex pattern set**The following `update-regex-pattern-set`updates the settings for the specified regex pattern set. This call requires an ID, which you can obtain from the call,`list-regex-pattern-sets`, and a lock token which you can obtain from the calls,`list-regex-pattern-sets`and`get-regex-pattern-set`. This call also returns a lock token that you can use for a subsequent update.`aws wafv2 update-regex-pattern-set \ --name``ExampleRegex`\ --scope`REGIONAL`\ --id`a1b2c3d4-5678-90ab-cdef-EXAMPLE11111`\ --regular-expression-list RegexString="^.+$" \ --lock-token`ed207e9c-82e9-4a77-aadd-81e6173ab7eb`Output: `{ "NextLockToken": "12ebc73e-fa68-417d-a9b8-2bdd761a4fa5" }`For more information, see [IP Sets and Regex Pattern Sets](https://docs.aws.amazon.com/waf/latest/developerguide/waf-referenced-set-managing.html)in the*AWS WAF, AWS Firewall Manager, and AWS Shield Advanced Developer Guide*.- 
                    For API details, see [UpdateRegexPatternSet](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/wafv2/update-regex-pattern-set.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `update-rule-group`.

- **AWS CLI**
- 
            
                    **To update a custom rule group**The following `update-rule-group`changes the visibility configuration for an existing custom rule group. This call requires an ID, which you can obtain from the call,`list-rule-groups`, and a lock token which you can obtain from the calls,`list-rule-groups`and`get-rule-group`. This call also returns a lock token that you can use for a subsequent update.`aws wafv2 update-rule-group \ --name``TestRuleGroup`\ --scope`REGIONAL`\ --id`a1b2c3d4-5678-90ab-cdef-EXAMPLE11111`\ --lock-token`7b3bcec2-0000-0000-0000-563bf47249f0`\ --visibility-config`SampledRequestsEnabled=false,CloudWatchMetricsEnabled=false,MetricName=TestMetricsForRuleGroup`\ --region`us-west-2`Output: `{ "NextLockToken": "1eb5ec48-0000-0000-0000-ee9b906c541e" }`For more information, see [Managing Your Own Rule Groups](https://docs.aws.amazon.com/waf/latest/developerguide/waf-user-created-rule-groups.html)in the*AWS WAF, AWS Firewall Manager, and AWS Shield Advanced Developer Guide*.- 
                    For API details, see [UpdateRuleGroup](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/wafv2/update-rule-group.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `update-web-acl`.

- **AWS CLI**
- 
            
                    **To update a web ACL**The following `update-web-acl`changes settings for an existing web ACL. This call requires an ID, which you can obtain from the call,`list-web-acls`, and a lock token and other settings, which you can obtain from the call`get-web-acl`. This call also returns a lock token that you can use for a subsequent update.`aws wafv2 update-web-acl \ --name``TestWebAcl`\ --scope`REGIONAL`\ --id`a1b2c3d4-5678-90ab-cdef-EXAMPLE11111`\ --lock-token`2294b3a1-0000-0000-0000-a3ae04329de9`\ --default-action`Block={}`\ --visibility-config`SampledRequestsEnabled=false,CloudWatchMetricsEnabled=false,MetricName=NewMetricTestWebAcl`\ --rules`file://waf-rule.json`\ --region`us-west-2`Output: `{ "NextLockToken": "714a0cfb-0000-0000-0000-2959c8b9a684" }`For more information, see [Managing and Using a Web Access Control List (Web ACL)](https://docs.aws.amazon.com/waf/latest/developerguide/web-acl.html)in the*AWS WAF, AWS Firewall Manager, and AWS Shield Advanced Developer Guide*.- 
                    For API details, see [UpdateWebAcl](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/wafv2/update-web-acl.html)in*AWS CLI Command Reference*.
 
-