# Route 53 examples using AWS CLI - AWS Command Line Interface

**Source:** [https://docs.aws.amazon.com/cli/latest/userguide/cli_route-53_code_examples.html](https://docs.aws.amazon.com/cli/latest/userguide/cli_route-53_code_examples.html)

---

The following code examples show you how to perform actions and implement common scenarios by using the AWS Command Line Interface with Route 53.

*Actions* are code excerpts from larger programs and must be run in context. While actions show you how to call individual service functions, you can see actions in context in their related scenarios.

Each example includes a link to the complete source code, where you can find instructions on how to set up and run the code in context.

###### Topics

## Actions

    The following code example shows how to use `change-resource-record-sets`.

- **AWS CLI**
- 
            
                    **To create, update, or delete a resource record set**The following `change-resource-record-sets`command creates a resource record set using the`hosted-zone-id``Z1R8UBAEXAMPLE`and the JSON-formatted configuration in the file`C:\awscli\route53\change-resource-record-sets.json`:`aws route53 change-resource-record-sets --hosted-zone-id``Z1R8UBAEXAMPLE`--change-batch file://C:\awscli\route53\change-resource-record-sets.jsonFor more information, see POST ChangeResourceRecordSets in the *Amazon Route 53 API Reference*.The configuration in the JSON file depends on the kind of resource record set you want to create: BasicWeightedAliasWeighted AliasLatencyLatency AliasFailoverFailover Alias **Basic Syntax**:`{ "Comment": "optional comment about the changes in this change batch request", "Changes": [ { "Action": "CREATE"|"DELETE"|"UPSERT", "ResourceRecordSet": { "Name": "DNS domain name", "Type": "SOA"|"A"|"TXT"|"NS"|"CNAME"|"MX"|"PTR"|"SRV"|"SPF"|"AAAA", "TTL": time to live in seconds, "ResourceRecords": [ { "Value": "applicable value for the record type" }, {...} ] } }, {...} ] }`**Weighted Syntax**:`{ "Comment": "optional comment about the changes in this change batch request", "Changes": [ { "Action": "CREATE"|"DELETE"|"UPSERT", "ResourceRecordSet": { "Name": "DNS domain name", "Type": "SOA"|"A"|"TXT"|"NS"|"CNAME"|"MX"|"PTR"|"SRV"|"SPF"|"AAAA", "SetIdentifier": "unique description for this resource record set", "Weight": value between 0 and 255, "TTL": time to live in seconds, "ResourceRecords": [ { "Value": "applicable value for the record type" }, {...} ], "HealthCheckId": "optional ID of an Amazon Route 53 health check" } }, {...} ] }`**Alias Syntax**:`{ "Comment": "optional comment about the changes in this change batch request", "Changes": [ { "Action": "CREATE"|"DELETE"|"UPSERT", "ResourceRecordSet": { "Name": "DNS domain name", "Type": "SOA"|"A"|"TXT"|"NS"|"CNAME"|"MX"|"PTR"|"SRV"|"SPF"|"AAAA", "AliasTarget": { "HostedZoneId": "hosted zone ID for your CloudFront distribution, Amazon S3 bucket, Elastic Load Balancing load balancer, or Amazon Route 53 hosted zone", "DNSName": "DNS domain name for your CloudFront distribution, Amazon S3 bucket, Elastic Load Balancing load balancer, or another resource record set in this hosted zone", "EvaluateTargetHealth": true|false }, "HealthCheckId": "optional ID of an Amazon Route 53 health check" } }, {...} ] }`**Weighted Alias Syntax**:`{ "Comment": "optional comment about the changes in this change batch request", "Changes": [ { "Action": "CREATE"|"DELETE"|"UPSERT", "ResourceRecordSet": { "Name": "DNS domain name", "Type": "SOA"|"A"|"TXT"|"NS"|"CNAME"|"MX"|"PTR"|"SRV"|"SPF"|"AAAA", "SetIdentifier": "unique description for this resource record set", "Weight": value between 0 and 255, "AliasTarget": { "HostedZoneId": "hosted zone ID for your CloudFront distribution, Amazon S3 bucket, Elastic Load Balancing load balancer, or Amazon Route 53 hosted zone", "DNSName": "DNS domain name for your CloudFront distribution, Amazon S3 bucket, Elastic Load Balancing load balancer, or another resource record set in this hosted zone", "EvaluateTargetHealth": true|false }, "HealthCheckId": "optional ID of an Amazon Route 53 health check" } }, {...} ] }`**Latency Syntax**:`{ "Comment": "optional comment about the changes in this change batch request", "Changes": [ { "Action": "CREATE"|"DELETE"|"UPSERT", "ResourceRecordSet": { "Name": "DNS domain name", "Type": "SOA"|"A"|"TXT"|"NS"|"CNAME"|"MX"|"PTR"|"SRV"|"SPF"|"AAAA", "SetIdentifier": "unique description for this resource record set", "Region": "Amazon EC2 region name", "TTL": time to live in seconds, "ResourceRecords": [ { "Value": "applicable value for the record type" }, {...} ], "HealthCheckId": "optional ID of an Amazon Route 53 health check" } }, {...} ] }`**Latency Alias Syntax**:`{ "Comment": "optional comment about the changes in this change batch request", "Changes": [ { "Action": "CREATE"|"DELETE"|"UPSERT", "ResourceRecordSet": { "Name": "DNS domain name", "Type": "SOA"|"A"|"TXT"|"NS"|"CNAME"|"MX"|"PTR"|"SRV"|"SPF"|"AAAA", "SetIdentifier": "unique description for this resource record set", "Region": "Amazon EC2 region name", "AliasTarget": { "HostedZoneId": "hosted zone ID for your CloudFront distribution, Amazon S3 bucket, Elastic Load Balancing load balancer, or Amazon Route 53 hosted zone", "DNSName": "DNS domain name for your CloudFront distribution, Amazon S3 bucket, Elastic Load Balancing load balancer, or another resource record set in this hosted zone", "EvaluateTargetHealth": true|false }, "HealthCheckId": "optional ID of an Amazon Route 53 health check" } }, {...} ] }`**Failover Syntax**:`{ "Comment": "optional comment about the changes in this change batch request", "Changes": [ { "Action": "CREATE"|"DELETE"|"UPSERT", "ResourceRecordSet": { "Name": "DNS domain name", "Type": "SOA"|"A"|"TXT"|"NS"|"CNAME"|"MX"|"PTR"|"SRV"|"SPF"|"AAAA", "SetIdentifier": "unique description for this resource record set", "Failover": "PRIMARY" | "SECONDARY", "TTL": time to live in seconds, "ResourceRecords": [ { "Value": "applicable value for the record type" }, {...} ], "HealthCheckId": "ID of an Amazon Route 53 health check" } }, {...} ] }`**Failover Alias Syntax**:`{ "Comment": "optional comment about the changes in this change batch request", "Changes": [ { "Action": "CREATE"|"DELETE"|"UPSERT", "ResourceRecordSet": { "Name": "DNS domain name", "Type": "SOA"|"A"|"TXT"|"NS"|"CNAME"|"MX"|"PTR"|"SRV"|"SPF"|"AAAA", "SetIdentifier": "unique description for this resource record set", "Failover": "PRIMARY" | "SECONDARY", "AliasTarget": { "HostedZoneId": "hosted zone ID for your CloudFront distribution, Amazon S3 bucket, Elastic Load Balancing load balancer, or Amazon Route 53 hosted zone", "DNSName": "DNS domain name for your CloudFront distribution, Amazon S3 bucket, Elastic Load Balancing load balancer, or another resource record set in this hosted zone", "EvaluateTargetHealth": true|false }, "HealthCheckId": "optional ID of an Amazon Route 53 health check" } }, {...} ] }`- 
                    For API details, see [ChangeResourceRecordSets](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/route53/change-resource-record-sets.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `change-tags-for-resource`.

- **AWS CLI**
- 
            
                    The following command adds a tag named `owner`to a healthcheck resource specified by ID:`aws route53 change-tags-for-resource --resource-type``healthcheck`--resource-id`6233434j-18c1-34433-ba8e-3443434`--add-tags`Key=owner,Value=myboss`The following command removes a tag named `owner`from a hosted zone resource specified by ID:`aws route53 change-tags-for-resource --resource-type``hostedzone`--resource-id`Z1523434445`--remove-tag-keys`owner`- 
                    For API details, see [ChangeTagsForResource](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/route53/change-tags-for-resource.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `create-health-check`.

- **AWS CLI**
- 
            
                    **To create a health check**The following `create-health-check`command creates a health check using the caller reference`2014-04-01-18:47`and the JSON-formatted configuration in the file`C:\awscli\route53\create-health-check.json`:`aws route53 create-health-check --caller-reference``2014-04-01-18:47`--health-check-config file://C:\awscli\route53\create-health-check.jsonJSON syntax: `{ "IPAddress": "IP address of the endpoint to check", "Port": port on the endpoint to check--required when Type is "TCP", "Type": "HTTP"|"HTTPS"|"HTTP_STR_MATCH"|"HTTPS_STR_MATCH"|"TCP", "ResourcePath": "path of the file that you want Amazon Route 53 to request--all Types except TCP", "FullyQualifiedDomainName": "domain name of the endpoint to check--all Types except TCP", "SearchString": "if Type is HTTP_STR_MATCH or HTTPS_STR_MATCH, the string to search for in the response body from the specified resource", "RequestInterval": 10 | 30, "FailureThreshold": integer between 1 and 10 }`To add the health check to a Route 53 resource record set, use the `change-resource-record-sets`command.For more information, see Amazon Route 53 Health Checks and DNS Failover in the *Amazon Route 53 Developer Guide*.- 
                    For API details, see [CreateHealthCheck](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/route53/create-health-check.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `create-hosted-zone`.

- **AWS CLI**
- 
            
                    **To create a hosted zone**The following `create-hosted-zone`command adds a hosted zone named`example.com`using the caller reference`2014-04-01-18:47`. The optional comment includes a space, so it must be enclosed in quotation marks:`aws route53 create-hosted-zone --name``example.com`--caller-reference`2014-04-01-18:47`--hosted-zone-config Comment="command-line version"For more information, see Working with Hosted Zones in the *Amazon Route 53 Developer Guide*.- 
                    For API details, see [CreateHostedZone](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/route53/create-hosted-zone.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `delete-health-check`.

- **AWS CLI**
- 
            
                    **To delete a health check**The following `delete-health-check`command deletes the health check with a`health-check-id`of`e75b48d9-547a-4c3d-88a5-ae4002397608`:`aws route53 delete-health-check --health-check-id``e75b48d9-547a-4c3d-88a5-ae4002397608`- 
                    For API details, see [DeleteHealthCheck](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/route53/delete-health-check.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `delete-hosted-zone`.

- **AWS CLI**
- 
            
                    **To delete a hosted zone**The following `delete-hosted-zone`command deletes the hosted zone with an`id`of`Z36KTIQEXAMPLE`:`aws route53 delete-hosted-zone --id``Z36KTIQEXAMPLE`- 
                    For API details, see [DeleteHostedZone](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/route53/delete-hosted-zone.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `get-change`.

- **AWS CLI**
- 
            
                    **To get the status of a change to resource record sets**The following `get-change`command gets the status and other information about the`change-resource-record-sets`request that has an`Id`of`/change/CWPIK4URU2I5S`:`aws route53 get-change --id``/change/CWPIK4URU2I5S`- 
                    For API details, see [GetChange](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/route53/get-change.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `get-health-check`.

- **AWS CLI**
- 
            
                    **To get information about a health check**The following `get-health-check`command gets information about the health check that has a`health-check-id`of`02ec8401-9879-4259-91fa-04e66d094674`:`aws route53 get-health-check --health-check-id``02ec8401-9879-4259-91fa-04e66d094674`- 
                    For API details, see [GetHealthCheck](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/route53/get-health-check.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `get-hosted-zone`.

- **AWS CLI**
- 
            
                    **To get information about a hosted zone**The following `get-hosted-zone`command gets information about the hosted zone with an`id`of`Z1R8UBAEXAMPLE`:`aws route53 get-hosted-zone --id``Z1R8UBAEXAMPLE`- 
                    For API details, see [GetHostedZone](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/route53/get-hosted-zone.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `list-health-checks`.

- **AWS CLI**
- 
            
                    **To list the health checks associated with the current AWS account**The following `list-health-checks`command lists detailed information about the first 100 health checks that are associated with the current AWS account.:`aws route53 list-health-checks`If you have more than 100 health checks, or if you want to list them in groups smaller than 100, include the `--maxitems`parameter. For example, to list health checks one at a time, use the following command:`aws route53 list-health-checks --max-items``1`To view the next health check, take the value of `NextToken`from the response to the previous command, and include it in the`--starting-token`parameter, for example:`aws route53 list-health-checks --max-items``1`--starting-token`Z3M3LMPEXAMPLE`- 
                    For API details, see [ListHealthChecks](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/route53/list-health-checks.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `list-hosted-zones-by-name`.

- **AWS CLI**
- 
            
                    The following command lists up to 100 hosted zones ordered by domain name: `aws route53 list-hosted-zones-by-name`Output: `{ "HostedZones": [ { "ResourceRecordSetCount": 2, "CallerReference": "test20150527-2", "Config": { "Comment": "test2", "PrivateZone": false }, "Id": "/hostedzone/Z119WBBTVP5WFX", "Name": "2.example.com." }, { "ResourceRecordSetCount": 2, "CallerReference": "test20150527-1", "Config": { "Comment": "test", "PrivateZone": false }, "Id": "/hostedzone/Z3P5QSUBK4POTI", "Name": "www.example.com." } ], "IsTruncated": false, "MaxItems": "100" }`The following command lists hosted zones ordered by name, beginning with `www.example.com`:`aws route53 list-hosted-zones-by-name --dns-name``www.example.com`Output: `{ "HostedZones": [ { "ResourceRecordSetCount": 2, "CallerReference": "mwunderl20150527-1", "Config": { "Comment": "test", "PrivateZone": false }, "Id": "/hostedzone/Z3P5QSUBK4POTI", "Name": "www.example.com." } ], "DNSName": "www.example.com", "IsTruncated": false, "MaxItems": "100" }`- 
                    For API details, see [ListHostedZonesByName](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/route53/list-hosted-zones-by-name.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `list-hosted-zones`.

- **AWS CLI**
- 
            
                    **To list the hosted zones associated with the current AWS account**The following `list-hosted-zones`command lists summary information about the first 100 hosted zones that are associated with the current AWS account.:`aws route53 list-hosted-zones`If you have more than 100 hosted zones, or if you want to list them in groups smaller than 100, include the `--max-items`parameter. For example, to list hosted zones one at a time, use the following command:`aws route53 list-hosted-zones --max-items``1`To view information about the next hosted zone, take the value of `NextToken`from the response to the previous command, and include it in the`--starting-token`parameter, for example:`aws route53 list-hosted-zones --max-items``1`--starting-token`Z3M3LMPEXAMPLE`- 
                    For API details, see [ListHostedZones](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/route53/list-hosted-zones.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `list-query-logging-configs`.

- **AWS CLI**
- 
            
                    **To list query logging configurations**The following `list-query-logging-configs`example lists information about the first 100 query logging configurations in your AWS account, for the hosted zone`Z1OX3WQEXAMPLE`.`aws route53 list-query-logging-configs \ --hosted-zone-id``Z1OX3WQEXAMPLE`Output: `{ "QueryLoggingConfigs": [ { "Id": "964ff34e-ae03-4f06-80a2-9683cexample", "HostedZoneId": "Z1OX3WQEXAMPLE", "CloudWatchLogsLogGroupArn": "arn:aws:logs:us-east-1:111122223333:log-group:/aws/route53/example.com:*" } ] }`For more information, see [Logging DNS queries](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/query-logs.html)in the*Amazon Route 53 Developer Guide*.- 
                    For API details, see [ListQueryLoggingConfigs](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/route53/list-query-logging-configs.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `list-resource-record-sets`.

- **AWS CLI**
- 
            
                    **To list the resource record sets in a hosted zone**The following `list-resource-record-sets`command lists summary information about the first 100 resource record sets in a specified hosted zone.:`aws route53 list-resource-record-sets --hosted-zone-id``Z2LD58HEXAMPLE`If the hosted zone contains more than 100 resource record sets, or if you want to list them in groups smaller than 100, include the `--maxitems`parameter. For example, to list resource record sets one at a time, use the following command:`aws route53 list-resource-record-sets --hosted-zone-id``Z2LD58HEXAMPLE`--max-items`1`To view information about the next resource record set in the hosted zone, take the value of `NextToken`from the response to the previous command, and include it in the`--starting-token`parameter, for example:`aws route53 list-resource-record-sets --hosted-zone-id``Z2LD58HEXAMPLE`--max-items`1`--starting-token`Z3M3LMPEXAMPLE`To view all the resource record sets of a particular name, use the `--query`parameter to filter them out. For example:`aws route53 list-resource-record-sets --hosted-zone-id``Z2LD58HEXAMPLE`--query`"ResourceRecordSets[?Name == 'example.domain.']"`- 
                    For API details, see [ListResourceRecordSets](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/route53/list-resource-record-sets.html)in*AWS CLI Command Reference*.
 
-