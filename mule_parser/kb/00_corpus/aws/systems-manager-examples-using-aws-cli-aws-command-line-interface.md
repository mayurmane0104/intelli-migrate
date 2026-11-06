# Systems Manager examples using AWS CLI - AWS Command Line Interface

**Source:** [https://docs.aws.amazon.com/cli/latest/userguide/cli_ssm_code_examples.html](https://docs.aws.amazon.com/cli/latest/userguide/cli_ssm_code_examples.html)

---

The following code examples show you how to perform actions and implement common scenarios by using the AWS Command Line Interface with Systems Manager.

*Actions* are code excerpts from larger programs and must be run in context. While actions show you how to call individual service functions, you can see actions in context in their related scenarios.

Each example includes a link to the complete source code, where you can find instructions on how to set up and run the code in context.

###### Topics

## Actions

    The following code example shows how to use `add-tags-to-resource`.

- **AWS CLI**
- 
            
                    **Example 1: To add tags to a maintenance window**The following `add-tags-to-resource`example adds a tag to the specified maintenance window.`aws ssm add-tags-to-resource \ --resource-type``"MaintenanceWindow"`\ --resource-id`"mw-03eb9db428EXAMPLE"`\ --tags`"Key=Stack,Value=Production"`This command produces no output. **Example 2: To add tags to a parameter**The following `add-tags-to-resource`example adds two tags to to the specified parameter.`aws ssm add-tags-to-resource \ --resource-type``"Parameter"`\ --resource-id`"My-Parameter"`\ --tags '`[{"Key":"Region","Value":"East"},{"Key":"Environment", "Value":"Production"}]`'This command produces no output. **Example 3: To add tags to an SSM document**The following `add-tags-to-resource`example adds a tag to to the specified document.`aws ssm add-tags-to-resource \ --resource-type``"Document"`\ --resource-id`"My-Document"`\ --tags`"Key=Quarter,Value=Q322"`This command produces no output. For more information, see [Tagging Systems Manager resources](https://docs.aws.amazon.com/systems-manager/latest/userguide/tagging-resources.html)in the*AWS Systems Manager User Guide*.- 
                    For API details, see [AddTagsToResource](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ssm/add-tags-to-resource.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `associate-ops-item-related-item`.

- **AWS CLI**
- 
            
                    **To associate a related item**The following `associate-ops-item-related-item`example associates a related item to the OpsItem.`aws ssm associate-ops-item-related-item \ --ops-item-id``"oi-649fExample"`\ --association-type`"RelatesTo"`\ --resource-type`"AWS::SSMIncidents::IncidentRecord"`\ --resource-uri`"arn:aws:ssm-incidents::111122223333:incident-record/Example-Response-Plan/c2bde883-f7d5-343a-b13a-bf5fe9ea689f"`Output: `{ "AssociationId": "61d7178d-a30d-4bc5-9b4e-a9e74EXAMPLE" }`For more information, see [Working with Incident Manager incidents in OpsCenter](https://docs.aws.amazon.com/systems-manager/latest/userguide/OpsCenter-create-OpsItems-for-Incident-Manager.html)in the*AWS Systems Manager User Guide*.- 
                    For API details, see [AssociateOpsItemRelatedItem](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ssm/associate-ops-item-related-item.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `cancel-command`.

- **AWS CLI**
- 
            
                    **Example 1: To cancel a command for all instances**The following `cancel-command`example attempts to cancel the specified command that is already running for all instances.`aws ssm cancel-command \ --command-id``"662add3d-5831-4a10-b64a-f2ff3EXAMPLE"`This command produces no output. **Example 2: To cancel a command for specific instances**The following `cancel-command`example attempts to cancel a command for the specified instance only.`aws ssm cancel-command \ --command-id``"662add3d-5831-4a10-b64a-f2ff3EXAMPLE"`--instance-ids`"i-02573cafcfEXAMPLE"`This command produces no output. For more information, see [Tagging Systems Manager Parameters](https://docs.aws.amazon.com/systems-manager/latest/userguide/sysman-paramstore-su-tag.html)in the*AWS Systems Manager User Guide*.- 
                    For API details, see [CancelCommand](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ssm/cancel-command.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `cancel-maintenance-window-execution`.

- **AWS CLI**
- 
            
                    **To cancel a maintenance window execution**This `cancel-maintenance-window-execution`example stops the specified maintenance window execution that is already in progress.`aws ssm cancel-maintenance-window-execution \ --window-execution-id``j2l8d5b5c-mw66-tk4d-r3g9-1d4d1EXAMPLE`Output: `{ "WindowExecutionId": "j2l8d5b5c-mw66-tk4d-r3g9-1d4d1EXAMPLE" }`For more information, see [Systems Manager Maintenance Windows Tutorials (AWS CLI)](https://docs.aws.amazon.com/systems-manager/latest/userguide/maintenance-windows-tutorials.html)in the*AWS Systems Manager User Guide*.- 
                    For API details, see [CancelMaintenanceWindowExecution](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ssm/cancel-maintenance-window-execution.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `create-activation`.

- **AWS CLI**
- 
            
                    **To create a managed instance activation**The following `create-activation`example creates a managed instance activation.`aws ssm create-activation \ --default-instance-name``"HybridWebServers"`\ --iam-role`"HybridWebServersRole"`\ --registration-limit`5`Output: `{ "ActivationId": "5743558d-563b-4457-8682-d16c3EXAMPLE", "ActivationCode": "dRmgnYaFv567vEXAMPLE" }`For more information, see [Step 4: Create a Managed-Instance Activation for a Hybrid Environment](https://docs.aws.amazon.com/systems-manager/latest/userguide/sysman-managed-instance-activation.html)in the*AWS Systems Manager User Guide*.- 
                    For API details, see [CreateActivation](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ssm/create-activation.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `create-association-batch`.

- **AWS CLI**
- 
            
                    **To create multiple associations**This example associates a configuration document with multiple instances. The output returns a list of successful and failed operations, if applicable. Command: `aws ssm create-association-batch --entries``"Name=AWS-UpdateSSMAgent,InstanceId=i-1234567890abcdef0"``"Name=AWS-UpdateSSMAgent,InstanceId=i-9876543210abcdef0"`Output: `{ "Successful": [ { "Name": "AWS-UpdateSSMAgent", "InstanceId": "i-1234567890abcdef0", "AssociationVersion": "1", "Date": 1550504725.007, "LastUpdateAssociationDate": 1550504725.007, "Status": { "Date": 1550504725.007, "Name": "Associated", "Message": "Associated with AWS-UpdateSSMAgent" }, "Overview": { "Status": "Pending", "DetailedStatus": "Creating" }, "DocumentVersion": "$DEFAULT", "AssociationId": "8dfe3659-4309-493a-8755-0123456789ab", "Targets": [ { "Key": "InstanceIds", "Values": [ "i-1234567890abcdef0" ] } ] }, { "Name": "AWS-UpdateSSMAgent", "InstanceId": "i-9876543210abcdef0", "AssociationVersion": "1", "Date": 1550504725.057, "LastUpdateAssociationDate": 1550504725.057, "Status": { "Date": 1550504725.057, "Name": "Associated", "Message": "Associated with AWS-UpdateSSMAgent" }, "Overview": { "Status": "Pending", "DetailedStatus": "Creating" }, "DocumentVersion": "$DEFAULT", "AssociationId": "9c9f7f20-5154-4fed-a83e-0123456789ab", "Targets": [ { "Key": "InstanceIds", "Values": [ "i-9876543210abcdef0" ] } ] } ], "Failed": [] }`- 
                    For API details, see [CreateAssociationBatch](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ssm/create-association-batch.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `create-association`.

- **AWS CLI**
- 
            
                    **Example 1: To associate a document using instance IDs**This example associates a configuration document with an instance, using instance IDs. `aws ssm create-association \ --instance-id``"i-0cb2b964d3e14fd9f"`\ --name`"AWS-UpdateSSMAgent"`Output: `{ "AssociationDescription": { "Status": { "Date": 1487875500.33, "Message": "Associated with AWS-UpdateSSMAgent", "Name": "Associated" }, "Name": "AWS-UpdateSSMAgent", "InstanceId": "i-0cb2b964d3e14fd9f", "Overview": { "Status": "Pending", "DetailedStatus": "Creating" }, "AssociationId": "b7c3266e-a544-44db-877e-b20d3a108189", "DocumentVersion": "$DEFAULT", "LastUpdateAssociationDate": 1487875500.33, "Date": 1487875500.33, "Targets": [ { "Values": [ "i-0cb2b964d3e14fd9f" ], "Key": "InstanceIds" } ] } }`For more information, see [CreateAssociation](https://docs.aws.amazon.com/systems-manager/latest/APIReference/API_CreateAssociation.html)in the*AWS Systems Manager API Reference*.**Example 2: To associate a document using targets**This example associates a configuration document with an instance, using targets. `aws ssm create-association \ --name``"AWS-UpdateSSMAgent"`\ --targets`"Key=instanceids,Values=i-0cb2b964d3e14fd9f"`Output: `{ "AssociationDescription": { "Status": { "Date": 1487875500.33, "Message": "Associated with AWS-UpdateSSMAgent", "Name": "Associated" }, "Name": "AWS-UpdateSSMAgent", "InstanceId": "i-0cb2b964d3e14fd9f", "Overview": { "Status": "Pending", "DetailedStatus": "Creating" }, "AssociationId": "b7c3266e-a544-44db-877e-b20d3a108189", "DocumentVersion": "$DEFAULT", "LastUpdateAssociationDate": 1487875500.33, "Date": 1487875500.33, "Targets": [ { "Values": [ "i-0cb2b964d3e14fd9f" ], "Key": "InstanceIds" } ] } }`For more information, see [CreateAssociation](https://docs.aws.amazon.com/systems-manager/latest/APIReference/API_CreateAssociation.html)in the*AWS Systems Manager API Reference*.**Example 3: To create an association that runs only once**This example creates a new association that only runs once on the specified date and time. Associations created with a date in the past or present (by the time it is processed the date is in the past) run immediately. `aws ssm create-association \ --name``"AWS-UpdateSSMAgent"`\ --targets`"Key=instanceids,Values=i-0cb2b964d3e14fd9f"`\ --schedule-expression`"at(2020-05-14T15:55:00)"`\ --apply-only-at-cron-intervalOutput: `{ "AssociationDescription": { "Status": { "Date": 1487875500.33, "Message": "Associated with AWS-UpdateSSMAgent", "Name": "Associated" }, "Name": "AWS-UpdateSSMAgent", "InstanceId": "i-0cb2b964d3e14fd9f", "Overview": { "Status": "Pending", "DetailedStatus": "Creating" }, "AssociationId": "b7c3266e-a544-44db-877e-b20d3a108189", "DocumentVersion": "$DEFAULT", "LastUpdateAssociationDate": 1487875500.33, "Date": 1487875500.33, "Targets": [ { "Values": [ "i-0cb2b964d3e14fd9f" ], "Key": "InstanceIds" } ] } }`For more information, see [CreateAssociation](https://docs.aws.amazon.com/systems-manager/latest/APIReference/API_CreateAssociation.html)in the*AWS Systems Manager API Reference*or[Reference: Cron and rate expressions for Systems Manager](https://docs.aws.amazon.com/systems-manager/latest/userguide/reference-cron-and-rate-expressions.html)in the*AWS Systems Manager User Guide*.- 
                    For API details, see [CreateAssociation](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ssm/create-association.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `create-document`.

- **AWS CLI**
- 
            
                    **To create a document**The following `create-document`example creates a Systems Manager document.`aws ssm create-document \ --content``file://exampleDocument.yml`\ --name`"Example"`\ --document-type`"Automation"`\ --document-format`YAML`Output: `{ "DocumentDescription": { "Hash": "fc2410281f40779e694a8b95975d0f9f316da8a153daa94e3d9921102EXAMPLE", "HashType": "Sha256", "Name": "Example", "Owner": "29884EXAMPLE", "CreatedDate": 1583256349.452, "Status": "Creating", "DocumentVersion": "1", "Description": "Document Example", "Parameters": [ { "Name": "AutomationAssumeRole", "Type": "String", "Description": "(Required) The ARN of the role that allows Automation to perform the actions on your behalf. If no role is specified, Systems Manager Automation uses your IAM permissions to execute this document.", "DefaultValue": "" }, { "Name": "InstanceId", "Type": "String", "Description": "(Required) The ID of the Amazon EC2 instance.", "DefaultValue": "" } ], "PlatformTypes": [ "Windows", "Linux" ], "DocumentType": "Automation", "SchemaVersion": "0.3", "LatestVersion": "1", "DefaultVersion": "1", "DocumentFormat": "YAML", "Tags": [] } }`For more information, see [Creating Systems Manager Documents](https://docs.aws.amazon.com/systems-manager/latest/userguide/create-ssm-doc.html)in the*AWS Systems Manager User Guide*.- 
                    For API details, see [CreateDocument](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ssm/create-document.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `create-maintenance-window`.

- **AWS CLI**
- 
            
                    **Example 1: To create a maintenance window**The following `create-maintenance-window`example creates a new maintenance window that every five minutes for up to two hours (as needed), prevents new tasks from starting within one hour of the end of the maintenance window execution, allows unassociated targets (instances that you haven't registered with the maintenance window), and indicates through the use of custom tags that its creator intends to use it in a tutorial.`aws ssm create-maintenance-window \ --name``"My-Tutorial-Maintenance-Window"`\ --schedule`"rate(5 minutes)"`\ --duration`2`--cutoff`1`\ --allow-unassociated-targets \ --tags`"Key=Purpose,Value=Tutorial"`Output: `{ "WindowId": "mw-0c50858d01EXAMPLE" }`**Example 2: To create a maintenance window that runs only once**The following `create-maintenance-window`example creates a new maintenance window that only runs one time on the specified date and time.`aws ssm create-maintenance-window \ --name``My-One-Time-Maintenance-Window`\ --schedule`"at(2020-05-14T15:55:00)"`\ --duration`5`\ --cutoff`2`\ --allow-unassociated-targets \ --tags`"Key=Environment,Value=Production"`Output: `{ "WindowId": "mw-01234567890abcdef" }`For more information, see [Maintenance Windows](https://docs.aws.amazon.com/systems-manager/latest/userguide/systems-manager-maintenance.html)in the*AWS Systems Manager User Guide*.- 
                    For API details, see [CreateMaintenanceWindow](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ssm/create-maintenance-window.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `create-ops-item`.

- **AWS CLI**
- 
            
                    **To create an OpsItems**The following `create-ops-item`example uses the /aws/resources key in OperationalData to create an OpsItem with an Amazon DynamoDB related resource.`aws ssm create-ops-item \ --title``"EC2 instance disk full"`\ --description`"Log clean up may have failed which caused the disk to be full"`\ --priority`2`\ --source`ec2`\ --operational-data '`{"/aws/resources":{"Value":"[{\"arn\": \"arn:aws:dynamodb:us-west-2:12345678:table/OpsItems\"}]","Type":"SearchableString"}}`' \ --notifications Arn="arn:aws:sns:us-west-2:12345678:TestUser"Output: `{ "OpsItemId": "oi-1a2b3c4d5e6f" }`For more information, see [Creating OpsItems](https://docs.aws.amazon.com/systems-manager/latest/userguide/OpsCenter-creating-OpsItems.html)in the*AWS Systems Manager User Guide*.- 
                    For API details, see [CreateOpsItem](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ssm/create-ops-item.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `create-patch-baseline`.

- **AWS CLI**
- 
            
                    **Example 1: To create a patch baseline with auto-approval**The following `create-patch-baseline`example creates a patch baseline for Windows Server that approves patches for a production environment seven days after they are released by Microsoft.`aws ssm create-patch-baseline \ --name``"Windows-Production-Baseline-AutoApproval"`\ --operating-system`"WINDOWS"`\ --approval-rules`"PatchRules=[{PatchFilterGroup={PatchFilters=[{Key=MSRC_SEVERITY,Values=[Critical,Important,Moderate]},{Key=CLASSIFICATION,Values=[SecurityUpdates,Updates,UpdateRollups,CriticalUpdates]}]},ApproveAfterDays=7}]"`\ --description`"Baseline containing all updates approved for Windows Server production systems"`Output: `{ "BaselineId": "pb-045f10b4f3EXAMPLE" }`**Example 2: To create a patch baseline with an approval cutoff date**The following `create-patch-baseline`example creates a patch baseline for Windows Server that approves all patches for a production environment that are released on or before July 7, 2020.`aws ssm create-patch-baseline \ --name``"Windows-Production-Baseline-AutoApproval"`\ --operating-system`"WINDOWS"`\ --approval-rules`"PatchRules=[{PatchFilterGroup={PatchFilters=[{Key=MSRC_SEVERITY,Values=[Critical,Important,Moderate]},{Key=CLASSIFICATION,Values=[SecurityUpdates,Updates,UpdateRollups,CriticalUpdates]}]},ApproveUntilDate=2020-07-07}]"`\ --description`"Baseline containing all updates approved for Windows Server production systems"`Output: `{ "BaselineId": "pb-045f10b4f3EXAMPLE" }`**Example 3: To create a patch baseline with approval rules stored in a JSON file**The following `create-patch-baseline`example creates a patch baseline for Amazon Linux 2017.09 that approves patches for a production environment seven days after they are released, specifies approval rules for the patch baseline, and specifies a custom repository for patches.`aws ssm create-patch-baseline \ --cli-input-json``file://my-amazon-linux-approval-rules-and-repo.json`Contents of `my-amazon-linux-approval-rules-and-repo.json`:`{ "Name": "Amazon-Linux-2017.09-Production-Baseline", "Description": "My approval rules patch baseline for Amazon Linux 2017.09 instances", "OperatingSystem": "AMAZON_LINUX", "Tags": [ { "Key": "Environment", "Value": "Production" } ], "ApprovalRules": { "PatchRules": [ { "ApproveAfterDays": 7, "EnableNonSecurity": true, "PatchFilterGroup": { "PatchFilters": [ { "Key": "SEVERITY", "Values": [ "Important", "Critical" ] }, { "Key": "CLASSIFICATION", "Values": [ "Security", "Bugfix" ] }, { "Key": "PRODUCT", "Values": [ "AmazonLinux2017.09" ] } ] } } ] }, "Sources": [ { "Name": "My-AL2017.09", "Products": [ "AmazonLinux2017.09" ], "Configuration": "[amzn-main] \nname=amzn-main-Base\nmirrorlist=http://repo./$awsregion./$awsdomain//$releasever/main/mirror.list //nmirrorlist_expire=300//nmetadata_expire=300 \npriority=10 \nfailovermethod=priority \nfastestmirror_enabled=0 \ngpgcheck=1 \ngpgkey=file:///etc/pki/rpm-gpg/RPM-GPG-KEY-amazon-ga \nenabled=1 \nretries=3 \ntimeout=5\nreport_instanceid=yes" } ] }`**Example 4: To create a patch baseline that specifies approved and rejected patches**The following `create-patch-baseline`example explicitly specifies patches to approve and reject as exception to the default approval rules.`aws ssm create-patch-baseline \ --name``"Amazon-Linux-2017.09-Alpha-Baseline"`\ --description`"My custom approve/reject patch baseline for Amazon Linux 2017.09 instances"`\ --operating-system`"AMAZON_LINUX"`\ --approved-patches`"CVE-2018-1234567,example-pkg-EE-2018*.amzn1.noarch"`\ --approved-patches-compliance-level`"HIGH"`\ --approved-patches-enable-non-security \ --tags`"Key=Environment,Value=Alpha"`For more information, see [Create a Custom Patch Baseline](https://docs.aws.amazon.com/systems-manager/latest/userguide/sysman-patch-baseline-console.html)in the*AWS Systems Manager User Guide*.- 
                    For API details, see [CreatePatchBaseline](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ssm/create-patch-baseline.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `create-resource-data-sync`.

- **AWS CLI**
- 
            
                    **To create a resource data sync**This example creates a resource data sync. There is no output if the command succeeds. Command: `aws ssm create-resource-data-sync --sync-name``"ssm-resource-data-sync"`--s3-destination`"BucketName=ssm-bucket,Prefix=inventory,SyncFormat=JsonSerDe,Region=us-east-1"`- 
                    For API details, see [CreateResourceDataSync](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ssm/create-resource-data-sync.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `delete-activation`.

- **AWS CLI**
- 
            
                    **To delete a managed instance activation**The following `delete-activation`example deletes a managed instance activation.`aws ssm delete-activation \ --activation-id``"aa673477-d926-42c1-8757-1358cEXAMPLE"`This command produces no output. For more information, see [Setting Up AWS Systems Manager for Hybrid Environments](https://docs.aws.amazon.com/systems-manager/latest/userguide/systems-manager-managedinstances.html)in the*AWS Systems Manager User Guide*.- 
                    For API details, see [DeleteActivation](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ssm/delete-activation.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `delete-association`.

- **AWS CLI**
- 
            
                    **Example 1: To delete an association using the association ID**The following `delete-association`example deletes the association for the specified association ID. There is no output if the command succeeds.`aws ssm delete-association \ --association-id``"8dfe3659-4309-493a-8755-0123456789ab"`This command produces no output. For more information, see [Editing and creating a new version of an association](https://docs.aws.amazon.com/systems-manager/latest/userguide/sysman-state-assoc-edit.html)in the*AWS Systems Manager User Guide*.**Example 2: To delete an association**The following `delete-association`example deletes the association between an instance and a document. There is no output if the command succeeds.`aws ssm delete-association \ --instance-id``"i-1234567890abcdef0"`\ --name`"AWS-UpdateSSMAgent"`This command produces no output. For more information, see [Working with associations in Systems Manager](https://docs.aws.amazon.com/systems-manager/latest/userguide/systems-manager-associations.html)in the*AWS Systems Manager User Guide*.- 
                    For API details, see [DeleteAssociation](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ssm/delete-association.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `delete-document`.

- **AWS CLI**
- 
            
                    **To delete a document**The following `delete-document`example deletes a Systems Manager document.`aws ssm delete-document \ --name``"Example"`This command produces no output. For more information, see [Creating Systems Manager Documents](https://docs.aws.amazon.com/systems-manager/latest/userguide/create-ssm-doc.html)in the*AWS Systems Manager User Guide*.- 
                    For API details, see [DeleteDocument](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ssm/delete-document.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `delete-inventory`.

- **AWS CLI**
- 
            
                    **To delete a custom inventory type**This example deletes a custom inventory schema. Command: `aws ssm delete-inventory --type-name``"Custom:RackInfo"`--schema-delete-option`"DeleteSchema"`Output: `{ "DeletionId": "d72ac9e8-1f60-4d40-b1c6-bf8c78c68c4d", "TypeName": "Custom:RackInfo", "DeletionSummary": { "TotalCount": 1, "RemainingCount": 1, "SummaryItems": [ { "Version": "1.0", "Count": 1, "RemainingCount": 1 } ] } }`**To disable a custom inventory type**This example disables a custom inventory schema. Command: `aws ssm delete-inventory --type-name``"Custom:RackInfo"`--schema-delete-option`"DisableSchema"`Output: `{ "DeletionId": "6961492a-8163-44ec-aa1e-923364dd0850", "TypeName": "Custom:RackInformation", "DeletionSummary": { "TotalCount": 0, "RemainingCount": 0, "SummaryItems": [] } }`- 
                    For API details, see [DeleteInventory](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ssm/delete-inventory.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `delete-maintenance-window`.

- **AWS CLI**
- 
            
                    **To delete a maintenance window**This `delete-maintenance-window`example removes the specified maintenance window.`aws ssm delete-maintenance-window \ --window-id``"mw-1a2b3c4d5e6f7g8h9"`Output: `{ "WindowId":"mw-1a2b3c4d5e6f7g8h9" }`For more information, see [Delete a Maintenance Window (AWS CLI)](https://docs.aws.amazon.com/systems-manager/latest/userguide/mw-cli-tutorial-delete-mw.html)in the*AWS Systems Manager User Guide*.- 
                    For API details, see [DeleteMaintenanceWindow](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ssm/delete-maintenance-window.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `delete-parameter`.

- **AWS CLI**
- 
            
                    **To delete a parameter**The following `delete-parameter`example deletes the specified single parameter.`aws ssm delete-parameter \ --name``"MyParameter"`This command produces no output. For more information, see [Working with Parameter Store](https://docs.aws.amazon.com/systems-manager/latest/userguide/parameter-store-working-with.html)in the*AWS Systems Manager User Guide*.- 
                    For API details, see [DeleteParameter](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ssm/delete-parameter.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `delete-parameters`.

- **AWS CLI**
- 
            
                    **To delete a list of parameters**The following `delete-parameters`example deletes the specified parameters.`aws ssm delete-parameters \ --names``"MyFirstParameter"``"MySecondParameter"``"MyInvalidParameterName"`Output: `{ "DeletedParameters": [ "MyFirstParameter", "MySecondParameter" ], "InvalidParameters": [ "MyInvalidParameterName" ] }`For more information, see [Working with Parameter Store](https://docs.aws.amazon.com/systems-manager/latest/userguide/parameter-store-working-with.html)in the*AWS Systems Manager User Guide*.- 
                    For API details, see [DeleteParameters](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ssm/delete-parameters.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `delete-patch-baseline`.

- **AWS CLI**
- 
            
                    **To delete a patch baseline**The following `delete-patch-baseline`example deletes the specified patch baseline.`aws ssm delete-patch-baseline \ --baseline-id``"pb-045f10b4f382baeda"`Output: `{ "BaselineId": "pb-045f10b4f382baeda" }`For more information, see [Update or Delete a Patch Baseline (Console)](https://docs.aws.amazon.com/systems-manager/latest/userguide/patch-baseline-update-or-delete.html)in the*AWS Systems Manager User Guide*.- 
                    For API details, see [DeletePatchBaseline](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ssm/delete-patch-baseline.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `delete-resource-data-sync`.

- **AWS CLI**
- 
            
                    **To delete a resource data sync**This example deletes a resource data sync. There is no output if the command succeeds. Command: `aws ssm delete-resource-data-sync --sync-name``"ssm-resource-data-sync"`- 
                    For API details, see [DeleteResourceDataSync](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ssm/delete-resource-data-sync.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `deregister-managed-instance`.

- **AWS CLI**
- 
            
                    **To deregister a managed instance**The following `deregister-managed-instance`example deregisters the specified managed instance.`aws ssm deregister-managed-instance \ --instance-id '``mi-08ab247cdfEXAMPLE`'This command produces no output. For more information, see [Deregistering managed nodes in a hybrid and multicloud environment](https://docs.aws.amazon.com/systems-manager/latest/userguide/fleet-manager-deregister-hybrid-nodes.html)in the*AWS Systems Manager User Guide*.- 
                    For API details, see [DeregisterManagedInstance](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ssm/deregister-managed-instance.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `deregister-patch-baseline-for-patch-group`.

- **AWS CLI**
- 
            
                    **To deregister a patch group from a patch baseline**The following `deregister-patch-baseline-for-patch-group`example deregisters the specified patch group from the specified patch baseline.`aws ssm deregister-patch-baseline-for-patch-group \ --patch-group``"Production"`\ --baseline-id`"pb-0ca44a362fEXAMPLE"`Output: `{ "PatchGroup":"Production", "BaselineId":"pb-0ca44a362fEXAMPLE" }`For more information, see [Add a Patch Group to a Patch Baseline](https://docs.aws.amazon.com/systems-manager/latest/userguide/sysman-patch-group-patchbaseline.html)in the*AWS Systems Manager User Guide*.- 
                    For API details, see [DeregisterPatchBaselineForPatchGroup](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ssm/deregister-patch-baseline-for-patch-group.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `deregister-target-from-maintenance-window`.

- **AWS CLI**
- 
            
                    **To remove a target from a maintenance window**The following `deregister-target-from-maintenance-window`example removes the specified target from the specified maintenance window.`aws ssm deregister-target-from-maintenance-window \ --window-id``"mw-ab12cd34ef56gh78"`\ --window-target-id`"1a2b3c4d-1a2b-1a2b-1a2b-1a2b3c4d-1a2"`Output: `{ "WindowId":"mw-ab12cd34ef56gh78", "WindowTargetId":"1a2b3c4d-1a2b-1a2b-1a2b-1a2b3c4d-1a2" }`For more information, see [Update a Maintenance Window (AWS CLI)](https://docs.aws.amazon.com/systems-manager/latest/userguide/maintenance-windows-cli-tutorials-update.html)in the*AWS Systems Manager User Guide*.- 
                    For API details, see [DeregisterTargetFromMaintenanceWindow](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ssm/deregister-target-from-maintenance-window.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `deregister-task-from-maintenance-window`.

- **AWS CLI**
- 
            
                    **To remove a task from a maintenance window**The following `deregister-task-from-maintenance-window`example removes the specified task from the specified maintenance window.`aws ssm deregister-task-from-maintenance-window \ --window-id``"mw-ab12cd34ef56gh78"`\ --window-task-id`"1a2b3c4d-1a2b-1a2b-1a2b-1a2b3c4d5e6c"`Output: `{ "WindowTaskId":"1a2b3c4d-1a2b-1a2b-1a2b-1a2b3c4d5e6c", "WindowId":"mw-ab12cd34ef56gh78" }`For more information, see [Systems Manager Maintenance Windows Tutorials (AWS CLI)](https://docs.aws.amazon.com/systems-manager/latest/userguide/maintenance-windows-tutorials.html)in the*AWS Systems Manager User Guide*.- 
                    For API details, see [DeregisterTaskFromMaintenanceWindow](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ssm/deregister-task-from-maintenance-window.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `describe-activations`.

- **AWS CLI**
- 
            
                    **To describe activations**The following `describe-activations`example lists details about the activations in your AWS account.`aws ssm describe-activations`Output: `{ "ActivationList": [ { "ActivationId": "5743558d-563b-4457-8682-d16c3EXAMPLE", "Description": "Example1", "IamRole": "HybridWebServersRole, "RegistrationLimit": 5, "RegistrationsCount": 5, "ExpirationDate": 1584316800.0, "Expired": false, "CreatedDate": 1581954699.792 }, { "ActivationId": "3ee0322b-f62d-40eb-b672-13ebfEXAMPLE", "Description": "Example2", "IamRole": "HybridDatabaseServersRole", "RegistrationLimit": 5, "RegistrationsCount": 5, "ExpirationDate": 1580515200.0, "Expired": true, "CreatedDate": 1578064132.002 }, ] }`For more information, see [Step 4: Create a Managed-Instance Activation for a Hybrid Environment](https://docs.aws.amazon.com/systems-manager/latest/userguide/sysman-managed-instance-activation.html)in the*AWS Systems Manager User Guide*.- 
                    For API details, see [DescribeActivations](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ssm/describe-activations.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `describe-association-execution-targets`.

- **AWS CLI**
- 
            
                    **To get details of an association execution**The following `describe-association-execution-targets`example describes the specified association execution.`aws ssm describe-association-execution-targets \ --association-id``"8dfe3659-4309-493a-8755-0123456789ab"`\ --execution-id`"7abb6378-a4a5-4f10-8312-0123456789ab"`Output: `{ "AssociationExecutionTargets": [ { "AssociationId": "8dfe3659-4309-493a-8755-0123456789ab", "AssociationVersion": "1", "ExecutionId": "7abb6378-a4a5-4f10-8312-0123456789ab", "ResourceId": "i-1234567890abcdef0", "ResourceType": "ManagedInstance", "Status": "Success", "DetailedStatus": "Success", "LastExecutionDate": 1550505538.497, "OutputSource": { "OutputSourceId": "97fff367-fc5a-4299-aed8-0123456789ab", "OutputSourceType": "RunCommand" } } ] }`For more information, see [Viewing association histories](https://docs.aws.amazon.com/systems-manager/latest/userguide/sysman-state-assoc-history.html)in the*AWS Systems Manager User Guide*.- 
                    For API details, see [DescribeAssociationExecutionTargets](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ssm/describe-association-execution-targets.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `describe-association-executions`.

- **AWS CLI**
- 
            
                    **Example 1: To get details of all executions for an association**The following `describe-association-executions`example describes all executions of the specified association.`aws ssm describe-association-executions \ --association-id``"8dfe3659-4309-493a-8755-0123456789ab"`Output: `{ "AssociationExecutions": [ { "AssociationId": "8dfe3659-4309-493a-8755-0123456789ab", "AssociationVersion": "1", "ExecutionId": "474925ef-1249-45a2-b93d-0123456789ab", "Status": "Success", "DetailedStatus": "Success", "CreatedTime": 1550505827.119, "ResourceCountByStatus": "{Success=1}" }, { "AssociationId": "8dfe3659-4309-493a-8755-0123456789ab", "AssociationVersion": "1", "ExecutionId": "7abb6378-a4a5-4f10-8312-0123456789ab", "Status": "Success", "DetailedStatus": "Success", "CreatedTime": 1550505536.843, "ResourceCountByStatus": "{Success=1}" }, ... ] }`For more information, see [Viewing association histories](https://docs.aws.amazon.com/systems-manager/latest/userguide/sysman-state-assoc-history.html)in the*AWS Systems Manager User Guide*.**Example 2: To get details of all executions for an association after a specific date and time**The following `describe-association-executions`example describes all executions of an association after the specified date and time.`aws ssm describe-association-executions \ --association-id``"8dfe3659-4309-493a-8755-0123456789ab"`\ --filters`"Key=CreatedTime,Value=2019-02-18T16:00:00Z,Type=GREATER_THAN"`Output: `{ "AssociationExecutions": [ { "AssociationId": "8dfe3659-4309-493a-8755-0123456789ab", "AssociationVersion": "1", "ExecutionId": "474925ef-1249-45a2-b93d-0123456789ab", "Status": "Success", "DetailedStatus": "Success", "CreatedTime": 1550505827.119, "ResourceCountByStatus": "{Success=1}" }, { "AssociationId": "8dfe3659-4309-493a-8755-0123456789ab", "AssociationVersion": "1", "ExecutionId": "7abb6378-a4a5-4f10-8312-0123456789ab", "Status": "Success", "DetailedStatus": "Success", "CreatedTime": 1550505536.843, "ResourceCountByStatus": "{Success=1}" }, ... ] }`For more information, see [Viewing association histories](https://docs.aws.amazon.com/systems-manager/latest/userguide/sysman-state-assoc-history.html)in the*AWS Systems Manager User Guide*.- 
                    For API details, see [DescribeAssociationExecutions](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ssm/describe-association-executions.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `describe-association`.

- **AWS CLI**
- 
            
                    **Example 1: To get details of an association**The following `describe-association`example describes the association for the specified association ID.`aws ssm describe-association \ --association-id``"8dfe3659-4309-493a-8755-0123456789ab"`Output: `{ "AssociationDescription": { "Name": "AWS-GatherSoftwareInventory", "AssociationVersion": "1", "Date": 1534864780.995, "LastUpdateAssociationDate": 1543235759.81, "Overview": { "Status": "Success", "AssociationStatusAggregatedCount": { "Success": 2 } }, "DocumentVersion": "$DEFAULT", "Parameters": { "applications": [ "Enabled" ], "awsComponents": [ "Enabled" ], "customInventory": [ "Enabled" ], "files": [ "" ], "instanceDetailedInformation": [ "Enabled" ], "networkConfig": [ "Enabled" ], "services": [ "Enabled" ], "windowsRegistry": [ "" ], "windowsRoles": [ "Enabled" ], "windowsUpdates": [ "Enabled" ] }, "AssociationId": "8dfe3659-4309-493a-8755-0123456789ab", "Targets": [ { "Key": "InstanceIds", "Values": [ "*" ] } ], "ScheduleExpression": "rate(24 hours)", "LastExecutionDate": 1550501886.0, "LastSuccessfulExecutionDate": 1550501886.0, "AssociationName": "Inventory-Association" } }`For more information, see [Editing and creating a new version of an association](https://docs.aws.amazon.com/systems-manager/latest/userguide/sysman-state-assoc-edit.html)in the*AWS Systems Manager User Guide*.**Example 2: To get details of an association for a specific instance and document**The following `describe-association`example describes the association between an instance and a document.`aws ssm describe-association \ --instance-id``"i-1234567890abcdef0"`\ --name`"AWS-UpdateSSMAgent"`Output: `{ "AssociationDescription": { "Status": { "Date": 1487876122.564, "Message": "Associated with AWS-UpdateSSMAgent", "Name": "Associated" }, "Name": "AWS-UpdateSSMAgent", "InstanceId": "i-1234567890abcdef0", "Overview": { "Status": "Pending", "DetailedStatus": "Associated", "AssociationStatusAggregatedCount": { "Pending": 1 } }, "AssociationId": "d8617c07-2079-4c18-9847-1234567890ab", "DocumentVersion": "$DEFAULT", "LastUpdateAssociationDate": 1487876122.564, "Date": 1487876122.564, "Targets": [ { "Values": [ "i-1234567890abcdef0" ], "Key": "InstanceIds" } ] } }`For more information, see [Editing and creating a new version of an association](https://docs.aws.amazon.com/systems-manager/latest/userguide/sysman-state-assoc-edit.html)in the*AWS Systems Manager User Guide*.- 
                    For API details, see [DescribeAssociation](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ssm/describe-association.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `describe-automation-executions`.

- **AWS CLI**
- 
            
                    **To describe an automation execution**The following `describe-automation-executions`example displays details about an Automation execution.`aws ssm describe-automation-executions \ --filters``Key=ExecutionId,Values=73c8eef8-f4ee-4a05-820c-e354fEXAMPLE`Output: `{ "AutomationExecutionMetadataList": [ { "AutomationExecutionId": "73c8eef8-f4ee-4a05-820c-e354fEXAMPLE", "DocumentName": "AWS-StartEC2Instance", "DocumentVersion": "1", "AutomationExecutionStatus": "Success", "ExecutionStartTime": 1583737233.748, "ExecutionEndTime": 1583737234.719, "ExecutedBy": "arn:aws:sts::29884EXAMPLE:assumed-role/mw_service_role/OrchestrationService", "LogFile": "", "Outputs": {}, "Mode": "Auto", "Targets": [], "ResolvedTargets": { "ParameterValues": [], "Truncated": false }, "AutomationType": "Local" } ] }`For more information, see [Running a Simple Automation Workflow](https://docs.aws.amazon.com/systems-manager/latest/userguide/automation-working-executing.html)in the*AWS Systems Manager User Guide*.- 
                    For API details, see [DescribeAutomationExecutions](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ssm/describe-automation-executions.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `describe-automation-step-executions`.

- **AWS CLI**
- 
            
                    **Example 1: To describe all steps for an automation execution**The following `describe-automation-step-executions`example displays details about the steps of an Automation execution.`aws ssm describe-automation-step-executions \ --automation-execution-id``73c8eef8-f4ee-4a05-820c-e354fEXAMPLE`Output: `{ "StepExecutions": [ { "StepName": "startInstances", "Action": "aws:changeInstanceState", "ExecutionStartTime": 1583737234.134, "ExecutionEndTime": 1583737234.672, "StepStatus": "Success", "Inputs": { "DesiredState": "\"running\"", "InstanceIds": "[\"i-0cb99161f6EXAMPLE\"]" }, "Outputs": { "InstanceStates": [ "running" ] }, "StepExecutionId": "95e70479-cf20-4d80-8018-7e4e2EXAMPLE", "OverriddenParameters": {} } ] }`**Example 2: To describe a specific step for an automation execution**The following `describe-automation-step-executions`example displays details about a specific step of an Automation execution.`aws ssm describe-automation-step-executions \ --automation-execution-id``73c8eef8-f4ee-4a05-820c-e354fEXAMPLE`\ --filters`Key=StepExecutionId,Values=95e70479-cf20-4d80-8018-7e4e2EXAMPLE`For more information, see [Running an Automation Workflow Step by Step (Command Line)](https://docs.aws.amazon.com/systems-manager/latest/userguide/automation-working-executing-manually.html#automation-working-executing-manually-commandline)in the*AWS Systems Manager User Guide*.- 
                    For API details, see [DescribeAutomationStepExecutions](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ssm/describe-automation-step-executions.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `describe-available-patches`.

- **AWS CLI**
- 
            
                    **To get available patches**The following `describe-available-patches`example retrieves details about all available patches for Windows Server 2019 that have a MSRC severity of Critical.`aws ssm describe-available-patches \ --filters``"Key=PRODUCT,Values=WindowsServer2019"``"Key=MSRC_SEVERITY,Values=Critical"`Output: `{ "Patches": [ { "Id": "fe6bd8c2-3752-4c8b-ab3e-1a7ed08767ba", "ReleaseDate": 1544047205.0, "Title": "2018-11 Update for Windows Server 2019 for x64-based Systems (KB4470788)", "Description": "Install this update to resolve issues in Windows. For a complete listing of the issues that are included in this update, see the associated Microsoft Knowledge Base article for more information. After you install this item, you may have to restart your computer.", "ContentUrl": "https://support.microsoft.com/en-us/kb/4470788", "Vendor": "Microsoft", "ProductFamily": "Windows", "Product": "WindowsServer2019", "Classification": "SecurityUpdates", "MsrcSeverity": "Critical", "KbNumber": "KB4470788", "MsrcNumber": "", "Language": "All" }, { "Id": "c96115e1-5587-4115-b851-22baa46a3f11", "ReleaseDate": 1549994410.0, "Title": "2019-02 Security Update for Adobe Flash Player for Windows Server 2019 for x64-based Systems (KB4487038)", "Description": "A security issue has been identified in a Microsoft software product that could affect your system. You can help protect your system by installing this update from Microsoft. For a complete listing of the issues that are included in this update, see the associated Microsoft Knowledge Base article. After you install this update, you may have to restart your system.", "ContentUrl": "https://support.microsoft.com/en-us/kb/4487038", "Vendor": "Microsoft", "ProductFamily": "Windows", "Product": "WindowsServer2019", "Classification": "SecurityUpdates", "MsrcSeverity": "Critical", "KbNumber": "KB4487038", "MsrcNumber": "", "Language": "All" }, ... ] }`**To get details of a specific patch**The following `describe-available-patches`example retrieves details about the specified patch.`aws ssm describe-available-patches \ --filters``"Key=PATCH_ID,Values=KB4480979"`Output: `{ "Patches": [ { "Id": "680861e3-fb75-432e-818e-d72e5f2be719", "ReleaseDate": 1546970408.0, "Title": "2019-01 Security Update for Adobe Flash Player for Windows Server 2016 for x64-based Systems (KB4480979)", "Description": "A security issue has been identified in a Microsoft software product that could affect your system. You can help protect your system by installing this update from Microsoft. For a complete listing of the issues that are included in this update, see the associated Microsoft Knowledge Base article. After you install this update, you may have to restart your system.", "ContentUrl": "https://support.microsoft.com/en-us/kb/4480979", "Vendor": "Microsoft", "ProductFamily": "Windows", "Product": "WindowsServer2016", "Classification": "SecurityUpdates", "MsrcSeverity": "Critical", "KbNumber": "KB4480979", "MsrcNumber": "", "Language": "All" } ] }`For more information, see [How Patch Manager Operations Work](https://docs.aws.amazon.com/systems-manager/latest/userguide/patch-manager-how-it-works.html)in the*AWS Systems Manager User Guide*.- 
                    For API details, see [DescribeAvailablePatches](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ssm/describe-available-patches.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `describe-document-permission`.

- **AWS CLI**
- 
            
                    **To describe document permissions**The following `describe-document-permission`example displays permission details about a Systems Manager document that is shared publicly.`aws ssm describe-document-permission \ --name``"Example"`\ --permission-type`"Share"`Output: `{ "AccountIds": [ "all" ], "AccountSharingInfoList": [ { "AccountId": "all", "SharedDocumentVersion": "$DEFAULT" } ] }`For more information, see [Share a Systems Manager Document](https://docs.aws.amazon.com/systems-manager/latest/userguide/ssm-how-to-share.html)in the*AWS Systems Manager User Guide*.- 
                    For API details, see [DescribeDocumentPermission](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ssm/describe-document-permission.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `describe-document`.

- **AWS CLI**
- 
            
                    **To display details of a document**The following `describe-document`example displays details about a Systems Manager document in your AWS account.`aws ssm describe-document \ --name``"Example"`Output: `{ "Document": { "Hash": "fc2410281f40779e694a8b95975d0f9f316da8a153daa94e3d9921102EXAMPLE", "HashType": "Sha256", "Name": "Example", "Owner": "29884EXAMPLE", "CreatedDate": 1583257938.266, "Status": "Active", "DocumentVersion": "1", "Description": "Document Example", "Parameters": [ { "Name": "AutomationAssumeRole", "Type": "String", "Description": "(Required) The ARN of the role that allows Automation to perform the actions on your behalf. If no role is specified, Systems Manager Automation uses your IAM permissions to execute this document.", "DefaultValue": "" }, { "Name": "InstanceId", "Type": "String", "Description": "(Required) The ID of the Amazon EC2 instance.", "DefaultValue": "" } ], "PlatformTypes": [ "Windows", "Linux" ], "DocumentType": "Automation", "SchemaVersion": "0.3", "LatestVersion": "1", "DefaultVersion": "1", "DocumentFormat": "YAML", "Tags": [] } }`For more information, see [Creating Systems Manager Documents](https://docs.aws.amazon.com/systems-manager/latest/userguide/create-ssm-doc.html)in the*AWS Systems Manager User Guide*.- 
                    For API details, see [DescribeDocument](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ssm/describe-document.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `describe-effective-instance-associations`.

- **AWS CLI**
- 
            
                    **To get details of the effective associations for an instance**The following `describe-effective-instance-associations`example retrieves details about the effective associations for an instance.Command: `aws ssm describe-effective-instance-associations --instance-id``"i-1234567890abcdef0"`Output: `{ "Associations": [ { "AssociationId": "8dfe3659-4309-493a-8755-0123456789ab", "InstanceId": "i-1234567890abcdef0", "Content": "{\n \"schemaVersion\": \"1.2\",\n \"description\": \"Update the Amazon SSM Agent to the latest version or specified version.\",\n \"parameters\": {\n \"version\": {\n \"default\": \"\",\n \"description\": \"(Optional) A specific version of the Amazon SSM Agent to install. If not specified, the agent will be updated to the latest version.\",\n \"type\": \"String\"\n },\n \"allowDowngrade\": {\n \"default\": \"false\",\n \"description\": \"(Optional) Allow the Amazon SSM Agent service to be downgraded to an earlier version. If set to false, the service can be upgraded to newer versions only (default). If set to true, specify the earlier version.\",\n \"type\": \"String\",\n \"allowedValues\": [\n \"true\",\n \"false\"\n ]\n }\n },\n \"runtimeConfig\": {\n \"aws:updateSsmAgent\": {\n \"properties\": [\n {\n \"agentName\": \"amazon-ssm-agent\",\n \"source\": \"https://s3.{Region}.amazonaws.com/amazon-ssm-{Region}/ssm-agent-manifest.json\",\n \"allowDowngrade\": \"{{ allowDowngrade }}\",\n \"targetVersion\": \"{{ version }}\"\n }\n ]\n }\n }\n}\n", "AssociationVersion": "1" } ] }`- 
                    For API details, see [DescribeEffectiveInstanceAssociations](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ssm/describe-effective-instance-associations.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `describe-effective-patches-for-patch-baseline`.

- **AWS CLI**
- 
            
                    **Example 1: To get all patches defined by a custom patch baseline**The following `describe-effective-patches-for-patch-baseline`example returns the patches defined by a custom patch baseline in the current AWS account. Note that for a custom baseline, only the ID is required for`--baseline-id`.`aws ssm describe-effective-patches-for-patch-baseline \ --baseline-id``"pb-08b654cf9b9681f04"`Output: `{ "EffectivePatches": [ { "Patch": { "Id": "fe6bd8c2-3752-4c8b-ab3e-1a7ed08767ba", "ReleaseDate": 1544047205.0, "Title": "2018-11 Update for Windows Server 2019 for x64-based Systems (KB4470788)", "Description": "Install this update to resolve issues in Windows. For a complete listing of the issues that are included in this update, see the associated Microsoft Knowledge Base article for more information. After you install this item, you may have to restart your computer.", "ContentUrl": "https://support.microsoft.com/en-us/kb/4470788", "Vendor": "Microsoft", "ProductFamily": "Windows", "Product": "WindowsServer2019", "Classification": "SecurityUpdates", "MsrcSeverity": "Critical", "KbNumber": "KB4470788", "MsrcNumber": "", "Language": "All" }, "PatchStatus": { "DeploymentStatus": "APPROVED", "ComplianceLevel": "CRITICAL", "ApprovalDate": 1544047205.0 } }, { "Patch": { "Id": "915a6b1a-f556-4d83-8f50-b2e75a9a7e58", "ReleaseDate": 1549994400.0, "Title": "2019-02 Cumulative Update for .NET Framework 3.5 and 4.7.2 for Windows Server 2019 for x64 (KB4483452)", "Description": "A security issue has been identified in a Microsoft software product that could affect your system. You can help protect your system by installing this update from Microsoft. For a complete listing of the issues that are included in this update, see the associated Microsoft Knowledge Base article. After you install this update, you may have to restart your system.", "ContentUrl": "https://support.microsoft.com/en-us/kb/4483452", "Vendor": "Microsoft", "ProductFamily": "Windows", "Product": "WindowsServer2019", "Classification": "SecurityUpdates", "MsrcSeverity": "Important", "KbNumber": "KB4483452", "MsrcNumber": "", "Language": "All" }, "PatchStatus": { "DeploymentStatus": "APPROVED", "ComplianceLevel": "CRITICAL", "ApprovalDate": 1549994400.0 } }, ... ], "NextToken": "--token string truncated--" }`**Example 2: To get all patches defined by an AWS managed patch baseline**The following `describe-effective-patches-for-patch-baseline`example returns the patches defined by an AWS managed patch baseline. Note that for an AWS managed baseline, the complete baseline ARN is required for`--baseline-id``aws ssm describe-effective-patches-for-patch-baseline \ --baseline-id``"arn:aws:ssm:us-east-2:733109147000:patchbaseline/pb-020d361a05defe4ed"`See example 1 for sample output. For more information, see [How Security Patches Are Selected](https://docs.aws.amazon.com/systems-manager/latest/userguide/patch-manager-how-it-works-selection.html)in the*AWS Systems Manager User Guide*.- 
                    For API details, see [DescribeEffectivePatchesForPatchBaseline](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ssm/describe-effective-patches-for-patch-baseline.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `describe-instance-associations-status`.

- **AWS CLI**
- 
            
                    **To describe the status of an instance's associations**This example shows details of the associations for an instance. Command: `aws ssm describe-instance-associations-status --instance-id``"i-1234567890abcdef0"`Output: `{ "InstanceAssociationStatusInfos": [ { "AssociationId": "8dfe3659-4309-493a-8755-0123456789ab", "Name": "AWS-GatherSoftwareInventory", "DocumentVersion": "1", "AssociationVersion": "1", "InstanceId": "i-1234567890abcdef0", "ExecutionDate": 1550501886.0, "Status": "Success", "ExecutionSummary": "1 out of 1 plugin processed, 1 success, 0 failed, 0 timedout, 0 skipped. ", "AssociationName": "Inventory-Association" }, { "AssociationId": "5c5a31f6-6dae-46f9-944c-0123456789ab", "Name": "AWS-UpdateSSMAgent", "DocumentVersion": "1", "AssociationVersion": "1", "InstanceId": "i-1234567890abcdef0", "ExecutionDate": 1550505828.548, "Status": "Success", "DetailedStatus": "Success", "AssociationName": "UpdateSSMAgent" } ] }`- 
                    For API details, see [DescribeInstanceAssociationsStatus](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ssm/describe-instance-associations-status.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `describe-instance-information`.

- **AWS CLI**
- 
            
                    **Example 1: To describe managed instance information**The following `describe-instance-information`example retrieves details of each of your managed instances.`aws ssm describe-instance-information`**Example 2: To describe information about a specific managed instance**The following `describe-instance-information`example shows details of the managed instance`i-028ea792daEXAMPLE`.`aws ssm describe-instance-information \ --filters``"Key=InstanceIds,Values=i-028ea792daEXAMPLE"`**Example 3: To describe information about managed instances with a specific tag key**The following `describe-instance-information`example shows details for managed instances that have the tag key`DEV`.`aws ssm describe-instance-information \ --filters``"Key=tag-key,Values=DEV"`Output: `{ "InstanceInformationList": [ { "InstanceId": "i-028ea792daEXAMPLE", "PingStatus": "Online", "LastPingDateTime": 1582221233.421, "AgentVersion": "2.3.842.0", "IsLatestVersion": true, "PlatformType": "Linux", "PlatformName": "SLES", "PlatformVersion": "15.1", "ResourceType": "EC2Instance", "IPAddress": "192.0.2.0", "ComputerName": "ip-198.51.100.0.us-east-2.compute.internal", "AssociationStatus": "Success", "LastAssociationExecutionDate": 1582220806.0, "LastSuccessfulAssociationExecutionDate": 1582220806.0, "AssociationOverview": { "DetailedStatus": "Success", "InstanceAssociationStatusAggregatedCount": { "Success": 2 } } } ] }`For more information, see [Managed Instances](https://docs.aws.amazon.com/systems-manager/latest/userguide/managed_instances.html)in the*AWS Systems Manager User Guide*.- 
                    For API details, see [DescribeInstanceInformation](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ssm/describe-instance-information.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `describe-instance-patch-states-for-patch-group`.

- **AWS CLI**
- 
            
                    **Example 1: To get the instance states for a patch group**The following `describe-instance-patch-states-for-patch-group`example retrieves details about the patch summary states per-instance for the specified patch group.`aws ssm describe-instance-patch-states-for-patch-group \ --patch-group``"Production"`Output: `{ "InstancePatchStates": [ { "InstanceId": "i-02573cafcfEXAMPLE", "PatchGroup": "Production", "BaselineId": "pb-0c10e65780EXAMPLE", "SnapshotId": "a3f5ff34-9bc4-4d2c-a665-4d1c1EXAMPLE", "OwnerInformation": "", "InstalledCount": 32, "InstalledOtherCount": 1, "InstalledPendingRebootCount": 0, "InstalledRejectedCount": 0, "MissingCount": 2, "FailedCount": 0, "UnreportedNotApplicableCount": 2671, "NotApplicableCount": 400, "OperationStartTime": "2021-08-04T11:03:50.590000-07:00", "OperationEndTime": "2021-08-04T11:04:21.555000-07:00", "Operation": "Scan", "RebootOption": "NoReboot", "CriticalNonCompliantCount": 0, "SecurityNonCompliantCount": 1, "OtherNonCompliantCount": 0 }, { "InstanceId": "i-0471e04240EXAMPLE", "PatchGroup": "Production", "BaselineId": "pb-09ca3fb51fEXAMPLE", "SnapshotId": "05d8ffb0-1bbe-4812-ba2d-d9b7bEXAMPLE", "OwnerInformation": "", "InstalledCount": 32, "InstalledOtherCount": 1, "InstalledPendingRebootCount": 0, "InstalledRejectedCount": 0, "MissingCount": 2, "FailedCount": 0, "UnreportedNotApplicableCount": 2671, "NotApplicableCount": 400, "OperationStartTime": "2021-08-04T22:06:20.340000-07:00", "OperationEndTime": "2021-08-04T22:07:11.220000-07:00", "Operation": "Scan", "RebootOption": "NoReboot", "CriticalNonCompliantCount": 0, "SecurityNonCompliantCount": 1, "OtherNonCompliantCount": 0 } ] }`**Example 2: To get the instance states for a patch group with more than five missing patches**The following `describe-instance-patch-states-for-patch-group`example retrieves details about the patch summary states for the specified patch group for instances with more than five missing patches.`aws ssm describe-instance-patch-states-for-patch-group \ --filters``Key=MissingCount,Type=GreaterThan,Values=5`\ --patch-group`"Production"`Output: `{ "InstancePatchStates": [ { "InstanceId": "i-02573cafcfEXAMPLE", "PatchGroup": "Production", "BaselineId": "pb-0c10e65780EXAMPLE", "SnapshotId": "a3f5ff34-9bc4-4d2c-a665-4d1c1EXAMPLE", "OwnerInformation": "", "InstalledCount": 46, "InstalledOtherCount": 4, "InstalledPendingRebootCount": 1, "InstalledRejectedCount": 1, "MissingCount": 7, "FailedCount": 0, "UnreportedNotApplicableCount": 232, "NotApplicableCount": 654, "OperationStartTime": "2021-08-04T11:03:50.590000-07:00", "OperationEndTime": "2021-08-04T11:04:21.555000-07:00", "Operation": "Scan", "RebootOption": "NoReboot", "CriticalNonCompliantCount": 0, "SecurityNonCompliantCount": 1, "OtherNonCompliantCount": 1 } ] }`**Example 3: To get the instance states for a patch group with fewer than ten instances that require a reboot**The following `describe-instance-patch-states-for-patch-group`example retrieves details about the patch summary states for the specified patch group for instances with fewer than ten instances requiring a reboot.`aws ssm describe-instance-patch-states-for-patch-group \ --filters``Key=InstalledPendingRebootCount,Type=LessThan,Values=10`\ --patch-group`"Production"`Output: `{ "InstancePatchStates": [ { "InstanceId": "i-02573cafcfEXAMPLE", "BaselineId": "pb-0c10e65780EXAMPLE", "SnapshotId": "a3f5ff34-9bc4-4d2c-a665-4d1c1EXAMPLE", "PatchGroup": "Production", "OwnerInformation": "", "InstalledCount": 32, "InstalledOtherCount": 1, "InstalledPendingRebootCount": 4, "InstalledRejectedCount": 0, "MissingCount": 2, "FailedCount": 0, "UnreportedNotApplicableCount": 846, "NotApplicableCount": 212, "OperationStartTime": "2021-08-046T11:03:50.590000-07:00", "OperationEndTime": "2021-08-06T11:04:21.555000-07:00", "Operation": "Scan", "RebootOption": "NoReboot", "CriticalNonCompliantCount": 0, "SecurityNonCompliantCount": 1, "OtherNonCompliantCount": 0 } ] }`For more information, see [Understanding patch compliance state values](https://docs.aws.amazon.com/systems-manager/latest/userguide/about-patch-compliance-states.html)in the*AWS Systems Manager User Guide*.- 
                    For API details, see [DescribeInstancePatchStatesForPatchGroup](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ssm/describe-instance-patch-states-for-patch-group.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `describe-instance-patch-states`.

- **AWS CLI**
- 
            
                    **To get the patch summary states for instances**This `describe-instance-patch-states`example gets the patch summary states for an instance.`aws ssm describe-instance-patch-states \ --instance-ids``"i-1234567890abcdef0"`Output: `{ "InstancePatchStates": [ { "InstanceId": "i-1234567890abcdef0", "PatchGroup": "my-patch-group", "BaselineId": "pb-0713accee01234567", "SnapshotId": "521c3536-930c-4aa9-950e-01234567abcd", "CriticalNonCompliantCount": 2, "SecurityNonCompliantCount": 2, "OtherNonCompliantCount": 1, "InstalledCount": 123, "InstalledOtherCount": 334, "InstalledPendingRebootCount": 0, "InstalledRejectedCount": 0, "MissingCount": 1, "FailedCount": 2, "UnreportedNotApplicableCount": 11, "NotApplicableCount": 2063, "OperationStartTime": "2021-05-03T11:00:56-07:00", "OperationEndTime": "2021-05-03T11:01:09-07:00", "Operation": "Scan", "LastNoRebootInstallOperationTime": "2020-06-14T12:17:41-07:00", "RebootOption": "RebootIfNeeded" } ] }`For more information, see [About Patch Compliance](https://docs.aws.amazon.com/systems-manager/latest/userguide/about-patch-compliance.html)in the*AWS Systems Manager User Guide*.- 
                    For API details, see [DescribeInstancePatchStates](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ssm/describe-instance-patch-states.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `describe-instance-patches`.

- **AWS CLI**
- 
            
                    **Example 1: To get the patch state details for an instance**The following `describe-instance-patches`example retrieves details about the patches for the specified instance.`aws ssm describe-instance-patches \ --instance-id``"i-1234567890abcdef0"`Output: `{ "Patches": [ { "Title": "2019-01 Security Update for Adobe Flash Player for Windows Server 2016 for x64-based Systems (KB4480979)", "KBId": "KB4480979", "Classification": "SecurityUpdates", "Severity": "Critical", "State": "Installed", "InstalledTime": "2019-01-09T00:00:00+00:00" }, { "Title": "", "KBId": "KB4481031", "Classification": "", "Severity": "", "State": "InstalledOther", "InstalledTime": "2019-02-08T00:00:00+00:00" }, ... ], "NextToken": "--token string truncated--" }`**Example 2: To get a list of patches in the Missing state for an instance**The following `describe-instance-patches`example retrieves information about patches that are in the Missing state for the specified instance.`aws ssm describe-instance-patches \ --instance-id``"i-1234567890abcdef0"`\ --filters`Key=State,Values=Missing`Output: `{ "Patches": [ { "Title": "Windows Malicious Software Removal Tool x64 - February 2019 (KB890830)", "KBId": "KB890830", "Classification": "UpdateRollups", "Severity": "Unspecified", "State": "Missing", "InstalledTime": "1970-01-01T00:00:00+00:00" }, ... ], "NextToken": "--token string truncated--" }`For more information, see [About Patch Compliance States](https://docs.aws.amazon.com/systems-manager/latest/userguide/about-patch-compliance-states.html)in the*AWS Systems Manager User Guide*.**Example 3: To get a list of patches installed since a specified InstalledTime for an instance**The following `describe-instance-patches`example retrieves information about patches installed since a specified time for the specified instance by combining the use of`--filters`and`--query`.`aws ssm describe-instance-patches \ --instance-id``"i-1234567890abcdef0"`\ --filters`Key=State,Values=Installed`\ --query`"Patches[?InstalledTime >= `2023-01-01T16:00:00`]"`Output: `{ "Patches": [ { "Title": "2023-03 Cumulative Update for Windows Server 2019 (1809) for x64-based Systems (KB5023702)", "KBId": "KB5023702", "Classification": "SecurityUpdates", "Severity": "Critical", "State": "Installed", "InstalledTime": "2023-03-16T11:00:00+00:00" }, ... ], "NextToken": "--token string truncated--" }`- 
                    For API details, see [DescribeInstancePatches](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ssm/describe-instance-patches.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `describe-inventory-deletions`.

- **AWS CLI**
- 
            
                    **To get inventory deletions**This example retrieves details for inventory deletion operations. Command: `aws ssm describe-inventory-deletions`Output: `{ "InventoryDeletions": [ { "DeletionId": "6961492a-8163-44ec-aa1e-01234567850", "TypeName": "Custom:RackInformation", "DeletionStartTime": 1550254911.0, "LastStatus": "InProgress", "LastStatusMessage": "The Delete is in progress", "DeletionSummary": { "TotalCount": 0, "RemainingCount": 0, "SummaryItems": [] }, "LastStatusUpdateTime": 1550254911.0 }, { "DeletionId": "d72ac9e8-1f60-4d40-b1c6-987654321c4d", "TypeName": "Custom:RackInfo", "DeletionStartTime": 1550254859.0, "LastStatus": "InProgress", "LastStatusMessage": "The Delete is in progress", "DeletionSummary": { "TotalCount": 1, "RemainingCount": 1, "SummaryItems": [ { "Version": "1.0", "Count": 1, "RemainingCount": 1 } ] }, "LastStatusUpdateTime": 1550254859.0 } ] }`**To get details of a specific inventory deletion**This example retrieves details for a specific inventory deletion operation. Command: `aws ssm describe-inventory-deletions --deletion-id``"d72ac9e8-1f60-4d40-b1c6-987654321c4d"`Output: `{ "InventoryDeletions": [ { "DeletionId": "d72ac9e8-1f60-4d40-b1c6-987654321c4d", "TypeName": "Custom:RackInfo", "DeletionStartTime": 1550254859.0, "LastStatus": "InProgress", "LastStatusMessage": "The Delete is in progress", "DeletionSummary": { "TotalCount": 1, "RemainingCount": 1, "SummaryItems": [ { "Version": "1.0", "Count": 1, "RemainingCount": 1 } ] }, "LastStatusUpdateTime": 1550254859.0 } ] }`- 
                    For API details, see [DescribeInventoryDeletions](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ssm/describe-inventory-deletions.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `describe-maintenance-window-execution-task-invocations`.

- **AWS CLI**
- 
            
                    **To get the specific task invocations performed for a maintenance window task execution**The following `describe-maintenance-window-execution-task-invocations`example lists the invocations for the specified task executed as part of the specified maintenance window execution.`aws ssm describe-maintenance-window-execution-task-invocations \ --window-execution-id``"518d5565-5969-4cca-8f0e-da3b2a638355"`\ --task-id`"ac0c6ae1-daa3-4a89-832e-d384503b6586"`Output: `{ "WindowExecutionTaskInvocationIdentities": [ { "Status": "SUCCESS", "Parameters": "{\"documentName\":\"AWS-RunShellScript\",\"instanceIds\":[\"i-0000293ffd8c57862\"],\"parameters\":{\"commands\":[\"df\"]},\"maxConcurrency\":\"1\",\"maxErrors\":\"1\"}", "InvocationId": "e274b6e1-fe56-4e32-bd2a-8073c6381d8b", "StartTime": 1487692834.723, "EndTime": 1487692834.871, "WindowExecutionId": "518d5565-5969-4cca-8f0e-da3b2a638355", "TaskExecutionId": "ac0c6ae1-daa3-4a89-832e-d384503b6586" } ] }`For more information, see [View Information About Tasks and Task Executions (AWS CLI)](https://docs.aws.amazon.com/systems-manager/latest/userguide/mw-cli-tutorial-task-info.html)in the*AWS Systems Manager User Guide*.- 
                    For API details, see [DescribeMaintenanceWindowExecutionTaskInvocations](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ssm/describe-maintenance-window-execution-task-invocations.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `describe-maintenance-window-execution-tasks`.

- **AWS CLI**
- 
            
                    **To list all tasks associated with a maintenance window execution**The following `ssm describe-maintenance-window-execution-tasks`example lists the tasks associated with the specified maintenance window execution.`aws ssm describe-maintenance-window-execution-tasks \ --window-execution-id``"518d5565-5969-4cca-8f0e-da3b2EXAMPLE"`Output: `{ "WindowExecutionTaskIdentities": [ { "Status": "SUCCESS", "TaskArn": "AWS-RunShellScript", "StartTime": 1487692834.684, "TaskType": "RUN_COMMAND", "EndTime": 1487692835.005, "WindowExecutionId": "518d5565-5969-4cca-8f0e-da3b2EXAMPLE", "TaskExecutionId": "ac0c6ae1-daa3-4a89-832e-d3845EXAMPLE" } ] }`For more information, see [View Information About Tasks and Task Executions (AWS CLI)](https://docs.aws.amazon.com/systems-manager/latest/userguide/mw-cli-tutorial-task-info.html)in the*AWS Systems Manager User Guide*.- 
                    For API details, see [DescribeMaintenanceWindowExecutionTasks](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ssm/describe-maintenance-window-execution-tasks.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `describe-maintenance-window-executions`.

- **AWS CLI**
- 
            
                    **Example 1: To list all executions for a maintenance window**The following `describe-maintenance-window-executions`example lists all of the executions for the specified maintenance window.`aws ssm describe-maintenance-window-executions \ --window-id``"mw-ab12cd34eEXAMPLE"`Output: `{ "WindowExecutions": [ { "WindowId": "mw-ab12cd34eEXAMPLE", "WindowExecutionId": "6027b513-64fe-4cf0-be7d-1191aEXAMPLE", "Status": "IN_PROGRESS", "StartTime": "2021-08-04T11:00:00.000000-07:00" }, { "WindowId": "mw-ab12cd34eEXAMPLE", "WindowExecutionId": "ff75b750-4834-4377-8f61-b3cadEXAMPLE", "Status": "SUCCESS", "StartTime": "2021-08-03T11:00:00.000000-07:00", "EndTime": "2021-08-03T11:37:21.450000-07:00" }, { "WindowId": "mw-ab12cd34eEXAMPLE", "WindowExecutionId": "9fac7dd9-ff21-42a5-96ad-bbc4bEXAMPLE", "Status": "FAILED", "StatusDetails": "One or more tasks in the orchestration failed.", "StartTime": "2021-08-02T11:00:00.000000-07:00", "EndTime": "2021-08-02T11:22:36.190000-07:00" } ] }`**Example 2: To list all executions for a maintenance window before a specified date**The following `describe-maintenance-window-executions`example lists all of the executions for the specified maintenance window before the specified date.`aws ssm describe-maintenance-window-executions \ --window-id``"mw-ab12cd34eEXAMPLE"`\ --filters`"Key=ExecutedBefore,Values=2021-08-03T00:00:00Z"`Output: `{ "WindowExecutions": [ { "WindowId": "mw-ab12cd34eEXAMPLE", "WindowExecutionId": "9fac7dd9-ff21-42a5-96ad-bbc4bEXAMPLE", "Status": "FAILED", "StatusDetails": "One or more tasks in the orchestration failed.", "StartTime": "2021-08-02T11:00:00.000000-07:00", "EndTime": "2021-08-02T11:22:36.190000-07:00" } ] }`**Example 3: To list all executions for a maintenance window after a specified date**The following `describe-maintenance-window-executions`example lists all of the executions for the specified maintenance window after the specified date.`aws ssm describe-maintenance-window-executions \ --window-id``"mw-ab12cd34eEXAMPLE"`\ --filters`"Key=ExecutedAfter,Values=2021-08-04T00:00:00Z"`Output: `{ "WindowExecutions": [ { "WindowId": "mw-ab12cd34eEXAMPLE", "WindowExecutionId": "6027b513-64fe-4cf0-be7d-1191aEXAMPLE", "Status": "IN_PROGRESS", "StartTime": "2021-08-04T11:00:00.000000-07:00" } ] }`For more information, see [View information about tasks and task executions (AWS CLI)](https://docs.aws.amazon.com/systems-manager/latest/userguide/mw-cli-tutorial-task-info.html)in the*AWS Systems Manager User Guide*.- 
                    For API details, see [DescribeMaintenanceWindowExecutions](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ssm/describe-maintenance-window-executions.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `describe-maintenance-window-schedule`.

- **AWS CLI**
- 
            
                    **Example 1: To list upcoming executions for a maintenance window**The following `describe-maintenance-window-schedule`example lists all upcoming executions for the specified maintenance window.`aws ssm describe-maintenance-window-schedule \ --window-id``mw-ab12cd34eEXAMPLE`Output: `{ "ScheduledWindowExecutions": [ { "WindowId": "mw-ab12cd34eEXAMPLE", "Name": "My-First-Maintenance-Window", "ExecutionTime": "2020-02-19T16:00Z" }, { "WindowId": "mw-ab12cd34eEXAMPLE", "Name": "My-First-Maintenance-Window", "ExecutionTime": "2020-02-26T16:00Z" }, ... ] }`**Example 2: To list all upcoming executions for a maintenance window before a specified date**The following `describe-maintenance-window-schedule`example lists all upcoming executions for the specified maintenance window that occur before the specified date.`aws ssm describe-maintenance-window-schedule \ --window-id``mw-0ecb1226dd7b2e9a6`\ --filters`"Key=ScheduledBefore,Values=2020-02-15T06:00:00Z"`**Example 3: To list all upcoming executions for a maintenance window after a specified date**The following `describe-maintenance-window-schedule`example lists all upcoming executions for the specified maintenance window that occur after the specified date.`aws ssm describe-maintenance-window-schedule \ --window-id``mw-0ecb1226dd7b2e9a6`\ --filters`"Key=ScheduledAfter,Values=2020-02-15T06:00:00Z"`For more information, see [View Information About Maintenance Windows (AWS CLI)](https://docs.aws.amazon.com/systems-manager/latest/userguide/maintenance-windows-cli-tutorials-describe.html)in the*AWS Systems Manager User Guide*.- 
                    For API details, see [DescribeMaintenanceWindowSchedule](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ssm/describe-maintenance-window-schedule.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `describe-maintenance-window-targets`.

- **AWS CLI**
- 
            
                    **Example 1: To list all targets for a Maintenance Window**The following `describe-maintenance-window-targets`example lists all of the targets for a maintenance window.`aws ssm describe-maintenance-window-targets \ --window-id``"mw-06cf17cbefEXAMPLE"`Output: `{ "Targets": [ { "ResourceType": "INSTANCE", "OwnerInformation": "Single instance", "WindowId": "mw-06cf17cbefEXAMPLE", "Targets": [ { "Values": [ "i-0000293ffdEXAMPLE" ], "Key": "InstanceIds" } ], "WindowTargetId": "350d44e6-28cc-44e2-951f-4b2c9EXAMPLE" }, { "ResourceType": "INSTANCE", "OwnerInformation": "Two instances in a list", "WindowId": "mw-06cf17cbefEXAMPLE", "Targets": [ { "Values": [ "i-0000293ffdEXAMPLE", "i-0cb2b964d3EXAMPLE" ], "Key": "InstanceIds" } ], "WindowTargetId": "e078a987-2866-47be-bedd-d9cf4EXAMPLE" } ] }`**Example 2: To list all targets for a maintenance window matching a specific owner information value**This `describe-maintenance-window-targets`example lists all of the targets for a maintenance window with a specific value.`aws ssm describe-maintenance-window-targets \ --window-id``"mw-0ecb1226ddEXAMPLE"`\ --filters`"Key=OwnerInformation,Values=CostCenter1"`Output: `{ "Targets": [ { "WindowId": "mw-0ecb1226ddEXAMPLE", "WindowTargetId": "da89dcc3-7f9c-481d-ba2b-edcb7d0057f9", "ResourceType": "INSTANCE", "Targets": [ { "Key": "tag:Environment", "Values": [ "Prod" ] } ], "OwnerInformation": "CostCenter1", "Name": "ProdTarget1" } ] }`For more information, see [View Information About Maintenance Windows (AWS CLI)](https://docs.aws.amazon.com/systems-manager/latest/userguide/maintenance-windows-cli-tutorials-describe.html)in the*AWS Systems Manager User Guide*.- 
                    For API details, see [DescribeMaintenanceWindowTargets](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ssm/describe-maintenance-window-targets.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `describe-maintenance-window-tasks`.

- **AWS CLI**
- 
            
                    **Example 1: To list all tasks for a maintenance window**The following `describe-maintenance-window-tasks`example lists all of the tasks for the specified maintenance window.`aws ssm describe-maintenance-window-tasks \ --window-id``"mw-06cf17cbefEXAMPLE"`Output: `{ "Tasks": [ { "WindowId": "mw-06cf17cbefEXAMPLE", "WindowTaskId": "018b31c3-2d77-4b9e-bd48-c91edEXAMPLE", "TaskArn": "AWS-RestartEC2Instance", "TaskParameters": {}, "Type": "AUTOMATION", "Description": "Restarting EC2 Instance for maintenance", "MaxConcurrency": "1", "MaxErrors": "1", "Name": "My-Automation-Example-Task", "Priority": 0, "ServiceRoleArn": "arn:aws:iam::111222333444:role/aws-service-role/ssm.amazonaws.com/AWSServiceRoleForAmazonSSM", "Targets": [ { "Key": "WindowTargetIds", "Values": [ "da89dcc3-7f9c-481d-ba2b-edcb7EXAMPLE" ] } ] }, { "WindowId": "mw-06cf17cbefEXAMPLE", "WindowTaskId": "1943dee0-0a17-4978-9bf4-3cc2fEXAMPLE", "TaskArn": "AWS-DisableS3BucketPublicReadWrite", "TaskParameters": {}, "Type": "AUTOMATION", "Description": "Automation task to disable read/write access on public S3 buckets", "MaxConcurrency": "10", "MaxErrors": "5", "Name": "My-Disable-S3-Public-Read-Write-Access-Automation-Task", "Priority": 0, "ServiceRoleArn": "arn:aws:iam::111222333444:role/aws-service-role/ssm.amazonaws.com/AWSServiceRoleForAmazonSSM", "Targets": [ { "Key": "WindowTargetIds", "Values": [ "da89dcc3-7f9c-481d-ba2b-edcb7EXAMPLE" ] } ] } ] }`**Example 2: To list all tasks for a maintenance window that invokes the AWS-RunPowerShellScript command document**The following `describe-maintenance-window-tasks`example lists all of the tasks for the specified maintenance window that invokes the`AWS-RunPowerShellScript`command document.`aws ssm describe-maintenance-window-tasks \ --window-id``"mw-ab12cd34eEXAMPLE"`\ --filters`"Key=TaskArn,Values=AWS-RunPowerShellScript"`Output: `{ "Tasks": [ { "WindowId": "mw-ab12cd34eEXAMPLE", "WindowTaskId": "0d36e6b4-3a4f-411e-adcb-3558eEXAMPLE", "TaskArn": "AWS-RunPowerShellScript", "Type": "RUN_COMMAND", "Targets": [ { "Key": "WindowTargetIds", "Values": [ "da89dcc3-7f9c-481d-ba2b-edcb7EXAMPLE" ] } ], "TaskParameters": {}, "Priority": 1, "ServiceRoleArn": "arn:aws:iam::111222333444:role/aws-service-role/ssm.amazonaws.com/AWSServiceRoleForAmazonSSM", "MaxConcurrency": "1", "MaxErrors": "1", "Name": "MyTask" } ] }`**Example 3: To list all tasks for a maintenance window that have a Priority of 3**The following `describe-maintenance-window-tasks`example lists all of the tasks for the specified maintenance window that have a`Priority`of`3`.`aws ssm describe-maintenance-window-tasks \ --window-id``"mw-ab12cd34eEXAMPLE"`\ --filters`"Key=Priority,Values=3"`Output: `{ "Tasks": [ { "WindowId": "mw-ab12cd34eEXAMPLE", "WindowTaskId": "0d36e6b4-3a4f-411e-adcb-3558eEXAMPLE", "TaskArn": "AWS-RunPowerShellScript", "Type": "RUN_COMMAND", "Targets": [ { "Key": "WindowTargetIds", "Values": [ "da89dcc3-7f9c-481d-ba2b-edcb7EXAMPLE" ] } ], "TaskParameters": {}, "Priority": 3, "ServiceRoleArn": "arn:aws:iam::111222333444:role/aws-service-role/ssm.amazonaws.com/AWSServiceRoleForAmazonSSM", "MaxConcurrency": "1", "MaxErrors": "1", "Name": "MyRunCommandTask" }, { "WindowId": "mw-ab12cd34eEXAMPLE", "WindowTaskId": "ee45feff-ad65-4a6c-b478-5cab8EXAMPLE", "TaskArn": "AWS-RestartEC2Instance", "Type": "AUTOMATION", "Targets": [ { "Key": "WindowTargetIds", "Values": [ "da89dcc3-7f9c-481d-ba2b-edcb7EXAMPLE" ] } ], "TaskParameters": {}, "Priority": 3, "ServiceRoleArn": "arn:aws:iam::111222333444:role/aws-service-role/ssm.amazonaws.com/AWSServiceRoleForAmazonSSM", "MaxConcurrency": "10", "MaxErrors": "5", "Name": "My-Automation-Task", "Description": "A description for my Automation task" } ] }`**Example 4: To list all tasks for a maintenance window that have a Priority of 1 and use Run Command**This `describe-maintenance-window-tasks`example lists all of the tasks for the specified maintenance window that have a`Priority`of`1`and use`Run Command`.`aws ssm describe-maintenance-window-tasks \ --window-id``"mw-ab12cd34eEXAMPLE"`\ --filters`"Key=Priority,Values=1"``"Key=TaskType,Values=RUN_COMMAND"`Output: `{ "Tasks": [ { "WindowId": "mw-ab12cd34eEXAMPLE", "WindowTaskId": "0d36e6b4-3a4f-411e-adcb-3558eEXAMPLE", "TaskArn": "AWS-RunPowerShellScript", "Type": "RUN_COMMAND", "Targets": [ { "Key": "WindowTargetIds", "Values": [ "da89dcc3-7f9c-481d-ba2b-edcb7EXAMPLE" ] } ], "TaskParameters": {}, "Priority": 1, "ServiceRoleArn": "arn:aws:iam::111222333444:role/aws-service-role/ssm.amazonaws.com/AWSServiceRoleForAmazonSSM", "MaxConcurrency": "1", "MaxErrors": "1", "Name": "MyRunCommandTask" } ] }`For more information, see [View information about maintenance windows (AWS CLI)](https://docs.aws.amazon.com/systems-manager/latest/userguide/maintenance-windows-cli-tutorials-describe.html)in the*AWS Systems Manager User Guide*.- 
                    For API details, see [DescribeMaintenanceWindowTasks](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ssm/describe-maintenance-window-tasks.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `describe-maintenance-windows-for-target`.

- **AWS CLI**
- 
            
                    **To list all maintenance windows associated with a specific instance**The following `describe-maintenance-windows-for-target`example lists the maintenance windows that have targets or tasks associated with the specified instance.`aws ssm describe-maintenance-windows-for-target \ --targets``Key=InstanceIds,Values=i-1234567890EXAMPLE`\ --resource-type`INSTANCE`Output: `{ "WindowIdentities": [ { "WindowId": "mw-0c5ed765acEXAMPLE", "Name": "My-First-Maintenance-Window" } ] }`For more information, see [View Information About Maintenance Windows (AWS CLI)](https://docs.aws.amazon.com/systems-manager/latest/userguide/maintenance-windows-cli-tutorials-describe.html)in the*AWS Systems Manager User Guide*.- 
                    For API details, see [DescribeMaintenanceWindowsForTarget](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ssm/describe-maintenance-windows-for-target.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `describe-maintenance-windows`.

- **AWS CLI**
- 
            
                    **Example 1: To list all maintenance windows**The following `describe-maintenance-windows`example lists all maintenance windows in your AWS account in the current Region.`aws ssm describe-maintenance-windows`Output: `{ "WindowIdentities": [ { "WindowId": "mw-0ecb1226ddEXAMPLE", "Name": "MyMaintenanceWindow-1", "Enabled": true, "Duration": 2, "Cutoff": 1, "Schedule": "rate(180 minutes)", "NextExecutionTime": "2020-02-12T23:19:20.596Z" }, { "WindowId": "mw-03eb9db428EXAMPLE", "Name": "MyMaintenanceWindow-2", "Enabled": true, "Duration": 3, "Cutoff": 1, "Schedule": "rate(7 days)", "NextExecutionTime": "2020-02-17T23:22:00.956Z" }, ] }`**Example 2: To list all enabled maintenance windows**The following `describe-maintenance-windows`example lists all enabled maintenance windows.`aws ssm describe-maintenance-windows \ --filters``"Key=Enabled,Values=true"`**Example 3: To list maintenance windows matching a specific name**This `describe-maintenance-windows`example lists all maintenance windows with the specified name.`aws ssm describe-maintenance-windows \ --filters``"Key=Name,Values=MyMaintenanceWindow"`For more information, see [View Information About Maintenance Windows (AWS CLI)](https://docs.aws.amazon.com/systems-manager/latest/userguide/maintenance-windows-cli-tutorials-describe.html)in the*AWS Systems Manager User Guide*.- 
                    For API details, see [DescribeMaintenanceWindows](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ssm/describe-maintenance-windows.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `describe-ops-items`.

- **AWS CLI**
- 
            
                    **To list a set of OpsItems**The following `describe-ops-items`example displays a list of all open OpsItems in your AWS account.`aws ssm describe-ops-items \ --ops-item-filters``"Key=Status,Values=Open,Operator=Equal"`Output: `{ "OpsItemSummaries": [ { "CreatedBy": "arn:aws:sts::111222333444:assumed-role/OpsItem-CWE-Role/fbf77cbe264a33509569f23e4EXAMPLE", "CreatedTime": "2020-03-14T17:02:46.375000-07:00", "LastModifiedBy": "arn:aws:sts::111222333444:assumed-role/OpsItem-CWE-Role/fbf77cbe264a33509569f23e4EXAMPLE", "LastModifiedTime": "2020-03-14T17:02:46.375000-07:00", "Source": "SSM", "Status": "Open", "OpsItemId": "oi-7cfc5EXAMPLE", "Title": "SSM Maintenance Window execution failed", "OperationalData": { "/aws/dedup": { "Value": "{\"dedupString\":\"SSMOpsItems-SSM-maintenance-window-execution-failed\"}", "Type": "SearchableString" }, "/aws/resources": { "Value": "[{\"arn\":\"arn:aws:ssm:us-east-2:111222333444:maintenancewindow/mw-034093d322EXAMPLE\"}]", "Type": "SearchableString" } }, "Category": "Availability", "Severity": "3" }, { "CreatedBy": "arn:aws:sts::1112223233444:assumed-role/OpsItem-CWE-Role/fbf77cbe264a33509569f23e4EXAMPLE", "CreatedTime": "2020-02-26T11:43:15.426000-08:00", "LastModifiedBy": "arn:aws:sts::111222333444:assumed-role/OpsItem-CWE-Role/fbf77cbe264a33509569f23e4EXAMPLE", "LastModifiedTime": "2020-02-26T11:43:15.426000-08:00", "Source": "EC2", "Status": "Open", "OpsItemId": "oi-6f966EXAMPLE", "Title": "EC2 instance stopped", "OperationalData": { "/aws/automations": { "Value": "[ { \"automationType\": \"AWS:SSM:Automation\", \"automationId\": \"AWS-RestartEC2Instance\" } ]", "Type": "SearchableString" }, "/aws/dedup": { "Value": "{\"dedupString\":\"SSMOpsItems-EC2-instance-stopped\"}", "Type": "SearchableString" }, "/aws/resources": { "Value": "[{\"arn\":\"arn:aws:ec2:us-east-2:111222333444:instance/i-0beccfbc02EXAMPLE\"}]", "Type": "SearchableString" } }, "Category": "Availability", "Severity": "3" } ] }`For more information, see [Working with OpsItems](https://docs.aws.amazon.com/systems-manager/latest/userguide/OpsCenter-working-with-OpsItems.html)in the*AWS Systems Manager User Guide*.- 
                    For API details, see [DescribeOpsItems](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ssm/describe-ops-items.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `describe-parameters`.

- **AWS CLI**
- 
            
                    **Example 1: To list all parameters**The following `describe-parameters`example lists all parameters in the current AWS account and Region.`aws ssm describe-parameters`Output: `{ "Parameters": [ { "Name": "MySecureStringParameter", "Type": "SecureString", "KeyId": "alias/aws/ssm", "LastModifiedDate": 1582155479.205, "LastModifiedUser": "arn:aws:sts::111222333444:assumed-role/Admin/Richard-Roe-Managed", "Description": "This is a SecureString parameter", "Version": 2, "Tier": "Advanced", "Policies": [ { "PolicyText": "{\"Type\":\"Expiration\",\"Version\":\"1.0\",\"Attributes\":{\"Timestamp\":\"2020-07-07T22:30:00Z\"}}", "PolicyType": "Expiration", "PolicyStatus": "Pending" }, { "PolicyText": "{\"Type\":\"ExpirationNotification\",\"Version\":\"1.0\",\"Attributes\":{\"Before\":\"12\",\"Unit\":\"Hours\"}}", "PolicyType": "ExpirationNotification", "PolicyStatus": "Pending" } ] }, { "Name": "MyStringListParameter", "Type": "StringList", "LastModifiedDate": 1582154764.222, "LastModifiedUser": "arn:aws:iam::111222333444:user/Mary-Major", "Description": "This is a StringList parameter", "Version": 1, "Tier": "Standard", "Policies": [] }, { "Name": "MyStringParameter", "Type": "String", "LastModifiedDate": 1582154711.976, "LastModifiedUser": "arn:aws:iam::111222333444:user/Alejandro-Rosalez", "Description": "This is a String parameter", "Version": 1, "Tier": "Standard", "Policies": [] }, { "Name": "latestAmi", "Type": "String", "LastModifiedDate": 1580862415.521, "LastModifiedUser": "arn:aws:sts::111222333444:assumed-role/lambda-ssm-role/Automation-UpdateSSM-Param", "Version": 3, "Tier": "Standard", "Policies": [] } ] }`**Example 2: To list all parameters matching specific metadata**This `describe-parameters`example lists all parameters matching a filter.aws ssm describe-parameters --filters "Key=Type,Values=StringList" Output: `{ "Parameters": [ { "Name": "MyStringListParameter", "Type": "StringList", "LastModifiedDate": 1582154764.222, "LastModifiedUser": "arn:aws:iam::111222333444:user/Mary-Major", "Description": "This is a StringList parameter", "Version": 1, "Tier": "Standard", "Policies": [] } ] }`For more information, see [Searching for Systems Manager Parameters](https://docs.aws.amazon.com/systems-manager/latest/userguide/parameter-search.html)in the*AWS Systems Manager User Guide*.- 
                    For API details, see [DescribeParameters](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ssm/describe-parameters.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `describe-patch-baselines`.

- **AWS CLI**
- 
            
                    **Example 1: To list all patch baselines**The following `describe-patch-baselines`example retrieves details for all patch baselines in your account in the current Region.`aws ssm describe-patch-baselines`Output: `{ "BaselineIdentities": [ { "BaselineName": "AWS-SuseDefaultPatchBaseline", "DefaultBaseline": true, "BaselineDescription": "Default Patch Baseline for Suse Provided by AWS.", "BaselineId": "arn:aws:ssm:us-east-2:733109147000:patchbaseline/pb-0123fdb36e334a3b2", "OperatingSystem": "SUSE" }, { "BaselineName": "AWS-DefaultPatchBaseline", "DefaultBaseline": false, "BaselineDescription": "Default Patch Baseline Provided by AWS.", "BaselineId": "arn:aws:ssm:us-east-2:733109147000:patchbaseline/pb-020d361a05defe4ed", "OperatingSystem": "WINDOWS" }, ... { "BaselineName": "MyWindowsPatchBaseline", "DefaultBaseline": true, "BaselineDescription": "My patch baseline for EC2 instances for Windows Server", "BaselineId": "pb-0ad00e0dd7EXAMPLE", "OperatingSystem": "WINDOWS" } ] }`**Example 2: To list all patch baselines provided by AWS**The following `describe-patch-baselines`example lists all patch baselines provided by AWS.`aws ssm describe-patch-baselines \ --filters``"Key=OWNER,Values=[AWS]"`**Example 3: To list all patch baselines that you own**The following `describe-patch-baselines`example lists all custom patch baselines created in your account in the current Region.`aws ssm describe-patch-baselines \ --filters``"Key=OWNER,Values=[Self]"`For more information, see [About Predefined and Custom Patch Baselines](https://docs.aws.amazon.com/systems-manager/latest/userguide/sysman-patch-baselines.html)in the*AWS Systems Manager User Guide*.- 
                    For API details, see [DescribePatchBaselines](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ssm/describe-patch-baselines.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `describe-patch-group-state`.

- **AWS CLI**
- 
            
                    **To get the state of a patch group**The following `describe-patch-group-state`example retrieves the high-level patch compliance summary for a patch group.`aws ssm describe-patch-group-state \ --patch-group``"Production"`Output: `{ "Instances": 21, "InstancesWithCriticalNonCompliantPatches": 1, "InstancesWithFailedPatches": 2, "InstancesWithInstalledOtherPatches": 3, "InstancesWithInstalledPatches": 21, "InstancesWithInstalledPendingRebootPatches": 2, "InstancesWithInstalledRejectedPatches": 1, "InstancesWithMissingPatches": 3, "InstancesWithNotApplicablePatches": 4, "InstancesWithOtherNonCompliantPatches": 1, "InstancesWithSecurityNonCompliantPatches": 1, "InstancesWithUnreportedNotApplicablePatches": 2 }`For more information, see About patch groups <https://docs.aws.amazon.com/systems-manager/latest/userguide/sysman-patch-patchgroups.html>__ and [Understanding patch compliance state values](https://docs.aws.amazon.com/systems-manager/latest/userguide/about-patch-compliance-states.html)in the*AWS Systems Manager User Guide*.- 
                    For API details, see [DescribePatchGroupState](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ssm/describe-patch-group-state.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `describe-patch-groups`.

- **AWS CLI**
- 
            
                    **To display patch group registrations**The following `describe-patch-groups`example lists the patch group registrations.`aws ssm describe-patch-groups`Output: `{ "Mappings": [ { "PatchGroup": "Production", "BaselineIdentity": { "BaselineId": "pb-0123456789abcdef0", "BaselineName": "ProdPatching", "OperatingSystem": "WINDOWS", "BaselineDescription": "Patches for Production", "DefaultBaseline": false } }, { "PatchGroup": "Development", "BaselineIdentity": { "BaselineId": "pb-0713accee01234567", "BaselineName": "DevPatching", "OperatingSystem": "WINDOWS", "BaselineDescription": "Patches for Development", "DefaultBaseline": true } }, ... ] }`For more information, see Create a Patch Group <https://docs.aws.amazon.com/systems-manager/latest/userguide/sysman-patch-group-tagging.html>__ and [Add a Patch Group to a Patch Baseline](https://docs.aws.amazon.com/systems-manager/latest/userguide/sysman-patch-group-patchbaseline.html)in the*AWS Systems Manager User Guide*.- 
                    For API details, see [DescribePatchGroups](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ssm/describe-patch-groups.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `describe-patch-properties`.

- **AWS CLI**
- 
            
                    **To list the Amazon Linux patch availability**The following `describe-patch-properties`example displays a list of the Amazon Linux products for which patches are available in your AWS account.`aws ssm describe-patch-properties \ --operating-system``AMAZON_LINUX`\ --property`PRODUCT`Output: `{ "Properties": [ { "Name": "AmazonLinux2012.03" }, { "Name": "AmazonLinux2012.09" }, { "Name": "AmazonLinux2013.03" }, { "Name": "AmazonLinux2013.09" }, { "Name": "AmazonLinux2014.03" }, { "Name": "AmazonLinux2014.09" }, { "Name": "AmazonLinux2015.03" }, { "Name": "AmazonLinux2015.09" }, { "Name": "AmazonLinux2016.03" }, { "Name": "AmazonLinux2016.09" }, { "Name": "AmazonLinux2017.03" }, { "Name": "AmazonLinux2017.09" }, { "Name": "AmazonLinux2018.03" } ] }`For more information, see [About Patch Baselines](https://docs.aws.amazon.com/systems-manager/latest/userguide/about-patch-baselines.html)in the*AWS Systems Manager User Guide*.- 
                    For API details, see [DescribePatchProperties](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ssm/describe-patch-properties.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `describe-sessions`.

- **AWS CLI**
- 
            
                    **Example 1: To list all active Session Manager sessions**This `describe-sessions`example retrieves a list of the active sessions created most recently (both connected and disconnected sessions) over the past 30 days that were started by the specified user. This command returns only results for connections to targets initiated using Session Manager. It does not list connections made through other means, such as Remote Desktop Connections or SSH.`aws ssm describe-sessions \ --state``"Active"`\ --filters`"key=Owner,value=arn:aws:sts::123456789012:assumed-role/Administrator/Shirley-Rodriguez"`Output: `{ "Sessions": [ { "SessionId": "John-07a16060613c408b5", "Target": "i-1234567890abcdef0", "Status": "Connected", "StartDate": 1550676938.352, "Owner": "arn:aws:sts::123456789012:assumed-role/Administrator/Shirley-Rodriguez", "OutputUrl": {} }, { "SessionId": "John-01edf534b8b56e8eb", "Target": "i-9876543210abcdef0", "Status": "Connected", "StartDate": 1550676842.194, "Owner": "arn:aws:sts::123456789012:assumed-role/Administrator/Shirley-Rodriguez", "OutputUrl": {} } ] }`**Example 2: To list all terminated Session Manager sessions**This `describe-sessions`example retrieves a list of the most recently terminated sessions from the past 30 days for all users.`aws ssm describe-sessions \ --state``"History"`Output: `{ "Sessions": [ { "SessionId": "Mary-Major-0022b1eb2b0d9e3bd", "Target": "i-1234567890abcdef0", "Status": "Terminated", "StartDate": 1550520701.256, "EndDate": 1550521931.563, "Owner": "arn:aws:sts::123456789012:assumed-role/Administrator/Mary-Major" }, { "SessionId": "Jane-Roe-0db53f487931ed9d4", "Target": "i-9876543210abcdef0", "Status": "Terminated", "StartDate": 1550161369.149, "EndDate": 1550162580.329, "Owner": "arn:aws:sts::123456789012:assumed-role/Administrator/Jane-Roe" }, ... ], "NextToken": "--token string truncated--" }`For more information, see [View Session History](https://docs.aws.amazon.com/systems-manager/latest/userguide/session-manager-working-with-view-history.html)in the*AWS Systems Manager User Guide*.- 
                    For API details, see [DescribeSessions](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ssm/describe-sessions.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `disassociate-ops-item-related-item`.

- **AWS CLI**
- 
            
                    **To delete a related item association**The following `disassociate-ops-item-related-item`example deletes the association between the OpsItem and a related item.`aws ssm disassociate-ops-item-related-item \ --ops-item-id``"oi-f99f2EXAMPLE"`\ --association-id`"e2036148-cccb-490e-ac2a-390e5EXAMPLE"`This command produces no output. For more information, see [Working with Incident Manager incidents in OpsCenter](https://docs.aws.amazon.com/systems-manager/latest/userguide/OpsCenter-create-OpsItems-for-Incident-Manager.html)in the*AWS Systems Manager User Guide*.- 
                    For API details, see [DisassociateOpsItemRelatedItem](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ssm/disassociate-ops-item-related-item.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `get-automation-execution`.

- **AWS CLI**
- 
            
                    **To display details about an automation execution**The following `get-automation-execution`example displays detailed information about an Automation execution.`aws ssm get-automation-execution \ --automation-execution-id``73c8eef8-f4ee-4a05-820c-e354fEXAMPLE`Output: `{ "AutomationExecution": { "AutomationExecutionId": "73c8eef8-f4ee-4a05-820c-e354fEXAMPLE", "DocumentName": "AWS-StartEC2Instance", "DocumentVersion": "1", "ExecutionStartTime": 1583737233.748, "ExecutionEndTime": 1583737234.719, "AutomationExecutionStatus": "Success", "StepExecutions": [ { "StepName": "startInstances", "Action": "aws:changeInstanceState", "ExecutionStartTime": 1583737234.134, "ExecutionEndTime": 1583737234.672, "StepStatus": "Success", "Inputs": { "DesiredState": "\"running\"", "InstanceIds": "[\"i-0cb99161f6EXAMPLE\"]" }, "Outputs": { "InstanceStates": [ "running" ] }, "StepExecutionId": "95e70479-cf20-4d80-8018-7e4e2EXAMPLE", "OverriddenParameters": {} } ], "StepExecutionsTruncated": false, "Parameters": { "AutomationAssumeRole": [ "" ], "InstanceId": [ "i-0cb99161f6EXAMPLE" ] }, "Outputs": {}, "Mode": "Auto", "ExecutedBy": "arn:aws:sts::29884EXAMPLE:assumed-role/mw_service_role/OrchestrationService", "Targets": [], "ResolvedTargets": { "ParameterValues": [], "Truncated": false } } }`For more information, see [Walkthrough: Patch a Linux AMI (AWS CLI)](https://docs.aws.amazon.com/systems-manager/latest/userguide/automation-walk-patch-linux-ami-cli.html)in the*AWS Systems Manager User Guide*.- 
                    For API details, see [GetAutomationExecution](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ssm/get-automation-execution.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `get-calendar-state`.

- **AWS CLI**
- 
            
                    **Example 1: To get the current state of a change calendar**This `get-calendar-state`example returns the state of a calendar at the current time. Because the example doesn't specify a time, the current state of the calendar is reported.`aws ssm get-calendar-state \ --calendar-names``"MyCalendar"`Output: `{ "State": "OPEN", "AtTime": "2020-02-19T22:28:51Z", "NextTransitionTime": "2020-02-24T21:15:19Z" }`**Example 2: To get the state of a change calendar at a specified time**This `get-calendar-state`example returns the state of a calendar at the specified time.`aws ssm get-calendar-state \ --calendar-names``"MyCalendar"`\ --at-time`"2020-07-19T21:15:19Z"`Output: `{ "State": "CLOSED", "AtTime": "2020-07-19T21:15:19Z" }`For more information, see [Get the State of the Change Calendar](https://docs.aws.amazon.com/systems-manager/latest/userguide/change-calendar-getstate.html)in the*AWS Systems Manager User Guide*.- 
                    For API details, see [GetCalendarState](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ssm/get-calendar-state.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `get-command-invocation`.

- **AWS CLI**
- 
            
                    **To display the details of a command invocation**The following `get-command-invocation`example lists all the invocations of the specified command on the specified instance.`aws ssm get-command-invocation \ --command-id``"ef7fdfd8-9b57-4151-a15c-db9a12345678"`\ --instance-id`"i-1234567890abcdef0"`Output: `{ "CommandId": "ef7fdfd8-9b57-4151-a15c-db9a12345678", "InstanceId": "i-1234567890abcdef0", "Comment": "b48291dd-ba76-43e0-b9df-13e11ddaac26:6960febb-2907-4b59-8e1a-d6ce8EXAMPLE", "DocumentName": "AWS-UpdateSSMAgent", "DocumentVersion": "", "PluginName": "aws:updateSsmAgent", "ResponseCode": 0, "ExecutionStartDateTime": "2020-02-19T18:18:03.419Z", "ExecutionElapsedTime": "PT0.091S", "ExecutionEndDateTime": "2020-02-19T18:18:03.419Z", "Status": "Success", "StatusDetails": "Success", "StandardOutputContent": "Updating amazon-ssm-agent from 2.3.842.0 to latest\nSuccessfully downloaded https://s3.us-east-2.amazonaws.com/amazon-ssm-us-east-2/ssm-agent-manifest.json\namazon-ssm-agent 2.3.842.0 has already been installed, update skipped\n", "StandardOutputUrl": "", "StandardErrorContent": "", "StandardErrorUrl": "", "CloudWatchOutputConfig": { "CloudWatchLogGroupName": "", "CloudWatchOutputEnabled": false } }`For more information, see [Understanding Command Statuses](https://docs.aws.amazon.com/systems-manager/latest/userguide/monitor-commands.html)in the*AWS Systems Manager User Guide*.- 
                    For API details, see [GetCommandInvocation](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ssm/get-command-invocation.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `get-connection-status`.

- **AWS CLI**
- 
            
                    **To display the connection status of a managed instance**This `get-connection-status`example returns the connection status of the specified managed instance.`aws ssm get-connection-status \ --target``i-1234567890abcdef0`Output: `{ "Target": "i-1234567890abcdef0", "Status": "connected" }`- 
                    For API details, see [GetConnectionStatus](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ssm/get-connection-status.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `get-default-patch-baseline`.

- **AWS CLI**
- 
            
                    **Example 1: To display the default Windows patch baseline**The following `get-default-patch-baseline`example retrieves details for the default patch baseline for Windows Server.`aws ssm get-default-patch-baseline`Output: `{ "BaselineId": "pb-0713accee01612345", "OperatingSystem": "WINDOWS" }`**Example 2: To display the default patch baseline for Amazon Linux**The following `get-default-patch-baseline`example retrieves details for the default patch baseline for Amazon Linux.`aws ssm get-default-patch-baseline \ --operating-system``AMAZON_LINUX`Output: `{ "BaselineId": "pb-047c6eb9c8fc12345", "OperatingSystem": "AMAZON_LINUX" }`For more information, see About Predefined and Custom Patch Baselines <https://docs.aws.amazon.com/systems-manager/latest/userguide/sysman-patch-baselines.html>__ and [Set an Existing Patch Baseline as the Default](https://docs.aws.amazon.com/systems-manager/latest/userguide/set-default-patch-baseline.html)in the*AWS Systems Manager User Guide*.- 
                    For API details, see [GetDefaultPatchBaseline](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ssm/get-default-patch-baseline.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `get-deployable-patch-snapshot-for-instance`.

- **AWS CLI**
- 
            
                    **To retrieve the current snapshot for the patch baseline an instance uses**The following `get-deployable-patch-snapshot-for-instance`example retrieves details for the current snapshot for the specified patch baseline used by an instance. This command must be run from the instance using the instance credentials. To ensure it uses the instance credentials, run`aws configure`and specify only the Region of your instance. Leave the`Access Key`and`Secret Key`fields empty.Tip: Use `uuidgen`to generate a`snapshot-id`.`aws ssm get-deployable-patch-snapshot-for-instance \ --instance-id``"i-1234567890abcdef0"`\ --snapshot-id`"521c3536-930c-4aa9-950e-01234567abcd"`Output: `{ "InstanceId": "i-1234567890abcdef0", "SnapshotId": "521c3536-930c-4aa9-950e-01234567abcd", "Product": "AmazonLinux2018.03", "SnapshotDownloadUrl": "https://patch-baseline-snapshot-us-east-1.s3.amazonaws.com/ed85194ef27214f5984f28b4d664d14f7313568fea7d4b6ac6c10ad1f729d7e7-773304212436/AMAZON_LINUX-521c3536-930c-4aa9-950e-01234567abcd?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Date=20190215T164031Z&X-Amz-SignedHeaders=host&X-Amz-Expires=86400&X-Amz-Credential=AKIAJ5C56P35AEBRX2QQ%2F20190215%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Signature=efaaaf6e3878e77f48a6697e015efdbda9c426b09c5822055075c062f6ad2149" }`For more information, see [Parameter name: Snapshot ID](https://docs.aws.amazon.com/systems-manager/latest/userguide/patch-manager-about-aws-runpatchbaseline.html#patch-manager-about-aws-runpatchbaseline-parameters-snapshot-id)in the*AWS Systems Manager User Guide*.- 
                    For API details, see [GetDeployablePatchSnapshotForInstance](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ssm/get-deployable-patch-snapshot-for-instance.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `get-document`.

- **AWS CLI**
- 
            
                    **To get document content**The following `get-document`example displays the content of a Systems Manager document.`aws ssm get-document \ --name``"AWS-RunShellScript"`Output: `{ "Name": "AWS-RunShellScript", "DocumentVersion": "1", "Status": "Active", "Content": "{\n \"schemaVersion\":\"1.2\",\n \"description\":\"Run a shell script or specify the commands to run.\",\n \"parameters\":{\n \"commands\":{\n \"type\":\"StringList\",\n \"description\":\"(Required) Specify a shell script or a command to run.\",\n \"minItems\":1,\n \"displayType\":\"textarea\"\n },\n \"workingDirectory\":{\n \"type\":\"String\",\n \"default\":\"\",\n \"description\":\"(Optional) The path to the working directory on your instance.\",\n \"maxChars\":4096\n },\n \"executionTimeout\":{\n \"type\":\"String\",\n \"default\":\"3600\",\n \"description\":\"(Optional) The time in seconds for a command to complete before it is considered to have failed. Default is 3600 (1 hour). Maximum is 172800 (48 hours).\",\n \"allowedPattern\":\"([1-9][0-9]{0,4})|(1[0-6][0-9]{4})|(17[0-1][0-9]{3})|(172[0-7][0-9]{2})|(172800)\"\n }\n },\n \"runtimeConfig\":{\n \"aws:runShellScript\":{\n \"properties\":[\n {\n \"id\":\"0.aws:runShellScript\",\n \"runCommand\":\"{{ commands }}\",\n \"workingDirectory\":\"{{ workingDirectory }}\",\n \"timeoutSeconds\":\"{{ executionTimeout }}\"\n }\n ]\n }\n }\n}\n", "DocumentType": "Command", "DocumentFormat": "JSON" }`For more information, see [AWS Systems Manager Documents](https://docs.aws.amazon.com/systems-manager/latest/userguide/sysman-ssm-docs.html)in the*AWS Systems Manager User Guide*.- 
                    For API details, see [GetDocument](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ssm/get-document.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `get-inventory-schema`.

- **AWS CLI**
- 
            
                    **To view your inventory schema**This example returns a list of inventory type names for the account. Command: `aws ssm get-inventory-schema`Output: `{ "Schemas": [ { "TypeName": "AWS:AWSComponent", "Version": "1.0", "Attributes": [ { "Name": "Name", "DataType": "STRING" }, { "Name": "ApplicationType", "DataType": "STRING" }, { "Name": "Publisher", "DataType": "STRING" }, { "Name": "Version", "DataType": "STRING" }, { "Name": "InstalledTime", "DataType": "STRING" }, { "Name": "Architecture", "DataType": "STRING" }, { "Name": "URL", "DataType": "STRING" } ] }, ... ], "NextToken": "--token string truncated--" }`**To view the inventory schema for a specific inventory type**This example return the inventory schema for a the AWS:AWSComponent inventory type. Command: `aws ssm get-inventory-schema --type-name``"AWS:AWSComponent"`- 
                    For API details, see [GetInventorySchema](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ssm/get-inventory-schema.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `get-inventory`.

- **AWS CLI**
- 
            
                    **To view your inventory**This example gets the custom metadata for your inventory. Command: `aws ssm get-inventory`Output: `{ "Entities": [ { "Data": { "AWS:InstanceInformation": { "Content": [ { "ComputerName": "ip-172-31-44-222.us-west-2.compute.internal", "InstanceId": "i-0cb2b964d3e14fd9f", "IpAddress": "172.31.44.222", "AgentType": "amazon-ssm-agent", "ResourceType": "EC2Instance", "AgentVersion": "2.0.672.0", "PlatformVersion": "2016.09", "PlatformName": "Amazon Linux AMI", "PlatformType": "Linux" } ], "TypeName": "AWS:InstanceInformation", "SchemaVersion": "1.0", "CaptureTime": "2017-02-20T18:03:58Z" } }, "Id": "i-0cb2b964d3e14fd9f" } ] }`- 
                    For API details, see [GetInventory](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ssm/get-inventory.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `get-maintenance-window-execution-task-invocation`.

- **AWS CLI**
- 
            
                    **To get information about a maintenance window task invocation**The following `get-maintenance-window-execution-task-invocation`example lists information about the specified task invocation that is part of the specified maintenance window execution.`aws ssm get-maintenance-window-execution-task-invocation \ --window-execution-id``"bc494bfa-e63b-49f6-8ad1-aa9f2EXAMPLE"`\ --task-id`"96f2ad59-97e3-461d-a63d-40c8aEXAMPLE"`\ --invocation-id`"a5273e2c-d2c6-4880-b3e1-5e550EXAMPLE"`Output: `{ "Status": "SUCCESS", "Parameters": "{\"comment\":\"\",\"documentName\":\"AWS-RunPowerShellScript\",\"instanceIds\":[\"i-1234567890EXAMPLE\"],\"maxConcurrency\":\"1\",\"maxErrors\":\"1\",\"parameters\":{\"executionTimeout\":[\"3600\"],\"workingDirectory\":[\"\"],\"commands\":[\"echo Hello\"]},\"timeoutSeconds\":600}", "ExecutionId": "03b6baa0-5460-4e15-83f2-ea685EXAMPLE", "InvocationId": "a5273e2c-d2c6-4880-b3e1-5e550EXAMPLE", "StartTime": 1549998326.421, "TaskType": "RUN_COMMAND", "EndTime": 1550001931.784, "WindowExecutionId": "bc494bfa-e63b-49f6-8ad1-aa9f2EXAMPLE", "StatusDetails": "Failed", "TaskExecutionId": "96f2ad59-97e3-461d-a63d-40c8aEXAMPLE" }`For more information, see [View Information About Tasks and Task Executions (AWS CLI)](https://docs.aws.amazon.com/systems-manager/latest/userguide/mw-cli-tutorial-task-info.html)in the*AWS Systems Manager User Guide*.- 
                    For API details, see [GetMaintenanceWindowExecutionTaskInvocation](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ssm/get-maintenance-window-execution-task-invocation.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `get-maintenance-window-execution-task`.

- **AWS CLI**
- 
            
                    **To get information about a maintenance window task execution**The following `get-maintenance-window-execution-task`example lists information about a task that is part of the specified maintenance window execution.`aws ssm get-maintenance-window-execution-task \ --window-execution-id``"518d5565-5969-4cca-8f0e-da3b2EXAMPLE"`\ --task-id`"ac0c6ae1-daa3-4a89-832e-d3845EXAMPLE"`Output: `{ "WindowExecutionId": "518d5565-5969-4cca-8f0e-da3b2EXAMPLE", "TaskExecutionId": "ac0c6ae1-daa3-4a89-832e-d3845EXAMPLE", "TaskArn": "AWS-RunPatchBaseline", "ServiceRole": "arn:aws:iam::111222333444:role/aws-service-role/ssm.amazonaws.com/AWSServiceRoleForAmazonSSM", "Type": "RUN_COMMAND", "TaskParameters": [ { "BaselineOverride": { "Values": [ "" ] }, "InstallOverrideList": { "Values": [ "" ] }, "Operation": { "Values": [ "Scan" ] }, "RebootOption": { "Values": [ "RebootIfNeeded" ] }, "SnapshotId": { "Values": [ "{{ aws:ORCHESTRATION_ID }}" ] }, "aws:InstanceId": { "Values": [ "i-02573cafcfEXAMPLE", "i-0471e04240EXAMPLE", "i-07782c72faEXAMPLE" ] } } ], "Priority": 1, "MaxConcurrency": "1", "MaxErrors": "3", "Status": "SUCCESS", "StartTime": "2021-08-04T11:45:35.088000-07:00", "EndTime": "2021-08-04T11:53:09.079000-07:00" }`For more information, see [View information about tasks and task executions (AWS CLI)](https://docs.aws.amazon.com/systems-manager/latest/userguide/mw-cli-tutorial-task-info.html)in the*AWS Systems Manager User Guide*.- 
                    For API details, see [GetMaintenanceWindowExecutionTask](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ssm/get-maintenance-window-execution-task.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `get-maintenance-window-execution`.

- **AWS CLI**
- 
            
                    **To get information about a maintenance window task execution**The following `get-maintenance-window-execution`example lists information about a task executed as part of the specified maintenance window execution.`aws ssm get-maintenance-window-execution \ --window-execution-id``"518d5565-5969-4cca-8f0e-da3b2EXAMPLE"`Output: `{ "Status": "SUCCESS", "TaskIds": [ "ac0c6ae1-daa3-4a89-832e-d3845EXAMPLE" ], "StartTime": 1487692834.595, "EndTime": 1487692835.051, "WindowExecutionId": "518d5565-5969-4cca-8f0e-da3b2EXAMPLE", }`For more information, see [View Information About Tasks and Task Executions (AWS CLI)](https://docs.aws.amazon.com/systems-manager/latest/userguide/mw-cli-tutorial-task-info.html)in the*AWS Systems Manager User Guide*.- 
                    For API details, see [GetMaintenanceWindowExecution](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ssm/get-maintenance-window-execution.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `get-maintenance-window-task`.

- **AWS CLI**
- 
            
                    **To get information about a maintenance window task**The following `get-maintenance-window-task`example retrieves details about the specified maintenance window task.`aws ssm get-maintenance-window-task \ --window-id``mw-0c5ed765acEXAMPLE`\ --window-task-id`0e842a8d-2d44-4886-bb62-af8dcEXAMPLE`Output: `{ "ServiceRoleArn": "arn:aws:iam::111222333444:role/aws-service-role/ssm.amazonaws.com/AWSServiceRoleForAmazonSSM", "MaxErrors": "1", "TaskArn": "AWS-RunPowerShellScript", "MaxConcurrency": "1", "WindowTaskId": "0e842a8d-2d44-4886-bb62-af8dcEXAMPLE", "TaskParameters": {}, "Priority": 1, "TaskInvocationParameters": { "RunCommand": { "Comment": "", "TimeoutSeconds": 600, "Parameters": { "commands": [ "echo Hello" ], "executionTimeout": [ "3600" ], "workingDirectory": [ "" ] } } }, "WindowId": "mw-0c5ed765acEXAMPLE", "TaskType": "RUN_COMMAND", "Targets": [ { "Values": [ "84c818da-b619-4d3d-9651-946f3EXAMPLE" ], "Key": "WindowTargetIds" } ], "Name": "ExampleTask" }`For more information, see [View Information About Maintenance Windows (AWS CLI)](https://docs.aws.amazon.com/systems-manager/latest/userguide/maintenance-windows-cli-tutorials-describe.html)in the*AWS Systems Manager User Guide*.- 
                    For API details, see [GetMaintenanceWindowTask](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ssm/get-maintenance-window-task.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `get-maintenance-window`.

- **AWS CLI**
- 
            
                    **To get information about a maintenance window**The following `get-maintenance-window`example retrieves details about the specified maintenance window.`aws ssm get-maintenance-window \ --window-id``"mw-03eb9db428EXAMPLE"`Output: `{ "AllowUnassociatedTargets": true, "CreatedDate": 1515006912.957, "Cutoff": 1, "Duration": 6, "Enabled": true, "ModifiedDate": 2020-01-01T10:04:04.099Z, "Name": "My-Maintenance-Window", "Schedule": "rate(3 days)", "WindowId": "mw-03eb9db428EXAMPLE", "NextExecutionTime": "2020-02-25T00:08:15.099Z" }`For more information, see [View information about maintenance windows (AWS CLI)](https://docs.aws.amazon.com/systems-manager/latest/userguide/maintenance-windows-cli-tutorials-describe.html)in the*AWS Systems Manager User Guide*.- 
                    For API details, see [GetMaintenanceWindow](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ssm/get-maintenance-window.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `get-ops-item`.

- **AWS CLI**
- 
            
                    **To view information about an OpsItem**The following `get-ops-item`example displays details about the specified OpsItem.`aws ssm get-ops-item \ --ops-item-id``oi-0b725EXAMPLE`Output: `{ "OpsItem": { "CreatedBy": "arn:aws:sts::111222333444:assumed-role/OpsItem-CWE-Role/fbf77cbe264a33509569f23e4EXAMPLE", "CreatedTime": "2019-12-04T15:52:16.793000-08:00", "Description": "CloudWatch Event Rule SSMOpsItems-EC2-instance-terminated was triggered. Your EC2 instance has terminated. See below for more details.", "LastModifiedBy": "arn:aws:sts::111222333444:assumed-role/OpsItem-CWE-Role/fbf77cbe264a33509569f23e4EXAMPLE", "LastModifiedTime": "2019-12-04T15:52:16.793000-08:00", "Notifications": [], "RelatedOpsItems": [], "Status": "Open", "OpsItemId": "oi-0b725EXAMPLE", "Title": "EC2 instance terminated", "Source": "EC2", "OperationalData": { "/aws/automations": { "Value": "[ { \"automationType\": \"AWS:SSM:Automation\", \"automationId\": \"AWS-CreateManagedWindowsInstance\" }, { \"automationType\": \"AWS:SSM:Automation\", \"automationId\": \"AWS-CreateManagedLinuxInstance\" } ]", "Type": "SearchableString" }, "/aws/dedup": { "Value": "{\"dedupString\":\"SSMOpsItems-EC2-instance-terminated\"}", "Type": "SearchableString" }, "/aws/resources": { "Value": "[{\"arn\":\"arn:aws:ec2:us-east-2:111222333444:instance/i-05adec7e97EXAMPLE\"}]", "Type": "SearchableString" }, "event-time": { "Value": "2019-12-04T23:52:16Z", "Type": "String" }, "instance-state": { "Value": "terminated", "Type": "String" } }, "Category": "Availability", "Severity": "4" } }`For more information, see [Working with OpsItems](https://docs.aws.amazon.com/systems-manager/latest/userguide/OpsCenter-working-with-OpsItems.html)in the*AWS Systems Manager User Guide*.- 
                    For API details, see [GetOpsItem](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ssm/get-ops-item.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `get-ops-summary`.

- **AWS CLI**
- 
            
                    **To view a summary of all OpsItems**The following `get-ops-summary`example displays a summary of all OpsItems in your AWS account.`aws ssm get-ops-summary`Output: `{ "Entities": [ { "Id": "oi-4309fEXAMPLE", "Data": { "AWS:OpsItem": { "CaptureTime": "2020-02-26T18:58:32.918Z", "Content": [ { "AccountId": "111222333444", "Category": "Availability", "CreatedBy": "arn:aws:sts::111222333444:assumed-role/OpsItem-CWE-Role/fbf77cbe264a33509569f23e4EXAMPLE", "CreatedTime": "2020-02-26T19:10:44.149Z", "Description": "CloudWatch Event Rule SSMOpsItems-EC2-instance-terminated was triggered. Your EC2 instance has terminated. See below for more details.", "LastModifiedBy": "arn:aws:sts::111222333444:assumed-role/OpsItem-CWE-Role/fbf77cbe264a33509569f23e4EXAMPLE", "LastModifiedTime": "2020-02-26T19:10:44.149Z", "Notifications": "", "OperationalData": "{\"/aws/automations\":{\"type\":\"SearchableString\",\"value\":\"[ { \\\"automationType\\\": \\\"AWS:SSM:Automation\\\", \\\"automationId\\\": \\\"AWS-CreateManagedWindowsInstance\\\" }, { \\\"automationType\\\": \\\"AWS:SSM:Automation\\\", \\\"automationId\\\": \\\"AWS-CreateManagedLinuxInstance\\\" } ]\"},\"/aws/resources\":{\"type\":\"SearchableString\",\"value\":\"[{\\\"arn\\\":\\\"arn:aws:ec2:us-east-2:111222333444:instance/i-0acbd0800fEXAMPLE\\\"}]\"},\"/aws/dedup\":{\"type\":\"SearchableString\",\"value\":\"{\\\"dedupString\\\":\\\"SSMOpsItems-EC2-instance-terminated\\\"}\"}}", "OpsItemId": "oi-4309fEXAMPLE", "RelatedItems": "", "Severity": "3", "Source": "EC2", "Status": "Open", "Title": "EC2 instance terminated" } ] } } }, { "Id": "oi-bb2a0e6a4541", "Data": { "AWS:OpsItem": { "CaptureTime": "2019-11-26T19:20:06.161Z", "Content": [ { "AccountId": "111222333444", "Category": "Availability", "CreatedBy": "arn:aws:sts::111222333444:assumed-role/OpsItem-CWE-Role/fbf77cbe264a33509569f23e4EXAMPLE", "CreatedTime": "2019-11-26T20:00:07.237Z", "Description": "CloudWatch Event Rule SSMOpsItems-SSM-maintenance-window-execution-failed was triggered. Your SSM Maintenance Window execution has failed. See below for more details.", "LastModifiedBy": "arn:aws:sts::111222333444:assumed-role/OpsItem-CWE-Role/fbf77cbe264a33509569f23e4EXAMPLE", "LastModifiedTime": "2019-11-26T20:00:07.237Z", "Notifications": "", "OperationalData": "{\"/aws/resources\":{\"type\":\"SearchableString\",\"value\":\"[{\\\"arn\\\":\\\"arn:aws:ssm:us-east-2:111222333444:maintenancewindow/mw-0e83ba440dEXAMPLE\\\"}]\"},\"/aws/dedup\":{\"type\":\"SearchableString\",\"value\":\"{\\\"dedupString\\\":\\\"SSMOpsItems-SSM-maintenance-window-execution-failed\\\"}\"}}", "OpsItemId": "oi-bb2a0EXAMPLE", "RelatedItems": "", "Severity": "3", "Source": "SSM", "Status": "Open", "Title": "SSM Maintenance Window execution failed" } ] } } } ] }`For more information, see [Working with OpsItems](https://docs.aws.amazon.com/systems-manager/latest/userguide/OpsCenter-working-with-OpsItems.html)in the*AWS Systems Manager User Guide*.- 
                    For API details, see [GetOpsSummary](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ssm/get-ops-summary.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `get-parameter-history`.

- **AWS CLI**
- 
            
                    **To get a value history for a parameter**The following `get-parameter-history`example lists the history of changes for the specified parameter, including its value.`aws ssm get-parameter-history \ --name``"MyStringParameter"`Output: `{ "Parameters": [ { "Name": "MyStringParameter", "Type": "String", "LastModifiedDate": 1582154711.976, "LastModifiedUser": "arn:aws:iam::111222333444:user/Mary-Major", "Description": "This is the first version of my String parameter", "Value": "Veni", "Version": 1, "Labels": [], "Tier": "Standard", "Policies": [] }, { "Name": "MyStringParameter", "Type": "String", "LastModifiedDate": 1582156093.471, "LastModifiedUser": "arn:aws:iam::111222333444:user/Mary-Major", "Description": "This is the second version of my String parameter", "Value": "Vidi", "Version": 2, "Labels": [], "Tier": "Standard", "Policies": [] }, { "Name": "MyStringParameter", "Type": "String", "LastModifiedDate": 1582156117.545, "LastModifiedUser": "arn:aws:iam::111222333444:user/Mary-Major", "Description": "This is the third version of my String parameter", "Value": "Vici", "Version": 3, "Labels": [], "Tier": "Standard", "Policies": [] } ] }`For more information, see [Working with parameter versions](https://docs.aws.amazon.com/systems-manager/latest/userguide/sysman-paramstore-versions.html)in the*AWS Systems Manager User Guide*.- 
                    For API details, see [GetParameterHistory](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ssm/get-parameter-history.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `get-parameter`.

- **AWS CLI**
- 
            
                    **Example 1: To display the value of a parameter**The following `get-parameter`example lists the value for the specified single parameter.`aws ssm get-parameter \ --name``"MyStringParameter"`Output: `{ "Parameter": { "Name": "MyStringParameter", "Type": "String", "Value": "Veni", "Version": 1, "LastModifiedDate": 1530018761.888, "ARN": "arn:aws:ssm:us-east-2:111222333444:parameter/MyStringParameter" "DataType": "text" } }`For more information, see [Working with Parameter Store](https://docs.aws.amazon.com/systems-manager/latest/userguide/parameter-store-working-with.html)in the*AWS Systems Manager User Guide*.**Example 2: To decrypt the value of a SecureString parameter**The following `get-parameter`example decrypts the value of the specified`SecureString`parameter.`aws ssm get-parameter \ --name``"MySecureStringParameter"`\ --with-decryptionOutput: `{ "Parameter": { "Name": "MySecureStringParameter", "Type": "SecureString", "Value": "16679b88-310b-4895-a943-e0764EXAMPLE", "Version": 2, "LastModifiedDate": 1582155479.205, "ARN": "arn:aws:ssm:us-east-2:111222333444:parameter/MySecureStringParameter" "DataType": "text" } }`For more information, see [Working with Parameter Store](https://docs.aws.amazon.com/systems-manager/latest/userguide/parameter-store-working-with.html)in the*AWS Systems Manager User Guide*.**Example 3: To display the value of a parameter using labels**The following `get-parameter`example lists the value for the specified single parameter with a specified label.`aws ssm get-parameter \ --name``"MyParameter:label"`Output: `{ "Parameter": { "Name": "MyParameter", "Type": "String", "Value": "parameter version 2", "Version": 2, "Selector": ":label", "LastModifiedDate": "2021-07-12T09:49:15.865000-07:00", "ARN": "arn:aws:ssm:us-west-2:786973925828:parameter/MyParameter", "DataType": "text" } }`For more information, see [Working with parameter labels](https://docs.aws.amazon.com/systems-manager/latest/userguide/sysman-paramstore-labels.html)in the*AWS Systems Manager User Guide*.**Example 4: To display the value of a parameter using versions**The following `get-parameter`example lists the value for the specified single parameter version.`aws ssm get-parameter \ --name``"MyParameter:2"`Output: `{ "Parameter": { "Name": "MyParameter", "Type": "String", "Value": "parameter version 2", "Version": 2, "Selector": ":2", "LastModifiedDate": "2021-07-12T09:49:15.865000-07:00", "ARN": "arn:aws:ssm:us-west-2:786973925828:parameter/MyParameter", "DataType": "text" } }`For more information, see [Working with parameter labels](https://docs.aws.amazon.com/systems-manager/latest/userguide/sysman-paramstore-labels.html)in the*AWS Systems Manager User Guide*.- 
                    For API details, see [GetParameter](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ssm/get-parameter.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `get-parameters-by-path`.

- **AWS CLI**
- 
            
                    **To list parameters in a specific path**The following `get-parameters-by-path`example lists the parameters within the specified hierarchy.`aws ssm get-parameters-by-path \ --path``"/site/newyork/department/"`Output: `{ "Parameters": [ { "Name": "/site/newyork/department/marketing", "Type": "String", "Value": "Floor 2", "Version": 1, "LastModifiedDate": 1530018761.888, "ARN": "arn:aws:ssm:us-east-1:111222333444:parameter/site/newyork/department/marketing" }, { "Name": "/site/newyork/department/infotech", "Type": "String", "Value": "Floor 3", "Version": 1, "LastModifiedDate": 1530018823.429, "ARN": "arn:aws:ssm:us-east-1:111222333444:parameter/site/newyork/department/infotech" }, ... ] }`For more information, see [Working with parameter hierarchies](https://docs.aws.amazon.com/systems-manager/latest/userguide/sysman-paramstore-hierarchies.html)in the*AWS Systems Manager User Guide*.- 
                    For API details, see [GetParametersByPath](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ssm/get-parameters-by-path.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `get-parameters`.

- **AWS CLI**
- 
            
                    **Example 1: To list the values for a parameter**The following `get-parameters`example lists the values for the three specified parameters.`aws ssm get-parameters \ --names``"MyStringParameter"``"MyStringListParameter"``"MyInvalidParameterName"`Output: `{ "Parameters": [ { "Name": "MyStringListParameter", "Type": "StringList", "Value": "alpha,beta,gamma", "Version": 1, "LastModifiedDate": 1582154764.222, "ARN": "arn:aws:ssm:us-east-2:111222333444:parameter/MyStringListParameter" "DataType": "text" }, { "Name": "MyStringParameter", "Type": "String", "Value": "Vici", "Version": 3, "LastModifiedDate": 1582156117.545, "ARN": "arn:aws:ssm:us-east-2:111222333444:parameter/MyStringParameter" "DataType": "text" } ], "InvalidParameters": [ "MyInvalidParameterName" ] }`For more information, see [Working with Parameter Store](https://docs.aws.amazon.com/systems-manager/latest/userguide/parameter-store-working-with.html)in the*AWS Systems Manager User Guide*.**Example 2: To list names and values of multiple parameters using the ``--query`` option**The following `get-parameters`example lists the names and values for the specified parameters.`aws ssm get-parameters \ --names``MyStringParameter``MyStringListParameter`\ --query`"Parameters[*].{Name:Name,Value:Value}"`Output: `[ { "Name": "MyStringListParameter", "Value": "alpha,beta,gamma" }, { "Name": "MyStringParameter", "Value": "Vidi" } ]`For more information, see [Working with Parameter Store](https://docs.aws.amazon.com/systems-manager/latest/userguide/parameter-store-working-with.html)in the*AWS Systems Manager User Guide*.**Example 3: To display the value of a parameter using labels**The following `get-parameter`example lists the value for the specified single parameter with a specified label.`aws ssm get-parameter \ --name``"MyParameter:label"`Output: `{ "Parameters": [ { "Name": "MyLabelParameter", "Type": "String", "Value": "parameter by label", "Version": 1, "Selector": ":label", "LastModifiedDate": "2021-07-12T09:49:15.865000-07:00", "ARN": "arn:aws:ssm:us-west-2:786973925828:parameter/MyParameter", "DataType": "text" }, { "Name": "MyVersionParameter", "Type": "String", "Value": "parameter by version", "Version": 2, "Selector": ":2", "LastModifiedDate": "2021-03-24T16:20:28.236000-07:00", "ARN": "arn:aws:ssm:us-west-2:786973925828:parameter/unlabel-param", "DataType": "text" } ], "InvalidParameters": [] }`For more information, see [Working with parameter labels](https://docs.aws.amazon.com/systems-manager/latest/userguide/sysman-paramstore-labels.html)in the*AWS Systems Manager User Guide*.- 
                    For API details, see [GetParameters](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ssm/get-parameters.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `get-patch-baseline-for-patch-group`.

- **AWS CLI**
- 
            
                    **To display the patch baseline for a patch group**The following `get-patch-baseline-for-patch-group`example retrieves details about the patch baseline for the specified patch group.`aws ssm get-patch-baseline-for-patch-group \ --patch-group``"DEV"`Output: `{ "PatchGroup": "DEV", "BaselineId": "pb-0123456789abcdef0", "OperatingSystem": "WINDOWS" }`For more information, see Create a Patch Group <https://docs.aws.amazon.com/systems-manager/latest/userguide/sysman-patch-group-tagging.html>__ and [Add a Patch Group to a Patch Baseline](https://docs.aws.amazon.com/systems-manager/latest/userguide/sysman-patch-group-patchbaseline.html)in the*AWS Systems Manager User Guide*.- 
                    For API details, see [GetPatchBaselineForPatchGroup](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ssm/get-patch-baseline-for-patch-group.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `get-patch-baseline`.

- **AWS CLI**
- 
            
                    **To display a patch baseline**The following `get-patch-baseline`example retrieves the details for the specified patch baseline.`aws ssm get-patch-baseline \ --baseline-id``"pb-0123456789abcdef0"`Output: `{ "BaselineId": "pb-0123456789abcdef0", "Name": "WindowsPatching", "OperatingSystem": "WINDOWS", "GlobalFilters": { "PatchFilters": [] }, "ApprovalRules": { "PatchRules": [ { "PatchFilterGroup": { "PatchFilters": [ { "Key": "PRODUCT", "Values": [ "WindowsServer2016" ] } ] }, "ComplianceLevel": "CRITICAL", "ApproveAfterDays": 0, "EnableNonSecurity": false } ] }, "ApprovedPatches": [], "ApprovedPatchesComplianceLevel": "UNSPECIFIED", "ApprovedPatchesEnableNonSecurity": false, "RejectedPatches": [], "RejectedPatchesAction": "ALLOW_AS_DEPENDENCY", "PatchGroups": [ "QA", "DEV" ], "CreatedDate": 1550244180.465, "ModifiedDate": 1550244180.465, "Description": "Patches for Windows Servers", "Sources": [] }`For more information, see [About Patch Baselines](https://docs.aws.amazon.com/systems-manager/latest/userguide/about-patch-baselines.html)in the*AWS Systems Manager User Guide*.- 
                    For API details, see [GetPatchBaseline](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ssm/get-patch-baseline.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `get-service-setting`.

- **AWS CLI**
- 
            
                    **To retrieve the service setting for Parameter Store throughput**The following `get-service-setting`This example retrieves the current service setting for Parameter Store throughput in the specified region.`aws ssm get-service-setting \ --setting-id``arn:aws:ssm:us-east-1:123456789012:servicesetting/ssm/parameter-store/high-throughput-enabled`Output: `{ "ServiceSetting": { "SettingId": "/ssm/parameter-store/high-throughput-enabled", "SettingValue": "false", "LastModifiedDate": 1555532818.578, "LastModifiedUser": "System", "ARN": "arn:aws:ssm:us-east-1:123456789012:servicesetting/ssm/parameter-store/high-throughput-enabled", "Status": "Default" } }`For more information, see [Increasing Parameter Store Throughput](https://docs.aws.amazon.com/systems-manager/latest/userguide/parameter-store-throughput.html)in the*AWS Systems Manager Users Guide*.- 
                    For API details, see [GetServiceSetting](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ssm/get-service-setting.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `label-parameter-version`.

- **AWS CLI**
- 
            
                    **Example 1: To add a label to latest version of a parameter**The following `label-parameter-version`example adds a label to the latest version of the specified parameter.`aws ssm label-parameter-version \ --name``"MyStringParameter"`\ --labels`"ProductionReady"`Output: `{ "InvalidLabels": [], "ParameterVersion": 3 }`For more information, see [Working with parameter labels](https://docs.aws.amazon.com/systems-manager/latest/userguide/sysman-paramstore-labels.html)in the*AWS Systems Manager User Guide*.**Example 2: To add a label to a specific version of a parameter**The following `label-parameter-version`example adds a label to the specified version of a parameter.`aws ssm label-parameter-version \ --name``"MyStringParameter"`\ --labels`"ProductionReady"`\ --parameter-version`"2"`--labels`"DevelopmentReady"`For more information, see [Working with parameter labels](https://docs.aws.amazon.com/systems-manager/latest/userguide/sysman-paramstore-labels.html)in the*AWS Systems Manager User Guide*.- 
                    For API details, see [LabelParameterVersion](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ssm/label-parameter-version.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `list-association-versions`.

- **AWS CLI**
- 
            
                    **To list all versions of an association for a specific association ID**The following `list-association-versions`example lists all versions of the specified associations.`aws ssm list-association-versions \ --association-id``"8dfe3659-4309-493a-8755-0123456789ab"`Output: `{ "AssociationVersions": [ { "AssociationId": "8dfe3659-4309-493a-8755-0123456789ab", "AssociationVersion": "1", "CreatedDate": 1550505536.726, "Name": "AWS-UpdateSSMAgent", "Parameters": { "allowDowngrade": [ "false" ], "version": [ "" ] }, "Targets": [ { "Key": "InstanceIds", "Values": [ "i-1234567890abcdef0" ] } ], "ScheduleExpression": "cron(0 00 12 ? * SUN *)", "AssociationName": "UpdateSSMAgent" } ] }`For more information, see [Working with associations in Systems Manager](https://docs.aws.amazon.com/systems-manager/latest/userguide/systems-manager-associations.html)in the*AWS Systems Manager User Guide*.- 
                    For API details, see [ListAssociationVersions](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ssm/list-association-versions.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `list-associations`.

- **AWS CLI**
- 
            
                    **Example 1: To list your associations for a specific instance**The following list-associations example lists all associations with the AssociationName, UpdateSSMAgent. `aws ssm list-associations``/`--association-filter-list`"key=AssociationName,value=UpdateSSMAgent"`Output: `{ "Associations": [ { "Name": "AWS-UpdateSSMAgent", "InstanceId": "i-1234567890abcdef0", "AssociationId": "8dfe3659-4309-493a-8755-0123456789ab", "AssociationVersion": "1", "Targets": [ { "Key": "InstanceIds", "Values": [ "i-016648b75dd622dab" ] } ], "Overview": { "Status": "Pending", "DetailedStatus": "Associated", "AssociationStatusAggregatedCount": { "Pending": 1 } }, "ScheduleExpression": "cron(0 00 12 ? * SUN *)", "AssociationName": "UpdateSSMAgent" } ] }`For more information, see [Working with associations in Systems Manager](https://docs.aws.amazon.com/systems-manager/latest/userguide/systems-manager-associations.html)in the*Systems Manager User Guide*.**Example 2: To list your associations for a specific document**The following list-associations example lists all associations for the specified document. `aws ssm list-associations``/`--association-filter-list`"key=Name,value=AWS-UpdateSSMAgent"`Output: `{ "Associations": [ { "Name": "AWS-UpdateSSMAgent", "InstanceId": "i-1234567890abcdef0", "AssociationId": "8dfe3659-4309-493a-8755-0123456789ab", "AssociationVersion": "1", "Targets": [ { "Key": "InstanceIds", "Values": [ "i-1234567890abcdef0" ] } ], "LastExecutionDate": 1550505828.548, "Overview": { "Status": "Success", "DetailedStatus": "Success", "AssociationStatusAggregatedCount": { "Success": 1 } }, "ScheduleExpression": "cron(0 00 12 ? * SUN *)", "AssociationName": "UpdateSSMAgent" }, { "Name": "AWS-UpdateSSMAgent", "InstanceId": "i-9876543210abcdef0", "AssociationId": "fbc07ef7-b985-4684-b82b-0123456789ab", "AssociationVersion": "1", "Targets": [ { "Key": "InstanceIds", "Values": [ "i-9876543210abcdef0" ] } ], "LastExecutionDate": 1550507531.0, "Overview": { "Status": "Success", "AssociationStatusAggregatedCount": { "Success": 1 } } } ] }`For more information, see [Working with associations in Systems Manager](https://docs.aws.amazon.com/systems-manager/latest/userguide/systems-manager-associations.html)in the*Systems Manager User Guide*.- 
                    For API details, see [ListAssociations](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ssm/list-associations.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `list-command-invocations`.

- **AWS CLI**
- 
            
                    **To list the invocations of a specific command**The following `list-command-invocations`example lists all the invocations of a command.`aws ssm list-command-invocations \ --command-id``"ef7fdfd8-9b57-4151-a15c-db9a12345678"`\ --detailsOutput: `{ "CommandInvocations": [ { "CommandId": "ef7fdfd8-9b57-4151-a15c-db9a12345678", "InstanceId": "i-02573cafcfEXAMPLE", "InstanceName": "", "Comment": "b48291dd-ba76-43e0-b9df-13e11ddaac26:6960febb-2907-4b59-8e1a-d6ce8EXAMPLE", "DocumentName": "AWS-UpdateSSMAgent", "DocumentVersion": "", "RequestedDateTime": 1582136283.089, "Status": "Success", "StatusDetails": "Success", "StandardOutputUrl": "", "StandardErrorUrl": "", "CommandPlugins": [ { "Name": "aws:updateSsmAgent", "Status": "Success", "StatusDetails": "Success", "ResponseCode": 0, "ResponseStartDateTime": 1582136283.419, "ResponseFinishDateTime": 1582136283.51, "Output": "Updating amazon-ssm-agent from 2.3.842.0 to latest\nSuccessfully downloaded https://s3.us-east-2.amazonaws.com/amazon-ssm-us-east-2/ssm-agent-manifest.json\namazon-ssm-agent 2.3.842.0 has already been installed, update skipped\n", "StandardOutputUrl": "", "StandardErrorUrl": "", "OutputS3Region": "us-east-2", "OutputS3BucketName": "", "OutputS3KeyPrefix": "" } ], "ServiceRole": "", "NotificationConfig": { "NotificationArn": "", "NotificationEvents": [], "NotificationType": "" }, "CloudWatchOutputConfig": { "CloudWatchLogGroupName": "", "CloudWatchOutputEnabled": false } }, { "CommandId": "ef7fdfd8-9b57-4151-a15c-db9a12345678", "InstanceId": "i-0471e04240EXAMPLE", "InstanceName": "", "Comment": "b48291dd-ba76-43e0-b9df-13e11ddaac26:6960febb-2907-4b59-8e1a-d6ce8EXAMPLE", "DocumentName": "AWS-UpdateSSMAgent", "DocumentVersion": "", "RequestedDateTime": 1582136283.02, "Status": "Success", "StatusDetails": "Success", "StandardOutputUrl": "", "StandardErrorUrl": "", "CommandPlugins": [ { "Name": "aws:updateSsmAgent", "Status": "Success", "StatusDetails": "Success", "ResponseCode": 0, "ResponseStartDateTime": 1582136283.812, "ResponseFinishDateTime": 1582136295.031, "Output": "Updating amazon-ssm-agent from 2.3.672.0 to latest\nSuccessfully downloaded https://s3.us-east-2.amazonaws.com/amazon-ssm-us-east-2/ssm-agent-manifest.json\nSuccessfully downloaded https://s3.us-east-2.amazonaws.com/amazon-ssm-us-east-2/amazon-ssm-agent-updater/2.3.842.0/amazon-ssm-agent-updater-snap-amd64.tar.gz\nSuccessfully downloaded https://s3.us-east-2.amazonaws.com/amazon-ssm-us-east-2/amazon-ssm-agent/2.3.672.0/amazon-ssm-agent-snap-amd64.tar.gz\nSuccessfully downloaded https://s3.us-east-2.amazonaws.com/amazon-ssm-us-east-2/amazon-ssm-agent/2.3.842.0/amazon-ssm-agent-snap-amd64.tar.gz\nInitiating amazon-ssm-agent update to 2.3.842.0\namazon-ssm-agent updated successfully to 2.3.842.0", "StandardOutputUrl": "", "StandardErrorUrl": "", "OutputS3Region": "us-east-2", "OutputS3BucketName": "", "OutputS3KeyPrefix": "8bee3135-398c-4d31-99b6-e42d2EXAMPLE/i-0471e04240EXAMPLE/awsupdateSsmAgent" } ], "ServiceRole": "", "NotificationConfig": { "NotificationArn": "", "NotificationEvents": [], "NotificationType": "" }, "CloudWatchOutputConfig": { "CloudWatchLogGroupName": "", "CloudWatchOutputEnabled": false } } ] }`For more information, see [Understanding Command Statuses](https://docs.aws.amazon.com/systems-manager/latest/userguide/monitor-commands.html)in the*AWS Systems Manager User Guide*.- 
                    For API details, see [ListCommandInvocations](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ssm/list-command-invocations.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `list-commands`.

- **AWS CLI**
- 
            
                    **Example 1: To get the status of a specific command**The following `list-commands`example retrieves and displays the status of the specified command.`aws ssm list-commands \ --command-id``"0831e1a8-a1ac-4257-a1fd-c831bEXAMPLE"`**Example 2: To get the status of commands requested after a specific date**The following `list-commands`example retrieves the details of commands requested after the specified date.`aws ssm list-commands \ --filter``"key=InvokedAfter,value=2020-02-01T00:00:00Z"`**Example 3: To list all commands requested in an AWS account**The following `list-commands`example lists all commands requested by users in the current AWS account and Region.`aws ssm list-commands`Output: `{ "Commands": [ { "CommandId": "8bee3135-398c-4d31-99b6-e42d2EXAMPLE", "DocumentName": "AWS-UpdateSSMAgent", "DocumentVersion": "", "Comment": "b48291dd-ba76-43e0-b9df-13e11ddaac26:6960febb-2907-4b59-8e1a-d6ce8EXAMPLE", "ExpiresAfter": "2020-02-19T11:28:02.500000-08:00", "Parameters": {}, "InstanceIds": [ "i-028ea792daEXAMPLE", "i-02feef8c46EXAMPLE", "i-038613f3f0EXAMPLE", "i-03a530a2d4EXAMPLE", "i-083b678d37EXAMPLE", "i-0dee81debaEXAMPLE" ], "Targets": [], "RequestedDateTime": "2020-02-19T10:18:02.500000-08:00", "Status": "Success", "StatusDetails": "Success", "OutputS3BucketName": "", "OutputS3KeyPrefix": "", "MaxConcurrency": "50", "MaxErrors": "100%", "TargetCount": 6, "CompletedCount": 6, "ErrorCount": 0, "DeliveryTimedOutCount": 0, "ServiceRole": "", "NotificationConfig": { "NotificationArn": "", "NotificationEvents": [], "NotificationType": "" }, "CloudWatchOutputConfig": { "CloudWatchLogGroupName": "", "CloudWatchOutputEnabled": false } } { "CommandId": "e9ade581-c03d-476b-9b07-26667EXAMPLE", "DocumentName": "AWS-FindWindowsUpdates", "DocumentVersion": "1", "Comment": "", "ExpiresAfter": "2020-01-24T12:37:31.874000-08:00", "Parameters": { "KbArticleIds": [ "" ], "UpdateLevel": [ "All" ] }, "InstanceIds": [], "Targets": [ { "Key": "InstanceIds", "Values": [ "i-00ec29b21eEXAMPLE", "i-09911ddd90EXAMPLE" ] } ], "RequestedDateTime": "2020-01-24T11:27:31.874000-08:00", "Status": "Success", "StatusDetails": "Success", "OutputS3BucketName": "my-us-east-2-bucket", "OutputS3KeyPrefix": "my-rc-output", "MaxConcurrency": "50", "MaxErrors": "0", "TargetCount": 2, "CompletedCount": 2, "ErrorCount": 0, "DeliveryTimedOutCount": 0, "ServiceRole": "arn:aws:iam::111222333444:role/aws-service-role/ssm.amazonaws.com/AWSServiceRoleForAmazonSSM", "NotificationConfig": { "NotificationArn": "arn:aws:sns:us-east-2:111222333444:my-us-east-2-notification-arn", "NotificationEvents": [ "All" ], "NotificationType": "Invocation" }, "CloudWatchOutputConfig": { "CloudWatchLogGroupName": "", "CloudWatchOutputEnabled": false } } { "CommandId": "d539b6c3-70e8-4853-80e5-0ce4fEXAMPLE", "DocumentName": "AWS-RunPatchBaseline", "DocumentVersion": "1", "Comment": "", "ExpiresAfter": "2020-01-24T12:21:04.350000-08:00", "Parameters": { "InstallOverrideList": [ "" ], "Operation": [ "Install" ], "RebootOption": [ "RebootIfNeeded" ], "SnapshotId": [ "" ] }, "InstanceIds": [], "Targets": [ { "Key": "InstanceIds", "Values": [ "i-00ec29b21eEXAMPLE", "i-09911ddd90EXAMPLE" ] } ], "RequestedDateTime": "2020-01-24T11:11:04.350000-08:00", "Status": "Success", "StatusDetails": "Success", "OutputS3BucketName": "my-us-east-2-bucket", "OutputS3KeyPrefix": "my-rc-output", "MaxConcurrency": "50", "MaxErrors": "0", "TargetCount": 2, "CompletedCount": 2, "ErrorCount": 0, "DeliveryTimedOutCount": 0, "ServiceRole": "arn:aws:iam::111222333444:role/aws-service-role/ssm.amazonaws.com/AWSServiceRoleForAmazonSSM", "NotificationConfig": { "NotificationArn": "arn:aws:sns:us-east-2:111222333444:my-us-east-2-notification-arn", "NotificationEvents": [ "All" ], "NotificationType": "Invocation" }, "CloudWatchOutputConfig": { "CloudWatchLogGroupName": "", "CloudWatchOutputEnabled": false } } ] }`For more information, see [Running Commands Using Systems Manager Run Command](https://docs.aws.amazon.com/systems-manager/latest/userguide/run-command.html)in the*AWS Systems Manager User Guide*.- 
                    For API details, see [ListCommands](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ssm/list-commands.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `list-compliance-items`.

- **AWS CLI**
- 
            
                    **To list compliance items for a specific instance**This example lists all compliance items for the specified instance. Command: `aws ssm list-compliance-items --resource-ids``"i-1234567890abcdef0"`--resource-types`"ManagedInstance"`Output: `{ "ComplianceItems": [ { "ComplianceType": "Association", "ResourceType": "ManagedInstance", "ResourceId": "i-1234567890abcdef0", "Id": "8dfe3659-4309-493a-8755-0123456789ab", "Title": "", "Status": "COMPLIANT", "Severity": "UNSPECIFIED", "ExecutionSummary": { "ExecutionTime": 1550408470.0 }, "Details": { "DocumentName": "AWS-GatherSoftwareInventory", "DocumentVersion": "1" } }, { "ComplianceType": "Association", "ResourceType": "ManagedInstance", "ResourceId": "i-1234567890abcdef0", "Id": "e4c2ed6d-516f-41aa-aa2a-0123456789ab", "Title": "", "Status": "COMPLIANT", "Severity": "UNSPECIFIED", "ExecutionSummary": { "ExecutionTime": 1550508475.0 }, "Details": { "DocumentName": "AWS-UpdateSSMAgent", "DocumentVersion": "1" } }, ... ], "NextToken": "--token string truncated--" }`**To list compliance items for a specific instance and association ID**This example lists all compliance items for the specified instance and association ID. Command: `aws ssm list-compliance-items --resource-ids``"i-1234567890abcdef0"`--resource-types`"ManagedInstance"`--filters`"Key=ComplianceType,Values=Association,Type=EQUAL"``"Key=Id,Values=e4c2ed6d-516f-41aa-aa2a-0123456789ab,Type=EQUAL"`**To list compliance items for a instance after a specific date and time**This example lists all compliance items for an instance after the specified date and time. Command: `aws ssm list-compliance-items --resource-ids``"i-1234567890abcdef0"`--resource-types`"ManagedInstance"`--filters`"Key=ExecutionTime,Values=2019-02-18T16:00:00Z,Type=GREATER_THAN"`- 
                    For API details, see [ListComplianceItems](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ssm/list-compliance-items.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `list-compliance-summaries`.

- **AWS CLI**
- 
            
                    **To list compliance summaries for all compliance types**This example lists compliance summaries for all compliance types in your account. Command: `aws ssm list-compliance-summaries`Output: `{ "ComplianceSummaryItems": [ { "ComplianceType": "Association", "CompliantSummary": { "CompliantCount": 2, "SeveritySummary": { "CriticalCount": 0, "HighCount": 0, "MediumCount": 0, "LowCount": 0, "InformationalCount": 0, "UnspecifiedCount": 2 } }, "NonCompliantSummary": { "NonCompliantCount": 0, "SeveritySummary": { "CriticalCount": 0, "HighCount": 0, "MediumCount": 0, "LowCount": 0, "InformationalCount": 0, "UnspecifiedCount": 0 } } }, { "ComplianceType": "Patch", "CompliantSummary": { "CompliantCount": 1, "SeveritySummary": { "CriticalCount": 0, "HighCount": 0, "MediumCount": 0, "LowCount": 0, "InformationalCount": 0, "UnspecifiedCount": 1 } }, "NonCompliantSummary": { "NonCompliantCount": 1, "SeveritySummary": { "CriticalCount": 1, "HighCount": 0, "MediumCount": 0, "LowCount": 0, "InformationalCount": 0, "UnspecifiedCount": 0 } } }, ... ], "NextToken": "eyJOZXh0VG9rZW4iOiBudWxsLCAiYm90b190cnVuY2F0ZV9hbW91bnQiOiAyfQ==" }`**To list compliance summaries for a specific compliance type**This example lists the compliance summary for the Patch compliance type. Command: `aws ssm list-compliance-summaries --filters``"Key=ComplianceType,Values=Patch,Type=EQUAL"`- 
                    For API details, see [ListComplianceSummaries](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ssm/list-compliance-summaries.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `list-document-metadata-history`.

- **AWS CLI**
- 
            
                    **Example: To view approval history and status for a change template**The following `list-document-metadata-history`example returns the approval history for the specified Change Manager change template.`aws ssm list-document-metadata-history \ --name``MyChangeManageTemplate`\ --metadata`DocumentReviews`Output: `{ "Name": "MyChangeManagerTemplate", "DocumentVersion": "1", "Author": "arn:aws:iam::111222333444;:user/JohnDoe", "Metadata": { "ReviewerResponse": [ { "CreateTime": "2021-07-30T11:58:28.025000-07:00", "UpdatedTime": "2021-07-30T12:01:19.274000-07:00", "ReviewStatus": "APPROVED", "Comment": [ { "Type": "COMMENT", "Content": "I approve this template version" } ], "Reviewer": "arn:aws:iam::111222333444;:user/ShirleyRodriguez" }, { "CreateTime": "2021-07-30T11:58:28.025000-07:00", "UpdatedTime": "2021-07-30T11:58:28.025000-07:00", "ReviewStatus": "PENDING" } ] } }`For more information, see [Reviewing and approving or rejecting change templates](https://docs.aws.amazon.com/systems-manager/latest/userguide/change-templates-review.html)in the*AWS Systems Manager User Guide*.- 
                    For API details, see [ListDocumentMetadataHistory](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ssm/list-document-metadata-history.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `list-document-versions`.

- **AWS CLI**
- 
            
                    **To list document versions**The following `list-document-versions`example lists all versions for a Systems Manager document.`aws ssm list-document-versions \ --name``"Example"`Output: `{ "DocumentVersions": [ { "Name": "Example", "DocumentVersion": "1", "CreatedDate": 1583257938.266, "IsDefaultVersion": true, "DocumentFormat": "YAML", "Status": "Active" } ] }`For more information, see [Sending Commands that Use the Document Version Parameter](https://docs.aws.amazon.com/systems-manager/latest/userguide/run-command-version.html)in the*AWS Systems Manager User Guide*.- 
                    For API details, see [ListDocumentVersions](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ssm/list-document-versions.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `list-documents`.

- **AWS CLI**
- 
            
                    **Example 1: To list documents**The following `list-documents`example lists documents owned by the requesting account tagged with the custom tag.`aws ssm list-documents \ --filters``Key=Owner,Values=Self``Key=tag:DocUse,Values=Testing`Output: `{ "DocumentIdentifiers": [ { "Name": "Example", "Owner": "29884EXAMPLE", "PlatformTypes": [ "Windows", "Linux" ], "DocumentVersion": "1", "DocumentType": "Automation", "SchemaVersion": "0.3", "DocumentFormat": "YAML", "Tags": [ { "Key": "DocUse", "Value": "Testing" } ] } ] }`For more information, see [AWS Systems Manager Documents](https://docs.aws.amazon.com/systems-manager/latest/userguide/sysman-ssm-docs.html)in the*AWS Systems Manager User Guide*.**Example 2: To list shared documents**The following `list-documents`example lists shared documents, including private shared documents not owned by AWS.`aws ssm list-documents \ --filters``Key=Name,Values=sharedDocNamePrefix``Key=Owner,Values=Private`Output: `{ "DocumentIdentifiers": [ { "Name": "Example", "Owner": "12345EXAMPLE", "PlatformTypes": [ "Windows", "Linux" ], "DocumentVersion": "1", "DocumentType": "Command", "SchemaVersion": "0.3", "DocumentFormat": "YAML", "Tags": [] } ] }`For more information, see [AWS Systems Manager Documents](https://docs.aws.amazon.com/systems-manager/latest/userguide/sysman-ssm-docs.html)in the*AWS Systems Manager User Guide*.- 
                    For API details, see [ListDocuments](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ssm/list-documents.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `list-inventory-entries`.

- **AWS CLI**
- 
            
                    **Example 1: To view specific inventory type entries for an instance**This following `list-inventory-entries`example lists the inventory entries for the AWS:Application inventory type on a specific instance.`aws ssm list-inventory-entries \ --instance-id``"i-1234567890abcdef0"`\ --type-name`"AWS:Application"`Output: `{ "TypeName": "AWS:Application", "InstanceId": "i-1234567890abcdef0", "SchemaVersion": "1.1", "CaptureTime": "2019-02-15T12:17:55Z", "Entries": [ { "Architecture": "i386", "Name": "Amazon SSM Agent", "PackageId": "{88a60be2-89a1-4df8-812a-80863c2a2b68}", "Publisher": "Amazon Web Services", "Version": "2.3.274.0" }, { "Architecture": "x86_64", "InstalledTime": "2018-05-03T13:42:34Z", "Name": "AmazonCloudWatchAgent", "Publisher": "", "Version": "1.200442.0" } ] }`**Example 2: To view custom inventory entries assigned to an instance**The following `list-inventory-entries`example lists a custom inventory entry assigned to an instance.`aws ssm list-inventory-entries \ --instance-id``"i-1234567890abcdef0"`\ --type-name`"Custom:RackInfo"`Output: `{ "TypeName": "Custom:RackInfo", "InstanceId": "i-1234567890abcdef0", "SchemaVersion": "1.0", "CaptureTime": "2021-05-22T10:01:01Z", "Entries": [ { "RackLocation": "Bay B/Row C/Rack D/Shelf E" } ] }`- 
                    For API details, see [ListInventoryEntries](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ssm/list-inventory-entries.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `list-ops-item-related-items`.

- **AWS CLI**
- 
            
                    **To list the related-item resources of an OpsItem**The following `list-ops-item-related-items`example lists the related-item resources of an OpsItem.`aws ssm list-ops-item-related-items \ --ops-item-id``"oi-f99f2EXAMPLE"`Output: `{ "Summaries": [ { "OpsItemId": "oi-f99f2EXAMPLE", "AssociationId": "e2036148-cccb-490e-ac2a-390e5EXAMPLE", "ResourceType": "AWS::SSMIncidents::IncidentRecord", "AssociationType": "IsParentOf", "ResourceUri": "arn:aws:ssm-incidents::111122223333:incident-record/example-response/64bd9b45-1d0e-2622-840d-03a87a1451fa", "CreatedBy": { "Arn": "arn:aws:sts::111122223333:assumed-role/AWSServiceRoleForIncidentManager/IncidentResponse" }, "CreatedTime": "2021-08-11T18:47:14.994000+00:00", "LastModifiedBy": { "Arn": "arn:aws:sts::111122223333:assumed-role/AWSServiceRoleForIncidentManager/IncidentResponse" }, "LastModifiedTime": "2021-08-11T18:47:14.994000+00:00" } ] }`For more information, see [Working with Incident Manager incidents in OpsCenter](https://docs.aws.amazon.com/systems-manager/latest/userguide/OpsCenter-create-OpsItems-for-Incident-Manager.html)in the*AWS Systems Manager User Guide*.- 
                    For API details, see [ListOpsItemRelatedItems](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ssm/list-ops-item-related-items.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `list-resource-compliance-summaries`.

- **AWS CLI**
- 
            
                    **To list resource-level compliance summary counts**This example lists resource-level compliance summary counts. Command: `aws ssm list-resource-compliance-summaries`Output: `{ "ResourceComplianceSummaryItems": [ { "ComplianceType": "Association", "ResourceType": "ManagedInstance", "ResourceId": "i-1234567890abcdef0", "Status": "COMPLIANT", "OverallSeverity": "UNSPECIFIED", "ExecutionSummary": { "ExecutionTime": 1550509273.0 }, "CompliantSummary": { "CompliantCount": 2, "SeveritySummary": { "CriticalCount": 0, "HighCount": 0, "MediumCount": 0, "LowCount": 0, "InformationalCount": 0, "UnspecifiedCount": 2 } }, "NonCompliantSummary": { "NonCompliantCount": 0, "SeveritySummary": { "CriticalCount": 0, "HighCount": 0, "MediumCount": 0, "LowCount": 0, "InformationalCount": 0, "UnspecifiedCount": 0 } } }, { "ComplianceType": "Patch", "ResourceType": "ManagedInstance", "ResourceId": "i-9876543210abcdef0", "Status": "COMPLIANT", "OverallSeverity": "UNSPECIFIED", "ExecutionSummary": { "ExecutionTime": 1550248550.0, "ExecutionId": "7abb6378-a4a5-4f10-8312-0123456789ab", "ExecutionType": "Command" }, "CompliantSummary": { "CompliantCount": 397, "SeveritySummary": { "CriticalCount": 0, "HighCount": 0, "MediumCount": 0, "LowCount": 0, "InformationalCount": 0, "UnspecifiedCount": 397 } }, "NonCompliantSummary": { "NonCompliantCount": 0, "SeveritySummary": { "CriticalCount": 0, "HighCount": 0, "MediumCount": 0, "LowCount": 0, "InformationalCount": 0, "UnspecifiedCount": 0 } } } ], "NextToken": "--token string truncated--" }`**To list resource-level compliance summaries for a specific compliance type**This example lists resource-level compliance summaries for the Patch compliance type. Command: `aws ssm list-resource-compliance-summaries --filters``"Key=ComplianceType,Values=Patch,Type=EQUAL"`- 
                    For API details, see [ListResourceComplianceSummaries](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ssm/list-resource-compliance-summaries.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `list-resource-data-sync`.

- **AWS CLI**
- 
            
                    **To list your resource data sync configurations**This example retrieves information about your resource data sync configurations. `aws ssm list-resource-data-sync`Output: `{ "ResourceDataSyncItems": [ { "SyncName": "MyResourceDataSync", "S3Destination": { "BucketName": "ssm-resource-data-sync", "SyncFormat": "JsonSerDe", "Region": "us-east-1" }, "LastSyncTime": 1550261472.003, "LastSuccessfulSyncTime": 1550261472.003, "LastStatus": "Successful", "SyncCreatedTime": 1543235736.72, "LastSyncStatusMessage": "The sync was successfully completed" } ] }`- 
                    For API details, see [ListResourceDataSync](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ssm/list-resource-data-sync.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `list-tags-for-resource`.

- **AWS CLI**
- 
            
                    **To list the tags applied to a patch baseline**The following `list-tags-for-resource`example lists the tags for a patch baseline.`aws ssm list-tags-for-resource \ --resource-type``"PatchBaseline"`\ --resource-id`"pb-0123456789abcdef0"`Output: `{ "TagList": [ { "Key": "Environment", "Value": "Production" }, { "Key": "Region", "Value": "EMEA" } ] }`For more information, see [Tagging AWS Resources](https://docs.aws.amazon.com/general/latest/gr/aws_tagging.html)in the*AWS General Reference*.- 
                    For API details, see [ListTagsForResource](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ssm/list-tags-for-resource.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `modify-document-permission`.

- **AWS CLI**
- 
            
                    **To modify document permissions**The following `modify-document-permission`example shares a Systems Manager document publicly.`aws ssm modify-document-permission \ --name``"Example"`\ --permission-type`"Share"`\ --account-ids-to-add`"All"`This command produces no output. For more information, see [Share a Systems Manager Document](https://docs.aws.amazon.com/systems-manager/latest/userguide/ssm-how-to-share.html)in the*AWS Systems Manager User Guide*.- 
                    For API details, see [ModifyDocumentPermission](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ssm/modify-document-permission.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `put-compliance-items`.

- **AWS CLI**
- 
            
                    **To register a compliance type and compliance details to a designated instance**This example registers the compliance type `Custom:AVCheck`to the specified managed instance. There is no output if the command succeeds.Command: `aws ssm put-compliance-items --resource-id``"i-1234567890abcdef0"`--resource-type`"ManagedInstance"`--compliance-type`"Custom:AVCheck"`--execution-summary`"ExecutionTime=2019-02-18T16:00:00Z"`--items`"Id=Version2.0,Title=ScanHost,Severity=CRITICAL,Status=COMPLIANT"`- 
                    For API details, see [PutComplianceItems](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ssm/put-compliance-items.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `put-inventory`.

- **AWS CLI**
- 
            
                    **To assign customer metadata to an instance**This example assigns rack location information to an instance. There is no output if the command succeeds. Command (Linux): `aws ssm put-inventory --instance-id``"i-016648b75dd622dab"`--items '`[{"TypeName": "Custom:RackInfo","SchemaVersion": "1.0","CaptureTime": "2019-01-22T10:01:01Z","Content":[{"RackLocation": "Bay B/Row C/Rack D/Shelf E"}]}]`'Command (Windows): `aws ssm put-inventory --instance-id``"i-016648b75dd622dab"`--items`"TypeName=Custom:RackInfo,SchemaVersion=1.0,CaptureTime=2019-01-22T10:01:01Z,Content=[{RackLocation='Bay B/Row C/Rack D/Shelf F'}]"`- 
                    For API details, see [PutInventory](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ssm/put-inventory.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `put-parameter`.

- **AWS CLI**
- 
            
                    **Example 1: To change a parameter value**The following `put-parameter`example changes the value of the specified parameter.`aws ssm put-parameter \ --name``"MyStringParameter"`\ --type`"String"`\ --value`"Vici"`\ --overwriteOutput: `{ "Version": 2, "Tier": "Standard" }`For more information, see [Create a Systems Manager parameter (AWS CLI)](https://docs.aws.amazon.com/systems-manager/latest/userguide/param-create-cli.html),[Managing parameter tiers](https://docs.aws.amazon.com/systems-manager/latest/userguide/parameter-store-advanced-parameters.html), and[Working with parameter policies](https://docs.aws.amazon.com/systems-manager/latest/userguide/parameter-store-policies.html)in the*AWS Systems Manager User Guide*.**Example 2: To create an advanced parameter**The following `put-parameter`example creates an advanced parameter.`aws ssm put-parameter \ --name``"MyAdvancedParameter"`\ --description`"This is an advanced parameter"`\ --value`"Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat [truncated]"`\ --type`"String"`\ --tier`Advanced`Output: `{ "Version": 1, "Tier": "Advanced" }`For more information, see [Create a Systems Manager parameter (AWS CLI)](https://docs.aws.amazon.com/systems-manager/latest/userguide/param-create-cli.html),[Managing parameter tiers](https://docs.aws.amazon.com/systems-manager/latest/userguide/parameter-store-advanced-parameters.html), and[Working with parameter policies](https://docs.aws.amazon.com/systems-manager/latest/userguide/parameter-store-policies.html)in the*AWS Systems Manager User Guide*.**Example 3: To convert a standard parameter to an advanced parameter**The following `put-parameter`example converts an existing standard parameter into an advanced parameter.`aws ssm put-parameter \ --name``"MyConvertedParameter"`\ --value`"abc123"`\ --type`"String"`\ --tier`Advanced`\ --overwriteOutput: `{ "Version": 2, "Tier": "Advanced" }`For more information, see [Create a Systems Manager parameter (AWS CLI)](https://docs.aws.amazon.com/systems-manager/latest/userguide/param-create-cli.html),[Managing parameter tiers](https://docs.aws.amazon.com/systems-manager/latest/userguide/parameter-store-advanced-parameters.html), and[Working with parameter policies](https://docs.aws.amazon.com/systems-manager/latest/userguide/parameter-store-policies.html)in the*AWS Systems Manager User Guide*.**Example 4: To create a parameter with a policy attached**The following `put-parameter`example creates an advanced parameter with a parameter policy attached.`aws ssm put-parameter \ --name``"/Finance/Payroll/q2accesskey"`\ --value`"P@sSwW)rd"`\ --type`"SecureString"`\ --tier`Advanced`\ --policies "[{\"Type\":\"Expiration\",\"Version\":\"1.0\",\"Attributes\":{\"Timestamp\":\"2020-06-30T00:00:00.000Z\"}},{\"Type\":\"ExpirationNotification\",\"Version\":\"1.0\",\"Attributes\":{\"Before\":\"5\",\"Unit\":\"Days\"}},{\"Type\":\"NoChangeNotification\",\"Version\":\"1.0\",\"Attributes\":{\"After\":\"60\",\"Unit\":\"Days\"}}]"Output: `{ "Version": 1, "Tier": "Advanced" }`For more information, see [Create a Systems Manager parameter (AWS CLI)](https://docs.aws.amazon.com/systems-manager/latest/userguide/param-create-cli.html),[Managing parameter tiers](https://docs.aws.amazon.com/systems-manager/latest/userguide/parameter-store-advanced-parameters.html), and[Working with parameter policies](https://docs.aws.amazon.com/systems-manager/latest/userguide/parameter-store-policies.html)in the*AWS Systems Manager User Guide*.**Example 5: To add a policy to an existing parameter**The following `put-parameter`example attaches a policy to an existing advanced parameter.`aws ssm put-parameter \ --name``"/Finance/Payroll/q2accesskey"`\ --value`"N3wP@sSwW)rd"`\ --type`"SecureString"`\ --tier`Advanced`\ --policies "[{\"Type\":\"Expiration\",\"Version\":\"1.0\",\"Attributes\":{\"Timestamp\":\"2020-06-30T00:00:00.000Z\"}},{\"Type\":\"ExpirationNotification\",\"Version\":\"1.0\",\"Attributes\":{\"Before\":\"5\",\"Unit\":\"Days\"}},{\"Type\":\"NoChangeNotification\",\"Version\":\"1.0\",\"Attributes\":{\"After\":\"60\",\"Unit\":\"Days\"}}]" --overwriteOutput: `{ "Version": 2, "Tier": "Advanced" }`For more information, see [Create a Systems Manager parameter (AWS CLI)](https://docs.aws.amazon.com/systems-manager/latest/userguide/param-create-cli.html),[Managing parameter tiers](https://docs.aws.amazon.com/systems-manager/latest/userguide/parameter-store-advanced-parameters.html), and[Working with parameter policies](https://docs.aws.amazon.com/systems-manager/latest/userguide/parameter-store-policies.html)in the*AWS Systems Manager User Guide*.- 
                    For API details, see [PutParameter](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ssm/put-parameter.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `register-default-patch-baseline`.

- **AWS CLI**
- 
            
                    **To set the default patch baseline**The following `register-default-patch-baseline`example registers the specified custom patch baseline as the default patch baseline for the operating system type that it supports.`aws ssm register-default-patch-baseline \ --baseline-id``"pb-abc123cf9bEXAMPLE"`Output: `{ "BaselineId":"pb-abc123cf9bEXAMPLE" }`The following `register-default-patch-baseline`example registers the default patch baseline provided by AWS for CentOS as the default patch baseline.`aws ssm register-default-patch-baseline \ --baseline-id``"arn:aws:ssm:us-east-2:733109147000:patchbaseline/pb-0574b43a65ea646ed"`Output: `{ "BaselineId":"pb-abc123cf9bEXAMPLE" }`For more information, see [About Predefined and Custom Patch Baselines](https://docs.aws.amazon.com/systems-manager/latest/userguide/sysman-patch-baselines.html)in the*AWS Systems Manager User Guide*.- 
                    For API details, see [RegisterDefaultPatchBaseline](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ssm/register-default-patch-baseline.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `register-patch-baseline-for-patch-group`.

- **AWS CLI**
- 
            
                    **To register a patch baseline for a patch group**The following `register-patch-baseline-for-patch-group`example registers a patch baseline for a patch group.`aws ssm register-patch-baseline-for-patch-group \ --baseline-id``"pb-045f10b4f382baeda"`\ --patch-group`"Production"`Output: `{ "BaselineId": "pb-045f10b4f382baeda", "PatchGroup": "Production" }`For more information, see Create a Patch Group <https://docs.aws.amazon.com/systems-manager/latest/userguide/sysman-patch-group-tagging.html>__ and [Add a Patch Group to a Patch Baseline](https://docs.aws.amazon.com/systems-manager/latest/userguide/sysman-patch-group-patchbaseline.html)in the*AWS Systems Manager User Guide*.- 
                    For API details, see [RegisterPatchBaselineForPatchGroup](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ssm/register-patch-baseline-for-patch-group.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `register-target-with-maintenance-window`.

- **AWS CLI**
- 
            
                    **Example 1: To register a single target with a maintenance window**The following `register-target-with-maintenance-window`example registers an instance with a maintenance window.`aws ssm register-target-with-maintenance-window \ --window-id``"mw-ab12cd34ef56gh78"`\ --target`"Key=InstanceIds,Values=i-0000293ffd8c57862"`\ --owner-information`"Single instance"`\ --resource-type`"INSTANCE"`Output: `{ "WindowTargetId":"1a2b3c4d-1a2b-1a2b-1a2b-1a2b3c4d-1a2" }`**Example 2: To register multiple targets with a maintenance window using instance IDs**The following `register-target-with-maintenance-window`example registers two instances with a maintenance window by specifying their instance IDs.`aws ssm register-target-with-maintenance-window \ --window-id``"mw-ab12cd34ef56gh78"`\ --target`"Key=InstanceIds,Values=i-0000293ffd8c57862,i-0cb2b964d3e14fd9f"`\ --owner-information`"Two instances in a list"`\ --resource-type`"INSTANCE"`Output: `{ "WindowTargetId":"1a2b3c4d-1a2b-1a2b-1a2b-1a2b3c4d-1a2" }`**Example 3: To register targets with a maintenance window using resource tags**The following `register-target-with-maintenance-window`example registers instances with a maintenance window by specifying resource tags that have been applied to the instances.`aws ssm register-target-with-maintenance-window \ --window-id``"mw-06cf17cbefcb4bf4f"`\ --targets`"Key=tag:Environment,Values=Prod"``"Key=Role,Values=Web"`\ --owner-information`"Production Web Servers"`\ --resource-type`"INSTANCE"`Output: `{ "WindowTargetId":"1a2b3c4d-1a2b-1a2b-1a2b-1a2b3c4d-1a2" }`**Example 4: To register targets using a group of tag keys**The following `register-target-with-maintenance-window`example register instances that all have one or more tag keys assigned to them, regardless of their key values.`aws ssm register-target-with-maintenance-window \ --window-id``"mw-0c50858d01EXAMPLE"`\ --resource-type`"INSTANCE"`\ --target`"Key=tag-key,Values=Name,Instance-Type,CostCenter"`Output: `{ "WindowTargetId":"1a2b3c4d-1a2b-1a2b-1a2b-1a2b3c4d-1a2" }`**Example 5: To register targets using a resource group name**The following `register-target-with-maintenance-window`example register a specified resource group, regardless of the type of resources it contains.`aws ssm register-target-with-maintenance-window \ --window-id``"mw-0c50858d01EXAMPLE"`\ --resource-type`"RESOURCE_GROUP"`\ --target`"Key=resource-groups:Name,Values=MyResourceGroup"`Output: `{ "WindowTargetId":"1a2b3c4d-1a2b-1a2b-1a2b-1a2b3c4d-1a2" }`For more information, see [Register a Target Instance with the Maintenance Window (AWS CLI)](https://docs.aws.amazon.com/systems-manager/latest/userguide/mw-cli-tutorial-targets.html)in the*AWS Systems Manager User Guide*.- 
                    For API details, see [RegisterTargetWithMaintenanceWindow](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ssm/register-target-with-maintenance-window.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `register-task-with-maintenance-window`.

- **AWS CLI**
- 
            
                    **Example 1: To register an Automation task with a maintenance window**The following `register-task-with-maintenance-window`example registers an Automation task with a maintenance window that is targeted at an instance.`aws ssm register-task-with-maintenance-window \ --window-id``"mw-082dcd7649EXAMPLE"`\ --targets`Key=InstanceIds,Values=i-1234520122EXAMPLE`\ --task-arn`AWS-RestartEC2Instance`\ --service-role-arn`arn:aws:iam::111222333444:role/SSM`--task-type`AUTOMATION`\ --task-invocation-parameters "{\"Automation\":{\"DocumentVersion\":\"\$LATEST\",\"Parameters\":{\"InstanceId\":[\"{{RESOURCE_ID}}\"]}}}" \ --priority`0`\ --max-concurrency`1`\ --max-errors`1`\ --name`"AutomationExample"`\ --description`"Restarting EC2 Instance for maintenance"`Output: `{ "WindowTaskId":"11144444-5555-6666-7777-88888888" }`For more information, see [Register a Task with the Maintenance Window (AWS CLI)](https://docs.aws.amazon.com/systems-manager/latest/userguide/mw-cli-tutorial-tasks.html)in the*AWS Systems Manager User Guide*.**Example 2: To register a Lambda task with a Maintenance Window**The following `register-task-with-maintenance-window`example registers a Lambda task with a Maintenance Window that is targeted at an instance.`aws ssm register-task-with-maintenance-window \ --window-id``"mw-082dcd7649dee04e4"`\ --targets`Key=InstanceIds,Values=i-12344d305eEXAMPLE`\ --task-arn`arn:aws:lambda:us-east-1:111222333444:function:SSMTestLAMBDA`\ --service-role-arn`arn:aws:iam::111222333444:role/SSM`\ --task-type`LAMBDA`\ --task-invocation-parameters '`{"Lambda":{"Payload":"{\"InstanceId\":\"{{RESOURCE_ID}}\",\"targetType\":\"{{TARGET_TYPE}}\"}","Qualifier":"$LATEST"}}`' \ --priority`0`\ --max-concurrency`10`\ --max-errors`5`\ --name`"Lambda_Example"`\ --description`"My Lambda Example"`Output: `{ "WindowTaskId":"22244444-5555-6666-7777-88888888" }`For more information, see [Register a Task with the Maintenance Window (AWS CLI)](https://docs.aws.amazon.com/systems-manager/latest/userguide/mw-cli-tutorial-tasks.html)in the*AWS Systems Manager User Guide*.**Example 3: To register a Run Command task with a maintenance window**The following `register-task-with-maintenance-window`example registers a Run Command task with a maintenance window that is targeted at an instance.`aws ssm register-task-with-maintenance-window \ --window-id``"mw-082dcd7649dee04e4"`\ --targets`"Key=InstanceIds,Values=i-12344d305eEXAMPLE"`\ --service-role-arn`"arn:aws:iam::111222333444:role/SSM"`\ --task-type`"RUN_COMMAND"`\ --name`"SSMInstallPowerShellModule"`\ --task-arn`"AWS-InstallPowerShellModule"`\ --task-invocation-parameters "{\"RunCommand\":{\"Comment\":\"\",\"OutputS3BucketName\":\"runcommandlogs\",\"Parameters\":{\"commands\":[\"Get-Module -ListAvailable\"],\"executionTimeout\":[\"3600\"],\"source\":[\"https:\/\/gallery.technet.microsoft.com\/EZOut-33ae0fb7\/file\/`1``1`0351\/1\/EZOut.zip\"],\"workingDirectory\":[\"\\\\\"]},\"TimeoutSeconds\":600}}" \ --max-concurrency 1 \ --max-errors 1 \ --priority`10`Output: `{ "WindowTaskId":"33344444-5555-6666-7777-88888888" }`For more information, see [Register a Task with the Maintenance Window (AWS CLI)](https://docs.aws.amazon.com/systems-manager/latest/userguide/mw-cli-tutorial-tasks.html)in the*AWS Systems Manager User Guide*.**Example 4: To register a Step Functions task with a maintenance window**The following `register-task-with-maintenance-window`example registers a Step Functions task with a maintenance window that is targeted at an instance.`aws ssm register-task-with-maintenance-window \ --window-id``"mw-1234d787d6EXAMPLE"`\ --targets`Key=WindowTargetIds,Values=12347414-69c3-49f8-95b8-ed2dcEXAMPLE`\ --task-arn`arn:aws:states:us-east-1:111222333444:stateMachine:SSMTestStateMachine`\ --service-role-arn`arn:aws:iam::111222333444:role/MaintenanceWindows`\ --task-type`STEP_FUNCTIONS`\ --task-invocation-parameters '`{"StepFunctions":{"Input":"{\"InstanceId\":\"{{RESOURCE_ID}}\"}"}}`' \ --priority`0`\ --max-concurrency`10`\ --max-errors`5`\ --name`"Step_Functions_Example"`\ --description`"My Step Functions Example"`Output: `{ "WindowTaskId":"44444444-5555-6666-7777-88888888" }`For more information, see [Register a Task with the Maintenance Window (AWS CLI)](https://docs.aws.amazon.com/systems-manager/latest/userguide/mw-cli-tutorial-tasks.html)in the*AWS Systems Manager User Guide*.**Example 5: To register a task using a maintenance windows target ID**The following `register-task-with-maintenance-window`example registers a task using a maintenance window target ID. The maintenance window target ID was in the output of the`aws ssm register-target-with-maintenance-window`command. You can also retrieve it from the output of the`aws ssm describe-maintenance-window-targets`command.`aws ssm register-task-with-maintenance-window \ --targets``"Key=WindowTargetIds,Values=350d44e6-28cc-44e2-951f-4b2c9EXAMPLE"`\ --task-arn`"AWS-RunShellScript"`\ --service-role-arn`"arn:aws:iam::111222333444:role/MaintenanceWindowsRole"`\ --window-id`"mw-ab12cd34eEXAMPLE"`\ --task-type`"RUN_COMMAND"`\ --task-parameters "{\"commands\":{\"Values\":[\"df\"]}}" \ --max-concurrency`1`\ --max-errors`1`\ --priority`10`Output: `{ "WindowTaskId":"33344444-5555-6666-7777-88888888" }`For more information, see [Register a Task with the Maintenance Window (AWS CLI)](https://docs.aws.amazon.com/systems-manager/latest/userguide/mw-cli-tutorial-tasks.html)in the*AWS Systems Manager User Guide*.- 
                    For API details, see [RegisterTaskWithMaintenanceWindow](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ssm/register-task-with-maintenance-window.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `remove-tags-from-resource`.

- **AWS CLI**
- 
            
                    **To remove a tag from a patch baseline**The following `remove-tags-from-resource`example removes tags from a patch baseline.`aws ssm remove-tags-from-resource \ --resource-type``"PatchBaseline"`\ --resource-id`"pb-0123456789abcdef0"`\ --tag-keys`"Region"`This command produces no output. For more information, see [Tagging AWS Resources](https://docs.aws.amazon.com/general/latest/gr/aws_tagging.html)in the*AWS General Reference*.- 
                    For API details, see [RemoveTagsFromResource](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ssm/remove-tags-from-resource.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `reset-service-setting`.

- **AWS CLI**
- 
            
                    **To reset the service setting for Parameter Store throughput**The following `reset-service-setting`example resets the service setting for Parameter Store throughput in the specified region to no longer use increased throughput.`aws ssm reset-service-setting \ --setting-id``arn:aws:ssm:us-east-1:123456789012:servicesetting/ssm/parameter-store/high-throughput-enabled`Output: `{ "ServiceSetting": { "SettingId": "/ssm/parameter-store/high-throughput-enabled", "SettingValue": "false", "LastModifiedDate": 1555532818.578, "LastModifiedUser": "System", "ARN": "arn:aws:ssm:us-east-1:123456789012:servicesetting/ssm/parameter-store/high-throughput-enabled", "Status": "Default" } }`For more information, see [Increasing Parameter Store Throughput](https://docs.aws.amazon.com/systems-manager/latest/userguide/parameter-store-throughput.html)in the*AWS Systems Manager User Guide*.- 
                    For API details, see [ResetServiceSetting](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ssm/reset-service-setting.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `resume-session`.

- **AWS CLI**
- 
            
                    **To resume a Session Manager session**This `resume-session`example resumes a Session Manager session with an instance after it has been disconnected. Note that this interactive command requires the Session Manager plugin to be installed on the client machine making the call.`aws ssm resume-session \ --session-id``Mary-Major-07a16060613c408b5`Output: `{ "SessionId": "Mary-Major-07a16060613c408b5", "TokenValue": "AAEAAVbTGsaOnyvcUoNGqifbv5r/8lgxuQljCuY8qVcvOnoBAAAAAFxtd3jIXAFUUXGTJ7zF/AWJPwDviOlF5p3dlAgrqVIVO6IEXhkHLz0/1gXKRKEME71E6TLOplLDJAMZ+kREejkZu4c5AxMkrQjMF+gtHP1bYJKTwtHQd1wjulPLexO8SHl7g5R/wekrj6WsDUpnEegFBfGftpAIz2GXQVfTJXKfkc5qepQ11C11DOIT2dozOqXgHwfQHfAKLErM5dWDZqKwyT1Z3iw7unQdm3p5qsbrugiOZ7CRANTE+ihfGa6MEJJ97Jmat/a2TspEnOjNn9Mvu5iwXIW2yCvWZrGUj+/QI5Xr7s1XJBEnSKR54o4fN0GV9RWl0RZsZm1m1ki0JJtiwwgZ", "StreamUrl": "wss://ssmmessages.us-east-2.amazonaws.com/v1/data-channel/Mary-Major-07a16060613c408b5?role=publish_subscribe" }`For more information, see [Install the Session Manager Plugin for the AWS CLI](https://docs.aws.amazon.com/systems-manager/latest/userguide/session-manager-working-with-install-plugin.html)in the*AWS Systems Manager User Guide*.- 
                    For API details, see [ResumeSession](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ssm/resume-session.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `send-automation-signal`.

- **AWS CLI**
- 
            
                    **To send a signal to an automation execution**The following `send-automation-signal`example sends an Approve signal to an Automation execution.`aws ssm send-automation-signal \ --automation-execution-id``73c8eef8-f4ee-4a05-820c-e354fEXAMPLE`\ --signal-type`"Approve"`This command produces no output. For more information, see [Running an Automation Workflow with Approvers](https://docs.aws.amazon.com/systems-manager/latest/userguide/automation-working-executing-approval.html)in the*AWS Systems Manager User Guide*.- 
                    For API details, see [SendAutomationSignal](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ssm/send-automation-signal.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `send-command`.

- **AWS CLI**
- 
            
                    **Example 1: To run a command on one or more remote instances**The following `send-command`example runs an`echo`command on a target instance.`aws ssm send-command \ --document-name``"AWS-RunShellScript"`\ --parameters '`commands=["echo HelloWorld"]`' \ --targets`"Key=instanceids,Values=i-1234567890abcdef0"`\ --comment`"echo HelloWorld"`Output: `{ "Command": { "CommandId": "92853adf-ba41-4cd6-9a88-142d1EXAMPLE", "DocumentName": "AWS-RunShellScript", "DocumentVersion": "", "Comment": "echo HelloWorld", "ExpiresAfter": 1550181014.717, "Parameters": { "commands": [ "echo HelloWorld" ] }, "InstanceIds": [ "i-0f00f008a2dcbefe2" ], "Targets": [], "RequestedDateTime": 1550173814.717, "Status": "Pending", "StatusDetails": "Pending", "OutputS3BucketName": "", "OutputS3KeyPrefix": "", "MaxConcurrency": "50", "MaxErrors": "0", "TargetCount": 1, "CompletedCount": 0, "ErrorCount": 0, "DeliveryTimedOutCount": 0, "ServiceRole": "", "NotificationConfig": { "NotificationArn": "", "NotificationEvents": [], "NotificationType": "" }, "CloudWatchOutputConfig": { "CloudWatchLogGroupName": "", "CloudWatchOutputEnabled": false } } }`For more information, see [Running Commands Using Systems Manager Run Command](https://docs.aws.amazon.com/systems-manager/latest/userguide/run-command.html)in the*AWS Systems Manager User Guide*.**Example 2: To get IP information about an instance**The following `send-command`example retrieves the IP information about an instance.`aws ssm send-command \ --instance-ids``"i-1234567890abcdef0"`\ --document-name`"AWS-RunShellScript"`\ --comment`"IP config"`\ --parameters`"commands=ifconfig"`See example 1 for sample output. For more information, see [Running Commands Using Systems Manager Run Command](https://docs.aws.amazon.com/systems-manager/latest/userguide/run-command.html)in the*AWS Systems Manager User Guide*.**Example 3: To run a command on instances with specific tags**The following `send-command`example runs a command on instances that have the tag key "ENV" and the value "Dev".`aws ssm send-command \ --targets``"Key=tag:ENV,Values=Dev"`\ --document-name`"AWS-RunShellScript"`\ --parameters`"commands=ifconfig"`See example 1 for sample output. For more information, see [Running Commands Using Systems Manager Run Command](https://docs.aws.amazon.com/systems-manager/latest/userguide/run-command.html)in the*AWS Systems Manager User Guide*.**Example 4: To run a command that sends SNS notifications**The following `send-command`example runs a command that sends SNS notifications for all notification events and the`Command`notification type.`aws ssm send-command \ --instance-ids``"i-1234567890abcdef0"`\ --document-name`"AWS-RunShellScript"`\ --comment`"IP config"`\ --parameters`"commands=ifconfig"`\ --service-role-arn`"arn:aws:iam::123456789012:role/SNS_Role"`\ --notification-config`"NotificationArn=arn:aws:sns:us-east-1:123456789012:SNSTopicName,NotificationEvents=All,NotificationType=Command"`See example 1 for sample output. For more information, see [Running Commands Using Systems Manager Run Command](https://docs.aws.amazon.com/systems-manager/latest/userguide/run-command.html)in the*AWS Systems Manager User Guide*.**Example 5: To run a command that outputs to S3 and CloudWatch**The following `send-command`example runs a command that outputs command details to an S3 bucket and to a CloudWatch Logs log group.`aws ssm send-command \ --instance-ids``"i-1234567890abcdef0"`\ --document-name`"AWS-RunShellScript"`\ --comment`"IP config"`\ --parameters`"commands=ifconfig"`\ --output-`s3-bucket-name`"s3-bucket-name" \ --output-s3-key-prefix`"runcommand"`\ --cloud-watch-output-config`"CloudWatchOutputEnabled=true,CloudWatchLogGroupName=CWLGroupName"`See example 1 for sample output. For more information, see [Running Commands Using Systems Manager Run Command](https://docs.aws.amazon.com/systems-manager/latest/userguide/run-command.html)in the*AWS Systems Manager User Guide*.**Example 6: To run commands on multiple instances with different tags**The following `send-command`example runs a command on instances with two different tag keys and values.`aws ssm send-command \ --document-name``"AWS-RunPowerShellScript"`\ --parameters commands=["echo helloWorld"] \ --targets`Key=tag:Env,Values=Dev``Key=tag:Role,Values=WebServers`See example 1 for sample output. For more information, see [Running Commands Using Systems Manager Run Command](https://docs.aws.amazon.com/systems-manager/latest/userguide/run-command.html)in the*AWS Systems Manager User Guide*.**Example 7: To target multiple instances with the same tag key**The following `send-command`example runs a command on instances that have the same tag key but with different values.`aws ssm send-command \ --document-name``"AWS-RunPowerShellScript"`\ --parameters commands=["echo helloWorld"] \ --targets`Key=tag:Env,Values=Dev,Test`See example 1 for sample output. For more information, see [Running Commands Using Systems Manager Run Command](https://docs.aws.amazon.com/systems-manager/latest/userguide/run-command.html)in the*AWS Systems Manager User Guide*.**Example 8: To run a command that uses a shared document**The following `send-command`example runs a shared document on a target instance.`aws ssm send-command \ --document-name``"arn:aws:ssm:us-east-1:123456789012:document/ExampleDocument"`\ --targets`"Key=instanceids,Values=i-1234567890abcdef0"`See example 1 for sample output. For more information, see [Using shared SSM documents](https://docs.aws.amazon.com/systems-manager/latest/userguide/ssm-using-shared.html)in the*AWS Systems Manager User Guide*.- 
                    For API details, see [SendCommand](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ssm/send-command.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `start-associations-once`.

- **AWS CLI**
- 
            
                    **To run an association immediately and only one time**The following `start-associations-once`example run the specified association immediately and only once. There is no output if the command succeeds.`aws ssm start-associations-once \ --association-id``"8dfe3659-4309-493a-8755-0123456789ab"`This command produces no output. For more information, see [Viewing association histories](https://docs.aws.amazon.com/systems-manager/latest/userguide/sysman-state-assoc-history.html)in the*AWS Systems Manager User Guide*.- 
                    For API details, see [StartAssociationsOnce](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ssm/start-associations-once.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `start-automation-execution`.

- **AWS CLI**
- 
            
                    **Example 1: To execute an automation document**The following `start-automation-execution`example runs an Automation document.`aws ssm start-automation-execution \ --document-name``"AWS-UpdateLinuxAmi"`\ --parameters`"AutomationAssumeRole=arn:aws:iam::123456789012:role/SSMAutomationRole,SourceAmiId=ami-EXAMPLE,IamInstanceProfileName=EC2InstanceRole"`Output: `{ "AutomationExecutionId": "4105a4fc-f944-11e6-9d32-0a1b2EXAMPLE" }`For more information, see [Running an Automation Workflow Manually](https://docs.aws.amazon.com/systems-manager/latest/userguide/automation-working-executing-manually.html)in the*AWS Systems Manager User Guide*.**Example 2: To run a shared automation document**The following `start-automation-execution`example runs a shared Automation document.`aws ssm start-automation-execution \ --document-name``"arn:aws:ssm:us-east-1:123456789012:document/ExampleDocument"`Output: `{ "AutomationExecutionId": "4105a4fc-f944-11e6-9d32-0a1b2EXAMPLE" }`For more information, see [Using shared SSM documents](https://docs.aws.amazon.com/systems-manager/latest/userguide/ssm-using-shared.html)in the*AWS Systems Manager User Guide*.- 
                    For API details, see [StartAutomationExecution](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ssm/start-automation-execution.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `start-change-request-execution`.

- **AWS CLI**
- 
            
                    **Example 1: To start a change request**The following `start-change-request-execution`example starts a change request with minimal options specified.`aws ssm start-change-request-execution \ --change-request-name``MyChangeRequest`\ --document-name`AWS-HelloWorldChangeTemplate`\ --runbooks '`[{"DocumentName": "AWS-HelloWorld","Parameters": {"AutomationAssumeRole": ["arn:aws:iam:us-east-2:1112223233444:role/MyChangeManagerAssumeRole"]}}]`' \ --parameters Approver="JohnDoe",ApproverType="IamUser",ApproverSnsTopicArn="arn:aws:sns:us-east-2:1112223233444:MyNotificationTopic"Output: `{ "AutomationExecutionId": "9d32a4fc-f944-11e6-4105-0a1b2EXAMPLE" }`**Example 2: To start a change request using an external JSON file**The following `start-automation-execution`example starts a change request with multiple options specified in a JSON file.`aws ssm start-change-request-execution \ --cli-input-json``file://MyChangeRequest.json`Contents of `MyChangeRequest.json`:`{ "ChangeRequestName": "MyChangeRequest", "DocumentName": "AWS-HelloWorldChangeTemplate", "DocumentVersion": "$DEFAULT", "ScheduledTime": "2021-12-30T03:00:00", "ScheduledEndTime": "2021-12-30T03:05:00", "Tags": [ { "Key": "Purpose", "Value": "Testing" } ], "Parameters": { "Approver": [ "JohnDoe" ], "ApproverType": [ "IamUser" ], "ApproverSnsTopicArn": [ "arn:aws:sns:us-east-2:111222333444;:MyNotificationTopic ] }, "Runbooks": [ { "DocumentName": "AWS-HelloWorld", "DocumentVersion": "1", "MaxConcurrency": "1", "MaxErrors": "1", "Parameters": { "AutomationAssumeRole": [ "arn:aws:iam::111222333444:role/MyChangeManagerAssumeRole" ] } } ], "ChangeDetails": "### Document Name: HelloWorldChangeTemplate\n\n## What does this document do?\nThis change template demonstrates the feature set available for creating change templates for Change Manager. This template starts a Runbook workflow for the Automation document called AWS-HelloWorld.\n\n## Input Parameters\n* ApproverSnsTopicArn: (Required) Amazon Simple Notification Service ARN for approvers.\n* Approver: (Required) The name of the approver to send this request to.\n* ApproverType: (Required) The type of reviewer.\n * Allowed Values: IamUser, IamGroup, IamRole, SSOGroup, SSOUser\n\n## Output Parameters\nThis document has no outputs \n" }`Output: `{ "AutomationExecutionId": "9d32a4fc-f944-11e6-4105-0a1b2EXAMPLE" }`For more information, see [Creating change requests](https://docs.aws.amazon.com/systems-manager/latest/userguide/change-requests-create.html)in the*AWS Systems Manager User Guide*.- 
                    For API details, see [StartChangeRequestExecution](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ssm/start-change-request-execution.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `start-session`.

- **AWS CLI**
- 
            
                    **Example 1: To start a Session Manager session**This `start-session`example establishes a connection with an instance for a Session Manager session. Note that this interactive command requires the Session Manager plugin to be installed on the client machine making the call.`aws ssm start-session \ --target``"i-1234567890abcdef0"`Output: `Starting session with SessionId: Jane-Roe-07a16060613c408b5`**Example 2: To start a Session Manager session using SSH**This `start-session`example establishes a connection with an instance for a Session Manager session using SSH. Note that this interactive command requires the Session Manager plugin to be installed on the client machine making the call, and that the command uses the default user on the instance, such as`ec2-user`for EC2 instances for Linux.`ssh -i /path/my-key-pair.pem ec2-user@i-02573cafcfEXAMPLE`Output: `Starting session with SessionId: ec2-user-07a16060613c408b5`For more information, see [Start a Session](https://docs.aws.amazon.com/systems-manager/latest/userguide/session-manager-working-with-sessions-start.html)and[Install the Session Manager Plugin for the AWS CLI](https://docs.aws.amazon.com/systems-manager/latest/userguide/session-manager-working-with-install-plugin.html)in the*AWS Systems Manager User Guide*.- 
                    For API details, see [StartSession](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ssm/start-session.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `stop-automation-execution`.

- **AWS CLI**
- 
            
                    **To stop an automation execution**The following `stop-automation-execution`example stops an Automation document.`aws ssm stop-automation-execution --automation-execution-id``"4105a4fc-f944-11e6-9d32-0a1b2EXAMPLE"`This command produces no output. For more information, see [Running an Automation Workflow Manually](https://docs.aws.amazon.com/systems-manager/latest/userguide/automation-working-executing-manually.html)in the*AWS Systems Manager User Guide*.- 
                    For API details, see [StopAutomationExecution](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ssm/stop-automation-execution.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `terminate-session`.

- **AWS CLI**
- 
            
                    **To end a Session Manager session**This `terminate-session`example permanently ends a session that was created by the user "Shirley-Rodriguez" and closes the data connection between the Session Manager client and SSM Agent on the instance.`aws ssm terminate-session \ --session-id``"Shirley-Rodriguez-07a16060613c408b5"`Output: `{ "SessionId": "Shirley-Rodriguez-07a16060613c408b5" }`For more information, see [Terminate a Session](https://docs.aws.amazon.com/systems-manager/latest/userguide/session-manager-working-with-sessions-end.html)in the*AWS Systems Manager User Guide*.- 
                    For API details, see [TerminateSession](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ssm/terminate-session.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `unlabel-parameter-version`.

- **AWS CLI**
- 
            
                    **To delete parameter labels**The following `unlabel-parameter-version`example deletes the specified labels from the given parameter version.`aws ssm unlabel-parameter-version \ --name``"parameterName"`\ --parameter-version`2`\ --labels`"label_1"``"label_2"``"label_3"`Output: `{ "RemovedLabels": [ "label_1" "label_2" "label_3" ], "InvalidLabels": [] }`For more information, see [Delete parameter labels (AWS CLI)](https://docs.aws.amazon.com/systems-manager/latest/userguide/sysman-paramstore-labels.html#systems-manager-parameter-store-labels-cli-delete)in the*AWS Systems Manager User Guide*.- 
                    For API details, see [UnlabelParameterVersion](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ssm/unlabel-parameter-version.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `update-association-status`.

- **AWS CLI**
- 
            
                    **To update the association status**The following `update-association-status`example updates the association status of the association between an instance and a document.`aws ssm update-association-status \ --name``"AWS-UpdateSSMAgent"`\ --instance-id`"i-1234567890abcdef0"`\ --association-status`"Date=1424421071.939,Name=Pending,Message=temp_status_change,AdditionalInfo=Additional-Config-Needed"`Output: `{ "AssociationDescription": { "Name": "AWS-UpdateSSMAgent", "InstanceId": "i-1234567890abcdef0", "AssociationVersion": "1", "Date": 1550507529.604, "LastUpdateAssociationDate": 1550507806.974, "Status": { "Date": 1424421071.0, "Name": "Pending", "Message": "temp_status_change", "AdditionalInfo": "Additional-Config-Needed" }, "Overview": { "Status": "Success", "AssociationStatusAggregatedCount": { "Success": 1 } }, "DocumentVersion": "$DEFAULT", "AssociationId": "8dfe3659-4309-493a-8755-0123456789ab", "Targets": [ { "Key": "InstanceIds", "Values": [ "i-1234567890abcdef0" ] } ], "LastExecutionDate": 1550507808.0, "LastSuccessfulExecutionDate": 1550507808.0 } }`For more information, see [Working with associations in Systems Manager](https://docs.aws.amazon.com/systems-manager/latest/userguide/systems-manager-associations.html)in the*AWS Systems Manager User Guide*.- 
                    For API details, see [UpdateAssociationStatus](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ssm/update-association-status.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `update-association`.

- **AWS CLI**
- 
            
                    **Example 1: To update a document association**The following `update-association`example updates an association with a new document version.`aws ssm update-association \ --association-id``"8dfe3659-4309-493a-8755-0123456789ab"`\ --document-version`"\$LATEST"`Output: `{ "AssociationDescription": { "Name": "AWS-UpdateSSMAgent", "AssociationVersion": "2", "Date": 1550508093.293, "LastUpdateAssociationDate": 1550508106.596, "Overview": { "Status": "Pending", "DetailedStatus": "Creating" }, "DocumentVersion": "$LATEST", "AssociationId": "8dfe3659-4309-493a-8755-0123456789ab", "Targets": [ { "Key": "tag:Name", "Values": [ "Linux" ] } ], "LastExecutionDate": 1550508094.879, "LastSuccessfulExecutionDate": 1550508094.879 } }`For more information, see [Editing and creating a new version of an association](https://docs.aws.amazon.com/systems-manager/latest/userguide/sysman-state-assoc-edit.html)in the*AWS Systems Manager User Guide*.**Example 2: To update the schedule expression of an association**The following `update-association`example updates the schedule expression for the specified association.`aws ssm update-association \ --association-id``"8dfe3659-4309-493a-8755-0123456789ab"`\ --schedule-expression`"cron(0 0 0/4 1/1 * ? *)"`Output: `{ "AssociationDescription": { "Name": "AWS-HelloWorld", "AssociationVersion": "2", "Date": "2021-02-08T13:54:19.203000-08:00", "LastUpdateAssociationDate": "2021-06-29T11:51:07.933000-07:00", "Overview": { "Status": "Pending", "DetailedStatus": "Creating" }, "DocumentVersion": "$DEFAULT", "AssociationId": "8dfe3659-4309-493a-8755-0123456789ab", "Targets": [ { "Key": "aws:NoOpAutomationTag", "Values": [ "AWS-NoOpAutomationTarget-Value" ] } ], "ScheduleExpression": "cron(0 0 0/4 1/1 * ? *)", "LastExecutionDate": "2021-06-26T19:00:48.110000-07:00", "ApplyOnlyAtCronInterval": false } }`For more information, see [Editing and creating a new version of an association](https://docs.aws.amazon.com/systems-manager/latest/userguide/sysman-state-assoc-edit.html)in the*AWS Systems Manager User Guide*.- 
                    For API details, see [UpdateAssociation](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ssm/update-association.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `update-document-default-version`.

- **AWS CLI**
- 
            
                    **To update the default version of a document**The following `update-document-default-version`example updates the default version of a Systems Manager document.`aws ssm update-document-default-version \ --name``"Example"`\ --document-version`"2"`Output: `{ "Description": { "Name": "Example", "DefaultVersion": "2" } }`For more information, see [Writing SSM Document Content](https://docs.aws.amazon.com/systems-manager/latest/userguide/create-ssm-doc.html#writing-ssm-doc-content)in the*AWS Systems Manager User Guide*.- 
                    For API details, see [UpdateDocumentDefaultVersion](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ssm/update-document-default-version.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `update-document-metadata`.

- **AWS CLI**
- 
            
                    **Example: To approve the latest version of a change template**The following `update-document-metadata`provides an approval for the latest version of a change template that has been submitted for review.`aws ssm update-document-metadata \ --name``MyChangeManagerTemplate`\ --document-reviews '`Action=Approve,Comment=[{Type=Comment,Content=Approved!}]`'This command produces no output. For more information, see [Reviewing and approving or rejecting change templates](https://docs.aws.amazon.com/systems-manager/latest/userguide/change-templates-review.html)in the*AWS Systems Manager User Guide*.- 
                    For API details, see [UpdateDocumentMetadata](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ssm/update-document-metadata.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `update-document`.

- **AWS CLI**
- 
            
                    **To create a new version of a document**The following `update-document`example creates a new version of a document when run on a Windows computer. The document specified by`--document`must be in JSON format. Note that`file://`must be referenced followed by the path of the content file. Because of the`$`at the beginning of the`--document-version`parameter, On Windows you must surround the value with double quotes. On Linux, MacOS, or at a PowerShell prompt, you must surround the value with single quotes.**Windows version**:`aws ssm update-document \ --name``"RunShellScript"`\ --content`"file://RunShellScript.json"`\ --document-version`"$LATEST"`**Linux/Mac version**:`aws ssm update-document \ --name``"RunShellScript"`\ --content`"file://RunShellScript.json"`\ --document-version '`$LATEST`'Output: `{ "DocumentDescription": { "Status": "Updating", "Hash": "f775e5df4904c6fa46686c4722fae9de1950dace25cd9608ff8d622046b68d9b", "Name": "RunShellScript", "Parameters": [ { "Type": "StringList", "Name": "commands", "Description": "(Required) Specify a shell script or a command to run." } ], "DocumentType": "Command", "PlatformTypes": [ "Linux" ], "DocumentVersion": "2", "HashType": "Sha256", "CreatedDate": 1487899655.152, "Owner": "809632081692", "SchemaVersion": "2.0", "DefaultVersion": "1", "LatestVersion": "2", "Description": "Run an updated script" } }`- 
                    For API details, see [UpdateDocument](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ssm/update-document.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `update-maintenance-window-target`.

- **AWS CLI**
- 
            
                    **To update a maintenance window target**The following `update-maintenance-window-target`example updates only the name of a maintenance window target.`aws ssm update-maintenance-window-target \ --window-id``"mw-0c5ed765acEXAMPLE"`\ --window-target-id`"57e8344e-fe64-4023-8191-6bf05EXAMPLE"`\ --name`"NewName"`\ --no-replaceOutput: `{ "Description": "", "OwnerInformation": "", "WindowTargetId": "57e8344e-fe64-4023-8191-6bf05EXAMPLE", "WindowId": "mw-0c5ed765acEXAMPLE", "Targets": [ { "Values": [ "i-1234567890EXAMPLE" ], "Key": "InstanceIds" } ], "Name": "NewName" }`For more information, see [Update a Maintenance Window (AWS CLI)](https://docs.aws.amazon.com/systems-manager/latest/userguide/maintenance-windows-cli-tutorials-update.html)in the*AWS Systems Manager User Guide*.- 
                    For API details, see [UpdateMaintenanceWindowTarget](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ssm/update-maintenance-window-target.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `update-maintenance-window-task`.

- **AWS CLI**
- 
            
                    **To update a maintenance window task**The following `update-maintenance-window-task`example updates the service role for a maintenance window task.`aws ssm update-maintenance-window-task \ --window-id``"mw-0c5ed765acEXAMPLE"`\ --window-task-id`"23d3809e-9fbe-4ddf-b41a-b49d7EXAMPLE"`\ --service-role-arn`"arn:aws:iam::111222333444:role/aws-service-role/ssm.amazonaws.com/AWSServiceRoleForAmazonSSM"`Output: `{ "ServiceRoleArn": "arn:aws:iam::111222333444:role/aws-service-role/ssm.amazonaws.com/AWSServiceRoleForAmazonSSM", "MaxErrors": "1", "TaskArn": "AWS-UpdateEC2Config", "MaxConcurrency": "1", "WindowTaskId": "23d3809e-9fbe-4ddf-b41a-b49d7EXAMPLE", "TaskParameters": {}, "Priority": 1, "TaskInvocationParameters": { "RunCommand": { "TimeoutSeconds": 600, "Parameters": { "allowDowngrade": [ "false" ] } } }, "WindowId": "mw-0c5ed765acEXAMPLE", "Description": "UpdateEC2Config", "Targets": [ { "Values": [ "57e8344e-fe64-4023-8191-6bf05EXAMPLE" ], "Key": "WindowTargetIds" } ], "Name": "UpdateEC2Config" }`For more information, see [Update a Maintenance Window (AWS CLI)](https://docs.aws.amazon.com/systems-manager/latest/userguide/maintenance-windows-cli-tutorials-update.html)in the*AWS Systems Manager User Guide*.- 
                    For API details, see [UpdateMaintenanceWindowTask](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ssm/update-maintenance-window-task.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `update-maintenance-window`.

- **AWS CLI**
- 
            
                    **Example 1: To update a maintenance window**The following `update-maintenance-window`example updates the name of a maintenance window.`aws ssm update-maintenance-window \ --window-id``"mw-1a2b3c4d5e6f7g8h9"`\ --name`"My-Renamed-MW"`Output: `{ "Cutoff": 1, "Name": "My-Renamed-MW", "Schedule": "cron(0 16 ? * TUE *)", "Enabled": true, "AllowUnassociatedTargets": true, "WindowId": "mw-1a2b3c4d5e6f7g8h9", "Duration": 4 }`**Example 2: To disable a maintenance window**The following `update-maintenance-window`example disables a maintenance window.`aws ssm update-maintenance-window \ --window-id``"mw-1a2b3c4d5e6f7g8h9"`\ --no-enabled**Example 3: To enable a maintenance window**The following `update-maintenance-window`example enables a maintenance window.`aws ssm update-maintenance-window \ --window-id``"mw-1a2b3c4d5e6f7g8h9"`\ --enabledFor more information, see [Update a Maintenance Window (AWS CLI)](https://docs.aws.amazon.com/systems-manager/latest/userguide/maintenance-windows-cli-tutorials-update.html)in the*AWS Systems Manager User Guide*.- 
                    For API details, see [UpdateMaintenanceWindow](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ssm/update-maintenance-window.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `update-managed-instance-role`.

- **AWS CLI**
- 
            
                    **To update the IAM role of a managed instance**The following `update-managed-instance-role`example updates the IAM instance profile of a managed instance.`aws ssm update-managed-instance-role \ --instance-id``"mi-08ab247cdfEXAMPLE"`\ --iam-role`"ExampleRole"`This command produces no output. For more information, see [Step 4: Create an IAM Instance Profile for Systems Manager](https://docs.aws.amazon.com/systems-manager/latest/userguide/setup-instance-profile.html)in the*AWS Systems Manager User Guide*.- 
                    For API details, see [UpdateManagedInstanceRole](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ssm/update-managed-instance-role.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `update-ops-item`.

- **AWS CLI**
- 
            
                    **To update an OpsItem**The following `update-ops-item`example updates the description, priority, and category for an OpsItem. In addition, the command specifies an SNS topic where the notifications are sent when this OpsItem is edited or changed.`aws ssm update-ops-item \ --ops-item-id``"oi-287b5EXAMPLE"`\ --description`"Primary OpsItem for failover event 2020-01-01-fh398yf"`\ --priority`2`\ --category`"Security"`\ --notifications`"Arn=arn:aws:sns:us-east-2:111222333444:my-us-east-2-topic"`Output: `This command produces no output.`For more information, see [Working with OpsItems](https://docs.aws.amazon.com/systems-manager/latest/userguide/OpsCenter-working-with-OpsItems.html)in the*AWS Systems Manager User Guide*.- 
                    For API details, see [UpdateOpsItem](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ssm/update-ops-item.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `update-patch-baseline`.

- **AWS CLI**
- 
            
                    **Example 1: To update a patch baseline**The following `update-patch-baseline`example adds the specified two patches as rejected and one patch as approved to the specified patch baseline.`aws ssm update-patch-baseline \ --baseline-id``"pb-0123456789abcdef0"`\ --rejected-patches`"KB2032276"``"MS10-048"`\ --approved-patches`"KB2124261"`Output: `{ "BaselineId": "pb-0123456789abcdef0", "Name": "WindowsPatching", "OperatingSystem": "WINDOWS", "GlobalFilters": { "PatchFilters": [] }, "ApprovalRules": { "PatchRules": [ { "PatchFilterGroup": { "PatchFilters": [ { "Key": "PRODUCT", "Values": [ "WindowsServer2016" ] } ] }, "ComplianceLevel": "CRITICAL", "ApproveAfterDays": 0, "EnableNonSecurity": false } ] }, "ApprovedPatches": [ "KB2124261" ], "ApprovedPatchesComplianceLevel": "UNSPECIFIED", "ApprovedPatchesEnableNonSecurity": false, "RejectedPatches": [ "KB2032276", "MS10-048" ], "RejectedPatchesAction": "ALLOW_AS_DEPENDENCY", "CreatedDate": 1550244180.465, "ModifiedDate": 1550244180.465, "Description": "Patches for Windows Servers", "Sources": [] }`**Example 2: To rename a patch baseline**The following `update-patch-baseline`example renames the specified patch baseline.`aws ssm update-patch-baseline \ --baseline-id``"pb-0713accee01234567"`\ --name`"Windows-Server-2012-R2-Important-and-Critical-Security-Updates"`For more information, see Update or Delete a Patch Baseline <https://docs.aws.amazon.com/systems-manager/latest/userguide/patch-baseline-update-or-delete.html>`__ in the *AWS Systems Manager User Guide*.- 
                    For API details, see [UpdatePatchBaseline](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ssm/update-patch-baseline.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `update-resource-data-sync`.

- **AWS CLI**
- 
            
                    **To update a resource data sync**The following `update-resource-data-sync`example updates a SyncFromSource resource data sync.`aws ssm update-resource-data-sync \ --sync-name``exampleSync`\ --sync-type`SyncFromSource`\ --sync-source '`{"SourceType":"SingleAccountMultiRegions", "SourceRegions":["us-east-1", "us-west-2"]}`'This command produces no output. For more information, see [Setting Up Systems Manager Explorer to Display Data from Multiple Accounts and Regions](https://docs.aws.amazon.com/systems-manager/latest/userguide/Explorer-resource-data-sync.html)in the*AWS Systems Manager User Guide*.- 
                    For API details, see [UpdateResourceDataSync](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ssm/update-resource-data-sync.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `update-service-setting`.

- **AWS CLI**
- 
            
                    **To update the service setting for Parameter Store throughput**The following `update-service-setting`example updates the current service setting for Parameter Store throughput in the specified region to use increased throughput.`aws ssm update-service-setting \ --setting-id``arn:aws:ssm:us-east-1:123456789012:servicesetting/ssm/parameter-store/high-throughput-enabled`\ --setting-value`true`This command produces no output. For more information, see [Increasing Parameter Store Throughput](https://docs.aws.amazon.com/systems-manager/latest/userguide/parameter-store-throughput.html)in the*AWS Systems Manager User Guide*.- 
                    For API details, see [UpdateServiceSetting](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ssm/update-service-setting.html)in*AWS CLI Command Reference*.
 
-