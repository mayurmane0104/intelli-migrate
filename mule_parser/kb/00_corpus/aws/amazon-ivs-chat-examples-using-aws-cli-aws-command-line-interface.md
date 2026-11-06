# Amazon IVS Chat examples using AWS CLI - AWS Command Line Interface

**Source:** [https://docs.aws.amazon.com/cli/latest/userguide/cli_ivschat_code_examples.html](https://docs.aws.amazon.com/cli/latest/userguide/cli_ivschat_code_examples.html)

---

The following code examples show you how to perform actions and implement common scenarios by using the AWS Command Line Interface with Amazon IVS Chat.

*Actions* are code excerpts from larger programs and must be run in context. While actions show you how to call individual service functions, you can see actions in context in their related scenarios.

Each example includes a link to the complete source code, where you can find instructions on how to set up and run the code in context.

###### Topics

## Actions

    The following code example shows how to use `create-chat-token`.

- **AWS CLI**
- 
            
                    **To create a chat token**The following `create-chat-token`example creates an encrypted chat token that is used to establish an individual WebSocket connection to a room. The token is valid for one minute, and a connection (session) established with the token is valid for the specified duration.`aws ivschat create-chat-token \ --room-identifier "arn:aws:ivschat:us-west-2:12345689012:room/g1H2I3j4k5L6", \ --user-id``"11231234"`\ --capabilities "SEND_MESSAGE", \ --session-duration-in-minutes`30`Output: `{ "token": "ACEGmnoq#1rstu2...BDFH3vxwy!4hlm!#5", "sessionExpirationTime": "2022-03-16T04:44:09+00:00" "state": "CREATING", "tokenExpirationTime": "2022-03-16T03:45:09+00:00" }`For more information, see [Step 3: Authenticate and Authorize Chat Clients](https://docs.aws.amazon.com/ivs/latest/userguide/getting-started-chat.html)in the*Amazon Interactive Video Service User Guide*.- 
                    For API details, see [CreateChatToken](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ivschat/create-chat-token.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `create-logging-configuration`.

- **AWS CLI**
- 
            
                    **To create a chat LoggingConfiguration resource**The following `create-logging-configuration`example creates a LoggingConfiguration resource that allows clients to store and record sent messages.`aws ivschat create-logging-configuration \ --destination-configuration``s3={bucketName=demo-logging-bucket}`\ --name`"test-logging-config"`\ --tags`"key1=value1, key2=value2"`Output: `{ "arn": "arn:aws:ivschat:us-west-2:123456789012:logging-configuration/ABcdef34ghIJ", "createTime": "2022-09-14T17:48:00.653000+00:00", "destinationConfiguration": { "s3": { "bucketName": "demo-logging-bucket" } }, "id": "ABcdef34ghIJ", "name": "test-logging-config", "state": "ACTIVE", "tags": { "key1" : "value1", "key2" : "value2" }, "updateTime": "2022-09-14T17:48:01.104000+00:00" }`For more information, see [Getting Started with Amazon IVS Chat](https://docs.aws.amazon.com/ivs/latest/userguide/getting-started-chat.html)in the*Amazon Interactive Video Service User Guide*.- 
                    For API details, see [CreateLoggingConfiguration](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ivschat/create-logging-configuration.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `create-room`.

- **AWS CLI**
- 
            
                    **To create a room**The following `create-room`example creates a new room.`aws ivschat create-room \ --name``"test-room-1"`\ --logging-configuration-identifiers`"arn:aws:ivschat:us-west-2:123456789012:logging-configuration/ABcdef34ghIJ"`\ --maximum-message-length`256`\ --maximum-message-rate-per-second`5`Output: `{ "arn": "arn:aws:ivschat:us-west-2:12345689012:room/g1H2I3j4k5L6", "id": "g1H2I3j4k5L6", "createTime": "2022-03-16T04:44:09+00:00", "loggingConfigurationIdentifiers": ["arn:aws:ivschat:us-west-2:123456789012:logging-configuration/ABcdef34ghIJ"], "maximumMessageLength": 256, "maximumMessageRatePerSecond": 5, "name": "test-room-1", "tags": {} "updateTime": "2022-03-16T07:22:09+00:00" }`For more information, see [Step 2: Create a Chat Room](https://docs.aws.amazon.com/ivs/latest/userguide/getting-started-chat.html)in the*Amazon Interactive Video Service User Guide*.- 
                    For API details, see [CreateRoom](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ivschat/create-room.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `delete-logging-configuration`.

- **AWS CLI**
- 
            
                    **To delete a chat LoggingConfiguration resource**The following `delete-logging-configuration`example deletes the LoggingConfiguration resource for the specified ARN.`aws ivschat delete-logging-configuration \ --identifier``"arn:aws:ivschat:us-west-2:123456789012:logging-configuration/ABcdef34ghIJ"`This command produces no output. For more information, see [Getting Started with Amazon IVS Chat](https://docs.aws.amazon.com/ivs/latest/userguide/getting-started-chat.html)in the*Amazon Interactive Video Service User Guide*.- 
                    For API details, see [DeleteLoggingConfiguration](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ivschat/delete-logging-configuration.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `delete-message`.

- **AWS CLI**
- 
            
                    **To delete messages from a specified room**The following `delete-message`example sends an even to the specified room, which directs clients to delete the specified message: that is, unrender it from view and delete it from the client's chat history.`aws ivschat delete-message \ --room-identifier``"arn:aws:ivschat:us-west-2:12345689012:room/g1H2I3j4k5L6"`\ --id`"ABC123def456"`\ --reason`"Message contains profanity"`Output: `{ "id": "12345689012" }`For more information, see [Getting Started with Amazon IVS Chat](https://docs.aws.amazon.com/ivs/latest/userguide/getting-started-chat.html)in the*Amazon Interactive Video Service User Guide*.- 
                    For API details, see [DeleteMessage](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ivschat/delete-message.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `delete-room`.

- **AWS CLI**
- 
            
                    **To delete a room**The following `delete-room`example deletes the specified room. Connected clients are disconnected. On success it returns HTTP 204 with an empty response body.`aws ivschat delete-room \ --identifier``"arn:aws:ivschat:us-west-2:12345689012:room/g1H2I3j4k5L6"`This command produces no output. For more information, see [Getting Started with Amazon IVS Chat](https://docs.aws.amazon.com/ivs/latest/userguide/getting-started-chat.html)in the*Amazon Interactive Video Service User Guide*.- 
                    For API details, see [DeleteRoom](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ivschat/delete-room.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `disconnect-user`.

- **AWS CLI**
- 
            
                    **To disconnect a user from a room**The following `disconnect-user`example disconnects all connections for the specified user from the specified room. On success it returns HTTP 200 with an empty response body.`aws ivschat disconnect-user \ --room-identifier``"arn:aws:ivschat:us-west-2:12345689012:room/g1H2I3j4k5L6"`\ --user-id`"ABC123def456"`\ --reason`"Violated terms of service"`This command produces no output. For more information, see [Getting Started with Amazon IVS Chat](https://docs.aws.amazon.com/ivs/latest/userguide/getting-started-chat.html)in the*Amazon Interactive Video Service User Guide*.- 
                    For API details, see [DisconnectUser](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ivschat/disconnect-user.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `get-logging-configuration`.

- **AWS CLI**
- 
            
                    **To get information about a LoggingConfiguration resource**The following `get-logging-configuration`example gets information about the LoggingConfiguration resource for the specified ARN.`aws ivschat get-logging-configuration \ --identifier``"arn:aws:ivschat:us-west-2:123456789012:logging-configuration/ABcdef34ghIJ"`Output: `{ "arn": "arn:aws:ivschat:us-west-2:123456789012:logging-configuration/ABcdef34ghIJ", "createTime": "2022-09-14T17:48:00.653000+00:00", "destinationConfiguration": { "s3": { "bucketName": "demo-logging-bucket" } }, "id": "ABcdef34ghIJ", "name": "test-logging-config", "state": "ACTIVE", "tags": { "key1" : "value1", "key2" : "value2" }, "updateTime": "2022-09-14T17:48:01.104000+00:00" }`For more information, see [Getting Started with Amazon IVS Chat](https://docs.aws.amazon.com/ivs/latest/userguide/getting-started-chat.html)in the*Amazon Interactive Video Service User Guide*.- 
                    For API details, see [GetLoggingConfiguration](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ivschat/get-logging-configuration.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `get-room`.

- **AWS CLI**
- 
            
                    **To get the specified room**The following `get-room`example gets information about the specified room.`aws ivschat get-room \ --identifier``"arn:aws:ivschat:us-west-2:12345689012:room/g1H2I3j4k5L6"`Output: `{ "arn": "arn:aws:ivschat:us-west-2:12345689012:room/g1H2I3j4k5L6", "createTime": "2022-03-16T04:44:09+00:00", "id": "g1H2I3j4k5L6", "loggingConfigurationIdentifiers": ["arn:aws:ivschat:us-west-2:123456789012:logging-configuration/ABcdef34ghIJ"], "maximumMessageLength": 256, "maximumMessageRatePerSecond": 5, "name": "test-room-1", "tags": {}, "updateTime": "2022-03-16T07:22:09+00:00" }`For more information, see [Getting Started with Amazon IVS Chat](https://docs.aws.amazon.com/ivs/latest/userguide/getting-started-chat.html)in the*Amazon Interactive Video Service User Guide*.- 
                    For API details, see [GetRoom](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ivschat/get-room.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `list-logging-configurations`.

- **AWS CLI**
- 
            
                    **To get summary information about all logging configurations for the user in the AWS region where the API request is processed**The following `list-logging-configurations`example lists information about all LoggingConfiguration resources for the user in the AWS region where the API request is processed.`aws ivschat list-logging-configurations \ --max-results``2`\ --next-token ""Output: `{ "nextToken": "set-2", "loggingConfigurations": [ { "arn": "arn:aws:ivschat:us-west-2:123456789012:logging-configuration/ABcdef34ghIJ", "createTime": "2022-09-14T17:48:00.653000+00:00", "destinationConfiguration": { "s3": { "bucketName": "demo-logging-bucket" } }, "id": "ABcdef34ghIJ", "name": "test-logging-config", "state": "ACTIVE", "tags": { "key1" : "value1", "key2" : "value2" }, "updateTime": "2022-09-14T17:48:01.104000+00:00" } ... ] }`For more information, see [Getting Started with Amazon IVS Chat](https://docs.aws.amazon.com/ivs/latest/userguide/getting-started-chat.html)in the*Amazon Interactive Video Service User Guide*.- 
                    For API details, see [ListLoggingConfigurations](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ivschat/list-logging-configurations.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `list-rooms`.

- **AWS CLI**
- 
            
                    **To get summary information about all your rooms in the current region**The following `list-rooms`example gets summary information about all the rooms in the AWS region where the request is processed. Results are sorted in descending order of updateTime.`aws ivschat list-rooms \ --logging-configuration-identifier``"arn:aws:ivschat:us-west-2:123456789012:logging-configuration/ABcdef34ghIJ"`\ --max-results`10`\ --next-token ""Output: `{ "nextToken": "page3", "rooms": [ { "arn:aws:ivschat:us-west-2:12345689012:room/g1H2I3j4k5L6", "createTime": "2022-03-16T04:44:09+00:00", "id": "g1H2I3j4k5L6", "loggingConfigurationIdentifiers": ["arn:aws:ivschat:us-west-2:123456789012:logging-configuration/ABcdef34ghIJ"], "name": "test-room-1", "tags": {}, "updateTime": "2022-03-16T07:22:09+00:00" } ] }`For more information, see [Getting Started with Amazon IVS Chat](https://docs.aws.amazon.com/ivs/latest/userguide/getting-started-chat.html)in the*Amazon Interactive Video Service User Guide*.- 
                    For API details, see [ListRooms](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ivschat/list-rooms.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `list-tags-for-resource`.

- **AWS CLI**
- 
            
                    **To list all tags for an AWS resource (for example: Room)**The following `list-tags-for-resource`example lists all tags for a specified resource ARN (Amazon Resource Name).`aws ivschat list-tags-for-resource \ --resource-arn``arn:aws:ivschat:us-west-2:12345689012:room/g1H2I3j4k5L6`Output: `{ "tags": { "key1": "value1", "key2": "value2" } }`For more information, see [Tagging](https://docs.aws.amazon.com/ivs/latest/APIReference/Welcome.html)in the*Amazon Interactive Video Service API Reference*.- 
                    For API details, see [ListTagsForResource](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ivschat/list-tags-for-resource.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `send-event`.

- **AWS CLI**
- 
            
                    **To send an event to a room**The following `send-event`example sends the given event to the specified room.`aws ivschat send-event \ --room-identifier``"arn:aws:ivschat:us-west-2:12345689012:room/g1H2I3j4k5L6"`\ --event-name`"SystemMessage"`\ --attributes \ "msgType"="user-notification", \ "msgText"="This chat room will close in 15 minutes."Output: `{ "id": "12345689012" }`For more information, see [Getting Started with Amazon IVS Chat](https://docs.aws.amazon.com/ivs/latest/userguide/getting-started-chat.html)in the*Amazon Interactive Video Service User Guide*.- 
                    For API details, see [SendEvent](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ivschat/send-event.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `tag-resource`.

- **AWS CLI**
- 
            
                    **To add or update tags for an AWS resource (for example: Room)**The following `tag-resource`example adds or updates tags for a specified resource ARN (Amazon Resource Name). On success it returns HTTP 200 with an empty response body.`aws ivschat tag-resource \ --resource-arn``arn:aws:ivschat:us-west-2:12345689012:room/g1H2I3j4k5L6`\ --tags`"tagkey1=tagkeyvalue1, tagkey2=tagkeyvalue2"`This command produces no output. For more information, see [Tagging](https://docs.aws.amazon.com/ivs/latest/APIReference/Welcome.html)in the*Amazon Interactive Video Service API Reference*.- 
                    For API details, see [TagResource](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ivschat/tag-resource.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `untag-resource`.

- **AWS CLI**
- 
            
                    **To remove tags for an AWS resource (for example: Room)**The following `untag-resource`example removes the specified tags for a specified resource ARN (Amazon Resource Name). On success it returns HTTP 200 with an empty response body.`aws ivschat untag-resource \ --resource-arn``arn:aws:ivschat:us-west-2:12345689012:room/g1H2I3j4k5L6`\ --tag-keys`"tagkey1, tagkey2"`This command produces no output. For more information, see [Tagging](https://docs.aws.amazon.com/ivs/latest/APIReference/Welcome.html)in the*Amazon Interactive Video Service API Reference*.- 
                    For API details, see [UntagResource](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ivschat/untag-resource.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `update-logging-configuration`.

- **AWS CLI**
- 
            
                    **To update a room's logging configuration**The following `update-logging-configuration`example updates a LoggingConfiguration resource with the given data.`aws ivschat update-logging-configuration \ --destination-configuration``s3={bucketName=demo-logging-bucket}`\ --identifier`"arn:aws:ivschat:us-west-2:123456789012:logging-configuration/ABcdef34ghIJ"`\ --name`"test-logging-config"`Output: `{ "arn": "arn:aws:ivschat:us-west-2:123456789012:logging-configuration/ABcdef34ghIJ", "createTime": "2022-09-14T17:48:00.653000+00:00", "destinationConfiguration": { "s3": { "bucketName": "demo-logging-bucket" } }, "id": "ABcdef34ghIJ", "name": "test-logging-config", "state": "ACTIVE", "tags": { "key1" : "value1", "key2" : "value2" }, "updateTime": "2022-09-14T17:48:01.104000+00:00" }`For more information, see [Getting Started with Amazon IVS Chat](https://docs.aws.amazon.com/ivs/latest/userguide/getting-started-chat.html)in the*Amazon Interactive Video Service User Guide*.- 
                    For API details, see [UpdateLoggingConfiguration](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ivschat/update-logging-configuration.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `update-room`.

- **AWS CLI**
- 
            
                    **To update a room's configuration**The following `update-room`example updates the specified room's configuration with the given data.`aws ivschat update-room \ --identifier``"arn:aws:ivschat:us-west-2:12345689012:room/g1H2I3j4k5L6"`\ --logging-configuration-identifiers`"arn:aws:ivschat:us-west-2:123456789012:logging-configuration/ABcdef34ghIJ"`\ --name`"chat-room-a"`\ --maximum-message-length`256`\ --maximum-message-rate-per-second`5`Output: `{ "arn": "arn:aws:ivschat:us-west-2:12345689012:room/g1H2I3j4k5L6", "createTime": "2022-03-16T04:44:09+00:00", "id": "g1H2I3j4k5L6", "loggingConfigurationIdentifiers": ["arn:aws:ivschat:us-west-2:123456789012:logging-configuration/ABcdef34ghIJ"], "maximumMessageLength": 256, "maximumMessageRatePerSecond": 5, "name": "chat-room-a", "tags": {}, "updateTime": "2022-03-16T07:22:09+00:00" }`For more information, see [Getting Started with Amazon IVS Chat](https://docs.aws.amazon.com/ivs/latest/userguide/getting-started-chat.html)in the*Amazon Interactive Video Service User Guide*.- 
                    For API details, see [UpdateRoom](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ivschat/update-room.html)in*AWS CLI Command Reference*.
 
-