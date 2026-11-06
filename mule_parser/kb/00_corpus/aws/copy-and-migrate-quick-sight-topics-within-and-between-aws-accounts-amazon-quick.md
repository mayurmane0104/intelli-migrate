# Copy and migrate Quick Sight topics within and between AWS accounts - Amazon Quick

**Source:** [https://docs.aws.amazon.com/quick/latest/userguide/topic-cli-walkthroughs.html](https://docs.aws.amazon.com/quick/latest/userguide/topic-cli-walkthroughs.html)

---

You can migrate your Quick Sight topics from one account to another with the Quick Sight command line interface (CLI). Instead of manually replicating the same topic across multiple dashboards, namespaces, or accounts, you can use the Quick Sight CLI to reuse the same topic repeatedly. This capability saves Quick Sight authors time and creates a standardized topic experience for dashboard readers across multiple dashboards.

To migrate topics with the Quick Sight CLI, use the following procedure

###### To migrate a topic to another account

- 
                    First, identify the topic that you want to migrate. You can view a list of every topic in your Quick account with a `list-topics`API command.`aws quicksight list-topics --aws-account-id``AWSACCOUNTID`
- 
                    After you have a list of topics, locate the topic that you want to migrate and make a `describe-topic`call to receive a JSON structure of the topic's configuration.`aws quicksight describe-topic --aws-account-id``AWSACCOUNTID`--topic-id`TOPICID`Following is an example of a `describe-topic`API response.`{ "Status": 200, "TopicId": "TopicExample", "Arn": "string", "Topic": [ { "Name": "{}", "DataSets": [ { "DataSetArn": "{}", "DataSetName": "{}", "DataSetDescription": "{}", "DataAggregation": "{}", "Filters": [], "Columns": [], "CalculatedFields": [], "NamedEntities": [] } ] } ], "RequestId": "requestId" }`
- 
                    Use the JSON response to create a skeleton file that you can input into a new `create-topic`call in your other Quick account. Before you make an API call with your skeleton file, make sure to change the AWS account ID and dataset ID in the skeleton file to match the AWS account ID and dataset ID that you are adding the new topic to. For more information about CLI skeleton files, see[Using CLI skeleton files](https://docs.aws.amazon.com/quicksight/latest/developerguide/cli-skeletons.html)in the*Amazon Quick Sight Developer Guide*.`aws quicksight create-topic --aws-account-id``AWSACCOUNTID`\ --cli-input-json`file://./create-topic-cli-input.json`

After you make a `create-topic` call to the Quick Sight API, the new
                topic appears in your account. To confirm that the new topic exists, make a
                    `list-topics` call to the Quick Sight API. If the source topic that
                was duplicated contains verified answers, the answers are not migrated to the new
                topic. To see a list of all verified answers that are configured to the original
                topic, use a `describe-topic` API call.