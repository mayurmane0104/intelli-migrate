# MediaTailor examples using AWS CLI - AWS Command Line Interface

**Source:** [https://docs.aws.amazon.com/cli/latest/userguide/cli_mediatailor_code_examples.html](https://docs.aws.amazon.com/cli/latest/userguide/cli_mediatailor_code_examples.html)

---

The following code examples show you how to perform actions and implement common scenarios by using the AWS Command Line Interface with MediaTailor.

*Actions* are code excerpts from larger programs and must be run in context. While actions show you how to call individual service functions, you can see actions in context in their related scenarios.

Each example includes a link to the complete source code, where you can find instructions on how to set up and run the code in context.

###### Topics

## Actions

    The following code example shows how to use `delete-playback-configuration`.

- **AWS CLI**
- 
            
                    **To delete a configuration**The following `delete-playback-configuration`deletes a configuration named`campaign_short`.`aws mediatailor delete-playback-configuration \ --name``campaign_short`This command produces no output. For more information, see [Deleting a Configuration](https://docs.aws.amazon.com/mediatailor/latest/ug/configurations-delete.html)in the*AWS Elemental MediaTailor User Guide*.- 
                    For API details, see [DeletePlaybackConfiguration](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/mediatailor/delete-playback-configuration.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `get-playback-configuration`.

- **AWS CLI**
- 
            
                    **To describe a configuration**The following `get-playback-configuration`displays all of the details of the configuration named`west_campaign`.`aws mediatailor get-playback-configuration \ --name``west_campaign`Output: `{ "AdDecisionServerUrl": "http://your.ads.url", "CdnConfiguration": {}, "DashConfiguration": { "ManifestEndpointPrefix": "https://170c14299689462897d0cc45fc2000bb.mediatailor.us-west-2.amazonaws.com/v1/dash/1cbfeaaecb69778e0c167d0505a2bc57da2b1754/west_campaign/", "MpdLocation": "EMT_DEFAULT", "OriginManifestType": "MULTI_PERIOD" }, "HlsConfiguration": { "ManifestEndpointPrefix": "https://170c14299689462897d0cc45fc2000bb.mediatailor.us-west-2.amazonaws.com/v1/master/1cbfeaaecb69778e0c167d0505a2bc57da2b1754/west_campaign/" }, "Name": "west_campaign", "PlaybackConfigurationArn": "arn:aws:mediatailor:us-west-2:123456789012:playbackConfiguration/west_campaign", "PlaybackEndpointPrefix": "https://170c14299689462897d0cc45fc2000bb.mediatailor.us-west-2.amazonaws.com", "SessionInitializationEndpointPrefix": "https://170c14299689462897d0cc45fc2000bb.mediatailor.us-west-2.amazonaws.com/v1/session/1cbfeaaecb69778e0c167d0505a2bc57da2b1754/west_campaign/", "Tags": {}, "VideoContentSourceUrl": "https://8343f7014c0ea438.mediapackage.us-west-2.amazonaws.com/out/v1/683f0f2ff7cd43a48902e6dcd5e16dcf/index.m3u8" }`For more information, see [Viewing a Configuration](https://docs.aws.amazon.com/mediatailor/latest/ug/configurations-view.html)in the*AWS Elemental MediaTailor User Guide*.- 
                    For API details, see [GetPlaybackConfiguration](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/mediatailor/get-playback-configuration.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `list-playback-configurations`.

- **AWS CLI**
- 
            
                    **To list all configurations**The following `list-playback-configurations`displays all of the details of the configuration on the current AWS account.`aws mediatailor list-playback-configurations`Output: `{ "Items": [ { "AdDecisionServerUrl": "http://your.ads.url", "CdnConfiguration": {}, "DashConfiguration": { "ManifestEndpointPrefix": "https://170c14299689462897d0cc45fc2000bb.mediatailor.us-west-2.amazonaws.com/v1/dash/1cbfeaaecb69778e0c167d0505a2bc57da2b1754/west_campaign/", "MpdLocation": "EMT_DEFAULT", "OriginManifestType": "MULTI_PERIOD" }, "HlsConfiguration": { "ManifestEndpointPrefix": "https://170c14299689462897d0cc45fc2000bb.mediatailor.us-west-2.amazonaws.com/v1/master/1cbfeaaecb69778e0c167d0505a2bc57da2b1754/west_campaign/" }, "Name": "west_campaign", "PlaybackConfigurationArn": "arn:aws:mediatailor:us-west-2:123456789012:playbackConfiguration/west_campaign", "PlaybackEndpointPrefix": "https://170c14299689462897d0cc45fc2000bb.mediatailor.us-west-2.amazonaws.com", "SessionInitializationEndpointPrefix": "https://170c14299689462897d0cc45fc2000bb.mediatailor.us-west-2.amazonaws.com/v1/session/1cbfeaaecb69778e0c167d0505a2bc57da2b1754/west_campaign/", "Tags": {}, "VideoContentSourceUrl": "https://8343f7014c0ea438.mediapackage.us-west-2.amazonaws.com/out/v1/683f0f2ff7cd43a48902e6dcd5e16dcf/index.m3u8" }, { "AdDecisionServerUrl": "http://your.ads.url", "CdnConfiguration": {}, "DashConfiguration": { "ManifestEndpointPrefix": "https://73511f91d6a24ca2b93f3cf1d7cedd67.mediatailor.us-west-2.amazonaws.com/v1/dash/1cbfeaaecb69778e0c167d0505a2bc57da2b1754/sports_campaign/", "MpdLocation": "DISABLED", "OriginManifestType": "MULTI_PERIOD" }, "HlsConfiguration": { "ManifestEndpointPrefix": "https://73511f91d6a24ca2b93f3cf1d7cedd67.mediatailor.us-west-2.amazonaws.com/v1/master/1cbfeaaecb69778e0c167d0505a2bc57da2b1754/sports_campaign/" }, "Name": "sports_campaign", "PlaybackConfigurationArn": "arn:aws:mediatailor:us-west-2:123456789012:playbackConfiguration/sports_campaign", "PlaybackEndpointPrefix": "https://73511f91d6a24ca2b93f3cf1d7cedd67.mediatailor.us-west-2.amazonaws.com", "SessionInitializationEndpointPrefix": "https://73511f91d6a24ca2b93f3cf1d7cedd67.mediatailor.us-west-2.amazonaws.com/v1/session/1cbfeaaecb69778e0c167d0505a2bc57da2b1754/sports_campaign/", "SlateAdUrl": "http://s3.bucket/slate_ad.mp4", "Tags": {}, "VideoContentSourceUrl": "https://c4af3793bf76b33c.mediapackage.us-west-2.amazonaws.com/out/v1/1dc6718be36f4f34bb9cd86bc50925e6/sports_endpoint/index.m3u8" } ] }`For more information, see Viewing a Configuration<https://docs.aws.amazon.com/mediatailor/latest/ug/configurations-view.html> in the *AWS Elemental MediaTailor User Guide*.- 
                    For API details, see [ListPlaybackConfigurations](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/mediatailor/list-playback-configurations.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `put-playback-configuration`.

- **AWS CLI**
- 
            
                    **To create a configuration**The following `put-playback-configuration`creates a configuration named`campaign_short`.`aws mediatailor put-playback-configuration \ --name``campaign_short`\ --ad-decision-server-url`http://your.ads.url`\ --video-content-source-url`http://video.bucket/index.m3u8`Output: `{ "AdDecisionServerUrl": "http://your.ads.url", "CdnConfiguration": {}, "DashConfiguration": { "ManifestEndpointPrefix": "https://13484114d38f4383bc0d6a7cb879bd00.mediatailor.us-west-2.amazonaws.com/v1/dash/1cbfeaaecb69778e0c167d0505a2bc57da2b1754/campaign_short/", "MpdLocation": "EMT_DEFAULT", "OriginManifestType": "MULTI_PERIOD" }, "HlsConfiguration": { "ManifestEndpointPrefix": "https://13484114d38f4383bc0d6a7cb879bd00.mediatailor.us-west-2.amazonaws.com/v1/master/1cbfeaaecb69778e0c167d0505a2bc57da2b1754/campaign_short/" }, "Name": "campaign_short", "PlaybackConfigurationArn": "arn:aws:mediatailor:us-west-2:123456789012:playbackConfiguration/campaign_short", "PlaybackEndpointPrefix": "https://13484114d38f4383bc0d6a7cb879bd00.mediatailor.us-west-2.amazonaws.com", "SessionInitializationEndpointPrefix": "https://13484114d38f4383bc0d6a7cb879bd00.mediatailor.us-west-2.amazonaws.com/v1/session/1cbfeaaecb69778e0c167d0505a2bc57da2b1754/campaign_short/", "Tags": {}, "VideoContentSourceUrl": "http://video.bucket/index.m3u8" }`For more information, see [Creating a Configuration](https://docs.aws.amazon.com/mediatailor/latest/ug/configurations-create.html)in the*AWS Elemental MediaTailor User Guide*.- 
                    For API details, see [PutPlaybackConfiguration](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/mediatailor/put-playback-configuration.html)in*AWS CLI Command Reference*.
 
-