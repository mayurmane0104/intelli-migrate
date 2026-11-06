# Incident Manager Contacts examples using AWS CLI - AWS Command Line Interface

**Source:** [https://docs.aws.amazon.com/cli/latest/userguide/cli_ssm-contacts_code_examples.html](https://docs.aws.amazon.com/cli/latest/userguide/cli_ssm-contacts_code_examples.html)

---

The following code examples show you how to perform actions and implement common scenarios by using the AWS Command Line Interface with Incident Manager Contacts.

*Actions* are code excerpts from larger programs and must be run in context. While actions show you how to call individual service functions, you can see actions in context in their related scenarios.

Each example includes a link to the complete source code, where you can find instructions on how to set up and run the code in context.

###### Topics

## Actions

    The following code example shows how to use `accept-page`.

- **AWS CLI**
- 
            
                    **To accept a page during and engagement**The following `accept-page`example uses an accept code sent to the contact channel to accept a page.`aws ssm-contacts accept-page \ --page-id``"arn:aws:ssm-contacts:us-east-2:682428703967:page/akuam/94ea0c7b-56d9-46c3-b84a-a37c8b067ad3"`\ --accept-type`READ`\ --accept-code`425440`This command produces no output For more information, see [Contacts](https://docs.aws.amazon.com/incident-manager/latest/userguide/contacts.html)in the*Incident Manager User Guide*.- 
                    For API details, see [AcceptPage](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ssm-contacts/accept-page.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `activate-contact-channel`.

- **AWS CLI**
- 
            
                    **Activate a contact's contact channel**The following `activate-contact-channel`example activates a contact channel and makes it usable as part of an incident.`aws ssm-contacts activate-contact-channel \ --contact-channel-id``"arn:aws:ssm-contacts:us-east-2:111122223333:contact-channel/akuam/fc7405c4-46b2-48b7-87b2-93e2f225b90d"`\ --activation-code`"466136"`This command produces no output. For more information, see [Contacts](https://docs.aws.amazon.com/incident-manager/latest/userguide/contacts.html)in the*Incident Manager User Guide*.- 
                    For API details, see [ActivateContactChannel](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ssm-contacts/activate-contact-channel.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `command-name`.

- **AWS CLI**
- 
            
                    **To delete a contact**The following `command-name`example deletes a contact. The contact will no longer be reachable from any escalation plan that refers to them.`aws ssm-contacts delete-contact \ --contact-id``"arn:aws:ssm-contacts:us-east-1:682428703967:contact/alejr"`This command produces no output. For more information, see [Contacts](https://docs.aws.amazon.com/incident-manager/latest/userguide/contacts.html)in the*Incident Manager User Guide*.- 
                    For API details, see [CommandName](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ssm-contacts/command-name.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `create-contact-channel`.

- **AWS CLI**
- 
            
                    **To create a contact channel**Creates a contact channel of type SMS for the contact Akua Mansa. Contact channels can be created of type SMS, EMAIL, or VOICE. `aws ssm-contacts create-contact-channel \ --contact-id``"arn:aws:ssm-contacts:us-east-1:111122223333:contact/akuam"`\ --name`"akuas sms-test"`\ --type`SMS`\ --delivery-address '`{"SimpleAddress": "+15005550199"}`'Output: `{ "ContactChannelArn": "arn:aws:ssm-contacts:us-east-1:111122223333:contact-channel/akuam/02f506b9-ea5d-4764-af89-2daa793ff024" }`For more information, see [Contacts](https://docs.aws.amazon.com/incident-manager/latest/userguide/contacts.html)in the*Incident Manager User Guide*.- 
                    For API details, see [CreateContactChannel](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ssm-contacts/create-contact-channel.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `create-contact`.

- **AWS CLI**
- 
            
                    **To create a contact**The following `create-contact`example creates a contact in your environment with a blank plan. The plan can be updated after creating contact channels. Use the create-contact-channel command with the output ARN of this command. After you have created contact channels for this contact use update-contact to update the plan.`aws ssm-contacts create-contact \ --alias``"akuam"`\ --display-name`"Akua Mansa"`\ --type`PERSONAL`\ --plan '`{"Stages": []}`'Output: `{ "ContactArn": "arn:aws:ssm-contacts:us-east-2:111122223333:contact/akuam" }`For more information, see [Contacts](https://docs.aws.amazon.com/incident-manager/latest/userguide/contacts.html)in the*Incident Manager User Guide*.- 
                    For API details, see [CreateContact](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ssm-contacts/create-contact.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `deactivate-contact-channel`.

- **AWS CLI**
- 
            
                    **To deactivate a contact channel**The following `deactivate-contact-channel`example deactivates a contact channel. Deactivating a contact channel means the contact channel will no longer be paged during an incident. You can also reactivate a contact channel at any time using the`activate-contact-channel`command.`aws ssm-contacts deactivate-contact-channel \ --contact-channel-id``"arn:aws:ssm-contacts:us-east-2:111122223333:contact-channel/akuam/fc7405c4-46b2-48b7-87b2-93e2f225b90d"`This command produces no output. For more information, see [Contacts](https://docs.aws.amazon.com/incident-manager/latest/userguide/contacts.html)in the*Incident Manager User Guide*.- 
                    For API details, see [DeactivateContactChannel](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ssm-contacts/deactivate-contact-channel.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `delete-contact-channel`.

- **AWS CLI**
- 
            
                    **To delete a contact channel**The following `delete-contact-channel`example deletes a contact channel. Deleting a contact channel ensures the contact channel will not be paged during an incident.`aws ssm-contacts delete-contact-channel \ --contact-channel-id``"arn:aws:ssm-contacts:us-east-1:111122223333:contact-channel/akuam/13149bad-52ee-45ea-ae1e-45857f78f9b2"`This command produces no output. For more information, see [Contacts](https://docs.aws.amazon.com/incident-manager/latest/userguide/contacts.html)in the*Incident Manager User Guide*.- 
                    For API details, see [DeleteContactChannel](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ssm-contacts/delete-contact-channel.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `delete-contact`.

- **AWS CLI**
- 
            
                    **To delete a contact**The following `delete-contact`example deletes a contact. The contact will no longer be reachable from any escalation plan that refers to them.`aws ssm-contacts delete-contact \ --contact-id``"arn:aws:ssm-contacts:us-east-1:111122223333:contact/alejr"`This command produces no output. For more information, see [Contacts](https://docs.aws.amazon.com/incident-manager/latest/userguide/contacts.html)in the*Incident Manager User Guide*.- 
                    For API details, see [DeleteContact](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ssm-contacts/delete-contact.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `describe-engagement`.

- **AWS CLI**
- 
            
                    **To describe the details of an engagement**The following `describe-engagement`example lists the details of an engagement to a contact or escalation plan. The subject and content are sent to the contact channels.`aws ssm-contacts describe-engagement \ --engagement-id``"arn:aws:ssm-contacts:us-east-2:111122223333:engagement/example_escalation/69e40ce1-8dbb-4d57-8962-5fbe7fc53356"`Output: `{ "ContactArn": "arn:aws:ssm-contacts:us-east-2:111122223333:contact/example_escalation", "EngagementArn": "arn:aws:ssm-contacts:us-east-2:111122223333:engagement/example_escalation/69e40ce1-8dbb-4d57-8962-5fbe7fc53356", "Sender": "cli", "Subject": "cli-test", "Content": "Testing engagements via CLI", "PublicSubject": "cli-test", "PublicContent": "Testing engagements va CLI", "StartTime": "2021-05-18T18:25:41.151000+00:00" }`For more information, see [Contacts](https://docs.aws.amazon.com/incident-manager/latest/userguide/contacts.html)in the*Incident Manager User Guide*.- 
                    For API details, see [DescribeEngagement](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ssm-contacts/describe-engagement.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `describe-page`.

- **AWS CLI**
- 
            
                    **To list the details of a page to a contact channel**The following `describe-page`example lists details of a page to a contact channel. The page will include the subject and content provided.`aws ssm-contacts describe-page \ --page-id``"arn:aws:ssm-contacts:us-east-2:111122223333:page/akuam/ad0052bd-e606-498a-861b-25726292eb93"`Output: `{ "PageArn": "arn:aws:ssm-contacts:us-east-2:111122223333:page/akuam/ad0052bd-e606-498a-861b-25726292eb93", "EngagementArn": "arn:aws:ssm-contacts:us-east-2:111122223333:engagement/akuam/78a29753-3674-4ac5-9f83-0468563567f0", "ContactArn": "arn:aws:ssm-contacts:us-east-2:111122223333:contact/akuam", "Sender": "cli", "Subject": "cli-test", "Content": "Testing engagements via CLI", "PublicSubject": "cli-test", "PublicContent": "Testing engagements va CLI", "SentTime": "2021-05-18T18:43:29.301000+00:00", "ReadTime": "2021-05-18T18:43:55.708000+00:00", "DeliveryTime": "2021-05-18T18:43:55.265000+00:00" }`For more information, see [Contacts](https://docs.aws.amazon.com/incident-manager/latest/userguide/contacts.html)in the*Incident Manager User Guide*.- 
                    For API details, see [DescribePage](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ssm-contacts/describe-page.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `get-contact-channel`.

- **AWS CLI**
- 
            
                    **To list the details of a contact channel**The following `get-contact-channel`example lists the details of a contact channel.`aws ssm-contacts get-contact-channel \ --contact-channel-id``"arn:aws:ssm-contacts:us-east-2:111122223333:contact-channel/akuam/fc7405c4-46b2-48b7-87b2-93e2f225b90d"`Output: `{ "ContactArn": "arn:aws:ssm-contacts:us-east-2:111122223333:contact/akuam", "ContactChannelArn": "arn:aws:ssm-contacts:us-east-2:111122223333:contact-channel/akuam/fc7405c4-46b2-48b7-87b2-93e2f225b90d", "Name": "akuas sms", "Type": "SMS", "DeliveryAddress": { "SimpleAddress": "+15005550199" }, "ActivationStatus": "ACTIVATED" }`For more information, see [Contacts](https://docs.aws.amazon.com/incident-manager/latest/userguide/contacts.html)in the*Incident Manager User Guide*.- 
                    For API details, see [GetContactChannel](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ssm-contacts/get-contact-channel.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `get-contact-policy`.

- **AWS CLI**
- 
            
                    **To list the resource policies of a contact**The following `get-contact-policy`example lists the resource policies associated with the specified contact.`aws ssm-contacts get-contact-policy \ --contact-arn``"arn:aws:ssm-contacts:us-east-1:111122223333:contact/akuam"`Output: `{ "ContactArn": "arn:aws:ssm-contacts:us-east-1:111122223333:contact/akuam", "Policy": "{\"Version\":\"2012-10-17\",\"Statement\":[{\"Sid\":\"SharePolicyForDocumentationDralia\",\"Effect\":\"Allow\",\"Principal\":{\"AWS\":\"222233334444\"},\"Action\":[\"ssm-contacts:GetContact\",\"ssm-contacts:StartEngagement\",\"ssm-contacts:DescribeEngagement\",\"ssm-contacts:ListPagesByEngagement\",\"ssm-contacts:StopEngagement\"],\"Resource\":[\"arn:aws:ssm-contacts:*:111122223333:contact/akuam\",\"arn:aws:ssm-contacts:*:111122223333:engagement/akuam/*\"]}]}" }`For more information, see [Working with shared contacts and response plans](https://docs.aws.amazon.com/incident-manager/latest/userguide/sharing.html)in the*Incident Manager User Guide*.- 
                    For API details, see [GetContactPolicy](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ssm-contacts/get-contact-policy.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `get-contact`.

- **AWS CLI**
- 
            
                    **Example 1: To describe a contact plan**The following `get-contact`example describes a contact.`aws ssm-contacts get-contact \ --contact-id``"arn:aws:ssm-contacts:us-east-2:111122223333:contact/akuam"`Output: `{ "ContactArn": "arn:aws:ssm-contacts:us-east-2:111122223333:contact/akuam", "Alias": "akuam", "DisplayName": "Akua Mansa", "Type": "PERSONAL", "Plan": { "Stages": [ { "DurationInMinutes": 5, "Targets": [ { "ChannelTargetInfo": { "ContactChannelId": "arn:aws:ssm-contacts:us-east-2:111122223333:contact-channel/akuam/beb25840-5ac8-4644-95cc-7a8de390fa65", "RetryIntervalInMinutes": 1 } } ] }, { "DurationInMinutes": 5, "Targets": [ { "ChannelTargetInfo": { "ContactChannelId": "arn:aws:ssm-contacts:us-east-2:111122223333:contact-channel/akuam/49f3c24d-5f9f-4638-ae25-3f49e04229ad", "RetryIntervalInMinutes": 1 } } ] }, { "DurationInMinutes": 5, "Targets": [ { "ChannelTargetInfo": { "ContactChannelId": "arn:aws:ssm-contacts:us-east-2:111122223333:contact-channel/akuam/77d4f447-f619-4954-afff-85551e369c2a", "RetryIntervalInMinutes": 1 } } ] } ] } }`**Example 2: To describe an escalation plan**The following `get-contact`example describes an escalation plan.`aws ssm-contacts get-contact \ --contact-id``"arn:aws:ssm-contacts:us-east-2:111122223333:contact/example_escalation"`Output: `{ "ContactArn": "arn:aws:ssm-contacts:us-east-2:111122223333:contact/example_escalation", "Alias": "example_escalation", "DisplayName": "Example Escalation", "Type": "ESCALATION", "Plan": { "Stages": [ { "DurationInMinutes": 5, "Targets": [ { "ContactTargetInfo": { "ContactId": "arn:aws:ssm-contacts:us-east-2:111122223333:contact/akuam", "IsEssential": true } } ] }, { "DurationInMinutes": 5, "Targets": [ { "ContactTargetInfo": { "ContactId": "arn:aws:ssm-contacts:us-east-2:111122223333:contact/alejr", "IsEssential": false } } ] }, { "DurationInMinutes": 0, "Targets": [ { "ContactTargetInfo": { "ContactId": "arn:aws:ssm-contacts:us-east-2:111122223333:contact/anasi", "IsEssential": false } } ] } ] } }`For more information, see [Contacts](https://docs.aws.amazon.com/incident-manager/latest/userguide/contacts.html)in the*Incident Manager User Guide*.- 
                    For API details, see [GetContact](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ssm-contacts/get-contact.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `list-contact-channels`.

- **AWS CLI**
- 
            
                    **To list the contact channels of a contact**The following `list-contact-channels`example lists the available contact channels of the specified contact.`aws ssm-contacts list-contact-channels \ --contact-id``"arn:aws:ssm-contacts:us-east-2:111122223333:contact/akuam"`Output: `{ [ { "ContactArn": "arn:aws:ssm-contacts:us-east-2:111122223333:contact/akuam", "Name": "akuas email", "Type": "EMAIL", "DeliveryAddress": { "SimpleAddress": "akuam@example.com" }, "ActivationStatus": "NOT_ACTIVATED" }, { "ContactChannelArn": "arn:aws:ssm-contacts:us-east-2:111122223333:contact-channel/akuam/fc7405c4-46b2-48b7-87b2-93e2f225b90d", "ContactArn": "arn:aws:ssm-contacts:us-east-2:111122223333:contact/akuam", "Name": "akuas sms", "Type": "SMS", "DeliveryAddress": { "SimpleAddress": "+15005550100" }, "ActivationStatus": "ACTIVATED" } ] }`For more information, see [Contacts](https://docs.aws.amazon.com/incident-manager/latest/userguide/contacts.html)in the*Incident Manager User Guide*.- 
                    For API details, see [ListContactChannels](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ssm-contacts/list-contact-channels.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `list-contacts`.

- **AWS CLI**
- 
            
                    **To list all escalation plans and contacts**The following `list-contacts`example lists the contacts and escalation plans in your account.`aws ssm-contacts list-contacts`Output: `{ "Contacts": [ { "ContactArn": "arn:aws:ssm-contacts:us-east-2:111122223333:contact/akuam", "Alias": "akuam", "DisplayName": "Akua Mansa", "Type": "PERSONAL" }, { "ContactArn": "arn:aws:ssm-contacts:us-east-2:111122223333:contact/alejr", "Alias": "alejr", "DisplayName": "Alejandro Rosalez", "Type": "PERSONAL" }, { "ContactArn": "arn:aws:ssm-contacts:us-east-2:111122223333:contact/anasi", "Alias": "anasi", "DisplayName": "Ana Carolina Silva", "Type": "PERSONAL" }, { "ContactArn": "arn:aws:ssm-contacts:us-east-2:111122223333:contact/example_escalation", "Alias": "example_escalation", "DisplayName": "Example Escalation", "Type": "ESCALATION" } ] }`For more information, see [Contacts](https://docs.aws.amazon.com/incident-manager/latest/userguide/contacts.html)in the*Incident Manager User Guide*.- 
                    For API details, see [ListContacts](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ssm-contacts/list-contacts.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `list-engagements`.

- **AWS CLI**
- 
            
                    **To list all engagements**The following `list-engagements`example lists engagements to escalation plans and contacts. You can also list engagements for a single incident.`aws ssm-contacts list-engagements`Output: `{ "Engagements": [ { "EngagementArn": "arn:aws:ssm-contacts:us-east-2:111122223333:engagement/akuam/91792571-0b53-4821-9f73-d25d13d9e529", "ContactArn": "arn:aws:ssm-contacts:us-east-2:111122223333:contact/akuam", "Sender": "cli", "StartTime": "2021-05-18T20:37:50.300000+00:00" }, { "EngagementArn": "arn:aws:ssm-contacts:us-east-2:111122223333:engagement/akuam/78a29753-3674-4ac5-9f83-0468563567f0", "ContactArn": "arn:aws:ssm-contacts:us-east-2:111122223333:contact/akuam", "Sender": "cli", "StartTime": "2021-05-18T18:40:26.666000+00:00" }, { "EngagementArn": "arn:aws:ssm-contacts:us-east-2:111122223333:engagement/example_escalation/69e40ce1-8dbb-4d57-8962-5fbe7fc53356", "ContactArn": "arn:aws:ssm-contacts:us-east-2:111122223333:contact/example_escalation", "Sender": "cli", "StartTime": "2021-05-18T18:25:41.151000+00:00" }, { "EngagementArn": "arn:aws:ssm-contacts:us-east-2:111122223333:engagement/akuam/607ced0e-e8fa-4ea7-8958-a237b8803f8f", "ContactArn": "arn:aws:ssm-contacts:us-east-2:111122223333:contact/akuam", "Sender": "cli", "StartTime": "2021-05-18T18:20:58.093000+00:00" } ] }`For more information, see [Contacts](https://docs.aws.amazon.com/incident-manager/latest/userguide/contacts.html)in the*Incident Manager User Guide*.- 
                    For API details, see [ListEngagements](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ssm-contacts/list-engagements.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `list-page-receipts`.

- **AWS CLI**
- 
            
                    **To list page receipts**The following `command-name`example lists whether a page was received or not by a contact.`aws ssm-contacts list-page-receipts \ --page-id``"arn:aws:ssm-contacts:us-east-2:111122223333:page/akuam/94ea0c7b-56d9-46c3-b84a-a37c8b067ad3"`Output: `{ "Receipts": [ { "ContactChannelArn": "arn:aws:ssm-contacts:us-east-2:111122223333:contact-channel/akuam/fc7405c4-46b2-48b7-87b2-93e2f225b90d", "ReceiptType": "DELIVERED", "ReceiptInfo": "425440", "ReceiptTime": "2021-05-18T20:42:57.485000+00:00" }, { "ContactChannelArn": "arn:aws:ssm-contacts:us-east-2:111122223333:contact-channel/akuam/fc7405c4-46b2-48b7-87b2-93e2f225b90d", "ReceiptType": "READ", "ReceiptInfo": "425440", "ReceiptTime": "2021-05-18T20:42:57.907000+00:00" }, { "ContactChannelArn": "arn:aws:ssm-contacts:us-east-2:111122223333:contact-channel/akuam/fc7405c4-46b2-48b7-87b2-93e2f225b90d", "ReceiptType": "SENT", "ReceiptInfo": "SM6656c19132f1465f9c9c1123a5dde7c9", "ReceiptTime": "2021-05-18T20:40:52.962000+00:00" } ] }`For more information, see [Contacts](https://docs.aws.amazon.com/incident-manager/latest/userguide/contacts.html)in the*Incident Manager User Guide*.- 
                    For API details, see [ListPageReceipts](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ssm-contacts/list-page-receipts.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `list-pages-by-contact`.

- **AWS CLI**
- 
            
                    **To list pages by contact**The following `list-pages-by-contact`example lists all pages to the specified contact.`aws ssm-contacts list-pages-by-contact \ --contact-id``"arn:aws:ssm-contacts:us-east-2:111122223333:contact/akuam"`Output: `{ "Pages": [ { "PageArn": "arn:aws:ssm-contacts:us-east-2:111122223333:page/akuam/ad0052bd-e606-498a-861b-25726292eb93", "EngagementArn": "arn:aws:ssm-contacts:us-east-2:111122223333:engagement/akuam/78a29753-3674-4ac5-9f83-0468563567f0", "ContactArn": "arn:aws:ssm-contacts:us-east-2:111122223333:contact/akuam", "Sender": "cli", "SentTime": "2021-05-18T18:43:29.301000+00:00", "DeliveryTime": "2021-05-18T18:43:55.265000+00:00", "ReadTime": "2021-05-18T18:43:55.708000+00:00" } ] }`For more information, see [Contacts](https://docs.aws.amazon.com/incident-manager/latest/userguide/contacts.html)in the*Incident Manager User Guide*.- 
                    For API details, see [ListPagesByContact](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ssm-contacts/list-pages-by-contact.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `list-pages-by-engagement`.

- **AWS CLI**
- 
            
                    **To list pages to contact channels started from an engagement.**The following `list-pages-by-engagement`example lists the pages that occurred while engaging the defined engagement plan.`aws ssm-contacts list-pages-by-engagement \ --engagement-id``"arn:aws:ssm-contacts:us-east-2:111122223333:engagement/akuam/78a29753-3674-4ac5-9f83-0468563567f0"`Output: `{ "Pages": [ { "PageArn": "arn:aws:ssm-contacts:us-east-2:111122223333:page/akuam/ad0052bd-e606-498a-861b-25726292eb93", "EngagementArn": "arn:aws:ssm-contacts:us-east-2:111122223333:engagement/akuam/78a29753-3674-4ac5-9f83-0468563567f0", "ContactArn": "arn:aws:ssm-contacts:us-east-2:111122223333:contact/akuam", "Sender": "cli", "SentTime": "2021-05-18T18:40:27.245000+00:00" } ] }`For more information, see [Contacts](https://docs.aws.amazon.com/incident-manager/latest/userguide/contacts.html)in the*Incident Manager User Guide*.- 
                    For API details, see [ListPagesByEngagement](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ssm-contacts/list-pages-by-engagement.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `list-tags-for-resource`.

- **AWS CLI**
- 
            
                    **To list tags for a contact**The following `list-tags-for-resource`example lists the tags of the specified contact.`aws ssm-contacts list-tags-for-resource \ --resource-arn``"arn:aws:ssm-contacts:us-east-1:111122223333:contact/akuam"`Output: `{ "Tags": [ { "Key": "group1", "Value": "1" } ] }`For more information, see [Tagging](https://docs.aws.amazon.com/incident-manager/latest/userguide/tagging.html)in the*Incident Manager User Guide*.- 
                    For API details, see [ListTagsForResource](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ssm-contacts/list-tags-for-resource.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `put-contact-policy`.

- **AWS CLI**
- 
            
                    **To share a contact and engagements**The following `put-contact-policy`example adds a resource policy to the contact Akua that shares the contact and related engagements with the principal.`aws ssm-contacts put-contact-policy \ --contact-arn``"arn:aws:ssm-contacts:us-east-1:111122223333:contact/akuam"`\ --policy "{\"Version\":\"2012-10-17\",\"Statement\":[{\"Sid\":\"ExampleResourcePolicy\",\"Action\":[\"ssm-contacts:GetContact\",\"ssm-contacts:StartEngagement\",\"ssm-contacts:DescribeEngagement\",\"ssm-contacts:ListPagesByEngagement\",\"ssm-contacts:StopEngagement\"],\"Principal\":{\"AWS\":\"222233334444\"},\"Effect\":\"Allow\",\"Resource\":[\"arn:aws:ssm-contacts:*:111122223333:contact\/akuam\",\"arn:aws:ssm-contacts:*:111122223333:engagement\/akuam\/*\"]}]}"This command produces no output. For more information, see [Working with shared contacts and response plans](https://docs.aws.amazon.com/incident-manager/latest/userguide/sharing.html)in the*Incident Manager User Guide*.- 
                    For API details, see [PutContactPolicy](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ssm-contacts/put-contact-policy.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `send-activation-code`.

- **AWS CLI**
- 
            
                    **To send an activation code**The following `send-activation-code`example sends an activation code and message to the specified contact channel.`aws ssm-contacts send-activation-code \ --contact-channel-id``"arn:aws:ssm-contacts:us-east-1:111122223333:contact-channel/akuam/8ddae2d1-12c8-4e45-b852-c8587266c400"`This command produces no output. For more information, see [Contacts](https://docs.aws.amazon.com/incident-manager/latest/userguide/contacts.html)in the*Incident Manager User Guide*.- 
                    For API details, see [SendActivationCode](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ssm-contacts/send-activation-code.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `start-engagement`.

- **AWS CLI**
- 
            
                    **Example 1: To page a contact's contact channels**The following `start-engagement`pages contact's contact channels. Sender, subject, public-subject, and public-content are all free from fields. Incident Manager sends the subject and content to the provided VOICE or EMAIL contact channels. Incident Manager sends the public-subject and public-content to the provided SMS contact channels. Sender is used to track who started the engagement.`aws ssm-contacts start-engagement \ --contact-id``"arn:aws:ssm-contacts:us-east-2:111122223333:contact/akuam"`\ --sender`"cli"`\ --subject`"cli-test"`\ --content`"Testing engagements via CLI"`\ --public-subject`"cli-test"`\ --public-content`"Testing engagements va CLI"`Output: `{ "EngagementArn": "arn:aws:ssm-contacts:us-east-2:111122223333:engagement/akuam/607ced0e-e8fa-4ea7-8958-a237b8803f8f" }`For more information, see [Contacts](https://docs.aws.amazon.com/incident-manager/latest/userguide/contacts.html)in the*Incident Manager User Guide*.**Example 2: To page a contact in the provided escalation plan.**The following `start-engagement`engages contact's through an escalation plan. Each contact is paged according to their engagement plan.`aws ssm-contacts start-engagement \ --contact-id``"arn:aws:ssm-contacts:us-east-2:111122223333:contact/example_escalation"`\ --sender`"cli"`\ --subject`"cli-test"`\ --content`"Testing engagements via CLI"`\ --public-subject`"cli-test"`\ --public-content`"Testing engagements va CLI"`Output: `{ "EngagementArn": "arn:aws:ssm-contacts:us-east-2:111122223333:engagement/example_escalation/69e40ce1-8dbb-4d57-8962-5fbe7fc53356" }`For more information, see [Contacts](https://docs.aws.amazon.com/incident-manager/latest/userguide/contacts.html)in the*Incident Manager User Guide*.- 
                    For API details, see [StartEngagement](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ssm-contacts/start-engagement.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `stop-engagement`.

- **AWS CLI**
- 
            
                    **To stop an engagement**The following `stop-engagement`example stops an engagement from paging further contacts and contact channels.`aws ssm-contacts stop-engagement \ --engagement-id``"arn:aws:ssm-contacts:us-east-2:111122223333:engagement/example_escalation/69e40ce1-8dbb-4d57-8962-5fbe7fc53356"`This command produces no output. For more information, see [Contacts](https://docs.aws.amazon.com/incident-manager/latest/userguide/contacts.html)in the*Incident Manager User Guide*.- 
                    For API details, see [StopEngagement](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ssm-contacts/stop-engagement.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `tag-resource`.

- **AWS CLI**
- 
            
                    **To tag a contact**The following `tag-resource`example tags a specified contact with the provided tag key value pair.`aws ssm-contacts tag-resource \ --resource-arn``"arn:aws:ssm-contacts:us-east-1:111122223333:contact/akuam"`\ --tags '`[{"Key":"group1","Value":"1"}]`'This command produces no output. For more information, see [Tagging](https://docs.aws.amazon.com/incident-manager/latest/userguide/tagging.html)in the*Incident Manager User Guide*.- 
                    For API details, see [TagResource](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ssm-contacts/tag-resource.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `untag-resource`.

- **AWS CLI**
- 
            
                    **To remove tags from a contact**The following `untag-resource`example removes the group1 tag from the specified contact.`aws ssm-contacts untag-resource \ --resource-arn``"arn:aws:ssm-contacts:us-east-1:111122223333:contact/akuam"`\ --tag-keys`"group1"`This command produces no output. For more information, see [Tagging](https://docs.aws.amazon.com/incident-manager/latest/userguide/tagging.html)in the*Incident Manager User Guide*.- 
                    For API details, see [UntagResource](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ssm-contacts/untag-resource.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `update-contact-channel`.

- **AWS CLI**
- 
            
                    **To update a contact channel**The following `update-contact-channel`example updates the name and delivery address of a contact channel.`aws ssm-contacts update-contact-channel \ --contact-channel-id``"arn:aws:ssm-contacts:us-east-2:111122223333:contact-channel/akuam/49f3c24d-5f9f-4638-ae25-3f49e04229ad"`\ --name`"akuas voice channel"`\ --delivery-address '`{"SimpleAddress": "+15005550198"}`'This command produces no output. For more information, see [Contacts](https://docs.aws.amazon.com/incident-manager/latest/userguide/contacts.html)in the*Incident Manager User Guide*.- 
                    For API details, see [UpdateContactChannel](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ssm-contacts/update-contact-channel.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `update-contact`.

- **AWS CLI**
- 
            
                    **To update the engagement plan of contact**The following `update-contact`example updates the engagement plan of the contact Akua to include the three types of contacts channels. This is done after creating contact channels for Akua.`aws ssm-contacts update-contact \ --contact-id``"arn:aws:ssm-contacts:us-east-2:111122223333:contact/akuam"`\ --plan '`{"Stages": [{"DurationInMinutes": 5, "Targets": [{"ChannelTargetInfo": {"ContactChannelId": "arn:aws:ssm-contacts:us-east-2:111122223333:contact-channel/akuam/beb25840-5ac8-4644-95cc-7a8de390fa65","RetryIntervalInMinutes": 1 }}]}, {"DurationInMinutes": 5, "Targets": [{"ChannelTargetInfo":{"ContactChannelId": "arn:aws:ssm-contacts:us-east-2:111122223333:contact-channel/akuam/49f3c24d-5f9f-4638-ae25-3f49e04229ad", "RetryIntervalInMinutes": 1}}]}, {"DurationInMinutes": 5, "Targets": [{"ChannelTargetInfo": {"ContactChannelId": "arn:aws:ssm-contacts:us-east-2:111122223333:contact-channel/akuam/77d4f447-f619-4954-afff-85551e369c2a","RetryIntervalInMinutes": 1 }}]}]}`'This command produces no output. For more information, see [Contacts](https://docs.aws.amazon.com/incident-manager/latest/userguide/contacts.html)in the*Incident Manager User Guide*.- 
                    For API details, see [UpdateContact](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ssm-contacts/update-contact.html)in*AWS CLI Command Reference*.
 
-