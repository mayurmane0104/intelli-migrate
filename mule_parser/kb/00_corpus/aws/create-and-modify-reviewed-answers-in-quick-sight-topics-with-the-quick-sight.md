# Create and modify reviewed answers in Quick Sight topics with the Quick Sight APIs - Amazon Quick

**Source:** [https://docs.aws.amazon.com/quick/latest/userguide/topic-reviewed-answer-apis.html](https://docs.aws.amazon.com/quick/latest/userguide/topic-reviewed-answer-apis.html)

---

After you create a Quick Sight topic, you can use the Quick Sight APIs to create, list, update, and delete reiewed answers for topics.

The command below batch creates up to 100 reviewed answers for a Quick Sight topic.

`aws quicksight batch-create-topic-reviewed-answer \ --topic-id``TOPICID`\ --aws-account-id`AWSACCOUNTID`\ —answers`ANSWERS`

You can also batch create reviewed answers from a CLI skeleton file with the
                following command. For more information about CLI skeleton files, see [Using CLI skeleton files](https://docs.aws.amazon.com/quicksight/latest/developerguide/cli-skeletons.html) in the *Amazon Quick Sight Developer
                    Guide*.

`aws quicksight batch-create-topic-reviewed-answer \ --cli-input-json``file://createTopicReviewedAnswer.json`

The command below lists all reviewed answers in a Quick Sight topic.

`aws quicksight list-topic-reviewed-answers \ --aws-account-id``AWSACCOUNTID`\ --topic-id`TOPICID`\

The example below batch deletes up to 100 reviewed answers from a topic.

`aws quicksight batch-delete-topic-reviewed-answer \ --topic-id``TOPICID`\ --aws-account-id`AWSACCOUNTID`\ —answer-ids: [`"AnswerId1, AnswerId2…"`]

You can also batch create topic reviewed answers form a CLI skeleton file with the
                following command. For more information about CLI skeleton files, see [Using CLI skeleton files](https://docs.aws.amazon.com/quicksight/latest/developerguide/cli-skeletons.html) in the *Amazon Quick Sight Developer
                    Guide*.

`aws quicksight batch-delete-topic-reviewed-answer \ --cli-input-json``file://deleteTopicReviewedAnswer.json`

To update a reviewed answer, delete the existing answer from the topic with the
                    `batch-delete-topic-reviewed-answer` API. Then, use the
                    `batch-create-topic-reviewed-answer` API to add the updated reviewed
                answer to the topic.