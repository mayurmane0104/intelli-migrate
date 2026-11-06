# Incident Manager examples using AWS CLI - AWS Command Line Interface

**Source:** [https://docs.aws.amazon.com/cli/latest/userguide/cli_ssm-incidents_code_examples.html](https://docs.aws.amazon.com/cli/latest/userguide/cli_ssm-incidents_code_examples.html)

---

The following code examples show you how to perform actions and implement common scenarios by using the AWS Command Line Interface with Incident Manager.

*Actions* are code excerpts from larger programs and must be run in context. While actions show you how to call individual service functions, you can see actions in context in their related scenarios.

Each example includes a link to the complete source code, where you can find instructions on how to set up and run the code in context.

###### Topics

## Actions

    The following code example shows how to use `create-replication-set`.

- **AWS CLI**
- 
            
                    **To create the replication set**The following `create-replication-set`example creates the replication set Incident Manager uses to replicate and encrypt data in your Amazon Web Services account. This example uses the us-east-1 and us-east-2 Regions while creating the replication set.`aws ssm-incidents create-replication-set \ --regions '``{"us-east-1": {"sseKmsKeyId": "arn:aws:kms:us-east-1:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab"}, "us-east-2": {"sseKmsKeyId": "arn:aws:kms:us-east-1:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab"}}`'Output: `{ "replicationSetArns": [ "arn:aws:ssm-incidents::111122223333:replication-set/c4bcb603-4bf9-bb3f-413c-08df53673b57" ] }`For more information, see [Using the Incident Manager replication set](https://docs.aws.amazon.com/incident-manager/latest/userguide/replication.html)in the*Incident Manager User Guide*.- 
                    For API details, see [CreateReplicationSet](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ssm-incidents/create-replication-set.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `create-response-plan`.

- **AWS CLI**
- 
            
                    **To create a response plan**The following `create-response-plan`example creates a response plan with the specified details.`aws ssm-incidents create-response-plan \ --chat-channel '``{"chatbotSns": ["arn:aws:sns:us-east-1:111122223333:Standard_User"]}`' \ --display-name`"Example response plan"`\ --incident-template '`{"impact": 5, "title": "example-incident"}`' \ --name`"example-response"`\ --actions '`[{"ssmAutomation": {"documentName": "AWSIncidents-CriticalIncidentRunbookTemplate", "documentVersion": "$DEFAULT", "roleArn": "arn:aws:iam::111122223333:role/aws-service-role/ssm-incidents.amazonaws.com/AWSServiceRoleForIncidentManager", "targetAccount": "RESPONSE_PLAN_OWNER_ACCOUNT"}}]`' \ --engagements '`["arn:aws:ssm-contacts:us-east-1:111122223333:contact/example"]`'Output: `{ "arn": "arn:aws:ssm-incidents::111122223333:response-plan/example-response" }`For more information, see [Incident preparation](https://docs.aws.amazon.com/incident-manager/latest/userguide/incident-response.html)in the*Incident Manager User Guide*.- 
                    For API details, see [CreateResponsePlan](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ssm-incidents/create-response-plan.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `create-timeline-event`.

- **AWS CLI**
- 
            
                    **Example 1: To create a custom timeline event**The following `create-timeline-event`example creates a custom timeline event at the specified time on the specified incident.`aws ssm-incidents create-timeline-event \ --event-data "\"example timeline event\"" \ --event-time``2022-10-01T20:30:00.000`\ --event-type`"Custom Event"`\ --incident-record-arn`"arn:aws:ssm-incidents::111122223333:incident-record/Example-Response-Plan/6ebcc812-85f5-b7eb-8b2f-283e4EXAMPLE"`Output: `{ "eventId": "c0bcc885-a41d-eb01-b4ab-9d2deEXAMPLE", "incidentRecordArn": "arn:aws:ssm-incidents::111122223333:incident-record/Example-Response-Plan/6ebcc812-85f5-b7eb-8b2f-283e4EXAMPLE" }`**Example 2: To create a timeline event with an incident note**The following `create-timeline-event`example creates a timeline event that is listed in the 'Incident notes' panel.`aws ssm-incidents create-timeline-event \ --event-data "\"New``Note`\"" \ --event-type "Note" \ --incident-record-arn`"arn:aws:ssm-incidents::111122223333:incident-record/Test/6cc46130-ca6c-3b38-68f1-f6abeEXAMPLE"`\ --event-time`2023-06-20T12:06:00.000`\ --event-references '`[{"resource":"arn:aws:ssm-incidents::111122223333:incident-record/Test/6cc46130-ca6c-3b38-68f1-f6abeEXAMPLE"}]`'Output: `{ "eventId": "a41dc885-c0bc-b4ab-eb01-de9d2EXAMPLE", "incidentRecordArn": "arn:aws:ssm-incidents::111122223333:incident-record/Example-Response-Plan/6ebcc812-85f5-b7eb-8b2f-283e4EXAMPLE" }`For more information, see [Incident details](https://docs.aws.amazon.com/incident-manager/latest/userguide/tracking-details.html)in the*Incident Manager User Guide*.- 
                    For API details, see [CreateTimelineEvent](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ssm-incidents/create-timeline-event.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `delete-incident-record`.

- **AWS CLI**
- 
            
                    **To delete an incident record**The following `delete-incident-record`example deletes the specified incident record.`aws ssm-incidents delete-incident-record \ --arn``"arn:aws:ssm-incidents::111122223333:incident-record/Example-Response-Plan/6ebcc812-85f5-b7eb-8b2f-283e4d844308"`This command produces no output. For more information, see [Incident tracking](https://docs.aws.amazon.com/incident-manager/latest/userguide/tracking.html)in the*Incident Manager User Guide*.- 
                    For API details, see [DeleteIncidentRecord](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ssm-incidents/delete-incident-record.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `delete-replication-set`.

- **AWS CLI**
- 
            
                    **To delete the replication set**The following `delete-replication-set`example deletes the replication set from your Amazon Web Services account. Deleting the replication set also deletes all Incident Manager data. This can't be undone.`aws ssm-incidents delete-replication-set \ --arn``"arn:aws:ssm-incidents::111122223333:replication-set/c4bcb603-4bf9-bb3f-413c-08df53673b57"`This command produces no output. For more information, see [Using the Incident Manager replication set](https://docs.aws.amazon.com/incident-manager/latest/userguide/replication.html)in the*Incident Manager User Guide*.- 
                    For API details, see [DeleteReplicationSet](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ssm-incidents/delete-replication-set.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `delete-resource-policy`.

- **AWS CLI**
- 
            
                    **To delete a resource policy**The following `delete-resource-policy`example deletes a resource policy from a response plan. This will revoke access from the principal or organization that the response plan was shared with.`aws ssm-incidents delete-resource-policy \ --policy-id``"be8b57191f0371f1c6827341aa3f0a03"`\ --resource-arn`"arn:aws:ssm-incidents::111122223333:response-plan/Example-Response-Plan"`This command produces no output. For more information, see [Working with shared contacts and response plans](https://docs.aws.amazon.com/incident-manager/latest/userguide/sharing.html)in the*Incident Manager User Guide*.- 
                    For API details, see [DeleteResourcePolicy](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ssm-incidents/delete-resource-policy.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `delete-response-plan`.

- **AWS CLI**
- 
            
                    **To delete a response plan**The following `delete-response-plan`example deletes the specified response plan.`aws ssm-incidents delete-response-plan \ --arn``"arn:aws:ssm-incidents::111122223333:response-plan/example-response"`This command produces no output. For more information, see [Incident preparation](https://docs.aws.amazon.com/incident-manager/latest/userguide/incident-response.html)in the*Incident Manager User Guide*.- 
                    For API details, see [DeleteResponsePlan](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ssm-incidents/delete-response-plan.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `delete-timeline-event`.

- **AWS CLI**
- 
            
                    **To delete a timeline event**The following `delete-timeline-event`example deletes a custom timeline event from the specified incident record.`aws ssm-incidents delete-timeline-event \ --event-id``"c0bcc885-a41d-eb01-b4ab-9d2de193643c"`\ --incident-record-arn`"arn:aws:ssm-incidents::111122223333:incident-record/Example-Response-Plan/6ebcc812-85f5-b7eb-8b2f-283e4d844308"`This command produces no output. For more information, see [Incident details](https://docs.aws.amazon.com/incident-manager/latest/userguide/tracking-details.html)in the*Incident Manager User Guide*.- 
                    For API details, see [DeleteTimelineEvent](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ssm-incidents/delete-timeline-event.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `get-incident-record`.

- **AWS CLI**
- 
            
                    **To get an incident record**The following `get-incident-record`example gets details about the specified incident record.`aws ssm-incidents get-incident-record \ --arn``"arn:aws:ssm-incidents::111122223333:incident-record/Example-Response-Plan/6ebcc812-85f5-b7eb-8b2f-283e4d844308"`Output: `{ "incidentRecord": { "arn": "arn:aws:ssm-incidents::111122223333:incident-record/Example-Response-Plan/6ebcc812-85f5-b7eb-8b2f-283e4d844308", "automationExecutions": [], "creationTime": "2021-05-21T18:16:57.579000+00:00", "dedupeString": "c4bcc812-85e7-938d-2b78-17181176ee1a", "impact": 5, "incidentRecordSource": { "createdBy": "arn:aws:iam::111122223333:user/draliatp", "invokedBy": "arn:aws:iam::111122223333:user/draliatp", "source": "aws.ssm-incidents.custom" }, "lastModifiedBy": "arn:aws:iam::111122223333:user/draliatp", "lastModifiedTime": "2021-05-21T18:16:59.149000+00:00", "notificationTargets": [], "status": "OPEN", "title": "Example-Incident" } }`For more information, see [Incident details](https://docs.aws.amazon.com/incident-manager/latest/userguide/tracking-details.html)in the*Incident Manager User Guide*.- 
                    For API details, see [GetIncidentRecord](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ssm-incidents/get-incident-record.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `get-replication-set`.

- **AWS CLI**
- 
            
                    **To get the replication set**The following `get-replication-set`example gets the details of the replication set Incident Manager uses to replicate and encrypt data in your Amazon Web Services account.`aws ssm-incidents get-replication-set \ --arn``"arn:aws:ssm-incidents::111122223333:replication-set/c4bcb603-4bf9-bb3f-413c-08df53673b57"`Output: `{ "replicationSet": { "createdBy": "arn:aws:sts::111122223333:assumed-role/Admin/username", "createdTime": "2021-05-14T17:57:22.010000+00:00", "deletionProtected": false, "lastModifiedBy": "arn:aws:sts::111122223333:assumed-role/Admin/username", "lastModifiedTime": "2021-05-14T17:57:22.010000+00:00", "regionMap": { "us-east-1": { "sseKmsKeyId": "DefaultKey", "status": "ACTIVE" }, "us-east-2": { "sseKmsKeyId": "DefaultKey", "status": "ACTIVE", "statusMessage": "Tagging inaccessible" } }, "status": "ACTIVE" } }`For more information, see [Using the Incident Manager replication set](https://docs.aws.amazon.com/incident-manager/latest/userguide/replication.html)in the*Incident Manager User Guide*.- 
                    For API details, see [GetReplicationSet](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ssm-incidents/get-replication-set.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `get-resource-policies`.

- **AWS CLI**
- 
            
                    **To list resource policies for a response plan**The following `command-name`example lists the resource policies associated with the specified response plan.`aws ssm-incidents get-resource-policies \ --resource-arn``"arn:aws:ssm-incidents::111122223333:response-plan/Example-Response-Plan"`Output: `{ "resourcePolicies": [ { "policyDocument": "{\"Version\":\"2012-10-17\",\"Statement\":[{\"Sid\":\"d901b37a-dbb0-458a-8842-75575c464219-external-principals\",\"Effect\":\"Allow\",\"Principal\":{\"AWS\":\"arn:aws:iam::222233334444:root\"},\"Action\":[\"ssm-incidents:GetResponsePlan\",\"ssm-incidents:StartIncident\",\"ssm-incidents:UpdateIncidentRecord\",\"ssm-incidents:GetIncidentRecord\",\"ssm-incidents:CreateTimelineEvent\",\"ssm-incidents:UpdateTimelineEvent\",\"ssm-incidents:GetTimelineEvent\",\"ssm-incidents:ListTimelineEvents\",\"ssm-incidents:UpdateRelatedItems\",\"ssm-incidents:ListRelatedItems\"],\"Resource\":[\"arn:aws:ssm-incidents:*:111122223333:response-plan/Example-Response-Plan\",\"arn:aws:ssm-incidents:*:111122223333:incident-record/Example-Response-Plan/*\"]}]}", "policyId": "be8b57191f0371f1c6827341aa3f0a03", "ramResourceShareRegion": "us-east-1" } ] }`For more information, see [Working with shared contacts and response plans](https://docs.aws.amazon.com/incident-manager/latest/userguide/sharing.html)in the*Incident Manager User Guide*.- 
                    For API details, see [GetResourcePolicies](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ssm-incidents/get-resource-policies.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `get-response-plan`.

- **AWS CLI**
- 
            
                    **To get details of a response plan**The following `command-name`example gets details about a specified response plan in your AWS account.`aws ssm-incidents get-response-plan \ --arn``"arn:aws:ssm-incidents::111122223333:response-plan/Example-Response-Plan"`Output: `{ "actions": [ { "ssmAutomation": { "documentName": "AWSIncidents-CriticalIncidentRunbookTemplate", "documentVersion": "$DEFAULT", "roleArn": "arn:aws:iam::111122223333:role/aws-service-role/ssm-incidents.amazonaws.com/AWSServiceRoleForIncidentManager", "targetAccount": "RESPONSE_PLAN_OWNER_ACCOUNT" } } ], "arn": "arn:aws:ssm-incidents::111122223333:response-plan/Example-Response-Plan", "chatChannel": { "chatbotSns": [ "arn:aws:sns:us-east-1:111122223333:Standard_User" ] }, "displayName": "Example response plan", "engagements": [ "arn:aws:ssm-contacts:us-east-1:111122223333:contact/example" ], "incidentTemplate": { "impact": 5, "title": "Example-Incident" }, "name": "Example-Response-Plan" }`For more information, see [Incident preparation](https://docs.aws.amazon.com/incident-manager/latest/userguide/incident-response.html)in the*Incident Manager User Guide*.- 
                    For API details, see [GetResponsePlan](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ssm-incidents/get-response-plan.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `get-timeline-event`.

- **AWS CLI**
- 
            
                    **To get details of a timeline event**The following `get-timeline-event`example returns details of the specified timeline event.`aws ssm-incidents get-timeline-event \ --event-id``20bcc812-8a94-4cd7-520c-0ff742111424`\ --incident-record-arn`"arn:aws:ssm-incidents::111122223333:incident-record/Example-Response-Plan/6ebcc812-85f5-b7eb-8b2f-283e4d844308"`Output: `{ "event": { "eventData": "\"Incident Started\"", "eventId": "20bcc812-8a94-4cd7-520c-0ff742111424", "eventTime": "2021-05-21T18:16:57+00:00", "eventType": "Custom Event", "eventUpdatedTime": "2021-05-21T18:16:59.944000+00:00", "incidentRecordArn": "arn:aws:ssm-incidents::111122223333:incident-record/Example-Response-Plan/6ebcc812-85f5-b7eb-8b2f-283e4d844308" } }`For more information, see [Incident details](https://docs.aws.amazon.com/incident-manager/latest/userguide/tracking-details.html)in the*Incident Manager User Guide*.- 
                    For API details, see [GetTimelineEvent](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ssm-incidents/get-timeline-event.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `list-incident-records`.

- **AWS CLI**
- 
            
                    **To list incident records**The following `command-name`example lists the incident records in your Amazon Web Services account.`aws ssm-incidents list-incident-records`Output: `{ "incidentRecordSummaries": [ { "arn": "arn:aws:ssm-incidents::111122223333:incident-record/Example-Response-Plan/6ebcc812-85f5-b7eb-8b2f-283e4d844308", "creationTime": "2021-05-21T18:16:57.579000+00:00", "impact": 5, "incidentRecordSource": { "createdBy": "arn:aws:iam::111122223333:user/draliatp", "invokedBy": "arn:aws:iam::111122223333:user/draliatp", "source": "aws.ssm-incidents.custom" }, "status": "OPEN", "title": "Example-Incident" } ] }`For more information, see [Incident list](https://docs.aws.amazon.com/incident-manager/latest/userguide/tracking-list.html)in the*Incident Manager User Guide*.- 
                    For API details, see [ListIncidentRecords](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ssm-incidents/list-incident-records.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `list-related-items`.

- **AWS CLI**
- 
            
                    **To list related items**The following `list-related-items`example lists the related items of the specified incident.`aws ssm-incidents list-related-items \ --incident-record-arn``"arn:aws:ssm-incidents::111122223333:incident-record/Example-Response-Plan/6ebcc812-85f5-b7eb-8b2f-283e4d844308"`Output: `{ "relatedItems": [ { "identifier": { "type": "OTHER", "value": { "url": "https://console.aws.amazon.com/systems-manager/opsitems/oi-8ef82158e190/workbench?region=us-east-1" } }, "title": "Example related item" }, { "identifier": { "type": "PARENT", "value": { "arn": "arn:aws:ssm:us-east-1:111122223333:opsitem/oi-8084126392ac" } }, "title": "parentItem" } ] }`For more information, see [Incident details](https://docs.aws.amazon.com/incident-manager/latest/userguide/tracking-details.html)in the*Incident Manager User Guide*.- 
                    For API details, see [ListRelatedItems](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ssm-incidents/list-related-items.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `list-replication-sets`.

- **AWS CLI**
- 
            
                    **To list the replication set**The following `list-replication-set`example lists the replication set Incident Manager uses to replicate and encrypt data in your AWS account.`aws ssm-incidents list-replication-sets`Output: `{ "replicationSetArns": [ "arn:aws:ssm-incidents::111122223333:replication-set/c4bcb603-4bf9-bb3f-413c-08df53673b57" ] }`For more information, see [Using the Incident Manager replication set](https://docs.aws.amazon.com/incident-manager/latest/userguide/replication.html)in the*Incident Manager User Guide*.- 
                    For API details, see [ListReplicationSets](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ssm-incidents/list-replication-sets.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `list-response-plans`.

- **AWS CLI**
- 
            
                    **To list the available response plans**The following `list-response-plans`example lists the available response plans in your Amazon Web Services account.`aws ssm-incidents list-response-plans`Output: `{ "responsePlanSummaries": [ { "arn": "arn:aws:ssm-incidents::111122223333:response-plan/Example-Response-Plan", "displayName": "Example response plan", "name": "Example-Response-Plan" } ] }`For more information, see [Incident preparation](https://docs.aws.amazon.com/incident-manager/latest/userguide/incident-response.html)in the*Incident Manager User Guide*.- 
                    For API details, see [ListResponsePlans](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ssm-incidents/list-response-plans.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `list-tags-for-resource`.

- **AWS CLI**
- 
            
                    **To list tags for a response plan**The following `list-tags-for-resource`example lists the tags associated with the specified response plan.`aws ssm-incidents list-tags-for-resource \ --resource-arn``"arn:aws:ssm-incidents::111122223333:response-plan/Example-Response-Plan"`Output: `{ "tags": { "group1": "1" } }`For more information, see [Tagging](https://docs.aws.amazon.com/incident-manager/latest/userguide/tagging.html)in the*Incident Manager User Guide*.- 
                    For API details, see [ListTagsForResource](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ssm-incidents/list-tags-for-resource.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `list-timeline-events`.

- **AWS CLI**
- 
            
                    **To list timeline events of an incident**The following `command-name`example lists the timeline events of the specified incident.`aws ssm-incidents list-timeline-events \ --incident-record-arn``"arn:aws:ssm-incidents::111122223333:incident-record/Example-Response-Plan/6ebcc812-85f5-b7eb-8b2f-283e4d844308"`Output: `{ "eventSummaries": [ { "eventId": "8cbcc889-35e1-a42d-2429-d6f100799915", "eventTime": "2021-05-21T22:36:13.766000+00:00", "eventType": "SSM Incident Record Update", "eventUpdatedTime": "2021-05-21T22:36:13.766000+00:00", "incidentRecordArn": "arn:aws:ssm-incidents::111122223333:incident-record/Example-Response-Plan/6ebcc812-85f5-b7eb-8b2f-283e4d844308" }, { "eventId": "a2bcc825-aab5-1787-c605-f9bb2640d85b", "eventTime": "2021-05-21T18:58:46.443000+00:00", "eventType": "SSM Incident Record Update", "eventUpdatedTime": "2021-05-21T18:58:46.443000+00:00", "incidentRecordArn": "arn:aws:ssm-incidents::111122223333:incident-record/Example-Response-Plan/6ebcc812-85f5-b7eb-8b2f-283e4d844308" }, { "eventId": "5abcc812-89c0-b0a8-9437-1c74223d4685", "eventTime": "2021-05-21T18:16:59.149000+00:00", "eventType": "SSM Incident Record Update", "eventUpdatedTime": "2021-05-21T18:16:59.149000+00:00", "incidentRecordArn": "arn:aws:ssm-incidents::111122223333:incident-record/Example-Response-Plan/6ebcc812-85f5-b7eb-8b2f-283e4d844308" }, { "eventId": "06bcc812-8820-405e-4065-8d2b14d29b92", "eventTime": "2021-05-21T18:16:58+00:00", "eventType": "SSM Automation Execution Start Failure for Incident", "eventUpdatedTime": "2021-05-21T18:16:58.689000+00:00", "incidentRecordArn": "arn:aws:ssm-incidents::111122223333:incident-record/Example-Response-Plan/6ebcc812-85f5-b7eb-8b2f-283e4d844308" }, { "eventId": "20bcc812-8a94-4cd7-520c-0ff742111424", "eventTime": "2021-05-21T18:16:57+00:00", "eventType": "Custom Event", "eventUpdatedTime": "2021-05-21T18:16:59.944000+00:00", "incidentRecordArn": "arn:aws:ssm-incidents::111122223333:incident-record/Example-Response-Plan/6ebcc812-85f5-b7eb-8b2f-283e4d844308" }, { "eventId": "c0bcc885-a41d-eb01-b4ab-9d2de193643c", "eventTime": "2020-10-01T20:30:00+00:00", "eventType": "Custom Event", "eventUpdatedTime": "2021-05-21T22:28:26.299000+00:00", "incidentRecordArn": "arn:aws:ssm-incidents::111122223333:incident-record/Example-Response-Plan/6ebcc812-85f5-b7eb-8b2f-283e4d844308" } ] }`For more information, see [Incident details](https://docs.aws.amazon.com/incident-manager/latest/userguide/tracking-details.html)in the*Incident Manager User Guide*.- 
                    For API details, see [ListTimelineEvents](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ssm-incidents/list-timeline-events.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `put-resource-policy`.

- **AWS CLI**
- 
            
                    **To share a response plan and incidents**The following `command-name`example adds a resource policy to the Example-Response-Plan that shares the response plan and associated incidents with the specified principal.`aws ssm-incidents put-resource-policy \ --resource-arn``"arn:aws:ssm-incidents::111122223333:response-plan/Example-Response-Plan"`\ --policy "{\"Version\":\"2012-10-17\",\"Statement\":[{\"Sid\":\"ExampleResourcePolciy\",\"Effect\":\"Allow\",\"Principal\":{\"AWS\":\"arn:aws:iam::222233334444:root\"},\"Action\":[\"ssm-incidents:GetResponsePlan\",\"ssm-incidents:StartIncident\",\"ssm-incidents:UpdateIncidentRecord\",\"ssm-incidents:GetIncidentRecord\",\"ssm-incidents:CreateTimelineEvent\",\"ssm-incidents:UpdateTimelineEvent\",\"ssm-incidents:GetTimelineEvent\",\"ssm-incidents:ListTimelineEvents\",\"ssm-incidents:UpdateRelatedItems\",\"ssm-incidents:ListRelatedItems\"],\"Resource\":[\"arn:aws:ssm-incidents:*:111122223333:response-plan/Example-Response-Plan\",\"arn:aws:ssm-incidents:*:111122223333:incident-record/Example-Response-Plan/*\"]}]}"Output: `{ "policyId": "be8b57191f0371f1c6827341aa3f0a03" }`For more information, see [Working with shared contacts and response plans](https://docs.aws.amazon.com/incident-manager/latest/userguide/sharing.html)in the*Incident Manager User Guide*.- 
                    For API details, see [PutResourcePolicy](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ssm-incidents/put-resource-policy.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `start-incident`.

- **AWS CLI**
- 
            
                    **To start an incident**The following `start-incident`example starts an incident using the specified response plan.`aws ssm-incidents start-incident \ --response-plan-arn``"arn:aws:ssm-incidents::111122223333:response-plan/Example-Response-Plan"`Output: `{ "incidentRecordArn": "arn:aws:ssm-incidents::682428703967:incident-record/Example-Response-Plan/6ebcc812-85f5-b7eb-8b2f-283e4d844308" }`For more information, see [Incident creation](https://docs.aws.amazon.com/incident-manager/latest/userguide/incident-creation.html)in the*Incident Manager User Guide*.- 
                    For API details, see [StartIncident](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ssm-incidents/start-incident.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `tag-resource`.

- **AWS CLI**
- 
            
                    **To tag a response plan**The following `tag-resource`example tags a specified response plan with the provided tag key-value pair.`aws ssm-incidents tag-resource \ --resource-arn``"arn:aws:ssm-incidents::111122223333:response-plan/Example-Response-Plan"`\ --tags '`{"group1":"1"}`'This command produces no output. For more information, see [Tagging](https://docs.aws.amazon.com/incident-manager/latest/userguide/tagging.html)in the*Incident Manager User Guide*.- 
                    For API details, see [TagResource](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ssm-incidents/tag-resource.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `untag-resource`.

- **AWS CLI**
- 
            
                    **To remove tags from a response plan**The following `untag-resource`example removes the specified tags from the response plan.`aws ssm-incidents untag-resource \ --resource-arn``"arn:aws:ssm-incidents::111122223333:response-plan/Example-Response-Plan"`\ --tag-keys '`["group1"]`'This command produces no output. For more information, see [Tagging](https://docs.aws.amazon.com/incident-manager/latest/userguide/tagging.html)in the*Incident Manager User Guide*.- 
                    For API details, see [UntagResource](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ssm-incidents/untag-resource.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `update-deletion-protection`.

- **AWS CLI**
- 
            
                    **To update replication set deletion protection**The following `update-deletion-protection`example updates the deletion protection in your account to protect you from deleting the last Region in your replication set.`aws ssm-incidents update-deletion-protection \ --arn``"arn:aws:ssm-incidents::111122223333:replication-set/a2bcc5c9-0f53-8047-7fef-c20749989b40"`\ --deletion-protectedThis command produces no output. For more information, see [Using the Incident Manager replication set](https://docs.aws.amazon.com/incident-manager/latest/userguide/replication.html)in the*Incident Manager User Guide*.- 
                    For API details, see [UpdateDeletionProtection](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ssm-incidents/update-deletion-protection.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `update-incident-record`.

- **AWS CLI**
- 
            
                    **To update an incident record**The following `command-name`example resolves the specified incident.`aws ssm-incidents update-incident-record \ --arn``"arn:aws:ssm-incidents::111122223333:incident-record/Example-Response-Plan/6ebcc812-85f5-b7eb-8b2f-283e4d844308"`\ --status`"RESOLVED"`This command produces no output. For more information, see [Incident details](https://docs.aws.amazon.com/incident-manager/latest/userguide/tracking-details.html)in the*Incident Manager User Guide*.- 
                    For API details, see [UpdateIncidentRecord](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ssm-incidents/update-incident-record.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `update-related-items`.

- **AWS CLI**
- 
            
                    **To update an incidents related item**The following `update-related-item`example removes a related item from the specified incident record.`aws ssm-incidents update-related-items \ --incident-record-arn``"arn:aws:ssm-incidents::111122223333:incident-record/Example-Response-Plan/6ebcc812-85f5-b7eb-8b2f-283e4d844308"`\ --related-items-update '`{"itemToRemove": {"type": "OTHER", "value": {"url": "https://console.aws.amazon.com/systems-manager/opsitems/oi-8ef82158e190/workbench?region=us-east-1"}}}`'This command produces no output. For more information, see [Incident details](https://docs.aws.amazon.com/incident-manager/latest/userguide/tracking-details.html)in the*Incident Manager User Guide*.- 
                    For API details, see [UpdateRelatedItems](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ssm-incidents/update-related-items.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `update-replication-set`.

- **AWS CLI**
- 
            
                    **To update a replication set**The following `command-name`example deletes the us-east-2 Region from the replication set.`aws ssm-incidents update-replication-set \ --arn``"arn:aws:ssm-incidents::111122223333:replication-set/a2bcc5c9-0f53-8047-7fef-c20749989b40"`\ --actions '`[{"deleteRegionAction": {"regionName": "us-east-2"}}]`'This command produces no output. For more information, see [Using the Incident Manager replication set](https://docs.aws.amazon.com/incident-manager/latest/userguide/replication.html)in the*Incident Manager User Guide*.- 
                    For API details, see [UpdateReplicationSet](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ssm-incidents/update-replication-set.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `update-response-plan`.

- **AWS CLI**
- 
            
                    **To update a response plan**The following `update-response-plan`example removes a chat channel from the specified response plan.`aws ssm-incidents update-response-plan \ --arn``"arn:aws:ssm-incidents::111122223333:response-plan/Example-Response-Plan"`\ --chat-channel '`{"empty":{}}`'This command produces no output. For more information, see [Incident preparation](https://docs.aws.amazon.com/incident-manager/latest/userguide/incident-response.html)in the*Incident Manager User Guide*.- 
                    For API details, see [UpdateResponsePlan](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ssm-incidents/update-response-plan.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `update-timeline-event`.

- **AWS CLI**
- 
            
                    **To update a timeline event**The following `update-timeline-event`example updates the time that the event occurred.`aws ssm-incidents update-timeline-event \ --event-id``20bcc812-8a94-4cd7-520c-0ff742111424`\ --incident-record-arn`"arn:aws:ssm-incidents::111122223333:incident-record/Example-Response-Plan/6ebcc812-85f5-b7eb-8b2f-283e4d844308"`\ --event-time`"2021-05-21T18:10:57+00:00"`This command produces no output. For more information, see [Incident details](https://docs.aws.amazon.com/incident-manager/latest/userguide/tracking-details.html)in the*Incident Manager User Guide*.- 
                    For API details, see [UpdateTimelineEvent](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ssm-incidents/update-timeline-event.html)in*AWS CLI Command Reference*.
 
-