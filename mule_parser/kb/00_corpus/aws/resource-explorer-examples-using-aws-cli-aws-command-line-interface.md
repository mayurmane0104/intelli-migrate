# Resource Explorer examples using AWS CLI - AWS Command Line Interface

**Source:** [https://docs.aws.amazon.com/cli/latest/userguide/cli_resource-explorer-2_code_examples.html](https://docs.aws.amazon.com/cli/latest/userguide/cli_resource-explorer-2_code_examples.html)

---

The following code examples show you how to perform actions and implement common scenarios by using the AWS Command Line Interface with Resource Explorer.

*Actions* are code excerpts from larger programs and must be run in context. While actions show you how to call individual service functions, you can see actions in context in their related scenarios.

Each example includes a link to the complete source code, where you can find instructions on how to set up and run the code in context.

###### Topics

## Actions

    The following code example shows how to use `associate-default-view`.

- **AWS CLI**
- 
            
                    **To set a Resource Explorer view as the default for its AWS Region**The following `associate-default-view`example sets a view, as specified by its ARN, to be the default view for the AWS Region in which you call the operation.`aws resource-explorer-2 associate-default-view \ --view-arn``arn:aws:resource-explorer-2:us-east-1:123456789012:view/My-Main-View/EXAMPLE8-90ab-cdef-fedc-EXAMPLE11111`Output: `{ "ViewArn": "arn:aws:resource-explorer-2:us-east-1:123456789012:view/My-Main-View/EXAMPLE8-90ab-cdef-fedc-EXAMPLE11111" }`For more information, see [Setting a default view in an AWS Region](https://docs.aws.amazon.com/resource-explorer/latest/userguide/manage-views-set-default.html)in the*AWS Resource Explorer Users Guide*.- 
                    For API details, see [AssociateDefaultView](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/resource-explorer-2/associate-default-view.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `batch-get-view`.

- **AWS CLI**
- 
            
                    **To retrieve details about multiple Resource Explorer views**The following `batch-get-view`example displays the details about two views specified by their ARNs. Use spaces to separate the multiple ARNs in the --view-arn parameter.`aws resource-explorer-2 batch-get-view \ --view-arns``arn:aws:resource-explorer-2:us-east-1:123456789012:view/My-EC2-Only-View/EXAMPLE8-90ab-cdef-fedc-EXAMPLE22222,`\`arn:aws:resource-explorer-2:us-east-1:123456789012:view/My-Main-View/EXAMPLE8-90ab-cdef-fedc-EXAMPLE11111`Output: `{ "Views": [ { "Filters": { "FilterString": "service:ec2" }, "IncludedProperties": [ { "Name": "tags" } ], "LastUpdatedAt": "2022-07-13T21:33:45.249000+00:00", "Owner": "123456789012", "Scope": "arn:aws:iam::123456789012:root", "ViewArn": "arn:aws:resource-explorer-2:us-east-1:123456789012:view/My-EC2-Only-View/EXAMPLE8-90ab-cdef-fedc-EXAMPLE22222" }, { "Filters": { "FilterString": "" }, "IncludedProperties": [ { "Name": "tags" } ], "LastUpdatedAt": "2022-07-13T20:34:11.314000+00:00", "Owner": "123456789012", "Scope": "arn:aws:iam::123456789012:root", "ViewArn": "arn:aws:resource-explorer-2:us-east-1:123456789012:view/My-Main-View/EXAMPLE8-90ab-cdef-fedc-EXAMPLE11111" } ] "Errors": [] }`For more information about views, see [About Resource Explorer views](https://docs.aws.amazon.com/resource-explorer/latest/userguide/manage-views-about.html)in the*AWS Resource Explorer Users Guide*.- 
                    For API details, see [BatchGetView](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/resource-explorer-2/batch-get-view.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `create-index`.

- **AWS CLI**
- 
            
                    **To turn on Resource Explorer in an AWS Region by creating an index**The following `create-index`example creates a local index in the AWS Region in which the operation is called. The AWS CLI automatically generates a random`client-token`parameter value and includes it in the call to AWS if you don't specify a value.`aws resource-explorer-2 create-index \ --region``us-east-1`Output: `{ "Arn": "arn:aws:resource-explorer-2:us-east-1:123456789012:index/EXAMPLE8-90ab-cdef-fedc-EXAMPLE22222c", "CreatedAt": "2022-11-01T20:00:59.149Z", "State": "CREATING" }`After you create a local index, you can convert it into the aggregator index for the account by running the [update-index-type](https://docs.aws.amazon.com/cli/latest/reference/resource-explorer-2/update-index-type.html)command.For more information, see [Turning on Resource Explorer in an AWS Region to index your resources](https://docs.aws.amazon.com/resource-explorer/latest/userguide/manage-service-register.html)in the*AWS Resource Explorer Users Guide*.- 
                    For API details, see [CreateIndex](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/resource-explorer-2/create-index.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `create-view`.

- **AWS CLI**
- 
            
                    **Example 1: To create an unfiltered view for the index in an AWS Region**The following `create-view`example creates a view in the specified AWS Region that returns all results in the Region without any filtering. The view includes the optional Tags field on returned results. Because this view is created in the Region that contains the aggregator index, it can include results from all Regions in the account that contain a Resource Explorer index.`aws resource-explorer-2 create-view \ --view-name``My-Main-View`\ --included-properties`Name=tags`\ --region`us-east-1`Output: `{ "View": { "Filters": { "FilterString": "" }, "IncludedProperties": [ { "Name": "tags" } ], "LastUpdatedAt": "2022-07-13T20:34:11.314000+00:00", "Owner": "123456789012", "Scope": "arn:aws:iam::123456789012:root", "ViewArn": "arn:aws:resource-explorer-2:us-east-1:123456789012:view/My-Main-View/EXAMPLE8-90ab-cdef-fedc-EXAMPLE11111" } }`**Example 2: To create a view that returns only resources associated with Amazon EC2**The following `create-view`creates a view in AWS Region`us-east-1`that returns only those resources in the Region that are associated with the Amazon EC2 service. The view includes the optional`Tags`field on returned results. Because this view is created in the Region that contains the aggregator index, it can include results from all Regions in the account that contain a Resource Explorer index.`aws resource-explorer-2 create-view \ --view-name``My-EC2-Only-View`\ --included-properties`Name=tags`\ --filters FilterString="service:ec2" \ --region`us-east-1`Output: `{ "View": { "Filters": { "FilterString": "service:ec2" }, "IncludedProperties": [ { "Name":"tags" } ], "LastUpdatedAt": "2022-07-13T21:35:09.059Z", "Owner": "123456789012", "Scope": "arn:aws:iam::123456789012:root", "ViewArn": "arn:aws:resource-explorer-2:us-east-1:123456789012:view/My-EC2-Only-View/EXAMPLE8-90ab-cdef-fedc-EXAMPLE22222" } }`For more information, see [Creating views for search](https://docs.aws.amazon.com/resource-explorer/latest/userguide/manage-views-create.html)in the*AWS Resource Explorer Users Guide*.- 
                    For API details, see [CreateView](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/resource-explorer-2/create-view.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `delete-index`.

- **AWS CLI**
- 
            
                    **To turn off Resource Explorer in an AWS Region by deleting its index**The following `delete-index`example deletes the specified Resource Explorer index in the AWS Region in which you make the request.`aws resource-explorer-2 delete-index \ --arn``arn:aws:resource-explorer-2:us-west-2:123456789012:index/EXAMPLE8-90ab-cdef-fedc-EXAMPLE22222`\ --region`us-west-2`Output: `{ "Arn": "arn:aws:resource-explorer-2:us-west-2:123456789012:index/EXAMPLE8-90ab-cdef-fedc-EXAMPLE22222", "State": "DELETING" }`For more information about deleting an index, see [Turning off AWS Resource Explorer in an AWS Region](https://docs.aws.amazon.com/resource-explorer/latest/userguide/manage-service-deregister.html)in the*AWS Resource Explorer Users Guide*.- 
                    For API details, see [DeleteIndex](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/resource-explorer-2/delete-index.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `delete-view`.

- **AWS CLI**
- 
            
                    **To delete a Resource Explorer view**The following `delete-view`example deletes a view specified by its ARN.`aws resource-explorer-2 delete-view \ --view-arn``arn:aws:resource-explorer-2:us-east-1:123456789012:view/EC2-Only-View/EXAMPLE8-90ab-cdef-fedc-EXAMPLE11111`Output: `{ "ViewArn": "arn:aws:resource-explorer-2:us-east-1:123456789012:view/EC2-Only-View/EXAMPLE8-90ab-cdef-fedc-EXAMPLE11111" }`For more information, see [Deleting views](https://docs.aws.amazon.com/resource-explorer/latest/userguide/manage-views-delete.html)in the*AWS Resource Explorer Users Guide*.- 
                    For API details, see [DeleteView](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/resource-explorer-2/delete-view.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `disassociate-default-view`.

- **AWS CLI**
- 
            
                    **To remove the default Resource Explorer view for an AWS Region**The following `disassociate-default-view`removes the default Resource Explorer view for the AWS Region in which you call the operation. After performing this operation, all search operations in the Region must explicitly specify a view or the operation fails.`aws resource-explorer-2 disassociate-default-view`This command produces no output. For more information, see [Setting a default view in an AWS Region](https://docs.aws.amazon.com/resource-explorer/latest/userguide/manage-views-set-default.html)in the*AWS Resource Explorer Users Guide*.- 
                    For API details, see [DisassociateDefaultView](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/resource-explorer-2/disassociate-default-view.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `get-default-view`.

- **AWS CLI**
- 
            
                    **To retrieve the Resource Explorer view that is the default view for its AWS Region**The following `get-default-view`example retrieves the ARN of the view that is the default for the AWS Region in which you call the operation.`aws resource-explorer-2 get-default-view`Output: `{ "ViewArn": "arn:aws:resource-explorer-2:us-east-1:123456789012:view/default-view/EXAMPLE8-90ab-cdef-fedc-EXAMPLE11111" }`For more information, see [Setting a default view in an AWS Region](https://docs.aws.amazon.com/resource-explorer/latest/userguide/manage-views-set-default.html)in the*AWS Resource Explorer Users Guide*.- 
                    For API details, see [GetDefaultView](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/resource-explorer-2/get-default-view.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `get-index`.

- **AWS CLI**
- 
            
                    **Example 1: To retrieve the details for a Resource Explorer aggregator index**The following `get-index`example displays the details for the Resource Explorer index in the specified AWS Region. Because the specified Region contains the aggregator index for the account, the output lists the Regions that replicate data into this Region's index.`aws resource-explorer-2 get-index \ --region``us-east-1`Output: `{ "Arn": "arn:aws:resource-explorer-2:us-east-1:123456789012:index/EXAMPLE8-90ab-cdef-fedc-EXAMPLE11111", "CreatedAt": "2022-07-12T18:59:10.503000+00:00", "LastUpdatedAt": "2022-07-13T18:41:58.799000+00:00", "ReplicatingFrom": [ "ap-south-1", "us-west-2" ], "State": "ACTIVE", "Tags": {}, "Type": "AGGREGATOR" }`**Example 2: To retrieve the details for a Resource Explorer local index**The following `get-index`example displays the details for the Resource Explorer index in the specified AWS Region. Because the specified Region contains a local index, the output lists the Region to which it replicates data from this Region's index.`aws resource-explorer-2 get-index \ --region``us-west-2`Output: `{ "Arn": "arn:aws:resource-explorer-2:us-west-2:123456789012:index/EXAMPLE8-90ab-cdef-fedc-EXAMPLE22222", "CreatedAt": "2022-07-12T18:59:10.503000+00:00", "LastUpdatedAt": "2022-07-13T18:41:58.799000+00:00", "ReplicatingTo": [ "us-west-2" ], "State": "ACTIVE", "Tags": {}, "Type": "LOCAL" }`For more information about indexes, see [Checking which AWS Regions have Resource Explorer turned on](https://docs.aws.amazon.com/resource-explorer/latest/userguide/manage-service-check.html)in the*AWS Resource Explorer Users Guide*.- 
                    For API details, see [GetIndex](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/resource-explorer-2/get-index.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `get-view`.

- **AWS CLI**
- 
            
                    **To retrieve details about a Resource Explorer view**The following `get-view`example displays the details about a view specified by its ARN.`aws resource-explorer-2 get-view \ --view-arn``arn:aws:resource-explorer-2:us-east-1:123456789012:view/EC2-Only-View/EXAMPLE8-90ab-cdef-fedc-EXAMPLE11111`Output: `{ "Tags" : {}, "View" : { "Filters" : { "FilterString" : "service:ec2" }, "IncludedProperties" : [ { "Name" : "tags" } ], "LastUpdatedAt" : "2022-07-13T21:33:45.249Z", "Owner" : "123456789012", "Scope" : "arn:aws:iam::123456789012:root", "ViewArn" : "arn:aws:resource-explorer-2:us-east-1:123456789012:view/EC2-Only-View/EXAMPLE8-90ab-cdef-fedc-EXAMPLE11111" } }`For more information about views, see [About Resource Explorer views](https://docs.aws.amazon.com/resource-explorer/latest/userguide/manage-views-about.html)in the*AWS Resource Explorer Users Guide*.- 
                    For API details, see [GetView](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/resource-explorer-2/get-view.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `list-indexes`.

- **AWS CLI**
- 
            
                    **To list the AWS Regions where Resource Explorer has indexes**The following `list-indexes`example lists the indexes for all Regions where Resource Explorer has an index. The response specifies the type of each index, its AWS Region, and its ARN.`aws resource-explorer-2 list-indexes`Output: `{ "Indexes": [ { "Arn": "arn:aws:resource-explorer-2:us-west-2:123456789012:index/EXAMPLE8-90ab-cdef-fedc-EXAMPLE11111", "Region": "us-west-2", "Type": "AGGREGATOR" }, { "Arn": "arn:aws:resource-explorer-2:us-east-1:123456789012:index/EXAMPLE8-90ab-cdef-fedc-EXAMPLE22222", "Region": "us-east-1", "Type": "LOCAL" }, { "Arn": "arn:aws:resource-explorer-2:us-east-2:123456789012:index/EXAMPLE8-90ab-cdef-fedc-EXAMPLE33333", "Region": "us-east-2", "Type": "LOCAL" }, { "Arn": "arn:aws:resource-explorer-2:us-west-1:123456789012:index/EXAMPLE8-90ab-cdef-fedc-EXAMPLE44444", "Region": "us-west-1", "Type": "LOCAL" } ] }`For more information about indexes, see [Checking which AWS Regions have Resource Explorer turned on](https://docs.aws.amazon.com/resource-explorer/latest/userguide/manage-service-check.html)in the*AWS Resource Explorer Users Guide*.- 
                    For API details, see [ListIndexes](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/resource-explorer-2/list-indexes.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `list-supported-resource-types`.

- **AWS CLI**
- 
            
                    **To list the AWS Regions where Resource Explorer has indexes**The following `list-supported-resource-types`example lists all of the resource types currently supported by &AREXlong;. The example response includes a`NextToken`value, which indicates that there is more output available to retrieve with additional calls.`aws resource-explorer-2 list-supported-resource-types \ --max-items``10`Output: `{ "ResourceTypes": [ { "ResourceType": "cloudfront:cache-policy", "Service": "cloudfront" }, { "ResourceType": "cloudfront:distribution", "Service": "cloudfront" }, { "ResourceType": "cloudfront:function", "Service": "cloudfront" }, { "ResourceType": "cloudfront:origin-access-identity", "Service": "cloudfront" }, { "ResourceType": "cloudfront:origin-request-policy", "Service": "cloudfront" }, { "ResourceType": "cloudfront:realtime-log-config", "Service": "cloudfront" }, { "ResourceType": "cloudfront:response-headers-policy", "Service": "cloudfront" }, { "ResourceType": "cloudwatch:alarm", "Service": "cloudwatch" }, { "ResourceType": "cloudwatch:dashboard", "Service": "cloudwatch" }, { "ResourceType": "cloudwatch:insight-rule", "Service": "cloudwatch" } ], "NextToken": "eyJOZXh0VG9rZW4iOiBudWxsLCAiYm90b190cnVuY2F0ZV9hbW91bnQiOiAxMH0=" }`To get the next part of the output, call the operation again, and pass the previous call's `NextToken`response value as the value for`--starting-token`. Repeat until`NextToken`is absent from the response.`aws resource-explorer-2 list-supported-resource-types \ --max-items``10`\ --starting-token`eyJOZXh0VG9rZW4iOiBudWxsLCAiYm90b190cnVuY2F0ZV9hbW91bnQiOiAxMH0=`Output: `{ "ResourceTypes": [ { "ResourceType": "cloudwatch:metric-stream", "Service": "cloudwatch" }, { "ResourceType": "dynamodb:table", "Service": "dynamodb" }, { "ResourceType": "ec2:capacity-reservation", "Service": "ec2" }, { "ResourceType": "ec2:capacity-reservation-fleet", "Service": "ec2" }, { "ResourceType": "ec2:client-vpn-endpoint", "Service": "ec2" }, { "ResourceType": "ec2:customer-gateway", "Service": "ec2" }, { "ResourceType": "ec2:dedicated-host", "Service": "ec2" }, { "ResourceType": "ec2:dhcp-options", "Service": "ec2" }, { "ResourceType": "ec2:egress-only-internet-gateway", "Service": "ec2" }, { "ResourceType": "ec2:elastic-gpu", "Service": "ec2" } ], "NextToken": "eyJOZXh0VG9rZW4iOiBudWxsLCAiYm90b190cnVuY2F0ZV9hbW91bnQiOiAyMH0=" }`For more information about indexes, see [Checking which AWS Regions have Resource Explorer turned on](https://docs.aws.amazon.com/resource-explorer/latest/userguide/manage-service-check.html)in the*AWS Resource Explorer Users Guide*.- 
                    For API details, see [ListSupportedResourceTypes](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/resource-explorer-2/list-supported-resource-types.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `list-tags-for-resource`.

- **AWS CLI**
- 
            
                    **To list the tags attached to a Resource Explorer view or index**The following `list-tags-for-resource`example lists the tag key and value pairs attached to view with the specified ARN. You must call the operation from the AWS Region that contains the resource.`aws resource-explorer-2 list-tags-for-resource \ --resource-arn``arn:aws:resource-explorer-2:us-east-1:123456789012:view/My-View/EXAMPLE8-90ab-cdef-fedc-EXAMPLE11111`Output: `{ "Tags": { "application": "MainCorpApp", "department": "1234" } }`For more information about tagging views, see [Tagging views for access control](https://docs.aws.amazon.com/resource-explorer/latest/userguide/manage-views-tag.html)in the*AWS Resource Explorer Users Guide*.- 
                    For API details, see [ListTagsForResource](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/resource-explorer-2/list-tags-for-resource.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `list-views`.

- **AWS CLI**
- 
            
                    **To list the Resource Explorer views available in an AWS Region**The following `list-views`example lists all of the views available in the Region in which you invoke the operation.`aws resource-explorer-2 list-views`Output: `{ "Views": [ "arn:aws:resource-explorer-2:us-east-1:123456789012:view/EC2-Only-View/EXAMPLE8-90ab-cdef-fedc-EXAMPLE11111", "arn:aws:resource-explorer-2:us-east-1:123456789012:view/Default-All-Resources-View/EXAMPLE8-90ab-cdef-fedc-EXAMPLE22222", "arn:aws:resource-explorer-2:us-east-1:123456789012:view/Production-Only-View/EXAMPLE8-90ab-cdef-fedc-EXAMPLE33333" ] }`For more information about views, see [About Resource Explorer views](https://docs.aws.amazon.com/resource-explorer/latest/userguide/manage-views-about.html)in the*AWS Resource Explorer Users Guide*.- 
                    For API details, see [ListViews](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/resource-explorer-2/list-views.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `search`.

- **AWS CLI**
- 
            
                    **Example 1: To search using the default view**The following `search`example displays all resources in the specified Region that are associated with the IAM service. The search uses the default view for the Region. The example response includes a`NextToken`value, which indicates that there is more output available to retrieve with additional calls.`aws resource-explorer-2 search \ --query-string``"service:iam"`Output: `{ "Count": { "Complete": true, "TotalResources": 55 }, "NextToken": "AG9VOEF1KLEXAMPLEOhJHVwo5chEXAMPLER5XiEpNrgsEXAMPLE...b0CmOFOryHEXAMPLE", "Resources": [{ "Arn": "arn:aws:iam::123456789012:policy/service-role/Some-Policy-For-A-Service-Role", "LastReportedAt": "2022-07-21T12:34:42Z", "OwningAccountId": "123456789012", "Properties": [], "Region": "global", "ResourceType": "iam:policy", "Service": "iam" }, { "Arn": "arn:aws:iam::123456789012:policy/service-role/Another-Policy-For-A-Service-Role", "LastReportedAt": "2022-07-21T12:34:42Z", "OwningAccountId": "123456789012", "Properties": [], "Region": "global", "ResourceType": "iam:policy", "Service": "iam" }, { ... TRUNCATED FOR BREVITY ... }], "ViewArn": "arn:aws:resource-explorer-2:us-east-1:123456789012:view/my-default-view/EXAMPLE8-90ab-cdef-fedc-EXAMPLE11111" }`**Example 2: To search using a specified view**The following `search`example search displays all resources ("*") in the specified AWS Region that are visible through the specified view. The results include only resources associated with Amazon EC2 because of the filters attached to the view.`aws resource-explorer-2 search \ --query-string``"*"`\ --view-arn`arn:aws:resource-explorer-2:us-east-1:123456789012:view/My-EC2-view/EXAMPLE8-90ab-cdef-fedc-EXAMPLE22222`Output: `HTTP/1.1 200 OK Date: Tue, 01 Nov 2022 20:00:59 GMT Content-Type: application/json Content-Length: <PayloadSizeBytes> { "Count": { "Complete": true, "TotalResources": 67 }, "Resources": [{ "Arn": "arn:aws:ec2:us-east-1:123456789012:network-acl/acl-1a2b3c4d", "LastReportedAt": "2022-07-21T18:52:02Z", "OwningAccountId": "123456789012", "Properties": [{ "Data": [{ "Key": "Department", "Value": "AppDevelopment" }, { "Key": "Environment", "Value": "Production" }], "LastReportedAt": "2021-11-15T14:48:29Z", "Name": "tags" }], "Region": "us-east-1", "ResourceType": "ec2:network-acl", "Service": "ec2" }, { "Arn": "arn:aws:ec2:us-east-1:123456789012:subnet/subnet-1a2b3c4d", "LastReportedAt": "2022-07-21T21:22:23Z", "OwningAccountId": "123456789012", "Properties": [{ "Data": [{ "Key": "Department", "Value": "AppDevelopment" }, { "Key": "Environment", "Value": "Production" }], "LastReportedAt": "2021-07-29T19:02:39Z", "Name": "tags" }], "Region": "us-east-1", "ResourceType": "ec2:subnet", "Service": "ec2" }, { "Arn": "arn:aws:ec2:us-east-1:123456789012:dhcp-options/dopt-1a2b3c4d", "LastReportedAt": "2022-07-21T06:08:53Z", "OwningAccountId": "123456789012", "Properties": [{ "Data": [{ "Key": "Department", "Value": "AppDevelopment" }, { "Key": "Environment", "Value": "Production" }], "LastReportedAt": "2021-11-15T15:11:05Z", "Name": "tags" }], "Region": "us-east-1", "ResourceType": "ec2:dhcpoptions", "Service": "ec2" }, { ... TRUNCATED FOR BREVITY ... }], "ViewArn": "arn:aws:resource-explorer-2:us-east-1:123456789012:view/My-EC2-view/EXAMPLE8-90ab-cdef-fedc-EXAMPLE22222" }`For more information, see [Using AWS Resource Explorer to search for resources](https://docs.aws.amazon.com/resource-explorer/latest/userguide/using-search.html)in the*AWS Resource Explorer Users Guide*.- 
                    For API details, see [Search](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/resource-explorer-2/search.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `tag-resource`.

- **AWS CLI**
- 
            
                    **To tag a Resource Explorer view**The following `tag-resource`example adds the tag key "environment" with the value "production" to the view with the specified ARN.`aws resource-explorer-2 tag-resource \ --resource-arn``arn:aws:resource-explorer-2:us-east-1:123456789012:view/My-View//EXAMPLE8-90ab-cdef-fedc-EXAMPLE11111`\ --tags`environment=production`This command produces no output. For more information, see [Tagging views for access control](https://docs.aws.amazon.com/resource-explorer/latest/userguide/manage-views-tag.html)in the*AWS Resource Explorer Users Guide*.- 
                    For API details, see [TagResource](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/resource-explorer-2/tag-resource.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `untag-resource`.

- **AWS CLI**
- 
            
                    **To remove a tag from a Resource Explorer view**The following `untag-resource`example removes any tag with the key name "environment" from the view with the specified ARN.`aws resource-explorer-2 untag-resource \ --resource-arn``arn:aws:resource-explorer-2:us-east-1:123456789012:view/My-View//EXAMPLE8-90ab-cdef-fedc-EXAMPLE11111`\ --tag-keys`environment`This command produces no output. For more information, see [Tagging views for access control](https://docs.aws.amazon.com/resource-explorer/latest/userguide/manage-views-tag.html)in the*AWS Resource Explorer Users Guide*.- 
                    For API details, see [UntagResource](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/resource-explorer-2/untag-resource.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `update-index-type`.

- **AWS CLI**
- 
            
                    **To change the type of a Resource Explorer index**The following `update-index-type`example converts the specified index from type`local`to type`aggregator`to turn on the ability to search for resources across all AWS Regions in the account. You must send the request to the AWS Region that contains the index you want to update.`aws resource-explorer-2 update-index-type \ --arn``arn:aws:resource-explorer-2:us-east-1:123456789012:index/EXAMPLE8-90ab-cdef-fedc-EXAMPLE11111`\ --type`aggregator`\ --region`us-east-1`Output: `{ "Arn":"arn:aws:resource-explorer-2:us-east-1:123456789012:index/EXAMPLE8-90ab-cdef-fedc-EXAMPLE11111", "LastUpdatedAt":"2022-07-13T18:41:58.799Z", "State":"updating", "Type":"aggregator" }`For more information about changing an index's type, see [Turning on cross-Region search by creating an aggregator index](https://docs.aws.amazon.com/resource-explorer/latest/userguide/manage-aggregator-region.html)in the*AWS Resource Explorer Users Guide*.- 
                    For API details, see [UpdateIndexType](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/resource-explorer-2/update-index-type.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `update-view`.

- **AWS CLI**
- 
            
                    **Example 1: To update the IncludedProperties field for a Resource Explorer view**The following `update-view`example updates the specified view by adding``tags``to the optional``IncludedProperties``. After running this operation, search operations that use this view include information about the tags attached to the resources that appear in the results.`aws resource-explorer-2 update-view \ --included-properties``Name=tags`\ --view-arn`arn:aws:resource-explorer-2:us-east-1:123456789012:view/My-View/EXAMPLE8-90ab-cdef-fedc-EXAMPLE22222`Output: `{ "View": { "Filters": { "FilterString": "" }, "IncludedProperties": [ { "Name": "tags" } ], "LastUpdatedAt": "2022-07-19T17:41:21.710000+00:00", "Owner": "123456789012", "Scope": "arn:aws:iam::123456789012:root", "ViewArn": "arn:aws:resource-explorer-2:us-east-1:123456789012:view/My-EC2-Only-View/EXAMPLE8-90ab-cdef-fedc-EXAMPLE11111" } }`**Example 2: To update the filters attached to a view**The following `update-view`example updates the specified view to use a filter that limits results to only resource types that are associated with the Amazon EC2 service.`aws resource-explorer-2 update-view \ --filters FilterString="service:ec2" \ --view-arn``arn:aws:resource-explorer-2:us-east-1:123456789012:view/My-View/EXAMPLE8-90ab-cdef-fedc-EXAMPLE22222`Output: `{ "View": { "Filters": { "FilterString": "service:ec2" }, "IncludedProperties": [], "LastUpdatedAt": "2022-07-19T17:41:21.710000+00:00", "Owner": "123456789012", "Scope": "arn:aws:iam::123456789012:root", "ViewArn": "arn:aws:resource-explorer-2:us-east-1:123456789012:view/My-View/EXAMPLE8-90ab-cdef-fedc-EXAMPLE22222" } }`For more information about views, see [About Resource Explorer views](https://docs.aws.amazon.com/resource-explorer/latest/userguide/manage-views-about.html)in the*AWS Resource Explorer Users Guide*.- 
                    For API details, see [UpdateView](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/resource-explorer-2/update-view.html)in*AWS CLI Command Reference*.
 
-