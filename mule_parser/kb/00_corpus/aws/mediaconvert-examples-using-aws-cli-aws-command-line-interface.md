# MediaConvert examples using AWS CLI - AWS Command Line Interface

**Source:** [https://docs.aws.amazon.com/cli/latest/userguide/cli_mediaconvert_code_examples.html](https://docs.aws.amazon.com/cli/latest/userguide/cli_mediaconvert_code_examples.html)

---

The following code examples show you how to perform actions and implement common scenarios by using the AWS Command Line Interface with MediaConvert.

*Actions* are code excerpts from larger programs and must be run in context. While actions show you how to call individual service functions, you can see actions in context in their related scenarios.

Each example includes a link to the complete source code, where you can find instructions on how to set up and run the code in context.

###### Topics

## Actions

    The following code example shows how to use `cancel-job`.

- **AWS CLI**
- 
            
                    **To cancel a job that is in a queue**The following `cancel-job`example cancels the job with ID`1234567891234-abc123`. You can't cancel a job that the service has started processing.`aws mediaconvert cancel-job \ --endpoint-url``https://abcd1234.mediaconvert.region-name-1.amazonaws.com`\ --region`region-name-1`\ --id`1234567891234-abc123`To get your account-specific endpoint, use `describe-endpoints`, or send the command without the endpoint. The service returns an error and your endpoint.For more information, see [Working with AWS Elemental MediaConvert Jobs](https://docs.aws.amazon.com/mediaconvert/latest/ug/working-with-jobs.html)in the*AWS Elemental MediaConvert User Guide*.- 
                    For API details, see [CancelJob](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/mediaconvert/cancel-job.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `create-job-template`.

- **AWS CLI**
- 
            
                    **To create a job template**The following `create-job-template`example creates a job template with the transcoding settings that are specified in the file`job-template.json`that resides on your system.`aws mediaconvert create-job-template \ --endpoint-url``https://abcd1234.mediaconvert.region-name-1.amazonaws.com`\ --region`region-name-1`\ --name`JobTemplate1`\ --cli-input-json`file://~/job-template.json`If you create your job template JSON file by using `get-job-template`and then modifying the file, remove the`JobTemplate`object, but keep the Settings child object inside it. Also, make sure to remove the following key-value pairs:`LastUpdated`,`Arn`,`Type`, and`CreatedAt`. You can specific the category, description, name, and queue either in the JSON file or at the command line.To get your account-specific endpoint, use `describe-endpoints`, or send the command without the endpoint. The service returns an error and your endpoint.If your request is successful, the service returns the JSON specification for the job template that you created. For more information, see [Working with AWS Elemental MediaConvert Job Templates](https://docs.aws.amazon.com/mediaconvert/latest/ug/working-with-job-templates.html)in the*AWS Elemental MediaConvert User Guide*.- 
                    For API details, see [CreateJobTemplate](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/mediaconvert/create-job-template.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `create-job`.

- **AWS CLI**
- 
            
                    **To create a job**The following `create-job`example creates a transcoding job with the settings that are specified in a file`job.json`that resides on the system that you send the command from. This JSON job specification might specify each setting individually, reference a job template, or reference output presets.`aws mediaconvert create-job \ --endpoint-url``https://abcd1234.mediaconvert.region-name-1.amazonaws.com`\ --region`region-name-1`\ --cli-input-json`file://~/job.json`You can use the AWS Elemental MediaConvert console to generate the JSON job specification by choosing your job settings, and then choosing **Show job JSON**at the bottom of the**Job**section.To get your account-specific endpoint, use `describe-endpoints`, or send the command without the endpoint. The service returns an error and your endpoint.If your request is successful, the service returns the JSON job specification that you sent with your request. For more information, see [Working with AWS Elemental MediaConvert Jobs](https://docs.aws.amazon.com/mediaconvert/latest/ug/working-with-jobs.html)in the*AWS Elemental MediaConvert User Guide*.- 
                    For API details, see [CreateJob](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/mediaconvert/create-job.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `create-preset`.

- **AWS CLI**
- 
            
                    **To create a custom output preset**The following `create-preset`example creates a custom output preset based on the output settings that are specified in the file`preset.json`. You can specify the category, description, and name either in the JSON file or at the command line.`aws mediaconvert create-preset \ --endpoint-url``https://abcd1234.mediaconvert.region-name-1.amazonaws.com`--region`region-name-1`\ --cli-input-json`file://~/preset.json`If you create your preset JSON file by using `get-preset`and then modifying the output file, ensure that you remove the following key-value pairs:`LastUpdated`,`Arn`,`Type`, and`CreatedAt`.To get your account-specific endpoint, use `describe-endpoints`, or send the command without the endpoint. The service returns an error and your endpoint.For more information, see [Working with AWS Elemental MediaConvert Output Presets](https://docs.aws.amazon.com/mediaconvert/latest/ug/working-with-presets.html)in the*AWS Elemental MediaConvert User Guide*.- 
                    For API details, see [CreatePreset](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/mediaconvert/create-preset.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `create-queue`.

- **AWS CLI**
- 
            
                    **To create a custom queue**The following `create-queue`example creates a custom transcoding queue.`aws mediaconvert create-queue \ --endpoint-url``https://abcd1234.mediaconvert.region-name-1.amazonaws.com`\ --region`region-name-1`\ --name`Queue1`\ --description`"Keep this queue empty unless job is urgent."`To get your account-specific endpoint, use `describe-endpoints`, or send the command without the endpoint. The service returns an error and your endpoint.Output: `{ "Queue": { "Status": "ACTIVE", "Name": "Queue1", "LastUpdated": 1518034928, "Arn": "arn:aws:mediaconvert:region-name-1:012345678998:queues/Queue1", "Type": "CUSTOM", "CreatedAt": 1518034928, "Description": "Keep this queue empty unless job is urgent." } }`For more information, see [Working with AWS Elemental MediaConvert Queues](https://docs.aws.amazon.com/mediaconvert/latest/ug/working-with-queues.html)in the*AWS Elemental MediaConvert User Guide*.- 
                    For API details, see [CreateQueue](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/mediaconvert/create-queue.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `delete-job-template`.

- **AWS CLI**
- 
            
                    **To delete a job template**The following `delete-job-template`example deletes the specified custom job template.`aws mediaconvert delete-job-template \ --name``"DASH Streaming"`\ --endpoint-url`https://abcd1234.mediaconvert.us-west-2.amazonaws.com`This command produces no output. Run `aws mediaconvert list-job-templates`to confirm that your template was deleted.For more information, see [Working with AWS Elemental MediaConvert Job Templates](https://docs.aws.amazon.com/mediaconvert/latest/ug/working-with-job-templates.html)in the*AWS Elemental MediaConvert User Guide*.- 
                    For API details, see [DeleteJobTemplate](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/mediaconvert/delete-job-template.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `delete-preset`.

- **AWS CLI**
- 
            
                    **To delete a custom on-demand queue**The following `delete-preset`example deletes the specified custom preset.`aws mediaconvert delete-preset \ --name``SimpleMP4`\ --endpoint-url`https://abcd1234.mediaconvert.us-west-2.amazonaws.com`This command produces no output. Run `aws mediaconvert list-presets`to confirm that your preset was deleted.For more information, see [Working with AWS Elemental MediaConvert Output Presets](https://docs.aws.amazon.com/mediaconvert/latest/ug/working-with-presets.html)in the*AWS Elemental MediaConvert User Guide*.- 
                    For API details, see [DeletePreset](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/mediaconvert/delete-preset.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `delete-queue`.

- **AWS CLI**
- 
            
                    **To delete a custom on-demand queue**The following `delete-queue`example deletes the specified custom on-demand queue.You can't delete your default queue. You can't delete a reserved queue that has an active pricing plan or that contains unprocessed jobs. `aws mediaconvert delete-queue \ --name``Customer1`\ --endpoint-url`https://abcd1234.mediaconvert.us-west-2.amazonaws.com`This command produces no output. Run `aws mediaconvert list-queues`to confirm that your queue was deleted.For more information, see [Working with AWS Elemental MediaConvert Queues](https://docs.aws.amazon.com/mediaconvert/latest/ug/working-with-queues.html)in the*AWS Elemental MediaConvert User Guide*.- 
                    For API details, see [DeleteQueue](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/mediaconvert/delete-queue.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `describe-endpoints`.

- **AWS CLI**
- 
            
                    **To get your account-specific endpoint**The following `describe-endpoints`example retrieves the endpoint that you need to send any other request to the service.`aws mediaconvert describe-endpoints`Output: `{ "Endpoints": [ { "Url": "https://abcd1234.mediaconvert.region-name-1.amazonaws.com" } ] }`For more information, see [Getting Started with MediaConvert Using the API](https://docs.aws.amazon.com/mediaconvert/latest/apireference/getting-started.html)in the*AWS Elemental MediaConvert API Reference*.- 
                    For API details, see [DescribeEndpoints](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/mediaconvert/describe-endpoints.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `get-job-template`.

- **AWS CLI**
- 
            
                    **To get details for a job template**The following `get-job-template`example displays the JSON definition of the specified custom job template.`aws mediaconvert get-job-template \ --name``"DASH Streaming"`\ --endpoint-url`https://abcd1234.mediaconvert.us-east-1.amazonaws.com`Output: `{ "JobTemplate": { "StatusUpdateInterval": "SECONDS_60", "LastUpdated": 1568652998, "Description": "Create a DASH streaming ABR stack", "CreatedAt": 1568652998, "Priority": 0, "Name": "DASH Streaming", "Settings": { ...<truncatedforbrevity>... }, "Arn": "arn:aws:mediaconvert:us-west-2:123456789012:jobTemplates/DASH Streaming", "Type": "CUSTOM" } }`For more information, see [Working with AWS Elemental MediaConvert Job Templates](https://docs.aws.amazon.com/mediaconvert/latest/ug/working-with-job-templates.html)in the*AWS Elemental MediaConvert User Guide*.- 
                    For API details, see [GetJobTemplate](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/mediaconvert/get-job-template.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `get-job`.

- **AWS CLI**
- 
            
                    **To get details for a particular job**The following example requests the information for the job with ID `1234567890987-1ab2c3`, which in this example ended in an error.`aws mediaconvert get-job \ --endpoint-url``https://abcd1234.mediaconvert.region-name-1.amazonaws.com`\ --region`region-name-1`\ --id`1234567890987-1ab2c3`To get your account-specific endpoint, use `describe-endpoints`, or send the command without the endpoint. The service returns an error and your endpoint.If your request is successful, the service returns a JSON file with job information, including job settings, any returned errors, and other job data, as follows: `{ "Job": { "Status": "ERROR", "Queue": "arn:aws:mediaconvert:region-name-1:012345678998:queues/Queue1", "Settings": { ...<truncated for brevity>... }, "ErrorMessage": "Unable to open input file [s3://my-input-bucket/file-name.mp4]: [Failed probe/open: [Failed to read data: AssumeRole failed]]", "ErrorCode": 1434, "Role": "arn:aws:iam::012345678998:role/MediaConvertServiceRole", "Arn": "arn:aws:mediaconvert:us-west-1:012345678998:jobs/1234567890987-1ab2c3", "UserMetadata": {}, "Timing": { "FinishTime": 1517442131, "SubmitTime": 1517442103, "StartTime": 1517442104 }, "Id": "1234567890987-1ab2c3", "CreatedAt": 1517442103 } }`For more information, see [Working with AWS Elemental MediaConvert Jobs](https://docs.aws.amazon.com/mediaconvert/latest/ug/working-with-jobs.html)in the*AWS Elemental MediaConvert User Guide*.- 
                    For API details, see [GetJob](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/mediaconvert/get-job.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `get-preset`.

- **AWS CLI**
- 
            
                    **To get details for a particular preset**The following `get-preset`example requests the JSON definition of the specified custom preset.`aws mediaconvert get-preset \ --name``SimpleMP4`\ --endpoint-url`https://abcd1234.mediaconvert.us-west-2.amazonaws.com`Output: `{ "Preset": { "Description": "Creates basic MP4 file. No filtering or preproccessing.", "Arn": "arn:aws:mediaconvert:us-west-2:123456789012:presets/SimpleMP4", "LastUpdated": 1568843141, "Name": "SimpleMP4", "Settings": { "ContainerSettings": { "Mp4Settings": { "FreeSpaceBox": "EXCLUDE", "CslgAtom": "INCLUDE", "MoovPlacement": "PROGRESSIVE_DOWNLOAD" }, "Container": "MP4" }, "AudioDescriptions": [ { "LanguageCodeControl": "FOLLOW_INPUT", "AudioTypeControl": "FOLLOW_INPUT", "CodecSettings": { "AacSettings": { "RawFormat": "NONE", "CodecProfile": "LC", "AudioDescriptionBroadcasterMix": "NORMAL", "SampleRate": 48000, "Bitrate": 96000, "RateControlMode": "CBR", "Specification": "MPEG4", "CodingMode": "CODING_MODE_2_0" }, "Codec": "AAC" } } ], "VideoDescription": { "RespondToAfd": "NONE", "TimecodeInsertion": "DISABLED", "Sharpness": 50, "ColorMetadata": "INSERT", "CodecSettings": { "H264Settings": { "FramerateControl": "INITIALIZE_FROM_SOURCE", "SpatialAdaptiveQuantization": "ENABLED", "Softness": 0, "Telecine": "NONE", "CodecLevel": "AUTO", "QualityTuningLevel": "SINGLE_PASS", "UnregisteredSeiTimecode": "DISABLED", "Slices": 1, "Syntax": "DEFAULT", "GopClosedCadence": 1, "AdaptiveQuantization": "HIGH", "EntropyEncoding": "CABAC", "InterlaceMode": "PROGRESSIVE", "ParControl": "INITIALIZE_FROM_SOURCE", "NumberBFramesBetweenReferenceFrames": 2, "GopSizeUnits": "FRAMES", "RepeatPps": "DISABLED", "CodecProfile": "MAIN", "FieldEncoding": "PAFF", "GopSize": 90.0, "SlowPal": "DISABLED", "SceneChangeDetect": "ENABLED", "GopBReference": "DISABLED", "RateControlMode": "CBR", "FramerateConversionAlgorithm": "DUPLICATE_DROP", "FlickerAdaptiveQuantization": "DISABLED", "DynamicSubGop": "STATIC", "MinIInterval": 0, "TemporalAdaptiveQuantization": "ENABLED", "Bitrate": 400000, "NumberReferenceFrames": 3 }, "Codec": "H_264" }, "AfdSignaling": "NONE", "AntiAlias": "ENABLED", "ScalingBehavior": "DEFAULT", "DropFrameTimecode": "ENABLED" } }, "Type": "CUSTOM", "CreatedAt": 1568841521 } }`For more information, see [Working with AWS Elemental MediaConvert Output Presets](https://docs.aws.amazon.com/mediaconvert/latest/ug/working-with-presets.html)in the*AWS Elemental MediaConvert User Guide*.- 
                    For API details, see [GetPreset](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/mediaconvert/get-preset.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `get-queue`.

- **AWS CLI**
- 
            
                    **To get details for a queue**The following `get-queue`example retrieves the details of the specified custom queue.`aws mediaconvert get-queue \ --name``Customer1`\ --endpoint-url`https://abcd1234.mediaconvert.us-west-2.amazonaws.com`Output: `{ "Queue": { "LastUpdated": 1526428502, "Type": "CUSTOM", "SubmittedJobsCount": 0, "Status": "ACTIVE", "PricingPlan": "ON_DEMAND", "CreatedAt": 1526428502, "ProgressingJobsCount": 0, "Arn": "arn:aws:mediaconvert:us-west-2:123456789012:queues/Customer1", "Name": "Customer1" } }`For more information, see [Working with AWS Elemental MediaConvert Queues](https://docs.aws.amazon.com/mediaconvert/latest/ug/working-with-queues.html)in the*AWS Elemental MediaConvert User Guide*.- 
                    For API details, see [GetQueue](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/mediaconvert/get-queue.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `list-job-templates`.

- **AWS CLI**
- 
            
                    **Example 1: To list your custom job templates**The following `list-job-templates`example lists all custom job templates in the current Region. To list the system job templates, see the next example.`aws mediaconvert list-job-templates \ --endpoint-url``https://abcd1234.mediaconvert.us-west-2.amazonaws.com`Output: `{ "JobTemplates": [ { "Description": "Create a DASH streaming ABR stack", "Arn": "arn:aws:mediaconvert:us-west-2:123456789012:jobTemplates/DASH Streaming", "Name": "DASH Streaming", "LastUpdated": 1568653007, "Priority": 0, "Settings": { ...<truncatedforbrevity>... }, "Type": "CUSTOM", "StatusUpdateInterval": "SECONDS_60", "CreatedAt": 1568653007 }, { "Description": "Create a high-res file", "Arn": "arn:aws:mediaconvert:us-west-2:123456789012:jobTemplates/File", "Name": "File", "LastUpdated": 1568653007, "Priority": 0, "Settings": { ...<truncatedforbrevity>... }, "Type": "CUSTOM", "StatusUpdateInterval": "SECONDS_60", "CreatedAt": 1568653023 } ] }`**Example 2: To list the MediaConvert system job templates**The following `list-job-templates`example lists all system job templates.`aws mediaconvert list-job-templates \ --endpoint-url``https://abcd1234.mediaconvert.us-east-1.amazonaws.com`\ --list-by`SYSTEM`Output: `{ "JobTemplates": [ { "CreatedAt": 1568321779, "Arn": "arn:aws:mediaconvert:us-east-1:123456789012:jobTemplates/System-Generic_Mp4_Hev1_Avc_Aac_Sdr_Qvbr", "Name": "System-Generic_Mp4_Hev1_Avc_Aac_Sdr_Qvbr", "Description": "GENERIC, MP4, AVC + HEV1(HEVC,SDR), AAC, SDR, QVBR", "Category": "GENERIC", "Settings": { "AdAvailOffset": 0, "OutputGroups": [ { "Outputs": [ { "Extension": "mp4", "Preset": "System-Generic_Hd_Mp4_Avc_Aac_16x9_Sdr_1280x720p_30Hz_5Mbps_Qvbr_Vq9", "NameModifier": "_Generic_Hd_Mp4_Avc_Aac_16x9_Sdr_1280x720p_30Hz_5000Kbps_Qvbr_Vq9" }, { "Extension": "mp4", "Preset": "System-Generic_Hd_Mp4_Avc_Aac_16x9_Sdr_1920x1080p_30Hz_10Mbps_Qvbr_Vq9", "NameModifier": "_Generic_Hd_Mp4_Avc_Aac_16x9_Sdr_1920x1080p_30Hz_10000Kbps_Qvbr_Vq9" }, { "Extension": "mp4", "Preset": "System-Generic_Sd_Mp4_Avc_Aac_16x9_Sdr_640x360p_30Hz_0.8Mbps_Qvbr_Vq7", "NameModifier": "_Generic_Sd_Mp4_Avc_Aac_16x9_Sdr_640x360p_30Hz_800Kbps_Qvbr_Vq7" }, { "Extension": "mp4", "Preset": "System-Generic_Hd_Mp4_Hev1_Aac_16x9_Sdr_1280x720p_30Hz_4Mbps_Qvbr_Vq9", "NameModifier": "_Generic_Hd_Mp4_Hev1_Aac_16x9_Sdr_1280x720p_30Hz_4000Kbps_Qvbr_Vq9" }, { "Extension": "mp4", "Preset": "System-Generic_Hd_Mp4_Hev1_Aac_16x9_Sdr_1920x1080p_30Hz_8Mbps_Qvbr_Vq9", "NameModifier": "_Generic_Hd_Mp4_Hev1_Aac_16x9_Sdr_1920x1080p_30Hz_8000Kbps_Qvbr_Vq9" }, { "Extension": "mp4", "Preset": "System-Generic_Uhd_Mp4_Hev1_Aac_16x9_Sdr_3840x2160p_30Hz_12Mbps_Qvbr_Vq9", "NameModifier": "_Generic_Uhd_Mp4_Hev1_Aac_16x9_Sdr_3840x2160p_30Hz_12000Kbps_Qvbr_Vq9" } ], "OutputGroupSettings": { "FileGroupSettings": { }, "Type": "FILE_GROUP_SETTINGS" }, "Name": "File Group" } ] }, "Type": "SYSTEM", "LastUpdated": 1568321779 }, ...<truncatedforbrevity>... ] }`For more information, see [Working with AWS Elemental MediaConvert Job Templates](https://docs.aws.amazon.com/mediaconvert/latest/ug/working-with-job-templates.html)in the*AWS Elemental MediaConvert User Guide*.- 
                    For API details, see [ListJobTemplates](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/mediaconvert/list-job-templates.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `list-jobs`.

- **AWS CLI**
- 
            
                    **To get details for all jobs in a region**The following example requests the information for all of your jobs in the specified region. `aws mediaconvert list-jobs \ --endpoint-url``https://abcd1234.mediaconvert.region-name-1.amazonaws.com`\ --region`region-name-1`To get your account-specific endpoint, use `describe-endpoints`, or send the command without the endpoint. The service returns an error and your endpoint.For more information, see [Working with AWS Elemental MediaConvert Jobs](https://docs.aws.amazon.com/mediaconvert/latest/ug/working-with-jobs.html)in the*AWS Elemental MediaConvert User Guide*.- 
                    For API details, see [ListJobs](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/mediaconvert/list-jobs.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `list-presets`.

- **AWS CLI**
- 
            
                    **Example 1: To list your custom output presets**The following `list-presets`example lists your custom output presets. To list the system presets, see the next example.`aws mediaconvert list-presets \ --endpoint-url``https://abcd1234.mediaconvert.us-west-2.amazonaws.com`Output: `{ "Presets": [ { "Name": "SimpleMP4", "CreatedAt": 1568841521, "Settings": { ...... }, "Arn": "arn:aws:mediaconvert:us-east-1:003235472598:presets/SimpleMP4", "Type": "CUSTOM", "LastUpdated": 1568843141, "Description": "Creates basic MP4 file. No filtering or preproccessing." }, { "Name": "SimpleTS", "CreatedAt": 1568843113, "Settings": { ... truncated for brevity ... }, "Arn": "arn:aws:mediaconvert:us-east-1:003235472598:presets/SimpleTS", "Type": "CUSTOM", "LastUpdated": 1568843113, "Description": "Create a basic transport stream." } ] }`**Example 2: To list the system output presets**The following `list-presets`example lists the available MediaConvert system presets. To list your custom presets, see the previous example.`aws mediaconvert list-presets \ --list-by``SYSTEM`\ --endpoint-url`https://abcd1234.mediaconvert.us-west-2.amazonaws.com`Output: `{ "Presets": [ { "Arn": "arn:aws:mediaconvert:us-west-2:123456789012:presets/System-Avc_16x9_1080p_29_97fps_8500kbps", "Name": "System-Avc_16x9_1080p_29_97fps_8500kbps", "CreatedAt": 1568321789, "Description": "Wifi, 1920x1080, 16:9, 29.97fps, 8500kbps", "LastUpdated": 1568321789, "Type": "SYSTEM", "Category": "HLS", "Settings": { ...<output settings removed for brevity>... } }, ...<list of presets shortened for brevity>... { "Arn": "arn:aws:mediaconvert:us-east-1:123456789012:presets/System-Xdcam_HD_1080i_29_97fps_35mpbs", "Name": "System-Xdcam_HD_1080i_29_97fps_35mpbs", "CreatedAt": 1568321790, "Description": "XDCAM MPEG HD, 1920x1080i, 29.97fps, 35mbps", "LastUpdated": 1568321790, "Type": "SYSTEM", "Category": "MXF", "Settings": { ...<output settings removed for brevity>... } } ] }`For more information, see [Working with AWS Elemental MediaConvert Output Presets](https://docs.aws.amazon.com/mediaconvert/latest/ug/working-with-presets.html)in the*AWS Elemental MediaConvert User Guide*.- 
                    For API details, see [ListPresets](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/mediaconvert/list-presets.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `list-queues`.

- **AWS CLI**
- 
            
                    **To list your queues**The following `list-queues`example lists all of your MediaConvert queues.`aws mediaconvert list-queues \ --endpoint-url``https://abcd1234.mediaconvert.us-west-2.amazonaws.com`Output: `{ "Queues": [ { "PricingPlan": "ON_DEMAND", "Type": "SYSTEM", "Status": "ACTIVE", "CreatedAt": 1503451595, "Name": "Default", "SubmittedJobsCount": 0, "ProgressingJobsCount": 0, "Arn": "arn:aws:mediaconvert:us-west-2:123456789012:queues/Default", "LastUpdated": 1534549158 }, { "PricingPlan": "ON_DEMAND", "Type": "CUSTOM", "Status": "ACTIVE", "CreatedAt": 1537460025, "Name": "Customer1", "SubmittedJobsCount": 0, "Description": "Jobs we run for our cusotmer.", "ProgressingJobsCount": 0, "Arn": "arn:aws:mediaconvert:us-west-2:123456789012:queues/Customer1", "LastUpdated": 1537460025 }, { "ProgressingJobsCount": 0, "Status": "ACTIVE", "Name": "transcode-library", "SubmittedJobsCount": 0, "LastUpdated": 1564066204, "ReservationPlan": { "Status": "ACTIVE", "ReservedSlots": 1, "PurchasedAt": 1564066203, "Commitment": "ONE_YEAR", "ExpiresAt": 1595688603, "RenewalType": "EXPIRE" }, "PricingPlan": "RESERVED", "Arn": "arn:aws:mediaconvert:us-west-2:123456789012:queues/transcode-library", "Type": "CUSTOM", "CreatedAt": 1564066204 } ] }`For more information, see [Working with AWS Elemental MediaConvert Queues](https://docs.aws.amazon.com/mediaconvert/latest/ug/working-with-queues.html)in the*AWS Elemental MediaConvert User Guide*.- 
                    For API details, see [ListQueues](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/mediaconvert/list-queues.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `list-tags-for-resource`.

- **AWS CLI**
- 
            
                    **To list the tags on a MediaConvert queue, job template, or output preset**The following `list-tags-for-resource`example lists the tags on the specified output preset.`aws mediaconvert list-tags-for-resource \ --arn``arn:aws:mediaconvert:us-west-2:123456789012:presets/SimpleMP4`\ --endpoint-url`https://abcd1234.mediaconvert.us-west-2.amazonaws.com`Output: `{ "ResourceTags": { "Tags": { "customer": "zippyVideo" }, "Arn": "arn:aws:mediaconvert:us-west-2:123456789012:presets/SimpleMP4" } }`For more information, see [Tagging AWS Elemental MediaConvert Queues, Job Templates, and Output Presets](https://docs.aws.amazon.com/mediaconvert/latest/ug/tagging-queues-templates-presets.html)in the*AWS Elemental MediaConvert User Guide*.- 
                    For API details, see [ListTagsForResource](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/mediaconvert/list-tags-for-resource.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `update-job-template`.

- **AWS CLI**
- 
            
                    **To change a job template**The following `update-job-template`example replaces the JSON definition of the specified custom job template with the JSON definition in the provided file.aws mediaconvert update-job-template --name File1 --endpoint-url https://abcd1234.mediaconvert.us-west-2.amazonaws.com --cli-input-json file://~/job-template-update.json Contents of `job-template-update.json`:`{ "Description": "A simple job template that generates a single file output.", "Queue": "arn:aws:mediaconvert:us-east-1:012345678998:queues/Default", "Name": "SimpleFile", "Settings": { "OutputGroups": [ { "Name": "File Group", "Outputs": [ { "ContainerSettings": { "Container": "MP4", "Mp4Settings": { "CslgAtom": "INCLUDE", "FreeSpaceBox": "EXCLUDE", "MoovPlacement": "PROGRESSIVE_DOWNLOAD" } }, "VideoDescription": { "ScalingBehavior": "DEFAULT", "TimecodeInsertion": "DISABLED", "AntiAlias": "ENABLED", "Sharpness": 50, "CodecSettings": { "Codec": "H_264", "H264Settings": { "InterlaceMode": "PROGRESSIVE", "NumberReferenceFrames": 3, "Syntax": "DEFAULT", "Softness": 0, "GopClosedCadence": 1, "GopSize": 90, "Slices": 1, "GopBReference": "DISABLED", "SlowPal": "DISABLED", "SpatialAdaptiveQuantization": "ENABLED", "TemporalAdaptiveQuantization": "ENABLED", "FlickerAdaptiveQuantization": "DISABLED", "EntropyEncoding": "CABAC", "Bitrate": 400000, "FramerateControl": "INITIALIZE_FROM_SOURCE", "RateControlMode": "CBR", "CodecProfile": "MAIN", "Telecine": "NONE", "MinIInterval": 0, "AdaptiveQuantization": "HIGH", "CodecLevel": "AUTO", "FieldEncoding": "PAFF", "SceneChangeDetect": "ENABLED", "QualityTuningLevel": "SINGLE_PASS", "FramerateConversionAlgorithm": "DUPLICATE_DROP", "UnregisteredSeiTimecode": "DISABLED", "GopSizeUnits": "FRAMES", "ParControl": "INITIALIZE_FROM_SOURCE", "NumberBFramesBetweenReferenceFrames": 2, "RepeatPps": "DISABLED", "DynamicSubGop": "STATIC" } }, "AfdSignaling": "NONE", "DropFrameTimecode": "ENABLED", "RespondToAfd": "NONE", "ColorMetadata": "INSERT" }, "AudioDescriptions": [ { "AudioTypeControl": "FOLLOW_INPUT", "CodecSettings": { "Codec": "AAC", "AacSettings": { "AudioDescriptionBroadcasterMix": "NORMAL", "Bitrate": 96000, "RateControlMode": "CBR", "CodecProfile": "LC", "CodingMode": "CODING_MODE_2_0", "RawFormat": "NONE", "SampleRate": 48000, "Specification": "MPEG4" } }, "LanguageCodeControl": "FOLLOW_INPUT" } ] } ], "OutputGroupSettings": { "Type": "FILE_GROUP_SETTINGS", "FileGroupSettings": {} } } ], "AdAvailOffset": 0 }, "StatusUpdateInterval": "SECONDS_60", "Priority": 0 }`The system returns the JSON payload that you send with your request, even when the request results in an error. Therefore, the JSON returned is not necessarily the new definition of the job template. Because the JSON payload can be long, you might need to scroll up to see any error messages. For more information, see [Working with AWS Elemental MediaConvert Job Templates](https://docs.aws.amazon.com/mediaconvert/latest/ug/working-with-job-templates.html)in the*AWS Elemental MediaConvert User Guide*.- 
                    For API details, see [UpdateJobTemplate](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/mediaconvert/update-job-template.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `update-preset`.

- **AWS CLI**
- 
            
                    **To change a preset**The following `update-preset`example replaces the description for the specified preset.`aws mediaconvert update-preset \ --name Customer1 \ --description "New description text." --endpoint-url https://abcd1234.mediaconvert.us-west-2.amazonaws.com`This command produces no output. Output: `{ "Preset": { "Arn": "arn:aws:mediaconvert:us-east-1:003235472598:presets/SimpleMP4", "Settings": { ...<output settings removed for brevity>... }, "Type": "CUSTOM", "LastUpdated": 1568938411, "Description": "New description text.", "Name": "SimpleMP4", "CreatedAt": 1568938240 } }`For more information, see [Working with AWS Elemental MediaConvert Output Presets](https://docs.aws.amazon.com/mediaconvert/latest/ug/working-with-presets.html)in the*AWS Elemental MediaConvert User Guide*.- 
                    For API details, see [UpdatePreset](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/mediaconvert/update-preset.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `update-queue`.

- **AWS CLI**
- 
            
                    **To change a queue**The following `update-queue`example pauses the specified queue, by changing its status to`PAUSED`.`aws mediaconvert update-queue \ --name``Customer1`\ --status`PAUSED`--endpoint-url`https://abcd1234.mediaconvert.us-west-2.amazonaws.com`Output: `{ "Queue": { "LastUpdated": 1568839845, "Status": "PAUSED", "ProgressingJobsCount": 0, "CreatedAt": 1526428516, "Arn": "arn:aws:mediaconvert:us-west-1:123456789012:queues/Customer1", "Name": "Customer1", "SubmittedJobsCount": 0, "PricingPlan": "ON_DEMAND", "Type": "CUSTOM" } }`For more information, see [Working with AWS Elemental MediaConvert Queues](https://docs.aws.amazon.com/mediaconvert/latest/ug/working-with-queues.html)in the*AWS Elemental MediaConvert User Guide*.- 
                    For API details, see [UpdateQueue](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/mediaconvert/update-queue.html)in*AWS CLI Command Reference*.
 
-