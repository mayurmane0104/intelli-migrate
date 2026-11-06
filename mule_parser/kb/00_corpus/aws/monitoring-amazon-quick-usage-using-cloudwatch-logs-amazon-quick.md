# Monitoring Amazon Quick usage using CloudWatch Logs - Amazon Quick

**Source:** [https://docs.aws.amazon.com/quick/latest/userguide/monitoring-quicksuite-chat-feedback-cloudwatch.html](https://docs.aws.amazon.com/quick/latest/userguide/monitoring-quicksuite-chat-feedback-cloudwatch.html)

---

You can use [Amazon CloudWatch Logs](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/AWS-logs-and-resource-policy.html) to deliver chat conversations, user feedback, agent/research hours usage, and index storage usage in Amazon Quick for you to analyze. These logs can be delivered to multiple destinations, such as CloudWatch, Amazon S3, or Amazon Data Firehose (standard rates apply). We recommend that you set up vended logs shortly after enabling Amazon Quick AI features.

The following are examples of tasks you can complete with logs from Amazon Quick:

- 
                Identify common user queries and pain points by reviewing the chat message content. 
- 
                Monitor the quality of responses by looking at metrics like `feedbackReason`.
- 
                Understand user sentiment and satisfaction by analyzing the feedback data, including comments and usefulness ratings. 
- 
                Generate custom dashboards and reports to track key metrics and trends over time. 
- 
                Identify and Analyze cases where the chat returned no answer or the user query was blocked 
- 
                Monitor agent and research hours usage 
- 
                Track index storage usage across knowledge bases and Spaces 

###### Important

Logs from conversations might include sensitive or personally identifiable data passed in the chats. You can filter out this information from your logs when setting up logs subscription. Or you can mask this data on your logs using CloudWatch Logs masking policies. For more information, see [Help protect sensitive log data with masking](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/mask-sensitive-log-data.html).

## Supported log destinations

            Amazon Quick can deliver logs to the following destinations:

- 
                    **Amazon CloudWatch Logs**- For real-time monitoring and analysis
- 
                    **Amazon S3**- For long-term storage and batch processing
- 
                    **Amazon Data Firehose**- For streaming analytics and data transformation

## Prerequisites

            Before you can enable logging, ensure you have:

- 
                    An active Amazon Quick instance with Enterprise or Professional subscriptions 
- 
                    Appropriate IAM permissions to configure log delivery 
- 
                    A destination configured for your logs (CloudWatch Logs, Amazon S3 bucket, or Firehose) 

## Configure logging

            To enable logging for Amazon Quick chat and feedback, you need to configure IAM permissions, create a delivery source and destination, and verify that logs are being delivered successfully.

### Set up IAM permissions

To set up CloudWatch Logs for Amazon Quick, use the following IAM policy examples to grant the necessary permissions.

```
{
    "Version": "2012-10-17",
    "Statement": [{
        "Sid": "QuicksightLogDeliveryPermissions",
        "Effect": "Allow",
        "Action": "quicksight:AllowVendedLogDeliveryForResource",
        "Resource": "arn:aws:quicksight:region:account-id:account/account-id"
    }]
}
```
You must also allow the `delivery.logs.amazonaws.com` service principal in your customer managed AWS KMS key policy.

```
{
    "Effect": "Allow",
    "Principal": {
        "Service": "delivery.logs.amazonaws.com"
    },
    "Action": [
        "kms:GenerateDataKey",
        "kms:Decrypt"
    ],
    "Resource": "*",
    "Condition": {
        "StringEquals": {
            "kms:EncryptionContext:SourceArn": "arn:partition:logs:region:account-id:*"
        }
    }
}
```
### Configure log subscription

For example IAM policies with all the required permissions for your specific logging destination, see [Enable logging from AWS services](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/AWS-logs-and-resource-policy.html) in the *Amazon CloudWatch Logs User Guide*.

Create a delivery source with the [PutDeliverySource](https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_PutDeliverySource.html) CloudWatch Logs API operation. Give the delivery source a name and for `resourceArn`, specify the ARN of your application. For `logType`, specify `CHAT_LOGS`, `AGENT_HOURS_LOGS`, `FEEDBACK_LOGS`, or `INDEX_USAGE_LOGS`.

```
{
    "logType": "CHAT_LOGS",
    "name": "my-quick-suite-delivery-source",
    "resourceArn": "arn:aws:quicksight:your-region:your-account-id:account/account-id"
}
```
```
{
    "logType": "FEEDBACK_LOGS",
    "name": "my-quick-suite-delivery-source",
    "resourceArn": "arn:aws:quicksight:your-region:your-account-id:account/account-id"
}
```
```
{
    "logType": "AGENT_HOURS_LOGS",
    "name": "my-quick-suite-delivery-source",
    "resourceArn": "arn:aws:quicksight:your-region:your-account-id:account/account-id"
}
```
```
{
    "logType": "INDEX_USAGE_LOGS",
    "name": "my-quick-index-usage-delivery-source",
    "resourceArn": "arn:aws:quicksight:your-region:your-account-id:account/account-id"
}
```
To enable user conversation logging with the CloudWatch Logs API operations, you call the `PutDeliverySource`, `PutDeliveryDestination`, and `CreateDelivery` API operations.

###### Note

Logs would be available for the region mentioned in resource ARN in `PutDeliverySource` input.

### Verify log delivery

Once configured, verify that logs are being delivered to your destination:

- 
                        **Verify the setup:**Verify the list of deliveries that have been created in the account by using the`DescribeDeliveries`API in CloudWatch Logs.
- 
                        **CloudWatch Logs**: Check the specified log group for new log streams.
- 
                        **Amazon S3**: Monitor your bucket for new log files.
- 
                        **Firehose**: Verify data is flowing through your delivery stream.

## Log schema and format

            Amazon Quick logs follow a structured schema with common fields shared across all log types and specific fields for chat and feedback logs.

### Common fields

All log events include these common fields:

- 
                        `resource_arn`- Resource ARN of your Amazon Quick account (for example,`arn:aws:quicksight:us-east-1:111122223333:account/111122223333:`)
- 
                        `event_timestamp`- ISO 8601 timestamp of the event (for example,`1763532110061`)
- 
                        `logType`- Type of log (for example,`Chat`or`Feedback`)
- 
                        `accountId`- AWS account ID (for example,`123456789012`)
- 
                        `user_arn`- Amazon Quick user ARN associated with the event (for example,`"arn:aws:quicksight:us-west-2:111122223333:user/default/user"`)

### Chat logs

Chat logs capture conversation interactions and contains below fields:

- 
                        `status_code`- Status of the chat request (for example,`Success, request_blocked, no_answer_found`)
- 
                        `namespace*`- Amazon Quick namespace for the event (for example,`default`)
- 
                        `user_type`- Amazon Quick user type associated with the event (for example,`ADMIN_PRO`)
- 
                        `conversation_id`- Unique ID for the user conversation
- 
                        `system_message_id`- System-generated message ID
- 
                        `latency*`- Chat message latency in milliseconds
- 
                        `time_to_first_token*`- Time in milliseconds of first response token
- 
                        `message_scope`- Scope of the message (for example,`all_resources, specific_resources, no_resources`)
- 
                        `user_message_id`- Unique ID of the user message
- 
                        `user_message`- user message in the conversation
- 
                        `agent_id`- Unique ID of the chat agent
- 
                        `flow_id`- Unique ID of the Amazon Quick Flow
- 
                        `system_text_message`- System response in the conversation
- 
                        `surface_type*`- Application being used for the conversation
- 
                        `web_search*`- Web search enabled or not
- 
                        `user_selected_resources`- List of resources selected by user
- 
                        `action_connectors`- List of action connectors
- 
                        `cited_resource`- List of cited resources
- 
                        `file_attachment`- List of files attached by user

The following is an example of chat logs:

```
{
    "status_code": "success",
    "namespace": "default",
    "user_type": "ADMIN_PRO",
    "conversation_id": "a11b2bbc-c123-3abc-a12b-12a34b5c678d",
    "system_message_id": "a11b2bbc-c123-3abc-a12b-12a34b5c678d",
    "latency": "10000", 
    "time_to_first_token": "10000",
    "message_scope": "all_resources",
    "user_message_id": "a11b2bbc-c123-3abc-a12b-12a34b5c678d",
    "user_message": "Hi chat",
    "agent_id": "a11b2bbc-c123-3abc-a12b-12a34b5c678d",
    "flow_id": "a11b2bbc-c123-3abc-a12b-12a34b5c678d?",
    "system_text_message": "Hello user",
    "surface_type": "WEB_EXPERIENCE",
    "web_search": "true"
    "user_selected_resources": [{"resource_type": "Dashboard","resource_id": "146abs-1222-534894"},{"resource_type": "Space","resource_id": "123abs-1234-534894"}],
    "action_connectors": [{"action_connector_id": "quicksight-website"},{"action_connector_id": "123abs-1234-534894"}]
    "cited_resource": [{"cited_resource_name": "Dashboard","cited_resource_id": "146abs-1222-534894","cited_resource_name": "ds1"},{"cited_resource_name": "Space","cited_resource_id": "123abs-1234-534894","cited_resource_name": "space1"}],
    "file_attachment": [{"file_attachmet_type": "pdf","file_attachment_name": "file1.pdf"},{"file_attachmet_type": "txt","file_attachment_name": "file2.txt"}]
}
```
### Feedback logs

Feedback logs capture user feedback on chat and contains below fields:

- 
                        `status_code`- Status of the event delivery
- 
                        `namespace*`- Amazon Quick namespace for the event (for example,`default`)
- 
                        `user_type`- Amazon Quick user type associated with the event (for example,`ADMIN_PRO`)
- 
                        `conversation_id`- Unique ID of the conversation
- 
                        `system_message_id`- System generated message ID
- 
                        `user_message_id`- Unique ID of user message
- 
                        `feedback_type`- Type of feedback (for example,`Not Useful, Useful`)
- 
                        `feedback_reason`- Feedback reason selected by the user
- 
                        `feedback_details`- (Optional) Additional details provided by the user

The following is an example of feedback logs:

```
{
    "status_code": "success",
    "namespace": "default",
    "user_type": "ADMIN_PRO",
    "conversation_id": "a11b2bbc-c123-3abc-a12b-12a34b5c678d",
    "system_message_id": "a11b2bbc-c123-3abc-a12b-12a34b5c678d",
    "user_message_id" : "a11b2bbc-c123-3abc-a12b-12a34b5c678d",
    "feedback_type" :"Not Useful / Useful"
    "feedback_reason" : "Too wordy,Issue with sources,Other etc."
    "feedback_details" : "additional text shared by user"
}
```
## Agent/Research hours Logs

                This log type captures the usage logs for different agents within your Quick account used for pricing:

- 
                        `subscription_type`- ENTERPRISE or PROFESSIONAL
- 
                        `reporting_service`- Service corresponding to the agent: RESEARCH, FLOWS OR AUTOMATIONS
- 
                        `usage_group`-`Included or Extra`based on the subscription type and usage so far
- 
                        `usage_hours`- Decimal value indicating the usage hours for the particular log instance
- 
                        `service_resource_arn`- ARN of the corresponding Agent’s service

The following is an example of Agent Hours logs:

```
{
    "subscription_type": "ENTERPRISE",
    "reporting_service": "RESEARCH",
    "usage_group": "Included",
    "usage_hours": 0.3333,
    "service_resource_arn": "arn:aws:quicksight:eu-west-1:111222333444:research/a11b2bbc-c123-3abc-a12b-12a34b5c678d"
}
```
## Index usage logs

            Index usage logs capture per-source storage metrics for knowledge bases and Spaces. Events are published whenever a change occurs (created, updated, synced, or deleted).

- 
                    `consumed_index_size`– Total size (in bytes) consumed by the entire index. This is the authoritative total, not computed by summing individual sources.
- 
                    `source_type`– Type of source:`SPACE`or`KB`.
- 
                    `source_name`– Display name of the Space or knowledge base.
- 
                    `source_arn`– Full ARN of the source.
- 
                    `consumed_source_size`– Size (in bytes) consumed by this individual source.
- 
                    `consumed_source_doc_count`– Number of documents in this source.

The following is an example of index usage logs:

```
{
    "account_id": "111122223333",
    "event_timestamp": 1774911984257,
    "log_type": "INDEX_USAGE_LOGS",
    "user_arn": "arn:aws:quicksight::111122223333:user/default/user",
    "resource_arn": "arn:aws:quicksight:us-west-2:111122223333:account/111122223333",
    "consumed_index_size": 500000,
    "source_type": "SPACE",
    "source_name": "my-space",
    "source_arn": "arn:aws:quicksight:us-west-2:111122223333:space/2744af89-31b2-423b-93a2-69b0cd0d7fa1",
    "consumed_source_size": 244436,
    "consumed_source_doc_count": 2
}
```
###### Note

Events are published per source on change. Not all sources
                    emit events every day. To reconstruct the current state, use
                    the most recent event per `source_arn`.

For information about building dashboards and running queries
                against index usage logs, see
                [Monitor index storage usage](./index-usage-monitoring.html).

###### Note

* Fields marked with ‘*’ do not get added by default to your log subscription. These need to be specified explicitly while calling CreateDelivery if required.

## Security considerations

            - 
                    **Encryption**: Use customer-managed AWS KMS keys for sensitive data
- 
                    **Access control**: Implement least-privilege IAM policies
- 
                    **Data retention**: Configure appropriate retention policies for your compliance requirements