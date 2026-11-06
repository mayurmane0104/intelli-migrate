# MediaPackage VOD examples using AWS CLI - AWS Command Line Interface

**Source:** [https://docs.aws.amazon.com/cli/latest/userguide/cli_mediapackage-vod_code_examples.html](https://docs.aws.amazon.com/cli/latest/userguide/cli_mediapackage-vod_code_examples.html)

---

The following code examples show you how to perform actions and implement common scenarios by using the AWS Command Line Interface with MediaPackage VOD.

*Actions* are code excerpts from larger programs and must be run in context. While actions show you how to call individual service functions, you can see actions in context in their related scenarios.

Each example includes a link to the complete source code, where you can find instructions on how to set up and run the code in context.

###### Topics

## Actions

    The following code example shows how to use `create-asset`.

- **AWS CLI**
- 
            
                    **To create an asset**The following `create-asset`example creates an asset named`Chicken_Asset`in the current AWS account. The asset ingests the file`30sec_chicken.smil`to MediaPackage.`aws mediapackage-vod create-asset \ --id``chicken_asset`\ --packaging-group-id`hls_chicken_gp`\ --source-role-arn`arn:aws:iam::111122223333:role/EMP_Vod`\ --source-arn`arn:aws:s3::111122223333:video-bucket/A/30sec_chicken.smil`Output: `{ "Arn":"arn:aws:mediapackage-vod:us-west-2:111122223333:assets/chicken_asset", "Id":"chicken_asset", "PackagingGroupId":"hls_chicken_gp", "SourceArn":"arn:aws:s3::111122223333:video-bucket/A/30sec_chicken.smil", "SourceRoleArn":"arn:aws:iam::111122223333:role/EMP_Vod", "EgressEndpoints":[ { "PackagingConfigurationId":"New_config_1", "Url":"https://c75ea2668ab49d02bca7ae10ef31c59e.egress.mediapackage-vod.us-west-2.amazonaws.com/out/v1/6644b55df1744261ab3732a8e5cdaf07/904b06a58c7645e08d57d40d064216ac/f5b2e633ff4942228095d164c10074f3/index.m3u8" }, { "PackagingConfigurationId":"new_hls", "Url":" https://c75ea2668ab49d02bca7ae10ef31c59e.egress.mediapackage-vod.us-west-2.amazonaws.com/out/v1/6644b55df1744261ab3732a8e5cdaf07/fe8f1f00a80e424cb4f8da4095835e9e/7370ec57432343af816332356d2bd5c6/string.m3u8" } ] }`For more information, see [Ingest an Asset](https://docs.aws.amazon.com/mediapackage/latest/ug/asset-create.html)in the*AWS Elemental MediaPackage User Guide*.- 
                    For API details, see [CreateAsset](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/mediapackage-vod/create-asset.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `create-packaging-configuration`.

- **AWS CLI**
- 
            
                    **To create a packaging configuration**The following `create-packaging-configuration`example creates a packaging configuration named`new_hls`in the packaging group named`hls_chicken`. This example uses a file on disk named`hls_pc.json`to provide the details.`aws mediapackage-vod create-packaging-configuration \ --id``new_hls`\ --packaging-group-id`hls_chicken`\ --hls-package`file://hls_pc.json`Contents of `hls_pc.json`:`{ "HlsManifests":[ { "AdMarkers":"NONE", "IncludeIframeOnlyStream":false, "ManifestName":"string", "ProgramDateTimeIntervalSeconds":60, "RepeatExtXKey":true, "StreamSelection":{ "MaxVideoBitsPerSecond":1000, "MinVideoBitsPerSecond":0, "StreamOrder":"ORIGINAL" } } ], "SegmentDurationSeconds":6, "UseAudioRenditionGroup":false }`Output: `{ "Arn":"arn:aws:mediapackage-vod:us-west-2:111122223333:packaging-configurations/new_hls", "Id":"new_hls", "PackagingGroupId":"hls_chicken", "HlsManifests":{ "SegmentDurationSeconds":6, "UseAudioRenditionGroup":false, "HlsMarkers":[ { "AdMarkers":"NONE", "IncludeIframeOnlyStream":false, "ManifestName":"string", "ProgramDateTimeIntervalSeconds":60, "RepeatExtXKey":true, "StreamSelection":{ "MaxVideoBitsPerSecond":1000, "MinVideoBitsPerSecond":0, "StreamOrder":"ORIGINAL" } } ] } }`For more information, see [Creating a Packaging Configuration](https://docs.aws.amazon.com/mediapackage/latest/ug/pkg-cfig-create.html)in the*AWS Elemental MediaPackage User Guide*.- 
                    For API details, see [CreatePackagingConfiguration](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/mediapackage-vod/create-packaging-configuration.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `create-packaging-group`.

- **AWS CLI**
- 
            
                    **To create a packaging group**The following `create-packaging-group`example lists all of the packaging groups that are configured in the current AWS account.`aws mediapackage-vod create-packaging-group \ --id``hls_chicken`Output: `{ "Arn": "arn:aws:mediapackage-vod:us-west-2:111122223333:packaging-groups/hls_chicken", "Id": "hls_chicken" }`For more information, see [Creating a Packaging Group](https://docs.aws.amazon.com/mediapackage/latest/ug/pkg-group-create.html)in the*AWS Elemental MediaPackage User Guide*.- 
                    For API details, see [CreatePackagingGroup](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/mediapackage-vod/create-packaging-group.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `delete-asset`.

- **AWS CLI**
- 
            
                    **To delete an asset**The following `delete-asset`example deletes the asset named`30sec_chicken`.`aws mediapackage-vod delete-asset \ --id``30sec_chicken`This command produces no output. For more information, see [Deleting an Asset](https://docs.aws.amazon.com/mediapackage/latest/ug/asset-delete.html)in the*AWS Elemental MediaPackage User Guide*.- 
                    For API details, see [DeleteAsset](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/mediapackage-vod/delete-asset.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `delete-packaging-configuration`.

- **AWS CLI**
- 
            
                    **To delete a packaging configuration**The following `delete-packaging-configuration`example deletes the packaging configuration named`CMAF`.`aws mediapackage-vod delete-packaging-configuration \ --id``CMAF`This command produces no output. For more information, see [Deleting a Packaging Configuration](https://docs.aws.amazon.com/mediapackage/latest/ug/pkg-cfig-delete.html)in the*AWS Elemental MediaPackage User Guide*.- 
                    For API details, see [DeletePackagingConfiguration](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/mediapackage-vod/delete-packaging-configuration.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `delete-packaging-group`.

- **AWS CLI**
- 
            
                    **To delete a packaging group**The following `delete-packaging-group`example deletes the packaging group named`Dash_widevine`.`aws mediapackage-vod delete-packaging-group \ --id``Dash_widevine`This command produces no output. For more information, see [Deleting a Packaging Group](https://docs.aws.amazon.com/mediapackage/latest/ug/pkg-group-delete.html)in the*AWS Elemental MediaPackage User Guide*.- 
                    For API details, see [DeletePackagingGroup](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/mediapackage-vod/delete-packaging-group.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `describe-asset`.

- **AWS CLI**
- 
            
                    **To describe an asset**The following `describe-asset`example displays all of the details of the asset named`30sec_chicken`.`aws mediapackage-vod describe-asset \ --id``30sec_chicken`Output: `{ "Arn":"arn:aws:mediapackage-vod:us-west-2:111122223333:assets/30sec_chicken", "Id":"30sec_chicken", "PackagingGroupId":"Packaging_group_1", "SourceArn":"arn:aws:s3::111122223333:video-bucket/A/30sec_chicken.smil", "SourceRoleArn":"arn:aws:iam::111122223333:role/EMP_Vod", "EgressEndpoints":[ { "PackagingConfigurationId":"DASH", "Url":"https://a5f46a44118ba3e3724ef39ef532e701.egress.mediapackage-vod.us-west-2.amazonaws.com/out/v1/aad7962c569946119c2d5a691be5663c/66c25aff456d463aae0855172b3beb27/4ddfda6da17c4c279a1b8401cba31892/index.mpd" }, { "PackagingConfigurationId":"HLS", "Url":"https://a5f46a44118ba3e3724ef39ef532e701.egress.mediapackage-vod.us-west-2.amazonaws.com/out/v1/aad7962c569946119c2d5a691be5663c/6e5bf286a3414254a2bf0d22ae148d7e/06b5875b4d004c3cbdc4da2dc4d14638/index.m3u8" }, { "PackagingConfigurationId":"CMAF", "Url":"https://a5f46a44118ba3e3724ef39ef532e701.egress.mediapackage-vod.us-west-2.amazonaws.com/out/v1/aad7962c569946119c2d5a691be5663c/628fb5d8d89e4702958b020af27fde0e/05eb062214064238ad6330a443aff7f7/index.m3u8" } ] }`For more information, see [Viewing Asset Details](https://docs.aws.amazon.com/mediapackage/latest/ug/asset-view.html)in the*AWS Elemental MediaPackage User Guide*.- 
                    For API details, see [DescribeAsset](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/mediapackage-vod/describe-asset.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `describe-packaging-configuration`.

- **AWS CLI**
- 
            
                    **To describe a packaging configuration**The following `describe-packaging-configuration`example displays all of the details of the packaging configuration named`DASH`.`aws mediapackage-vod describe-packaging-configuration \ --id``DASH`Output: `{ "Arn":"arn:aws:mediapackage-vod:us-west-2:111122223333:packaging-configurations/DASH", "Id":"DASH", "PackagingGroupId":"Packaging_group_1", "DashPackage":[ { "SegmentDurationSeconds":"2" }, { "DashManifests":{ "ManifestName":"index", "MinBufferTimeSeconds":"30", "Profile":"NONE" } } ] }`For more information, see [Viewing Packaging Configuration Details](https://docs.aws.amazon.com/mediapackage/latest/ug/pkg-cfig-view.html)in the*AWS Elemental MediaPackage User Guide*.- 
                    For API details, see [DescribePackagingConfiguration](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/mediapackage-vod/describe-packaging-configuration.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `describe-packaging-group`.

- **AWS CLI**
- 
            
                    **To describe a packaging group**The following `describe-packaging-group`example displays all of the details of the packaging group named`Packaging_group_1`.`aws mediapackage-vod describe-packaging-group \ --id``Packaging_group_1`Output: `{ "Arn": "arn:aws:mediapackage-vod:us-west-2:111122223333:packaging-groups/Packaging_group_1", "Id": "Packaging_group_1" }`For more information, see [Viewing Packaging Group Details](https://docs.aws.amazon.com/mediapackage/latest/ug/pkg-group-view.html)in the*AWS Elemental MediaPackage User Guide*.- 
                    For API details, see [DescribePackagingGroup](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/mediapackage-vod/describe-packaging-group.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `list-assets`.

- **AWS CLI**
- 
            
                    **To list all assets**The following `list-assets`example lists all of the assets that are configured in the current AWS account.`aws mediapackage-vod list-assets`Output: `{ "Assets": [ "Arn": "arn:aws:mediapackage-vod:us-west-2:111122223333:assets/30sec_chicken", "Id": "30sec_chicken", "PackagingGroupId": "Packaging_group_1", "SourceArn": "arn:aws:s3::111122223333:video-bucket/A/30sec_chicken.smil", "SourceRoleArn": "arn:aws:iam::111122223333:role/EMP_Vod" ] }`For more information, see [Viewing Asset Details](https://docs.aws.amazon.com/mediapackage/latest/ug/asset-view.html)in the*AWS Elemental MediaPackage User Guide*.- 
                    For API details, see [ListAssets](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/mediapackage-vod/list-assets.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `list-packaging-configurations`.

- **AWS CLI**
- 
            
                    **To list all packaging configurations**The following `list-packaging-configurations`example lists all of the packaging configurations that are configured on the packaging group named`Packaging_group_1`.`aws mediapackage-vod list-packaging-configurations \ --packaging-group-id``Packaging_group_1`Output: `{ "PackagingConfigurations":[ { "Arn":"arn:aws:mediapackage-vod:us-west-2:111122223333:packaging-configurations/CMAF", "Id":"CMAF", "PackagingGroupId":"Packaging_group_1", "CmafPackage":[ { "SegmentDurationSeconds":"2" }, { "HlsManifests":{ "AdMarkers":"NONE", "RepeatExtXKey":"False", "ManifestName":"index", "ProgramDateTimeIntervalSeconds":"0", "IncludeIframeOnlyStream":"False" } } ] }, { "Arn":"arn:aws:mediapackage-vod:us-west-2:111122223333:packaging-configurations/DASH", "Id":"DASH", "PackagingGroupId":"Packaging_group_1", "DashPackage":[ { "SegmentDurationSeconds":"2" }, { "DashManifests":{ "ManifestName":"index", "MinBufferTimeSeconds":"30", "Profile":"NONE" } } ] }, { "Arn":"arn:aws:mediapackage-vod:us-west-2:111122223333:packaging-configurations/HLS", "Id":"HLS", "PackagingGroupId":"Packaging_group_1", "HlsPackage":[ { "SegmentDurationSeconds":"6", "UseAudioRenditionGroup":"False" }, { "HlsManifests":{ "AdMarkers":"NONE", "RepeatExtXKey":"False", "ManifestName":"index", "ProgramDateTimeIntervalSeconds":"0", "IncludeIframeOnlyStream":"False" } } ] }, { "Arn":"arn:aws:mediapackage-vod:us-west-2:111122223333:packaging-configurations/New_config_0_copy", "Id":"New_config_0_copy", "PackagingGroupId":"Packaging_group_1", "HlsPackage":[ { "SegmentDurationSeconds":"6", "UseAudioRenditionGroup":"False" }, { "Encryption":{ "EncryptionMethod":"AWS_128", "SpekeKeyProvider":{ "RoleArn":"arn:aws:iam:111122223333::role/SPEKERole", "Url":"https://lfgubdvs97.execute-api.us-west-2.amazonaws.com/EkeStage/copyProtection/", "SystemIds":[ "81376844-f976-481e-a84e-cc25d39b0b33" ] } } }, { "HlsManifests":{ "AdMarkers":"NONE", "RepeatExtXKey":"False", "ManifestName":"index", "ProgramDateTimeIntervalSeconds":"0", "IncludeIframeOnlyStream":"False" } } ] } ] }`For more information, see [Viewing Packaging Configuration Details](https://docs.aws.amazon.com/mediapackage/latest/ug/pkg-cfig-view.html)in the*AWS Elemental MediaPackage User Guide*.- 
                    For API details, see [ListPackagingConfigurations](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/mediapackage-vod/list-packaging-configurations.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `list-packaging-groups`.

- **AWS CLI**
- 
            
                    **To list all packaging groups**The following `list-packaging-groups`example lists all of the packaging groups that are configured in the current AWS account.`aws mediapackage-vod list-packaging-groups`Output: `{ "PackagingGroups": [ { "Arn": "arn:aws:mediapackage-vod:us-west-2:111122223333:packaging-groups/Dash_widevine", "Id": "Dash_widevine" }, { "Arn": "arn:aws:mediapackage-vod:us-west-2:111122223333:packaging-groups/Encrypted_HLS", "Id": "Encrypted_HLS" }, { "Arn": "arn:aws:mediapackage-vod:us-west-2:111122223333:packaging-groups/Packaging_group_1", "Id": "Packaging_group_1" } ] }`For more information, see [Viewing Packaging Group Details](https://docs.aws.amazon.com/mediapackage/latest/ug/pkg-group-view.html)in the*AWS Elemental MediaPackage User Guide*.- 
                    For API details, see [ListPackagingGroups](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/mediapackage-vod/list-packaging-groups.html)in*AWS CLI Command Reference*.
 
-