# GuardDuty examples using AWS CLI - AWS Command Line Interface

**Source:** [https://docs.aws.amazon.com/cli/latest/userguide/cli_guardduty_code_examples.html](https://docs.aws.amazon.com/cli/latest/userguide/cli_guardduty_code_examples.html)

---

The following code examples show you how to perform actions and implement common scenarios by using the AWS Command Line Interface with GuardDuty.

*Actions* are code excerpts from larger programs and must be run in context. While actions show you how to call individual service functions, you can see actions in context in their related scenarios.

Each example includes a link to the complete source code, where you can find instructions on how to set up and run the code in context.

###### Topics

## Actions

    The following code example shows how to use `accept-invitation`.

- **AWS CLI**
- 
            
                    **To accept an invitation to become a GuardDuty member account in the current region**The following `accept-invitation`example shows how to accept an invitation to become a GuardDuty member account in the current region.`aws guardduty accept-invitation \ --detector-id``12abc34d567e8fa901bc2d34eexample`\ --master-id`123456789111`\ --invitation-id`d6b94fb03a66ff665f7db8764example`This command produces no output. For more information, see [Managing GuardDuty accounts by invitation](https://docs.aws.amazon.com/guardduty/latest/ug/guardduty_invitations.html)in the GuardDuty User Guide.- 
                    For API details, see [AcceptInvitation](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/guardduty/accept-invitation.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `archive-findings`.

- **AWS CLI**
- 
            
                    **To archive findings in the current region**This `archive-findings`example shows how to archive findings in the current region.`aws guardduty archive-findings \ --detector-id``12abc34d567e8fa901bc2d34eexample`\ --finding-ids`d6b94fb03a66ff665f7db8764example``3eb970e0de00c16ec14e6910fexample`This command produces no output. For more information, see [Creating suppression rules](https://docs.aws.amazon.com/guardduty/latest/ug/findings_suppression-rules-console.html)in the*GuardDuty User Guide*.- 
                    For API details, see [ArchiveFindings](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/guardduty/archive-findings.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `create-detector`.

- **AWS CLI**
- 
            
                    **To enable GuardDuty in the current region**This example shows how to create a new detector, which enables GuardDuty, in the current region.: `aws guardduty create-detector \ --enable`Output: `{ "DetectorId": "b6b992d6d2f48e64bc59180bfexample" }`For more information, see [Enable Amazon GuardDuty](https://docs.aws.amazon.com/guardduty/latest/ug/guardduty_settingup.html#guardduty_enable-gd)in the*GuardDuty User Guide*.- 
                    For API details, see [CreateDetector](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/guardduty/create-detector.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `create-filter`.

- **AWS CLI**
- 
            
                    **Example 1: To create a new filter in the current region**The following `create-filter`example creates a filter that matches all Portscan findings for instance created from a specific image. This does not suppress those findings.`aws guardduty create-filter \ --detector-id``b6b992d6d2f48e64bc59180bfexample`\ --name`myFilterExample`\ --finding-criteria '`{"Criterion": {"type": {"Eq": ["Recon:EC2/Portscan"]},"resource.instanceDetails.imageId": {"Eq": ["ami-0a7a207083example"]}}}`'Output: `{ "Name": "myFilterExample" }`For more information, see [Filtering GuardDuty findings](https://docs.aws.amazon.com/guardduty/latest/ug/guardduty_filter-findings.html)in the*GuardDuty User Guide*.**Example 2: To create a new filter and suppress findings in the current region**The following `create-filter`example creates a filter that matches all Portscan findings for instance created from a specific image. This filter archives those findings so that they do not appear in your current findings.`aws guardduty create-filter \ --detector-id``b6b992d6d2f48e64bc59180bfexample`\ --action`ARCHIVE`\ --name`myFilterSecondExample`\ --finding-criteria '`{"Criterion": {"type": {"Eq": ["Recon:EC2/Portscan"]},"resource.instanceDetails.imageId": {"Eq": ["ami-0a7a207083example"]}}}`'Output: `{ "Name": "myFilterSecondExample" }`For more information, see [Filtering GuardDuty findings](https://docs.aws.amazon.com/guardduty/latest/ug/guardduty_filter-findings.html)in the*GuardDuty User Guide*.- 
                    For API details, see [CreateFilter](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/guardduty/create-filter.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `create-ip-set`.

- **AWS CLI**
- 
            
                    **To create and activate a trusted IP set**The following `create-ip-set`example creates and activates a trusted IP set in the current Region.`aws guardduty create-ip-set \ --detector-id``12abc34d567e8fa901bc2d34eexample`\ --name`new-ip-set-example`\ --format`TXT`\ --location`s3://amzn-s3-demo-bucket/customtrustlist.csv`\ --activateOutput: `{ "IpSetId": "d4b94fc952d6912b8f3060768example" }`For more information, see [Working with Trusted IP Lists and Threat Lists](https://docs.aws.amazon.com/guardduty/latest/ug/guardduty_upload_lists.html)in the*GuardDuty User Guide*.- 
                    For API details, see [CreateIpSet](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/guardduty/create-ip-set.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `create-members`.

- **AWS CLI**
- 
            
                    **To associate a new member with your GuardDuty master account in the current region.**This example shows how to associate member accounts to be managed by the current account as the GuardDuty master. `aws guardduty create-members --detector-id``b6b992d6d2f48e64bc59180bfexample`\ --account-details`AccountId=111122223333,Email=first+member@example.com``AccountId=111111111111``,Email=another+member@example.com`Output: `{ "UnprocessedAccounts": [] }`For more information, see [Managing multiple accounts](https://docs.aws.amazon.com/guardduty/latest/ug/guardduty_accounts.html)in the GuardDuty User Guide.- 
                    For API details, see [CreateMembers](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/guardduty/create-members.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `create-publishing-destination`.

- **AWS CLI**
- 
            
                    **To create a publishing destination to export GuardDuty findings in the current region to.**The following `create-publishing-destination`example shows how to set up a publishing destination to export current (not archived) GuardDuty findings to keep track of historical findings data.`aws guardduty create-publishing-destination \ --detector-id``b6b992d6d2f48e64bc59180bfexample`\ --destination-type`S3`\ --destination-properties '`DestinationArn=arn:aws:s3:::amzn-s3-demo-bucket,KmsKeyArn=arn:aws:kms:us-west-1:111122223333:key/84cee9c5-dea1-401a-ab6d-e1de7example`'Output: `{ "DestinationId": "46b99823849e1bbc242dfbe3cexample" }`For more information, see [Exporting generated GuardDuty findings to Amazon S3 buckets](https://docs.aws.amazon.com/guardduty/latest/ug/guardduty_exportfindings.html)in the*GuardDuty User Guide*.- 
                    For API details, see [CreatePublishingDestination](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/guardduty/create-publishing-destination.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `create-sample-findings`.

- **AWS CLI**
- 
            
                    **To create sample GuardDuty findings in the current region.**This example shows how to create a sample finding of the provided types. `aws guardduty create-sample-findings \ --detector-id``b6b992d6d2f48e64bc59180bfexample`\ --finding-types`UnauthorizedAccess:EC2/TorClient``UnauthorizedAccess:EC2/TorRelay`This command produces no output. For more information, see [Sample findings](https://docs.aws.amazon.com/guardduty/latest/ug/sample_findings.html)in the*GuardDuty User Guide*.- 
                    For API details, see [CreateSampleFindings](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/guardduty/create-sample-findings.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `create-threat-intel-set`.

- **AWS CLI**
- 
            
                    **To create and activate a new threat intel set**The following `create-threat-intel-set`example creates and activates a threat intel set in the current Region.`aws guardduty create-threat-intel-set \ --detector-id``b6b992d6d2f48e64bc59180bfexample`\ --name`myThreatSet-example`\ --format`TXT`\ --location`s3://amzn-s3-demo-bucket/threatlist.csv`\ --activateOutput: `{ "ThreatIntelSetId": "20b9a4691aeb33506b808878cexample" }`For more information, see [Working with Trusted IP Lists and Threat Lists](https://docs.aws.amazon.com/guardduty/latest/ug/guardduty_upload_lists.html)in the*GuardDuty User Guide*.- 
                    For API details, see [CreateThreatIntelSet](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/guardduty/create-threat-intel-set.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `decline-invitations`.

- **AWS CLI**
- 
            
                    **To decline an invitation to have Guardduty managed by another account in the current region.**This example shows how to decline a membership invitation. `aws guardduty decline-invitations \ --account-ids``111122223333`Output: `{ "UnprocessedAccounts": [] }`For more information, see [Managing GuardDuty accounts by invitation](https://docs.aws.amazon.com/guardduty/latest/ug/guardduty_invitations.html)in the GuardDuty User Guide.- 
                    For API details, see [DeclineInvitations](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/guardduty/decline-invitations.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `delete-detector`.

- **AWS CLI**
- 
            
                    **To delete a detector, and disable GuardDuty, in the current region.**This example shows how to delete a detector, if successful, this will disable GuardDuty in the region associated with that detector. `aws guardduty delete-detector \ --detector-id``b6b992d6d2f48e64bc59180bfexample`This command produces no output. For more information, see [Suspending or disabling GuardDuty](https://docs.aws.amazon.com/guardduty/latest/ug/guardduty_suspend-disable.html)in the*GuardDuty User Guide*.- 
                    For API details, see [DeleteDetector](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/guardduty/delete-detector.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `delete-filter`.

- **AWS CLI**
- 
            
                    **To delete an existing filter in the current region**This example shows how to create delete a filter. `aws guardduty delete-filter \ --detector-id``b6b992d6d2f48e64bc59180bfexample`\ --filter-name`byebyeFilter`This command produces no output. For more information, see [Filtering findings](https://docs.aws.amazon.com/guardduty/latest/ug/guardduty_filter-findings.html)in the GuardDuty User Guide.- 
                    For API details, see [DeleteFilter](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/guardduty/delete-filter.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `disable-organization-admin-account`.

- **AWS CLI**
- 
            
                    **To remove an account as the delegated administrator for GuardDuty within your organization**This example shows how to remove an account as the delegated administrator for GuardDuty. `aws guardduty disable-organization-admin-account \ --admin-account-id``111122223333`This command produces no output. For more information, see [Managing accounts with AWS organizations](https://docs.aws.amazon.com/guardduty/latest/ug/guardduty_organizations.html)in the*GuardDuty User Guide*.- 
                    For API details, see [DisableOrganizationAdminAccount](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/guardduty/disable-organization-admin-account.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `disassociate-from-master-account`.

- **AWS CLI**
- 
            
                    **To disassociate from your current administrator account in the current region**The following `disassociate-from-master-account`example disassociates your account from the current GuardDuty administrator account in the current AWS region.`aws guardduty disassociate-from-master-account \ --detector-id``d4b040365221be2b54a6264dcexample`This command produces no output. For more information, see [Understanding the relationship between GuardDuty administrator account and member accounts](https://docs.aws.amazon.com/guardduty/latest/ug/administrator_member_relationships.html)in the*GuardDuty User Guide*.- 
                    For API details, see [DisassociateFromMasterAccount](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/guardduty/disassociate-from-master-account.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `get-detector`.

- **AWS CLI**
- 
            
                    **To retrieve details of a specific detector**The following `get-detector`example displays the configurations details of the specified detector.`aws guardduty get-detector \ --detector-id``12abc34d567e8fa901bc2d34eexample`Output: `{ "Status": "ENABLED", "ServiceRole": "arn:aws:iam::111122223333:role/aws-service-role/guardduty.amazonaws.com/AWSServiceRoleForAmazonGuardDuty", "Tags": {}, "FindingPublishingFrequency": "SIX_HOURS", "UpdatedAt": "2018-11-07T03:24:22.938Z", "CreatedAt": "2017-12-22T22:51:31.940Z" }`For more information, see [Concepts and Terminology](https://docs.aws.amazon.com/guardduty/latest/ug/guardduty_concepts.html)in the GuardDuty User Guide.- 
                    For API details, see [GetDetector](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/guardduty/get-detector.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `get-findings`.

- **AWS CLI**
- 
            
                    **Example 1: To retrieve the details of a specific finding**The following `get-findings`example retrieves the full JSON finding details of the specified finding.`aws guardduty get-findings \ --detector-id``12abc34d567e8fa901bc2d34eexample`\ --finding-id`1ab92989eaf0e742df4a014d5example`Output: `{ "Findings": [ { "Resource": { "ResourceType": "AccessKey", "AccessKeyDetails": { "UserName": "testuser", "UserType": "IAMUser", "PrincipalId": "AIDACKCEVSQ6C2EXAMPLE", "AccessKeyId": "ASIASZ4SI7REEEXAMPLE" } }, "Description": "APIs commonly used to discover the users, groups, policies and permissions in an account, was invoked by IAM principal testuser under unusual circumstances. Such activity is not typically seen from this principal.", "Service": { "Count": 5, "Archived": false, "ServiceName": "guardduty", "EventFirstSeen": "2020-05-26T22:02:24Z", "ResourceRole": "TARGET", "EventLastSeen": "2020-05-26T22:33:55Z", "DetectorId": "d4b040365221be2b54a6264dcexample", "Action": { "ActionType": "AWS_API_CALL", "AwsApiCallAction": { "RemoteIpDetails": { "GeoLocation": { "Lat": 51.5164, "Lon": -0.093 }, "City": { "CityName": "London" }, "IpAddressV4": "52.94.36.7", "Organization": { "Org": "Amazon.com", "Isp": "Amazon.com", "Asn": "16509", "AsnOrg": "AMAZON-02" }, "Country": { "CountryName": "United Kingdom" } }, "Api": "ListPolicyVersions", "ServiceName": "iam.amazonaws.com", "CallerType": "Remote IP" } } }, "Title": "Unusual user permission reconnaissance activity by testuser.", "Type": "Recon:IAMUser/UserPermissions", "Region": "us-east-1", "Partition": "aws", "Arn": "arn:aws:guardduty:us-east-1:111122223333:detector/d4b040365221be2b54a6264dcexample/finding/1ab92989eaf0e742df4a014d5example", "UpdatedAt": "2020-05-26T22:55:21.703Z", "SchemaVersion": "2.0", "Severity": 5, "Id": "1ab92989eaf0e742df4a014d5example", "CreatedAt": "2020-05-26T22:21:48.385Z", "AccountId": "111122223333" } ] }`For more information, see [Findings](https://docs.aws.amazon.com/guardduty/latest/ug/guardduty_findings.html)in the GuardDuty User Guide.- 
                    For API details, see [GetFindings](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/guardduty/get-findings.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `get-ip-set`.

- **AWS CLI**
- 
            
                    **To list get details on a specified trusted IP set**The following `get-ip-set`example shows the status and details of the specified trusted IP set.`aws guardduty get-ip-set \ --detector-id``12abc34d567e8fa901bc2d34eexample`\ --ip-set-id`d4b94fc952d6912b8f3060768example`Output: `{ "Status": "ACTIVE", "Location": "s3://amzn-s3-demo-bucket.s3-us-west-2.amazonaws.com/customlist.csv", "Tags": {}, "Format": "TXT", "Name": "test-ip-set-example" }`For more information, see [Working with Trusted IP Lists and Threat Lists](https://docs.aws.amazon.com/guardduty/latest/ug/guardduty_upload_lists.html)in the*GuardDuty User Guide*.- 
                    For API details, see [GetIpSet](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/guardduty/get-ip-set.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `get-master-account`.

- **AWS CLI**
- 
            
                    **To retrieve details about your master account in the current region**The following `get-master-account`example displays the status and details of the master account associated with your detector in the current region.`aws guardduty get-master-account \ --detector-id``12abc34d567e8fa901bc2d34eexample`Output: `{ "Master": { "InvitationId": "04b94d9704854a73f94e061e8example", "InvitedAt": "2020-06-09T22:23:04.970Z", "RelationshipStatus": "Enabled", "AccountId": "111122223333" } }`For more information, see [Understanding the relationship between GuardDuty administrator account and member account](https://docs.aws.amazon.com/guardduty/latest/ug/administrator_member_relationships.html)in the*GuardDuty User Guide*.- 
                    For API details, see [GetMasterAccount](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/guardduty/get-master-account.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `list-detectors`.

- **AWS CLI**
- 
            
                    **To list the available detectors in the current region**The following `list-detectors`example lists the available detectors in your current AWS region.`aws guardduty list-detectors`Output: `{ "DetectorIds": [ "12abc34d567e8fa901bc2d34eexample" ] }`For more information, see [Concepts and Terminology](https://docs.aws.amazon.com/guardduty/latest/ug/guardduty_concepts.html)in the GuardDuty User Guide.- 
                    For API details, see [ListDetectors](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/guardduty/list-detectors.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `list-findings`.

- **AWS CLI**
- 
            
                    **Example 1: To list all findings for the current region**The following `list-findings`example displays a list of all findingIds for the current region sorted by severity from highest to lowest.`aws guardduty list-findings \ --detector-id``12abc34d567e8fa901bc2d34eexample`\ --sort-criteria '`{"AttributeName": "severity","OrderBy":"DESC"}`'Output: `{ "FindingIds": [ "04b8ab50fd29c64fc771b232dexample", "5ab8ab50fd21373735c826d3aexample", "90b93de7aba69107f05bbe60bexample", ... ] }`For more information, see [Findings](https://docs.aws.amazon.com/guardduty/latest/ug/guardduty_findings.html)in the GuardDuty User Guide.**Example 2: To list findings for the current region matching a specific finding criteria**The following `list-findings`example displays a list of all findingIds that match a specified finding type.`aws guardduty list-findings \ --detector-id``12abc34d567e8fa901bc2d34eexample`\ --finding-criteria '`{"Criterion":{"type": {"Eq":["UnauthorizedAccess:EC2/SSHBruteForce"]}}}`'Output: `{ "FindingIds": [ "90b93de7aba69107f05bbe60bexample", "6eb9430d7023d30774d6f05e3example", "2eb91a2d060ac9a21963a5848example", "44b8ab50fd2b0039a9e48f570example", "9eb8ab4cd2b7e5b66ba4f5e96example", "e0b8ab3a38e9b0312cc390ceeexample" ] }`For more information, see [Findings](https://docs.aws.amazon.com/guardduty/latest/ug/guardduty_findings.html)in the GuardDuty User Guide.**Example 3: To list findings for the current region matching a specific set of finding criteria defined within a JSON file**The following `list-findings`example displays a list of all findingIds that are not archived, and involve the IAM user named "testuser", as specified in a JSON file.`aws guardduty list-findings \ --detector-id``12abc34d567e8fa901bc2d34eexample`\ --finding-criteria`file://myfile.json`Contents of `myfile.json`:`{"Criterion": { "resource.accessKeyDetails.userName":{ "Eq":[ "testuser" ] }, "service.archived": { "Eq": [ "false" ] } } }`Output: `{ "FindingIds": [ "1ab92989eaf0e742df4a014d5example" ] }`For more information, see [Findings](https://docs.aws.amazon.com/guardduty/latest/ug/guardduty_findings.html)in the GuardDuty User Guide.- 
                    For API details, see [ListFindings](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/guardduty/list-findings.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `list-invitations`.

- **AWS CLI**
- 
            
                    **To list details on your invitations to become a member account in the current region**The following `list-invitations`example lists details and statuses on your invitations to become a GuardDuty member account in the current region.`aws guardduty list-invitations`Output: `{ "Invitations": [ { "InvitationId": "d6b94fb03a66ff665f7db8764example", "InvitedAt": "2020-06-10T17:56:38.221Z", "RelationshipStatus": "Invited", "AccountId": "123456789111" } ] }`For more information, see [Managing GuardDuty Accounts by Invitation](https://docs.aws.amazon.com/guardduty/latest/ug/guardduty_invitations.html)in the GuardDuty User Guide.- 
                    For API details, see [ListInvitations](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/guardduty/list-invitations.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `list-ip-sets`.

- **AWS CLI**
- 
            
                    **To list trusted IP sets in the current region**The following `list-ip-sets`example lists the trusted IP sets in your current AWS region.`aws guardduty list-ip-sets \ --detector-id``12abc34d567e8fa901bc2d34eexample`Output: `{ "IpSetIds": [ "d4b94fc952d6912b8f3060768example" ] }`For more information, see [Working with Trusted IP Lists and Threat Lists](https://docs.aws.amazon.com/guardduty/latest/ug/guardduty_upload_lists.html)in the GuardDuty User Guide.- 
                    For API details, see [ListIpSets](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/guardduty/list-ip-sets.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `list-members`.

- **AWS CLI**
- 
            
                    **Example 1: To list only current members in the current Region**The following `list-members`example lists and provides details of only current member accounts associated with the GuardDuty administrator account, in the current region.`aws guardduty list-members \ --detector-id``12abc34d567e8fa901bc2d34eexample`\ --only-associated="true"Output: `{ "Members": [ { "RelationshipStatus": "Enabled", "InvitedAt": "2020-06-09T22:49:00.910Z", "MasterId": "111122223333", "DetectorId": "7ab8b2f61b256c87f793f6a86example", "UpdatedAt": "2020-06-09T23:08:22.512Z", "Email": "your+member@example.com", "AccountId": "123456789012" } ] }`For more information, see [Understanding the relationship between GuardDuty administrator account and member accounts](https://docs.aws.amazon.com/guardduty/latest/ug/administrator_member_relationships.html)in the*GuardDuty User Guide*.**Example 2: To list all the members in the current Region**The following `list-members`example lists and provides details of all the member accounts, including those who have been disassociated or have not yet accepted the invite from the GuardDuty administrator, in the current region.`aws guardduty list-members \ --detector-id``12abc34d567e8fa901bc2d34eexample`\ --only-associated="false"Output: `{ "Members": [ { "RelationshipStatus": "Enabled", "InvitedAt": "2020-06-09T22:49:00.910Z", "MasterId": "111122223333", "DetectorId": "7ab8b2f61b256c87f793f6a86example", "UpdatedAt": "2020-06-09T23:08:22.512Z", "Email": "your+other+member@example.com", "AccountId": "555555555555" } ] }`For more information, see [Understanding the relationship between GuardDuty administrator account and member accounts](https://docs.aws.amazon.com/guardduty/latest/ug/administrator_member_relationships.html)in the*GuardDuty User Guide*.- 
                    For API details, see [ListMembers](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/guardduty/list-members.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `update-detector`.

- **AWS CLI**
- 
            
                    **Example 1: To enable runtime monitoring in GuardDuty**The following `update-detector`example enables runtime monitoring without additional configuration.`aws guardduty update-detector \ --detector-id``12abc34d567e8fa901bc2d34eexample`\ --features '`Name=RUNTIME_MONITORING,Status=ENABLED`'This command produces no output. For more information, see [Runtime monitoring](https://docs.aws.amazon.com/guardduty/latest/ug/runtime-monitoring.html)in the*GuardDuty User Guide*.**Example 2: To enable runtime monitoring with additional configuration**The following `update-detector`example enables runtime monitoring with additional configuration for EC2, ECS Fargate, and EKS.`aws guardduty update-detector \ --detector-id``12abc34d567e8fa901bc2d34eexample`\ --features '`Name=RUNTIME_MONITORING,Status=ENABLED,AdditionalConfiguration=[{Name=EC2_AGENT_MANAGEMENT,Status=ENABLED},{Name=ECS_FARGATE_AGENT_MANAGEMENT,Status=ENABLED},{Name=EKS_ADDON_MANAGEMENT,Status=ENABLED}]`'This command produces no output. For more information, see [Runtime monitoring](https://docs.aws.amazon.com/guardduty/latest/ug/runtime-monitoring.html)in the*GuardDuty User Guide*.- 
                    For API details, see [UpdateDetector](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/guardduty/update-detector.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `update-ip-set`.

- **AWS CLI**
- 
            
                    **To update a trusted IP set**The following `update-ip-set`example shows how to update the details of a trusted IP set.`aws guardduty update-ip-set \ --detector-id``12abc34d567e8fa901bc2d34eexample`\ --ip-set-id`d4b94fc952d6912b8f3060768example`\ --location`https://amzn-s3-demo-bucket.s3-us-west-2.amazonaws.com/customtrustlist2.csv`This command produces no output. For more information, see [Working with Trusted IP Lists and Threat Lists](https://docs.aws.amazon.com/guardduty/latest/ug/guardduty_upload_lists.html)in the*GuardDuty User Guide*.- 
                    For API details, see [UpdateIpSet](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/guardduty/update-ip-set.html)in*AWS CLI Command Reference*.
 
-