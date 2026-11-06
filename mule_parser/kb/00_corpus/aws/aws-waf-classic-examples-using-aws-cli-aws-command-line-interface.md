# AWS WAF Classic examples using AWS CLI - AWS Command Line Interface

**Source:** [https://docs.aws.amazon.com/cli/latest/userguide/cli_waf_code_examples.html](https://docs.aws.amazon.com/cli/latest/userguide/cli_waf_code_examples.html)

---

The following code examples show you how to perform actions and implement common scenarios by using the AWS Command Line Interface with AWS WAF Classic.

*Actions* are code excerpts from larger programs and must be run in context. While actions show you how to call individual service functions, you can see actions in context in their related scenarios.

Each example includes a link to the complete source code, where you can find instructions on how to set up and run the code in context.

###### Topics

## Actions

    The following code example shows how to use `put-logging-configuration`.

- **AWS CLI**
- 
            
                    **To create a logging configuration for the web ACL ARN with the specified Kinesis Firehose stream ARN**The following `put-logging-configuration`example displays logging configuration for WAF with CloudFront.`aws waf put-logging-configuration \ --logging-configuration``ResourceArn=arn:aws:waf::123456789012:webacl/3bffd3ed-fa2e-445e-869f-a6a7cf153fd3,LogDestinationConfigs=arn:aws:firehose:us-east-1:123456789012:deliverystream/aws-waf-logs-firehose-stream,RedactedFields=[]`Output: `{ "LoggingConfiguration": { "ResourceArn": "arn:aws:waf::123456789012:webacl/3bffd3ed-fa2e-445e-869f-a6a7cf153fd3", "LogDestinationConfigs": [ "arn:aws:firehose:us-east-1:123456789012:deliverystream/aws-waf-logs-firehose-stream" ] } }`- 
                    For API details, see [PutLoggingConfiguration](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/waf/put-logging-configuration.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `update-byte-match-set`.

- **AWS CLI**
- 
            
                    **To update a byte match set**The following `update-byte-match-set`command deletes a ByteMatchTuple object (filter) in a ByteMatchSet:`aws waf update-byte-match-set --byte-match-set-id``a123fae4-b567-8e90-1234-5ab67ac8ca90`--change-token`12cs345-67cd-890b-1cd2-c3a4567d89f1`--updates Action="DELETE",ByteMatchTuple={FieldToMatch={Type="HEADER",Data="referer"},TargetString="badrefer1",TextTransformation="NONE",PositionalConstraint="CONTAINS"}For more information, see Working with String Match Conditions in the *AWS WAF*developer guide.- 
                    For API details, see [UpdateByteMatchSet](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/waf/update-byte-match-set.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `update-ip-set`.

- **AWS CLI**
- 
            
                    **To update an IP set**The following `update-ip-set`command updates an IPSet with an IPv4 address and deletes an IPv6 address:`aws waf update-ip-set --ip-set-id``a123fae4-b567-8e90-1234-5ab67ac8ca90`--change-token`12cs345-67cd-890b-1cd2-c3a4567d89f1`--updates Action="INSERT",IPSetDescriptor={Type="IPV4",Value="12.34.56.78/16"},Action="DELETE",IPSetDescriptor={Type="IPV6",Value="1111:0000:0000:0000:0000:0000:0000:0111/128"}Alternatively you can use a JSON file to specify the input. For example: `aws waf update-ip-set --ip-set-id``a123fae4-b567-8e90-1234-5ab67ac8ca90`--change-token`12cs345-67cd-890b-1cd2-c3a4567d89f1`--updates`file://change.json`Where content of the JSON file is: `[ { "Action": "INSERT", "IPSetDescriptor": { "Type": "IPV4", "Value": "12.34.56.78/16" } }, { "Action": "DELETE", "IPSetDescriptor": { "Type": "IPV6", "Value": "1111:0000:0000:0000:0000:0000:0000:0111/128" } } ]`For more information, see Working with IP Match Conditions in the *AWS WAF*developer guide.- 
                    For API details, see [UpdateIpSet](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/waf/update-ip-set.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `update-rule`.

- **AWS CLI**
- 
            
                    **To update a rule**The following `update-rule`command deletes a Predicate object in a rule:`aws waf update-rule --rule-id``a123fae4-b567-8e90-1234-5ab67ac8ca90`--change-token`12cs345-67cd-890b-1cd2-c3a4567d89f1`--updates Action="DELETE",Predicate={Negated=false,Type="ByteMatch",DataId="MyByteMatchSetID"}For more information, see Working with Rules in the *AWS WAF*developer guide.- 
                    For API details, see [UpdateRule](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/waf/update-rule.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `update-size-constraint-set`.

- **AWS CLI**
- 
            
                    **To update a size constraint set**The following `update-size-constraint-set`command deletes a SizeConstraint object (filters) in a size constraint set:`aws waf update-size-constraint-set --size-constraint-set-id``a123fae4-b567-8e90-1234-5ab67ac8ca90`--change-token`12cs345-67cd-890b-1cd2-c3a4567d89f1`--updates Action="DELETE",SizeConstraint={FieldToMatch={Type="QUERY_STRING"},TextTransformation="NONE",ComparisonOperator="GT",Size=0}For more information, see Working with Size Constraint Conditions in the *AWS WAF*developer guide.- 
                    For API details, see [UpdateSizeConstraintSet](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/waf/update-size-constraint-set.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `update-sql-injection-match-set`.

- **AWS CLI**
- 
            
                    **To update a SQL Injection Match Set**The following `update-sql-injection-match-set`command deletes a SqlInjectionMatchTuple object (filters) in a SQL injection match set:`aws waf update-sql-injection-match-set --sql-injection-match-set-id``a123fae4-b567-8e90-1234-5ab67ac8ca90`--change-token`12cs345-67cd-890b-1cd2-c3a4567d89f1`--updates Action="DELETE",SqlInjectionMatchTuple={FieldToMatch={Type="QUERY_STRING"},TextTransformation="URL_DECODE"}For more information, see Working with SQL Injection Match Conditions in the *AWS WAF*developer guide.- 
                    For API details, see [UpdateSqlInjectionMatchSet](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/waf/update-sql-injection-match-set.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `update-web-acl`.

- **AWS CLI**
- 
            
                    **To update a web ACL**The following `update-web-acl`command deletes an`ActivatedRule`object in a WebACL.aws waf update-web-acl --web-acl-id a123fae4-b567-8e90-1234-5ab67ac8ca90 --change-token 12cs345-67cd-890b-1cd2-c3a4567d89f1 --updates Action="DELETE",ActivatedRule='{Priority=1,RuleId="WAFRule-1-Example",Action={Type="ALLOW"},Type="REGULAR"}' Output: `{ "ChangeToken": "12cs345-67cd-890b-1cd2-c3a4567d89f1" }`For more information, see [Working with Web ACLs](https://docs.aws.amazon.com/waf/latest/developerguide/classic-web-acl-working-with.html)in the*AWS WAF, AWS Firewall Manager, and AWS Shield Advanced Developer Guide*.- 
                    For API details, see [UpdateWebAcl](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/waf/update-web-acl.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `update-xss-match-set`.

- **AWS CLI**
- 
            
                    **To update an XSSMatchSet**The following `update-xss-match-set`command deletes an XssMatchTuple object (filters) in an XssMatchSet:`aws waf update-xss-match-set --xss-match-set-id``a123fae4-b567-8e90-1234-5ab67ac8ca90`--change-token`12cs345-67cd-890b-1cd2-c3a4567d89f1`--updates Action="DELETE",XssMatchTuple={FieldToMatch={Type="QUERY_STRING"},TextTransformation="URL_DECODE"}For more information, see Working with Cross-site Scripting Match Conditions in the *AWS WAF*developer guide.- 
                    For API details, see [UpdateXssMatchSet](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/waf/update-xss-match-set.html)in*AWS CLI Command Reference*.
 
-