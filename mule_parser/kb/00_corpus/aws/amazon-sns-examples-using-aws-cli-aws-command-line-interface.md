# Amazon SNS examples using AWS CLI - AWS Command Line Interface

**Source:** [https://docs.aws.amazon.com/cli/latest/userguide/cli_sns_code_examples.html](https://docs.aws.amazon.com/cli/latest/userguide/cli_sns_code_examples.html)

---

The following code examples show you how to perform actions and implement common scenarios by using the AWS Command Line Interface with Amazon SNS.

*Actions* are code excerpts from larger programs and must be run in context. While actions show you how to call individual service functions, you can see actions in context in their related scenarios.

*Scenarios* are code examples that show you how to accomplish specific tasks by calling multiple functions within a service or combined with other AWS services.

Each example includes a link to the complete source code, where you can find instructions on how to set up and run the code in context.

## Actions

    The following code example shows how to use `add-permission`.

- **AWS CLI**
- 
            
                    **To add a permission to a topic**The following `add-permission`example adds the permission for AWS account`987654321098`to use the`Publish`action with the specified topic under AWS account`123456789012`.`aws sns add-permission \ --topic-arn``arn:aws:sns:us-west-2:123456789012:MyTopic`\ --label`Publish-Permission`\ --aws-account-id`987654321098`\ --action-name`Publish`This command produces no output. - 
                    For API details, see [AddPermission](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sns/add-permission.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `check-if-phone-number-is-opted-out`.

- **AWS CLI**
- 
            
                    **To check SMS message opt-out for a phone number**The following `check-if-phone-number-is-opted-out`example checks whether the specified phone number is opted out of receiving SMS messages from the current AWS account.`aws sns check-if-phone-number-is-opted-out \ --phone-number``+1555550100`Output: `{ "isOptedOut": false }`- 
                    For API details, see [CheckIfPhoneNumberIsOptedOut](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sns/check-if-phone-number-is-opted-out.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `confirm-subscription`.

- **AWS CLI**
- 
            
                    **To confirm a subscription**The following `confirm-subscription`command completes the confirmation process started when you subscribed to an SNS topic named`my-topic`. The --token parameter comes from the confirmation message sent to the notification endpoint specified in the subscribe call.`aws sns confirm-subscription \ --topic-arn``arn:aws:sns:us-west-2:123456789012:my-topic`\ --token`2336412f37fb687f5d51e6e241d7700ae02f7124d8268910b858cb4db727ceeb2474bb937929d3bdd7ce5d0cce19325d036bc858d3c217426bcafa9c501a2cace93b83f1dd3797627467553dc438a8c974119496fc3eff026eaa5d14472ded6f9a5c43aec62d83ef5f49109da7176391`Output: `{ "SubscriptionArn": "arn:aws:sns:us-west-2:123456789012:my-topic:8a21d249-4329-4871-acc6-7be709c6ea7f" }`- 
                    For API details, see [ConfirmSubscription](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sns/confirm-subscription.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `create-platform-application`.

- **AWS CLI**
- 
            
                    **To create a platform application**The following `create-platform-application`example creates a Google Firebase platform application using the specified platform credential.`aws sns create-platform-application \ --name``MyApplication`\ --platform`GCM`\ --attributes`PlatformCredential=EXAMPLEabcd12345jklm67890stuv12345bcdef`Output: `{ "PlatformApplicationArn": "arn:aws:sns:us-west-2:123456789012:app/GCM/MyApplication" }`- 
                    For API details, see [CreatePlatformApplication](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sns/create-platform-application.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `create-topic`.

- **AWS CLI**
- 
            
                    **To create an SNS topic**The following `create-topic`example creates an SNS topic named`my-topic`.`aws sns create-topic \ --name``my-topic`Output: `{ "ResponseMetadata": { "RequestId": "1469e8d7-1642-564e-b85d-a19b4b341f83" }, "TopicArn": "arn:aws:sns:us-west-2:123456789012:my-topic" }`For more information, see [Using the AWS Command Line Interface with Amazon SQS and Amazon SNS](https://docs.aws.amazon.com/cli/latest/userguide/cli-sqs-queue-sns-topic.html)in the*AWS Command Line Interface User Guide*.- 
                    For API details, see [CreateTopic](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sns/create-topic.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `delete-endpoint`.

- **AWS CLI**
- 
            
                    **To delete a platform application endpoint**The following `delete-endpoint`example deletes the specified platform application endpoint.`aws sns delete-endpoint \ --endpoint-arn``arn:aws:sns:us-west-2:123456789012:endpoint/GCM/MyApplication/12345678-abcd-9012-efgh-345678901234`This command produces no output. - 
                    For API details, see [DeleteEndpoint](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sns/delete-endpoint.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `delete-platform-application`.

- **AWS CLI**
- 
            
                    **To delete a platform application**The following `delete-platform-application`example deletes the specified platform application.`aws sns delete-platform-application \ --platform-application-arn``arn:aws:sns:us-west-2:123456789012:app/ADM/MyApplication`This command produces no output. - 
                    For API details, see [DeletePlatformApplication](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sns/delete-platform-application.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `delete-topic`.

- **AWS CLI**
- 
            
                    **To delete an SNS topic**The following `delete-topic`example deletes the specified SNS topic.`aws sns delete-topic \ --topic-arn``"arn:aws:sns:us-west-2:123456789012:my-topic"`This command produces no output. - 
                    For API details, see [DeleteTopic](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sns/delete-topic.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `get-endpoint-attributes`.

- **AWS CLI**
- 
            
                    **To list platform application endpoint attributes**The following `get-endpoint-attributes`example lists the attributes for the specified platform application endpoint.`aws sns get-endpoint-attributes \ --endpoint-arn``arn:aws:sns:us-west-2:123456789012:endpoint/GCM/MyApplication/12345678-abcd-9012-efgh-345678901234`Output: `{ "Attributes": { "Enabled": "true", "Token": "EXAMPLE12345..." } }`- 
                    For API details, see [GetEndpointAttributes](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sns/get-endpoint-attributes.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `get-platform-application-attributes`.

- **AWS CLI**
- 
            
                    **To list the platform application attributes**The following `get-platform-application-attributes`example lists the attributes for the specified platform application.`aws sns get-platform-application-attributes \ --platform-application-arn``arn:aws:sns:us-west-2:123456789012:app/MPNS/MyApplication`Output: `{ "Attributes": { "Enabled": "true", "SuccessFeedbackSampleRate": "100" } }`- 
                    For API details, see [GetPlatformApplicationAttributes](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sns/get-platform-application-attributes.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `get-sms-attributes`.

- **AWS CLI**
- 
            
                    **To list the default SMS message attributes**The following `get-sms-attributes`example lists the default attributes for sending SMS messages.`aws sns get-sms-attributes`Output: `{ "attributes": { "DefaultSenderID": "MyName" } }`- 
                    For API details, see [GetSMSAttributes](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sns/get-sms-attributes.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `get-subscription-attributes`.

- **AWS CLI**
- 
            
                    **To retrieve subscription attributes for a topic**The following `get-subscription-attributes`displays the attributes of the specified subscription. You can get the`subscription-arn`from the output of the`list-subscriptions`command.`aws sns get-subscription-attributes \ --subscription-arn``"arn:aws:sns:us-west-2:123456789012:my-topic:8a21d249-4329-4871-acc6-7be709c6ea7f"`Output: `{ "Attributes": { "Endpoint": "my-email@example.com", "Protocol": "email", "RawMessageDelivery": "false", "ConfirmationWasAuthenticated": "false", "Owner": "123456789012", "SubscriptionArn": "arn:aws:sns:us-west-2:123456789012:my-topic:8a21d249-4329-4871-acc6-7be709c6ea7f", "TopicArn": "arn:aws:sns:us-west-2:123456789012:my-topic" } }`- 
                    For API details, see [GetSubscriptionAttributes](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sns/get-subscription-attributes.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `get-topic-attributes`.

- **AWS CLI**
- 
            
                    **To retrieve the attributes of a topic**The following `get-topic-attributes`example displays the attributes for the specified topic.`aws sns get-topic-attributes \ --topic-arn``"arn:aws:sns:us-west-2:123456789012:my-topic"`Output: `{ "Attributes": { "SubscriptionsConfirmed": "1", "DisplayName": "my-topic", "SubscriptionsDeleted": "0", "EffectiveDeliveryPolicy": "{\"http\":{\"defaultHealthyRetryPolicy\":{\"minDelayTarget\":20,\"maxDelayTarget\":20,\"numRetries\":3,\"numMaxDelayRetries\":0,\"numNoDelayRetries\":0,\"numMinDelayRetries\":0,\"backoffFunction\":\"linear\"},\"disableSubscriptionOverrides\":false}}", "Owner": "123456789012", "Policy": "{\"Version\":\"2008-10-17\",\"Id\":\"__default_policy_ID\",\"Statement\":[{\"Sid\":\"__default_statement_ID\",\"Effect\":\"Allow\",\"Principal\":{\"AWS\":\"*\"},\"Action\":[\"SNS:Subscribe\",\"SNS:ListSubscriptionsByTopic\",\"SNS:DeleteTopic\",\"SNS:GetTopicAttributes\",\"SNS:Publish\",\"SNS:RemovePermission\",\"SNS:AddPermission\",\"SNS:SetTopicAttributes\"],\"Resource\":\"arn:aws:sns:us-west-2:123456789012:my-topic\",\"Condition\":{\"StringEquals\":{\"AWS:SourceOwner\":\"0123456789012\"}}}]}", "TopicArn": "arn:aws:sns:us-west-2:123456789012:my-topic", "SubscriptionsPending": "0" } }`- 
                    For API details, see [GetTopicAttributes](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sns/get-topic-attributes.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `list-endpoints-by-platform-application`.

- **AWS CLI**
- 
            
                    **To list the endpoints for a platform application**The following `list-endpoints-by-platform-application`example lists the endpoints and endpoint attributes for the specified platform application.`aws sns list-endpoints-by-platform-application \ --platform-application-arn``arn:aws:sns:us-west-2:123456789012:app/GCM/MyApplication`Output: `{ "Endpoints": [ { "Attributes": { "Token": "EXAMPLE12345..., "Enabled": "true" }, "EndpointArn": "arn:aws:sns:us-west-2:123456789012:endpoint/GCM/MyApplication/12345678-abcd-9012-efgh-345678901234" } ] }`- 
                    For API details, see [ListEndpointsByPlatformApplication](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sns/list-endpoints-by-platform-application.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `list-phone-numbers-opted-out`.

- **AWS CLI**
- 
            
                    **To list SMS message opt-outs**The following `list-phone-numbers-opted-out`example lists the phone numbers opted out of receiving SMS messages.`aws sns list-phone-numbers-opted-out`Output: `{ "phoneNumbers": [ "+15555550100" ] }`- 
                    For API details, see [ListPhoneNumbersOptedOut](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sns/list-phone-numbers-opted-out.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `list-platform-applications`.

- **AWS CLI**
- 
            
                    **To list platform applications**The following `list-platform-applications`example lists the platform applications for ADM and MPNS.`aws sns list-platform-applications`Output: `{ "PlatformApplications": [ { "PlatformApplicationArn": "arn:aws:sns:us-west-2:123456789012:app/ADM/MyApplication", "Attributes": { "SuccessFeedbackSampleRate": "100", "Enabled": "true" } }, { "PlatformApplicationArn": "arn:aws:sns:us-west-2:123456789012:app/MPNS/MyOtherApplication", "Attributes": { "SuccessFeedbackSampleRate": "100", "Enabled": "true" } } ] }`- 
                    For API details, see [ListPlatformApplications](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sns/list-platform-applications.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `list-subscriptions-by-topic`.

- **AWS CLI**
- 
            
                    **To list the subscriptions associated with a topic**The following `list-subscriptions-by-topic`retrieves a list of SNS subscriptions associated with the specified topic.`aws sns list-subscriptions-by-topic \ --topic-arn``"arn:aws:sns:us-west-2:123456789012:my-topic"`Output: `{ "Subscriptions": [ { "Owner": "123456789012", "Endpoint": "my-email@example.com", "Protocol": "email", "TopicArn": "arn:aws:sns:us-west-2:123456789012:my-topic", "SubscriptionArn": "arn:aws:sns:us-west-2:123456789012:my-topic:8a21d249-4329-4871-acc6-7be709c6ea7f" } ] }`- 
                    For API details, see [ListSubscriptionsByTopic](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sns/list-subscriptions-by-topic.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `list-subscriptions`.

- **AWS CLI**
- 
            
                    **To list your SNS subscriptions**The following `list-subscriptions`example displays a list of the SNS subscriptions in your AWS account.`aws sns list-subscriptions`Output: `{ "Subscriptions": [ { "Owner": "123456789012", "Endpoint": "my-email@example.com", "Protocol": "email", "TopicArn": "arn:aws:sns:us-west-2:123456789012:my-topic", "SubscriptionArn": "arn:aws:sns:us-west-2:123456789012:my-topic:8a21d249-4329-4871-acc6-7be709c6ea7f" } ] }`- 
                    For API details, see [ListSubscriptions](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sns/list-subscriptions.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `list-tags-for-resource`.

- **AWS CLI**
- 
            
                    **To list tags for a topic**The following `list-tags-for-resource`example lists the tags for the specified Amazon SNS topic.`aws sns list-tags-for-resource \ --resource-arn``arn:aws:sns:us-west-2:123456789012:MyTopic`Output: `{ "Tags": [ { "Key": "Team", "Value": "Alpha" } ] }`- 
                    For API details, see [ListTagsForResource](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sns/list-tags-for-resource.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `list-topics`.

- **AWS CLI**
- 
            
                    **To list your SNS topics**The following `list-topics`example lists all of SNS topics in your AWS account.`aws sns list-topics`Output: `{ "Topics": [ { "TopicArn": "arn:aws:sns:us-west-2:123456789012:my-topic" } ] }`- 
                    For API details, see [ListTopics](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sns/list-topics.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `opt-in-phone-number`.

- **AWS CLI**
- 
            
                    **To opt-in for SMS messages**The following `opt-in-phone-number`example opts the specified phone number into receiving SMS messages.`aws sns opt-in-phone-number \ --phone-number``+15555550100`This command produces no output. - 
                    For API details, see [OptInPhoneNumber](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sns/opt-in-phone-number.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `publish`.

- **AWS CLI**
- 
            
                    **Example 1: To publish a message to a topic**The following `publish`example publishes the specified message to the specified SNS topic. The message comes from a text file, which enables you to include line breaks.`aws sns publish \ --topic-arn``"arn:aws:sns:us-west-2:123456789012:my-topic"`\ --message`file://message.txt`Contents of `message.txt`:`Hello World Second Line`Output: `{ "MessageId": "123a45b6-7890-12c3-45d6-111122223333" }`**Example 2: To publish an SMS message to a phone number**The following `publish`example publishes the message`Hello world!`to the phone number`+1-555-555-0100`.`aws sns publish \ --message``"Hello world!"`\ --phone-number`+1-555-555-0100`Output: `{ "MessageId": "123a45b6-7890-12c3-45d6-333322221111" }`- 
                    For API details, see [Publish](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sns/publish.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `put-data-protection-policy`.

- **AWS CLI**
- 
            
                    **To set data protection policy****Example 1: To deny publishers from publishing messages with CreditCardNumber**The following `put-data-protection-policy`example denies publishers from publishing messages with CreditCardNumber.`aws sns put-data-protection-policy \ --resource-arn``arn:aws:sns:us-east-1:123456789012:mytopic`\ --data-protection-policy "{\"Name\":\"data_protection_policy\",\"Description\":\"Example data protection policy\",\"Version\":\"2021-06-01\",\"Statement\":[{\"DataDirection\":\"Inbound\",\"Principal\":[\"*\"],\"DataIdentifier\":[\"arn:aws:dataprotection::aws:data-identifier/CreditCardNumber\"],\"Operation\":{\"Deny\":{}}}]}"This command produces no output. **Example 2: To load parameters from a file**The following `put-data-protection-policy`loads parameters from a file.`aws sns put-data-protection-policy \ --resource-arn``arn:aws:sns:us-west-2:123456789012:MyTopic`\ --data-protection-policy`file://policy.json`This command produces no output. - 
                    For API details, see [PutDataProtectionPolicy](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sns/put-data-protection-policy.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `remove-permission`.

- **AWS CLI**
- 
            
                    **To remove a permission from a topic**The following `remove-permission`example removes the permission`Publish-Permission`from the specified topic.`aws sns remove-permission \ --topic-arn``arn:aws:sns:us-west-2:123456789012:MyTopic`\ --label`Publish-Permission`This command produces no output. - 
                    For API details, see [RemovePermission](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sns/remove-permission.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `set-endpoint-attributes`.

- **AWS CLI**
- 
            
                    **To set endpoint attributes**The following `set-endpoint-attributes`example disables the specified platform application endpoint.`aws sns set-endpoint-attributes \ --endpoint-arn``arn:aws:sns:us-west-2:123456789012:endpoint/GCM/MyApplication/12345678-abcd-9012-efgh-345678901234`\ --attributes`Enabled=false`Output: `{ "Attributes": { "Enabled": "false", "Token": "EXAMPLE12345..." } }`- 
                    For API details, see [SetEndpointAttributes](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sns/set-endpoint-attributes.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `set-platform-application-attributes`.

- **AWS CLI**
- 
            
                    **To set platform application attributes**The following `set-platform-application-attributes`example sets the`EventDeliveryFailure`attribute for the specified platform application to the ARN of the specified Amazon SNS topic.`aws sns set-platform-application-attributes \ --platform-application-arn``arn:aws:sns:us-west-2:123456789012:app/GCM/MyApplication`\ --attributes`EventDeliveryFailure=arn:aws:sns:us-west-2:123456789012:AnotherTopic`This command produces no output. - 
                    For API details, see [SetPlatformApplicationAttributes](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sns/set-platform-application-attributes.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `set-sms-attributes`.

- **AWS CLI**
- 
            
                    **To set SMS message attributes**The following `set-sms-attributes`example sets the default sender ID for SMS messages to`MyName`.`aws sns set-sms-attributes \ --attributes``DefaultSenderID=MyName`This command produces no output. - 
                    For API details, see [SetSMSAttributes](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sns/set-sms-attributes.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `set-subscription-attributes`.

- **AWS CLI**
- 
            
                    **To set subscription attributes**The following `set-subscription-attributes`example sets the`RawMessageDelivery`attribute to an SQS subscription.`aws sns set-subscription-attributes \ --subscription-arn``arn:aws:sns:us-east-1:123456789012:mytopic:f248de18-2cf6-578c-8592-b6f1eaa877dc`\ --attribute-name`RawMessageDelivery`\ --attribute-value`true`This command produces no output. The following `set-subscription-attributes`example sets a`FilterPolicy`attribute to an SQS subscription.`aws sns set-subscription-attributes \ --subscription-arn``arn:aws:sns:us-east-1:123456789012:mytopic:f248de18-2cf6-578c-8592-b6f1eaa877dc`\ --attribute-name`FilterPolicy`\ --attribute-value "{ \"anyMandatoryKey\": [\"any\", \"of\", \"these\"] }"This command produces no output. The following `set-subscription-attributes`example removes the`FilterPolicy`attribute from an SQS subscription.`aws sns set-subscription-attributes \ --subscription-arn``arn:aws:sns:us-east-1:123456789012:mytopic:f248de18-2cf6-578c-8592-b6f1eaa877dc`\ --attribute-name`FilterPolicy`\ --attribute-value`"{}"`This command produces no output. - 
                    For API details, see [SetSubscriptionAttributes](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sns/set-subscription-attributes.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `set-topic-attributes`.

- **AWS CLI**
- 
            
                    **To set an attribute for a topic**The following `set-topic-attributes`example sets the`DisplayName`attribute for the specified topic.`aws sns set-topic-attributes \ --topic-arn``arn:aws:sns:us-west-2:123456789012:MyTopic`\ --attribute-name`DisplayName`\ --attribute-value`MyTopicDisplayName`This command produces no output. - 
                    For API details, see [SetTopicAttributes](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sns/set-topic-attributes.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `subscribe`.

- **AWS CLI**
- 
            
                    **To subscribe to a topic**The following `subscribe`command subscribes an email address to the specified topic.`aws sns subscribe \ --topic-arn``arn:aws:sns:us-west-2:123456789012:my-topic`\ --protocol`email`\ --notification-endpoint`my-email@example.com`Output: `{ "SubscriptionArn": "pending confirmation" }`- 
                    For API details, see [Subscribe](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sns/subscribe.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `tag-resource`.

- **AWS CLI**
- 
            
                    **To add a tag to a topic**The following `tag-resource`example adds a metadata tag to the specified Amazon SNS topic.`aws sns tag-resource \ --resource-arn``arn:aws:sns:us-west-2:123456789012:MyTopic`\ --tags`Key=Team,Value=Alpha`This command produces no output. - 
                    For API details, see [TagResource](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sns/tag-resource.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `unsubscribe`.

- **AWS CLI**
- 
            
                    **To unsubscribe from a topic**The following `unsubscribe`example deletes the specified subscription from a topic.`aws sns unsubscribe \ --subscription-arn``arn:aws:sns:us-west-2:0123456789012:my-topic:8a21d249-4329-4871-acc6-7be709c6ea7f`This command produces no output. - 
                    For API details, see [Unsubscribe](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sns/unsubscribe.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `untag-resource`.

- **AWS CLI**
- 
            
                    **To remove a tag from a topic**The following `untag-resource`example removes any tags with the specified keys from the specified Amazon SNS topic.`aws sns untag-resource \ --resource-arn``arn:aws:sns:us-west-2:123456789012:MyTopic`\ --tag-keys`Team`This command produces no output. - 
                    For API details, see [UntagResource](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sns/untag-resource.html)in*AWS CLI Command Reference*.
 
- 
                    

## Scenarios

    The following code example shows how to create a platform endpoint for Amazon SNS push notifications.

- **AWS CLI**
- 
            
                    **To create a platform application endpoint**The following `create-platform-endpoint`example creates an endpoint for the specified platform application using the specified token.`aws sns create-platform-endpoint \ --platform-application-arn``arn:aws:sns:us-west-2:123456789012:app/GCM/MyApplication`\ --token`EXAMPLE12345...`Output: `{ "EndpointArn": "arn:aws:sns:us-west-2:1234567890:endpoint/GCM/MyApplication/12345678-abcd-9012-efgh-345678901234" }`