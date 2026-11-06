# Detective examples using AWS CLI - AWS Command Line Interface

**Source:** [https://docs.aws.amazon.com/cli/latest/userguide/cli_detective_code_examples.html](https://docs.aws.amazon.com/cli/latest/userguide/cli_detective_code_examples.html)

---

The following code examples show you how to perform actions and implement common scenarios by using the AWS Command Line Interface with Detective.

*Actions* are code excerpts from larger programs and must be run in context. While actions show you how to call individual service functions, you can see actions in context in their related scenarios.

Each example includes a link to the complete source code, where you can find instructions on how to set up and run the code in context.

###### Topics

## Actions

    The following code example shows how to use `accept-invitation`.

- **AWS CLI**
- 
            
                    **To accept an invitation to become a member account in a behavior graph**The following `accept-invitation`example accepts an invitation to become a member account in behavior graph arn:aws:detective:us-east-1:111122223333:graph:123412341234.`aws detective accept-invitation \ --graph-arn``arn:aws:detective:us-east-1:111122223333:graph:123412341234`This command produces no output. For more information, see [Responding to a behavior graph invitation](https://docs.aws.amazon.com/detective/latest/adminguide/member-invitation-response.html)in the*Amazon Detective Administration Guide*.- 
                    For API details, see [AcceptInvitation](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/detective/accept-invitation.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `create-graph`.

- **AWS CLI**
- 
            
                    **To enable Amazon Detective and create a new behavior graph**The following `create-graph`example enables Detective for the AWS account that runs the command in the Region where the command is run. A new behavior graph is created that has that account as its administrator account. The command also assigns the value Finance to the Department tag.`aws detective create-graph \ --tags '``{"Department": "Finance"}`'Output: `{ "GraphArn": "arn:aws:detective:us-east-1:111122223333:graph:027c7c4610ea4aacaf0b883093cab899" }`For more information, see [Enabling Amazon Detective](https://docs.aws.amazon.com/detective/latest/adminguide/detective-enabling.html)in the*Amazon Detective Administration Guide*.- 
                    For API details, see [CreateGraph](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/detective/create-graph.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `create-members`.

- **AWS CLI**
- 
            
                    **To invite member accounts to a behavior graph**The following `create-members`example invites two AWS accounts to become member accounts in the behavior graph arn:aws:detective:us-east-1:111122223333:graph:123412341234. For each account, the request provides the AWS account ID and the account root user email address. The request includes a custom message to insert into the invitation email.`aws detective create-members \ --accounts``AccountId=444455556666,EmailAddress=mmajor@example.com``AccountId=123456789012,EmailAddress=jstiles@example.com`\ --graph-arn`arn:aws:detective:us-east-1:111122223333:graph:123412341234`\ --message`"This is Paul Santos. I need to add your account to the data we use for security investigation in Amazon Detective. If you have any questions, contact me at psantos@example.com."`Output: `{ "Members": [ { "AccountId": "444455556666", "AdministratorId": "111122223333", "EmailAddress": "mmajor@example.com", "GraphArn": "arn:aws:detective:us-east-1:111122223333:graph:123412341234", "InvitedTime": 1579826107000, "MasterId": "111122223333", "Status": "INVITED", "UpdatedTime": 1579826107000 }, { "AccountId": "123456789012", "AdministratorId": "111122223333", "EmailAddress": "jstiles@example.com", "GraphArn": "arn:aws:detective:us-east-1:111122223333:graph:123412341234", "InvitedTime": 1579826107000, "MasterId": "111122223333", "Status": "VERIFICATION_IN_PROGRESS", "UpdatedTime": 1579826107000 } ], "UnprocessedAccounts": [ ] }`For more information, see Inviting member accounts to a behavior graph<https://docs.aws.amazon.com/detective/latest/adminguide/graph-admin-add-member-accounts.html> in the *Amazon Detective Administration Guide*.**To invite member accounts without sending invitation emails**The following `create-members`example invites two AWS accounts to become member accounts in the behavior graph arn:aws:detective:us-east-1:111122223333:graph:123412341234. For each account, the request provides the AWS account ID and the account root user email address. The member accounts do not receive invitation emails.`aws detective create-members \ --accounts``AccountId=444455556666,EmailAddress=mmajor@example.com``AccountId=123456789012,EmailAddress=jstiles@example.com`\ --graph-arn`arn:aws:detective:us-east-1:111122223333:graph:123412341234`\ --disable-email-notificationOutput: `{ "Members": [ { "AccountId": "444455556666", "AdministratorId": "111122223333", "EmailAddress": "mmajor@example.com", "GraphArn": "arn:aws:detective:us-east-1:111122223333:graph:123412341234", "InvitedTime": 1579826107000, "MasterId": "111122223333", "Status": "INVITED", "UpdatedTime": 1579826107000 }, { "AccountId": "123456789012", "AdministratorId": "111122223333", "EmailAddress": "jstiles@example.com", "GraphArn": "arn:aws:detective:us-east-1:111122223333:graph:123412341234", "InvitedTime": 1579826107000, "MasterId": "111122223333", "Status": "VERIFICATION_IN_PROGRESS", "UpdatedTime": 1579826107000 } ], "UnprocessedAccounts": [ ] }`For more information, see Inviting member accounts to a behavior graph<https://docs.aws.amazon.com/detective/latest/adminguide/graph-admin-add-member-accounts.html> in the *Amazon Detective Administration Guide*.- 
                    For API details, see [CreateMembers](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/detective/create-members.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `delete-graph`.

- **AWS CLI**
- 
            
                    **To disable Detective and delete the behavior graph**The following `delete-graph`example disables Detective and deletes the specified behavior graph.`aws detective delete-graph \ --graph-arn``arn:aws:detective:us-east-1:111122223333:graph:123412341234`This command produces no output. For more information, see [Disabling Amazon Detective](https://docs.aws.amazon.com/detective/latest/adminguide/detective-disabling.html)in the*Amazon Detective Administration Guide*.- 
                    For API details, see [DeleteGraph](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/detective/delete-graph.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `delete-members`.

- **AWS CLI**
- 
            
                    **To remove member accounts from a behavior graph**The following `delete-members`example removes two member accounts from the behavior graph arn:aws:detective:us-east-1:111122223333:graph:123412341234. To identify the accounts, the request provides the AWS account IDs.`aws detective delete-members \ --account-ids``444455556666``123456789012`\ --graph-arn`arn:aws:detective:us-east-1:111122223333:graph:123412341234`Output: `{ "AccountIds": [ "444455556666", "123456789012" ], "UnprocessedAccounts": [ ] }`For more information, see Removing member accounts from a behavior graph<https://docs.aws.amazon.com/detective/latest/adminguide/graph-admin-remove-member-accounts.html> in the *Amazon Detective Administration Guide*.- 
                    For API details, see [DeleteMembers](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/detective/delete-members.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `disassociate-membership`.

- **AWS CLI**
- 
            
                    **To resign membership from a behavior graph**The following disassociate-membership example removes the AWS account that runs the command from the behavior graph arn:aws:detective:us-east-1:111122223333:graph:123412341234. `aws detective disassociate-membership \ --graph-arn``arn:aws:detective:us-east-1:111122223333:graph:123412341234`For more information, see Removing your account from a behavior graph<https://docs.aws.amazon.com/detective/latest/adminguide/member-remove-self-from-graph.html> in the *Amazon Detective Administration Guide*.- 
                    For API details, see [DisassociateMembership](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/detective/disassociate-membership.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `get-members`.

- **AWS CLI**
- 
            
                    **To retrieve information about selected behavior graph member accounts**The following `get-members`example retrieves information about two member accounts in the behavior graph arn:aws:detective:us-east-1:111122223333:graph:123412341234. For the two accounts, the request provides the AWS account IDs.`aws detective get-members \ --account-ids``444455556666``123456789012`\ --graph-arn`arn:aws:detective:us-east-1:111122223333:graph:123412341234`Output: `{ "MemberDetails": [ { "AccountId": "444455556666", "AdministratorId": "111122223333", "EmailAddress": "mmajor@example.com", "GraphArn": "arn:aws:detective:us-east-1:111122223333:graph:123412341234", "InvitedTime": 1579826107000, "MasterId": "111122223333", "Status": "INVITED", "UpdatedTime": 1579826107000 } { "AccountId": "123456789012", "AdministratorId": "111122223333", "EmailAddress": "jstiles@example.com", "GraphArn": "arn:aws:detective:us-east-1:111122223333:graph:123412341234", "InvitedTime": 1579826107000, "MasterId": "111122223333", "Status": "INVITED", "UpdatedTime": 1579826107000 } ], "UnprocessedAccounts": [ ] }`For more information, see Viewing the list of accounts in a behavior graph<https://docs.aws.amazon.com/detective/latest/adminguide/graph-admin-view-accounts.html> in the *Amazon Detective Administration Guide*.- 
                    For API details, see [GetMembers](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/detective/get-members.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `list-graphs`.

- **AWS CLI**
- 
            
                    **To view a list of behavior graphs that your account is the administrator for**The following `list-graphs`example retrieves the behavior graphs that the calling account is the administrator for within the current Region.`aws detective list-graphs`Output: `{ "GraphList": [ { "Arn": "arn:aws:detective:us-east-1:111122223333:graph:123412341234", "CreatedTime": 1579736111000 } ] }`- 
                    For API details, see [ListGraphs](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/detective/list-graphs.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `list-invitations`.

- **AWS CLI**
- 
            
                    **To view a list of behavior graphs that an account is a member of or is invited to**The following `list-invitations`example retrieves the behavior graphs that the calling account has been invited to. The results include only open and accepted invitations. They do not include rejected invitations or removed memberships.`aws detective list-invitations`Output: `{ "Invitations": [ { "AccountId": "444455556666", "AdministratorId": "111122223333", "EmailAddress": "mmajor@example.com", "GraphArn": "arn:aws:detective:us-east-1:111122223333:graph:123412341234", "InvitedTime": 1579826107000, "MasterId": "111122223333", "Status": "INVITED", "UpdatedTime": 1579826107000 } ] }`For more information, see Viewing your list of behavior graph invitations<https://docs.aws.amazon.com/detective/latest/adminguide/member-view-graph-invitations.html> in the *Amazon Detective Administration Guide*.- 
                    For API details, see [ListInvitations](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/detective/list-invitations.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `list-members`.

- **AWS CLI**
- 
            
                    **To list the member accounts in a behavior graph**The following `list-members`example retrieves the invited and enabled member accounts for the behavior graph`arn:aws:detective:us-east-1:111122223333:graph:123412341234`. The results do not include member accounts that were removed.`aws detective list-members \ --graph-arn``arn:aws:detective:us-east-1:111122223333:graph:123412341234`Output: `{ "MemberDetails": [ { "AccountId": "444455556666", "AdministratorId": "111122223333", "EmailAddress": "mmajor@example.com", "GraphArn": "arn:aws:detective:us-east-1:111122223333:graph:123412341234", "InvitedTime": 1579826107000, "MasterId": "111122223333", "Status": "INVITED", "UpdatedTime": 1579826107000 }, { "AccountId": "123456789012", "AdministratorId": "111122223333", "EmailAddress": "jstiles@example.com", "GraphArn": "arn:aws:detective:us-east-1:111122223333:graph:123412341234", "InvitedTime": 1579826107000, "MasterId": "111122223333", "PercentOfGraphUtilization": 2, "PercentOfGraphUtilizationUpdatedTime": 1586287843, "Status": "ENABLED", "UpdatedTime": 1579973711000, "VolumeUsageInBytes": 200, "VolumeUsageUpdatedTime": 1586287843 } ] }`For more information, see [Viewing the list of accounts in a behavior graph](https://docs.aws.amazon.com/detective/latest/adminguide/graph-admin-view-accounts.html)in the*Amazon Detective Administration Guide*.- 
                    For API details, see [ListMembers](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/detective/list-members.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `list-tags-for-resource`.

- **AWS CLI**
- 
            
                    **To retrieve the tags assigned to a behavior graph**The following `list-tags-for-resource`example returns the tags assigned to the specified behavior graph.`aws detective list-tags-for-resource \ --resource-arn``arn:aws:detective:us-east-1:111122223333:graph:123412341234`Output: `{ "Tags": { "Department" : "Finance" } }`For more information, see [Managing tags for a behavior graph](https://docs.aws.amazon.com/detective/latest/adminguide/graph-tags.html)in the*Amazon Detective Administration Guide*.- 
                    For API details, see [ListTagsForResource](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/detective/list-tags-for-resource.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `reject-invitation`.

- **AWS CLI**
- 
            
                    **To reject an invitation to become a member account in a behavior graph**The following `reject-invitation`example rejects an invitation to become a member account in the behavior graph arn:aws:detective:us-east-1:111122223333:graph:123412341234.`aws detective reject-invitation \ --graph-arn``arn:aws:detective:us-east-1:111122223333:graph:123412341234`This command produces no output. For more information, see Responding to a behavior graph invitation<https://docs.aws.amazon.com/detective/latest/adminguide/member-invitation-response.html> in the *Amazon Detective Administration Guide*.- 
                    For API details, see [RejectInvitation](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/detective/reject-invitation.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `tag-resource`.

- **AWS CLI**
- 
            
                    **To assign a tag to a resource**The following `tag-resource`example assigns a value for the Department tag to the specified behavior graph.`aws detective tag-resource \ --resource-arn``arn:aws:detective:us-east-1:111122223333:graph:123412341234`\ --tags '`{"Department":"Finance"}`'This command produces no output. For more information, see [Managing tags for a behavior graph](https://docs.aws.amazon.com/detective/latest/adminguide/graph-tags.html)in the*Amazon Detective Administration Guide*.- 
                    For API details, see [TagResource](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/detective/tag-resource.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `untag-resource`.

- **AWS CLI**
- 
            
                    **To remove a tag value from a resource**The following `untag-resource`example removes the Department tag from the specified behavior graph.`aws detective untag-resource \ --resource-arn``arn:aws:detective:us-east-1:111122223333:graph:123412341234`\ --tag-keys`"Department"`This command produces no output. For more information, see [Managing tags for a behavior graph](https://docs.aws.amazon.com/detective/latest/adminguide/graph-tags.html)in the*Amazon Detective Administration Guide*.- 
                    For API details, see [UntagResource](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/detective/untag-resource.html)in*AWS CLI Command Reference*.
 
-