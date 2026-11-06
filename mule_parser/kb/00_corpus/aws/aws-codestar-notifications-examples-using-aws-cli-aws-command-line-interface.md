# AWS CodeStar Notifications examples using AWS CLI - AWS Command Line Interface

**Source:** [https://docs.aws.amazon.com/cli/latest/userguide/cli_codestar-notifications_code_examples.html](https://docs.aws.amazon.com/cli/latest/userguide/cli_codestar-notifications_code_examples.html)

---

The following code examples show you how to perform actions and implement common scenarios by using the AWS Command Line Interface with AWS CodeStar Notifications.

*Actions* are code excerpts from larger programs and must be run in context. While actions show you how to call individual service functions, you can see actions in context in their related scenarios.

Each example includes a link to the complete source code, where you can find instructions on how to set up and run the code in context.

###### Topics

## Actions

    The following code example shows how to use `create-notification-rule`.

- **AWS CLI**
- 
            
                    **To create a notification rule**The following `create-notification-rule`example uses a JSON file named`rule.json`to create a notification rule named`MyNotificationRule`for a repository named`MyDemoRepo`in the specified AWS account. Notifications with the`FULL`detail type are sent to the specified target Amazon SNS topic when branches and tags are created.`aws codestar-notifications create-notification-rule \ --cli-input-json``file://rule.json`Contents of `rule.json`:`{ "Name": "MyNotificationRule", "EventTypeIds": [ "codecommit-repository-branches-and-tags-created" ], "Resource": "arn:aws:codecommit:us-east-1:123456789012:MyDemoRepo", "Targets": [ { "TargetType": "SNS", "TargetAddress": "arn:aws:sns:us-east-1:123456789012:MyNotificationTopic" } ], "Status": "ENABLED", "DetailType": "FULL" }`Output: `{ "Arn": "arn:aws:codestar-notifications:us-east-1:123456789012:notificationrule/dc82df7a-EXAMPLE" }`For more information, see [Create a Notification rule](https://docs.aws.amazon.com/codestar-notifications/latest/userguide/notification-rule-create.html)in the*AWS Developer Tools Console User Guide*.- 
                    For API details, see [CreateNotificationRule](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codestar-notifications/create-notification-rule.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `delete-notification-rule`.

- **AWS CLI**
- 
            
                    **To delete a notification rule**The following `delete-notification-rule`example deletes the specified notification rule.`aws codestar-notifications delete-notification-rule \ --arn``arn:aws:codestar-notifications:us-east-1:123456789012:notificationrule/dc82df7a-EXAMPLE`Output: `{ "Arn": "arn:aws:codestar-notifications:us-east-1:123456789012:notificationrule/dc82df7a-EXAMPLE" }`For more information, see [Delete a Notification Rule](https://docs.aws.amazon.com/codestar-notifications/latest/userguide/notification-rule-delete.html)in the*AWS Developer Tools Console User Guide*.- 
                    For API details, see [DeleteNotificationRule](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codestar-notifications/delete-notification-rule.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `delete-target`.

- **AWS CLI**
- 
            
                    **To delete a notification rule target**The following `delete-target`example removes the specified target from all notification rules configured to use it as a target, and then deletes the target.`aws codestar-notifications delete-target \ --target-address``arn:aws:sns:us-east-1:123456789012:MyNotificationTopic`\ --force-unsubscribe-allThis command produces no output. For more information, see [Delete a Notification Rule Target](https://docs.aws.amazon.com/codestar-notifications/latest/userguide/notification-target-delete.html)in the*AWS Developer Tools Console User Guide*.- 
                    For API details, see [DeleteTarget](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codestar-notifications/delete-target.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `describe-notification-rule`.

- **AWS CLI**
- 
            
                    **To retrieve details of a notification rule**The following `describe-notification-rule`example retrieves the details of the specified notification rule.`aws codestar-notifications describe-notification-rule \ --arn``arn:aws:codestar-notifications:us-west-2:123456789012:notificationrule/dc82df7a-EXAMPLE`Output: `{ "LastModifiedTimestamp": 1569199844.857, "EventTypes": [ { "ServiceName": "CodeCommit", "EventTypeName": "Branches and tags: Created", "ResourceType": "Repository", "EventTypeId": "codecommit-repository-branches-and-tags-created" } ], "Status": "ENABLED", "DetailType": "FULL", "Resource": "arn:aws:codecommit:us-west-2:123456789012:MyDemoRepo", "Arn": "arn:aws:codestar-notifications:us-west-w:123456789012:notificationrule/dc82df7a-EXAMPLE", "Targets": [ { "TargetStatus": "ACTIVE", "TargetAddress": "arn:aws:sns:us-west-2:123456789012:MyNotificationTopic", "TargetType": "SNS" } ], "Name": "MyNotificationRule", "CreatedTimestamp": 1569199844.857, "CreatedBy": "arn:aws:iam::123456789012:user/Mary_Major" }`For more information, see [View Notification Rules](https://docs.aws.amazon.com/codestar-notifications/latest/userguide/notification-rule-view.html)in the*AWS Developer Tools Console User Guide*.- 
                    For API details, see [DescribeNotificationRule](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codestar-notifications/describe-notification-rule.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `list-event-types`.

- **AWS CLI**
- 
            
                    **To get a list of event types for a notification rule**The following `list-event-types`example retrieves a filtered list of all available notification event types for CodeDeploy applications. If instead you use no filter, the command returns all notification event types for all resource types.`aws codestar-notifications list-event-types \ --filters``Name=SERVICE_NAME,Value=CodeDeploy`Output: `{ "EventTypes": [ { "EventTypeId": "codedeploy-application-deployment-succeeded", "ServiceName": "CodeDeploy", "EventTypeName": "Deployment: Succeeded", "ResourceType": "Application" }, { "EventTypeId": "codedeploy-application-deployment-failed", "ServiceName": "CodeDeploy", "EventTypeName": "Deployment: Failed", "ResourceType": "Application" }, { "EventTypeId": "codedeploy-application-deployment-started", "ServiceName": "CodeDeploy", "EventTypeName": "Deployment: Started", "ResourceType": "Application" } ] }`For more information, see [Create a Notification Rule](https://docs.aws.amazon.com/codestar-notifications/latest/userguide/notification-rule-create.html)in the*AWS Developer Tools Console User Guide*.- 
                    For API details, see [ListEventTypes](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codestar-notifications/list-event-types.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `list-notification-rules`.

- **AWS CLI**
- 
            
                    **To retrieve a list of notification rules**The following `list-notification-rules`example retrieves a list of all notification rules in the specified AWS Region.`aws codestar-notifications list-notification-rules --region``us-east-1`Output: `{ "NotificationRules": [ { "Id": "dc82df7a-EXAMPLE", "Arn": "arn:aws:codestar-notifications:us-east-1:123456789012:notificationrule/dc82df7a-EXAMPLE" }, { "Id": "8d1f0983-EXAMPLE", "Arn": "arn:aws:codestar-notifications:us-east-1:123456789012:notificationrule/8d1f0983-EXAMPLE" } ] }`For more information, see [View Notification Rules](https://docs.aws.amazon.com/codestar-notifications/latest/userguide/notification-rule-view.html)in the*AWS Developer Tools Console User Guide*.- 
                    For API details, see [ListNotificationRules](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codestar-notifications/list-notification-rules.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `list-tags-for-resource`.

- **AWS CLI**
- 
            
                    **To get a list of tags attached to a notification rule**The following `list-tags-for-resource`example retrieves a list of all tags attached to the specified notification rule. In this example, the notification rule currently has no tags associated with it.`aws codestar-notifications list-tags-for-resource \ --arn``arn:aws:codestar-notifications:us-east-1:123456789012:notificationrule/fe1efd35-EXAMPLE`Output: `{ "Tags": {} }`For more information, see [Create a Notification Rule](https://docs.aws.amazon.com/codestar-notifications/latest/userguide/notification-rule-create.html)in the*AWS Developer Tools Console User Guide*.- 
                    For API details, see [ListTagsForResource](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codestar-notifications/list-tags-for-resource.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `list-targets`.

- **AWS CLI**
- 
            
                    **To retrieve a list of notification rule targets**The following `list-targets`example retrieves a list of all notification rule targets in the specified AWS Region.`aws codestar-notifications list-targets \ --region``us-east-1`Output: `{ "Targets": [ { "TargetAddress": "arn:aws:sns:us-east-1:123456789012:MySNSTopicForNotificationRules", "TargetType": "SNS", "TargetStatus": "ACTIVE" }, { "TargetAddress": "arn:aws:sns:us-east-1:123456789012:MySNSTopicForNotificationsAboutMyDemoRepo", "TargetType": "SNS", "TargetStatus": "ACTIVE" } ] }`For more information, see [View Notification Rule Targets](https://docs.aws.amazon.com/codestar-notifications/latest/userguide/notification-target-view.html)in the*AWS Developer Tools Console User Guide*.- 
                    For API details, see [ListTargets](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codestar-notifications/list-targets.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `subscribe`.

- **AWS CLI**
- 
            
                    **To add a target to a notification rule**The following `subscribe`example adds an Amazon SNS topic as a target for the specified notification rule.`aws codestar-notifications subscribe \ --arn``arn:aws:codestar-notifications:us-east-1:123456789012:notificationrule/dc82df7a-EXAMPLE`\ --target`TargetType=SNS,TargetAddress=arn:aws:sns:us-east-1:123456789012:MyNotificationTopic`Output: `{ "Arn": "arn:aws:codestar-notifications:us-east-1:123456789012:notificationrule/dc82df7a-EXAMPLE" }`For more information, see [Add or Remove an Amazon SNS Topic as a Target for a Notification Rule](https://docs.aws.amazon.com/codestar-notifications/latest/userguide/notification-target-change-rule.html)in the*AWS Developer Tools Console User Guide*.- 
                    For API details, see [Subscribe](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codestar-notifications/subscribe.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `tag-resource`.

- **AWS CLI**
- 
            
                    **To add a tag to a notification rule**The following `tag-resource`example adds a tag with the key name of`Team`and the value of`Li_Juan`to the specified notification rule.`aws codestar-notifications tag-resource \ --arn``arn:aws:codestar-notifications:us-east-1:123456789012:notificationrule/fe1efd35-EXAMPLE`\ --tags`Team=Li_Juan`Output: `{ "Tags": { "Team": "Li_Juan" } }`For more information, see [Create a Notification Rule](https://docs.aws.amazon.com/codestar-notifications/latest/userguide/notification-rule-create.html)in the*AWS Developer Tools Console User Guide*.- 
                    For API details, see [TagResource](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codestar-notifications/tag-resource.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `unsubscribe`.

- **AWS CLI**
- 
            
                    **To remove a target from a notification rule**The following `unsubscribe`example removes an Amazon SNS topic as a target from the specified notification rule.`aws codestar-notifications unsubscribe \ --arn``arn:aws:codestar-notifications:us-east-1:123456789012:notificationrule/dc82df7a-EXAMPLE`\ --target`TargetType=SNS,TargetAddress=arn:aws:sns:us-east-1:123456789012:MyNotificationTopic`Output: `{ "Arn": "arn:aws:codestar-notifications:us-east-1:123456789012:notificationrule/dc82df7a-EXAMPLE" "TargetAddress": "arn:aws:sns:us-east-1:123456789012:MyNotificationTopic" }`For more information, see [Add or Remove an Amazon SNS Topic as a Target for a Notification Rule](https://docs.aws.amazon.com/codestar-notifications/latest/userguide/notification-target-change-rule.html)in the*AWS Developer Tools Console User Guide*.- 
                    For API details, see [Unsubscribe](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codestar-notifications/unsubscribe.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `untag-resource`.

- **AWS CLI**
- 
            
                    **To remove a tag from a notification rule**The following `untag-resource`example removes the tag with the key name`Team`from the specified notification rule.`aws codestar-notifications untag-resource \ --arn``arn:aws:codestar-notifications:us-east-1:123456789012:notificationrule/fe1efd35-EXAMPLE`\ --tag-keys`Team`This command produces no output. For more information, see [Edit a Notification Rule](https://docs.aws.amazon.com/codestar-notifications/latest/userguide/notification-rule-edit.html)in the*AWS Developer Tools Console User Guide*.- 
                    For API details, see [UntagResource](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codestar-notifications/untag-resource.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `update-notification-rule`.

- **AWS CLI**
- 
            
                    **To update a notification rule**The following `update-notification-rule`example updates a notification rule named`MyNotificationRule`in the AWS account`123456789012`using a JSON file named`update.json`.`aws codestar-notifications update-notification-rule \ --cli-input-json``file://update.json`Contents of `update.json`:`{ "Name": "MyUpdatedNotificationRule", "EventTypeIds": [ "codecommit-repository-branches-and-tags-created" ], "Resource": "arn:aws:codecommit:us-east-1:123456789012:MyDemoRepo", "Targets": [ { "TargetType": "SNS", "TargetAddress": "arn:aws:sns:us-east-1:123456789012:MyNotificationTopic" } ], "Status": "ENABLED", "DetailType": "FULL" }`Output: `{ "Arn": "arn:aws:codestar-notifications:us-east-1:123456789012:notificationrule/dc82df7a-EXAMPLE" }`For more information, see [Edit a notification rule](https://docs.aws.amazon.com/dtconsole/latest/userguide/notification-rule-edit.html)in the*AWS Developer Tools Console User Guide*.- 
                    For API details, see [UpdateNotificationRule](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codestar-notifications/update-notification-rule.html)in*AWS CLI Command Reference*.
 
-