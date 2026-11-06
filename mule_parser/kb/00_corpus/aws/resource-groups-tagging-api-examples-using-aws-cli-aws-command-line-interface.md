# Resource Groups Tagging API examples using AWS CLI - AWS Command Line Interface

**Source:** [https://docs.aws.amazon.com/cli/latest/userguide/cli_resource-groups-tagging-api_code_examples.html](https://docs.aws.amazon.com/cli/latest/userguide/cli_resource-groups-tagging-api_code_examples.html)

---

The following code examples show you how to perform actions and implement common scenarios by using the AWS Command Line Interface with Resource Groups Tagging API.

*Actions* are code excerpts from larger programs and must be run in context. While actions show you how to call individual service functions, you can see actions in context in their related scenarios.

Each example includes a link to the complete source code, where you can find instructions on how to set up and run the code in context.

###### Topics

## Actions

    The following code example shows how to use `get-resources`.

- **AWS CLI**
- 
            
                    **To get a list of tagged resources**The following `get-resources`example displays a list of resources in the account that are tagged with the specified key name and value.`aws resourcegroupstaggingapi get-resources \ --tag-filters``Key=Environment,Values=Production`\ --tags-per-page`100`Output: `{ "ResourceTagMappingList": [ { "ResourceARN": " arn:aws:inspector:us-west-2:123456789012:target/0-nvgVhaxX/template/0-7sbz2Kz0", "Tags": [ { "Key": "Environment", "Value": "Production" } ] } ] }`For more information, see [GetResources](https://docs.aws.amazon.com/resourcegroupstagging/latest/APIReference/API_GetResources.html)in the*Resource Groups Tagging API Reference*.- 
                    For API details, see [GetResources](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/resourcegroupstaggingapi/get-resources.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `get-tag-keys`.

- **AWS CLI**
- 
            
                    **To get a list of all tag keys**The following `get-tag-keys`example retrieves the list of all tag key names used by resources in the account.`aws resourcegroupstaggingapi get-tag-keys`Output: `{ "TagKeys": [ "Environment", "CostCenter", "Department" ] }`For more information, see [GetTagKeys](https://docs.aws.amazon.com/resourcegroupstagging/latest/APIReference/API_GetTagKeys.html)in the*Resource Groups Tagging API Reference*.- 
                    For API details, see [GetTagKeys](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/resourcegroupstaggingapi/get-tag-keys.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `get-tag-values`.

- **AWS CLI**
- 
            
                    **To get a list of all tag values**The following `get-tag-values`example displays all of the values used for the specified key for all resources in the`aws resourcegroupstaggingapi get-tag-values \ --key=Environment`Output: `{ "TagValues": [ "Alpha", "Gamma", "Production" ] }`For more information, see [GetTagValues](https://docs.aws.amazon.com/resourcegroupstagging/latest/APIReference/API_GetTagValues.html)in the*Resource Groups Tagging API Reference*.- 
                    For API details, see [GetTagValues](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/resourcegroupstaggingapi/get-tag-values.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `tag-resources`.

- **AWS CLI**
- 
            
                    **To attach a tag to a resource**The following `tag-resources`example tags the specified resource with a key name and value.`aws resourcegroupstaggingapi tag-resources \ --resource-arn-list``arn:aws:s3:::MyProductionBucket`\ --tags`Environment=Production,CostCenter=1234`Output: `{ "FailedResourcesMap": {} }`For more information, see [TagResources](https://docs.aws.amazon.com/resourcegroupstagging/latest/APIReference/API_TagResources.html)in the*Resource Groups Tagging API Reference*.- 
                    For API details, see [TagResources](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/resourcegroupstaggingapi/tag-resources.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `untag-resources`.

- **AWS CLI**
- 
            
                    **To remove a tag from a resource**The following `untag-resources`example removes the specified tag keys and any associated values from the specified resource.`aws resourcegroupstaggingapi untag-resources \ --resource-arn-list``arn:aws:s3:::amzn-s3-demo-bucket`\ --tag-keys`Environment``CostCenter`Output: `{ "FailedResourcesMap": {} }`For more information, see [UntagResources](https://docs.aws.amazon.com/resourcegroupstagging/latest/APIReference/API_UntagResources.html)in the*Resource Groups Tagging API Reference*.- 
                    For API details, see [UntagResources](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/resourcegroupstaggingapi/untag-resources.html)in*AWS CLI Command Reference*.
 
-