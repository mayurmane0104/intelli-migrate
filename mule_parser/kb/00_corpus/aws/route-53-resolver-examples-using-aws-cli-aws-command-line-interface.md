# Route 53 Resolver examples using AWS CLI - AWS Command Line Interface

**Source:** [https://docs.aws.amazon.com/cli/latest/userguide/cli_route53resolver_code_examples.html](https://docs.aws.amazon.com/cli/latest/userguide/cli_route53resolver_code_examples.html)

---

The following code examples show you how to perform actions and implement common scenarios by using the AWS Command Line Interface with Route 53 Resolver.

*Actions* are code excerpts from larger programs and must be run in context. While actions show you how to call individual service functions, you can see actions in context in their related scenarios.

Each example includes a link to the complete source code, where you can find instructions on how to set up and run the code in context.

###### Topics

## Actions

    The following code example shows how to use `associate-firewall-rule-group`.

- **AWS CLI**
- 
            
                    **To associate a firewall rule group with a VPC**The following `associate-firewall-rule-group`example associates a DNS Firewall rule group with an Amazon VPC.`aws route53resolver associate-firewall-rule-group \ --name``test-association`\ --firewall-rule-group-id`rslvr-frg-47f93271fexample`\ --vpc-id`vpc-31e92222`\ --priority`101`Output: `{ "FirewallRuleGroupAssociation": { "Id": "rslvr-frgassoc-57e8873d7example", "Arn": "arn:aws:route53resolver:us-west-2:123456789012:firewall-rule-group-association/rslvr-frgassoc-57e8873d7example", "FirewallRuleGroupId": "rslvr-frg-47f93271fexample", "VpcId": "vpc-31e92222", "Name": "test-association", "Priority": 101, "MutationProtection": "DISABLED", "Status": "UPDATING", "StatusMessage": "Creating Firewall Rule Group Association", "CreatorRequestId": "2ca1a304-32b3-4f5f-bc4c-EXAMPLE11111", "CreationTime": "2021-05-25T21:47:48.755768Z", "ModificationTime": "2021-05-25T21:47:48.755768Z" } }`For more information, see [Managing associations between your VPC and Route 53 Resolver DNS Firewall rule groups](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/resolver-dns-firewall-vpc-associating-rule-group.html)in the*Amazon Route 53 Developer Guide*.- 
                    For API details, see [AssociateFirewallRuleGroup](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/route53resolver/associate-firewall-rule-group.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `associate-resolver-endpoint-ip-address`.

- **AWS CLI**
- 
            
                    **To associate another IP address with a Resolver endpoint**The following `associate-resolver-endpoint-ip-address`example associates another IP address with an inbound Resolver endpoint. If you specify only a subnet ID and omit the IP address from the`--ip-address`parameter, Resolver chooses an IP address for you from among the available IP addresses in the specified subnet.`aws route53resolver associate-resolver-endpoint-ip-address \ --resolver-endpoint-id``rslvr-in-497098ad5example`\ --ip-address="SubnetId=subnet-12d8exam,Ip=192.0.2.118"Output: `{ "ResolverEndpoint": { "Id": "rslvr-in-497098ad5example", "CreatorRequestId": "AWSConsole.25.0123456789", "Arn": "arn:aws:route53resolver:us-west-2:111122223333:resolver-endpoint/rslvr-in-497098ad5example", "Name": "my-inbound-endpoint", "SecurityGroupIds": [ "sg-05cd7b25d6example" ], "Direction": "INBOUND", "IpAddressCount": 3, "HostVPCId": "vpc-304bexam", "Status": "UPDATING", "StatusMessage": "Updating the Resolver Endpoint", "CreationTime": "2020-01-02T23:25:45.538Z", "ModificationTime": "2020-01-02T23:25:45.538Z" } }`For more information, see [Values That You Specify When You Create or Edit Inbound Endpoints](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/resolver-forwarding-inbound-queries.html#resolver-forwarding-inbound-queries-values)in the*Amazon Route 53 Developer Guide*.- 
                    For API details, see [AssociateResolverEndpointIpAddress](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/route53resolver/associate-resolver-endpoint-ip-address.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `associate-resolver-rule`.

- **AWS CLI**
- 
            
                    **To associate a Resolver rule with a VPC**The following `associate-resolver-rule`example associates a Resolver rule with an Amazon VPC. After you run the command, Resolver starts to forward DNS queries to your network based on the settings in the rule, such as the domain name of the queries that are forwarded.`aws route53resolver associate-resolver-rule \ --name``my-resolver-rule-association`\ --resolver-rule-id`rslvr-rr-42b60677c0example`\ --vpc-id`vpc-304bexam`Output: `{ "ResolverRuleAssociation": { "Id": "rslvr-rrassoc-d61cbb2c8bexample", "ResolverRuleId": "rslvr-rr-42b60677c0example", "Name": "my-resolver-rule-association", "VPCId": "vpc-304bexam", "Status": "CREATING", "StatusMessage": "[Trace id: 1-5dc5a8fa-ec2cc480d2ef07617example] Creating the association." } }`For more information, see [Forwarding Outbound DNS Queries to Your Network](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/resolver-forwarding-outbound-queries.html)in the*Amazon Route 53 Developer Guide*.- 
                    For API details, see [AssociateResolverRule](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/route53resolver/associate-resolver-rule.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `create-firewall-domain-list`.

- **AWS CLI**
- 
            
                    **To create a Route 53 Resolver DNS Firewall domain list**The following `create-firewall-domain-list`example creates a Route 53 Resolver DNS Firewall domain list, named test, in your AWS account.`aws route53resolver create-firewall-domain-list \ --creator-request-id``my-request-id`\ --name`test`Output: `{ "FirewallDomainList": { "Id": "rslvr-fdl-d61cbb2cbexample", "Arn": "arn:aws:route53resolver:us-west-2:123456789012:firewall-domain-list/rslvr-fdl-d61cbb2cbexample", "Name": "test", "DomainCount": 0, "Status": "COMPLETE", "StatusMessage": "Created Firewall Domain List", "CreatorRequestId": "my-request-id", "CreationTime": "2021-05-25T15:55:51.115365Z", "ModificationTime": "2021-05-25T15:55:51.115365Z" } }`For more information, see [Managing your own domain lists](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/resolver-dns-firewall-user-managed-domain-lists.html)in the*Amazon Route 53 Developer Guide*.- 
                    For API details, see [CreateFirewallDomainList](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/route53resolver/create-firewall-domain-list.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `create-firewall-rule-group`.

- **AWS CLI**
- 
            
                    **To create a Firewall rule group**The following `create-firewall-rule-group`example creates a DNS Firewall rule group.`aws route53resolver create-firewall-rule-group \ --creator-request-id``my-request-id`\ --name`test`Output: `{ "FirewallRuleGroup": { "Id": "rslvr-frg-47f93271fexample", "Arn": "arn:aws:route53resolver:us-west-2:123456789012:firewall-rule-group/rslvr-frg-47f93271fexample", "Name": "test", "RuleCount": 0, "Status": "COMPLETE", "StatusMessage": "Created Firewall Rule Group", "OwnerId": "123456789012", "CreatorRequestId": "my-request-id", "ShareStatus": "NOT_SHARED", "CreationTime": "2021-05-25T18:59:26.490017Z", "ModificationTime": "2021-05-25T18:59:26.490017Z" } }`For more information, see [Managing rule groups and rules in DNS Firewall](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/resolver-dns-firewall-rule-group-managing.html)in the*Amazon Route 53 Developer Guide*.- 
                    For API details, see [CreateFirewallRuleGroup](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/route53resolver/create-firewall-rule-group.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `create-firewall-rule`.

- **AWS CLI**
- 
            
                    **To create a firewall rule**The following `create-firewall-rule`example creates a firewall rule in a DNS Firewall rule for domains listed in a DNS Firewall domain list.`aws route53resolver create-firewall-rule \ --name``allow-rule`\ --firewall-rule-group-id`rslvr-frg-47f93271fexample`\ --firewall-domain-list-id`rslvr-fdl-9e956e9ffexample`\ --priority`101`\ --action`ALLOW`Output: `{ "FirewallRule": { "FirewallRuleGroupId": "rslvr-frg-47f93271fexample", "FirewallDomainListId": "rslvr-fdl-9e956e9ffexample", "Name": "allow-rule", "Priority": 101, "Action": "ALLOW", "CreatorRequestId": "d81e3fb7-020b-415e-939f-EXAMPLE11111", "CreationTime": "2021-05-25T21:44:00.346093Z", "ModificationTime": "2021-05-25T21:44:00.346093Z" } }`For more information, see [Managing rule groups and rules in DNS Firewall](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/resolver-dns-firewall-rule-group-managing.html)in the*Amazon Route 53 Developer Guide*.- 
                    For API details, see [CreateFirewallRule](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/route53resolver/create-firewall-rule.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `create-resolver-endpoint`.

- **AWS CLI**
- 
            
                    **To create an inbound Resolver endpoint**The following `create-resolver-endpoint`example creates an inbound Resolver endpoint. You can use the same command to create both inbound and outbound endpoints.aws route53resolver create-resolver-endpoint --name my-inbound-endpoint --creator-request-id 2020-01-01-18:47 --security-group-ids "sg-f62bexam" --direction INBOUND --ip-addresses SubnetId=subnet-ba47exam,Ip=192.0.2.255 SubnetId=subnet-12d8exam,Ip=192.0.2.254 Output: `{ "ResolverEndpoint": { "Id": "rslvr-in-f9ab8a03f1example", "CreatorRequestId": "2020-01-01-18:47", "Arn": "arn:aws:route53resolver:us-west-2:111122223333:resolver-endpoint/rslvr-in-f9ab8a03f1example", "Name": "my-inbound-endpoint", "SecurityGroupIds": [ "sg-f62bexam" ], "Direction": "INBOUND", "IpAddressCount": 2, "HostVPCId": "vpc-304examp", "Status": "CREATING", "StatusMessage": "[Trace id: 1-5dc1ff84-f3477826e4a190025example] Creating the Resolver Endpoint", "CreationTime": "2020-01-01T23:02:29.583Z", "ModificationTime": "2020-01-01T23:02:29.583Z" } }`**To create an outbound Resolver endpoint**The following `create-resolver-endpoint`example creates an outbound resolver endpoint using the values in the JSON-formatted document`create-outbound-resolver-endpoint.json`.`aws route53resolver create-resolver-endpoint \ --cli-input-json file://c:\temp\create-outbound-resolver-endpoint.json`Contents of `create-outbound-resolver-endpoint.json`:`{ "CreatorRequestId": "2020-01-01-18:47", "Direction": "OUTBOUND", "IpAddresses": [ { "Ip": "192.0.2.255", "SubnetId": "subnet-ba47exam" }, { "Ip": "192.0.2.254", "SubnetId": "subnet-12d8exam" } ], "Name": "my-outbound-endpoint", "SecurityGroupIds": [ "sg-05cd7b25d6example" ], "Tags": [ { "Key": "my-key-name", "Value": "my-key-value" } ] }`For more information, see [Resolving DNS Queries Between VPCs and Your Network](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/resolver.html)in the*Amazon Route 53 Developer Guide*.- 
                    For API details, see [CreateResolverEndpoint](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/route53resolver/create-resolver-endpoint.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `create-resolver-rule`.

- **AWS CLI**
- 
            
                    **To create a Resolver rule**The following `create-resolver-rule`example creates a Resolver forwarding rule. The rule uses the outbound endpoint rslvr-out-d5e5920e37example to forward DNS queries for`example.com`to the IP addresses 10.24.8.75 and 10.24.8.156.`aws route53resolver create-resolver-rule \ --creator-request-id``2020-01-02-18:47`\ --domain-name`example.com`\ --name`my-rule`\ --resolver-endpoint-id`rslvr-out-d5e5920e37example`\ --rule-type`FORWARD`\ --target-ips`"Ip=10.24.8.75"``"Ip=10.24.8.156"`Output: `{ "ResolverRule": { "Status": "COMPLETE", "RuleType": "FORWARD", "ResolverEndpointId": "rslvr-out-d5e5920e37example", "Name": "my-rule", "DomainName": "example.com.", "CreationTime": "2022-05-10T21:35:30.923187Z", "TargetIps": [ { "Ip": "10.24.8.75", "Port": 53 }, { "Ip": "10.24.8.156", "Port": 53 } ], "CreatorRequestId": "2022-05-10-16:33", "ModificationTime": "2022-05-10T21:35:30.923187Z", "ShareStatus": "NOT_SHARED", "Arn": "arn:aws:route53resolver:us-east-1:111117012054:resolver-rule/rslvr-rr-b1e0b905e93611111", "OwnerId": "111111111111", "Id": "rslvr-rr-rslvr-rr-b1e0b905e93611111", "StatusMessage": "[Trace id: 1-22222222-3e56afcc71a3724664f22e24] Successfully created Resolver Rule." } }`- 
                    For API details, see [CreateResolverRule](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/route53resolver/create-resolver-rule.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `delete-firewall-domain-list`.

- **AWS CLI**
- 
            
                    **To delete a Route 53 Resolver DNS Firewall domain list**The following `delete-firewall-domain-list`example deletes a Route 53 Resolver DNS Firewall domain list, named test, in your AWS account.`aws route53resolver delete-firewall-domain-list \ --firewall-domain-list-id``rslvr-fdl-9e956e9ffexample`Output: `{ "FirewallDomainList": { "Id": "rslvr-fdl-9e956e9ffexample", "Arn": "arn:aws:route53resolver:us-west-2:123456789012:firewall-domain-list/rslvr-fdl-9e956e9ffexample", "Name": "test", "DomainCount": 6, "Status": "DELETING", "StatusMessage": "Deleting the Firewall Domain List", "CreatorRequestId": "my-request-id", "CreationTime": "2021-05-25T15:55:51.115365Z", "ModificationTime": "2021-05-25T18:58:05.588024Z" } }`For more information, see [Managing your own domain lists](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/resolver-dns-firewall-user-managed-domain-lists.html)in the*Amazon Route 53 Developer Guide*.- 
                    For API details, see [DeleteFirewallDomainList](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/route53resolver/delete-firewall-domain-list.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `delete-firewall-rule-group`.

- **AWS CLI**
- 
            
                    **To delete a firewall rule group**The following `delete-firewall-rule-group`example deletes a firewall rule group.`aws route53resolver delete-firewall-rule-group \ --firewall-rule-group-id``rslvr-frg-47f93271fexample`Output: `{ "FirewallRuleGroup": { "Id": "rslvr-frg-47f93271fexample", "Arn": "arn:aws:route53resolver:us-west-2:123456789012:firewall-rule-group/rslvr-frg-47f93271fexample", "Name": "test", "RuleCount": 0, "Status": "UPDATING", "StatusMessage": "Updating Firewall Rule Group", "OwnerId": "123456789012", "CreatorRequestId": "my-request-id", "ShareStatus": "NOT_SHARED", "CreationTime": "2021-05-25T18:59:26.490017Z", "ModificationTime": "2021-05-25T21:51:53.028688Z" } }`For more information, see [Managing rule groups and rules in DNS Firewall](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/resolver-dns-firewall-rule-group-managing.html)in the*Amazon Route 53 Developer Guide*.- 
                    For API details, see [DeleteFirewallRuleGroup](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/route53resolver/delete-firewall-rule-group.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `delete-firewall-rule`.

- **AWS CLI**
- 
            
                    **To delete a firewall rule**The following `delete-firewall-rule`example deletes a specified firewall rule.`aws route53resolver delete-firewall-rule \ --firewall-rule-group-id``rslvr-frg-47f93271fexample`\ --firewall-domain-list-id`rslvr-fdl-9e956e9ffexample`Output: `{ "FirewallRule": { "FirewallRuleGroupId": "rslvr-frg-47f93271fexample", "FirewallDomainListId": "rslvr-fdl-9e956e9ffexample", "Name": "allow-rule", "Priority": 102, "Action": "ALLOW", "CreatorRequestId": "d81e3fb7-020b-415e-939f-EXAMPLE11111", "CreationTime": "2021-05-25T21:44:00.346093Z", "ModificationTime": "2021-05-25T21:45:59.611600Z" } }`For more information, see [Managing rule groups and rules in DNS Firewall](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/resolver-dns-firewall-rule-group-managing.html)in the*Amazon Route 53 Developer Guide*.- 
                    For API details, see [DeleteFirewallRule](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/route53resolver/delete-firewall-rule.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `delete-resolver-endpoint`.

- **AWS CLI**
- 
            
                    **To delete a Resolver endpoint**The following `delete-resolver-endpoint`example deletes the specified endpoint.**Important**If you delete an inbound endpoint, DNS queries from your network are no longer forwarded to Resolver in the VPC that you specified in the endpoint. If you delete an outbound endpoint, Resolver stops forwarding DNS queries from your VPC to your network for rules that specify the deleted outbound endpoint.`aws route53resolver delete-resolver-endpoint \ --resolver-endpoint-id``rslvr-in-497098ad59example`Output: `{ "ResolverEndpoint": { "Id": "rslvr-in-497098ad59example", "CreatorRequestId": "AWSConsole.25.157290example", "Arn": "arn:aws:route53resolver:us-west-2:111122223333:resolver-endpoint/rslvr-in-497098ad59example", "Name": "my-inbound-endpoint", "SecurityGroupIds": [ "sg-05cd7b25d6example" ], "Direction": "INBOUND", "IpAddressCount": 5, "HostVPCId": "vpc-304bexam", "Status": "DELETING", "StatusMessage": "[Trace id: 1-5dc5b658-811b5be0922bbc382example] Deleting ResolverEndpoint.", "CreationTime": "2020-01-01T23:25:45.538Z", "ModificationTime": "2020-01-02T23:25:45.538Z" } }`- 
                    For API details, see [DeleteResolverEndpoint](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/route53resolver/delete-resolver-endpoint.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `delete-resolver-rule`.

- **AWS CLI**
- 
            
                    **To delete a Resolver rule**The following `delete-resolver-rule`example deletes the specified rule.**Note**If a rule is associated with any VPCs, you must first disassociate the rule from the VPCs before you can delete it.`aws route53resolver delete-resolver-rule \ --resolver-rule-id``rslvr-rr-5b3809426bexample`Output: `{ "ResolverRule": { "Id": "rslvr-rr-5b3809426bexample", "CreatorRequestId": "2020-01-03-18:47", "Arn": "arn:aws:route53resolver:us-west-2:111122223333:resolver-rule/rslvr-rr-5b3809426bexample", "DomainName": "zenith.example.com.", "Status": "DELETING", "StatusMessage": "[Trace id: 1-5dc5e05b-602e67b052cb74f05example] Deleting Resolver Rule.", "RuleType": "FORWARD", "Name": "my-resolver-rule", "TargetIps": [ { "Ip": "192.0.2.50", "Port": 53 } ], "ResolverEndpointId": "rslvr-out-d5e5920e3example", "OwnerId": "111122223333", "ShareStatus": "NOT_SHARED" } }`- 
                    For API details, see [DeleteResolverRule](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/route53resolver/delete-resolver-rule.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `disassociate-firewall-rule-group`.

- **AWS CLI**
- 
            
                    **To disassociate a firewall rule group from a VPC**The following `disassociate-firewall-rule-group`example disassociates a DNS Firewall rule group from an Amazon VPC.`aws route53resolver disassociate-firewall-rule-group \ --firewall-rule-group-association-id``rslvr-frgassoc-57e8873d7example`Output: `{ "FirewallRuleGroupAssociation": { "Id": "rslvr-frgassoc-57e8873d7example", "Arn": "arn:aws:route53resolver:us-west-2:123456789012:firewall-rule-group-association/rslvr-frgassoc-57e8873d7example", "FirewallRuleGroupId": "rslvr-frg-47f93271fexample", "VpcId": "vpc-31e92222", "Name": "test-association", "Priority": 103, "MutationProtection": "DISABLED", "Status": "DELETING", "StatusMessage": "Deleting the Firewall Rule Group Association", "CreatorRequestId": "2ca1a304-32b3-4f5f-bc4c-EXAMPLE11111", "CreationTime": "2021-05-25T21:47:48.755768Z", "ModificationTime": "2021-05-25T21:51:02.377887Z" } }`For more information, see [Managing associations between your VPC and Route 53 Resolver DNS Firewall rule groups](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/resolver-dns-firewall-vpc-associating-rule-group.html)in the*Amazon Route 53 Developer Guide*.- 
                    For API details, see [DisassociateFirewallRuleGroup](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/route53resolver/disassociate-firewall-rule-group.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `disassociate-resolver-endpoint-ip-address`.

- **AWS CLI**
- 
            
                    **To disassociate an IP address from a Resolver endpoint**The following `disassociate-resolver-endpoint-ip-address`example removes an IP address from a specified Resolver inbound or outbound endpoint.**Note**An endpoint must have at least two IP addresses. If an endpoint currently has only two IP addresses and you want to replace one address with another address, you must first use[associate-resolver-endpoint-ip-address](https://docs.aws.amazon.com/cli/latest/reference/route53resolver/associate-resolver-endpoint-ip-address.html)to associate the new IP address. Then you can disassociate one of the original IP addresses from the endpoint.`aws route53resolver disassociate-resolver-endpoint-ip-address \ --resolver-endpoint-id``rslvr-in-f9ab8a03f1example`\ --ip-address="SubnetId=subnet-12d8a459,Ip=172.31.40.121"Output: `{ "ResolverEndpoint": { "Id": "rslvr-in-f9ab8a03f1example", "CreatorRequestId": "2020-01-01-18:47", "Arn": "arn:aws:route53resolver:us-west-2:111122223333:resolver-endpoint/rslvr-in-f9ab8a03f1example", "Name": "my-inbound-endpoint", "SecurityGroupIds": [ "sg-f62bexam" ], "Direction": "INBOUND", "IpAddressCount": 3, "HostVPCId": "vpc-304bexam", "Status": "UPDATING", "StatusMessage": "Updating the Resolver Endpoint", "CreationTime": "2020-01-01T23:02:29.583Z", "ModificationTime": "2020-01-05T23:02:29.583Z" } }`- 
                    For API details, see [DisassociateResolverEndpointIpAddress](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/route53resolver/disassociate-resolver-endpoint-ip-address.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `disassociate-resolver-rule`.

- **AWS CLI**
- 
            
                    **To disassociate a Resolver rule from an Amazon VPC**The following `disassociate-resolver-rule`example removes the association between the specified Resolver rule and the specified VPC. You can disassociate a rule from a VPC in the following circumstances:For DNS queries that originate in this VPC, you want Resolver to stop forwarding queries to your network for the domain name that is specified in the rule.You want to delete the forwarding rule. If a rule is currently associated with one or more VPCs, you must disassociate the rule from all VPCs before you can delete it. `aws route53resolver disassociate-resolver-rule \ --resolver-rule-id rslvr-rr-4955cb98ceexample \ --vpc-id vpc-304bexam`Output: `{ "ResolverRuleAssociation": { "Id": "rslvr-rrassoc-322f4e8b9cexample", "ResolverRuleId": "rslvr-rr-4955cb98ceexample", "Name": "my-resolver-rule-association", "VPCId": "vpc-304bexam", "Status": "DELETING", "StatusMessage": "[Trace id: 1-5dc5ffa2-a26c38004c1f94006example] Deleting Association" } }`- 
                    For API details, see [DisassociateResolverRule](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/route53resolver/disassociate-resolver-rule.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `get-firewall-config`.

- **AWS CLI**
- 
            
                    **To get a firewall config for a VPC**The following `get-firewall-config`example retrieves the DNS Firewall behavior for the specified VPC.`aws route53resolver get-firewall-config \ --resource-id``vpc-31e92222`Output: `{ "FirewallConfig": { "Id": "rslvr-fc-86016850cexample", "ResourceId": "vpc-31e9222", "OwnerId": "123456789012", "FirewallFailOpen": "DISABLED" } }`For more information, see [DNS Firewall VPC configuration](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/resolver-dns-firewall-vpc-configuration.html)in the*Amazon Route 53 Developer Guide*.- 
                    For API details, see [GetFirewallConfig](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/route53resolver/get-firewall-config.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `get-firewall-domain-list`.

- **AWS CLI**
- 
            
                    **To get a Route 53 Resolver DNS Firewall domain list**The following `get-firewall-domain-list`example retrieves the domain list with the ID you specify.`aws route53resolver get-firewall-domain-list \ --firewall-domain-list-id``rslvr-fdl-42b60677cexample`Output: `{ "FirewallDomainList": { "Id": "rslvr-fdl-9e956e9ffexample", "Arn": "arn:aws:route53resolver:us-west-2:123457689012:firewall-domain-list/rslvr-fdl-42b60677cexample", "Name": "test", "DomainCount": 0, "Status": "COMPLETE", "StatusMessage": "Created Firewall Domain List", "CreatorRequestId": "my-request-id", "CreationTime": "2021-05-25T15:55:51.115365Z", "ModificationTime": "2021-05-25T15:55:51.115365Z" } }`For more information, see [Managing your own domain lists](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/resolver-dns-firewall-user-managed-domain-lists.html)in the*Amazon Route 53 Developer Guide*.- 
                    For API details, see [GetFirewallDomainList](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/route53resolver/get-firewall-domain-list.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `get-firewall-rule-group-association`.

- **AWS CLI**
- 
            
                    **To get a firewall rule group association**The following `get-firewall-rule-group-association`example retrieves a firewall rule group association.`aws route53resolver get-firewall-rule-group-association \ --firewall-rule-group-association-id``rslvr-frgassoc-57e8873d7example`Output: `{ "FirewallRuleGroupAssociation": { "Id": "rslvr-frgassoc-57e8873d7example", "Arn": "arn:aws:route53resolver:us-west-2:123456789012:firewall-rule-group-association/rslvr-frgassoc-57e8873d7example", "FirewallRuleGroupId": "rslvr-frg-47f93271fexample", "VpcId": "vpc-31e92222", "Name": "test-association", "Priority": 101, "MutationProtection": "DISABLED", "Status": "COMPLETE", "StatusMessage": "Finished rule group association update", "CreatorRequestId": "2ca1a304-32b3-4f5f-bc4c-EXAMPLE11111", "CreationTime": "2021-05-25T21:47:48.755768Z", "ModificationTime": "2021-05-25T21:47:48.755768Z" } }`For more information, see [Managing associations between your VPC and Route 53 Resolver DNS Firewall rule groups](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/resolver-dns-firewall-vpc-associating-rule-group.html)in the*Amazon Route 53 Developer Guide*.- 
                    For API details, see [GetFirewallRuleGroupAssociation](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/route53resolver/get-firewall-rule-group-association.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `get-firewall-rule-group-policy`.

- **AWS CLI**
- 
            
                    **To get an AWS IAM policy**The following `get-firewall-rule-group-policy`example gets the AWS Identity and Access Management (AWS IAM) policy for sharing the specified rule group.`aws route53resolver get-firewall-rule-group-policy \ --arn``arn:aws:route53resolver:us-west-2:AWS_ACCOUNT_ID:firewall-rule-group/rslvr-frg-47f93271fexample`Output: `{ "FirewallRuleGroupPolicy": "{\"Version\":\"2012-10-17\",\"Statement\":[{\"Sid\":\"test\",\"Effect\":\"Allow\",\"Principal\":{\"AWS\":\"arn:aws:iam::AWS_ACCOUNT_ID:root\"},\"Action\":[\"route53resolver:GetFirewallRuleGroup\",\"route53resolver:ListFirewallRuleGroups\"],\"Resource\":\"arn:aws:route53resolver:us-east-1:AWS_ACCOUNT_ID:firewall-rule-group/rslvr-frg-47f93271fexample\"}]}" }`For more information, see [Managing rule groups and rules in DNS Firewall](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/resolver-dns-firewall-rule-group-managing.html)in the*Amazon Route 53 Developer Guide*.- 
                    For API details, see [GetFirewallRuleGroupPolicy](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/route53resolver/get-firewall-rule-group-policy.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `get-firewall-rule-group`.

- **AWS CLI**
- 
            
                    **To get a Firewall rule group**The following `get-firewall-rule-group`example retrieves information about a DNS Firewall rule group with the ID you provide.`aws route53resolver get-firewall-rule-group \ --firewall-rule-group-id``rslvr-frg-47f93271fexample`Output: `{ "FirewallRuleGroup": { "Id": "rslvr-frg-47f93271fexample", "Arn": "arn:aws:route53resolver:us-west-2:123456789012:firewall-rule-group/rslvr-frg-47f93271fexample", "Name": "test", "RuleCount": 0, "Status": "COMPLETE", "StatusMessage": "Created Firewall Rule Group", "OwnerId": "123456789012", "CreatorRequestId": "my-request-id", "ShareStatus": "NOT_SHARED", "CreationTime": "2021-05-25T18:59:26.490017Z", "ModificationTime": "2021-05-25T18:59:26.490017Z" } }`For more information, see [Managing rule groups and rules in DNS Firewall](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/resolver-dns-firewall-rule-group-managing.html)in the*Amazon Route 53 Developer Guide*.- 
                    For API details, see [GetFirewallRuleGroup](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/route53resolver/get-firewall-rule-group.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `get-resolver-endpoint`.

- **AWS CLI**
- 
            
                    **To get information about a Resolver endpoint**The following `get-resolver-endpoint`example displays details for the outbound specified endpoint. You can use`get-resolver-endpoint`for both inbound and outbound endpoints by specifying the applicable endpoint ID.`aws route53resolver get-resolver-endpoint \ --resolver-endpoint-id``rslvr-out-d5e5920e37example`Output: `{ "ResolverEndpoint": { "Id": "rslvr-out-d5e5920e37example", "CreatorRequestId": "2020-01-01-18:47", "Arn": "arn:aws:route53resolver:us-west-2:111122223333:resolver-endpoint/rslvr-out-d5e5920e37example", "Name": "my-outbound-endpoint", "SecurityGroupIds": [ "sg-05cd7b25d6example" ], "Direction": "OUTBOUND", "IpAddressCount": 2, "HostVPCId": "vpc-304bexam", "Status": "OPERATIONAL", "StatusMessage": "This Resolver Endpoint is operational.", "CreationTime": "2020-01-01T23:50:50.979Z", "ModificationTime": "2020-01-02T23:50:50.979Z" } }`For more information, see [Values That You Specify When You Create or Edit Inbound Endpoints](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/resolver-forwarding-inbound-queries.html#resolver-forwarding-inbound-queries-values)in the*Amazon Route 53 Developer Guide*.- 
                    For API details, see [GetResolverEndpoint](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/route53resolver/get-resolver-endpoint.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `get-resolver-rule-association`.

- **AWS CLI**
- 
            
                    **To get information about the association between a Resolver rule and a VPC**The following `get-resolver-rule-association`example displays details about the association between a specified Resolver rule and a VPC. You associate a resolver rule and a VPC using[associate-resolver-rule](https://docs.aws.amazon.com/cli/latest/reference/route53resolver/associate-resolver-rule.html).`aws route53resolver get-resolver-rule-association \ --resolver-rule-association-id``rslvr-rrassoc-d61cbb2c8bexample`Output: `{ "ResolverRuleAssociation": { "Id": "rslvr-rrassoc-d61cbb2c8bexample", "ResolverRuleId": "rslvr-rr-42b60677c0example", "Name": "my-resolver-rule-association", "VPCId": "vpc-304bexam", "Status": "COMPLETE", "StatusMessage": "" } }`- 
                    For API details, see [GetResolverRuleAssociation](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/route53resolver/get-resolver-rule-association.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `get-resolver-rule`.

- **AWS CLI**
- 
            
                    **To get information about a Resolver rule**The following `get-resolver-rule`example displays details about the specified Resolver rule, such as the domain name that the rule forwards DNS queries for and the ID of the outbound resolver endpoint that the rule is associated with.`aws route53resolver get-resolver-rule \ --resolver-rule-id``rslvr-rr-42b60677c0example`Output: `{ "ResolverRule": { "Id": "rslvr-rr-42b60677c0example", "CreatorRequestId": "2020-01-01-18:47", "Arn": "arn:aws:route53resolver:us-west-2:111122223333:resolver-rule/rslvr-rr-42b60677c0example", "DomainName": "example.com.", "Status": "COMPLETE", "StatusMessage": "[Trace id: 1-5dc4b177-ff1d9d001a0f80005example] Successfully created Resolver Rule.", "RuleType": "FORWARD", "Name": "my-rule", "TargetIps": [ { "Ip": "192.0.2.45", "Port": 53 } ], "ResolverEndpointId": "rslvr-out-d5e5920e37example", "OwnerId": "111122223333", "ShareStatus": "NOT_SHARED" } }`For more information, see [Values That You Specify When You Create or Edit Rules](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/resolver-forwarding-outbound-queries.html#resolver-forwarding-outbound-queries-rule-values)in the*Amazon Route 53 Developer Guide*.- 
                    For API details, see [GetResolverRule](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/route53resolver/get-resolver-rule.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `import-firewall-domains`.

- **AWS CLI**
- 
            
                    **To import domains into a domain list**The following `import-firewall-domains`example imports a set of domains from a file into a DNS Firewall domain list that you specify.`aws route53resolver import-firewall-domains \ --firewall-domain-list-id``rslvr-fdl-d61cbb2cbexample`\ --operation`REPLACE`\ --domain-file-url`s3://PATH/TO/YOUR/FILE`Output: `{ "Id": "rslvr-fdl-d61cbb2cbexample", "Name": "test", "Status": "IMPORTING", "StatusMessage": "Importing domains from provided file." }`For more information, see [Managing your own domain lists](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/resolver-dns-firewall-user-managed-domain-lists.html)in the*Amazon Route 53 Developer Guide*.- 
                    For API details, see [ImportFirewallDomains](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/route53resolver/import-firewall-domains.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `list-firewall-configs`.

- **AWS CLI**
- 
            
                    **To list firewall configs**The following `list-firewall-configs`example lists your DNS Firewall configurations.`aws route53resolver list-firewall-configs`Output: `{ "FirewallConfigs": [ { "Id": "rslvr-fc-86016850cexample", "ResourceId": "vpc-31e92222", "OwnerId": "123456789012", "FirewallFailOpen": "DISABLED" } ] }`For more information, see [DNS Firewall VPC configuration](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/resolver-dns-firewall-vpc-configuration.html)in the*Amazon Route 53 Developer Guide*.- 
                    For API details, see [ListFirewallConfigs](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/route53resolver/list-firewall-configs.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `list-firewall-domain-lists`.

- **AWS CLI**
- 
            
                    **To list all of Route 53 Resolver DNS Firewall domain lists**The following `list-firewall-domain-lists`example lists all the domain lists.`aws route53resolver list-firewall-domain-lists`Output: `{ "FirewallDomainLists": [ { "Id": "rslvr-fdl-2c46f2ecfexample", "Arn": "arn:aws:route53resolver:us-west-2:123456789012:firewall-domain-list/rslvr-fdl-2c46f2ecfexample", "Name": "AWSManagedDomainsMalwareDomainList", "CreatorRequestId": "AWSManagedDomainsMalwareDomainList", "ManagedOwnerName": "Route 53 Resolver DNS Firewall" }, { "Id": "rslvr-fdl-aa970e9e1example", "Arn": "arn:aws:route53resolver:us-west-2:123456789012:firewall-domain-list/rslvr-fdl-aa970e9e1example", "Name": "AWSManagedDomainsBotnetCommandandControl", "CreatorRequestId": "AWSManagedDomainsBotnetCommandandControl", "ManagedOwnerName": "Route 53 Resolver DNS Firewall" }, { "Id": "rslvr-fdl-42b60677cexample", "Arn": "arn:aws:route53resolver:us-west-2:123456789111:firewall-domain-list/rslvr-fdl-42b60677cexample", "Name": "test", "CreatorRequestId": "my-request-id" } ] }`For more information, see [Route 53 Resolver DNS Firewall domain lists](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/resolver-dns-firewall-domain-lists.html)in the*Amazon Route 53 Developer Guide*.- 
                    For API details, see [ListFirewallDomainLists](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/route53resolver/list-firewall-domain-lists.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `list-firewall-domains`.

- **AWS CLI**
- 
            
                    **To list domains in a domain list**The following `list-firewall-domains`example lists the domains in a DNS Firewall domain list that you specify.`aws route53resolver list-firewall-domains \ --firewall-domain-list-id``rslvr-fdl-d61cbb2cbexample`Output: `{ "Domains": [ "test1.com.", "test2.com.", "test3.com." ] }`For more information, see [Managing your own domain lists](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/resolver-dns-firewall-user-managed-domain-lists.html)in the*Amazon Route 53 Developer Guide*.- 
                    For API details, see [ListFirewallDomains](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/route53resolver/list-firewall-domains.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `list-firewall-rule-group-associations`.

- **AWS CLI**
- 
            
                    **To list DNS Firewall rule group associations**The following `list-firewall-rule-group-associations`example lists your DNS Firewall rule group associations with Amazon VPCs.`aws route53resolver list-firewall-rule-group-associations`Output: `{ "FirewallRuleGroupAssociations": [ { "Id": "rslvr-frgassoc-57e8873d7example", "Arn": "arn:aws:route53resolver:us-west-2:123456789012:firewall-rule-group-association/rslvr-frgassoc-57e8873d7example", "FirewallRuleGroupId": "rslvr-frg-47f93271fexample", "VpcId": "vpc-31e92222", "Name": "test-association", "Priority": 101, "MutationProtection": "DISABLED", "Status": "UPDATING", "StatusMessage": "Creating Firewall Rule Group Association", "CreatorRequestId": "2ca1a304-32b3-4f5f-bc4c-EXAMPLE11111", "CreationTime": "2021-05-25T21:47:48.755768Z", "ModificationTime": "2021-05-25T21:47:48.755768Z" } ] }`For more information, see [Managing associations between your VPC and Route 53 Resolver DNS Firewall rule group](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/resolver-dns-firewall-vpc-associating-rule-group.html)in the*Amazon Route 53 Developer Guide*.- 
                    For API details, see [ListFirewallRuleGroupAssociations](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/route53resolver/list-firewall-rule-group-associations.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `list-firewall-rule-groups`.

- **AWS CLI**
- 
            
                    **To get a list of your Firewall rule groups**The following `list-firewall-rule-groups`example lists your DNS Firewall rule groups.`aws route53resolver list-firewall-rule-groups`Output: `{ "FirewallRuleGroups": [ { "Id": "rslvr-frg-47f93271fexample", "Arn": "arn:aws:route53resolver:us-west-2:123456789012:firewall-rule-group/rslvr-frg-47f93271fexample", "Name": "test", "OwnerId": "123456789012", "CreatorRequestId": "my-request-id", "ShareStatus": "NOT_SHARED" } ] }`For more information, see [Managing rule groups and rules in DNS Firewall](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/resolver-dns-firewall-rule-group-managing.html)in the*Amazon Route 53 Developer Guide*.- 
                    For API details, see [ListFirewallRuleGroups](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/route53resolver/list-firewall-rule-groups.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `list-firewall-rules`.

- **AWS CLI**
- 
            
                    **To list firewall rules**The following `list-firewall-rules`example list all of your DNS Firewall rules within a firewall rule group.`aws route53resolver list-firewall-rules \ --firewall-rule-group-id``rslvr-frg-47f93271fexample`Output: `{ "FirewallRules": [ { "FirewallRuleGroupId": "rslvr-frg-47f93271fexample", "FirewallDomainListId": "rslvr-fdl-9e956e9ffexample", "Name": "allow-rule", "Priority": 101, "Action": "ALLOW", "CreatorRequestId": "d81e3fb7-020b-415e-939f-EXAMPLE11111", "CreationTime": "2021-05-25T21:44:00.346093Z", "ModificationTime": "2021-05-25T21:44:00.346093Z" } ] }`For more information, see [Managing rule groups and rules in DNS Firewall](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/resolver-dns-firewall-rule-group-managing.html)in the*Amazon Route 53 Developer Guide*.- 
                    For API details, see [ListFirewallRules](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/route53resolver/list-firewall-rules.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `list-resolver-endpoint-ip-addresses`.

- **AWS CLI**
- 
            
                    **To list IP addresses for a specified inbound or outbound endpoint**The following `list-resolver-endpoint-ip-addresses`example lists information about the IP addresses that are associated with the inbound endpoint`rslvr-in-f9ab8a03f1example`. You can also use`list-resolver-endpoint-ip-addresses`for outbound endpoints by specifying the applicable endpoint ID.`aws route53resolver list-resolver-endpoint-ip-addresses \ --resolver-endpoint-id``rslvr-in-f9ab8a03f1example`Output: `{ "MaxResults": 10, "IpAddresses": [ { "IpId": "rni-1de60cdbfeexample", "SubnetId": "subnet-ba47exam", "Ip": "192.0.2.44", "Status": "ATTACHED", "StatusMessage": "This IP address is operational.", "CreationTime": "2020-01-03T23:02:29.587Z", "ModificationTime": "2020-01-03T23:03:05.555Z" }, { "IpId": "rni-aac7085e38example", "SubnetId": "subnet-12d8exam", "Ip": "192.0.2.45", "Status": "ATTACHED", "StatusMessage": "This IP address is operational.", "CreationTime": "2020-01-03T23:02:29.593Z", "ModificationTime": "2020-01-03T23:02:55.060Z" } ] }`For more information about the values in the output, see [Values That You Specify When You Create or Edit Inbound Endpoints](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/resolver-forwarding-inbound-queries.html#resolver-forwarding-inbound-queries-values), and[Values That You Specify When You Create or Edit Outbound Endpoints](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/resolver-forwarding-outbound-queries.html#resolver-forwarding-outbound-queries-endpoint-values), both in the*Amazon Route 53 Developer Guide*.- 
                    For API details, see [ListResolverEndpointIpAddresses](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/route53resolver/list-resolver-endpoint-ip-addresses.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `list-resolver-endpoints`.

- **AWS CLI**
- 
            
                    **To list Resolver endpoints in an AWS Region**The following `list-resolver-endpoints`example lists the inbound and outbound Resolver endpoints that exist in the current account.`aws route53resolver list-resolver-endpoints`Output: `{ "MaxResults": 10, "ResolverEndpoints": [ { "Id": "rslvr-in-497098ad59example", "CreatorRequestId": "2020-01-01-18:47", "Arn": "arn:aws:route53resolver:us-west-2:111122223333:resolver-endpoint/rslvr-in-497098ad59example", "Name": "my-inbound-endpoint", "SecurityGroupIds": [ "sg-05cd7b25d6example" ], "Direction": "INBOUND", "IpAddressCount": 2, "HostVPCId": "vpc-304bexam", "Status": "OPERATIONAL", "StatusMessage": "This Resolver Endpoint is operational.", "CreationTime": "2020-01-01T23:25:45.538Z", "ModificationTime": "2020-01-01T23:25:45.538Z" }, { "Id": "rslvr-out-d5e5920e37example", "CreatorRequestId": "2020-01-01-18:48", "Arn": "arn:aws:route53resolver:us-west-2:111122223333:resolver-endpoint/rslvr-out-d5e5920e37example", "Name": "my-outbound-endpoint", "SecurityGroupIds": [ "sg-05cd7b25d6example" ], "Direction": "OUTBOUND", "IpAddressCount": 2, "HostVPCId": "vpc-304bexam", "Status": "OPERATIONAL", "StatusMessage": "This Resolver Endpoint is operational.", "CreationTime": "2020-01-01T23:50:50.979Z", "ModificationTime": "2020-01-01T23:50:50.979Z" } ] }`- 
                    For API details, see [ListResolverEndpoints](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/route53resolver/list-resolver-endpoints.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `list-resolver-rule-associations`.

- **AWS CLI**
- 
            
                    **To list associations between Resolver rules and VPCs**The following `list-resolver-rule-associations`example lists the associations between resolver rules and VPCs in the current AWS account.`aws route53resolver list-resolver-rule-associations`Output: `{ "MaxResults": 30, "ResolverRuleAssociations": [ { "Id": "rslvr-autodefined-assoc-vpc-304bexam-internet-resolver", "ResolverRuleId": "rslvr-autodefined-rr-internet-resolver", "Name": "System Rule Association", "VPCId": "vpc-304bexam", "Status": "COMPLETE", "StatusMessage": "" }, { "Id": "rslvr-rrassoc-d61cbb2c8bexample", "ResolverRuleId": "rslvr-rr-42b60677c0example", "Name": "my-resolver-rule-association", "VPCId": "vpc-304bexam", "Status": "COMPLETE", "StatusMessage": "" } ] }`For more information, see [How Route 53 Resolver Forwards DNS Queries from Your VPCs to Your Network](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/resolver.html#resolver-overview-forward-vpc-to-network)in the*Amazon Route 53 Developer Guide*.- 
                    For API details, see [ListResolverRuleAssociations](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/route53resolver/list-resolver-rule-associations.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `list-resolver-rules`.

- **AWS CLI**
- 
            
                    **To list Resolver rules**The following `list-resolver-rules`example lists all the Resolver rules in the current AWS account.`aws route53resolver list-resolver-rules`Output: `{ "MaxResults": 30, "ResolverRules": [ { "Id": "rslvr-autodefined-rr-internet-resolver", "CreatorRequestId": "", "Arn": "arn:aws:route53resolver:us-west-2::autodefined-rule/rslvr-autodefined-rr-internet-resolver", "DomainName": ".", "Status": "COMPLETE", "RuleType": "RECURSIVE", "Name": "Internet Resolver", "OwnerId": "Route 53 Resolver", "ShareStatus": "NOT_SHARED" }, { "Id": "rslvr-rr-42b60677c0example", "CreatorRequestId": "2020-01-01-18:47", "Arn": "arn:aws:route53resolver:us-west-2:111122223333:resolver-rule/rslvr-rr-42b60677c0bc4e299", "DomainName": "example.com.", "Status": "COMPLETE", "StatusMessage": "[Trace id: 1-5dc4b177-ff1d9d001a0f80005example] Successfully created Resolver Rule.", "RuleType": "FORWARD", "Name": "my-rule", "TargetIps": [ { "Ip": "192.0.2.45", "Port": 53 } ], "ResolverEndpointId": "rslvr-out-d5e5920e37example", "OwnerId": "111122223333", "ShareStatus": "NOT_SHARED" } ] }`For more information, see [How Route 53 Resolver Forwards DNS Queries from Your VPCs to Your Network](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/resolver.html#resolver-overview-forward-vpc-to-network)in the*Amazon Route 53 Developer Guide*.- 
                    For API details, see [ListResolverRules](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/route53resolver/list-resolver-rules.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `list-tags-for-resource`.

- **AWS CLI**
- 
            
                    **To list the tags for a Resolver resource**The following `list-tags-for-resource`example lists the tags that are assigned to the specified Resolver rule.`aws route53resolver list-tags-for-resource \ --resource-arn``"arn:aws:route53resolver:us-west-2:111122223333:resolver-rule/rslvr-rr-42b60677c0example"`Output: `{ "Tags": [ { "Key": "my-key-1", "Value": "my-value-1" }, { "Key": "my-key-2", "Value": "my-value-2" } ] }`For information about using tags for cost allocation, see [Using Cost Allocation Tags](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/cost-alloc-tags.html)in the*AWS Billing and Cost Management User Guide*.- 
                    For API details, see [ListTagsForResource](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/route53resolver/list-tags-for-resource.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `put-firewall-rule-group-policy`.

- **AWS CLI**
- 
            
                    **To attach an AWS IAM policy to share a Firewall rule group policy**The following `put-firewall-rule-group-policy`example attaches an AWS Identity and Access Management (AWS IAM) policy for sharing the rule group.`aws route53resolver put-firewall-rule-group-policy \ --arn``arn:aws:route53resolver:us-east-1:AWS_ACCOUNT_ID:firewall-rule-group/rslvr-frg-47f93271fexample`\ --firewall-rule-group-policy "{\"Version\":\"2012-10-17\",\"Statement\":[{\"Sid\":\"test\",\"Effect\":\"Allow\",\"Principal\":{\"AWS\":\"arn:aws:iam::AWS_ACCOUNT_ID:root\"},\"Action\":[\"route53resolver:GetFirewallRuleGroup\",\"route53resolver:ListFirewallRuleGroups\"],\"Resource\":\"arn:aws:route53resolver:us-east-1:AWS_ACCOUNT_ID:firewall-rule-group/rslvr-frg-47f93271fexample\"}]}"Output: `{ "ReturnValue": true }`For more information, see [Managing rule groups and rules in DNS Firewall](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/resolver-dns-firewall-rule-group-managing.html)in the*Amazon Route 53 Developer Guide*.- 
                    For API details, see [PutFirewallRuleGroupPolicy](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/route53resolver/put-firewall-rule-group-policy.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `put-resolver-rule-policy`.

- **AWS CLI**
- 
            
                    **To share a Resolver rule with another AWS account**The following `put-resolver-rule-policy`example specifies a Resolver rule that you want to share with another AWS account, the account that you want to share the rule with, and the rule-related operations that you want the account to be able to perform on the rules.**Note**You must run this command using credentials from the same account that created the rule.`aws route53resolver put-resolver-rule-policy \ --region``us-east-1`\ --arn`"arn:aws:route53resolver:us-east-1:111122223333:resolver-rule/rslvr-rr-42b60677c0example"`\ --resolver-rule-policy "{\"Version\": \"2012-10-17\", \ \"Statement\": [ { \ \"Effect\" : \"Allow\", \ \"Principal\" : {\"AWS\" : \"444455556666\" }, \ \"Action\" : [ \ \"route53resolver:GetResolverRule\", \ \"route53resolver:AssociateResolverRule\", \ \"route53resolver:DisassociateResolverRule\", \ \"route53resolver:ListResolverRules\", \ \"route53resolver:ListResolverRuleAssociations\" ], \ \"Resource\" : [ \"arn:aws:route53resolver:us-east-1:111122223333:resolver-rule/rslvr-rr-42b60677c0example\" ] } ] }"Output: `{ "ReturnValue": true }`After you run `put-resolver-rule-policy`, you can run the following two Resource Access Manager (RAM) commands. You must use the account that you want to share the rule with:`get-resource-share-invitations`returns the value`resourceShareInvitationArn`. You need this value to accept the invitation to use the shared rule.`accept-resource-share-invitation`accepts the invitation to use the shared rule.For more information, see the following documentation: [get-resource-share-invitations](https://docs.aws.amazon.com/cli/latest/reference/ram/get-resource-share-invitations.html)[accept-resource-share-invitations](https://docs.aws.amazon.com/cli/latest/reference/ram/accept-resource-share-invitation.html)[Sharing Forwarding Rules with Other AWS Accounts and Using Shared Rules](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/resolver-rules-managing.html#resolver-rules-managing-sharing)in the*Amazon Route 53 Developer Guide*- 
                    For API details, see [PutResolverRulePolicy](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/route53resolver/put-resolver-rule-policy.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `tag-resource`.

- **AWS CLI**
- 
            
                    **To associate tags with a Resolver resource**The following `tag-resource`example associates two tag key/value pairs with the specified Resolver rule.`aws route53resolver tag-resource \ --resource-arn``"arn:aws:route53resolver:us-west-2:111122223333:resolver-rule/rslvr-rr-42b60677c0example"`\ --tags`"Key=my-key-1,Value=my-value-1"``"Key=my-key-2,Value=my-value-2"`This command produces no output. For information about using tags for cost allocation, see [Using Cost Allocation Tags](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/cost-alloc-tags.html)in the*AWS Billing and Cost Management User Guide*.- 
                    For API details, see [TagResource](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/route53resolver/tag-resource.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `untag-resource`.

- **AWS CLI**
- 
            
                    **To remove tags from a Resolver resource**The following `untag-resource`example removes two tags from the specified Resolver rule.`aws route53resolver untag-resource \ --resource-arn``"arn:aws:route53resolver:us-west-2:111122223333:resolver-rule/rslvr-rr-42b60677c0example"`\ --tag-keys`my-key-1``my-key-2`This command produces no output. To confirm that the tags were removed, you can use [list-tags-for-resource](https://docs.aws.amazon.com/cli/latest/reference/route53resolver/list-tags-for-resource.html).For information about using tags for cost allocation, see [Using Cost Allocation Tags](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/cost-alloc-tags.html)in the*AWS Billing and Cost Management User Guide*.- 
                    For API details, see [UntagResource](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/route53resolver/untag-resource.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `update-firewall-config`.

- **AWS CLI**
- 
            
                    **To update a firewall config**The following `update-firewall-config`example updates DNS Firewall configuration.`aws route53resolver update-firewall-config \ --resource-id``vpc-31e92222`\ --firewall-fail-open`DISABLED`Output: `{ "FirewallConfig": { "Id": "rslvr-fc-86016850cexample", "ResourceId": "vpc-31e92222", "OwnerId": "123456789012", "FirewallFailOpen": "DISABLED" } }`For more information, see [DNS Firewall VPC configuration](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/resolver-dns-firewall-vpc-configuration.html)in the*Amazon Route 53 Developer Guide*.- 
                    For API details, see [UpdateFirewallConfig](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/route53resolver/update-firewall-config.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `update-firewall-domains`.

- **AWS CLI**
- 
            
                    **To update a domain list**The following `update-firewall-domains`example adds the domains to a domain list with the ID you provide.`aws route53resolver update-firewall-domains \ --firewall-domain-list-id``rslvr-fdl-42b60677cexampleb`\ --operation`ADD`\ --domains`test1.com``test2.com``test3.com`Output: `{ "Id": "rslvr-fdl-42b60677cexample", "Name": "test", "Status": "UPDATING", "StatusMessage": "Updating the Firewall Domain List" }`For more information, see [Managing your own domain lists](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/resolver-dns-firewall-user-managed-domain-lists.html)in the*Amazon Route 53 Developer Guide*.- 
                    For API details, see [UpdateFirewallDomains](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/route53resolver/update-firewall-domains.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `update-firewall-rule-group-association`.

- **AWS CLI**
- 
            
                    **To update a firewall rule group association**The following `update-firewall-rule-group-association`example updates a firewall rule group association.`aws route53resolver update-firewall-rule-group-association \ --firewall-rule-group-association-id``rslvr-frgassoc-57e8873d7example`\ --priority`103`Output: `{ "FirewallRuleGroupAssociation": { "Id": "rslvr-frgassoc-57e8873d7example", "Arn": "arn:aws:route53resolver:us-west-2:123456789012:firewall-rule-group-association/rslvr-frgassoc-57e8873d7example", "FirewallRuleGroupId": "rslvr-frg-47f93271fexample", "VpcId": "vpc-31e92222", "Name": "test-association", "Priority": 103, "MutationProtection": "DISABLED", "Status": "UPDATING", "StatusMessage": "Updating the Firewall Rule Group Association Attributes", "CreatorRequestId": "2ca1a304-32b3-4f5f-bc4c-EXAMPLE11111", "CreationTime": "2021-05-25T21:47:48.755768Z", "ModificationTime": "2021-05-25T21:50:09.272569Z" } }`For more information, see [Managing associations between your VPC and Route 53 Resolver DNS Firewall rule group](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/resolver-dns-firewall-vpc-associating-rule-group.html)in the*Amazon Route 53 Developer Guide*.- 
                    For API details, see [UpdateFirewallRuleGroupAssociation](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/route53resolver/update-firewall-rule-group-association.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `update-firewall-rule`.

- **AWS CLI**
- 
            
                    **To update a firewall rule**The following `update-firewall-rule`example updates a firewall rule with the parameters you specify.`aws route53resolver update-firewall-rule \ --firewall-rule-group-id``rslvr-frg-47f93271fexample`\ --firewall-domain-list-id`rslvr-fdl-9e956e9ffexample`\ --priority`102`Output: `{ "FirewallRule": { "FirewallRuleGroupId": "rslvr-frg-47f93271fexample", "FirewallDomainListId": "rslvr-fdl-9e956e9ffexample", "Name": "allow-rule", "Priority": 102, "Action": "ALLOW", "CreatorRequestId": "d81e3fb7-020b-415e-939f-EXAMPLE11111", "CreationTime": "2021-05-25T21:44:00.346093Z", "ModificationTime": "2021-05-25T21:45:59.611600Z" } }`For more information, see [Managing rule groups and rules in DNS Firewall](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/resolver-dns-firewall-rule-group-managing.html)in the*Amazon Route 53 Developer Guide*.- 
                    For API details, see [UpdateFirewallRule](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/route53resolver/update-firewall-rule.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `update-resolver-endpoint`.

- **AWS CLI**
- 
            
                    **To update the name of a Resolver endpoint**The following `update-resolver-endpoint`example updates the name of a Resolver endpoint. Updating other values isn't supported.`aws route53resolver update-resolver-endpoint \ --resolver-endpoint-id``rslvr-in-b5d45e32bdc445f09`\ --name`my-renamed-inbound-endpoint`Output: `{ "ResolverEndpoint": { "Id": "rslvr-in-b5d45e32bdexample", "CreatorRequestId": "2020-01-02-18:48", "Arn": "arn:aws:route53resolver:us-west-2:111122223333:resolver-endpoint/rslvr-in-b5d45e32bdexample", "Name": "my-renamed-inbound-endpoint", "SecurityGroupIds": [ "sg-f62bexam" ], "Direction": "INBOUND", "IpAddressCount": 2, "HostVPCId": "vpc-304bexam", "Status": "OPERATIONAL", "StatusMessage": "This Resolver Endpoint is operational.", "CreationTime": "2020-01-01T18:33:59.265Z", "ModificationTime": "2020-01-08T18:33:59.265Z" } }`- 
                    For API details, see [UpdateResolverEndpoint](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/route53resolver/update-resolver-endpoint.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `update-resolver-rule`.

- **AWS CLI**
- 
            
                    **Example 1: To update settings Resolver endpoint**The following `update-resolver-rule`example updates the name of the rule, the IP addresses on your on-premises network that DNS queries are forwarded to, and the ID of the outbound Resolver endpoint that you're using to forward queries to your network.**Note**Existing values for`TargetIps`are overwritten, so you must specify all the IP addresses that you want the rule to have after the update.`aws route53resolver update-resolver-rule \ --resolver-rule-id``rslvr-rr-1247fa64f3example`\ --config Name="my-2nd-rule",TargetIps=[{Ip=192.0.2.45,Port=53},{Ip=192.0.2.46,Port=53}],ResolverEndpointId=rslvr-out-7b89ed0d25exampleOutput: `{ "ResolverRule": { "Id": "rslvr-rr-1247fa64f3example", "CreatorRequestId": "2020-01-02-18:47", "Arn": "arn:aws:route53resolver:us-west-2:111122223333:resolver-rule/rslvr-rr-1247fa64f3example", "DomainName": "www.example.com.", "Status": "COMPLETE", "StatusMessage": "[Trace id: 1-5dcc90b9-8a8ee860aba1ebd89example] Successfully updated Resolver Rule.", "RuleType": "FORWARD", "Name": "my-2nd-rule", "TargetIps": [ { "Ip": "192.0.2.45", "Port": 53 }, { "Ip": "192.0.2.46", "Port": 53 } ], "ResolverEndpointId": "rslvr-out-7b89ed0d25example", "OwnerId": "111122223333", "ShareStatus": "NOT_SHARED" } }`**Example 2: To update settings Resolver endpoint using a file for ``config`` settings**You can alternatively include the `config`settings in a JSON file and then specify that file when you call`update-resolver-rule`.`aws route53resolver update-resolver-rule \ --resolver-rule-id``rslvr-rr-1247fa64f3example`\ --config file://c:\temp\update-resolver-rule.jsonContents of `update-resolver-rule.json`.`{ "Name": "my-2nd-rule", "TargetIps": [ { "Ip": "192.0.2.45", "Port": 53 }, { "Ip": "192.0.2.46", "Port": 53 } ], "ResolverEndpointId": "rslvr-out-7b89ed0d25example" }`For more information, see [Values That You Specify When You Create or Edit Rules](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/resolver-forwarding-outbound-queries.html#resolver-forwarding-outbound-queries-rule-values)in the*Amazon Route 53 Developer Guide*.- 
                    For API details, see [UpdateResolverRule](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/route53resolver/update-resolver-rule.html)in*AWS CLI Command Reference*.
 
-