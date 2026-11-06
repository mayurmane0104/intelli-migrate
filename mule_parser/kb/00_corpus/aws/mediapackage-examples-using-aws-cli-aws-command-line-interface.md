# MediaPackage examples using AWS CLI - AWS Command Line Interface

**Source:** [https://docs.aws.amazon.com/cli/latest/userguide/cli_mediapackage_code_examples.html](https://docs.aws.amazon.com/cli/latest/userguide/cli_mediapackage_code_examples.html)

---

The following code examples show you how to perform actions and implement common scenarios by using the AWS Command Line Interface with MediaPackage.

*Actions* are code excerpts from larger programs and must be run in context. While actions show you how to call individual service functions, you can see actions in context in their related scenarios.

Each example includes a link to the complete source code, where you can find instructions on how to set up and run the code in context.

###### Topics

## Actions

    The following code example shows how to use `create-channel`.

- **AWS CLI**
- 
            
                    **To create a channel**The following `create-channel`command creates a channel named`sportschannel`in the current account.`aws mediapackage create-channel --id``sportschannel`Output: `{ "Arn": "arn:aws:mediapackage:us-west-2:111222333:channels/6d345804ec3f46c9b454a91d4a80d0e0", "HlsIngest": { "IngestEndpoints": [ { "Id": "6d345804ec3f46c9b454a91d4a80d0e0", "Password": "generatedwebdavpassword1", "Url": "https://f31c86aed53b815a.mediapackage.us-west-2.amazonaws.com/in/v2/6d345804ec3f46c9b454a91d4a80d0e0/6d345804ec3f46c9b454a91d4a80d0e0/channel", "Username": "generatedwebdavusername1" }, { "Id": "2daa32878af24803b24183727211b8ff", "Password": "generatedwebdavpassword2", "Url": "https://6ebbe7e04c4b0afa.mediapackage.us-west-2.amazonaws.com/in/v2/6d345804ec3f46c9b454a91d4a80d0e0/2daa32878af24803b24183727211b8ff/channel", "Username": "generatedwebdavusername2" } ] }, "Id": "sportschannel", "Tags": { "region": "west" } }`For more information, see [Creating a Channel](https://docs.aws.amazon.com/mediapackage/latest/ug/channels-create.html)in the*AWS Elemental MediaPackage User Guide*.- 
                    For API details, see [CreateChannel](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/mediapackage/create-channel.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `create-origin-endpoint`.

- **AWS CLI**
- 
            
                    **To create an origin endpoint**The following `create-origin-endpoint`command creates an origin endpoint named`cmafsports`with the package settings provided in a JSON file and specified endpoint settings.`aws mediapackage create-origin-endpoint \ --channel-id``sportschannel`\ --id`cmafsports`\ --cmaf-package`file://file/path/cmafpkg.json`--description`"cmaf output of sports"`\ --id`cmaf_sports`\ --manifest-name`sports_channel`\ --startover-window-seconds`300`\ --tags`region=west,media=sports`\ --time-delay-seconds`10`Output: `{ "Arn": "arn:aws:mediapackage:us-west-2:111222333:origin_endpoints/1dc6718be36f4f34bb9cd86bc50925e6", "ChannelId": "sportschannel", "CmafPackage": { "HlsManifests": [ { "AdMarkers": "PASSTHROUGH", "Id": "cmaf_sports_endpoint", "IncludeIframeOnlyStream": true, "ManifestName": "index", "PlaylistType": "EVENT", "PlaylistWindowSeconds": 300, "ProgramDateTimeIntervalSeconds": 300, "Url": "https://c4af3793bf76b33c.mediapackage.us-west-2.amazonaws.com/out/v1/1dc6718be36f4f34bb9cd86bc50925e6/cmaf_sports_endpoint/index.m3u8" } ], "SegmentDurationSeconds": 2, "SegmentPrefix": "sportschannel" }, "Description": "cmaf output of sports", "Id": "cmaf_sports", "ManifestName": "sports_channel", "StartoverWindowSeconds": 300, "Tags": { "region": "west", "media": "sports" }, "TimeDelaySeconds": 10, "Url": "", "Whitelist": [] }`For more information, see [Creating an Endpoint](https://docs.aws.amazon.com/mediapackage/latest/ug/endpoints-create.html)in the*AWS Elemental MediaPackage User Guide*.- 
                    For API details, see [CreateOriginEndpoint](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/mediapackage/create-origin-endpoint.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `delete-channel`.

- **AWS CLI**
- 
            
                    **To delete a channel**The following `delete-channel`command deletes the channel named`test`.`aws mediapackage delete-channel \ --id``test`This command produces no output. For more information, see [Deleting a Channel](https://docs.aws.amazon.com/mediapackage/latest/ug/channels-delete.html)in the*AWS Elemental MediaPackage User Guide*.- 
                    For API details, see [DeleteChannel](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/mediapackage/delete-channel.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `delete-origin-endpoint`.

- **AWS CLI**
- 
            
                    **To delete an origin endpoint**The following `delete-origin-endpoint`command deletes the origin endpoint named`tester2`.`aws mediapackage delete-origin-endpoint \ --id``tester2`For more information, see [Deleting an Endpoint](https://docs.aws.amazon.com/mediapackage/latest/ug/endpoints-delete.html)in the*AWS Elemental MediaPackage User Guide*.- 
                    For API details, see [DeleteOriginEndpoint](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/mediapackage/delete-origin-endpoint.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `describe-channel`.

- **AWS CLI**
- 
            
                    **To describe a channel**The following `describe-channel`command displays all of the details of the channel named`test`.`aws mediapackage describe-channel \ --id``test`Output: `{ "Arn": "arn:aws:mediapackage:us-west-2:111222333:channels/584797f1740548c389a273585dd22a63", "HlsIngest": { "IngestEndpoints": [ { "Id": "584797f1740548c389a273585dd22a63", "Password": "webdavgeneratedpassword1", "Url": "https://9be9c4405c474882.mediapackage.us-west-2.amazonaws.com/in/v2/584797f1740548c389a273585dd22a63/584797f1740548c389a273585dd22a63/channel", "Username": "webdavgeneratedusername1" }, { "Id": "7d187c8616fd455f88aaa5a9fcf74442", "Password": "webdavgeneratedpassword2", "Url": "https://7bf454c57220328d.mediapackage.us-west-2.amazonaws.com/in/v2/584797f1740548c389a273585dd22a63/7d187c8616fd455f88aaa5a9fcf74442/channel", "Username": "webdavgeneratedusername2" } ] }, "Id": "test", "Tags": {} }`For more information, see Viewing Channel Details<https://docs.aws.amazon.com/mediapackage/latest/ug/channels-view.html> in the *AWS Elemental MediaPackage User Guide*- 
                    For API details, see [DescribeChannel](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/mediapackage/describe-channel.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `describe-origin-endpoint`.

- **AWS CLI**
- 
            
                    **To describe an origin endpoint**The following `describe-origin-endpoint`command displays all of the details of the origin endpoint named`cmaf_sports`.`aws mediapackage describe-origin-endpoint \ --id``cmaf_sports`Output: `{ "Arn": "arn:aws:mediapackage:us-west-2:111222333:origin_endpoints/1dc6718be36f4f34bb9cd86bc50925e6", "ChannelId": "sportschannel", "CmafPackage": { "HlsManifests": [ { "AdMarkers": "NONE", "Id": "cmaf_sports_endpoint", "IncludeIframeOnlyStream": false, "PlaylistType": "EVENT", "PlaylistWindowSeconds": 60, "ProgramDateTimeIntervalSeconds": 0, "Url": "https://c4af3793bf76b33c.mediapackage.us-west-2.amazonaws.com/out/v1/1dc6718be36f4f34bb9cd86bc50925e6/cmaf_sports_endpoint/index.m3u8" } ], "SegmentDurationSeconds": 2, "SegmentPrefix": "sportschannel" }, "Id": "cmaf_sports", "ManifestName": "index", "StartoverWindowSeconds": 0, "Tags": { "region": "west", "media": "sports" }, "TimeDelaySeconds": 0, "Url": "", "Whitelist": [] }`For more information, see [Viewing a Single Endpoint](https://docs.aws.amazon.com/mediapackage/latest/ug/endpoints-view-one.html)in the*AWS Elemental MediaPackage User Guide*.- 
                    For API details, see [DescribeOriginEndpoint](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/mediapackage/describe-origin-endpoint.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `list-channels`.

- **AWS CLI**
- 
            
                    **To list all channels**The following `list-channels`command lists all of the channels that are configured on the current AWS account.`aws mediapackage list-channels`Output: `{ "Channels": [ { "Arn": "arn:aws:mediapackage:us-west-2:111222333:channels/584797f1740548c389a273585dd22a63", "HlsIngest": { "IngestEndpoints": [ { "Id": "584797f1740548c389a273585dd22a63", "Password": "webdavgeneratedpassword1", "Url": "https://9be9c4405c474882.mediapackage.us-west-2.amazonaws.com/in/v2/584797f1740548c389a273585dd22a63/584797f1740548c389a273585dd22a63/channel", "Username": "webdavgeneratedusername1" }, { "Id": "7d187c8616fd455f88aaa5a9fcf74442", "Password": "webdavgeneratedpassword2", "Url": "https://7bf454c57220328d.mediapackage.us-west-2.amazonaws.com/in/v2/584797f1740548c389a273585dd22a63/7d187c8616fd455f88aaa5a9fcf74442/channel", "Username": "webdavgeneratedusername2" } ] }, "Id": "test", "Tags": {} } ] }`For more information, see [Viewing Channel Details](https://docs.aws.amazon.com/mediapackage/latest/ug/channels-view.html)in the*AWS Elemental MediaPackage User Guide*.- 
                    For API details, see [ListChannels](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/mediapackage/list-channels.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `list-origin-endpoints`.

- **AWS CLI**
- 
            
                    **To list all origin-endpoints on a channel**The following `list-origin-endpoints`command lists all of the origin endpoints that are configured on the channel named`test`.`aws mediapackage list-origin-endpoints \ --channel-id``test`Output: `{ "OriginEndpoints": [ { "Arn": "arn:aws:mediapackage:us-west-2:111222333:origin_endpoints/247cff871f2845d3805129be22f2c0a2", "ChannelId": "test", "DashPackage": { "ManifestLayout": "FULL", "ManifestWindowSeconds": 60, "MinBufferTimeSeconds": 30, "MinUpdatePeriodSeconds": 15, "PeriodTriggers": [], "Profile": "NONE", "SegmentDurationSeconds": 2, "SegmentTemplateFormat": "NUMBER_WITH_TIMELINE", "StreamSelection": { "MaxVideoBitsPerSecond": 2147483647, "MinVideoBitsPerSecond": 0, "StreamOrder": "ORIGINAL" }, "SuggestedPresentationDelaySeconds": 25 }, "Id": "tester2", "ManifestName": "index", "StartoverWindowSeconds": 0, "Tags": {}, "TimeDelaySeconds": 0, "Url": "https://8343f7014c0ea438.mediapackage.us-west-2.amazonaws.com/out/v1/247cff871f2845d3805129be22f2c0a2/index.mpd", "Whitelist": [] }, { "Arn": "arn:aws:mediapackage:us-west-2:111222333:origin_endpoints/869e237f851549e9bcf10e3bc2830839", "ChannelId": "test", "HlsPackage": { "AdMarkers": "NONE", "IncludeIframeOnlyStream": false, "PlaylistType": "EVENT", "PlaylistWindowSeconds": 60, "ProgramDateTimeIntervalSeconds": 0, "SegmentDurationSeconds": 6, "StreamSelection": { "MaxVideoBitsPerSecond": 2147483647, "MinVideoBitsPerSecond": 0, "StreamOrder": "ORIGINAL" }, "UseAudioRenditionGroup": false }, "Id": "tester", "ManifestName": "index", "StartoverWindowSeconds": 0, "Tags": {}, "TimeDelaySeconds": 0, "Url": "https://8343f7014c0ea438.mediapackage.us-west-2.amazonaws.com/out/v1/869e237f851549e9bcf10e3bc2830839/index.m3u8", "Whitelist": [] } ] }`For more information, see [Viewing all Endpoints Associated with a Channel](https://docs.aws.amazon.com/mediapackage/latest/ug/endpoints-view-all.html)in the*AWS Elemental MediaPackage User Guide*.- 
                    For API details, see [ListOriginEndpoints](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/mediapackage/list-origin-endpoints.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `list-tags-for-resource`.

- **AWS CLI**
- 
            
                    **To list the tags assigned to a resource**The following `list-tags-for-resource`command lists the tags that are assigned to the specified resource.`aws mediapackage list-tags-for-resource \ --resource-arn``arn:aws:mediapackage:us-west-2:111222333:channels/6d345804ec3f46c9b454a91d4a80d0e0`Output: `{ "Tags": { "region": "west" } }`For more information, see [Tagging Resources in AWS Elemental MediaPackage](https://docs.aws.amazon.com/mediapackage/latest/ug/tagging.html)in the*AWS Elemental MediaPackage User Guide*.- 
                    For API details, see [ListTagsForResource](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/mediapackage/list-tags-for-resource.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `rotate-ingest-endpoint-credentials`.

- **AWS CLI**
- 
            
                    **To rotate ingest credentials**The following `rotate-ingest-endpoint-credentials`command rotates the WebDAV username and password for the specified ingest endpoint.`aws mediapackage rotate-ingest-endpoint-credentials \ --id``test`\ --ingest-endpoint-id`584797f1740548c389a273585dd22a63`Output: `{ "Arn": "arn:aws:mediapackage:us-west-2:111222333:channels/584797f1740548c389a273585dd22a63", "HlsIngest": { "IngestEndpoints": [ { "Id": "584797f1740548c389a273585dd22a63", "Password": "webdavregeneratedpassword1", "Url": "https://9be9c4405c474882.mediapackage.us-west-2.amazonaws.com/in/v2/584797f1740548c389a273585dd22a63/584797f1740548c389a273585dd22a63/channel", "Username": "webdavregeneratedusername1" }, { "Id": "7d187c8616fd455f88aaa5a9fcf74442", "Password": "webdavgeneratedpassword2", "Url": "https://7bf454c57220328d.mediapackage.us-west-2.amazonaws.com/in/v2/584797f1740548c389a273585dd22a63/7d187c8616fd455f88aaa5a9fcf74442/channel", "Username": "webdavgeneratedusername2" } ] }, "Id": "test", "Tags": {} }`For more information, see [Rotating Credentials on an Input URL](https://docs.aws.amazon.com/mediapackage/latest/ug/channels-rotate-creds)in the*AWS Elemental MediaPackage User Guide*.- 
                    For API details, see [RotateIngestEndpointCredentials](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/mediapackage/rotate-ingest-endpoint-credentials.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `tag-resource`.

- **AWS CLI**
- 
            
                    **To add a tag to a resource**The following `tag-resource`commands adds a`region=west`key and value pair to the specified resource.`aws mediapackage tag-resource \ --resource-arn``arn:aws:mediapackage:us-west-2:111222333:channels/6d345804ec3f46c9b454a91d4a80d0e0`\ --tags`region=west`This command produces no output. For more information, see [Tagging Resources in AWS Elemental MediaPackage](https://docs.aws.amazon.com/mediapackage/latest/ug/tagging.html)in the*AWS Elemental MediaPackage User Guide*.- 
                    For API details, see [TagResource](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/mediapackage/tag-resource.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `untag-resource`.

- **AWS CLI**
- 
            
                    **To remove a tag from a resource**The following `untag-resource`command removes the tag with the key`region`from the specified channel.`aws mediapackage untag-resource \ --resource-arn``arn:aws:mediapackage:us-west-2:111222333:channels/6d345804ec3f46c9b454a91d4a80d0e0`\ --tag-keys`region`For more information, see [Tagging Resources in AWS Elemental MediaPackage](https://docs.aws.amazon.com/mediapackage/latest/ug/tagging.html)in the*AWS Elemental MediaPackage User Guide*.- 
                    For API details, see [UntagResource](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/mediapackage/untag-resource.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `update-channel`.

- **AWS CLI**
- 
            
                    **To update a channel**The following `update-channel`command updates the channel named`sportschannel`to include the description`24x7 sports`.`aws mediapackage update-channel \ --id``sportschannel`\ --description`"24x7 sports"`Output: `{ "Arn": "arn:aws:mediapackage:us-west-2:111222333:channels/6d345804ec3f46c9b454a91d4a80d0e0", "Description": "24x7 sports", "HlsIngest": { "IngestEndpoints": [ { "Id": "6d345804ec3f46c9b454a91d4a80d0e0", "Password": "generatedwebdavpassword1", "Url": "https://f31c86aed53b815a.mediapackage.us-west-2.amazonaws.com/in/v2/6d345804ec3f46c9b454a91d4a80d0e0/6d345804ec3f46c9b454a91d4a80d0e0/channel", "Username": "generatedwebdavusername1" }, { "Id": "2daa32878af24803b24183727211b8ff", "Password": "generatedwebdavpassword2", "Url": "https://6ebbe7e04c4b0afa.mediapackage.us-west-2.amazonaws.com/in/v2/6d345804ec3f46c9b454a91d4a80d0e0/2daa32878af24803b24183727211b8ff/channel", "Username": "generatedwebdavusername2" } ] }, "Id": "sportschannel", "Tags": {} }`For more information, see [Editing a Channel](https://docs.aws.amazon.com/mediapackage/latest/ug/channels-edit.html)in the*AWS Elemental MediaPackage User Guide*.- 
                    For API details, see [UpdateChannel](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/mediapackage/update-channel.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `update-origin-endpoint`.

- **AWS CLI**
- 
            
                    **To update an origin endpoint**The following `update-origin-endpoint`command updates the origin endpoint named`cmaf_sports`. It changes the time delay to`0`seconds.`aws mediapackage update-origin-endpoint \ --id``cmaf_sports`\ --time-delay-seconds`0`Output: `{ "Arn": "arn:aws:mediapackage:us-west-2:111222333:origin_endpoints/1dc6718be36f4f34bb9cd86bc50925e6", "ChannelId": "sportschannel", "CmafPackage": { "HlsManifests": [ { "AdMarkers": "NONE", "Id": "cmaf_sports_endpoint", "IncludeIframeOnlyStream": false, "PlaylistType": "EVENT", "PlaylistWindowSeconds": 60, "ProgramDateTimeIntervalSeconds": 0, "Url": "https://c4af3793bf76b33c.mediapackage.us-west-2.amazonaws.com/out/v1/1dc6718be36f4f34bb9cd86bc50925e6/cmaf_sports_endpoint/index.m3u8" } ], "SegmentDurationSeconds": 2, "SegmentPrefix": "sportschannel" }, "Id": "cmaf_sports", "ManifestName": "index", "StartoverWindowSeconds": 0, "Tags": { "region": "west", "media": "sports" }, "TimeDelaySeconds": 0, "Url": "", "Whitelist": [] }`For more information, see [Editing an Endpoint](https://docs.aws.amazon.com/mediapackage/latest/ug/endpoints-edit.html)in the*AWS Elemental MediaPackage User Guide*.- 
                    For API details, see [UpdateOriginEndpoint](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/mediapackage/update-origin-endpoint.html)in*AWS CLI Command Reference*.
 
-