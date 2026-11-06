# WorkDocs examples using AWS CLI - AWS Command Line Interface

**Source:** [https://docs.aws.amazon.com/cli/latest/userguide/cli_workdocs_code_examples.html](https://docs.aws.amazon.com/cli/latest/userguide/cli_workdocs_code_examples.html)

---

The following code examples show you how to perform actions and implement common scenarios by using the AWS Command Line Interface with WorkDocs.

*Actions* are code excerpts from larger programs and must be run in context. While actions show you how to call individual service functions, you can see actions in context in their related scenarios.

Each example includes a link to the complete source code, where you can find instructions on how to set up and run the code in context.

###### Topics

## Actions

    The following code example shows how to use `abort-document-version-upload`.

- **AWS CLI**
- 
            
                    **To stop a document version upload**This example stops a previously initiated document version upload. Command: `aws workdocs abort-document-version-upload --document-id``feaba64d4efdf271c2521b60a2a44a8f057e84beaabbe22f01267313209835f2`--version-id`1536773972914-ddb67663e782e7ce8455ebc962217cf9f9e47b5a9a702e5c84dcccd417da9313`Output: `None`- 
                    For API details, see [AbortDocumentVersionUpload](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/workdocs/abort-document-version-upload.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `activate-user`.

- **AWS CLI**
- 
            
                    **To activate a user**This example activates an inactive user. Command: `aws workdocs activate-user --user-id``"S-1-1-11-1111111111-2222222222-3333333333-3333&d-926726012c"`Output: `{ "User": { "Id": "S-1-1-11-1111111111-2222222222-3333333333-3333&d-926726012c", "Username": "exampleUser", "EmailAddress": "exampleUser@site.awsapps.com", "GivenName": "Example", "Surname": "User", "OrganizationId": "d-926726012c", "RootFolderId": "75f67c183aa1217409ac87576a45c03a5df5e6d8c51c35c01669970538e86cd0", "RecycleBinFolderId": "642b7dd3e60b14204534f3df7b1959e01b5d170f8c2707f410e40a8149120a57", "Status": "ACTIVE", "Type": "MINIMALUSER", "CreatedTimestamp": 1521226107.747, "ModifiedTimestamp": 1525297406.462, "Storage": { "StorageUtilizedInBytes": 0, "StorageRule": { "StorageAllocatedInBytes": 0, "StorageType": "QUOTA" } } } }`- 
                    For API details, see [ActivateUser](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/workdocs/activate-user.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `add-resource-permissions`.

- **AWS CLI**
- 
            
                    **To add permissions for a resource**This example adds permissions to the resource for the specified principals. Command: `aws workdocs add-resource-permissions --resource-id``d90d93c1fe44bad0c8471e973ebaab339090401a95e777cffa58e977d2983b65`--principals`Id=anonymous,Type=ANONYMOUS,Role=VIEWER`Output: `{ "ShareResults": [ { "PrincipalId": "anonymous", "Role": "VIEWER", "Status": "SUCCESS", "ShareId": "d90d93c1fe44bad0c8471e973ebaab339090401a95e777cffa58e977d2983b65", "StatusMessage": "" } ] }`- 
                    For API details, see [AddResourcePermissions](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/workdocs/add-resource-permissions.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `create-comment`.

- **AWS CLI**
- 
            
                    **To add a new comment**This example adds a new comment to the specified document version. Command: `aws workdocs create-comment --document-id``15df51e0335cfcc6a2e4de9dd8be9f22ee40545ad9176f54758dcf903be982d3`--version-id`1521672507741-9f7df0ea5dd0b121c4f3564a0c7c0b4da95cd12c635d3c442af337a88e297920`--text`"This is a comment."`Output: `{ "Comment": { "CommentId": "1534799058197-c7f5c84de9115875bbca93e0367bbebac609541d461636b760849b88b1609dd5", "ThreadId": "1534799058197-c7f5c84de9115875bbca93e0367bbebac609541d461636b760849b88b1609dd5", "Text": "This is a comment.", "Contributor": { "Id": "arn:aws:iam::123456789123:user/exampleUser", "Username": "exampleUser", "GivenName": "Example", "Surname": "User", "Status": "ACTIVE" }, "CreatedTimestamp": 1534799058.197, "Status": "PUBLISHED", "Visibility": "PUBLIC" } }`- 
                    For API details, see [CreateComment](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/workdocs/create-comment.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `create-custom-metadata`.

- **AWS CLI**
- 
            
                    **To create custom metadata**This example creates custom metadata for the specified document. Command: `aws workdocs create-custom-metadata --resource-id``d90d93c1fe44bad0c8471e973ebaab339090401a95e777cffa58e977d2983b65`--custom-metadata`KeyName1=example,KeyName2=example2`Output: `None`- 
                    For API details, see [CreateCustomMetadata](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/workdocs/create-custom-metadata.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `create-folder`.

- **AWS CLI**
- 
            
                    **To create a folder**This example creates a folder. Command: `aws workdocs create-folder --name``documents`--parent-folder-id`1ece93e5fe75315c7407c4967918b4fd9da87ddb2a588e67b7fdaf4a98fde678`Output: `{ "Metadata": { "Id": "50893c0af679524d1a0e0651130ed6d073e1a05f95bd12c42dcde5d35634ed08", "Name": "documents", "CreatorId": "S-1-1-11-1111111111-2222222222-3333333333-3333&d-926726012c", "ParentFolderId": "1ece93e5fe75315c7407c4967918b4fd9da87ddb2a588e67b7fdaf4a98fde678", "CreatedTimestamp": 1534450467.622, "ModifiedTimestamp": 1534450467.622, "ResourceState": "ACTIVE", "Signature": "", "Size": 0, "LatestVersionSize": 0 } }`- 
                    For API details, see [CreateFolder](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/workdocs/create-folder.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `create-labels`.

- **AWS CLI**
- 
            
                    **To create labels**This example creates a series of labels for a document. Command: `aws workdocs create-labels --resource-id``d90d93c1fe44bad0c8471e973ebaab339090401a95e777cffa58e977d2983b65`--labels`"documents"``"examples"``"my_documents"`Output: `None`- 
                    For API details, see [CreateLabels](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/workdocs/create-labels.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `create-notification-subscription`.

- **AWS CLI**
- 
            
                    **To create a notification subscription**The following `create-notification-subscription`example configures a notification subscription for the specified Amazon WorkDocs organization.`aws workdocs create-notification-subscription \ --organization-id``d-123456789c`\ --protocol`HTTPS`\ --subscription-type`ALL`\ --notification-endpoint`"https://example.com/example"`Output: `{ "Subscription": { "SubscriptionId": "123ab4c5-678d-901e-f23g-45h6789j0123", "EndPoint": "https://example.com/example", "Protocol": "HTTPS" } }`For more information, see [Subscribe to Notifications](https://docs.aws.amazon.com/workdocs/latest/developerguide/subscribe-notifications.html)in the*Amazon WorkDocs Developer Guide*.- 
                    For API details, see [CreateNotificationSubscription](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/workdocs/create-notification-subscription.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `create-user`.

- **AWS CLI**
- 
            
                    **To create a new user**This example creates a new user in a Simple AD or Microsoft AD directory. Command: `aws workdocs create-user --organization-id``d-926726012c`--username`exampleUser2`--email-address`exampleUser2@site.awsapps.com`--given-name`example2Name`--surname`example2Surname`--password`examplePa$$w0rd`Output: `{ "User": { "Id": "S-1-1-11-1111111111-2222222222-3333333333-3333&d-926726012c", "Username": "exampleUser2", "EmailAddress": "exampleUser2@site.awsapps.com", "GivenName": "example2Name", "Surname": "example2Surname", "OrganizationId": "d-926726012c", "RootFolderId": "35b886cb17198cbd547655e58b025dff0cf34aaed638be52009567e23dc67390", "RecycleBinFolderId": "9858c3e9ed4c2460dde9aadb4c69fde998070dd46e5e985bd08ec6169ea249ff", "Status": "ACTIVE", "Type": "MINIMALUSER", "CreatedTimestamp": 1535478836.584, "ModifiedTimestamp": 1535478836.584, "Storage": { "StorageUtilizedInBytes": 0, "StorageRule": { "StorageAllocatedInBytes": 0, "StorageType": "QUOTA" } } } }`- 
                    For API details, see [CreateUser](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/workdocs/create-user.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `deactivate-user`.

- **AWS CLI**
- 
            
                    **To deactivate a user**This example deactivates an active user. Command: `aws workdocs deactivate-user --user-id``"S-1-1-11-1111111111-2222222222-3333333333-3333&d-926726012c"`Output: `None`- 
                    For API details, see [DeactivateUser](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/workdocs/deactivate-user.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `delete-comment`.

- **AWS CLI**
- 
            
                    **To delete a specified comment from a document version**This example deletes the specified comment from the specified document version. Command: `aws workdocs delete-comment --document-id``15df51e0335cfcc6a2e4de9dd8be9f22ee40545ad9176f54758dcf903be982d3`--version-id`1521672507741-9f7df0ea5dd0b121c4f3564a0c7c0b4da95cd12c635d3c442af337a88e297920`--comment-id`1534799058197-c7f5c84de9115875bbca93e0367bbebac609541d461636b760849b88b1609dd5`Output: `None`- 
                    For API details, see [DeleteComment](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/workdocs/delete-comment.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `delete-custom-metadata`.

- **AWS CLI**
- 
            
                    **To delete custom metadata from a resource**This example deletes all custom metadata from the specified resource. Command: `aws workdocs delete-custom-metadata --resource-id``d90d93c1fe44bad0c8471e973ebaab339090401a95e777cffa58e977d2983b65`--delete-allOutput: `None`- 
                    For API details, see [DeleteCustomMetadata](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/workdocs/delete-custom-metadata.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `delete-document`.

- **AWS CLI**
- 
            
                    **To delete a document**This example deletes the specified document. Command: `aws workdocs delete-document --document-id``b83ed5e5b167b65ef69de9d597627ff1a0d4f07a45e67f1fab7d26b54427de0a`Output: `None`- 
                    For API details, see [DeleteDocument](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/workdocs/delete-document.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `delete-folder-contents`.

- **AWS CLI**
- 
            
                    **To delete the contents of a folder**This example deletes the contents of the specified folder. Command: `aws workdocs delete-folder-contents --folder-id``26fa8aa4ba2071447c194f7b150b07149dbdb9e1c8a301872dcd93a4735ce65d`Output: `None`- 
                    For API details, see [DeleteFolderContents](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/workdocs/delete-folder-contents.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `delete-folder`.

- **AWS CLI**
- 
            
                    **To delete a folder**This example deletes the specified folder. Command: `aws workdocs delete-folder --folder-id``26fa8aa4ba2071447c194f7b150b07149dbdb9e1c8a301872dcd93a4735ce65d`Output: `None`- 
                    For API details, see [DeleteFolder](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/workdocs/delete-folder.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `delete-labels`.

- **AWS CLI**
- 
            
                    **To delete labels**This example deletes the specified labels from a document. Command: `aws workdocs delete-labels --resource-id``d90d93c1fe44bad0c8471e973ebaab339090401a95e777cffa58e977d2983b65`--labels`"documents"``"examples"`Output: `None`- 
                    For API details, see [DeleteLabels](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/workdocs/delete-labels.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `delete-notification-subscription`.

- **AWS CLI**
- 
            
                    **To delete a notification subscription**The following `delete-notification-subscription`example deletes the specified notification subscription.`aws workdocs delete-notification-subscription \ --subscription-id``123ab4c5-678d-901e-f23g-45h6789j0123`\ --organization-id`d-123456789c`This command produces no output. For more information, see [Subscribe to Notifications](https://docs.aws.amazon.com/workdocs/latest/developerguide/subscribe-notifications.html)in the*Amazon WorkDocs Developer Guide*.- 
                    For API details, see [DeleteNotificationSubscription](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/workdocs/delete-notification-subscription.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `delete-user`.

- **AWS CLI**
- 
            
                    **To delete a user**This example deletes a user. Command: `aws workdocs delete-user --user-id``"S-1-1-11-1111111111-2222222222-3333333333-3333&d-926726012c"`Output: `None`- 
                    For API details, see [DeleteUser](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/workdocs/delete-user.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `describe-activities`.

- **AWS CLI**
- 
            
                    **To get a list of user activities**This example returns a list of the latest user activities for the specified organization, with a limit set for the latest two activities. Command: `aws workdocs describe-activities --organization-id``d-926726012c`--limit`2`Output: `{ "UserActivities": [ { "Type": "DOCUMENT_VERSION_DOWNLOADED", "TimeStamp": 1534800122.17, "Initiator": { "Id": "arn:aws:iam::123456789123:user/exampleUser" }, "ResourceMetadata": { "Type": "document", "Name": "updatedDoc", "Id": "15df51e0335cfcc6a2e4de9dd8be9f22ee40545ad9176f54758dcf903be982d3", "Owner": { "Id": "S-1-1-11-1111111111-2222222222-3333333333-3333&d-926726012c", "GivenName": "exampleName", "Surname": "exampleSurname" } } }, { "Type": "DOCUMENT_VERSION_VIEWED", "TimeStamp": 1534799079.207, "Initiator": { "Id": "S-1-1-11-1111111111-2222222222-3333333333-3333&d-926726012c", "GivenName": "exampleName", "Surname": "exampleSurname" }, "ResourceMetadata": { "Type": "document", "Name": "updatedDoc", "Id": "15df51e0335cfcc6a2e4de9dd8be9f22ee40545ad9176f54758dcf903be982d3", "Owner": { "Id": "S-1-1-11-1111111111-2222222222-3333333333-3333&d-926726012c", "GivenName": "exampleName", "Surname": "exampleSurname" } } } ], "Marker": "DnF1ZXJ5VGhlbkZldGNoAgAAAAAAAAS7FmlTaU1OdlFTU1h1UU00VVFIbDlRWHcAAAAAAAAJTRY3bWh5eUgzaVF1ZXN2RUE5Wm8tTTdR" }`- 
                    For API details, see [DescribeActivities](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/workdocs/describe-activities.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `describe-comments`.

- **AWS CLI**
- 
            
                    **To list all comments for a specified document version**This example lists all the comments for the specified document version. Command: `aws workdocs describe-comments --document-id``15df51e0335cfcc6a2e4de9dd8be9f22ee40545ad9176f54758dcf903be982d3`--version-id`1521672507741-9f7df0ea5dd0b121c4f3564a0c7c0b4da95cd12c635d3c442af337a88e297920`Output: `{ "Comments": [ { "CommentId": "1534799058197-c7f5c84de9115875bbca93e0367bbebac609541d461636b760849b88b1609dd5", "ThreadId": "1534799058197-c7f5c84de9115875bbca93e0367bbebac609541d461636b760849b88b1609dd5", "Text": "This is a comment.", "Contributor": { "Username": "arn:aws:iam::123456789123:user/exampleUser", "Type": "USER" }, "CreatedTimestamp": 1534799058.197, "Status": "PUBLISHED", "Visibility": "PUBLIC" } ] }`- 
                    For API details, see [DescribeComments](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/workdocs/describe-comments.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `describe-document-versions`.

- **AWS CLI**
- 
            
                    **To retrieve a document's versions**This example retrieves the document versions for the specified document, including initialized versions and a URL for the source document. Command: `aws workdocs describe-document-versions --document-id``d90d93c1fe44bad0c8471e973ebaab339090401a95e777cffa58e977d2983b65`--fields`SOURCE`Output: `{ "DocumentVersions": [ { "Id": "1534452029587-15e129dfc187505c407588df255be83de2920d733859f1d2762411d22a83e3ef", "Name": "exampleDoc.docx", "ContentType": "application/vnd.openxmlformats-officedocument.wordprocessingml.document", "Size": 13922, "Signature": "1a23456b78901c23d4ef56gh7EXAMPLE", "Status": "ACTIVE", "CreatedTimestamp": 1534452029.587, "ModifiedTimestamp": 1534452029.849, "CreatorId": "S-1-1-11-1111111111-2222222222-3333333333-3333&d-926726012c", "Source": { "ORIGINAL": "https://gb-us-west-2-prod-doc-source.s3.us-west-2.amazonaws.com/d90d93c1fe44bad0c8471e973ebaab339090401a95e777cffa58e977d2983b65/1534452029587-15e129dfc187505c407588df255be83de2920d733859f1d2762411d22a83e3ef?response-content-disposition=attachment%3B%20filename%2A%3DUTF-8%27%27exampleDoc29.docx&X-Amz-Algorithm=AWS1-ABCD-EFG234&X-Amz-Date=20180816T204149Z&X-Amz-SignedHeaders=host&X-Amz-Expires=900&X-Amz-Credential=AKIAIOSFODNN7EXAMPLE%2F20180816%2Fus-west-2%2Fs3%2Faws1_request&X-Amz-Signature=01Ab2c34d567e8f90123g456hi78j901k2345678l901234mno56pqr78EXAMPLE" } }, { "Id": "1529005196082-bb75fa19abc287699cb07147f75816dce43a53a10f28dc001bf61ef2fab01c59", "Name": "exampleDoc.pdf", "ContentType": "application/pdf", "Size": 425916, "Signature": "1a23456b78901c23d4ef56gh7EXAMPLE", "Status": "ACTIVE", "CreatedTimestamp": 1529005196.082, "ModifiedTimestamp": 1529005196.796, "CreatorId": "S-1-1-11-1111111111-2222222222-3333333333-3333&d-926726012c", "Source": { "ORIGINAL": "https://gb-us-west-2-prod-doc-source.s3.us-west-2.amazonaws.com/d90d93c1fe44bad0c8471e973ebaab339090401a95e777cffa58e977d2983b65/1529005196082-bb75fa19abc287699cb07147f75816dce43a53a10f28dc001bf61ef2fab01c59?response-content-disposition=attachment%3B%20filename%2A%3DUTF-8%27%27exampleDoc29.pdf&X-Amz-Algorithm=AWS1-ABCD-EFG234&X-Amz-Date=20180816T204149Z&X-Amz-SignedHeaders=host&X-Amz-Expires=900&X-Amz-Credential=AKIAIOSFODNN7EXAMPLE%2F20180816%2Fus-west-2%2Fs3%2Faws1_request&X-Amz-Signature=01Ab2c34d567e8f90123g456hi78j901k2345678l901234mno56pqr78EXAMPLE" } } ] }`- 
                    For API details, see [DescribeDocumentVersions](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/workdocs/describe-document-versions.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `describe-folder-contents`.

- **AWS CLI**
- 
            
                    **To describe the contents of a folder**This example describes all the active contents of the specified folder, including its documents and subfolders, sorted by date in ascending order. Command: `aws workdocs describe-folder-contents --folder-id``1ece93e5fe75315c7407c4967918b4fd9da87ddb2a588e67b7fdaf4a98fde678`--sort`DATE`--order`ASCENDING`--type`ALL`Output: `{ "Folders": [ { "Id": "50893c0af679524d1a0e0651130ed6d073e1a05f95bd12c42dcde5d35634ed08", "Name": "testing", "CreatorId": "S-1-1-11-1111111111-2222222222-3333333333-3333&d-926726012c", "ParentFolderId": "1ece93e5fe75315c7407c4967918b4fd9da87ddb2a588e67b7fdaf4a98fde678", "CreatedTimestamp": 1534450467.622, "ModifiedTimestamp": 1534451113.504, "ResourceState": "ACTIVE", "Signature": "1a23456b78901c23d4ef56gh7EXAMPLE", "Size": 23019, "LatestVersionSize": 11537 } ], "Documents": [ { "Id": "d90d93c1fe44bad0c8471e973ebaab339090401a95e777cffa58e977d2983b65", "CreatorId": "S-1-1-11-1111111111-2222222222-3333333333-3333&d-926726012c", "ParentFolderId": "1ece93e5fe75315c7407c4967918b4fd9da87ddb2a588e67b7fdaf4a98fde678", "CreatedTimestamp": 1529005196.082, "ModifiedTimestamp": 1534452483.01, "LatestVersionMetadata": { "Id": "1534452029587-15e129dfc187505c407588df255be83de2920d733859f1d2762411d22a83e3ef", "Name": "exampleDoc.docx", "ContentType": "application/vnd.openxmlformats-officedocument.wordprocessingml.document", "Size": 13922, "Signature": "1a23456b78901c23d4ef56gh7EXAMPLE", "Status": "ACTIVE", "CreatedTimestamp": 1534452029.587, "ModifiedTimestamp": 1534452029.587, "CreatorId": "S-1-1-11-1111111111-2222222222-3333333333-3333&d-926726012c" }, "ResourceState": "ACTIVE" } ] }`- 
                    For API details, see [DescribeFolderContents](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/workdocs/describe-folder-contents.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `describe-groups`.

- **AWS CLI**
- 
            
                    **To retrieve a list of groups**The following `describe-groups`example lists the groups associated with the specified Amazon WorkDocs organization.`aws workdocs d``e`scribe-groups \ --search-query "e" \ --organization-id`d-123456789c`Output: `{ "Groups": [ { "Id": "S-1-1-11-1122222222-2222233333-3333334444-4444&d-123456789c", "Name": "Example Group 1" }, { "Id": "S-1-1-11-1122222222-2222233333-3333334444-5555&d-123456789c", "Name": "Example Group 2" } ] }`For more information, see [Getting Started with Amazon WorkDocs](https://docs.aws.amazon.com/workdocs/latest/adminguide/getting_started.html)in the*Amazon WorkDocs Administration Guide*.- 
                    For API details, see [DescribeGroups](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/workdocs/describe-groups.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `describe-notification-subscriptions`.

- **AWS CLI**
- 
            
                    **To retrieve a list of notification subscriptions**The following `describe-notification-subscriptions`example retrieves the notification subscriptions for the specified Amazon WorkDocs organization.`aws workdocs describe-notification-subscriptions \ --organization-id``d-123456789c`Output: `{ "Subscriptions": [ { "SubscriptionId": "123ab4c5-678d-901e-f23g-45h6789j0123", "EndPoint": "https://example.com/example", "Protocol": "HTTPS" } ] }`For more information, see [Subscribe to Notifications](https://docs.aws.amazon.com/workdocs/latest/developerguide/subscribe-notifications.html)in the*Amazon WorkDocs Developer Guide*.- 
                    For API details, see [DescribeNotificationSubscriptions](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/workdocs/describe-notification-subscriptions.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `describe-resource-permissions`.

- **AWS CLI**
- 
            
                    **To get a list of permissions for a resource**This example returns a list of the permissions for the specified resource (document or folder). Command: `aws workdocs describe-resource-permissions --resource-id``15df51e0335cfcc6a2e4de9dd8be9f22ee40545ad9176f54758dcf903be982d3`Output: `{ "Principals": [ { "Id": "anonymous", "Type": "ANONYMOUS", "Roles": [ { "Role": "VIEWER", "Type": "DIRECT" } ] }, { "Id": "S-1-1-11-1111111111-2222222222-3333333333-3333&d-926726012c", "Type": "USER", "Roles": [ { "Role": "OWNER", "Type": "DIRECT" } ] }, { "Id": "d-926726012c", "Type": "ORGANIZATION", "Roles": [ { "Role": "VIEWER", "Type": "INHERITED" } ] } ] }`- 
                    For API details, see [DescribeResourcePermissions](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/workdocs/describe-resource-permissions.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `describe-users`.

- **AWS CLI**
- 
            
                    **To retrieve details for specified users**This example retrieves details for all the users in the specified organization. Command: `aws workdocs describe-users --organization-id``d-926726012c`Output: `{ "Users": [ { "Id": "S-1-1-11-1111111111-2222222222-3333333333-3333&d-926726012c", "Username": "example1User", "OrganizationId": "d-926726012c", "RootFolderId": "3c0e3f849dd20a9771d937b9bbcc97e18796150ae56c26d64a4fa0320a2dedc9", "RecycleBinFolderId": "c277f4c4d647be1f5147b3184ffa96e1e2bf708278b696cacba68ba13b91f4fe", "Status": "INACTIVE", "Type": "USER", "CreatedTimestamp": 1535478999.452, "ModifiedTimestamp": 1535478999.452 }, { "Id": "S-1-1-11-1111111111-2222222222-3333333333-4444&d-926726012c", "Username": "example2User", "EmailAddress": "example2User@site.awsapps.com", "GivenName": "example2Name", "Surname": "example2Surname", "OrganizationId": "d-926726012c", "RootFolderId": "35b886cb17198cbd547655e58b025dff0cf34aaed638be52009567e23dc67390", "RecycleBinFolderId": "9858c3e9ed4c2460dde9aadb4c69fde998070dd46e5e985bd08ec6169ea249ff", "Status": "ACTIVE", "Type": "MINIMALUSER", "CreatedTimestamp": 1535478836.584, "ModifiedTimestamp": 1535478836.584 } ] }`- 
                    For API details, see [DescribeUsers](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/workdocs/describe-users.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `get-document-path`.

- **AWS CLI**
- 
            
                    **To retrieve a document's path information**This example retrieves the path information (hierarchy from the root folder) for the specified document, and includes the names of the parent folders. Command: `aws workdocs get-document-path --document-id``d90d93c1fe44bad0c8471e973ebaab339090401a95e777cffa58e977d2983b65`--fields`NAME`Output: `{ "Path": { "Components": [ { "Id": "a43d29cbb8e7c4d25cfee8b803a504b0dc63e760b55ad0c611c6b87691eb6ff3", "Name": "/" }, { "Id": "1ece93e5fe75315c7407c4967918b4fd9da87ddb2a588e67b7fdaf4a98fde678", "Name": "Top Level Folder" }, { "Id": "d90d93c1fe44bad0c8471e973ebaab339090401a95e777cffa58e977d2983b65", "Name": "exampleDoc.docx" } ] } }`- 
                    For API details, see [GetDocumentPath](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/workdocs/get-document-path.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `get-document-version`.

- **AWS CLI**
- 
            
                    **To retrieve version metadata for a specified document**This example retrieves version metadata for the specified document, including a source URL and custom metadata. Command: `aws workdocs get-document-version --document-id``15df51e0335cfcc6a2e4de9dd8be9f22ee40545ad9176f54758dcf903be982d3`--version-id`1521672507741-9f7df0ea5dd0b121c4f3564a0c7c0b4da95cd12c635d3c442af337a88e297920`--fields`SOURCE`--include-custom-metadataOutput: `{ "Metadata": { "Id": "1521672507741-9f7df0ea5dd0b121c4f3564a0c7c0b4da95cd12c635d3c442af337a88e297920", "Name": "exampleDoc", "ContentType": "application/vnd.openxmlformats-officedocument.wordprocessingml.document", "Size": 11537, "Signature": "1a23456b78901c23d4ef56gh7EXAMPLE", "Status": "ACTIVE", "CreatedTimestamp": 1521672507.741, "ModifiedTimestamp": 1534451113.504, "CreatorId": "S-1-1-11-1111111111-2222222222-3333333333-3333&d-926726012c", "Source": { "ORIGINAL": "https://gb-us-west-2-prod-doc-source.s3.us-west-2.amazonaws.com/15df51e0335cfcc6a2e4de9dd8be9f22ee40545ad9176f54758dcf903be982d3/1521672507741-9f7df0ea5dd0b121c4f3564a0c7c0b4da95cd12c635d3c442af337a88e297920?response-content-disposition=attachment%3B%20filename%2A%3DUTF-8%27%27exampleDoc&X-Amz-Algorithm=AWS1-ABCD-EFG234&X-Amz-Date=20180820T212202Z&X-Amz-SignedHeaders=host&X-Amz-Expires=900&X-Amz-Credential=AKIAIOSFODNN7EXAMPLE%2F20180820%2Fus-west-2%2Fs3%2Faws1_request&X-Amz-Signature=01Ab2c34d567e8f90123g456hi78j901k2345678l901234mno56pqr78EXAMPLE" } } }`- 
                    For API details, see [GetDocumentVersion](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/workdocs/get-document-version.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `get-document`.

- **AWS CLI**
- 
            
                    **To retrieve document details**This example retrieves the details of the specified document. Command: `aws workdocs get-document --document-id``d90d93c1fe44bad0c8471e973ebaab339090401a95e777cffa58e977d2983b65`Output: `{ "Metadata": { "Id": "d90d93c1fe44bad0c8471e973ebaab339090401a95e777cffa58e977d2983b65", "CreatorId": "S-1-1-11-1111111111-2222222222-3333333333-3333&d-926726012c", "ParentFolderId": "1ece93e5fe75315c7407c4967918b4fd9da87ddb2a588e67b7fdaf4a98fde678", "CreatedTimestamp": 1529005196.082, "ModifiedTimestamp": 1534452483.01, "LatestVersionMetadata": { "Id": "1534452029587-15e129dfc187505c407588df255be83de2920d733859f1d2762411d22a83e3ef", "Name": "exampleDoc.docx", "ContentType": "application/vnd.openxmlformats-officedocument.wordprocessingml.document", "Size": 13922, "Signature": "1a23456b78901c23d4ef56gh7EXAMPLE", "Status": "ACTIVE", "CreatedTimestamp": 1534452029.587, "ModifiedTimestamp": 1534452029.587, "CreatorId": "S-1-1-11-1111111111-2222222222-3333333333-3333&d-926726012c" }, "ResourceState": "ACTIVE" } }`- 
                    For API details, see [GetDocument](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/workdocs/get-document.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `get-folder-path`.

- **AWS CLI**
- 
            
                    **To retrieve path information for a folder**This example retrieves the path information (hierarchy from the root folder) for the specified folder, and includes the names of the parent folders. Command: `aws workdocs get-folder-path --folder-id``50893c0af679524d1a0e0651130ed6d073e1a05f95bd12c42dcde5d35634ed08`--fields`NAME`Output: `{ "Path": { "Components": [ { "Id": "a43d29cbb8e7c4d25cfee8b803a504b0dc63e760b55ad0c611c6b87691eb6ff3", "Name": "/" }, { "Id": "1ece93e5fe75315c7407c4967918b4fd9da87ddb2a588e67b7fdaf4a98fde678", "Name": "Top Level Folder" }, { "Id": "50893c0af679524d1a0e0651130ed6d073e1a05f95bd12c42dcde5d35634ed08", "Name": "Sublevel Folder" } ] } }`- 
                    For API details, see [GetFolderPath](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/workdocs/get-folder-path.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `get-folder`.

- **AWS CLI**
- 
            
                    **To retrieve the metadata for a folder**This example retrieves the metadata for the specified folder. Command: `aws workdocs get-folder --folder-id``50893c0af679524d1a0e0651130ed6d073e1a05f95bd12c42dcde5d35634ed08`Output: `{ "Metadata": { "Id": "50893c0af679524d1a0e0651130ed6d073e1a05f95bd12c42dcde5d35634ed08", "Name": "exampleFolder", "CreatorId": "S-1-1-11-1111111111-2222222222-3333333333-3333&d-926726012c", "ParentFolderId": "1ece93e5fe75315c7407c4967918b4fd9da87ddb2a588e67b7fdaf4a98fde678", "CreatedTimestamp": 1534450467.622, "ModifiedTimestamp": 1534451113.504, "ResourceState": "ACTIVE", "Signature": "1a23456b78901c23d4ef56gh7EXAMPLE", "Size": 23019, "LatestVersionSize": 11537 } }`- 
                    For API details, see [GetFolder](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/workdocs/get-folder.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `get-resources`.

- **AWS CLI**
- 
            
                    **To retrieve shared resources**The following `get-resources`example retrieves the resources shared with the specified Amazon WorkDocs user.`aws workdocs get-resources \ --user-id``"S-1-1-11-1111111111-2222222222-3333333333-3333"`\ --collection-type`SHARED_WITH_ME`Output: `{ "Folders": [], "Documents": [] }`For more information, see [Sharing Files and Folders](https://docs.aws.amazon.com/workdocs/latest/userguide/share-docs.html)in the*Amazon WorkDocs User Guide*.- 
                    For API details, see [GetResources](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/workdocs/get-resources.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `initiate-document-version-upload`.

- **AWS CLI**
- 
            
                    **To initiate a document version upload**The following `initiate-document-upload`example creates a new document object and version object.`aws workdocs initiate-document-version-upload \ --name``exampledocname`\ --parent-folder-id`eacd546d952531c633452ed67cac23161aa0d5df2e8061223a59e8f67e7b6189`Output: `{ "Metadata": { "Id": "feaba64d4efdf271c2521b60a2a44a8f057e84beaabbe22f01267313209835f2", "CreatorId": "S-1-1-11-1111111111-2222222222-3333333333-3333&d-926726012c", "ParentFolderId": "eacd546d952531c633452ed67cac23161aa0d5df2e8061223a59e8f67e7b6189", "CreatedTimestamp": 1536773972.914, "ModifiedTimestamp": 1536773972.914, "LatestVersionMetadata": { "Id": "1536773972914-ddb67663e782e7ce8455ebc962217cf9f9e47b5a9a702e5c84dcccd417da9313", "Name": "exampledocname", "ContentType": "application/octet-stream", "Size": 0, "Status": "INITIALIZED", "CreatedTimestamp": 1536773972.914, "ModifiedTimestamp": 1536773972.914, "CreatorId": "arn:aws:iam::123456789123:user/EXAMPLE" }, "ResourceState": "ACTIVE" }, "UploadMetadata": { "UploadUrl": "https://gb-us-west-2-prod-doc-source.s3.us-west-2.amazonaws.com/feaba64d4efdf271c2521b60a2a44a8f057e84beaabbe22f01267313209835f2/1536773972914-ddb67663e782e7ce8455ebc962217cf9f9e47b5a9a702e5c84dcccd417da9313?X-Amz-Algorithm=AWS1-ABCD-EFG234&X-Amz-Date=20180912T173932Z&X-Amz-SignedHeaders=content-type%3Bhost%3Bx-amz-server-side-encryption&X-Amz-Expires=899&X-Amz-Credential=AKIAIOSFODNN7EXAMPLE%2F20180912%2Fus-west-2%2Fs3%2Faws1_request&X-Amz-Signature=01Ab2c34d567e8f90123g456hi78j901k2345678l901234mno56pqr78EXAMPLE", "SignedHeaders": { "Content-Type": "application/octet-stream", "x-amz-server-side-encryption": "ABC123" } } }`- 
                    For API details, see [InitiateDocumentVersionUpload](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/workdocs/initiate-document-version-upload.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `remove-all-resource-permissions`.

- **AWS CLI**
- 
            
                    **To remove all permissions from a specified resource**This example removes all permissions from the specified resource. Command: `aws workdocs remove-all-resource-permissions --resource-id``1ece93e5fe75315c7407c4967918b4fd9da87ddb2a588e67b7fdaf4a98fde678`Output: `None`- 
                    For API details, see [RemoveAllResourcePermissions](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/workdocs/remove-all-resource-permissions.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `remove-resource-permission`.

- **AWS CLI**
- 
            
                    **To remove permissions from a resource**This example removes permissions from the resource for the specified principal. Command: `aws workdocs remove-resource-permission --resource-id``1ece93e5fe75315c7407c4967918b4fd9da87ddb2a588e67b7fdaf4a98fde678`--principal-id`anonymous`Output: `None`- 
                    For API details, see [RemoveResourcePermission](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/workdocs/remove-resource-permission.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `update-document-version`.

- **AWS CLI**
- 
            
                    **To change a document version status to Active**This example changes the status of the document version to Active. Command: `aws workdocs update-document-version --document-id``15df51e0335cfcc6a2e4de9dd8be9f22ee40545ad9176f54758dcf903be982d3`--version-id`1521672507741-9f7df0ea5dd0b121c4f3564a0c7c0b4da95cd12c635d3c442af337a88e297920`--version-status`ACTIVE`Output: `None`- 
                    For API details, see [UpdateDocumentVersion](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/workdocs/update-document-version.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `update-document`.

- **AWS CLI**
- 
            
                    **To update a document**This example updates a document's name and parent folder. Command: `aws workdocs update-document --document-id``15df51e0335cfcc6a2e4de9dd8be9f22ee40545ad9176f54758dcf903be982d3`--name`updatedDoc`--parent-folder-id`50893c0af679524d1a0e0651130ed6d073e1a05f95bd12c42dcde5d35634ed08`Output: `None`- 
                    For API details, see [UpdateDocument](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/workdocs/update-document.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `update-folder`.

- **AWS CLI**
- 
            
                    **To update a folder**This example updates a folder's name and parent folder. Command: `aws workdocs update-folder --folder-id``50893c0af679524d1a0e0651130ed6d073e1a05f95bd12c42dcde5d35634ed08`--name`exampleFolder1`--parent-folder-id`1ece93e5fe75315c7407c4967918b4fd9da87ddb2a588e67b7fdaf4a98fde678`Output: `None`- 
                    For API details, see [UpdateFolder](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/workdocs/update-folder.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `update-user`.

- **AWS CLI**
- 
            
                    **To update a user**This example updates the time zone for the specified user. Command: `aws workdocs update-user --user-id``"S-1-1-11-1111111111-2222222222-3333333333-3333&d-926726012c"`--time-zone-id`"America/Los_Angeles"`Output: `{ "User": { "Id": "S-1-1-11-1111111111-2222222222-3333333333-3333&d-926726012c", "Username": "exampleUser", "EmailAddress": "exampleUser@site.awsapps.com", "GivenName": "Example", "Surname": "User", "OrganizationId": "d-926726012c", "RootFolderId": "c5eceb5e1a2d1d460c9d1af8330ae117fc8d39bb1d3ed6acd0992d5ff192d986", "RecycleBinFolderId": "6ca20102926ad15f04b1d248d6d6e44f2449944eda5c758f9a1e9df6a6b7fa66", "Status": "ACTIVE", "Type": "USER", "TimeZoneId": "America/Los_Angeles", "Storage": { "StorageUtilizedInBytes": 0, "StorageRule": { "StorageAllocatedInBytes": 53687091200, "StorageType": "QUOTA" } } } }`- 
                    For API details, see [UpdateUser](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/workdocs/update-user.html)in*AWS CLI Command Reference*.
 
-