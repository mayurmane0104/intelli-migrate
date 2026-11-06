# Amazon IVS Real-Time Streaming examples using AWS CLI - AWS Command Line Interface

**Source:** [https://docs.aws.amazon.com/cli/latest/userguide/cli_ivs-realtime_code_examples.html](https://docs.aws.amazon.com/cli/latest/userguide/cli_ivs-realtime_code_examples.html)

---

The following code examples show you how to perform actions and implement common scenarios by using the AWS Command Line Interface with Amazon IVS Real-Time Streaming.

*Actions* are code excerpts from larger programs and must be run in context. While actions show you how to call individual service functions, you can see actions in context in their related scenarios.

Each example includes a link to the complete source code, where you can find instructions on how to set up and run the code in context.

###### Topics

## Actions

    The following code example shows how to use `create-encoder-configuration`.

- **AWS CLI**
- 
            
                    **To create a composition encoder configuration**The following `create-encoder-configuration`example creates a composition encoder configuration with the specified properties.`aws ivs-realtime create-encoder-configuration \ --name``test-ec`--video`bitrate=3500000,framerate=30.0,height=1080,width=1920`Output: `{ "encoderConfiguration": { "arn": "arn:aws:ivs:ap-northeast-1:123456789012:encoder-configuration/ABabCDcdEFef", "name": "test-ec", "tags": {}, "video": { "bitrate": 3500000, "framerate": 30, "height": 1080, "width": 1920 } } }`For more information, see [Enabling Multiple Hosts on an Amazon IVS Stream](https://docs.aws.amazon.com/ivs/latest/LowLatencyUserGuide/multiple-hosts.html)in the*Amazon Interactive Video Service User Guide*.- 
                    For API details, see [CreateEncoderConfiguration](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ivs-realtime/create-encoder-configuration.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `create-ingest-configuration`.

- **AWS CLI**
- 
            
                    **To create an ingest configuration**The following `create-ingest-configuration`example creates an ingest configuration using RTMPS protocol.`aws ivs-realtime create-ingest-configuration \ --name``ingest1`\ --ingest-protocol`rtmps`Output: `{ "ingestConfiguration": { "name": "ingest1", "arn": "arn:aws:ivs:us-west-2:123456789012:ingest-configuration/AbCdEfGh1234", "ingestProtocol": "RTMPS", "streamKey": "rt_123456789012_us-west-2_AbCdEfGh1234_abcd1234efgh5678ijkl9012MNOP34", "stageArn": "", "participantId": "xyZ654abC321", "state": "INACTIVE", "userId": "", "tags": {} } }`For more information, see [IVS Stream Ingest | Real-Time Streaming](https://docs.aws.amazon.com/ivs/latest/RealTimeUserGuide/rt-stream-ingest.html)in the*Amazon Interactive Video Service User Guide*.- 
                    For API details, see [CreateIngestConfiguration](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ivs-realtime/create-ingest-configuration.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `create-participant-token`.

- **AWS CLI**
- 
            
                    **To create a stage participant token**The following `create-participant-token`example creates a participant toke for the specified stage.`aws ivs-realtime create-participant-token \ --stage-arn``arn:aws:ivs:us-west-2:123456789012:stage/abcdABCDefgh`\ --user-id`bob`Output: `{ "participantToken": { "expirationTime": "2023-03-07T09:47:43+00:00", "participantId": "ABCDEfghij01234KLMN6789", "token": "abcd1234defg5678" } }`For more information, see [Enabling Multiple Hosts on an Amazon IVS Stream](https://docs.aws.amazon.com/ivs/latest/userguide/multiple-hosts.html)in the*Amazon Interactive Video Service User Guide*.- 
                    For API details, see [CreateParticipantToken](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ivs-realtime/create-participant-token.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `create-stage`.

- **AWS CLI**
- 
            
                    **Example 1: To create a stage**The following `create-stage`example creates a stage and stage participant token for a specified user.`aws ivs-realtime create-stage \ --name``stage1`\ --participant-token-configurations`userId=alice`Output: `{ "participantTokens": [ { "participantId": "ABCDEfghij01234KLMN5678", "token": "a1b2c3d4567890ab", "userId": "alice" } ], "stage": { "activeSessionId": "st-a1b2c3d4e5f6g", "arn": "arn:aws:ivs:us-west-2:123456789012:stage/abcdABCDefgh", "autoParticipantRecordingConfiguration": { "storageConfigurationArn": "", "mediaTypes": [ "AUDIO_VIDEO" ], "thumbnailConfiguration": { "targetIntervalSeconds": 60, "storage": [ "SEQUENTIAL" ], "recordingMode": "DISABLED" }, "recordingReconnectWindowSeconds": 0, "hlsConfiguration": { "targetSegmentDurationSeconds": 6 }, "recordParticipantReplicas": true }, "endpoints": { "events": "wss://global.events.live-video.net", "rtmp": "rtmp://9x0y8z7s6t5u.global-contribute-staging.live-video.net/app/", "rtmps": "rtmps://9x0y8z7s6t5u.global-contribute-staging.live-video.net:443/app/", "whip": "https://9x0y8z7s6t5u.global-bm.whip.live-video.net" }, "name": "stage1", "tags": {} } }`For more information, see [Enabling Multiple Hosts on an Amazon IVS Stream](https://docs.aws.amazon.com/ivs/latest/LowLatencyUserGuide/multiple-hosts.html)in the*Amazon IVS Low-Latency Streaming User Guide*.**Example 2: To create a stage and configure individual participant recording**The following `create-stage`example creates a stage and configures individual participant recording.`aws ivs-realtime create-stage \ --name``stage1`\ --auto-participant-recording-configuration '`{"mediaTypes": ["AUDIO_VIDEO"],"storageConfigurationArn": "arn:aws:ivs:us-west-2:123456789012:storage-configuration/abcdABCDefgh", "recordingReconnectWindowSeconds": 100, \ "hlsConfiguration": {"targetSegmentDurationSeconds": 5}}`'Output: `{ "stage": { "activeSessionId": "st-a1b2c3d4e5f6g", "arn": "arn:aws:ivs:us-west-2:123456789012:stage/abcdABCDefgh", "autoParticipantRecordingConfiguration": { "storageConfigurationArn": "arn:aws:ivs:us-west-2:123456789012:storage-configuration/abcdABCDefgh" "mediaTypes": [ "AUDIO_VIDEO" ], "thumbnailConfiguration": { "targetIntervalSeconds": 60, "storage": [ "SEQUENTIAL" ], "recordingMode": "DISABLED" }, "recordingReconnectWindowSeconds": 100, "hlsConfiguration": { "targetSegmentDurationSeconds": 5 }, "recordParticipantReplicas": true }, "endpoints": { "events": "wss://global.events.live-video.net", "rtmp": "rtmp://9x0y8z7s6t5u.global-contribute-staging.live-video.net/app/", "rtmps": "rtmps://9x0y8z7s6t5u.global-contribute-staging.live-video.net:443/app/", "whip": "https://9x0y8z7s6t5u.global-bm.whip.live-video.net" }, "name": "stage1", "tags": {} } }`For more information, see [Enabling Multiple Hosts on an Amazon IVS Stream](https://docs.aws.amazon.com/ivs/latest/LowLatencyUserGuide/multiple-hosts.html)in the*Amazon IVS Low-Latency Streaming User Guide*.**Example 3: To create a stage and configure individual participant recording with thumbnail recording enabled**The following `create-stage`example creates a stage and configures individual participant recording with thumbnail recording enabled.`aws ivs-realtime create-stage \ --name``stage1`\ --auto-participant-recording-configuration '`{"mediaTypes": ["AUDIO_VIDEO"],"storageConfigurationArn": "arn:aws:ivs:us-west-2:123456789012:storage-configuration/abcdABCDefgh", \ "thumbnailConfiguration": {"recordingMode": "INTERVAL","storage": ["SEQUENTIAL"],"targetIntervalSeconds": 60}}`'Output: `{ "stage": { "activeSessionId": "st-a1b2c3d4e5f6g", "arn": "arn:aws:ivs:us-west-2:123456789012:stage/abcdABCDefgh", "autoParticipantRecordingConfiguration": { "storageConfigurationArn": "arn:aws:ivs:us-west-2:123456789012:storage-configuration/abcdABCDefgh", "mediaTypes": [ "AUDIO_VIDEO" ], "thumbnailConfiguration": { "targetIntervalSeconds": 60, "storage": [ "SEQUENTIAL" ], "recordingMode": "INTERVAL" }, "recordingReconnectWindowSeconds": 0, "hlsConfiguration": { "targetSegmentDurationSeconds": 6 }, "recordParticipantReplicas": true }, "endpoints": { "events": "wss://global.events.live-video.net", "rtmp": "rtmp://9x0y8z7s6t5u.global-contribute-staging.live-video.net/app/", "rtmps": "rtmps://9x0y8z7s6t5u.global-contribute-staging.live-video.net:443/app/", "whip": "https://9x0y8z7s6t5u.global-bm.whip.live-video.net" }, "name": "stage1", "tags": {} } }`For more information, see [Enabling Multiple Hosts on an Amazon IVS Stream](https://docs.aws.amazon.com/ivs/latest/LowLatencyUserGuide/multiple-hosts.html)in the*Amazon IVS Low-Latency Streaming User Guide*.- 
                    For API details, see [CreateStage](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ivs-realtime/create-stage.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `create-storage-configuration`.

- **AWS CLI**
- 
            
                    **To create a composition storage configuration**The following `create-storage-configuration`example creates a composition storage configuration with the specified properties.`aws ivs-realtime create-storage-configuration \ --name``"test-sc"`--s3`"bucketName=amzn-s3-demo-bucket"`Output: `{ "storageConfiguration": { "arn": "arn:aws:ivs:ap-northeast-1:123456789012:storage-configuration/ABabCDcdEFef", "name": "test-sc", "s3": { "bucketName": "amzn-s3-demo-bucket" }, "tags": {} } }`For more information, see [Enabling Multiple Hosts on an Amazon IVS Stream](https://docs.aws.amazon.com/ivs/latest/LowLatencyUserGuide/multiple-hosts.html)in the*Amazon Interactive Video Service User Guide*.- 
                    For API details, see [CreateStorageConfiguration](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ivs-realtime/create-storage-configuration.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `delete-encoder-configuration`.

- **AWS CLI**
- 
            
                    **To delete a composition encoder configuration**The following `delete-encoder-configuration`deletes the composition encoder configuration specified by the given ARN (Amazon Resource Name).`aws ivs-realtime delete-encoder-configuration \ --arn``"arn:aws:ivs:ap-northeast-1:123456789012:encoder-configuration/ABabCDcdEFef"`This command produces no output. For more information, see [Enabling Multiple Hosts on an Amazon IVS Stream](https://docs.aws.amazon.com/ivs/latest/LowLatencyUserGuide/multiple-hosts.html)in the*Amazon Interactive Video Service User Guide*.- 
                    For API details, see [DeleteEncoderConfiguration](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ivs-realtime/delete-encoder-configuration.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `delete-ingest-configuration`.

- **AWS CLI**
- 
            
                    **Example 1: To delete an inactive ingest configuration**The following `delete-ingest-configuration`example deletes the inactive ingest configuration for a specified ingest-configuration ARN (Amazon Resource Name).`aws ivs-realtime delete-ingest-configuration \ --arn``arn:aws:ivs:us-west-2:123456789012:ingest-configuration/AbCdEfGh1234`This command produces no output. For more information, see [IVS Stream Ingest | Real-Time Streaming](https://docs.aws.amazon.com/ivs/latest/RealTimeUserGuide/rt-stream-ingest.html)in the*Amazon Interactive Video Service User Guide*.**Example 2: To force delete an active ingest configuration**The following `delete-ingest-configuration`example forces deletion of the active ingest configuration for a specified ingest-configuration ARN (Amazon Resource Name).`aws ivs-realtime delete-ingest-configuration \ --arn``arn:aws:ivs:us-west-2:123456789012:ingest-configuration/AbCdEfGh1234`\ --forceThis command produces no output. For more information, see [IVS Stream Ingest | Real-Time Streaming](https://docs.aws.amazon.com/ivs/latest/RealTimeUserGuide/rt-stream-ingest.html)in the*Amazon Interactive Video Service User Guide*.- 
                    For API details, see [DeleteIngestConfiguration](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ivs-realtime/delete-ingest-configuration.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `delete-public-key`.

- **AWS CLI**
- 
            
                    **To delete a public key**The following `delete-public-key`deletes the specified public key.`aws ivs-realtime delete-public-key \ --arn``arn:aws:ivs:us-west-2:123456789012:public-key/abcdABC1efg2`This command produces no output. For more information, see [Distribute Participant Tokens](https://docs.aws.amazon.com/ivs/latest/RealTimeUserGuide/getting-started-distribute-tokens.html)in the*Amazon IVS Real-Time Streaming User Guide*.- 
                    For API details, see [DeletePublicKey](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ivs-realtime/delete-public-key.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `delete-stage`.

- **AWS CLI**
- 
            
                    **To delete a stage**The following `delete-stage`example deletes the specified stage.`aws ivs-realtime delete-stage \ --arn``arn:aws:ivs:us-west-2:123456789012:stage/abcdABCDefgh`This command produces no output. For more information, see [Enabling Multiple Hosts on an Amazon IVS Stream](https://docs.aws.amazon.com/ivs/latest/userguide/multiple-hosts.html)in the*Amazon Interactive Video Service User Guide*.- 
                    For API details, see [DeleteStage](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ivs-realtime/delete-stage.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `delete-storage-configuration`.

- **AWS CLI**
- 
            
                    **To delete a composition storage configuration**The following `delete-storage-configuration`deletes the composition storage configuration specified by the given ARN (Amazon Resource Name).`aws ivs-realtime delete-storage-configuration \ --arn``"arn:aws:ivs:ap-northeast-1:123456789012:storage-configuration/ABabCDcdEFef"`This command produces no output. For more information, see [Enabling Multiple Hosts on an Amazon IVS Stream](https://docs.aws.amazon.com/ivs/latest/LowLatencyUserGuide/multiple-hosts.html)in the*Amazon Interactive Video Service User Guide*.- 
                    For API details, see [DeleteStorageConfiguration](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ivs-realtime/delete-storage-configuration.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `disconnect-participant`.

- **AWS CLI**
- 
            
                    **To disconnect a stage participant**The following `disconnect-participant`example disconnects the specified participant from the specified stage.`aws ivs-realtime disconnect-participant \ --stage-arn``arn:aws:ivs:us-west-2:123456789012:stage/abcdABCDefgh`\ --participant-id`ABCDEfghij01234KLMN5678`This command produces no output. For more information, see [Enabling Multiple Hosts on an Amazon IVS Stream](https://docs.aws.amazon.com/ivs/latest/userguide/multiple-hosts.html)in the*Amazon Interactive Video Service User Guide*.- 
                    For API details, see [DisconnectParticipant](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ivs-realtime/disconnect-participant.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `get-composition`.

- **AWS CLI**
- 
            
                    **Example 1: To get a composition with default layout settings**The following `get-composition`example gets the composition for the ARN (Amazon Resource Name) specified.`aws ivs-realtime get-composition \ --arn``"arn:aws:ivs:ap-northeast-1:123456789012:composition/abcdABCDefgh"`Output: `{ "composition": { "arn": "arn:aws:ivs:ap-northeast-1:123456789012:composition/abcdABCDefgh", "destinations": [ { "configuration": { "channel": { "channelArn": "arn:aws:ivs:ap-northeast-1:123456789012:channel/abcABCdefDEg", "encoderConfigurationArn": "arn:aws:ivs:ap-northeast-1:123456789012:encoder-configuration/ABabCDcdEFef" }, "name": "" }, "id": "AabBCcdDEefF", "startTime": "2023-10-16T23:26:00+00:00", "state": "ACTIVE" }, { "configuration": { "name": "", "s3": { "encoderConfigurationArns": [ "arn:aws:ivs:arn:aws:ivs:ap-northeast-1:123456789012:encoder-configuration/ABabCDcdEFef" ], "recordingConfiguration": { "format": "HLS", "hlsConfiguration": { "targetSegmentDurationSeconds": 2 } }, "storageConfigurationArn": "arn:arn:aws:ivs:ap-northeast-1:123456789012:storage-configuration/FefABabCDcdE", } }, "detail": { "s3": { "recordingPrefix": "aBcDeFgHhGfE/AbCdEfGhHgFe/GHFabcgefABC/composite" } }, "id": "GHFabcgefABC", "startTime": "2023-10-16T23:26:00+00:00", "state": "STARTING" } ], "layout": { "grid": { "featuredParticipantAttribute": "", "gridGap": 2, "omitStoppedVideo": false, "participantOrderAttribute": "", "videoAspectRatio": "VIDEO", "videoFillMode": "" } }, "stageArn": "arn:aws:ivs:ap-northeast-1:123456789012:stage/defgABCDabcd", "startTime": "2023-10-16T23:24:00+00:00", "state": "ACTIVE", "tags": {} } }`For more information, see [IVS Composite Recording | Real-Time Streaming](https://docs.aws.amazon.com/ivs/latest/RealTimeUserGuide/rt-composite-recording.html)in the*Amazon Interactive Video Service User Guide*.**Example 2: To get a composition with PiP layout**The following `get-composition`example gets the composition for the ARN (Amazon Resource Name) specified, which uses PiP layout.`aws ivs-realtime get-composition \ --arn``"arn:aws:ivs:ap-northeast-1:123456789012:composition/wxyzWXYZpqrs"`Output: `{ "composition": { "arn": "arn:aws:ivs:ap-northeast-1:123456789012:composition/wxyzWXYZpqrs", "destinations": [ { "configuration": { "channel": { "channelArn": "arn:aws:ivs:ap-northeast-1:123456789012:channel/abcABCdefDEg", "encoderConfigurationArn": "arn:aws:ivs:ap-northeast-1:123456789012:encoder-configuration/ABabCDcdEFef" }, "name": "" }, "id": "AabBCcdDEefF", "startTime": "2023-10-16T23:26:00+00:00", "state": "ACTIVE" }, { "configuration": { "name": "", "s3": { "encoderConfigurationArns": [ "arn:aws:ivs:arn:aws:ivs:ap-northeast-1:123456789012:encoder-configuration/ABabCDcdEFef" ], "recordingConfiguration": { "format": "HLS", "hlsConfiguration": { "targetSegmentDurationSeconds": 2 } }, "storageConfigurationArn": "arn:arn:aws:ivs:ap-northeast-1:123456789012:storage-configuration/FefABabCDcdE" } }, "detail": { "s3": { "recordingPrefix": "aBcDeFgHhGfE/AbCdEfGhHgFe/GHFabcgefABC/composite" } }, "id": "GHFabcgefABC", "startTime": "2023-10-16T23:26:00+00:00", "state": "STARTING" } ], "layout": { "pip": { "featuredParticipantAttribute": "abcdefg", "gridGap": 0, "omitStoppedVideo": false, "participantOrderAttribute": "", "pipBehavior": "STATIC", "pipOffset": 0, "pipParticipantAttribute": "", "pipPosition": "BOTTOM_RIGHT", "videoFillMode": "COVER" } }, "stageArn": "arn:aws:ivs:ap-northeast-1:123456789012:stage/defgABCDabcd", "startTime": "2023-10-16T23:24:00+00:00", "state": "ACTIVE", "tags": {} } }`For more information, see [IVS Composite Recording | Real-Time Streaming](https://docs.aws.amazon.com/ivs/latest/RealTimeUserGuide/rt-composite-recording.html)in the*Amazon Interactive Video Service User Guide*.**Example 3: To get a composition with thumbnail recording enabled**The following `get-composition`example gets the composition for the ARN (Amazon Resource Name) specified, which has thumbnail recording enabled with default settings.`aws ivs-realtime get-composition \ --arn``"arn:aws:ivs:ap-northeast-1:123456789012:composition/abcdABCDefgh"`Output: `{ "composition": { "arn": "arn:aws:ivs:ap-northeast-1:123456789012:composition/abcdABCDefgh", "destinations": [ { "configuration": { "channel": { "channelArn": "arn:aws:ivs:ap-northeast-1:123456789012:channel/abcABCdefDEg", "encoderConfigurationArn": "arn:aws:ivs:ap-northeast-1:123456789012:encoder-configuration/ABabCDcdEFef" }, "name": "" }, "id": "AabBCcdDEefF", "startTime": "2023-10-16T23:26:00+00:00", "state": "ACTIVE" }, { "configuration": { "name": "", "s3": { "encoderConfigurationArns": [ "arn:aws:ivs:arn:aws:ivs:ap-northeast-1:123456789012:encoder-configuration/ABabCDcdEFef" ], "recordingConfiguration": { "format": "HLS", "hlsConfiguration": { "targetSegmentDurationSeconds": 2 } }, "storageConfigurationArn": "arn:arn:aws:ivs:ap-northeast-1:123456789012:storage-configuration/FefABabCDcdE", "thumbnailConfigurations": [ { "targetIntervalSeconds": 60, "storage": [ "SEQUENTIAL" ], } ] } }, "detail": { "s3": { "recordingPrefix": "aBcDeFgHhGfE/AbCdEfGhHgFe/GHFabcgefABC/composite" } }, "id": "GHFabcgefABC", "startTime": "2023-10-16T23:26:00+00:00", "state": "STARTING" } ], "layout": { "grid": { "featuredParticipantAttribute": "" "gridGap": 2, "omitStoppedVideo": false, "participantOrderAttribute": "", "videoAspectRatio": "VIDEO", "videoFillMode": "" } }, "stageArn": "arn:aws:ivs:ap-northeast-1:123456789012:stage/defgABCDabcd", "startTime": "2023-10-16T23:24:00+00:00", "state": "ACTIVE", "tags": {} } }`For more information, see [IVS Composite Recording | Real-Time Streaming](https://docs.aws.amazon.com/ivs/latest/RealTimeUserGuide/rt-composite-recording.html)in the*Amazon Interactive Video Service User Guide*.- 
                    For API details, see [GetComposition](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ivs-realtime/get-composition.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `get-encoder-configuration`.

- **AWS CLI**
- 
            
                    **To get a composition encoder configuration**The following `get-encoder-configuration`example gets the composition encoder configuration specified by the given ARN (Amazon Resource Name).`aws ivs-realtime get-encoder-configuration \ --arn``"arn:aws:ivs:ap-northeast-1:123456789012:encoder-configuration/abcdABCDefgh"`Output: `{ "encoderConfiguration": { "arn": "arn:aws:ivs:ap-northeast-1:123456789012:encoder-configuration/abcdABCDefgh", "name": "test-ec", "tags": {}, "video": { "bitrate": 3500000, "framerate": 30, "height": 1080, "width": 1920 } } }`For more information, see [Enabling Multiple Hosts on an Amazon IVS Stream](https://docs.aws.amazon.com/ivs/latest/LowLatencyUserGuide/multiple-hosts.html)in the*Amazon Interactive Video Service User Guide*.- 
                    For API details, see [GetEncoderConfiguration](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ivs-realtime/get-encoder-configuration.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `get-ingest-configuration`.

- **AWS CLI**
- 
            
                    **To get ingest configuration information**The following `get-ingest-configuration`example gets the ingest configuration for a specified ingest-configuration ARN (Amazon Resource Name).`aws ivs-realtime get-ingest-configuration \ --arn``arn:aws:ivs:us-west-2:123456789012:ingest-configuration/AbCdEfGh1234`Output: `{ "ingestConfiguration": { "name": "ingest1", "arn": "arn:aws:ivs:us-west-2:123456789012:ingest-configuration/AbCdEfGh1234", "ingestProtocol": "RTMPS", "streamKey": "rt_123456789012_us-west-2_AbCdEfGh1234_abcd1234efgh5678ijkl9012MNOP34", "stageArn": "", "participantId": "xyZ654abC321", "state": "INACTIVE", "userId": "", "tags": {} } }`For more information, see [IVS Stream Ingest | Real-Time Streaming](https://docs.aws.amazon.com/ivs/latest/RealTimeUserGuide/rt-stream-ingest.html)in the*Amazon Interactive Video Service User Guide*.- 
                    For API details, see [GetIngestConfiguration](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ivs-realtime/get-ingest-configuration.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `get-participant`.

- **AWS CLI**
- 
            
                    **Example 1: To get a stage participant**The following `get-participant`example gets the stage participant for a specified participant ID and session ID in the specified stage ARN (Amazon Resource Name).`aws ivs-realtime get-participant \ --stage-arn``arn:aws:ivs:us-west-2:123456789012:stage/abcdABCDefgh`\ --session-id`st-a1b2c3d4e5f6g`\ --participant-id`abCDEf12GHIj`Output: `{ "participant": { "browserName": "Google Chrome", "browserVersion": "116", "firstJoinTime": "2023-04-26T20:30:34+00:00", "ispName": "Comcast", "osName": "Microsoft Windows 10 Pro", "osVersion": "10.0.19044", "participantId": "abCDEf12GHIj", "published": true, "recordingS3BucketName": "bucket-name", "recordingS3Prefix": "abcdABCDefgh/st-a1b2c3d4e5f6g/abCDEf12GHIj/1234567890", "recordingState": "ACTIVE", "sdkVersion": "", "state": "CONNECTED", "userId": "" } }`For more information, see [Enabling Multiple Hosts on an Amazon IVS Stream](https://docs.aws.amazon.com/ivs/latest/LowLatencyUserGuide/multiple-hosts.html)in the*Amazon IVS Low-Latency Streaming User Guide*.**Example 2: To get a stage participant that has been replicated to another stage**The following `get-participant`example gets the stage participant for a specified participant ID and session ID in the specified stage ARN (Amazon Resource Name), when the participant has also been replicated to another stage.`aws ivs-realtime get-participant \ --stage-arn``arn:aws:ivs:us-west-2:123456789012:stage/abcdABCDefgh`\ --session-id`st-a1b2c3d4e5f6g`\ --participant-id`abCDEf12GHIj`Output: `{ "participant": { "browserName": "Google Chrome", "browserVersion": "116", "firstJoinTime": "2023-04-26T20:30:34+00:00", "ispName": "Comcast", "osName": "Microsoft Windows 10 Pro", "osVersion": "10.0.19044", "participantId": "abCDEf12GHIj", "published": true, "recordingS3BucketName": "bucket-name", "recordingS3Prefix": "abcdABCDefgh/st-a1b2c3d4e5f6g/abCDEf12GHIj/1234567890", "recordingState": "ACTIVE", "replicationState": "ACTIVE", "replicationType": "SOURCE", "sdkVersion": "", "state": "CONNECTED", "userId": "" } }`For more information, see [Enabling Multiple Hosts on an Amazon IVS Stream](https://docs.aws.amazon.com/ivs/latest/LowLatencyUserGuide/multiple-hosts.html)in the*Amazon IVS Low-Latency Streaming User Guide*.**Example 3: To get a stage participant that has been replicated from another stage**The following `get-participant`example gets the stage participant for a specified participant ID and session ID in the specified stage ARN (Amazon Resource Name), when the participant has been replicated from another stage.`aws ivs-realtime get-participant \ --stage-arn``arn:aws:ivs:us-west-2:123456789012:stage/abcdABCDefgh`\ --session-id`st-a1b2c3d4e5f6g`\ --participant-id`abCDEf12GHIj`Output: `{ "participant": { "browserName": "Google Chrome", "browserVersion": "116", "firstJoinTime": "2023-04-26T20:30:34+00:00", "ispName": "Comcast", "osName": "Microsoft Windows 10 Pro", "osVersion": "10.0.19044", "participantId": "abCDEf12GHIj", "published": true, "recordingS3BucketName": "bucket-name", "recordingS3Prefix": "abcdABCDefgh/st-a1b2c3d4e5f6g/abCDEf12GHIj/1234567890", "recordingState": "ACTIVE", "replicationState": "ACTIVE", "replicationType": "REPLICA", "sdkVersion": "", "state": "CONNECTED", "userId": "" } }`For more information, see [Enabling Multiple Hosts on an Amazon IVS Stream](https://docs.aws.amazon.com/ivs/latest/LowLatencyUserGuide/multiple-hosts.html)in the*Amazon IVS Low-Latency Streaming User Guide*.- 
                    For API details, see [GetParticipant](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ivs-realtime/get-participant.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `get-public-key`.

- **AWS CLI**
- 
            
                    **To get an existing public key used to sign stage participant tokens**The following `get-public-key`example gets a public key specified by the provided ARN, for sigining stage participant tokens.`aws ivs-realtime get-public-key \ --arn``arn:aws:ivs:us-west-2:123456789012:public-key/abcdABC1efg2`Output: `{ "publicKey": { "arn": "arn:aws:ivs:us-west-2:123456789012:public-key/abcdABC1efg2", "name": "", "publicKeyMaterial": "-----BEGIN PUBLIC KEY-----\nMHYwEAYHKoZIzj0CAQYFK4EEACIDYgAEqVWUtqs6EktQMR1sCYmEzGvRwtaycI16\n9pmzcpiWu/uhNStGlteJ5odRfRwVkoQUMnSZXTCcbn9bBTTmiWo4mJcFOOAzsthH\n0UAb8NdD4tUE0At4a9hYP9IETEXAMPLE\n-----END PUBLIC KEY-----", "fingerprint": "12:a3:44:56:bc:7d:e8:9f:10:2g:34:hi:56:78:90:12", "tags": {} } }`For more information, see [Distribute Participant Tokens](https://docs.aws.amazon.com/ivs/latest/RealTimeUserGuide/getting-started-distribute-tokens.html)in the*Amazon IVS Real-Time Streaming User Guide*.- 
                    For API details, see [GetPublicKey](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ivs-realtime/get-public-key.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `get-stage-session`.

- **AWS CLI**
- 
            
                    **To get a stage session**The following `get-stage-session`example gets the stage session for a specified session ID of a specified stage ARN (Amazon Resource Name).`aws ivs-realtime get-stage-session \ --stage-arn``arn:aws:ivs:us-west-2:123456789012:stage/abcdABCDefgh`\ --session-id`st-a1b2c3d4e5f6g`Output: `{ "stageSession": { "endTime": "2023-04-26T20:36:29+00:00", "sessionId": "st-a1b2c3d4e5f6g", "startTime": "2023-04-26T20:30:29.602000+00:00" } }`For more information, see [Enabling Multiple Hosts on an Amazon IVS Stream](https://docs.aws.amazon.com/ivs/latest/userguide/multiple-hosts.html)in the*Amazon Interactive Video Service User Guide*.- 
                    For API details, see [GetStageSession](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ivs-realtime/get-stage-session.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `get-stage`.

- **AWS CLI**
- 
            
                    **To get a stage's configuration information**The following `get-stage`example gets the stage configuration for a specified stage ARN (Amazon Resource Name).`aws ivs-realtime get-stage \ --arn``arn:aws:ivs:us-west-2:123456789012:stage/abcdABCDefgh`Output: `{ "stage": { "activeSessionId": "st-a1b2c3d4e5f6g", "arn": "arn:aws:ivs:us-west-2:123456789012:stage/abcdABCDefgh", "autoParticipantRecordingConfiguration": { "storageConfigurationArn": "", "mediaTypes": [ "AUDIO_VIDEO" ], "thumbnailConfiguration": { "targetIntervalSeconds": 60, "storage": [ "SEQUENTIAL" ], "recordingMode": "DISABLED" }, "recordingReconnectWindowSeconds": 0, "hlsConfiguration": { "targetSegmentDurationSeconds": 6 }, "recordParticipantReplicas": true }, "endpoints": { "events": "wss://global.events.live-video.net", "rtmp": "rtmp://9x0y8z7s6t5u.global-contribute-staging.live-video.net/app/", "rtmps": "rtmps://9x0y8z7s6t5u.global-contribute-staging.live-video.net:443/app/", "whip": "https://9x0y8z7s6t5u.global-bm.whip.live-video.net" }, "name": "test", "tags": {} } }`For more information, see [Enabling Multiple Hosts on an Amazon IVS Stream](https://docs.aws.amazon.com/ivs/latest/LowLatencyUserGuide/multiple-hosts.html)in the*Amazon IVS Low-Latency Streaming User Guide*.- 
                    For API details, see [GetStage](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ivs-realtime/get-stage.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `get-storage-configuration`.

- **AWS CLI**
- 
            
                    **To get a composition storage configuration**The following `get-storage-configuration`example gets the composition storage configuration specified by the given ARN (Amazon Resource Name).`aws ivs-realtime get-storage-configuration \ --arn``"arn:aws:ivs:ap-northeast-1:123456789012:storage-configuration/abcdABCDefgh"`Output: `{ "storageConfiguration": { "arn": "arn:aws:ivs:ap-northeast-1:123456789012:storage-configuration/abcdABCDefgh", "name": "test-sc", "s3": { "bucketName": "amzn-s3-demo-bucket" }, "tags": {} } }`For more information, see [Enabling Multiple Hosts on an Amazon IVS Stream](https://docs.aws.amazon.com/ivs/latest/LowLatencyUserGuide/multiple-hosts.html)in the*Amazon Interactive Video Service User Guide*.- 
                    For API details, see [GetStorageConfiguration](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ivs-realtime/get-storage-configuration.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `import-public-key`.

- **AWS CLI**
- 
            
                    **To import an existing public key to be used to sign stage participant tokens**The following `import-public-key`example imports a public key from a material file, to be used for sigining stage participant tokens.`aws ivs-realtime import-public-key \ --public-key-material="`cat public.pem`"`Output: `{ "publicKey": { "arn": "arn:aws:ivs:us-west-2:123456789012:public-key/abcdABC1efg2", "name": "", "publicKeyMaterial": "-----BEGIN PUBLIC KEY-----\nMHYwEAYHKoZIzj0CAQYFK4EEACIDYgAEqVWUtqs6EktQMR1sCYmEzGvRwtaycI16\n9pmzcpiWu/uhNStGlteJ5odRfRwVkoQUMnSZXTCcbn9bBTTmiWo4mJcFOOAzsthH\n0UAb8NdD4tUE0At4a9hYP9IETEXAMPLE\n-----END PUBLIC KEY-----", "fingerprint": "12:a3:44:56:bc:7d:e8:9f:10:2g:34:hi:56:78:90:12", "tags": {} } }`For more information, see [Distribute Participant Tokens](https://docs.aws.amazon.com/ivs/latest/RealTimeUserGuide/getting-started-distribute-tokens.html)in the*Amazon IVS Real-Time Streaming User Guide*.- 
                    For API details, see [ImportPublicKey](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ivs-realtime/import-public-key.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `list-compositions`.

- **AWS CLI**
- 
            
                    **To get a list of compositions**The following `list-compositions`lists all compositions for your AWS account, in the AWS region where the API request is processed.`aws ivs-realtime list-compositions`Output: `{ "compositions": [ { "arn": "arn:aws:ivs:ap-northeast-1:123456789012:composition/abcdABCDefgh", "destinations": [ { "id": "AabBCcdDEefF", "startTime": "2023-10-16T23:25:23+00:00", "state": "ACTIVE" } ], "stageArn": "arn:aws:ivs:ap-northeast-1:123456789012:stage/defgABCDabcd", "startTime": "2023-10-16T23:25:21+00:00", "state": "ACTIVE", "tags": {} }, { "arn": "arn:aws:ivs:ap-northeast-1:123456789012:composition/ABcdabCDefgh", "destinations": [ { "endTime": "2023-10-16T23:25:00.786512+00:00", "id": "aABbcCDdeEFf", "startTime": "2023-10-16T23:24:01+00:00", "state": "STOPPED" }, { "endTime": "2023-10-16T23:25:00.786512+00:00", "id": "deEFfaABbcCD", "startTime": "2023-10-16T23:24:01+00:00", "state": "STOPPED" } ], "endTime": "2023-10-16T23:25:00+00:00", "stageArn": "arn:aws:ivs:ap-northeast-1:123456789012:stage/efghabcdABCD", "startTime": "2023-10-16T23:24:00+00:00", "state": "STOPPED", "tags": {} } ] }`For more information, see [Enabling Multiple Hosts on an Amazon IVS Stream](https://docs.aws.amazon.com/ivs/latest/LowLatencyUserGuide/multiple-hosts.html)in the*Amazon Interactive Video Service User Guide*.- 
                    For API details, see [ListCompositions](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ivs-realtime/list-compositions.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `list-encoder-configurations`.

- **AWS CLI**
- 
            
                    **To list composition encoder configurations**The following `list-encoder-configurations`lists all composition encoder configurations for your AWS account, in the AWS region where the API request is processed.`aws ivs-realtime list-encoder-configurations`Output: `{ "encoderConfigurations": [ { "arn": "arn:aws:ivs:ap-northeast-1:123456789012:encoder-configuration/abcdABCDefgh", "name": "test-ec-1", "tags": {} }, { "arn": "arn:aws:ivs:ap-northeast-1:123456789012:encoder-configuration/ABCefgEFGabc", "name": "test-ec-2", "tags": {} } ] }`For more information, see [Enabling Multiple Hosts on an Amazon IVS Stream](https://docs.aws.amazon.com/ivs/latest/LowLatencyUserGuide/multiple-hosts.html)in the*Amazon Interactive Video Service User Guide*.- 
                    For API details, see [ListEncoderConfigurations](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ivs-realtime/list-encoder-configurations.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `list-ingest-configurations`.

- **AWS CLI**
- 
            
                    **To get summary information about all ingest configurations**The following `list-ingest-configurations`example lists all ingest configurations for your AWS account, in the AWS region where the API request is processed.`aws ivs-realtime list-ingest-configurations`Output: `{ "ingestConfigurations": [ { "name": "", "arn": "arn:aws:ivs:us-west-2:123456789012:ingest-configuration/XYZuvwSt4567", "ingestProtocol": "RTMPS", "stageArn": "arn:aws:ivs:us-west-2:123456789012:stage/abcdABCDefgh", "participnatId": "abC789Xyz456", "state": "INACTIVE" "userId": "", } ] }`For more information, see [IVS Stream Ingest | Real-Time Streaming](https://docs.aws.amazon.com/ivs/latest/RealTimeUserGuide/rt-stream-ingest.html)in the*Amazon Interactive Video Service User Guide*.- 
                    For API details, see [ListIngestConfigurations](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ivs-realtime/list-ingest-configurations.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `list-participant-events`.

- **AWS CLI**
- 
            
                    **Example 1: To get a list of stage participant events**The following `list-participant-events`example lists all participant events for a specified participant ID and session ID of a specified stage ARN (Amazon Resource Name).`aws ivs-realtime list-participant-events \ --stage-arn``arn:aws:ivs:us-west-2:123456789012:stage/abcdABCDefgh`\ --session-id`st-a1b2c3d4e5f6g`\ --participant-id`abCDEf12GHIj`Output: `{ "events": [ { "eventTime": "2023-04-26T20:36:28+00:00", "name": "LEFT", "participantId": "abCDEf12GHIj" }, { "eventTime": "2023-04-26T20:36:28+00:00", "name": "PUBLISH_STOPPED", "participantId": "abCDEf12GHIj" }, { "eventTime": "2023-04-26T20:30:34+00:00", "name": "JOINED", "participantId": "abCDEf12GHIj" }, { "eventTime": "2023-04-26T20:30:34+00:00", "name": "PUBLISH_STARTED", "participantId": "abCDEf12GHIj" } ] }`For more information, see [Enabling Multiple Hosts on an Amazon IVS Stream](https://docs.aws.amazon.com/ivs/latest/LowLatencyUserGuide/multiple-hosts.html)in the*Amazon IVS Low-Latency Streaming User Guide*.**Example 2: To get a list of stage participant events, including participant replication stop and start**The following `list-participant-events`example lists all participant events for a specified session ID of a specified stage ARN (Amazon Resource Name), where a participant is replicated to another stage.`aws ivs-realtime list-participant-events \ --stage-arn``arn:aws:ivs:us-west-2:123456789012:stage/abcdABCDefgh`\ --session-id`st-a1b2c3d4e5f6g`\ --participant-id`abCDEf12GHIj`Output: `{ "events": [ { "eventTime": "2025-04-26T20:36:28+00:00", "name": "LEFT", "participantId": "abCDEf12GHIj" }, { "eventTime": "2025-04-26T20:36:28+00:00", "name": "PUBLISH_STOPPED", "participantId": "abCDEf12GHIj" }, { "eventTime": "2025-04-26T20:30:34+00:00", "name": "JOINED", "participantId": "abCDEf12GHIj" }, { "eventTime": "2025-04-26T20:30:34+00:00", "name": "PUBLISH_STARTED", "participantId": "abCDEf12GHIj" }, { "name": "REPLICATION_STARTED", "participantId": "abCDEf12GHIj", "eventTime": "2025-04-26T20:30:34+00:00", "destinationStageArn": "arn:aws:ivs:us-west-2:12345678901:stage/ABCDabcdefgh", "destinationSessionId": "st-b1c2d3e4f5g6a" }, { "name": "REPLICATION_STOPPED", "participantId": "abCDEf12GHIj", "eventTime": "2025-04-26T20:32:34+00:00", "destinationStageArn": "arn:aws:ivs:us-west-2:12345678901:stage/ABCDabcdefgh", "destinationSessionId": "st-b1c2d3e4f5g6a" } ] }`For more information, see [Enabling Multiple Hosts on an Amazon IVS Stream](https://docs.aws.amazon.com/ivs/latest/LowLatencyUserGuide/multiple-hosts.html)in the*Amazon IVS Low-Latency Streaming User Guide*.- 
                    For API details, see [ListParticipantEvents](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ivs-realtime/list-participant-events.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `list-participant-replicas`.

- **AWS CLI**
- 
            
                    **To get a list of stage participant replicas**The following `list-participant-replicas`example lists all stage participants replicated from the specified source stage ARN (Amazon Resource Name) to another stage.`aws ivs-realtime list-participant-replicas \ --source-stage-arn``arn:aws:ivs:us-west-2:123456789012:stage/abcdABCDefgh`\ --participant-id`abCDEf12GHIj`Output: `{ "replicas": [ { "sourceStageArn": "arn:aws:ivs:us-west-2:123456789012:stage/abcdABCDefgh", "participantId": "abCDEf12GHIj", "sourceSessionId": "st-a1b2c3d4e5f6g", "destinationStageArn": "arn:aws:ivs:us-west-2:012345678901:stage/ABCDabcdefgh", "destinationSessionId": "st-b1c2d3e4f5g6a", "replicationState": "ACTIVE" } ] }`For more information, see [IVS Participant Replication](https://docs.aws.amazon.com/ivs/latest/RealTimeUserGuide/rt-participant-replication.html)in the*Amazon IVS Real-Time Streaming User Guide*.- 
                    For API details, see [ListParticipantReplicas](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ivs-realtime/list-participant-replicas.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `list-participants`.

- **AWS CLI**
- 
            
                    **Example 1: To get a list of stage participants**The following `list-participants`example lists all participants for a specified session ID of a specified stage ARN (Amazon Resource Name).`aws ivs-realtime list-participants \ --stage-arn``arn:aws:ivs:us-west-2:123456789012:stage/abcdABCDefgh`\ --session-id`st-a1b2c3d4e5f6g`Output: `{ "participants": [ { "firstJoinTime": "2023-04-26T20:30:34+00:00", "participantId": "abCDEf12GHIj", "published": true, "recordingState": "STOPPED", "state": "DISCONNECTED", "userId": "" } ] }`For more information, see [Enabling Multiple Hosts on an Amazon IVS Stream](https://docs.aws.amazon.com/ivs/latest/LowLatencyUserGuide/multiple-hosts.html)in the*Amazon IVS Low-Latency Streaming User Guide*.**Example 2: To get a list of stage participants, when a participant has been replicated to another stage**The following `list-participants`example lists all participants for a specified session ID of a specified stage ARN (Amazon Resource Name), when a participant has been replicated to another stage.`aws ivs-realtime list-participants \ --stage-arn``arn:aws:ivs:us-west-2:123456789012:stage/abcdABCDefgh`\ --session-id`st-a1b2c3d4e5f6g`Output: `{ "participants": [ { "firstJoinTime": "2023-04-26T20:30:34+00:00", "participantId": "abCDEf12GHIj", "published": true, "recordingState": "STOPPED", "state": "DISCONNECTED", "userId": "", "replicationState": "ACTIVE", "replicationType": "SOURCE", "sourceStageArn": "", "sourceSessionId": "" } ] }`For more information, see [Enabling Multiple Hosts on an Amazon IVS Stream](https://docs.aws.amazon.com/ivs/latest/LowLatencyUserGuide/multiple-hosts.html)in the*Amazon IVS Low-Latency Streaming User Guide*.**Example 3: To get a list of stage participants, when a participant has been replicated from another stage**The following `list-participants`example lists all participants for a specified session ID of a specified stage ARN (Amazon Resource Name), when a participant has been replicated from another stage.`aws ivs-realtime list-participants \ --stage-arn``arn:aws:ivs:us-west-2:123456789012:stage/abcdABCDefgh`\ --session-id`st-a1b2c3d4e5f6g`Output: `{ "participants": [ { "firstJoinTime": "2023-04-26T20:30:34+00:00", "participantId": "abCDEf12GHIj", "published": true, "recordingState": "STOPPED", "state": "DISCONNECTED", "userId": "", "replicationState": "ACTIVE", "replicationType": "REPLICA", "sourceStageArn": "arn:aws:ivs:us-west-2:123456789012:stage/abcdABCDefgh", "sourceSessionId": "st-a1b2c3d4e5f6g" } ] }`For more information, see [Enabling Multiple Hosts on an Amazon IVS Stream](https://docs.aws.amazon.com/ivs/latest/LowLatencyUserGuide/multiple-hosts.html)in the*Amazon IVS Low-Latency Streaming User Guide*.- 
                    For API details, see [ListParticipants](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ivs-realtime/list-participants.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `list-public-keys`.

- **AWS CLI**
- 
            
                    **To list existing public keys available to sign stage participant tokens**The following `list-public-keys`example lists all public keys available for sigining stage participant tokens, in the AWS region where the API request is processed.`aws ivs-realtime list-public-keys`Output: `{ "publicKeys": [ { "arn": "arn:aws:ivs:us-west-2:123456789012:public-key/abcdABC1efg2", "name": "", "tags": {} }, { "arn": "arn:aws:ivs:us-west-2:123456789012:public-key/3bcdABCDefg4", "name": "", "tags": {} } ] }`For more information, see [Distribute Participant Tokens](https://docs.aws.amazon.com/ivs/latest/RealTimeUserGuide/getting-started-distribute-tokens.html)in the*Amazon IVS Real-Time Streaming User Guide*.- 
                    For API details, see [ListPublicKeys](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ivs-realtime/list-public-keys.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `list-stage-sessions`.

- **AWS CLI**
- 
            
                    **To get a list of stage sessions**The following `list-stage-sessions`example lists all sessions for a specified stage ARN (Amazon Resource Name).`aws ivs-realtime list-stage-sessions \ --stage-arn``arn:aws:ivs:us-west-2:123456789012:stage/abcdABCDefgh`Output: `{ "stageSessions": [ { "endTime": "2023-04-26T20:36:29+00:00", "sessionId": "st-a1b2c3d4e5f6g", "startTime": "2023-04-26T20:30:29.602000+00:00" } ] }`For more information, see [Enabling Multiple Hosts on an Amazon IVS Stream](https://docs.aws.amazon.com/ivs/latest/userguide/multiple-hosts.html)in the*Amazon Interactive Video Service User Guide*.- 
                    For API details, see [ListStageSessions](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ivs-realtime/list-stage-sessions.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `list-stages`.

- **AWS CLI**
- 
            
                    **To get summary information about all stages**The following `list-stages`example lists all stages for your AWS account, in the AWS region where the API request is processed.`aws ivs-realtime list-stages`Output: `{ "stages": [ { "activeSessionId": "st-a1b2c3d4e5f6g", "arn": "arn:aws:ivs:us-west-2:123456789012:stage/abcdABCDefgh", "name": "stage1", "tags": {} }, { "activeSessionId": "st-a123bcd456efg", "arn": "arn:aws:ivs:us-west-2:123456789012:stage/abcd1234ABCD", "name": "stage2", "tags": {} }, { "activeSessionId": "st-abcDEF1234ghi", "arn": "arn:aws:ivs:us-west-2:123456789012:stage/ABCD1234efgh", "name": "stage3", "tags": {} } ] }`For more information, see [Enabling Multiple Hosts on an Amazon IVS Stream](https://docs.aws.amazon.com/ivs/latest/LowLatencyUserGuide/multiple-hosts.html)in the*Amazon Interactive Video Service User Guide*.- 
                    For API details, see [ListStages](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ivs-realtime/list-stages.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `list-storage-configurations`.

- **AWS CLI**
- 
            
                    **To list composition storage configurations**The following `list-storage-configurations`lists all composition storage configurations for your AWS account, in the AWS region where the API request is processed.`aws ivs-realtime list-storage-configurations`Output: `{ "storageConfigurations": [ { "arn": "arn:aws:ivs:ap-northeast-1:123456789012:storage-configuration/abcdABCDefgh", "name": "test-sc-1", "s3": { "bucketName": "amzn-s3-demo-bucket-1" }, "tags": {} }, { "arn": "arn:aws:ivs:ap-northeast-1:123456789012:storage-configuration/ABCefgEFGabc", "name": "test-sc-2", "s3": { "bucketName": "amzn-s3-demo-bucket-2" }, "tags": {} } ] }`For more information, see [Enabling Multiple Hosts on an Amazon IVS Stream](https://docs.aws.amazon.com/ivs/latest/LowLatencyUserGuide/multiple-hosts.html)in the*Amazon Interactive Video Service User Guide*.- 
                    For API details, see [ListStorageConfigurations](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ivs-realtime/list-storage-configurations.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `start-composition`.

- **AWS CLI**
- 
            
                    **Example 1: To start a composition with default layout settings**The following `start-composition`example starts a composition for the specified stage to be streamed to the specified locations.`aws ivs-realtime start-composition \ --stage-arn``arn:aws:ivs:ap-northeast-1:123456789012:stage/defgABCDabcd`\ --destinations '`[{"channel": {"channelArn": "arn:aws:ivs:ap-northeast-1:123456789012:channel/abcABCdefDEg", \ "encoderConfigurationArn": "arn:aws:ivs:ap-northeast-1:123456789012:encoder-configuration/ABabCDcdEFef"}}, \ {"s3":{"encoderConfigurationArns":["arn:aws:ivs:ap-northeast-1:123456789012:encoder-configuration/ABabCDcdEFef"], \ "recordingConfiguration": {"hlsConfiguration": {"targetSegmentDurationSeconds": 5}}, \ "storageConfigurationArn":"arn:aws:ivs:ap-northeast-1:123456789012:storage-configuration/FefABabCDcdE"}}]`'Output: `{ "composition": { "arn": "arn:aws:ivs:ap-northeast-1:123456789012:composition/abcdABCDefgh", "destinations": [ { "configuration": { "channel": { "channelArn": "arn:aws:ivs:ap-northeast-1:123456789012:channel/abcABCdefDEg", "encoderConfigurationArn": "arn:aws:ivs:ap-northeast-1:123456789012:encoder-configuration/ABabCDcdEFef" }, "name": "" }, "id": "AabBCcdDEefF", "state": "STARTING" }, { "configuration": { "name": "", "s3": { "encoderConfigurationArns": [ "arn:aws:ivs:arn:aws:ivs:ap-northeast-1:123456789012:encoder-configuration/ABabCDcdEFef" ], "recordingConfiguration": { "format": "HLS", "hlsConfiguration": { "targetSegmentDurationSeconds": 5 } }, "storageConfigurationArn": "arn:arn:aws:ivs:ap-northeast-1:123456789012:storage-configuration/FefABabCDcdE" } }, "detail": { "s3": { "recordingPrefix": "aBcDeFgHhGfE/AbCdEfGhHgFe/GHFabcgefABC/composite" } }, "id": "GHFabcgefABC", "state": "STARTING" } ], "layout": { "grid": { "featuredParticipantAttribute": "" "gridGap": 2, "omitStoppedVideo": false, "participantOrderAttribute": "", "videoAspectRatio": "VIDEO", "videoFillMode": "" } }, "stageArn": "arn:aws:ivs:ap-northeast-1:123456789012:stage/defgABCDabcd", "startTime": "2023-10-16T23:24:00+00:00", "state": "STARTING", "tags": {} } }`For more information, see [IVS Composite Recording | Real-Time Streaming](https://docs.aws.amazon.com/ivs/latest/RealTimeUserGuide/rt-composite-recording.html)in the*Amazon Interactive Video Service User Guide*.**Example 2: To start a composition with PiP layout**The following `start-composition`example starts a composition for the specified stage to be streamed to the specified locations using PiP layout.`aws ivs-realtime start-composition \ --stage-arn``arn:aws:ivs:ap-northeast-1:123456789012:stage/defgABCDabcd`\ --destinations '`[{"channel": {"channelArn": "arn:aws:ivs:ap-northeast-1:123456789012:channel/abcABCdefDEg", \ "encoderConfigurationArn": "arn:aws:ivs:ap-northeast-1:123456789012:encoder-configuration/ABabCDcdEFef"}}, \ {"s3":{"encoderConfigurationArns":["arn:aws:ivs:ap-northeast-1:123456789012:encoder-configuration/ABabCDcdEFef"], \ "storageConfigurationArn":"arn:aws:ivs:ap-northeast-1:123456789012:storage-configuration/FefABabCDcdE"}}]`' \ --layout pip='{featuredParticipantAttribute="abcdefg"}'Output: `{ "composition": { "arn": "arn:aws:ivs:ap-northeast-1:123456789012:composition/wxyzWXYZpqrs", "destinations": [ { "configuration": { "channel": { "channelArn": "arn:aws:ivs:ap-northeast-1:123456789012:channel/abcABCdefDEg", "encoderConfigurationArn": "arn:aws:ivs:ap-northeast-1:123456789012:encoder-configuration/ABabCDcdEFef" }, "name": "" }, "id": "AabBCcdDEefF", "state": "STARTING" }, { "configuration": { "name": "", "s3": { "encoderConfigurationArns": [ "arn:aws:ivs:arn:aws:ivs:ap-northeast-1:123456789012:encoder-configuration/ABabCDcdEFef" ], "recordingConfiguration": { "format": "HLS", "hlsConfiguration": { "targetSegmentDurationSeconds": 2 } }, "storageConfigurationArn": "arn:arn:aws:ivs:ap-northeast-1:123456789012:storage-configuration/FefABabCDcdE" } }, "detail": { "s3": { "recordingPrefix": "aBcDeFgHhGfE/AbCdEfGhHgFe/GHFabcgefABC/composite" } }, "id": "GHFabcgefABC", "state": "STARTING" } ], "layout": { "pip": { "featuredParticipantAttribute": "abcdefg", "gridGap": 0, "omitStoppedVideo": false, "participantOrderAttribute": "", "pipBehavior": "STATIC", "pipOffset": 0, "pipParticipantAttribute": "", "pipPosition": "BOTTOM_RIGHT", "videoFillMode": "COVER" } }, "stageArn": "arn:aws:ivs:ap-northeast-1:123456789012:stage/defgABCDabcd", "startTime": "2023-10-16T23:24:00+00:00", "state": "STARTING", "tags": {} } }`For more information, see [IVS Composite Recording | Real-Time Streaming](https://docs.aws.amazon.com/ivs/latest/RealTimeUserGuide/rt-composite-recording.html)in the*Amazon Interactive Video Service User Guide*.**Example 3: To start a composition with thumbnail recording enabled**The following `start-composition`example starts a composition for the specified stage to be streamed to the specified locations with thumbnail recording enabled.`aws ivs-realtime start-composition \ --stage-arn``arn:aws:ivs:ap-northeast-1:123456789012:stage/defgABCDabcd`\ --destinations '`[{"channel": {"channelArn": "arn:aws:ivs:ap-northeast-1:123456789012:channel/abcABCdefDEg", \ "encoderConfigurationArn": "arn:aws:ivs:ap-northeast-1:123456789012:encoder-configuration/ABabCDcdEFef"}}, \ {"s3": {"encoderConfigurationArns": ["arn:aws:ivs:ap-northeast-1:123456789012:encoder-configuration/ABabCDcdEFef"], \ "storageConfigurationArn": "arn:aws:ivs:ap-northeast-1:123456789012:storage-configuration/FefABabCDcdE", \ "thumbnailConfigurations": [{"storage": ["SEQUENTIAL"],"targetIntervalSeconds": 60}]}}]`'Output: `{ "composition": { "arn": "arn:aws:ivs:ap-northeast-1:123456789012:composition/abcdABCDefgh", "destinations": [ { "configuration": { "channel": { "channelArn": "arn:aws:ivs:ap-northeast-1:123456789012:channel/abcABCdefDEg", "encoderConfigurationArn": "arn:aws:ivs:ap-northeast-1:123456789012:encoder-configuration/ABabCDcdEFef" }, "name": "" }, "id": "AabBCcdDEefF", "state": "STARTING" }, { "configuration": { "name": "", "s3": { "encoderConfigurationArns": [ "arn:aws:ivs:arn:aws:ivs:ap-northeast-1:123456789012:encoder-configuration/ABabCDcdEFef" ], "recordingConfiguration": { "format": "HLS", "hlsConfiguration": { "targetSegmentDurationSeconds": 2 } }, "storageConfigurationArn": "arn:arn:aws:ivs:ap-northeast-1:123456789012:storage-configuration/FefABabCDcdE", "thumbnailConfigurations": [ { "targetIntervalSeconds": 60, "storage": [ "SEQUENTIAL" ] } ] } }, "detail": { "s3": { "recordingPrefix": "aBcDeFgHhGfE/AbCdEfGhHgFe/GHFabcgefABC/composite" } }, "id": "GHFabcgefABC", "state": "STARTING" } ], "layout": { "grid": { "featuredParticipantAttribute": "" "gridGap": 2, "omitStoppedVideo": false, "participantOrderAttribute": "", "videoAspectRatio": "VIDEO", "videoFillMode": "" } }, "stageArn": "arn:aws:ivs:ap-northeast-1:123456789012:stage/defgABCDabcd", "startTime": "2023-10-16T23:24:00+00:00", "state": "STARTING", "tags": {} } }`For more information, see [Composite Recording (Real-Time Streaming)](https://docs.aws.amazon.com/ivs/latest/RealTimeUserGuide/rt-composite-recording.html)in the*Amazon Interactive Video Service User Guide*.**Example 4: To start a composition using grid layout with custom participant ordering**The following `start-composition`example starts a composition for the specified stage to be streamed to the specified locations using grid layout with custom participant ordering.`aws ivs-realtime start-composition \ --stage-arn``arn:aws:ivs:ap-northeast-1:123456789012:stage/defgABCDabcd`\ --destinations '`[{"channel": {"channelArn": "arn:aws:ivs:ap-northeast-1:123456789012:channel/abcABCdefDEg", \ "encoderConfigurationArn": "arn:aws:ivs:ap-northeast-1:123456789012:encoder-configuration/ABabCDcdEFef"}}, \ {"s3": {"encoderConfigurationArns": ["arn:aws:ivs:ap-northeast-1:123456789012:encoder-configuration/ABabCDcdEFef"], \ "storageConfigurationArn": "arn:aws:ivs:ap-northeast-1:123456789012:storage-configuration/FefABabCDcdE", \ "thumbnailConfigurations": [{"storage": ["SEQUENTIAL"],"targetIntervalSeconds": 60}]}}]`' \ --layout grid='{participantOrderAttribute="abcdefg"}'Output: `{ "composition": { "arn": "arn:aws:ivs:ap-northeast-1:123456789012:composition/abcdABCDefgh", "destinations": [ { "configuration": { "channel": { "channelArn": "arn:aws:ivs:ap-northeast-1:123456789012:channel/abcABCdefDEg", "encoderConfigurationArn": "arn:aws:ivs:ap-northeast-1:123456789012:encoder-configuration/ABabCDcdEFef" }, "name": "" }, "id": "AabBCcdDEefF", "state": "STARTING" }, { "configuration": { "name": "", "s3": { "encoderConfigurationArns": [ "arn:aws:ivs:arn:aws:ivs:ap-northeast-1:123456789012:encoder-configuration/ABabCDcdEFef" ], "recordingConfiguration": { "format": "HLS", "hlsConfiguration": { "targetSegmentDurationSeconds": 2 } }, "storageConfigurationArn": "arn:arn:aws:ivs:ap-northeast-1:123456789012:storage-configuration/FefABabCDcdE", "thumbnailConfigurations": [ { "targetIntervalSeconds": 60, "storage": [ "SEQUENTIAL" ] } ] } }, "detail": { "s3": { "recordingPrefix": "aBcDeFgHhGfE/AbCdEfGhHgFe/GHFabcgefABC/composite" } }, "id": "GHFabcgefABC", "state": "STARTING" } ], "layout": { "grid": { "featuredParticipantAttribute": "" "gridGap": 2, "omitStoppedVideo": false, "participantOrderAttribute": "abcdefg", "videoAspectRatio": "VIDEO", "videoFillMode": "" } }, "stageArn": "arn:aws:ivs:ap-northeast-1:123456789012:stage/defgABCDabcd", "startTime": "2023-10-16T23:24:00+00:00", "state": "STARTING", "tags": {} } }`For more information, see [IVS Composite Recording | Real-Time Streaming](https://docs.aws.amazon.com/ivs/latest/RealTimeUserGuide/rt-composite-recording.html)in the*Amazon Interactive Video Service User Guide*.- 
                    For API details, see [StartComposition](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ivs-realtime/start-composition.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `start-participant-replication`.

- **AWS CLI**
- 
            
                    **To start replicating a participant from one stage to another stage**The following `start-participant-replication`example replicates a participant from a source stage to a destination stage, with each stage specified by its ARN (Amazon Resource Name).`aws ivs-realtime start-participant-replication \ --source-stage-arn``arn:aws:ivs:us-west-2:123456789012:stage/abcdABCDefgh`\ --destination-stage-arn`arn:aws:ivs:us-west-2:234567890123:stage/bcdABCDefghi`\ --participant-id`abCDEf12GHIj`Output: `{ "accessControlAllowOrigin": "*", "accessControlExposeHeaders": "Access-Control-Allow-Origin,Access-Control-Expose-Headers,Cache-Control,Content-Length, \ Content-Security-Policy,Content-Type,date,Strict-Transport-Security,x-amz-apigw-id,x-amzn-errormessage,x-amzn-errortype, \ x-amzn-requestid,x-amzn-trace-id,X-Content-Type-Options,X-Frame-Options", "cacheControl": "no-store, no-cache", "contentSecurityPolicy": "default-src 'self'; upgrade-insecure-requests;", "strictTransportSecurity": "max-age:47304000; includeSubDomains", "xContentTypeOptions": "nosniff", "xFrameOptions": "DENY" }`For more information, see [IVS Participant Replication](https://docs.aws.amazon.com/ivs/latest/RealTimeUserGuide/rt-participant-replication.html)in the*Amazon IVS Real-Time Streaming User Guide*.- 
                    For API details, see [StartParticipantReplication](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ivs-realtime/start-participant-replication.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `stop-composition`.

- **AWS CLI**
- 
            
                    **To stop a composition**The following `stop-composition`stops the composition specified by the given ARN (Amazon Resource Name).`aws ivs-realtime stop-composition \ --arn``"arn:aws:ivs:ap-northeast-1:123456789012:composition/abcdABCDefgh"`This command produces no output. For more information, see [Enabling Multiple Hosts on an Amazon IVS Stream](https://docs.aws.amazon.com/ivs/latest/LowLatencyUserGuide/multiple-hosts.html)in the*Amazon Interactive Video Service User Guide*.- 
                    For API details, see [StopComposition](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ivs-realtime/stop-composition.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `stop-participant-replication`.

- **AWS CLI**
- 
            
                    **To stop replicating a participant from one stage to another stage**The following `stop-participant-replication`example stops replicating a participant from a source stage to a destination stage, with each stage specified by its ARN (Amazon Resource Name).`aws ivs-realtime stop-participant-replication \ --source-stage-arn``arn:aws:ivs:us-west-2:123456789012:stage/abcdABCDefgh`\ --destination-stage-arn`arn:aws:ivs:us-west-2:234567890123:stage/bcdABCDefghi`\ --participant-id`abCDEf12GHIj`Output: `{ "accessControlAllowOrigin": "*", "accessControlExposeHeaders": "Access-Control-Allow-Origin,Access-Control-Expose-Headers,Cache-Control,Content-Length, \ Content-Security-Policy,Content-Type,date,Strict-Transport-Security,x-amz-apigw-id,x-amzn-errormessage,x-amzn-errortype, \ x-amzn-requestid,x-amzn-trace-id,X-Content-Type-Options,X-Frame-Options", "cacheControl": "no-store, no-cache", "contentSecurityPolicy": "default-src 'self'; upgrade-insecure-requests;", "strictTransportSecurity": "max-age:47304000; includeSubDomains", "xContentTypeOptions": "nosniff", "xFrameOptions": "DENY" }`For more information, see [IVS Participant Replication](https://docs.aws.amazon.com/ivs/latest/RealTimeUserGuide/rt-participant-replication.html)in the*Amazon IVS Real-Time Streaming User Guide*.- 
                    For API details, see [StopParticipantReplication](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ivs-realtime/stop-participant-replication.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `update-ingest-configuration`.

- **AWS CLI**
- 
            
                    **To update an ingest configuration**The following `update-inegst-configuration`example updates an ingest configuration to attach it to a stage.`aws ivs-realtime update-ingest-configuration \ --arn``arn:aws:ivs:us-west-2:123456789012:ingest-configuration/AbCdEfGh1234`\ --stage-arn`arn:aws:ivs:us-west-2:123456789012:stage/abcdABCDefgh`Output: `{ "ingestConfiguration": { "name": "ingest1", "arn": "arn:aws:ivs:us-west-2:123456789012:ingest-configuration/AbCdEfGh1234", "ingestProtocol": "RTMPS", "streamKey": "rt_123456789012_us-west-2_AbCdEfGh1234_abcd1234efgh5678ijkl9012MNOP34", "stageArn": "arn:aws:ivs:us-west-2:123456789012:stage/abcdABCDefgh", "participantId": "xyZ654abC321", "state": "INACTIVE", "userId": "", "tags": {} } }`For more information, see [IVS Stream Ingest | Real-Time Streaming](https://docs.aws.amazon.com/ivs/latest/RealTimeUserGuide/rt-stream-ingest.html)in the*Amazon Interactive Video Service User Guide*.- 
                    For API details, see [UpdateIngestConfiguration](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ivs-realtime/update-ingest-configuration.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `update-stage`.

- **AWS CLI**
- 
            
                    **Example 1: To update a stage's configuration**The following `update-stage`example updates a stage for a specified stage ARN to update the stage name and configure individual participant recording with thumbnail recording enabled.`aws ivs-realtime update-stage \ --arn``arn:aws:ivs:us-west-2:123456789012:stage/abcdABCDefgh`\ --auto-participant-recording-configuration '`{"mediaTypes": ["AUDIO_VIDEO"],"storageConfigurationArn": "arn:aws:ivs:us-west-2:123456789012:storage-configuration/abcdABCDefgh", "recordingReconnectWindowSeconds": 100, \ "thumbnailConfiguration": {"recordingMode": "INTERVAL","storage": ["SEQUENTIAL"],"targetIntervalSeconds": 60}} \ "hlsConfiguration": {"targetSegmentDurationSeconds": 5}}`' \ --name`stage1a`Output: `{ "stage": { "arn": "arn:aws:ivs:us-west-2:123456789012:stage/abcdABCDefgh", "autoParticipantRecordingConfiguration": { "mediaTypes": [ "AUDIO_VIDEO" ], "storageConfigurationArn": "arn:aws:ivs:us-west-2:123456789012:storage-configuration/abcdABCDefgh", "thumbnailConfiguration": { "targetIntervalSeconds": 60, "storage": [ "SEQUENTIAL" ], "recordingMode": "INTERVAL" }, "recordingReconnectWindowSeconds": 100, "hlsConfiguration": { "targetSegmentDurationSeconds": 5 }, "recordParticipantReplicas": true }, "endpoints": { "events": "wss://global.events.live-video.net", "rtmp": "rtmp://9x0y8z7s6t5u.global-contribute-staging.live-video.net/app/", "rtmps": "rtmps://9x0y8z7s6t5u.global-contribute-staging.live-video.net:443/app/", "whip": "https://1a2b3c4d5e6f.global-bm.whip.live-video.net" }, "name": "stage1a", "tags": {} } }`For more information, see [Enabling Multiple Hosts on an Amazon IVS Stream](https://docs.aws.amazon.com/ivs/latest/LowLatencyUserGuide/multiple-hosts.html)in the*Amazon IVS Low-Latency Streaming User Guide*.**Example 2: To update a stage's configuration, including disabling participant replica recording**The following `update-stage`example updates a stage for a specified stage ARN to update the stage name and configure individual participant recording with thumbnail recording enabled and participant replica recording disabled.`aws ivs-realtime update-stage \ --arn``arn:aws:ivs:us-west-2:123456789012:stage/abcdABCDefgh`\ --auto-participant-recording-configuration '`{"mediaTypes": ["AUDIO_VIDEO"],"storageConfigurationArn": "arn:aws:ivs:us-west-2:123456789012:storage-configuration/abcdABCDefgh", "recordingReconnectWindowSeconds": 100, \ "thumbnailConfiguration": {"recordingMode": "INTERVAL","storage": ["SEQUENTIAL"],"targetIntervalSeconds": 60}, "recordParticipantReplicas":false} \ "hlsConfiguration": {"targetSegmentDurationSeconds": 5}}`' \ --name`stage1a`Output: `{ "stage": { "arn": "arn:aws:ivs:us-west-2:123456789012:stage/abcdABCDefgh", "autoParticipantRecordingConfiguration": { "mediaTypes": [ "AUDIO_VIDEO" ], "storageConfigurationArn": "arn:aws:ivs:us-west-2:123456789012:storage-configuration/abcdABCDefgh", "thumbnailConfiguration": { "targetIntervalSeconds": 60, "storage": [ "SEQUENTIAL" ], "recordingMode": "INTERVAL" }, "recordingReconnectWindowSeconds": 100, "hlsConfiguration": { "targetSegmentDurationSeconds": 5 }, "recordParticipantReplicas": false }, "endpoints": { "events": "wss://global.events.live-video.net", "rtmp": "rtmp://9x0y8z7s6t5u.global-contribute-staging.live-video.net/app/", "rtmps": "rtmps://9x0y8z7s6t5u.global-contribute-staging.live-video.net:443/app/", "whip": "https://1a2b3c4d5e6f.global-bm.whip.live-video.net" }, "name": "stage1a", "tags": {} } }`For more information, see [Enabling Multiple Hosts on an Amazon IVS Stream](https://docs.aws.amazon.com/ivs/latest/LowLatencyUserGuide/multiple-hosts.html)in the*Amazon IVS Low-Latency Streaming User Guide*.- 
                    For API details, see [UpdateStage](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ivs-realtime/update-stage.html)in*AWS CLI Command Reference*.
 
-