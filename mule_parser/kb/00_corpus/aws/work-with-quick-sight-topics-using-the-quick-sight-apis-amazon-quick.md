# Work with Quick Sight topics using the Quick Sight APIs - Amazon Quick

**Source:** [https://docs.aws.amazon.com/quick/latest/userguide/topic-cli-examples.html](https://docs.aws.amazon.com/quick/latest/userguide/topic-cli-examples.html)

---

The following example creates a new topic.

`aws quicksight create-topic --aws-account-id``AWSACCOUNTID`--topic-id`TOPICID`--topic`TOPIC`

You can also create a new topic by using a CLI skeleton file with the following
                command. For more information about CLI skeleton files, see [Using CLI skeleton files](https://docs.aws.amazon.com/quicksight/latest/developerguide/cli-skeletons.html) in the *Amazon Quick Sight Developer
                    Guide*.

`aws quicksight create-topic --cli-input-json file://createtopic.json`

When you create a new topic, the dataset refresh configuration is not copied to
                the topic. To set a topic refresh schedule for your new topic, you can make a
                    `create-topic-refresh-schedule` API call. For more information about
                configuring topic refresh schedules with the CLI, see [Configure Quick Sight topic refresh schedules with the Quick Sight CLI](./topic-refresh-apis.html).

After you create your first topic, you can update, delete, list, or request a summary of a topic.

The following example updates a topic.

`aws quicksight update-topic --aws-account-id``AWSACCOUNTID`--topic-id`TOPICID`--topic`TOPIC`

You can also update a topic by using a CLI skeleton file with the following
                command. For more information about CLI skeleton files, see [Using CLI skeleton files](https://docs.aws.amazon.com/quicksight/latest/developerguide/cli-skeletons.html) in the *Amazon Quick Sight Developer
                    Guide*.

`aws quicksight update-topic --cli-input-json file://updatetopic.json`

The following example provides a list of all topics in a Quick account.

`aws quicksight list-topics --aws-account-id``AWSACCOUNTID`

The following example deletes a topic.

`aws quicksight delete-topic --aws-account-id``AWSACCOUNTID`--topic-id`TOPICID`

The following example provides information about how a topic was configured.

`aws quicksight describe-topic --aws-account-id``AWSACCOUNTID`--topic-id`TOPICID`

The following command updates the permissions of a topic.

`aws quicksight update-topic-permissions --aws-account-id``AWSACCOUNTID`--topic-id`TOPICID`--grant-permissions Principal=arn:aws:quicksight:`us-east-1`:`AWSACCOUNTID`:user/default/`USERNAME`,Actions=quicksight:DescribeTopic --revoke-permissions Principal=arn:aws:quicksight:`us-east-1`:`AWSACCOUNTID`:user/default/`USERNAME`,Actions=quicksight:DescribeTopic

Use the `grant-permissions` parameter to grant read and author
                permissions to Quick account users. To grant read permissions to an
                account user, enter the following value: `"quicksight:DescribeTopic"`. To
                grant permissions to an account user, enter the following values:

- 
                    `"quicksight:DescribeTopic"`
- 
                    `"quicksight:DescribeTopicRefresh"`
- 
                    `"quicksight:ListTopicRefreshSchedules"`
- 
                    `"quicksight:DescribeTopicRefreshSchedule"`
- 
                    `"quicksight:DeleteTopic"`
- 
                    `"quicksight:UpdateTopic"`
- 
                    `"quicksight:CreateTopicRefreshSchedule"`
- 
                    `"quicksight:DeleteTopicRefreshSchedule"`
- 
                    `"quicksight:UpdateTopicRefreshSchedule"`
- 
                    `"quicksight:DescribeTopicPermissions"`
- 
                    `"quicksight:UpdateTopicPermissions"`

The `RevokePermissions` parameter revokes all permissions granted to an
                account user.

The following command describes all permissions from a topic.

`aws quicksight describe-topic-permissions --aws-account-id``AWSACCOUNTID`--topic-id`TOPICID`

After you create a Quick Sight topic, you can use the Amazon Quick Sight APIs to [configure
                    a topic refresh schedule](https://docs.aws.amazon.com/quicksuite/latest/userguide/topic-refresh-apis), [migrate Quick Sight
                    topics within or between accounts](https://docs.aws.amazon.com/quicksuite/latest/userguide/topic-cli-walkthroughs), and [ create reviewed
                    answers](https://docs.aws.amazon.com/quicksuite/latest/userguide/topic-reviewed-answer-apis).