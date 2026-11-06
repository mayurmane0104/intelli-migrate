# Amazon IVS examples using AWS CLI - AWS Command Line Interface

**Source:** [https://docs.aws.amazon.com/cli/latest/userguide/cli_ivs_code_examples.html](https://docs.aws.amazon.com/cli/latest/userguide/cli_ivs_code_examples.html)

---

The following code examples show you how to perform actions and implement common scenarios by using the AWS Command Line Interface with Amazon IVS.

*Actions* are code excerpts from larger programs and must be run in context. While actions show you how to call individual service functions, you can see actions in context in their related scenarios.

Each example includes a link to the complete source code, where you can find instructions on how to set up and run the code in context.

###### Topics

## Actions

    The following code example shows how to use `batch-get-channel`.

- **AWS CLI**
- 
            
                    **To get channel configuration information about multiple channels**The following `batch-get-channel`example lists information about the specified channels.`aws ivs batch-get-channel \ --arns``arn:aws:ivs:us-west-2:123456789012:channel/abcdABCDefgh`\`arn:aws:ivs:us-west-2:123456789012:channel/efghEFGHijkl`Output: `{ "channels": [ { "arn": "arn:aws:ivs:us-west-2:123456789012:channel/abcdABCDefgh", "authorized": false, "containerFormat": "TS", "ingestEndpoint": "a1b2c3d4e5f6.global-contribute.live-video.net", "insecureIngest": false, "latencyMode": "LOW", "multitrackInputConfiguration": { "enabled": false, "maximumResolution": "FULL_HD", "policy": "ALLOW" }, "name": "channel-1", "playbackUrl": "https://a1b2c3d4e5f6.us-west-2.playback.live-video.net/api/video/v1/us-west-2.123456789012.channel-1.abcdEFGH.m3u8", "preset": "", "playbackRestrictionPolicyArn": "", "recordingConfigurationArn": "arn:aws:ivs:us-west-2:123456789012:recording-configuration/ABCD12cdEFgh", "srt": { "endpoint": "a1b2c3d4e5f6.srt.live-video.net", "passphrase": "AB1C2defGHijkLMNo3PqQRstUvwxyzaBCDEfghh4ijklMN5opqrStuVWxyzAbCDEfghIJ" }, "tags": {}, "type": "STANDARD" }, { "arn": "arn:aws:ivs:us-west-2:123456789012:channel/efghEFGHijkl", "authorized": false, "containerFormat": "FRAGMENTED_MP4", "ingestEndpoint": "a1b2c3d4e5f6.global-contribute.live-video.net", "insecureIngest": false, "latencyMode": "LOW", "multitrackInputConfiguration": { "enabled": true, "maximumResolution": "FULL_HD", "policy": "ALLOW" }, "name": "channel-2", "playbackUrl": "https://a1b2c3d4e5f6.us-west-2.playback.live-video.net/api/video/v1/us-west-2.123456789012.channel-2.abcdEFGH.m3u8", "preset": "", "playbackRestrictionPolicyArn": "arn:aws:ivs:us-west-2:123456789012:playback-restriction-policy/ABcdef34ghIJ"", "recordingConfigurationArn": "", "srt": { "endpoint": "a1b2c3d4e5f6.srt.live-video.net", "passphrase": "BA1C2defGHijkLMNo3PqQRstUvwxyzaBCDEfghh4ijklMN5opqrStuVWxyzAbCDEfghIJ" }, "tags": {}, "type": "STANDARD" } ] }`For more information, see [Create a Channel](https://docs.aws.amazon.com/ivs/latest/LowLatencyUserGuide/getting-started-create-channel.html)in the*IVS Low-Latency User Guide*.- 
                    For API details, see [BatchGetChannel](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ivs/batch-get-channel.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `batch-get-stream-key`.

- **AWS CLI**
- 
            
                    **To get information about multiple stream keys**The following `batch-get-stream-key`example gets information about the specified stream keys.`aws ivs batch-get-stream-key \ --arns``arn:aws:ivs:us-west-2:123456789012:stream-key/skSKABCDefgh`\`arn:aws:ivs:us-west-2:123456789012:stream-key/skSKIJKLmnop`Output: `{ "streamKeys": [ { "arn": "arn:aws:ivs:us-west-2:123456789012:stream-key/skSKABCDefgh", "value": "sk_us-west-2_abcdABCDefgh_567890abcdef", "channelArn": "arn:aws:ivs:us-west-2:123456789012:channel/abcdABCDefgh", "tags": {} }, { "arn": "arn:aws:ivs:us-west-2:123456789012:stream-key/skSKIJKLmnop", "value": "sk_us-west-2_abcdABCDefgh_567890ghijkl", "channelArn": "arn:aws:ivs:us-west-2:123456789012:channel/abcdABCDefgh", "tags": {} } ] }`For more information, see [Create a Channel](https://docs.aws.amazon.com/ivs/latest/LowLatencyUserGuide/getting-started-create-channel.html)in the*IVS Low-Latency User Guide*.- 
                    For API details, see [BatchGetStreamKey](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ivs/batch-get-stream-key.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `batch-start-viewer-session-revocation`.

- **AWS CLI**
- 
            
                    **To revoke viewer sessions for multiple channel-ARN and viewer-ID pairs**The following `batch-start-viewer-session-revocation`example performs session revocation on multiple channel-ARN and viewer-ID pairs simultaneously. The request may complete normally but return values in the errors field if the caller does not have permission to revoke specified session.`aws ivs batch-start-viewer-session-revocation \ --viewer-sessions '``[{"channelArn":"arn:aws:ivs:us-west-2:123456789012:channel/abcdABCDefgh1","viewerId":"abcdefg1","viewerSessionVersionsLessThanOrEqualTo":1234567890}, \ {"channelArn":"arn:aws:ivs:us-west-2:123456789012:channel/abcdABCDefgh2","viewerId":"abcdefg2","viewerSessionVersionsLessThanOrEqualTo":1234567890}]`'Output: `{ "errors": [ { "channelArn": "arn:aws:ivs:us-west-2:123456789012:channel/abcdABCDefgh1", "viewerId": "abcdefg1", "code": "403", "message": "not authorized", }, { "channelArn": "arn:aws:ivs:us-west-2:123456789012:channel/abcdABCDefgh2", "viewerId": "abcdefg2", "code": "403", "message": "not authorized", } ] }`For more information, see [Setting Up Private Channels](https://docs.aws.amazon.com/ivs/latest/userguide/private-channels.html)in the*Amazon Interactive Video Service User Guide*.- 
                    For API details, see [BatchStartViewerSessionRevocation](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ivs/batch-start-viewer-session-revocation.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `create-channel`.

- **AWS CLI**
- 
            
                    **Example 1: To create a channel with no recording**The following `create-channel`example creates a new channel and an associated stream key to start streaming.`aws ivs create-channel \ --name '``test-channel`' \ --no-insecure-ingestOutput: `{ "channel": { "arn": "arn:aws:ivs:us-west-2:123456789012:channel/abcdABCDefgh", "authorized": false, "containerFormat": "TS", "name": "test-channel", "latencyMode": "LOW", "multitrackInputConfiguration": { "enabled": false, "maximumResolution": "FULL_HD", "policy": "ALLOW" }, "playbackRestrictionPolicyArn": "", "recordingConfigurationArn": "", "srt": { "endpoint": "a1b2c3d4e5f6.srt.live-video.net", "passphrase": "AB1C2defGHijkLMNo3PqQRstUvwxyzaBCDEfghh4ijklMN5opqrStuVWxyzAbCDEfghIJ" }, "ingestEndpoint": "a1b2c3d4e5f6.global-contribute.live-video.net", "insecureIngest": false, "playbackUrl": "https://a1b2c3d4e5f6.us-west-2.playback.live-video.net/api/video/v1/us-west-2.123456789012.channel.abcdEFGH.m3u8", "preset": "", "tags": {}, "type": "STANDARD" }, "streamKey": { "arn": "arn:aws:ivs:us-west-2:123456789012:stream-key/g1H2I3j4k5L6", "value": "sk_us-west-2_abcdABCDefgh_567890abcdef", "channelArn": "arn:aws:ivs:us-west-2:123456789012:channel/abcdABCDefgh", "tags": {} } }`For more information, see [Create a Channel](https://docs.aws.amazon.com/ivs/latest/LowLatencyUserGuide/getting-started-create-channel.html)in the*IVS Low-Latency User Guide*.**Example 2: To create a channel with recording enabled, using the RecordingConfiguration resource specified by its ARN**The following `create-channel`example creates a new channel and an associated stream key to start streaming, and sets up recording for the channel:`aws ivs create-channel \ --name``test-channel-with-recording`\ --insecure-ingest \ --recording-configuration-arn '`arn:aws:ivs:us-west-2:123456789012:recording-configuration/ABCD12cdEFgh`'Output: `{ "channel": { "arn": "arn:aws:ivs:us-west-2:123456789012:channel/abcdABCDefgh", "containerFormat": "TS", "name": "test-channel-with-recording", "latencyMode": "LOW", "multitrackInputConfiguration": { "enabled": false, "maximumResolution": "FULL_HD", "policy": "ALLOW" }, "type": "STANDARD", "playbackRestrictionPolicyArn": "", "recordingConfigurationArn": "arn:aws:ivs:us-west-2:123456789012:recording-configuration/ABCD12cdEFgh", "srt": { "endpoint": "a1b2c3d4e5f6.srt.live-video.net", "passphrase": "BA1C2defGHijkLMNo3PqQRstUvwxyzaBCDEfghh4ijklMN5opqrStuVWxyzAbCDEfghIJ" }, "ingestEndpoint": "a1b2c3d4e5f6.global-contribute.live-video.net", "insecureIngest": true, "playbackUrl": "https://a1b2c3d4e5f6.us-west-2.playback.live-video.net/api/video/v1/us-west-2.123456789012.channel.abcdEFGH.m3u8", "preset": "", "authorized": false, "tags": {}, "type": "STANDARD" }, "streamKey": { "arn": "arn:aws:ivs:us-west-2:123456789012:stream-key/abcdABCDefgh", "value": "sk_us-west-2_abcdABCDefgh_567890abcdef", "channelArn": "arn:aws:ivs:us-west-2:123456789012:channel/abcdABCDefgh", "tags": {} } }`For more information, see [Record to Amazon S3](https://docs.aws.amazon.com/ivs/latest/LowLatencyUserGuide/record-to-s3.html)in the*IVS Low-Latency User Guide*.**Example 3: To create a channel with a playback restriction policy specified by its ARN**The following `create-channel`example creates a new channel and an associated stream key to start streaming, and sets up a playback restriction policy for the channel:`aws ivs create-channel \ --name``test-channel-with-playback-restriction-policy`\ --insecure-ingest \ --playback-restriction-policy-arn '`arn:aws:ivs:us-west-2:123456789012:playback-restriction-policy/ABcdef34ghIJ`'Output: `{ "channel": { "arn": "arn:aws:ivs:us-west-2:123456789012:channel/abcdABCDefgh", "containerFormat": "TS", "name": "test-channel-with-playback-restriction-policy", "latencyMode": "LOW", "multitrackInputConfiguration": { "enabled": false, "maximumResolution": "FULL_HD", "policy": "ALLOW" }, "type": "STANDARD", "playbackRestrictionPolicyArn": "arn:aws:ivs:us-west-2:123456789012:playback-restriction-policy/ABcdef34ghIJ", "recordingConfigurationArn": "", "srt": { "endpoint": "a1b2c3d4e5f6.srt.live-video.net", "passphrase": "AB1C2edfGHijkLMNo3PqQRstUvwxyzaBCDEfghh4ijklMN5opqrStuVWxyzAbCDEfghIJ" }, "ingestEndpoint": "a1b2c3d4e5f6.global-contribute.live-video.net", "insecureIngest": true, "playbackUrl": "https://a1b2c3d4e5f6.us-west-2.playback.live-video.net/api/video/v1/us-west-2.123456789012.channel.abcdEFGH.m3u8", "preset": "", "authorized": false, "tags": {}, "type": "STANDARD" }, "streamKey": { "arn": "arn:aws:ivs:us-west-2:123456789012:stream-key/abcdABCDefgh", "value": "sk_us-west-2_abcdABCDefgh_567890abcdef", "channelArn": "arn:aws:ivs:us-west-2:123456789012:channel/abcdABCDefgh", "tags": {} } }`For more information, see [Undesired Content and Viewers](https://docs.aws.amazon.com/ivs/latest/LowLatencyUserGuide/undesired-content.html)in the*IVS Low-Latency User Guide*.**Example 4: To create a channel with multitrack enabled**The following `create-channel`example creates a new channel and an associated stream key to start streaming, and enables multitrack.`aws ivs create-channel \ --name '``test-channel`' \ --no-insecure-ingest \ --container-format '`FRAGMENTED_MP4`' \ --multitrack-input-configuration '`{"enabled": true,"maximumResolution": "FULL_HD","policy": "ALLOW"}`'Output: `{ "channel": { "arn": "arn:aws:ivs:us-west-2:123456789012:channel/abcdABCDefgh", "authorized": false, "containerFormat": "FRAGMENTED_MP4", "name": "test-channel", "latencyMode": "LOW", "multitrackInputConfiguration": { "enabled": true, "maximumResolution": "FULL_HD", "policy": "ALLOW" }, "playbackRestrictionPolicyArn": "", "recordingConfigurationArn": "", "srt": { "endpoint": "a1b2c3d4e5f6.srt.live-video.net", "passphrase": "AB1C2defGHijkLMNo3PqQRstUvwxyzaBCDEfghh4ijklMN5opqrStuVWxyzAbCDEfghIJ" }, "ingestEndpoint": "a1b2c3d4e5f6.global-contribute.live-video.net", "insecureIngest": false, "playbackUrl": "https://a1b2c3d4e5f6.us-west-2.playback.live-video.net/api/video/v1/us-west-2.123456789012.channel.abcdEFGH.m3u8", "preset": "", "tags": {}, "type": "STANDARD" }, "streamKey": { "arn": "arn:aws:ivs:us-west-2:123456789012:stream-key/g1H2I3j4k5L6", "value": "sk_us-west-2_abcdABCDefgh_567890abcdef", "channelArn": "arn:aws:ivs:us-west-2:123456789012:channel/abcdABCDefgh", "tags": {} } }`For more information, see [Create a Channel](https://docs.aws.amazon.com/ivs/latest/LowLatencyUserGuide/multitrack-video.html)in the*IVS Low-Latency User Guide*.- 
                    For API details, see [CreateChannel](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ivs/create-channel.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `create-playback-restriction-policy`.

- **AWS CLI**
- 
            
                    **To create a playback restriction policy**The following `create-playback-restriction-policy`example creates a new playback resriction policy.`aws ivs create-playback-restriction-policy \ --name``"test-playback-restriction-policy"`\ --enable-strict-origin-enforcement \ --tags`"key1=value1, key2=value2"`\ --allowed-countries`US``MX`\ --allowed-origins`https://www.website1.com``https://www.website2.com`Output: `{ "playbackRestrictionPolicy": { "arn": "arn:aws:ivs:us-west-2:123456789012:playback-restriction-policy/ABcdef34ghIJ", "allowedCountries": [ "US", "MX" ], "allowedOrigins": [ "https://www.website1.com", "https://www.website2.com" ], "enableStrictOriginEnforcement": true, "name": "test-playback-restriction-policy", "tags": { "key1": "value1", "key2": "value2" } } }`For more information, see [Undesired Content and Viewers](https://docs.aws.amazon.com/ivs/latest/LowLatencyUserGuide/undesired-content.html)in the*IVS Low-Latency User Guide*.- 
                    For API details, see [CreatePlaybackRestrictionPolicy](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ivs/create-playback-restriction-policy.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `create-recording-configuration`.

- **AWS CLI**
- 
            
                    **To create a RecordingConfiguration resource**The following `create-recording-configuration`example creates a RecordingConfiguration resource to enable recording to Amazon S3.`aws ivs create-recording-configuration \ --name``"test-recording-config"`\ --recording-reconnect-window-seconds`60`\ --tags`"key1=value1, key2=value2"`\ --rendition-configuration renditionSelection="CUSTOM",renditions="HD" \ --thumbnail-configuration recordingMode="INTERVAL",targetIntervalSeconds=1,storage="LATEST",resolution="LOWEST_RESOLUTION" \ --destination-configuration`s3={bucketName=demo-recording-bucket}`Output: `{ "recordingConfiguration": { "arn": "arn:aws:ivs:us-west-2:123456789012:recording-configuration/ABcdef34ghIJ", "name": "test-recording-config", "destinationConfiguration": { "s3": { "bucketName": "demo-recording-bucket" } }, "state": "CREATING", "tags": { "key1": "value1", "key2": "value2" }, "thumbnailConfiguration": { "recordingMode": "INTERVAL", "targetIntervalSeconds": 1, "resolution": "LOWEST_RESOLUTION", "storage": [ "LATEST" ] }, "recordingReconnectWindowSeconds": 60, "renditionConfiguration": { "renditionSelection": "CUSTOM", "renditions": [ "HD" ] } } }`For more information, see [Record to Amazon S3](https://docs.aws.amazon.com/ivs/latest/userguide/record-to-s3.html)in the*Amazon Interactive Video Service User Guide*.- 
                    For API details, see [CreateRecordingConfiguration](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ivs/create-recording-configuration.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `create-stream-key`.

- **AWS CLI**
- 
            
                    **To create a stream key**The following `create-stream-key`example creates a stream key for a specified ARN (Amazon Resource Name).`aws ivs create-stream-key \ --channel-arn``arn:aws:ivs:us-west-2:123456789012:channel/abcdABCDefgh`Output: `{ "streamKey": { "arn": "arn:aws:ivs:us-west-2:123456789012:stream-key/abcdABCDefgh", "value": "sk_us-west-2_abcdABCDefgh_567890abcdef", "channelArn": "arn:aws:ivs:us-west-2:123456789012:channel/abcdABCDefgh", "tags": {} } }`For more information, see [Create a Channel](https://docs.aws.amazon.com/ivs/latest/LowLatencyUserGuide/getting-started-create-channel.html)in the*IVS Low-Latency User Guide*.- 
                    For API details, see [CreateStreamKey](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ivs/create-stream-key.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `delete-channel`.

- **AWS CLI**
- 
            
                    **To delete a channel and its associated stream keys**The following `delete-channel`example deletes the channel with the specified ARN (Amazon Resource Name).`aws ivs delete-channel \ --arn``arn:aws:ivs:us-west-2:123456789012:channel/abcdABCDefgh`This command produces no output. For more information, see [Create a Channel](https://docs.aws.amazon.com/ivs/latest/LowLatencyUserGuide/getting-started-create-channel.html)in the*IVS Low-Latency User Guide*.- 
                    For API details, see [DeleteChannel](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ivs/delete-channel.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `delete-playback-key-pair`.

- **AWS CLI**
- 
            
                    **To delete a specified playback key pair**The following `delete-playback-key-pair`example returns the fingerprint of the specified key pair.`aws ivs delete-playback-key-pair \ --arn``arn:aws:ivs:us-west-2:123456789012:playback-key/abcd1234efgh`This command produces no output. For more information, see [Setting Up Private Channels](https://docs.aws.amazon.com/ivs/latest/userguide/private-channels.html)in the*Amazon Interactive Video Service User Guide*.- 
                    For API details, see [DeletePlaybackKeyPair](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ivs/delete-playback-key-pair.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `delete-playback-restriction-policy`.

- **AWS CLI**
- 
            
                    **To delete a playback restriction policy**The following `delete-playback-restriction-policy`example deletes the playback resriction policy with the specified policy ARN (Amazon Resource Name).`aws ivs delete-playback-restriction-policy \ --arn``"arn:aws:ivs:us-west-2:123456789012:playback-restriction-policy/ABcdef34ghIJ"`This command produces no output. For more information, see [Undesired Content and Viewers](https://docs.aws.amazon.com/ivs/latest/LowLatencyUserGuide/undesired-content.html)in the*IVS Low-Latency User Guide*.- 
                    For API details, see [DeletePlaybackRestrictionPolicy](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ivs/delete-playback-restriction-policy.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `delete-recording-configuration`.

- **AWS CLI**
- 
            
                    **To delete the RecordingConfiguration resource specified by its ARN**The following `delete-recording-configuration`example deletes the RecordingConfiguration resource with the specified ARN.`aws ivs delete-recording-configuration \ --arn``"arn:aws:ivs:us-west-2:123456789012:recording-configuration/ABcdef34ghIJ"`This command produces no output. For more information, see [Record to Amazon S3](https://docs.aws.amazon.com/ivs/latest/userguide/record-to-s3.html)in the*Amazon Interactive Video Service User Guide*.- 
                    For API details, see [DeleteRecordingConfiguration](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ivs/delete-recording-configuration.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `delete-stream-key`.

- **AWS CLI**
- 
            
                    **To delete a stream key**The following `delete-stream-key`example deletes the stream key for a specified ARN (Amazon Resource Name), so it can no longer be used to stream.`aws ivs delete-stream-key \ --arn``arn:aws:ivs:us-west-2:123456789012:stream-key/g1H2I3j4k5L6`This command produces no output. For more information, see [Create a Channel](https://docs.aws.amazon.com/ivs/latest/LowLatencyUserGuide/getting-started-create-channel.html)in the*IVS Low-Latency User Guide*.- 
                    For API details, see [DeleteStreamKey](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ivs/delete-stream-key.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `get-channel`.

- **AWS CLI**
- 
            
                    **To get a channel's configuration information**The following `get-channel`example gets the channel configuration for a specified channel ARN (Amazon Resource Name).`aws ivs get-channel \ --arn '``arn:aws:ivs:us-west-2:123456789012:channel/abcdABCDefgh`'Output: `{ "channel": { "arn": "arn:aws:ivs:us-west-2:123456789012:channel/abcdABCDefgh", "authorized": false, "containerFormat": "TS", "ingestEndpoint": "a1b2c3d4e5f6.global-contribute.live-video.net", "insecureIngest": false, "latencyMode": "LOW", "multitrackInputConfiguration": { "enabled": false, "maximumResolution": "FULL_HD", "policy": "ALLOW" }, "name": "channel-1", "playbackRestrictionPolicyArn": "", "playbackUrl": "https://a1b2c3d4e5f6.us-west-2.playback.live-video.net/api/video/v1/us-west-2.123456789012.channel.abcdEFGH.m3u8", "preset": "", "recordingConfigurationArn": "", "srt": { "endpoint": "a1b2c3d4e5f6.srt.live-video.net", "passphrase": "AB1C2defGHijkLMNo3PqQRstUvwxyzaBCDEfghh4ijklMN5opqrStuVWxyzAbCDEfghIJ" }, "tags": {} "type": "STANDARD", } }`For more information, see [Create a Channel](https://docs.aws.amazon.com/ivs/latest/LowLatencyUserGuide/getting-started-create-channel.html)in the*IVS Low-Latency User Guide*.- 
                    For API details, see [GetChannel](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ivs/get-channel.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `get-playback-key-pair`.

- **AWS CLI**
- 
            
                    **To get a specified playback key pair**The following `get-playback-key-pair`example returns the fingerprint of the specified key pair.`aws ivs get-playback-key-pair \ --arn``arn:aws:ivs:us-west-2:123456789012:playback-key/abcd1234efgh`Output: `{ "keyPair": { "arn": "arn:aws:ivs:us-west-2:123456789012:playback-key/abcd1234efgh", "name": "my-playback-key", "fingerprint": "0a:1b:2c:ab:cd:ef:34:56:70:b1:b2:71:01:2a:a3:72", "tags": {} } }`For more information, see [Setting Up Private Channels](https://docs.aws.amazon.com/ivs/latest/userguide//private-channels.html)in the*Amazon Interactive Video Service User Guide*.- 
                    For API details, see [GetPlaybackKeyPair](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ivs/get-playback-key-pair.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `get-playback-restriction-policy`.

- **AWS CLI**
- 
            
                    **To get a playback restriction policy's configuration information**The following `get-playback-restriction-policy`example gets the playback restriciton policy configuration with the specified policy ARN (Amazon Resource Name).`aws ivs get-playback-restriction-policy \ --arn``"arn:aws:ivs:us-west-2:123456789012:playback-restriction-policy/ABcdef34ghIJ"`Output: `{ "playbackRestrictionPolicy": { "arn": "arn:aws:ivs:us-west-2:123456789012:playback-restriction-policy/ABcdef34ghIJ", "allowedCountries": [ "US", "MX" ], "allowedOrigins": [ "https://www.website1.com", "https://www.website2.com" ], "enableStrictOriginEnforcement": true, "name": "test-playback-restriction-policy", "tags": { "key1": "value1", "key2": "value2" } } }`For more information, see [Undesired Content and Viewers](https://docs.aws.amazon.com/ivs/latest/LowLatencyUserGuide/undesired-content.html)in the*IVS Low-Latency User Guide*.- 
                    For API details, see [GetPlaybackRestrictionPolicy](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ivs/get-playback-restriction-policy.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `get-recording-configuration`.

- **AWS CLI**
- 
            
                    **To get information about a RecordingConfiguration resource**The following `get-recording-configuration`example gets information about the RecordingConfiguration resource for the specified ARN.`aws ivs get-recording-configuration \ --arn``"arn:aws:ivs:us-west-2:123456789012:recording-configuration/ABcdef34ghIJ"`Output: `{ "recordingConfiguration": { "arn": "arn:aws:ivs:us-west-2:123456789012:recording-configuration/ABcdef34ghIJ", "destinationConfiguration": { "s3": { "bucketName": "demo-recording-bucket" } }, "name": "test-recording-config", "recordingReconnectWindowSeconds": 60, "state": "ACTIVE", "tags": { "key1" : "value1", "key2" : "value2" }, "thumbnailConfiguration": { "recordingMode": "INTERVAL", "targetIntervalSeconds": 1, "resolution": "LOWEST_RESOLUTION", "storage": [ "LATEST" ] }, "renditionConfiguration": { "renditionSelection": "CUSTOM", "renditions": [ "HD" ] } } }`For more information, see [Record to Amazon S3](https://docs.aws.amazon.com/ivs/latest/userguide/record-to-s3.html)in the*Amazon Interactive Video Service User Guide*.- 
                    For API details, see [GetRecordingConfiguration](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ivs/get-recording-configuration.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `get-stream-key`.

- **AWS CLI**
- 
            
                    **To get information about a stream**The following `get-stream-key`example gets information about the specified stream key.`aws ivs get-stream-key \ --arn``arn:aws:ivs:us-west-2:123456789012:stream-key/skSKABCDefgh`--region=us-west-2Output: `{ "streamKey": { "arn": "arn:aws:ivs:us-west-2:123456789012:stream-key/skSKABCDefgh", "value": "sk_us-west-2_abcdABCDefgh_567890abcdef", "channelArn": "arn:aws:ivs:us-west-2:123456789012:channel/abcdABCDefgh", "tags": {} } }`For more information, see [Create a Channel](https://docs.aws.amazon.com/ivs/latest/LowLatencyUserGuide/getting-started-create-channel.html)in the*IVS Low-Latency User Guide*.- 
                    For API details, see [GetStreamKey](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ivs/get-stream-key.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `get-stream-session`.

- **AWS CLI**
- 
            
                    **To get metadata for a specified stream**The following `get-stream-session`example gets the metadata configuration for the specified channel ARN (Amazon Resource Name) and the specified stream; if`streamId`is not provided, the most recent stream for the channel is selected.`aws ivs get-stream-session \ --channel-arn '``arn:aws:ivs:us-west-2:123456789012:channel/abcdABCDefgh`' \ --stream-id '`mystream`'Output: `{ "streamSession": { "streamId": "mystream1", "startTime": "2023-06-26T19:09:28+00:00", "channel": { "arn": "arn:aws:ivs:us-west-2:123456789012:channel/abcdABCDefgh", "name": "mychannel", "latencyMode": "LOW", "type": "STANDARD", "recordingConfigurationArn": "arn:aws:ivs:us-west-2:123456789012:recording-configuration/ABcdef34ghIJ", "ingestEndpoint": "a1b2c3d4e5f6.global-contribute.live-video.net", "playbackUrl": "url-string", "authorized": false, "insecureIngest": false, "preset": "" }, "ingestConfiguration": { "audio": { "channels": 2, "codec": "mp4a.40.2", "sampleRate": 8000, "targetBitrate": 46875, "track": "Track0" }, "video": { "avcProfile": "Baseline", "avcLevel": "4.2", "codec": "avc1.42C02A", "encoder": "Lavf58.45.100", "level": "4.2", "profile": "Baseline", "targetBitrate": 8789062, "targetFramerate": 60, "track": "Track0", "videoHeight": 1080, "videoWidth": 1920 } }, "ingestConfigurations": { "audioConfigurations": [ { "channels": 2, "codec": "mp4a.40.2", "sampleRate": 8000, "targetBitrate": 46875, "track": "Track0" } ], "videoConfigurations": [ { "codec": "avc1.42C02A", "encoder": "Lavf58.45.100", "level": "4.2", "profile": "Baseline", "targetBitrate": 8789062, "targetFramerate": 60, "track": "Track0", "videoHeight": 1080, "videoWidth": 1920 } ] }, "recordingConfiguration": { "arn": "arn:aws:ivs:us-west-2:123456789012:recording-configuration/ABcdef34ghIJ", "name": "test-recording-config", "destinationConfiguration": { "s3": { "bucketName": "demo-recording-bucket" } }, "state": "ACTIVE", "tags": { "key1": "value1", "key2": "value2" }, "thumbnailConfiguration": { "recordingMode": "INTERVAL", "targetIntervalSeconds": 1, "resolution": "LOWEST_RESOLUTION", "storage": [ "LATEST" ] }, "recordingReconnectWindowSeconds": 60, "renditionConfiguration": { "renditionSelection": "CUSTOM", "renditions": [ "HD" ] } }, "truncatedEvents": [ { "code": "StreamTakeoverInvalidPriority", "name": "Stream Takeover Failure", "type": "IVS Stream State Change", "eventTime": "2023-06-26T19:09:48+00:00" }, { "name": "Stream Takeover", "type": "IVS Stream State Change", "eventTime": "2023-06-26T19:09:47+00:00" }, { "name": "Recording Start", "type": "IVS Recording State Change", "eventTime": "2023-06-26T19:09:35+00:00" }, { "name": "Stream Start", "type": "IVS Stream State Change", "eventTime": "2023-06-26T19:09:34+00:00" }, { "name": "Session Created", "type": "IVS Stream State Change", "eventTime": "2023-06-26T19:09:28+00:00" } ] } }`For more information, see [Create a Channel](https://docs.aws.amazon.com/ivs/latest/LowLatencyUserGuide/getting-started-create-channel.html)in the*IVS Low-Latency User Guide*.- 
                    For API details, see [GetStreamSession](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ivs/get-stream-session.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `get-stream`.

- **AWS CLI**
- 
            
                    **To get information about a stream**The following `get-stream`example gets information about the stream for the specified channel.`aws ivs get-stream \ --channel-arn``arn:aws:ivs:us-west-2:123456789012:channel/abcdABCDefgh`Output: `{ "stream": { "channelArn": "arn:aws:ivs:us-west-2:123456789012:channel/abcdABCDefgh", "playbackUrl": "https://a1b2c3d4e5f6.us-west-2.playback.live-video.net/api/video/v1/us-west-2.123456789012.channel.abcdEFGH.m3u8", "startTime": "2020-05-05T21:55:38Z", "state": "LIVE", "health": "HEALTHY", "streamId": "st-ABCDEfghij01234KLMN5678", "viewerCount": 1 } }`For more information, see [Create a Channel](https://docs.aws.amazon.com/ivs/latest/LowLatencyUserGuide/getting-started-create-channel.html)in the*IVS Low-Latency User Guide*.- 
                    For API details, see [GetStream](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ivs/get-stream.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `import-playback-key-pair`.

- **AWS CLI**
- 
            
                    **To import the public portion of a new key pair**The following `import-playback-key-pair`example imports the specified public key (specified as a string in PEM format) and returns the arn and fingerprint of the new key pair.`aws ivs import-playback-key-pair \ --name``"my-playback-key"`\ --public-key-material`"G1lbnQxOTA3BgNVBAMMMFdoeSBhcmUgeW91IGRl..."`Output: `{ "keyPair": { "arn": "arn:aws:ivs:us-west-2:123456789012:playback-key/abcd1234efgh", "name": "my-playback-key", "fingerprint": "0a:1b:2c:ab:cd:ef:34:56:70:b1:b2:71:01:2a:a3:72", "tags": {} } }`For more information, see [Setting Up Private Channels](https://docs.aws.amazon.com/ivs/latest/userguide//private-channels.html)in the*Amazon Interactive Video Service User Guide*.- 
                    For API details, see [ImportPlaybackKeyPair](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ivs/import-playback-key-pair.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `list-channels`.

- **AWS CLI**
- 
            
                    **Example 1: To get summary information about all channels**The following `list-channels`example lists all channels for your AWS account.`aws ivs list-channels`Output: `{ "channels": [ { "arn": "arn:aws:ivs:us-west-2:123456789012:channel/abcdABCDefgh", "name": "channel-1", "latencyMode": "LOW", "authorized": false, "insecureIngest": false, "preset": "", "playbackRestrictionPolicyArn": "", "recordingConfigurationArn": "arn:aws:ivs:us-west-2:123456789012:recording-configuration/ABCD12cdEFgh", "tags": {}, "type": "STANDARD" }, { "arn": "arn:aws:ivs:us-west-2:123456789012:channel/efghEFGHijkl", "name": "channel-2", "latencyMode": "LOW", "authorized": false, "preset": "", "playbackRestrictionPolicyArn": "arn:aws:ivs:us-west-2:123456789012:playback-restriction-policy/ABcdef34ghIJ", "recordingConfigurationArn": "", "tags": {}, "type": "STANDARD" } ] }`For more information, see [Create a Channel](https://docs.aws.amazon.com/ivs/latest/LowLatencyUserGuide/getting-started-create-channel.html)in the*IVS Low-Latency User Guide*.**Example 2: To get summary information about all channels, filtered by the specified RecordingConfiguration ARN**The following `list-channels`example lists all channels for your AWS account, that are associated with the specified RecordingConfiguration ARN.`aws ivs list-channels \ --filter-by-recording-configuration-arn``"arn:aws:ivs:us-west-2:123456789012:recording-configuration/ABCD12cdEFgh"`Output: `{ "channels": [ { "arn": "arn:aws:ivs:us-west-2:123456789012:channel/abcdABCDefgh", "name": "channel-1", "latencyMode": "LOW", "authorized": false, "insecureIngest": false, "preset": "", "playbackRestrictionPolicyArn": "", "recordingConfigurationArn": "arn:aws:ivs:us-west-2:123456789012:recording-configuration/ABCD12cdEFgh", "tags": {}, "type": "STANDARD" } ] }`For more information, see [Record to Amazon S3](https://docs.aws.amazon.com/ivs/latest/LowLatencyUserGuide/record-to-s3.html)in the*IVS Low-Latency User Guide*.**Example 3: To get summary information about all channels, filtered by the specified PlaybackRestrictionPolicy ARN**The following `list-channels`example lists all channels for your AWS account, that are associated with the specified PlaybackRestrictionPolicy ARN.`aws ivs list-channels \ --filter-by-playback-restriction-policy-arn``"arn:aws:ivs:us-west-2:123456789012:playback-restriction-policy/ABcdef34ghIJ"`Output: `{ "channels": [ { "arn": "arn:aws:ivs:us-west-2:123456789012:channel/efghEFGHijkl", "name": "channel-2", "latencyMode": "LOW", "authorized": false, "preset": "", "playbackRestrictionPolicyArn": "arn:aws:ivs:us-west-2:123456789012:playback-restriction-policy/ABcdef34ghIJ", "recordingConfigurationArn": "", "tags": {}, "type": "STANDARD" } ] }`For more information, see [Undesired Content and Viewers](https://docs.aws.amazon.com/ivs/latest/LowLatencyUserGuide/undesired-content.html)in the*IVS Low-Latency User Guide*.- 
                    For API details, see [ListChannels](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ivs/list-channels.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `list-playback-key-pairs`.

- **AWS CLI**
- 
            
                    **To get summary information about all playback key pairs**The following `list-playback-key-pairs`example returns information about all key pairs.`aws ivs list-playback-key-pairs`Output: `{ "keyPairs": [ { "arn": "arn:aws:ivs:us-west-2:123456789012:playback-key/abcd1234efgh", "name": "test-key-0", "tags": {} }, { "arn": "arn:aws:ivs:us-west-2:123456789012:playback-key/ijkl5678mnop", "name": "test-key-1", "tags": {} } ] }`For more information, see [Setting Up Private Channels](https://docs.aws.amazon.com/ivs/latest/userguide//private-channels.html)in the*Amazon Interactive Video Service User Guide*.- 
                    For API details, see [ListPlaybackKeyPairs](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ivs/list-playback-key-pairs.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `list-playback-restriction-policies`.

- **AWS CLI**
- 
            
                    **To get summary information about all playback restriction policies**The following `list-playback-restriction-policies`example lists all playback restriction policies for your AWS account.`aws ivs list-playback-restriction-policies`Output: `{ "playbackRestrictionPolicies": [ { "arn": "arn:aws:ivs:us-west-2:123456789012:playback-restriction-policy/ABcdef34ghIJ", "allowedCountries": [ "US", "MX" ], "allowedOrigins": [ "https://www.website1.com", "https://www.website2.com" ], "enableStrictOriginEnforcement": true, "name": "test-playback-restriction-policy", "tags": { "key1": "value1", "key2": "value2" } } ] }`For more information, see [Undesired Content and Viewers](https://docs.aws.amazon.com/ivs/latest/LowLatencyUserGuide/undesired-content.html)in the*IVS Low-Latency User Guide*.- 
                    For API details, see [ListPlaybackRestrictionPolicies](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ivs/list-playback-restriction-policies.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `list-recording-configurations`.

- **AWS CLI**
- 
            
                    **To list all the RecordingConfiguration resources created in this account**The following `list-recording-configurations`example gets information about all RecordingConfiguration resources in your account.`aws ivs list-recording-configurations`Output: `{ "recordingConfigurations": [ { "arn": "arn:aws:ivs:us-west-2:123456789012:recording-configuration/ABcdef34ghIJ", "name": "test-recording-config-1", "destinationConfiguration": { "s3": { "bucketName": "demo-recording-bucket-1" } }, "state": "ACTIVE", "tags": {} }, { "arn": "arn:aws:ivs:us-west-2:123456789012:recording-configuration/CD12abcdGHIJ", "name": "test-recording-config-2", "destinationConfiguration": { "s3": { "bucketName": "demo-recording-bucket-2" } }, "state": "ACTIVE", "tags": {} } ] }`For more information, see [Record to Amazon S3](https://docs.aws.amazon.com/ivs/latest/userguide/record-to-s3.html)in the*Amazon Interactive Video Service User Guide*.- 
                    For API details, see [ListRecordingConfigurations](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ivs/list-recording-configurations.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `list-stream-keys`.

- **AWS CLI**
- 
            
                    **To get a list of stream keys**The following `list-stream-keys`example lists all stream keys for a specified ARN (Amazon Resource Name).`aws ivs list-stream-keys \ --channel-arn``arn:aws:ivs:us-west-2:123456789012:channel/abcdABCDefgh`Output: `{ "streamKeys": [ { "arn": "arn:aws:ivs:us-west-2:123456789012:stream-key/abcdABCDefgh", "channelArn": "arn:aws:ivs:us-west-2:123456789012:channel/abcdABCDefgh", "tags": {} } ] }`FFor more information, see [Create a Channel](https://docs.aws.amazon.com/ivs/latest/LowLatencyUserGuide/getting-started-create-channel.html)in the*IVS Low-Latency User Guide*.- 
                    For API details, see [ListStreamKeys](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ivs/list-stream-keys.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `list-stream-sessions`.

- **AWS CLI**
- 
            
                    **To get a summary of current and previous streams for a specified channel in the current AWS region**The following `list-stream-sessions`example reports summary information for streams for a specified channel ARN (Amazon Resource Name).`aws ivs list-stream-sessions \ --channel-arn``arn:aws:ivs:us-west-2:123456789012:channel/abcdABCDefgh`\ --max-results`25`\ --next-token ""Output: `{ "nextToken": "set-2", "streamSessions": [ { "startTime": 1641578182, "endTime": 1641579982, "hasErrorEvent": false, "streamId": "mystream" } ... ] }`For more information, see [Create a Channel](https://docs.aws.amazon.com/ivs/latest/LowLatencyUserGuide/getting-started-create-channel.html)in the*IVS Low-Latency User Guide*.- 
                    For API details, see [ListStreamSessions](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ivs/list-stream-sessions.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `list-streams`.

- **AWS CLI**
- 
            
                    **To get a list of live streams and their state**The following `list-streams`example lists all live streams for your AWS account.`aws ivs list-streams`Output: `{ "streams": [ { "channelArn": "arn:aws:ivs:us-west-2:123456789012:channel/abcdABCDefgh", "state": "LIVE", "health": "HEALTHY", "streamId": "st-ABCDEfghij01234KLMN5678", "viewerCount": 1 } ] }`For more information, see [Create a Channel](https://docs.aws.amazon.com/ivs/latest/LowLatencyUserGuide/getting-started-create-channel.html)in the*IVS Low-Latency User Guide*.- 
                    For API details, see [ListStreams](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ivs/list-streams.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `list-tags-for-resource`.

- **AWS CLI**
- 
            
                    **To list all tags for an AWS resource (for example: channel, stream key)**The following `list-tags-for-resource`example lists all tags for a specified resource ARN (Amazon Resource Name).`aws ivs list-tags-for-resource \ --resource-arn``arn:aws:ivs:us-west-2:12345689012:channel/abcdABCDefgh`Output: `{ "tags": { "key1": "value1", "key2": "value2" } }`For more information, see [Tagging](https://docs.aws.amazon.com/ivs/latest/APIReference/Welcome.html)in the*Amazon Interactive Video Service API Reference*.- 
                    For API details, see [ListTagsForResource](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ivs/list-tags-for-resource.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `put-metadata`.

- **AWS CLI**
- 
            
                    **To insert metadata into the active stream for a specified channel**The following `put-metadata`example inserts the given metadata into the stream for the specified channel.`aws ivs put-metadata \ --channel-arn``arn:aws:ivs:us-west-2:123456789012:channel/abcdABCDefgh`\ --metadata '`{"my": "metadata"}`'This command produces no output. For more information, see [Create a Channel](https://docs.aws.amazon.com/ivs/latest/LowLatencyUserGuide/getting-started-create-channel.html)in the*IVS Low-Latency User Guide*.- 
                    For API details, see [PutMetadata](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ivs/put-metadata.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `start-viewer-session-revocation`.

- **AWS CLI**
- 
            
                    **To revoke a viewer session for a given multiple channel-ARN and viewer-ID pair**The following `start-viewer-session-revocation`example starts the process of revoking the viewer session associated with a specified channel ARN and viewer ID, up to and including the specified session version number. If the version is not provided, it defaults to 0.`aws ivs start-viewer-session-revocation \ --channel-arn``arn:aws:ivs:us-west-2:123456789012:channel/abcdABCDefgh`\ --viewer-id`abcdefg`\ --viewer-session-versions-less-than-or-equal-to`1234567890`This command produces no output. For more information, see [Setting Up Private Channels](https://docs.aws.amazon.com/ivs/latest/userguide/private-channels.html)in the*Amazon Interactive Video Service User Guide*.- 
                    For API details, see [StartViewerSessionRevocation](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ivs/start-viewer-session-revocation.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `stop-stream`.

- **AWS CLI**
- 
            
                    **To stop a specified stream**The following `stop-stream`example stops the stream on the specified channel.`aws ivs stop-stream \ --channel-arn``arn:aws:ivs:us-west-2:123456789012:channel/abcdABCDefgh`This command produces no output. For more information, see [Create a Channel](https://docs.aws.amazon.com/ivs/latest/LowLatencyUserGuide/getting-started-create-channel.html)in the*IVS Low-Latency User Guide*.- 
                    For API details, see [StopStream](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ivs/stop-stream.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `tag-resource`.

- **AWS CLI**
- 
            
                    **To add or update tags for an AWS resource (for example: channel, stream key)**The following `tag-resource`example adds or updates tags for a specified resource ARN (Amazon Resource Name).`aws ivs tag-resource \ --resource-arn``arn:aws:ivs:us-west-2:123456789012:channel/abcdABCDefgh`\ --tags`"tagkey1=tagvalue1, tagkey2=tagvalue2"`This command produces no output. For more information, see [Tagging](https://docs.aws.amazon.com/ivs/latest/APIReference/Welcome.html)in the*Amazon Interactive Video Service API Reference*.- 
                    For API details, see [TagResource](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ivs/tag-resource.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `untag-resource`.

- **AWS CLI**
- 
            
                    **To remove tags for an AWS resource (for example: channel, stream key)**The following `untag-resource`example removes the specified tags for a specified resource ARN (Amazon Resource Name).`aws ivs untag-resource \ --resource-arn``arn:aws:ivs:us-west-2:123456789012:channel/abcdABCDefgh`\ --tag-keys`"tagkey1, tagkey2"`This command produces no output. For more information, see [Tagging](https://docs.aws.amazon.com/ivs/latest/APIReference/Welcome.html)in the*Amazon Interactive Video Service API Reference*.- 
                    For API details, see [UntagResource](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ivs/untag-resource.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `update-channel`.

- **AWS CLI**
- 
            
                    **Example 1: To update a channel's configuration information**The following `update-channel`example updates the channel configuration for a specified channel ARN to change the channel name. This does not affect an ongoing stream of this channel; you must stop and restart the stream for the changes to take effect.`aws ivs update-channel \ --arn '``arn:aws:ivs:us-west-2:123456789012:channel/abcdABCDefgh`' \ --name '`channel-1`' \ --insecure-ingestOutput: `{ "channel": { "arn": "arn:aws:ivs:us-west-2:123456789012:channel/abcdABCDefgh", "name": "channel-1", "latencyMode": "LOW", "containerFormat": "TS", "multitrackInputConfiguration": { "enabled": false, "maximumResolution": "FULL_HD", "policy": "ALLOW" }, "type": "STANDARD", "playbackRestrictionPolicyArn": "", "recordingConfigurationArn": "", "srt": { "endpoint": "a1b2c3d4e5f6.srt.live-video.net", "passphrase": "AB1C2defGHijkLMNo3PqQRstUvwxyzaBCDEfghh4ijklMN5opqrStuVWxyzAbCDEfghIJ" }, "ingestEndpoint": "a1b2c3d4e5f6.global-contribute.live-video.net", "insecureIngest": true, "playbackUrl": "https://a1b2c3d4e5f6.us-west-2.playback.live-video.net/api/video/v1/us-west-2.123456789012.channel.abcdEFGH.m3u8", "preset": "", "authorized": false, "tags": {} }`For more information, see [Create a Channel](https://docs.aws.amazon.com/ivs/latest/LowLatencyUserGuide/getting-started-create-channel.html)in the*IVS Low-Latency User Guide*.**Example 2: To update a channel's configuration to enable recording**The following `update-channel`example updates the channel configuration for a specified channel ARN to enable recording. This does not affect an ongoing stream of this channel; you must stop and restart the stream for the changes to take effect.`aws ivs update-channel \ --arn '``arn:aws:ivs:us-west-2:123456789012:channel/abcdABCDefgh`' \ --no-insecure-ingest \ --recording-configuration-arn '`arn:aws:ivs:us-west-2:123456789012:recording-configuration/ABCD12cdEFgh`'Output: `{ "channel": { "arn": "arn:aws:ivs:us-west-2:123456789012:channel/abcdABCDefgh", "name": "test-channel-with-recording", "latencyMode": "LOW", "containerFormat": "TS", "multitrackInputConfiguration": { "enabled": false, "maximumResolution": "FULL_HD", "policy": "ALLOW" }, "type": "STANDARD", "playbackRestrictionPolicyArn": "", "recordingConfigurationArn": "arn:aws:ivs:us-west-2:123456789012:recording-configuration/ABCD12cdEFgh", "srt": { "endpoint": "a1b2c3d4e5f6.srt.live-video.net", "passphrase": "BA1C2defGHijkLMNo3PqQRstUvwxyzaBCDEfghh4ijklMN5opqrStuVWxyzAbCDEfghIJ" }, "ingestEndpoint": "a1b2c3d4e5f6.global-contribute.live-video.net", "insecureIngest": false, "playbackUrl": "https://a1b2c3d4e5f6.us-west-2.playback.live-video.net/api/video/v1/us-west-2.123456789012.channel.abcdEFGH.m3u8", "preset": "", "authorized": false, "tags": {} } }`For more information, see [Record to Amazon S3](https://docs.aws.amazon.com/ivs/latest/LowLatencyUserGuide/record-to-s3.html)in the*IVS Low-Latency User Guide*.**Example 3: To update a channel's configuration to disable recording**The following `update-channel`example updates the channel configuration for a specified channel ARN to disable recording. This does not affect an ongoing stream of this channel; you must stop and restart the stream for the changes to take effect.`aws ivs update-channel \ --arn '``arn:aws:ivs:us-west-2:123456789012:channel/abcdABCDefgh`' \ --recording-configuration-arn ''Output: `{ "channel": { "arn": "arn:aws:ivs:us-west-2:123456789012:channel/abcdABCDefgh", "name": "test-channel-with-recording", "latencyMode": "LOW", "containerFormat": "TS", "multitrackInputConfiguration": { "enabled": false, "maximumResolution": "FULL_HD", "policy": "ALLOW" }, "type": "STANDARD", "playbackRestrictionPolicyArn": "", "recordingConfigurationArn": "", "srt": { "endpoint": "a1b2c3d4e5f6.srt.live-video.net", "passphrase": "AB1C2edfGHijkLMNo3PqQRstUvwxyzaBCDEfghh4ijklMN5opqrStuVWxyzAbCDEfghIJ" }, "ingestEndpoint": "a1b2c3d4e5f6.global-contribute.live-video.net", "insecureIngest": false, "playbackUrl": "https://a1b2c3d4e5f6.us-west-2.playback.live-video.net/api/video/v1/us-west-2.123456789012.channel.abcdEFGH.m3u8", "preset": "", "authorized": false, "tags": {} } }`For more information, see [Record to Amazon S3](https://docs.aws.amazon.com/ivs/latest/LowLatencyUserGuide/record-to-s3.html)in the*IVS Low-Latency User Guide*.**Example 4: To update a channel's configuration to enable playback restriction**The following `update-channel`example updates the channel configuration for a specified channel ARN to apply a playback restriction policy. This does not affect an ongoing stream of this channel; you must stop and restart the stream for the changes to take effect.`aws ivs update-channel \ --arn '``arn:aws:ivs:us-west-2:123456789012:channel/abcdABCDefgh`' \ --no-insecure-ingest \ --playback-restriction-policy-arn '`arn:aws:ivs:us-west-2:123456789012:playback-restriction-policy/ABcdef34ghIJ`'Output: `{ "channel": { "arn": "arn:aws:ivs:us-west-2:123456789012:channel/abcdABCDefgh", "name": "test-channel-with-playback-restriction-policy", "latencyMode": "LOW", "containerFormat": "TS", "multitrackInputConfiguration": { "enabled": false, "maximumResolution": "FULL_HD", "policy": "ALLOW" }, "type": "STANDARD", "playbackRestrictionPolicyArn": "arn:aws:ivs:us-west-2:123456789012:playback-restriction-policy/ABcdef34ghIJ", "recordingConfigurationArn": "", "srt": { "endpoint": "a1b2c3d4e5f6.srt.live-video.net", "passphrase": "AB1C2defGHijkLMNo3PqQRstUvwxyzaCBDEfghh4ijklMN5opqrStuVWxyzAbCDEfghIJ" }, "ingestEndpoint": "a1b2c3d4e5f6.global-contribute.live-video.net", "insecureIngest": false, "playbackUrl": "https://a1b2c3d4e5f6.us-west-2.playback.live-video.net/api/video/v1/us-west-2.123456789012.channel.abcdEFGH.m3u8", "preset": "", "authorized": false, "tags": {} } }`For more information, see [Undesired Content and Viewers](https://docs.aws.amazon.com/ivs/latest/LowLatencyUserGuide/undesired-content.html)in the*IVS Low-Latency User Guide*.**Example 5: To update a channel's configuration to disable playback restriction**The following `update-channel`example updates the channel configuration for a specified channel ARN to disable playback restriction. This does not affect an ongoing stream of this channel; you must stop and restart the stream for the changes to take effect.`aws ivs update-channel \ --arn '``arn:aws:ivs:us-west-2:123456789012:channel/abcdABCDefgh`' \ --playback-restriction-policy-arn ''Output: `{ "channel": { "arn": "arn:aws:ivs:us-west-2:123456789012:channel/abcdABCDefgh", "name": "test-channel-with-playback-restriction-policy", "latencyMode": "LOW", "containerFormat": "TS", "multitrackInputConfiguration": { "enabled": false, "maximumResolution": "FULL_HD", "policy": "ALLOW" }, "type": "STANDARD", "playbackRestrictionPolicyArn": "", "recordingConfigurationArn": "", "srt": { "endpoint": "a1b2c3d4e5f6.srt.live-video.net", "passphrase": "AB1C2defGHijkLMNo3PqQRstUvwxyzaBCDeFghh4ijklMN5opqrStuVWxyzAbCDEfghIJ" }, "ingestEndpoint": "a1b2c3d4e5f6.global-contribute.live-video.net", "insecureIngest": false, "playbackUrl": "https://a1b2c3d4e5f6.us-west-2.playback.live-video.net/api/video/v1/us-west-2.123456789012.channel.abcdEFGH.m3u8", "preset": "", "authorized": false, "tags": {} } }`For more information, see [Undesired Content and Viewers](https://docs.aws.amazon.com/ivs/latest/LowLatencyUserGuide/undesired-content.html)in the*IVS Low-Latency User Guide*.**Example 6: To update a channel's configuration to enable multitrack**The following `update-channel`example updates the channel configuration for a specified channel ARN to enable multitrack. This does not affect an ongoing stream of this channel; you must stop and restart the stream for the changes to take effect.`aws ivs update-channel \ --arn '``arn:aws:ivs:us-west-2:123456789012:channel/abcdABCDefgh`' \ --container-format '`FRAGMENTED_MP4`' \ --multitrack-input-configuration '`{"enabled": true,"maximumResolution": "FULL_HD","policy": "ALLOW"}`'Output: `{ "channel": { "arn": "arn:aws:ivs:us-west-2:123456789012:channel/abcdABCDefgh", "containerFormat": "FRAGMENTED_MP4", "name": "test-channel-with-multitrack", "latencyMode": "LOW", "multitrackInputConfiguration": { "enabled": true, "maximumResolution": "FULL_HD", "policy": "ALLOW" }, "type": "STANDARD", "playbackRestrictionPolicyArn": "", "recordingConfigurationArn": "", "srt": { "endpoint": "a1b2c3d4e5f6.srt.live-video.net", "passphrase": "AB1C2defGHijkLMNo3PqQRstUvwxyzaCBDEfghh4ijklMN5opqrStuVWxyzAbCDEfghIJ" }, "ingestEndpoint": "a1b2c3d4e5f6.global-contribute.live-video.net", "insecureIngest": false, "playbackUrl": "https://a1b2c3d4e5f6.us-west-2.playback.live-video.net/api/video/v1/us-west-2.123456789012.channel.abcdEFGH.m3u8", "preset": "", "authorized": false, "tags": {} } }`For more information, see [Undesired Content and Viewers](https://docs.aws.amazon.com/ivs/latest/LowLatencyUserGuide/multitrack-video.html)in the*IVS Low-Latency User Guide*.**Example 7: To update a channel's configuration to disable playback restriction**The following `update-channel`example updates the channel configuration for a specified channel ARN to disable multitrack. This does not affect an ongoing stream of this channel; you must stop and restart the stream for the changes to take effect.`aws ivs update-channel \ --arn '``arn:aws:ivs:us-west-2:123456789012:channel/abcdABCDefgh`' \ --container-format '`TS`' \ --multitrack-input-configuration '`{"enabled": false}`'Output: `{ "channel": { ""arn": "arn:aws:ivs:us-west-2:123456789012:channel/abcdABCDefgh", "containerFormat": "TS", "name": "test-channel-with-multitrack", "latencyMode": "LOW", "multitrackInputConfiguration": { "enabled": false, "maximumResolution": "FULL_HD", "policy": "ALLOW" }, "type": "STANDARD", "playbackRestrictionPolicyArn": "", "recordingConfigurationArn": "", "srt": { "endpoint": "a1b2c3d4e5f6.srt.live-video.net", "passphrase": "AB1C2defGHijkLMNo3PqQRstUvwxyzaCBDEfghh4ijklMN5opqrStuVWxyzAbCDEfghIJ" }, "ingestEndpoint": "a1b2c3d4e5f6.global-contribute.live-video.net", "insecureIngest": false, "playbackUrl": "https://a1b2c3d4e5f6.us-west-2.playback.live-video.net/api/video/v1/us-west-2.123456789012.channel.abcdEFGH.m3u8", "preset": "", "authorized": false, "tags": {} } }`For more information, see [Undesired Content and Viewers](https://docs.aws.amazon.com/ivs/latest/LowLatencyUserGuide/multitrack-video.html)in the*IVS Low-Latency User Guide*.- 
                    For API details, see [UpdateChannel](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ivs/update-channel.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `update-playback-restriction-policy`.

- **AWS CLI**
- 
            
                    **To update a playback restriction policy**The following `update-playback-restriction-policy`example updates the playback restriction policy with the specified policy ARN to disable strict origin enforcement. This does not affect an ongoing stream of the associated channel; you must stop and restart the stream for the changes to take effect.`aws ivs update-playback-restriction-policy \ --arn``"arn:aws:ivs:us-west-2:123456789012:playback-restriction-policy/ABcdef34ghIJ"`\ --no-enable-strict-origin-enforcementOutput: `{ "playbackRestrictionPolicy": { "arn": "arn:aws:ivs:us-west-2:123456789012:playback-restriction-policy/ABcdef34ghIJ", "allowedCountries": [ "US", "MX" ], "allowedOrigins": [ "https://www.website1.com", "https://www.website2.com" ], "enableStrictOriginEnforcement": false, "name": "test-playback-restriction-policy", "tags": { "key1": "value1", "key2": "value2" } } }`For more information, see [Undesired Content and Viewers](https://docs.aws.amazon.com/ivs/latest/LowLatencyUserGuide/undesired-content.html)in the*IVS Low-Latency User Guide*.- 
                    For API details, see [UpdatePlaybackRestrictionPolicy](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ivs/update-playback-restriction-policy.html)in*AWS CLI Command Reference*.
 
-