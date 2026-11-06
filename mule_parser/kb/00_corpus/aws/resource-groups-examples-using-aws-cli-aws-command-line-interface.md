# Resource Groups examples using AWS CLI - AWS Command Line Interface

**Source:** [https://docs.aws.amazon.com/cli/latest/userguide/cli_resource-groups_code_examples.html](https://docs.aws.amazon.com/cli/latest/userguide/cli_resource-groups_code_examples.html)

---

The following code examples show you how to perform actions and implement common scenarios by using the AWS Command Line Interface with Resource Groups.

*Actions* are code excerpts from larger programs and must be run in context. While actions show you how to call individual service functions, you can see actions in context in their related scenarios.

Each example includes a link to the complete source code, where you can find instructions on how to set up and run the code in context.

###### Topics

## Actions

    The following code example shows how to use `create-group`.

- **AWS CLI**
- 
            
                    **Example 1: To create a tag-based resource group**The following `create-group`example creates a tag-based resource group of Amazon EC2 instances in the current region. It's based on a query for resources that are tagged with the key`Name`, and the value`WebServers`. The group name is`tbq-WebServer`. The query is in a separate JSON file that is passed to the command.`aws resource-groups create-group \ --name``tbq-WebServer`\ --resource-query`file://query.json`Contents of `query.json`:`{ "Type": "TAG_FILTERS_1_0", "Query": "{\"ResourceTypeFilters\":[\"AWS::EC2::Instance\"],\"TagFilters\":[{\"Key\":\"Name\", \"Values\":[\"WebServers\"]}]}" }`Output: `{ "Group": { "GroupArn": "arn:aws:resource-groups:us-west-2:123456789012:group/tbq-WebServer", "Name": "tbq-WebServer" }, "ResourceQuery": { "Type": "TAG_FILTERS_1_0", "Query": "{\"ResourceTypeFilters\":[\"AWS::EC2::Instance\"],\"TagFilters\":[{\"Key\":\"Name\", \"Values\":[\"WebServers\"]}]}" } }`**Example 2: To create a CloudFormation stack-based resource group**The following `create-group`example creates an AWS CloudFormation stack-based resource group named`sampleCFNstackgroup`. The query includes all resources in the specified CloudFormation stack that are supported by AWS Resource Groups.`aws resource-groups create-group \ --name``cbq-CFNstackgroup`\ --resource-query`file://query.json`Contents of `query.json`:`{ "Type": "CLOUDFORMATION_STACK_1_0", "Query": "{\"ResourceTypeFilters\":[\"AWS::AllSupported\"],\"StackIdentifier\":\"arn:aws:cloudformation:us-west-2:123456789012:stack/MyCFNStack/1415z9z0-z39z-11z8-97z5-500z212zz6fz\"}" }`Output: `{ "Group": { "GroupArn": "arn:aws:resource-groups:us-west-2:123456789012:group/cbq-CFNstackgroup", "Name": "cbq-CFNstackgroup" }, "ResourceQuery": { "Type": "CLOUDFORMATION_STACK_1_0", "Query": "{\"ResourceTypeFilters\":[\"AWS::AllSupported\"],\"StackIdentifier\":\"arn:aws:cloudformation:us-east-2:123456789012:stack/MyCFNStack/1415z9z0-z39z-11z8-97z5-500z212zz6fz\"}"}' } }`For more information, see [Create Groups](https://docs.aws.amazon.com/ARG/latest/userguide/gettingstarted-query.html)in the*AWS Resource Groups User Guide*.- 
                    For API details, see [CreateGroup](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/resource-groups/create-group.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `delete-group`.

- **AWS CLI**
- 
            
                    **To update the description for a resource group**The following `delete-group`example updates the specified resource group.`aws resource-groups delete-group \ --group-name``tbq-WebServer`Output: `{ "Group": { "GroupArn": "arn:aws:resource-groups:us-west-2:1234567890:group/tbq-WebServer", "Name": "tbq-WebServer" } }`For more information, see [Delete Groups](https://docs.aws.amazon.com/ARG/latest/userguide/deleting-resource-groups.html)in the*AWS Resource Groups User Guide*.- 
                    For API details, see [DeleteGroup](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/resource-groups/delete-group.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `get-group-query`.

- **AWS CLI**
- 
            
                    **To get the query attached to a resource group**The following `get-group-query`example displays query attached to the specified resource group.`aws resource-groups get-group-query \ --group-name``tbq-WebServer`Output: `{ "GroupQuery": { "GroupName": "tbq-WebServer", "ResourceQuery": { "Type": "TAG_FILTERS_1_0", "Query": "{\"ResourceTypeFilters\":[\"AWS::EC2::Instance\"],\"TagFilters\":[{\"Key\":\"Name\", \"Values\":[\"WebServers\"]}]}" } } }`- 
                    For API details, see [GetGroupQuery](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/resource-groups/get-group-query.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `get-group`.

- **AWS CLI**
- 
            
                    **To get information about a resource group**The following `get-group`example displays details about the specified resource group. To get the query attached to the group, use`get-group-query`.`aws resource-groups get-group \ --group-name``tbq-WebServer`Output: `{ "Group": { "GroupArn": "arn:aws:resource-groups:us-west-2:123456789012:group/tbq-WebServer", "Name": "tbq-WebServer", "Description": "A tag-based query resource group of WebServers." } }`- 
                    For API details, see [GetGroup](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/resource-groups/get-group.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `get-tags`.

- **AWS CLI**
- 
            
                    **To retrieve the tags attached to a resource group**The following `get-tags`example displays the tag key and value pairs attached to the specified resource group (the group itself, not its members).`aws resource-groups get-tags \ --arn``arn:aws:resource-groups:us-west-2:123456789012:group/tbq-WebServer`Output: `{ "Arn": "arn:aws:resource-groups:us-west-2:123456789012:group/tbq-WebServer", "Tags": { "QueryType": "tags", "QueryResources": "ec2-instances" } }`- 
                    For API details, see [GetTags](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/resource-groups/get-tags.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `list-group-resources`.

- **AWS CLI**
- 
            
                    **To list all of the resources in a resource group**Example 1: The following `list-resource-groups`example lists all of the resources that are part of the specified resource group.`aws resource-groups list-group-resources \ --group-name``tbq-WebServer`Output: `{ "ResourceIdentifiers": [ { "ResourceArn": "arn:aws:ec2:us-west-2:123456789012:instance/i-09f77fa38c12345ab", "ResourceType": "AWS::EC2::Instance" } ] }`Example 2: The following example lists all of the resources in the group that also have a 'resource-type' of the 'AWS::EC2::Instance'. : aws resource-groups list-group-resources --group-name tbq-WebServer --filters Name=resource-type,Values=AWS::EC2::Instance - 
                    For API details, see [ListGroupResources](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/resource-groups/list-group-resources.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `list-groups`.

- **AWS CLI**
- 
            
                    **To list the available resource groups**The following `list-groups`example displays a list of all of the resource groups.`aws resource-groups list-groups`Output: `{ "GroupIdentifiers": [ { "GroupName": "tbq-WebServer", "GroupArn": "arn:aws:resource-groups:us-west-2:123456789012:group/tbq-WebServer3" }, { "GroupName": "cbq-CFNStackQuery", "GroupArn": "arn:aws:resource-groups:us-west-2:123456789012:group/cbq-CFNStackQuery" } ], "Groups": [ { "GroupArn": "arn:aws:resource-groups:us-west-2:123456789012:group/tbq-WebServer", "Name": "tbq-WebServer" }, { "GroupArn": "arn:aws:resource-groups:us-west-2:123456789012:group/cbq-CFNStackQuery", "Name": "cbq-CFNStackQuery" } ] }`- 
                    For API details, see [ListGroups](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/resource-groups/list-groups.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `list-resource-groups`.

- **AWS CLI**
- 
            
                    **To list all of the resources in a resource group**The following `list-resource-groups`example lists all of the resources that are part of the specified resource group.`aws resource-groups list-group-resources \ --group-name``tbq-WebServer`Output: `{ "ResourceIdentifiers": [ { "ResourceArn": "arn:aws:ec2:us-west-2:123456789012:instance/i-09f77fa38c12345ab", "ResourceType": "AWS::EC2::Instance" } ] }`- 
                    For API details, see [ListResourceGroups](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/resource-groups/list-resource-groups.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `put-group-configuration`.

- **AWS CLI**
- 
            
                    **To attach a service configuration to a resource group**Example 1: The following `put-group-configuration`example specifies that the resource group is to contain only Amazon EC2 capacity reservations for instances in the`C5`or`M5`families.`aws resource-groups put-group-configuration \ --group``MyTestGroup`\ --configuration`file://config.json`Contents of `config.json`:`[ { "Type": "AWS::EC2::HostManagement", "Parameters": [ { "Name": "allowed-host-families", "Values": [ "c5", "m5" ] }, { "Name": "any-host-based-license-configuration", "Values": [ "true" ] } ] }, { "Type": "AWS::ResourceGroups::Generic", "Parameters": [ { "Name": "allowed-resource-types", "Values": [ "AWS::EC2::Host" ] }, { "Name": "deletion-protection", "Values": [ "UNLESS_EMPTY" ] } ] } ]`This command produces no output if successful. For more information, see [Service configurations for resource groups](https://docs.aws.amazon.com/ARG/latest/APIReference/about-slg.html)in the*Resource Groups API Reference Guide*.- 
                    For API details, see [PutGroupConfiguration](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/resource-groups/put-group-configuration.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `search-resources`.

- **AWS CLI**
- 
            
                    **To find resources that match a query**The following `search-resources`example retrieves a list of all AWS resources that match the specified query.`aws resource-groups search-resources \ --resource-query``file://query.json`Contents of `query.json`:`{ "Type": "TAG_FILTERS_1_0", "Query": "{\"ResourceTypeFilters\":[\"AWS::EC2::Instance\"],\"TagFilters\":[{\"Key\":\"Patch Group\", \"Values\":[\"Dev\"]}]}" }`Output: `{ "ResourceIdentifiers": [ { "ResourceArn": "arn:aws:ec2:us-west-2:123456789012:instance/i-01a23bc45d67890ef", "ResourceType": "AWS::EC2::Instance" } ] }`- 
                    For API details, see [SearchResources](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/resource-groups/search-resources.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `tag`.

- **AWS CLI**
- 
            
                    **To attach a tag to a resource group**The following `tag`example attaches the specified tag key and value pairs to the specified resource group (the group itself, not its members).`aws resource-groups tag \ --tags``QueryType=tags,QueryResources=ec2-instances`\ --arn`arn:aws:resource-groups:us-west-2:128716708097:group/tbq-WebServer`Output: `{ "Arn": "arn:aws:resource-groups:us-west-2:128716708097:group/tbq-WebServer", "Tags": { "QueryType": "tags", "QueryResources": "ec2-instances" } }`For more information, see [Manage tags](https://docs.aws.amazon.com/ARG/latest/userguide/tagging-resources.html)in the*AWS Resource Groups User Guide*.- 
                    For API details, see [Tag](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/resource-groups/tag.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `untag`.

- **AWS CLI**
- 
            
                    **To remove tags from a resource group**The following `untags`example removes any tag with the specified key from the resource group itself, not its members.`aws resource-groups untag \ --arn``arn:aws:resource-groups:us-west-2:123456789012:group/tbq-WebServer`\ --keys`QueryType`Output: `{ "Arn": "arn:aws:resource-groups:us-west-2:123456789012:group/tbq-WebServer", "Keys": [ "QueryType" ] }`For more information, see [Manage tags](https://docs.aws.amazon.com/ARG/latest/userguide/tagging-resources.html)in the*AWS Resource Groups User Guide*.- 
                    For API details, see [Untag](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/resource-groups/untag.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `update-group-query`.

- **AWS CLI**
- 
            
                    **Example 1: To update the query for a tag-based resource group**The following `update-group-query`example updates the query attached to the specified tag-based resource group.`aws resource-groups update-group-query \ --group-name``tbq-WebServer`\ --resource-query '`{"Type":"TAG_FILTERS_1_0", "Query":"{\"ResourceTypeFilters\":[\"AWS::EC2::Instance\"],\"TagFilters\":[{\"Key\":\"Name\", \"Values\":[\"WebServers\"]}]}"}`'Output: `{ "Group": { "GroupArn": "arn:aws:resource-groups:us-east-2:123456789012:group/tbq-WebServer", "Name": "tbq-WebServer" }, "ResourceQuery": { "Type": "TAG_FILTERS_1_0", "Query": "{\"ResourceTypeFilters\":[\"AWS::EC2::Instance\"],\"TagFilters\":[{\"Key\":\"Name\", \"Values\":[\"WebServers\"]}]}" } }`For more information, see [Update Groups](https://docs.aws.amazon.com/ARG/latest/userguide/updating-resource-groups.html)in the*AWS Resource Groups User Guide*.**Example 2: To update the query for a CloudFormation stack-based resource group**The following `update-group-query`example updates the query attached to the specified AWS CloudFormation stack-based resource group.`aws resource-groups update-group-query \ --group-name``cbq-CFNstackgroup`\ --resource-query '`{"Type": "CLOUDFORMATION_STACK_1_0", "Query": "{\"ResourceTypeFilters\":[\"AWS::AllSupported\"],\"StackIdentifier\":\"arn:aws:cloudformation:us-west-2:123456789012:stack/MyCFNStack/1415z9z0-z39z-11z8-97z5-500z212zz6fz\"}"}`'Output: `{ "Group": { "GroupArn": "arn:aws:resource-groups:us-west-2:123456789012:group/cbq-CFNstackgroup", "Name": "cbq-CFNstackgroup" }, "ResourceQuery": { "Type": "CLOUDFORMATION_STACK_1_0", "Query": "{\"ResourceTypeFilters\":[\"AWS::AllSupported\"],\"StackIdentifier\":\"arn:aws:cloudformation:us-west-2:123456789012:stack/MyCFNStack/1415z9z0-z39z-11z8-97z5-500z212zz6fz\"}" } }`For more information, see [Update Groups](https://docs.aws.amazon.com/ARG/latest/userguide/updating-resource-groups.html)in the*AWS Resource Groups User Guide*.- 
                    For API details, see [UpdateGroupQuery](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/resource-groups/update-group-query.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `update-group`.

- **AWS CLI**
- 
            
                    **To update the description for a resource group**The following `update-group`example updates the description for the specified resource group.`aws resource-groups update-group \ --group-name``tbq-WebServer`\ --description`"Resource group for all web server resources."`Output: `{ "Group": { "GroupArn": "arn:aws:resource-groups:us-west-2:123456789012:group/tbq-WebServer", "Name": "tbq-WebServer" "Description": "Resource group for all web server resources." } }`For more information, see [Update Groups](https://docs.aws.amazon.com/ARG/latest/userguide/updating-resource-groups.html)in the*AWS Resource Groups User Guide*.- 
                    For API details, see [UpdateGroup](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/resource-groups/update-group.html)in*AWS CLI Command Reference*.
 
-