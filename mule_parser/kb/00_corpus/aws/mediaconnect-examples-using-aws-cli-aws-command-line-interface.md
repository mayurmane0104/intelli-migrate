# MediaConnect examples using AWS CLI - AWS Command Line Interface

**Source:** [https://docs.aws.amazon.com/cli/latest/userguide/cli_mediaconnect_code_examples.html](https://docs.aws.amazon.com/cli/latest/userguide/cli_mediaconnect_code_examples.html)

---

The following code examples show you how to perform actions and implement common scenarios by using the AWS Command Line Interface with MediaConnect.

*Actions* are code excerpts from larger programs and must be run in context. While actions show you how to call individual service functions, you can see actions in context in their related scenarios.

Each example includes a link to the complete source code, where you can find instructions on how to set up and run the code in context.

###### Topics

## Actions

    The following code example shows how to use `add-flow-outputs`.

- **AWS CLI**
- 
            
                    **To add outputs to a flow**The following `add-flow-outputs`example adds outputs to the specified flow.`aws mediaconnect add-flow-outputs \ --flow-arn``arn:aws:mediaconnect:us-east-1:111122223333:flow:1-23aBC45dEF67hiJ8-12AbC34DE5fG:BaseballGame`\ --outputs Description='NYC stream',Destination=192.0.2.12,Name=NYC,Port=3333,Protocol=rtp-fec,SmoothingLatency=100 Description='LA stream',Destination=203.0.113.9,Name=LA,Port=4444,Protocol=rtp-fec,SmoothingLatency=100Output: `{ "Outputs": [ { "Port": 3333, "OutputArn": "arn:aws:mediaconnect:us-east-1:111122223333:output:2-3aBC45dEF67hiJ89-c34de5fG678h:NYC", "Name": "NYC", "Description": "NYC stream", "Destination": "192.0.2.12", "Transport": { "Protocol": "rtp-fec", "SmoothingLatency": 100 } }, { "Port": 4444, "OutputArn": "arn:aws:mediaconnect:us-east-1:111122223333:output:2-987655dEF67hiJ89-c34de5fG678h:LA", "Name": "LA", "Description": "LA stream", "Destination": "203.0.113.9", "Transport": { "Protocol": "rtp-fec", "SmoothingLatency": 100 } } ], "FlowArn": "arn:aws:mediaconnect:us-east-1:111122223333:flow:1-23aBC45dEF67hiJ8-12AbC34DE5fG:BaseballGame" }`For more information, see [Adding Outputs to a Flow](https://docs.aws.amazon.com/mediaconnect/latest/ug/outputs-add.html)in the*AWS Elemental MediaConnect User Guide*.- 
                    For API details, see [AddFlowOutputs](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/mediaconnect/add-flow-outputs.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `create-flow`.

- **AWS CLI**
- 
            
                    **To create a flow**The following `create-flow`example creates a flow with the specified configuration.`aws mediaconnect create-flow \ --availability-zone``us-west-2c`\ --name`ExampleFlow`\ --source Description='Example source, backup',IngestPort=1055,Name=BackupSource,Protocol=rtp,WhitelistCidr=10.24.34.0/23Output: `{ "Flow": { "FlowArn": "arn:aws:mediaconnect:us-east-1:123456789012:flow:1-23aBC45dEF67hiJ8-12AbC34DE5fG:ExampleFlow", "AvailabilityZone": "us-west-2c", "EgressIp": "54.245.71.21", "Source": { "IngestPort": 1055, "SourceArn": "arn:aws:mediaconnect:us-east-1:123456789012:source:2-3aBC45dEF67hiJ89-c34de5fG678h:BackupSource", "Transport": { "Protocol": "rtp", "MaxBitrate": 80000000 }, "Description": "Example source, backup", "IngestIp": "54.245.71.21", "WhitelistCidr": "10.24.34.0/23", "Name": "mySource" }, "Entitlements": [], "Name": "ExampleFlow", "Outputs": [], "Status": "STANDBY", "Description": "Example source, backup" } }`For more information, see [Creating a Flow](https://docs.aws.amazon.com/mediaconnect/latest/ug/flows-create.html)in the*AWS Elemental MediaConnect User Guide*.- 
                    For API details, see [CreateFlow](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/mediaconnect/create-flow.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `delete-flow`.

- **AWS CLI**
- 
            
                    **To delete a flow**The following `delete-flow`example deletes the specified flow.`aws mediaconnect delete-flow \ --flow-arn``arn:aws:mediaconnect:us-east-1:123456789012:flow:1-23aBC45dEF67hiJ8-12AbC34DE5fG:AwardsShow`Output: `{ "FlowArn": "arn:aws:mediaconnect:us-east-1:123456789012:flow:1-23aBC45dEF67hiJ8-12AbC34DE5fG:AwardsShow", "Status": "DELETING" }`For more information, see [Deleting a Flow](https://docs.aws.amazon.com/mediaconnect/latest/ug/flows-delete.html)in the*AWS Elemental MediaConnect User Guide*.- 
                    For API details, see [DeleteFlow](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/mediaconnect/delete-flow.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `describe-flow`.

- **AWS CLI**
- 
            
                    **To view the details of a flow**The following `describe-flow`example displays the specified flow's details, such as ARN, Availability Zone, status, source, entitlements, and outputs.`aws mediaconnect describe-flow \ --flow-arn``arn:aws:mediaconnect:us-east-1:123456789012:flow:1-23aBC45dEF67hiJ8-12AbC34DE5fG:AwardsShow`Output: `{ "Flow": { "EgressIp": "54.201.4.39", "AvailabilityZone": "us-west-2c", "Status": "ACTIVE", "FlowArn": "arn:aws:mediaconnect:us-east-1:123456789012:flow:1-23aBC45dEF67hiJ8-12AbC34DE5fG:AwardsShow", "Entitlements": [ { "EntitlementArn": "arn:aws:mediaconnect:us-west-2:123456789012:entitlement:1-AaBb11CcDd22EeFf-34DE5fG12AbC:MyEntitlement", "Description": "Assign to this account", "Name": "MyEntitlement", "Subscribers": [ "444455556666" ] } ], "Description": "NYC awards show", "Name": "AwardsShow", "Outputs": [ { "Port": 2355, "Name": "NYC", "Transport": { "SmoothingLatency": 0, "Protocol": "rtp-fec" }, "OutputArn": "arn:aws:mediaconnect:us-east-1:123456789012:output:2-3aBC45dEF67hiJ89-c34de5fG678h:NYC", "Destination": "192.0.2.0" }, { "Port": 3025, "Name": "LA", "Transport": { "SmoothingLatency": 0, "Protocol": "rtp-fec" }, "OutputArn": "arn:aws:mediaconnect:us-east-1:123456789012:output:2-987655dEF67hiJ89-c34de5fG678h:LA", "Destination": "192.0.2.0" } ], "Source": { "IngestIp": "54.201.4.39", "SourceArn": "arn:aws:mediaconnect:us-east-1:123456789012:source:3-4aBC56dEF78hiJ90-4de5fG6Hi78Jk:ShowSource", "Transport": { "MaxBitrate": 80000000, "Protocol": "rtp" }, "IngestPort": 1069, "Description": "Saturday night show", "Name": "ShowSource", "WhitelistCidr": "10.24.34.0/23" } } }`For more information, see [Viewing the Details of a Flow](https://docs.aws.amazon.com/mediaconnect/latest/ug/flows-view-details.html)in the*AWS Elemental MediaConnect User Guide*.- 
                    For API details, see [DescribeFlow](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/mediaconnect/describe-flow.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `grant-flow-entitlements`.

- **AWS CLI**
- 
            
                    **To grant an entitlement on a flow**The following `grant-flow-entitlements`example grants an entitlement to the specified existing flow to share your content with another AWS account.`aws mediaconnect grant-flow-entitlements \ --flow-arn``arn:aws:mediaconnect:us-east-1:111122223333:flow:1-23aBC45dEF67hiJ8-12AbC34DE5fG:BaseballGame`\ --entitlements Description='For AnyCompany',Encryption={"Algorithm=aes128,KeyType=static-key,RoleArn=arn:aws:iam::111122223333:role/MediaConnect-ASM,SecretArn=arn:aws:secretsmanager:us-west-2:111122223333:secret:mySecret1"},Name=AnyCompany_Entitlement,Subscribers=444455556666 Description='For Example Corp',Name=ExampleCorp,Subscribers=777788889999Output: `{ "Entitlements": [ { "Name": "AnyCompany_Entitlement", "EntitlementArn": "arn:aws:mediaconnect:us-west-2:111122223333:entitlement:1-11aa22bb11aa22bb-3333cccc4444:AnyCompany_Entitlement", "Subscribers": [ "444455556666" ], "Description": "For AnyCompany", "Encryption": { "SecretArn": "arn:aws:secretsmanager:us-west-2:111122223333:secret:mySecret1", "Algorithm": "aes128", "RoleArn": "arn:aws:iam::111122223333:role/MediaConnect-ASM", "KeyType": "static-key" } }, { "Name": "ExampleCorp", "EntitlementArn": "arn:aws:mediaconnect:us-west-2:111122223333:entitlement:1-3333cccc4444dddd-1111aaaa2222:ExampleCorp", "Subscribers": [ "777788889999" ], "Description": "For Example Corp" } ], "FlowArn": "arn:aws:mediaconnect:us-east-1:111122223333:flow:1-23aBC45dEF67hiJ8-12AbC34DE5fG:BaseballGame" }`For more information, see [Granting an Entitlement on a Flow](https://docs.aws.amazon.com/mediaconnect/latest/ug/entitlements-grant.html)in the*AWS Elemental MediaConnect User Guide*.- 
                    For API details, see [GrantFlowEntitlements](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/mediaconnect/grant-flow-entitlements.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `list-entitlements`.

- **AWS CLI**
- 
            
                    **To view a list of entitlements**The following `list-entitlements`example displays a list of all entitlements that have been granted to the account.`aws mediaconnect list-entitlements`Output: `{ "Entitlements": [ { "EntitlementArn": "arn:aws:mediaconnect:us-west-2:111122223333:entitlement:1-11aa22bb11aa22bb-3333cccc4444:MyEntitlement", "EntitlementName": "MyEntitlement" } ] }`For more information, see [ListEntitlements](https://docs.aws.amazon.com/mediaconnect/latest/api/v1-entitlements.html)in the*AWS Elemental MediaConnect API Reference*.- 
                    For API details, see [ListEntitlements](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/mediaconnect/list-entitlements.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `list-flows`.

- **AWS CLI**
- 
            
                    **To view a list of flows**The following `list-flows`example displays a list of flows.`aws mediaconnect list-flows`Output: `{ "Flows": [ { "Status": "STANDBY", "SourceType": "OWNED", "AvailabilityZone": "us-west-2a", "Description": "NYC awards show", "Name": "AwardsShow", "FlowArn": "arn:aws:mediaconnect:us-east-1:111122223333:flow:1-23aBC45dEF67hiJ8-12AbC34DE5fG:AwardsShow" }, { "Status": "STANDBY", "SourceType": "OWNED", "AvailabilityZone": "us-west-2c", "Description": "LA basketball game", "Name": "BasketballGame", "FlowArn": "arn:aws:mediaconnect:us-east-1:111122223333:flow:1-23aBC45dEF67hiJ8-12AbC34DE5fG:BasketballGame" } ] }`For more information, see [Viewing a List of Flows](https://docs.aws.amazon.com/mediaconnect/latest/ug/flows-view-list.html)in the*AWS Elemental MediaConnect User Guide*.- 
                    For API details, see [ListFlows](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/mediaconnect/list-flows.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `list-tags-for-resource`.

- **AWS CLI**
- 
            
                    **To list tags for a MediaConnect resource**The following `list-tags-for-resource`example displays the tag keys and values associated with the specified MediaConnect resource.`aws mediaconnect list-tags-for-resource \ --resource-arn``arn:aws:mediaconnect:us-east-1:123456789012:flow:1-23aBC45dEF67hiJ8-12AbC34DE5fG:BasketballGame`Output: `{ "Tags": { "region": "west", "stage": "prod" } }`For more information, see [ListTagsForResource, TagResource, UntagResource](https://docs.aws.amazon.com/mediaconnect/latest/api/tags-resourcearn.html)in the*AWS Elemental MediaConnect API Reference*.- 
                    For API details, see [ListTagsForResource](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/mediaconnect/list-tags-for-resource.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `remove-flow-output`.

- **AWS CLI**
- 
            
                    **To remove an output from a flow**The following `remove-flow-output`example removes an output from the specified flow.`aws mediaconnect remove-flow-output \ --flow-arn``arn:aws:mediaconnect:us-east-1:111122223333:flow:1-23aBC45dEF67hiJ8-12AbC34DE5fG:BaseballGame`\ --output-arn`arn:aws:mediaconnect:us-east-1:111122223333:output:2-3aBC45dEF67hiJ89-c34de5fG678h:NYC`Output: `{ "FlowArn": "arn:aws:mediaconnect:us-east-1:111122223333:flow:1-23aBC45dEF67hiJ8-12AbC34DE5fG:BaseballGame", "OutputArn": "arn:aws:mediaconnect:us-east-1:111122223333:output:2-3aBC45dEF67hiJ89-c34de5fG678h:NYC" }`For more information, see [Removing Outputs from a Flow](https://docs.aws.amazon.com/mediaconnect/latest/ug/outputs-remove.html)in the*AWS Elemental MediaConnect User Guide*.- 
                    For API details, see [RemoveFlowOutput](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/mediaconnect/remove-flow-output.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `revoke-flow-entitlement`.

- **AWS CLI**
- 
            
                    **To revoke an entitlement**The following `revoke-flow-entitlement`example revokes an entitlement on the specified flow.`aws mediaconnect revoke-flow-entitlement \ --flow-arn``arn:aws:mediaconnect:us-east-1:111122223333:flow:1-23aBC45dEF67hiJ8-12AbC34DE5fG:BaseballGame`\ --entitlement-arn`arn:aws:mediaconnect:us-west-2:111122223333:entitlement:1-11aa22bb11aa22bb-3333cccc4444:AnyCompany_Entitlement`Output: `{ "FlowArn": "arn:aws:mediaconnect:us-east-1:111122223333:flow:1-23aBC45dEF67hiJ8-12AbC34DE5fG:BaseballGame", "EntitlementArn": "arn:aws:mediaconnect:us-west-2:111122223333:entitlement:1-11aa22bb11aa22bb-3333cccc4444:AnyCompany_Entitlement" }`For more information, see [Revoking an Entitlement](https://docs.aws.amazon.com/mediaconnect/latest/ug/entitlements-revoke.html)in the*AWS Elemental MediaConnect User Guide*.- 
                    For API details, see [RevokeFlowEntitlement](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/mediaconnect/revoke-flow-entitlement.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `start-flow`.

- **AWS CLI**
- 
            
                    **To start a flow**The following `start-flow`example starts the specified flow.`aws mediaconnect start-flow \ --flow-arn``arn:aws:mediaconnect:us-east-1:123456789012:flow:1-23aBC45dEF67hiJ8-12AbC34DE5fG:AwardsShow`This command produces no output. Output: `{ "FlowArn": "arn:aws:mediaconnect:us-east-1:123456789012:flow:1-23aBC45dEF67hiJ8-12AbC34DE5fG:AwardsShow", "Status": "STARTING" }`For more information, see [Starting a Flow](https://docs.aws.amazon.com/mediaconnect/latest/ug/flows-start.html)in the*AWS Elemental MediaConnect User Guide*.- 
                    For API details, see [StartFlow](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/mediaconnect/start-flow.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `stop-flow`.

- **AWS CLI**
- 
            
                    **To stop a flow**The following `stop-flow`example stops the specified flow.`aws mediaconnect stop-flow \ --flow-arn``arn:aws:mediaconnect:us-east-1:123456789012:flow:1-23aBC45dEF67hiJ8-12AbC34DE5fG:AwardsShow`Output: `{ "Status": "STOPPING", "FlowArn": "arn:aws:mediaconnect:us-east-1:123456789012:flow:1-23aBC45dEF67hiJ8-12AbC34DE5fG:AwardsShow" }`For more information, see [Stopping a Flow](https://docs.aws.amazon.com/mediaconnect/latest/ug/flows-stop.html)in the*AWS Elemental MediaConnect User Guide*.- 
                    For API details, see [StopFlow](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/mediaconnect/stop-flow.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `tag-resource`.

- **AWS CLI**
- 
            
                    **To add tags to a MediaConnect resource**The following `tag-resource`example adds a tag with a key name and value to the specified MediaConnect resource.`aws mediaconnect tag-resource \ --resource-arn``arn:aws:mediaconnect:us-east-1:123456789012:flow:1-23aBC45dEF67hiJ8-12AbC34DE5fG:BasketballGame`--tags`region=west`This command produces no output. For more information, see [ListTagsForResource, TagResource, UntagResource](https://docs.aws.amazon.com/mediaconnect/latest/api/tags-resourcearn.html)in the*AWS Elemental MediaConnect API Reference*.- 
                    For API details, see [TagResource](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/mediaconnect/tag-resource.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `untag-resource`.

- **AWS CLI**
- 
            
                    **To remove tags from a MediaConnect resource**The following `untag-resource`example remove the tag with the specified key name and its associated value from a MediaConnect resource.`aws mediaconnect untag-resource \ --resource-arn``arn:aws:mediaconnect:us-east-1:123456789012:flow:1-23aBC45dEF67hiJ8-12AbC34DE5fG:BasketballGame`\ --tag-keys`region`This command produces no output. For more information, see [ListTagsForResource, TagResource, UntagResource](https://docs.aws.amazon.com/mediaconnect/latest/api/tags-resourcearn.html)in the*AWS Elemental MediaConnect API Reference*.- 
                    For API details, see [UntagResource](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/mediaconnect/untag-resource.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `update-flow-entitlement`.

- **AWS CLI**
- 
            
                    **To update an entitlement**The following `update-flow-entitlement`example updates the specified entitlement with a new description and subscriber.`aws mediaconnect update-flow-entitlement \ --flow-arn``arn:aws:mediaconnect:us-east-1:111122223333:flow:1-23aBC45dEF67hiJ8-12AbC34DE5fG:BaseballGame`\ --entitlement-arn`arn:aws:mediaconnect:us-west-2:111122223333:entitlement:1-11aa22bb11aa22bb-3333cccc4444:AnyCompany_Entitlement`\ --description '`For AnyCompany Affiliate`' \ --subscribers`777788889999`Output: `{ "FlowArn": "arn:aws:mediaconnect:us-east-1:111122223333:flow:1-23aBC45dEF67hiJ8-12AbC34DE5fG:BaseballGame", "Entitlement": { "Name": "AnyCompany_Entitlement", "Description": "For AnyCompany Affiliate", "EntitlementArn": "arn:aws:mediaconnect:us-west-2:111122223333:entitlement:1-11aa22bb11aa22bb-3333cccc4444:AnyCompany_Entitlement", "Encryption": { "KeyType": "static-key", "Algorithm": "aes128", "RoleArn": "arn:aws:iam::111122223333:role/MediaConnect-ASM", "SecretArn": "arn:aws:secretsmanager:us-west-2:111122223333:secret:mySecret1" }, "Subscribers": [ "777788889999" ] } }`For more information, see [Updating an Entitlement](https://docs.aws.amazon.com/mediaconnect/latest/ug/entitlements-update.html)in the*AWS Elemental MediaConnect User Guide*.- 
                    For API details, see [UpdateFlowEntitlement](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/mediaconnect/update-flow-entitlement.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `update-flow-output`.

- **AWS CLI**
- 
            
                    **To update an output on a flow**The following `update-flow-output`example update an output on the specified flow.`aws mediaconnect update-flow-output \ --flow-arn``arn:aws:mediaconnect:us-east-1:111122223333:flow:1-23aBC45dEF67hiJ8-12AbC34DE5fG:BaseballGame`\ --output-arn`arn:aws:mediaconnect:us-east-1:111122223333:output:2-3aBC45dEF67hiJ89-c34de5fG678h:NYC`\ --port`3331`Output: `{ "FlowArn": "arn:aws:mediaconnect:us-east-1:111122223333:flow:1-23aBC45dEF67hiJ8-12AbC34DE5fG:BaseballGame", "Output": { "Name": "NYC", "Port": 3331, "Description": "NYC stream", "Transport": { "Protocol": "rtp-fec", "SmoothingLatency": 100 }, "OutputArn": "arn:aws:mediaconnect:us-east-1:111122223333:output:2-3aBC45dEF67hiJ89-c34de5fG678h:NYC", "Destination": "192.0.2.12" } }`For more information, see [Updating Outputs on a Flow](https://docs.aws.amazon.com/mediaconnect/latest/ug/outputs-update.html)in the*AWS Elemental MediaConnect User Guide*.- 
                    For API details, see [UpdateFlowOutput](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/mediaconnect/update-flow-output.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `update-flow-source`.

- **AWS CLI**
- 
            
                    **To update the source of an existing flow**The following `update-flow-source`example updates the source of an existing flow.`aws mediaconnect update-flow-source \ --flow-arn``arn:aws:mediaconnect:us-east-1:111122223333:flow:1-23aBC45dEF67hiJ8-12AbC34DE5fG:AwardsShow`\ --source-arn`arn:aws:mediaconnect:us-east-1:111122223333:source:3-4aBC56dEF78hiJ90-4de5fG6Hi78Jk:ShowSource`\ --description '`Friday night show`' \ --ingest-port`3344`\ --protocol`rtp-fec`\ --whitelist-cidr`10.24.34.0/23`Output: `{ "FlowArn": "arn:aws:mediaconnect:us-east-1:111122223333:flow:1-23aBC45dEF67hiJ8-12AbC34DE5fG:AwardsShow", "Source": { "IngestIp": "34.210.136.56", "WhitelistCidr": "10.24.34.0/23", "Transport": { "Protocol": "rtp-fec" }, "IngestPort": 3344, "Name": "ShowSource", "Description": "Friday night show", "SourceArn": "arn:aws:mediaconnect:us-east-1:111122223333:source:3-4aBC56dEF78hiJ90-4de5fG6Hi78Jk:ShowSource" } }`For more information, see [Updating the Source of a Flow](https://docs.aws.amazon.com/mediaconnect/latest/ug/source-update.html)in the*AWS Elemental MediaConnect User Guide*.- 
                    For API details, see [UpdateFlowSource](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/mediaconnect/update-flow-source.html)in*AWS CLI Command Reference*.
 
-