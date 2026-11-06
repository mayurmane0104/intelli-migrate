# Configure Quick Sight topic refresh schedules with the Quick Sight CLI - Amazon Quick

**Source:** [https://docs.aws.amazon.com/quick/latest/userguide/topic-refresh-apis.html](https://docs.aws.amazon.com/quick/latest/userguide/topic-refresh-apis.html)

---

The following command creates a refresh schedule of a topic.

`aws quicksight create-topic-refresh-schedule --aws-account-id``AWSACCOUNTID`--topic-id`TOPICID`--dataset-arn`DATASETARN`--refresh-schedule`REFRESHSCHEDULE`

After you create a refresh schedule for a topic, you can update, delete, list, or request a summary of the topic's refresh schedule.

The following command updates the refresh schedule of a topic.

`aws quicksight update-topic-refresh-schedule --aws-account-id``AWSACCOUNTID`--topic-id`TOPICID`--dataset-id`DATASETID`--refresh-schedule`REFRESHSCHEDULE`

The following example provides a list of all refresh schedules configured to a topic.

`aws quicksight list-topic-refresh-schedules --aws-account-id``AWSACCOUNTID`--topic-id`TOPICID`

The following example deletes a topic refresh schedule.

`aws quicksight delete-topic-refresh-schedule --aws-account-id``AWSACCOUNTID`--topic-id`TOPICID`--dataset-id`DATASETID`

The following example provides information about how a topic refresh schedule was configured.

`aws quicksight describe-topic-refresh-schedule --aws-account-id``AWSACCOUNTID`--topic-id`TOPICID`--dataset-id`DATASETID`