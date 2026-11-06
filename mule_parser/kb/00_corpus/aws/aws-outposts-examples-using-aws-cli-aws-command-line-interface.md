# AWS Outposts examples using AWS CLI - AWS Command Line Interface

**Source:** [https://docs.aws.amazon.com/cli/latest/userguide/cli_outposts_code_examples.html](https://docs.aws.amazon.com/cli/latest/userguide/cli_outposts_code_examples.html)

---

The following code examples show you how to perform actions and implement common scenarios by using the AWS Command Line Interface with AWS Outposts.

*Actions* are code excerpts from larger programs and must be run in context. While actions show you how to call individual service functions, you can see actions in context in their related scenarios.

Each example includes a link to the complete source code, where you can find instructions on how to set up and run the code in context.

###### Topics

## Actions

    The following code example shows how to use `get-outpost-instance-types`.

- **AWS CLI**
- 
            
                    **To get the instance types on your Outpost**The following `get-outpost-instance-types`example gets the instance types for the specified Outpost.`aws outposts get-outpost-instance-types \ --outpost-id``op-0ab23c4567EXAMPLE`Output: `{ "InstanceTypes": [ { "InstanceType": "c5d.large" }, { "InstanceType": "i3en.24xlarge" }, { "InstanceType": "m5d.large" }, { "InstanceType": "r5d.large" } ], "OutpostId": "op-0ab23c4567EXAMPLE", "OutpostArn": "arn:aws:outposts:us-west-2:123456789012:outpost/op-0ab23c4567EXAMPLE" }`For more information, see [Launch an instance on your Outpost](https://docs.aws.amazon.com/outposts/latest/userguide/launch-instance.html)in the*AWS Outposts User Guide*.- 
                    For API details, see [GetOutpostInstanceTypes](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/outposts/get-outpost-instance-types.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `get-outpost`.

- **AWS CLI**
- 
            
                    **To get Outpost details**The following `get-outpost`example displays the details for the specified Outpost.`aws outposts get-outpost \ --outpost-id``op-0ab23c4567EXAMPLE`Output: `{ "Outpost": { "OutpostId": "op-0ab23c4567EXAMPLE", "OwnerId": "123456789012", "OutpostArn": "arn:aws:outposts:us-west-2:123456789012:outpost/op-0ab23c4567EXAMPLE", "SiteId": "os-0ab12c3456EXAMPLE", "Name": "EXAMPLE", "LifeCycleStatus": "ACTIVE", "AvailabilityZone": "us-west-2a", "AvailabilityZoneId": "usw2-az1", "Tags": {} } }`For more information, see [Working with Outposts](https://docs.aws.amazon.com/outposts/latest/userguide/work-with-outposts.html)in the*AWS Outposts User Guide*.- 
                    For API details, see [GetOutpost](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/outposts/get-outpost.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `list-outposts`.

- **AWS CLI**
- 
            
                    **To list Outposts**The following `list-outposts`example lists the Outposts in your AWS account.`aws outposts list-outposts`Output: `{ "Outposts": [ { "OutpostId": "op-0ab23c4567EXAMPLE", "OwnerId": "123456789012", "OutpostArn": "arn:aws:outposts:us-west-2:123456789012:outpost/op-0ab23c4567EXAMPLE", "SiteId": "os-0ab12c3456EXAMPLE", "Name": "EXAMPLE", "Description": "example", "LifeCycleStatus": "ACTIVE", "AvailabilityZone": "us-west-2a", "AvailabilityZoneId": "usw2-az1", "Tags": { "Name": "EXAMPLE" } }, { "OutpostId": "op-4fe3dc21baEXAMPLE", "OwnerId": "123456789012", "OutpostArn": "arn:aws:outposts:us-west-2:123456789012:outpost/op-4fe3dc21baEXAMPLE", "SiteId": "os-0ab12c3456EXAMPLE", "Name": "EXAMPLE2", "LifeCycleStatus": "ACTIVE", "AvailabilityZone": "us-west-2a", "AvailabilityZoneId": "usw2-az1", "Tags": {} } ] }`For more information, see [Working with Outposts](https://docs.aws.amazon.com/outposts/latest/userguide/work-with-outposts.html)in the*AWS Outposts User Guide*.- 
                    For API details, see [ListOutposts](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/outposts/list-outposts.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `list-sites`.

- **AWS CLI**
- 
            
                    **To list sites**The following `list-sites`example lists the available Outpost sites in your AWS account.`aws outposts list-sites`Output: `{ "Sites": [ { "SiteId": "os-0ab12c3456EXAMPLE", "AccountId": "123456789012", "Name": "EXAMPLE", "Description": "example", "Tags": {} } ] }`For more information, see [Working with Outposts](https://docs.aws.amazon.com/outposts/latest/userguide/work-with-outposts.html)in the*AWS Outposts User Guide*.- 
                    For API details, see [ListSites](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/outposts/list-sites.html)in*AWS CLI Command Reference*.
 
-