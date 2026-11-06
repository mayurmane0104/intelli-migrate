# Amazon Pinpoint examples using AWS CLI - AWS Command Line Interface

**Source:** [https://docs.aws.amazon.com/cli/latest/userguide/cli_pinpoint_code_examples.html](https://docs.aws.amazon.com/cli/latest/userguide/cli_pinpoint_code_examples.html)

---

The following code examples show you how to perform actions and implement common scenarios by using the AWS Command Line Interface with Amazon Pinpoint.

*Actions* are code excerpts from larger programs and must be run in context. While actions show you how to call individual service functions, you can see actions in context in their related scenarios.

Each example includes a link to the complete source code, where you can find instructions on how to set up and run the code in context.

###### Topics

## Actions

    The following code example shows how to use `create-app`.

- **AWS CLI**
- 
            
                    **Example 1: To create an application**The following `create-app`example creates a new application (project).`aws pinpoint create-app \ --create-application-request``Name=ExampleCorp`Output: `{ "ApplicationResponse": { "Arn": "arn:aws:mobiletargeting:us-west-2:AIDACKCEVSQ6C2EXAMPLE:apps/810c7aab86d42fb2b56c8c966example", "Id": "810c7aab86d42fb2b56c8c966example", "Name": "ExampleCorp", "tags": {} } }`**Example 2: To create an application that is tagged**The following `create-app`example creates a new application (project) and associates a tag (key and value) with the application.`aws pinpoint create-app \ --create-application-request Name=ExampleCorp,tags={"Stack"="Test"}`Output: `{ "ApplicationResponse": { "Arn": "arn:aws:mobiletargeting:us-west-2:AIDACKCEVSQ6C2EXAMPLE:apps/810c7aab86d42fb2b56c8c966example", "Id": "810c7aab86d42fb2b56c8c966example", "Name": "ExampleCorp", "tags": { "Stack": "Test" } } }`- 
                    For API details, see [CreateApp](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/pinpoint/create-app.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `create-sms-template`.

- **AWS CLI**
- 
            
                    **Creates a message template for messages that are sent through the SMS channel**The following `create-sms-template`example creates a SMS message template.`aws pinpoint create-sms-template \ --template-name``TestTemplate`\ --sms-template-request`file://myfile.json`\ --region`us-east-1`Contents of `myfile.json`:`{ "Body": "hello\n how are you?\n food is good", "TemplateDescription": "Test SMS Template" }`Output: `{ "CreateTemplateMessageBody": { "Arn": "arn:aws:mobiletargeting:us-east-1:AIDACKCEVSQ6C2EXAMPLE:templates/TestTemplate/SMS", "Message": "Created", "RequestID": "8c36b17f-a0b0-400f-ac21-29e9b62a975d" } }`For more information, see [Amazon Pinpoint message templates](https://docs.aws.amazon.com/pinpoint/latest/userguide/messages-templates.html)in the*Amazon Pinpoint User Guide*.- 
                    For API details, see [CreateSmsTemplate](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/pinpoint/create-sms-template.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `delete-app`.

- **AWS CLI**
- 
            
                    **To delete an application**The following `delete-app`example deletes an application (project).`aws pinpoint delete-app \ --application-id``810c7aab86d42fb2b56c8c966example`Output: `{ "ApplicationResponse": { "Arn": "arn:aws:mobiletargeting:us-west-2:AIDACKCEVSQ6C2EXAMPLE:apps/810c7aab86d42fb2b56c8c966example", "Id": "810c7aab86d42fb2b56c8c966example", "Name": "ExampleCorp", "tags": {} } }`- 
                    For API details, see [DeleteApp](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/pinpoint/delete-app.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `get-apns-channel`.

- **AWS CLI**
- 
            
                    **To retrieve information about the status and settings of the APNs channel for an application**The following `get-apns-channel`example retrieves information about the status and settings of the APNs channel for an application.`aws pinpoint get-apns-channel \ --application-id``9ab1068eb0a6461c86cce7f27ce0efd7`\ --region`us-east-1`Output: `{ "APNSChannelResponse": { "ApplicationId": "9ab1068eb0a6461c86cce7f27ce0efd7", "CreationDate": "2019-05-09T21:54:45.082Z", "DefaultAuthenticationMethod": "CERTIFICATE", "Enabled": true, "HasCredential": true, "HasTokenKey": false, "Id": "apns", "IsArchived": false, "LastModifiedDate": "2019-05-09T22:04:01.067Z", "Platform": "APNS", "Version": 2 } }`- 
                    For API details, see [GetApnsChannel](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/pinpoint/get-apns-channel.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `get-app`.

- **AWS CLI**
- 
            
                    **To retrieve information about an application (project)**The following `get-app`example retrieves information about an application (project).`aws pinpoint get-app \ --application-id``810c7aab86d42fb2b56c8c966example`\ --region`us-east-1`Output: `{ "ApplicationResponse": { "Arn": "arn:aws:mobiletargeting:us-east-1:AIDACKCEVSQ6C2EXAMPLE:apps/810c7aab86d42fb2b56c8c966example", "Id": "810c7aab86d42fb2b56c8c966example", "Name": "ExampleCorp", "tags": { "Year": "2019", "Stack": "Production" } } }`- 
                    For API details, see [GetApp](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/pinpoint/get-app.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `get-apps`.

- **AWS CLI**
- 
            
                    **To retrieve information about all of your applications**The following `get-apps`example retrieves information about all of your applications (projects).`aws pinpoint get-apps`Output: `{ "ApplicationsResponse": { "Item": [ { "Arn": "arn:aws:mobiletargeting:us-west-2:AIDACKCEVSQ6C2EXAMPLE:apps/810c7aab86d42fb2b56c8c966example", "Id": "810c7aab86d42fb2b56c8c966example", "Name": "ExampleCorp", "tags": { "Year": "2019", "Stack": "Production" } }, { "Arn": "arn:aws:mobiletargeting:us-west-2:AIDACKCEVSQ6C2EXAMPLE:apps/42d8c7eb0990a57ba1d5476a3example", "Id": "42d8c7eb0990a57ba1d5476a3example", "Name": "AnyCompany", "tags": {} }, { "Arn": "arn:aws:mobiletargeting:us-west-2:AIDACKCEVSQ6C2EXAMPLE:apps/80f5c382b638ffe5ad12376bbexample", "Id": "80f5c382b638ffe5ad12376bbexample", "Name": "ExampleCorp_Test", "tags": { "Year": "2019", "Stack": "Test" } } ], "NextToken": "eyJDcmVhdGlvbkRhdGUiOiIyMDE5LTA3LTE2VDE0OjM4OjUzLjkwM1oiLCJBY2NvdW50SWQiOiI1MTIzOTcxODM4NzciLCJBcHBJZCI6Ijk1ZTM2MGRiMzBkMjQ1ZjRiYTYwYjhlMzllMzZlNjZhIn0" } }`The presence of the `NextToken`response value indicates that there is more output available. Call the command again and supply that value as the`NextToken`input parameter.- 
                    For API details, see [GetApps](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/pinpoint/get-apps.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `get-campaign`.

- **AWS CLI**
- 
            
                    **To retrieve information about the status, configuration, and other settings for a campaign**The following `get-campaign`example retrieves information about the status, configuration, and other settings for a campaign.`aws pinpoint get-campaign \ --application-id``6e0b7591a90841d2b5d93fa11143e5a7`\ --campaign-id`a1e63c6cc0eb43ed826ffcc3cc90b30d`\ --region`us-east-1`Output: `{ "CampaignResponse": { "AdditionalTreatments": [], "ApplicationId": "6e0b7591a90841d2b5d93fa11143e5a7", "Arn": "arn:aws:mobiletargeting:us-east-1:AIDACKCEVSQ6C2EXAMPLE:apps/6e0b7591a90841d2b5d93fa11143e5a7/campaigns/a1e63c6cc0eb43ed826ffcc3cc90b30d", "CreationDate": "2019-10-08T18:40:16.581Z", "Description": " ", "HoldoutPercent": 0, "Id": "a1e63c6cc0eb43ed826ffcc3cc90b30d", "IsPaused": false, "LastModifiedDate": "2019-10-08T18:40:16.581Z", "Limits": { "Daily": 0, "MaximumDuration": 60, "MessagesPerSecond": 50, "Total": 0 }, "MessageConfiguration": { "EmailMessage": { "FromAddress": "sender@example.com", "HtmlBody": "<!DOCTYPE html>\n <html lang=\"en\">\n <head>\n <meta http-equiv=\"Content-Type\" content=\"text/html; charset=utf-8\" />\n</head>\n<body>Hello</body>\n</html>", "Title": "PinpointDemo" } }, "Name": "MyCampaign", "Schedule": { "IsLocalTime": false, "StartTime": "IMMEDIATE", "Timezone": "utc" }, "SegmentId": "b66c9e42f71444b2aa2e0ffc1df28f60", "SegmentVersion": 1, "State": { "CampaignStatus": "COMPLETED" }, "tags": {}, "TemplateConfiguration": {}, "Version": 1 } }`- 
                    For API details, see [GetCampaign](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/pinpoint/get-campaign.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `get-campaigns`.

- **AWS CLI**
- 
            
                    **To retrieves information about the status, configuration, and other settings for all the campaigns that are associated with an application**The following `get-campaigns`example retrieves information about the status, configuration, and other settings for all the campaigns that are associated with an application.`aws pinpoint get-campaigns \ --application-id``6e0b7591a90841d2b5d93fa11143e5a7`\ --region`us-east-1`Output: `{ "CampaignsResponse": { "Item": [ { "AdditionalTreatments": [], "ApplicationId": "6e0b7591a90841d2b5d93fa11143e5a7", "Arn": "arn:aws:mobiletargeting:us-east-1:AIDACKCEVSQ6C2EXAMPLE:apps/6e0b7591a90841d2b5d93fa11143e5a7/campaigns/7e1280344c8f4a9aa40a00b006fe44f1", "CreationDate": "2019-10-08T18:40:22.905Z", "Description": " ", "HoldoutPercent": 0, "Id": "7e1280344c8f4a9aa40a00b006fe44f1", "IsPaused": false, "LastModifiedDate": "2019-10-08T18:40:22.905Z", "Limits": {}, "MessageConfiguration": { "EmailMessage": { "FromAddress": "sender@example.com", "HtmlBody": "<!DOCTYPE html>\n <html lang=\"en\">\n <head>\n <meta http-equiv=\"Content-Type\" content=\"text/html; charset=utf-8\" />\n</head>\n<body>Hello</body>\n</html>", "Title": "PInpointDemo Test" } }, "Name": "MyCampaign1", "Schedule": { "IsLocalTime": false, "QuietTime": {}, "StartTime": "IMMEDIATE", "Timezone": "UTC" }, "SegmentId": "b66c9e42f71444b2aa2e0ffc1df28f60", "SegmentVersion": 1, "State": { "CampaignStatus": "COMPLETED" }, "tags": {}, "TemplateConfiguration": {}, "Version": 1 }, { "AdditionalTreatments": [], "ApplicationId": "6e0b7591a90841d2b5d93fa11143e5a7", "Arn": "arn:aws:mobiletargeting:us-east-1:AIDACKCEVSQ6C2EXAMPLE:apps/6e0b7591a90841d2b5d93fa11143e5a7/campaigns/a1e63c6cc0eb43ed826ffcc3cc90b30d", "CreationDate": "2019-10-08T18:40:16.581Z", "Description": " ", "HoldoutPercent": 0, "Id": "a1e63c6cc0eb43ed826ffcc3cc90b30d", "IsPaused": false, "LastModifiedDate": "2019-10-08T18:40:16.581Z", "Limits": { "Daily": 0, "MaximumDuration": 60, "MessagesPerSecond": 50, "Total": 0 }, "MessageConfiguration": { "EmailMessage": { "FromAddress": "sender@example.com", "HtmlBody": "<!DOCTYPE html>\n <html lang=\"en\">\n <head>\n <meta http-equiv=\"Content-Type\" content=\"text/html; charset=utf-8\" />\n</head>\n<body>Demo</body>\n</html>", "Title": "PinpointDemo" } }, "Name": "MyCampaign2", "Schedule": { "IsLocalTime": false, "StartTime": "IMMEDIATE", "Timezone": "utc" }, "SegmentId": "b66c9e42f71444b2aa2e0ffc1df28f60", "SegmentVersion": 1, "State": { "CampaignStatus": "COMPLETED" }, "tags": {}, "TemplateConfiguration": {}, "Version": 1 } ] } }`- 
                    For API details, see [GetCampaigns](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/pinpoint/get-campaigns.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `get-channels`.

- **AWS CLI**
- 
            
                    **To retrieves information about the history and status of each channel for an application**The following `get-channels`example retrieves information about the history and status of each channel for an application.`aws pinpoint get-channels \ --application-id``6e0b7591a90841d2b5d93fa11143e5a7`\ --region`us-east-1`Output: `{ "ChannelsResponse": { "Channels": { "GCM": { "ApplicationId": "6e0b7591a90841d2b5d93fa11143e5a7", "CreationDate": "2019-10-08T18:28:23.182Z", "Enabled": true, "HasCredential": true, "Id": "gcm", "IsArchived": false, "LastModifiedDate": "2019-10-08T18:28:23.182Z", "Version": 1 }, "SMS": { "ApplicationId": "6e0b7591a90841d2b5d93fa11143e5a7", "CreationDate": "2019-10-08T18:39:18.511Z", "Enabled": true, "Id": "sms", "IsArchived": false, "LastModifiedDate": "2019-10-08T18:39:18.511Z", "Version": 1 }, "EMAIL": { "ApplicationId": "6e0b7591a90841d2b5d93fa11143e5a7", "CreationDate": "2019-10-08T18:27:23.990Z", "Enabled": true, "Id": "email", "IsArchived": false, "LastModifiedDate": "2019-10-08T18:27:23.990Z", "Version": 1 }, "IN_APP": { "Enabled": true, "IsArchived": false, "Version": 0 } } } }`- 
                    For API details, see [GetChannels](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/pinpoint/get-channels.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `get-email-channel`.

- **AWS CLI**
- 
            
                    **To retrieve information about the status and settings of the Email channel for an application**The following `get-email-channel`example retrieves status and settings of the Email channel for an application.`aws pinpoint get-email-channel \ --application-id``6e0b7591a90841d2b5d93fa11143e5a7`\ --region`us-east-1`Output: `{ "EmailChannelResponse": { "ApplicationId": "6e0b7591a90841d2b5d93fa11143e5a7", "CreationDate": "2019-10-08T18:27:23.990Z", "Enabled": true, "FromAddress": "sender@example.com", "Id": "email", "Identity": "arn:aws:ses:us-east-1:AIDACKCEVSQ6C2EXAMPLE:identity/sender@example.com", "IsArchived": false, "LastModifiedDate": "2019-10-08T18:27:23.990Z", "MessagesPerSecond": 1, "Platform": "EMAIL", "RoleArn": "arn:aws:iam::AIDACKCEVSQ6C2EXAMPLE:role/pinpoint-events", "Version": 1 } }`- 
                    For API details, see [GetEmailChannel](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/pinpoint/get-email-channel.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `get-endpoint`.

- **AWS CLI**
- 
            
                    **To retrieve information about the settings and attributes of a specific endpoint for an application**The following `get-endpoint`example retrieves information about the settings and attributes of a specific endpoint for an application.`aws pinpoint get-endpoint \ --application-id``611e3e3cdd47474c9c1399a505665b91`\ --endpoint-id`testendpoint`\ --region`us-east-1`Output: `{ "EndpointResponse": { "Address": "+11234567890", "ApplicationId": "611e3e3cdd47474c9c1399a505665b91", "Attributes": {}, "ChannelType": "SMS", "CohortId": "63", "CreationDate": "2019-01-28T23:55:11.534Z", "EffectiveDate": "2021-08-06T00:04:51.763Z", "EndpointStatus": "ACTIVE", "Id": "testendpoint", "Location": { "Country": "USA" }, "Metrics": { "SmsDelivered": 1.0 }, "OptOut": "ALL", "RequestId": "a204b1f2-7e26-48a7-9c80-b49a2143489d", "User": { "UserAttributes": { "Age": [ "24" ] }, "UserId": "testuser" } } }`- 
                    For API details, see [GetEndpoint](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/pinpoint/get-endpoint.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `get-gcm-channel`.

- **AWS CLI**
- 
            
                    **To retrieve information about the status and settings of the GCM channel for an application**The following `get-gcm-channel`example retrieves information about the status and settings of the GCM channel for an application.`aws pinpoint get-gcm-channel \ --application-id``6e0b7591a90841d2b5d93fa11143e5a7`\ --region`us-east-1`Output: `{ "GCMChannelResponse": { "ApplicationId": "6e0b7591a90841d2b5d93fa11143e5a7", "CreationDate": "2019-10-08T18:28:23.182Z", "Enabled": true, "HasCredential": true, "Id": "gcm", "IsArchived": false, "LastModifiedDate": "2019-10-08T18:28:23.182Z", "Platform": "GCM", "Version": 1 } }`- 
                    For API details, see [GetGcmChannel](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/pinpoint/get-gcm-channel.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `get-sms-channel`.

- **AWS CLI**
- 
            
                    **To retrieve information about the status and settings of the SMS channel for an application**The following `get-sms-channel`example retrieves status and settings of the sms channel for an application.`aws pinpoint get-sms-channel \ --application-id``6e0b7591a90841d2b5d93fa11143e5a7`\ --region`us-east-1`Output: `{ "SMSChannelResponse": { "ApplicationId": "6e0b7591a90841d2b5d93fa11143e5a7", "CreationDate": "2019-10-08T18:39:18.511Z", "Enabled": true, "Id": "sms", "IsArchived": false, "LastModifiedDate": "2019-10-08T18:39:18.511Z", "Platform": "SMS", "PromotionalMessagesPerSecond": 20, "TransactionalMessagesPerSecond": 20, "Version": 1 } }`- 
                    For API details, see [GetSmsChannel](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/pinpoint/get-sms-channel.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `get-sms-template`.

- **AWS CLI**
- 
            
                    **Retrieves the content and settings of a message template for messages that are sent through the SMS channel**The following `get-sms-template`example retrieves the content and settings of a SMS message template.`aws pinpoint get-sms-template \ --template-name``TestTemplate`\ --region`us-east-1`Output: `{ "SMSTemplateResponse": { "Arn": "arn:aws:mobiletargeting:us-east-1:AIDACKCEVSQ6C2EXAMPLE:templates/TestTemplate/SMS", "Body": "hello\n how are you?\n food is good", "CreationDate": "2023-06-20T21:37:30.124Z", "LastModifiedDate": "2023-06-20T21:37:30.124Z", "tags": {}, "TemplateDescription": "Test SMS Template", "TemplateName": "TestTemplate", "TemplateType": "SMS", "Version": "1" } }`For more information, see [Amazon Pinpoint message templates](https://docs.aws.amazon.com/pinpoint/latest/userguide/messages-templates.html)in the*Amazon Pinpoint User Guide*.- 
                    For API details, see [GetSmsTemplate](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/pinpoint/get-sms-template.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `get-voice-channel`.

- **AWS CLI**
- 
            
                    **To retrieve information about the status and settings of the voice channel for an application**The following `get-voice-channel`example retrieves status and settings of the voice channel for an application.`aws pinpoint get-voice-channel \ --application-id``6e0b7591a90841d2b5d93fa11143e5a7`\ --region`us-east-1`Output: `{ "VoiceChannelResponse": { "ApplicationId": "6e0b7591a90841d2b5d93fa11143e5a7", "CreationDate": "2022-04-28T00:17:03.836Z", "Enabled": true, "Id": "voice", "IsArchived": false, "LastModifiedDate": "2022-04-28T00:17:03.836Z", "Platform": "VOICE", "Version": 1 } }`- 
                    For API details, see [GetVoiceChannel](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/pinpoint/get-voice-channel.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `list-tags-for-resource`.

- **AWS CLI**
- 
            
                    **To retrieve a list of tags for a resource**The following `list-tags-for-resource`example retrieves all the tags (key names and values) that are associated with the specified resource.`aws pinpoint list-tags-for-resource \ --resource-arn``arn:aws:mobiletargeting:us-west-2:AIDACKCEVSQ6C2EXAMPLE:apps/810c7aab86d42fb2b56c8c966example`Output: `{ "TagsModel": { "tags": { "Year": "2019", "Stack": "Production" } } }`For more information, see 'Tagging Amazon Pinpoint Resources <https://docs.aws.amazon.com/pinpoint/latest/developerguide/tagging-resources.html>'__ in the *Amazon Pinpoint Developer Guide*.- 
                    For API details, see [ListTagsForResource](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/pinpoint/list-tags-for-resource.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `phone-number-validate`.

- **AWS CLI**
- 
            
                    **Retrieves information about a phone number**The following `phone-number-validate`retrieves information about a phone number.`aws pinpoint phone-number-validate \ --number-validate-request PhoneNumber="+12065550142" \ --region``us-east-1`Output: `{ "NumberValidateResponse": { "Carrier": "ExampleCorp Mobile", "City": "Seattle", "CleansedPhoneNumberE164": "+12065550142", "CleansedPhoneNumberNational": "2065550142", "Country": "United States", "CountryCodeIso2": "US", "CountryCodeNumeric": "1", "OriginalPhoneNumber": "+12065550142", "PhoneType": "MOBILE", "PhoneTypeCode": 0, "Timezone": "America/Los_Angeles", "ZipCode": "98101" } }`For more information, see [Amazon Pinpoint SMS channel](https://docs.aws.amazon.com/pinpoint/latest/userguide/channels-sms.html)in the*Amazon Pinpoint User Guide*.- 
                    For API details, see [PhoneNumberValidate](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/pinpoint/phone-number-validate.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `send-messages`.

- **AWS CLI**
- 
            
                    **To send SMS message using the endpoint of an application**The following `send-messages`example sends a direct message for an application with an endpoint.`aws pinpoint send-messages \ --application-id``611e3e3cdd47474c9c1399a505665b91`\ --message-request`file://myfile.json`\ --region`us-west-2`Contents of `myfile.json`:`{ "MessageConfiguration": { "SMSMessage": { "Body": "hello, how are you?" } }, "Endpoints": { "testendpoint": {} } }`Output: `{ "MessageResponse": { "ApplicationId": "611e3e3cdd47474c9c1399a505665b91", "EndpointResult": { "testendpoint": { "Address": "+12345678900", "DeliveryStatus": "SUCCESSFUL", "MessageId": "itnuqhai5alf1n6ahv3udc05n7hhddr6gb3lq6g0", "StatusCode": 200, "StatusMessage": "MessageId: itnuqhai5alf1n6ahv3udc05n7hhddr6gb3lq6g0" } }, "RequestId": "c7e23264-04b2-4a46-b800-d24923f74753" } }`For more information, see [Amazon Pinpoint SMS channel](https://docs.aws.amazon.com/pinpoint/latest/userguide/channels-sms.html)in the*Amazon Pinpoint User Guide*.- 
                    For API details, see [SendMessages](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/pinpoint/send-messages.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `send-users-messages`.

- **AWS CLI**
- 
            
                    **To send SMS message for an user of an application**The following `send-users-messages`example sends a direct message for an user of an application.`aws pinpoint send-users-messages \ --application-id``611e3e3cdd47474c9c1399a505665b91`\ --send-users-message-request`file://myfile.json`\ --region`us-west-2`Contents of `myfile.json`:`{ "MessageConfiguration": { "SMSMessage": { "Body": "hello, how are you?" } }, "Users": { "testuser": {} } }`Output: `{ "SendUsersMessageResponse": { "ApplicationId": "611e3e3cdd47474c9c1399a505665b91", "RequestId": "e0b12cf5-2359-11e9-bb0b-d5fb91876b25", "Result": { "testuser": { "testuserendpoint": { "DeliveryStatus": "SUCCESSFUL", "MessageId": "7qu4hk5bqhda3i7i2n4pjf98qcuh8b7p45ifsmo0", "StatusCode": 200, "StatusMessage": "MessageId: 7qu4hk5bqhda3i7i2n4pjf98qcuh8b7p45ifsmo0", "Address": "+12345678900" } } } } }`For more information, see [Amazon Pinpoint SMS channel](https://docs.aws.amazon.com/pinpoint/latest/userguide/channels-sms.html)in the*Amazon Pinpoint User Guide*.- 
                    For API details, see [SendUsersMessages](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/pinpoint/send-users-messages.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `tag-resource`.

- **AWS CLI**
- 
            
                    **To add tags to a resource**The following example adds two tags (key names and values) to a resource. `aws pinpoint list-tags-for-resource \ --resource-arn``arn:aws:mobiletargeting:us-east-1:AIDACKCEVSQ6C2EXAMPLE:apps/810c7aab86d42fb2b56c8c966example`\ --tags-model`tags={Stack=Production,Year=2019}`This command produces no output. For more information, see 'Tagging Amazon Pinpoint Resources <https://docs.aws.amazon.com/pinpoint/latest/developerguide/tagging-resources.html>'__ in the *Amazon Pinpoint Developer Guide*.- 
                    For API details, see [TagResource](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/pinpoint/tag-resource.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `untag-resource`.

- **AWS CLI**
- 
            
                    **Example 1: To remove a tag from a resource**The following `untag-resource`example removes the specified tag (key name and value) from a resource.`aws pinpoint untag-resource \ --resource-arn``arn:aws:mobiletargeting:us-west-2:AIDACKCEVSQ6C2EXAMPLE:apps/810c7aab86d42fb2b56c8c966example`\ --tag-keys`Year`This command produces no output. **Example 2: To remove multiple tags from a resource**The following `untag-resource`example removes the specified tags (key names and values) from a resource.`aws pinpoint untag-resource \ --resource-arn``arn:aws:mobiletargeting:us-east-1:AIDACKCEVSQ6C2EXAMPLE:apps/810c7aab86d42fb2b56c8c966example`\ --tag-keys`Year``Stack`This command produces no output. For more information, see 'Tagging Amazon Pinpoint Resources <https://docs.aws.amazon.com/pinpoint/latest/developerguide/tagging-resources.html>'__ in the *Amazon Pinpoint Developer Guide*.- 
                    For API details, see [UntagResource](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/pinpoint/untag-resource.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `update-sms-channel`.

- **AWS CLI**
- 
            
                    **To enable SMS channel or to update the status and settings of the SMS channel for an application.**The following `update-sms-channel`example enables SMS channel for an SMS channel for an application.`aws pinpoint update-sms-channel \ --application-id``611e3e3cdd47474c9c1399a505665b91`\ --sms-channel-request`Enabled=true`\ --region`us-west-2`Output: `{ "SMSChannelResponse": { "ApplicationId": "611e3e3cdd47474c9c1399a505665b91", "CreationDate": "2019-01-28T23:25:25.224Z", "Enabled": true, "Id": "sms", "IsArchived": false, "LastModifiedDate": "2023-05-18T23:22:50.977Z", "Platform": "SMS", "PromotionalMessagesPerSecond": 20, "TransactionalMessagesPerSecond": 20, "Version": 3 } }`For more information, see [Amazon Pinpoint SMS channel](https://docs.aws.amazon.com/pinpoint/latest/userguide/channels-sms.html)in the*Amazon Pinpoint User Guide*.- 
                    For API details, see [UpdateSmsChannel](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/pinpoint/update-sms-channel.html)in*AWS CLI Command Reference*.
 
-