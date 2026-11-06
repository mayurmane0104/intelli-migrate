# Amazon WorkMail examples using AWS CLI - AWS Command Line Interface

**Source:** [https://docs.aws.amazon.com/cli/latest/userguide/cli_workmail_code_examples.html](https://docs.aws.amazon.com/cli/latest/userguide/cli_workmail_code_examples.html)

---

The following code examples show you how to perform actions and implement common scenarios by using the AWS Command Line Interface with Amazon WorkMail.

*Actions* are code excerpts from larger programs and must be run in context. While actions show you how to call individual service functions, you can see actions in context in their related scenarios.

Each example includes a link to the complete source code, where you can find instructions on how to set up and run the code in context.

###### Topics

## Actions

    The following code example shows how to use `associate-delegate-to-resource`.

- **AWS CLI**
- 
            
                    **To add a delegate to a resource**The following `associate-delegate-to-resource`command adds a delegate to a resource.`aws workmail associate-delegate-to-resource \ --organization-id``m-d281d0a2fd824be5b6cd3d3ce909fd27`\ --resource-id`r-68bf2d3b1c0244aab7264c24b9217443`\ --entity-id`S-1-1-11-1111111111-2222222222-3333333333-3333`This command produces no output. - 
                    For API details, see [AssociateDelegateToResource](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/workmail/associate-delegate-to-resource.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `associate-member-to-group`.

- **AWS CLI**
- 
            
                    **To add a member to a group**The following `associate-member-to-group`command adds the specified member to a group.`aws workmail associate-member-to-group \ --organization-id``m-d281d0a2fd824be5b6cd3d3ce909fd27`\ --group-id`S-1-1-11-1122222222-2222233333-3333334444-4444`\ --member-id`S-1-1-11-1111111111-2222222222-3333333333-3333`This command produces no output. - 
                    For API details, see [AssociateMemberToGroup](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/workmail/associate-member-to-group.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `create-alias`.

- **AWS CLI**
- 
            
                    **To create an alias**The following `create-alias`command creates an alias for the specified entity (user or group).`aws workmail create-alias \ --organization-id``m-d281d0a2fd824be5b6cd3d3ce909fd27`\ --entity-id`S-1-1-11-1122222222-2222233333-3333334444-4444`\ --alias`exampleAlias@site.awsapps.com`This command produces no output. - 
                    For API details, see [CreateAlias](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/workmail/create-alias.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `create-group`.

- **AWS CLI**
- 
            
                    **To create a new group**The following `create-group`command creates a new group for the specified organization.`aws workmail create-group \ --organization-id``m-d281d0a2fd824be5b6cd3d3ce909fd27`\ --name`exampleGroup1`Output: `{ "GroupId": "S-1-1-11-1122222222-2222233333-3333334444-4444" }`- 
                    For API details, see [CreateGroup](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/workmail/create-group.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `create-resource`.

- **AWS CLI**
- 
            
                    **To create a new resource**The following `create-resource`command creates a new resource (meeting room) for the specified organization.`aws workmail create-resource \ --organization-id``m-d281d0a2fd824be5b6cd3d3ce909fd27`\ --name`exampleRoom1`\ --type`ROOM`Output: `{ "ResourceId": "r-7afe0efbade843a58cdc10251fce992c" }`- 
                    For API details, see [CreateResource](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/workmail/create-resource.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `create-user`.

- **AWS CLI**
- 
            
                    **To create a new user**The following `create-user`command creates a new user.`aws workmail create-user \ --organization-id``m-d281d0a2fd824be5b6cd3d3ce909fd27`\ --name`exampleName`\ --display-name`exampleDisplayName`\ --password`examplePa$$w0rd`Output: `{ "UserId": "S-1-1-11-1111111111-2222222222-3333333333-3333" }`- 
                    For API details, see [CreateUser](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/workmail/create-user.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `delete-access-control-rule`.

- **AWS CLI**
- 
            
                    **To delete an access control rule**The following `delete-access-control-rule`example deletes the specified access control rule from the specified Amazon WorkMail organization.`aws workmail delete-access-control-rule \ --organization-id``m-n1pq2345678r901st2u3vx45x6789yza`\ --name`"myRule"`This command produces no output. For more information, see [Working with Access Control Rules](https://docs.aws.amazon.com/workmail/latest/adminguide/access-rules.html)in the*Amazon WorkMail Administrator Guide*.- 
                    For API details, see [DeleteAccessControlRule](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/workmail/delete-access-control-rule.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `delete-alias`.

- **AWS CLI**
- 
            
                    **To delete an alias**The following `delete-alias`command deletes the alias for the specified entity (user or group).`aws workmail delete-alias \ --organization-id``m-d281d0a2fd824be5b6cd3d3ce909fd27`\ --entity-id`S-1-1-11-1122222222-2222233333-3333334444-4444`\ --alias`exampleAlias@site.awsapps.com`This command produces no output. - 
                    For API details, see [DeleteAlias](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/workmail/delete-alias.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `delete-group`.

- **AWS CLI**
- 
            
                    **To delete an existing group**The following `delete-group`command deletes an existing group from Amazon WorkMail.`aws workmail delete-group \ --organization-id``m-d281d0a2fd824be5b6cd3d3ce909fd27`\ --group-id`S-1-1-11-1122222222-2222233333-3333334444-4444`This command produces no output. - 
                    For API details, see [DeleteGroup](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/workmail/delete-group.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `delete-mailbox-permissions`.

- **AWS CLI**
- 
            
                    **To delete mailbox permissions**The following `delete-mailbox-permissions`command deletes mailbox permissions that were previously granted to a user or group. The entity represents the user that owns the mailbox, and the grantee represents the user or group for whom to delete permissions.`aws workmail delete-mailbox-permissions \ --organization-id``m-d281d0a2fd824be5b6cd3d3ce909fd27`\ --entity-id`S-1-1-11-1122222222-2222233333-3333334444-4444`\ --grantee-id`S-1-1-11-1111111111-2222222222-3333333333-3333`This command produces no output. - 
                    For API details, see [DeleteMailboxPermissions](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/workmail/delete-mailbox-permissions.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `delete-resource`.

- **AWS CLI**
- 
            
                    **To delete an existing resource**The following `delete-resource`command deletes an existing resource from Amazon WorkMail.`aws workmail delete-resource \ --organization-id``m-d281d0a2fd824be5b6cd3d3ce909fd27`\ --resource-id`r-7afe0efbade843a58cdc10251fce992c`This command produces no output. - 
                    For API details, see [DeleteResource](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/workmail/delete-resource.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `delete-user`.

- **AWS CLI**
- 
            
                    **To delete a user**The following `delete-user`command deletes the specified user from Amazon WorkMail and all subsequent systems.`aws workmail delete-user \ --organization-id``m-d281d0a2fd824be5b6cd3d3ce909fd27`\ --user-id`S-1-1-11-1111111111-2222222222-3333333333-3333`This command produces no output. - 
                    For API details, see [DeleteUser](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/workmail/delete-user.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `deregister-from-work-mail`.

- **AWS CLI**
- 
            
                    **To disable an existing entity**The following `deregister-from-work-mail`command disables an existing entity (user, group, or resource) from using Amazon WorkMail.`aws workmail deregister-from-work-mail \ --organization-id``m-d281d0a2fd824be5b6cd3d3ce909fd27`\ --entity-id`S-1-1-11-1111111111-2222222222-3333333333-3333`This command produces no output. - 
                    For API details, see [DeregisterFromWorkMail](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/workmail/deregister-from-work-mail.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `describe-group`.

- **AWS CLI**
- 
            
                    **To retrieve information for a group**The following `describe-group`command retrieves information about the specified group.`aws workmail describe-group \ --organization-id``m-d281d0a2fd824be5b6cd3d3ce909fd27`\ --group-id`S-1-1-11-1122222222-2222233333-3333334444-4444`Output: `{ "GroupId": "S-1-1-11-1122222222-2222233333-3333334444-4444", "Name": "exampleGroup1", "State": "ENABLED" }`- 
                    For API details, see [DescribeGroup](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/workmail/describe-group.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `describe-organization`.

- **AWS CLI**
- 
            
                    **To retrieve information for an organization**The following `describe-organization`command retrieves information for the specified Amazon WorkMail organization.`aws workmail describe-organization \ --organization-id``m-d281d0a2fd824be5b6cd3d3ce909fd27`Output: `{ "OrganizationId": "m-d281d0a2fd824be5b6cd3d3ce909fd27", "Alias": "alias", "State": "Active", "DirectoryId": "d-926726012c", "DirectoryType": "VpcDirectory", "DefaultMailDomain": "site.awsapps.com", "CompletedDate": 1522693605.468, "ARN": "arn:aws:workmail:us-west-2:111122223333:organization/m-n1pq2345678r901st2u3vx45x6789yza" }`For more information, see [Working with Organizations](https://docs.aws.amazon.com/workmail/latest/adminguide/organizations_overview.html)in the*Amazon WorkMail Administrator Guide*.- 
                    For API details, see [DescribeOrganization](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/workmail/describe-organization.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `describe-resource`.

- **AWS CLI**
- 
            
                    **To retrieve information for a resource**The following `describe-resource`command retrieves information about the specified resource.`aws workmail describe-resource \ --organization-id``m-d281d0a2fd824be5b6cd3d3ce909fd27`\ --resource-id`r-7afe0efbade843a58cdc10251fce992c`Output: `{ "ResourceId": "r-7afe0efbade843a58cdc10251fce992c", "Name": "exampleRoom1", "Type": "ROOM", "BookingOptions": { "AutoAcceptRequests": true, "AutoDeclineRecurringRequests": false, "AutoDeclineConflictingRequests": true }, "State": "ENABLED" }`- 
                    For API details, see [DescribeResource](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/workmail/describe-resource.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `describe-user`.

- **AWS CLI**
- 
            
                    **To retrieve user information**The following `describe-user`command retrieves information about the specified user.`aws workmail describe-user \ --organization-id``m-d281d0a2fd824be5b6cd3d3ce909fd27`\ --user-id`S-1-1-11-1111111111-2222222222-3333333333-3333`Output: `{ "UserId": "S-1-1-11-1111111111-2222222222-3333333333-3333", "Name": "exampleUser1", "Email": "exampleUser1@site.awsapps.com", "DisplayName": "", "State": "ENABLED", "UserRole": "USER", "EnabledDate": 1532459261.827 }`- 
                    For API details, see [DescribeUser](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/workmail/describe-user.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `disassociate-delegate-from-resource`.

- **AWS CLI**
- 
            
                    **To remove a member from a resource**The following `disassociate-delegate-from-resource`command removes the specified member from a resource.`ws workmail disassociate-delegate-from-resource \ --organization-id m-d281d0a2fd824be5b6cd3d3ce909fd27 \ --resource-id r-68bf2d3b1c0244aab7264c24b9217443 \ --entity-id S-1-1-11-1111111111-2222222222-3333333333-3333`This command produces no output. - 
                    For API details, see [DisassociateDelegateFromResource](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/workmail/disassociate-delegate-from-resource.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `disassociate-member-from-group`.

- **AWS CLI**
- 
            
                    **To remove a member from a group**The following `disassociate-member-from-group`command removes the specified member from a group.`aws workmail disassociate-member-from-group \ --organization-id``m-d281d0a2fd824be5b6cd3d3ce909fd27`\ --group-id`S-1-1-11-1122222222-2222233333-3333334444-4444`\ --member-id`S-1-1-11-1111111111-2222222222-3333333333-3333`This command produces no output. - 
                    For API details, see [DisassociateMemberFromGroup](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/workmail/disassociate-member-from-group.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `get-access-control-effect`.

- **AWS CLI**
- 
            
                    **To get the effect of access control rules**The following `get-access-control-effect`example retrieves the effect of the specified Amazon WorkMail organization's access control rules for the specified IP address, access protocol action, and user ID.`aws workmail get-access-control-effect \ --organization-id``m-n1pq2345678r901st2u3vx45x6789yza`\ --ip-address`"192.0.2.0"`\ --action`"WindowsOutlook"`\ --user-id`"S-1-1-11-1111111111-2222222222-3333333333-3333"`Output: `{ "Effect": "DENY", "MatchedRules": [ "myRule" ] }`For more information, see [Working with Access Control Rules](https://docs.aws.amazon.com/workmail/latest/adminguide/access-rules.html)in the*Amazon WorkMail Administrator Guide*.- 
                    For API details, see [GetAccessControlEffect](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/workmail/get-access-control-effect.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `get-mailbox-details`.

- **AWS CLI**
- 
            
                    **To get a user's mailbox details**The following `get-mailbox-details`command retrieves details about the specified user's mailbox.`aws workmail get-mailbox-details \ --organization-id``m-n1pq2345678r901st2u3vx45x6789yza`\ --user-id`S-1-1-11-1111111111-2222222222-3333333333-3333`Output: `{ "MailboxQuota": 51200, "MailboxSize": 0.03890800476074219 }`For more information, see [Managing User Accounts](https://docs.aws.amazon.com/workmail/latest/adminguide/manage-users.html)in the*Amazon WorkMail Administrator Guide*.- 
                    For API details, see [GetMailboxDetails](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/workmail/get-mailbox-details.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `list-access-control-rules`.

- **AWS CLI**
- 
            
                    **To list access control rules**The following `list-access-control-rules`example lists the access control rules for the specified Amazon WorkMail organization.`aws workmail list-access-control-rules \ --organization-id``m-n1pq2345678r901st2u3vx45x6789yza`Output: `{ "Rules": [ { "Name": "default", "Effect": "ALLOW", "Description": "Default WorkMail Rule", "DateCreated": 0.0, "DateModified": 0.0 }, { "Name": "myRule", "Effect": "DENY", "Description": "my rule", "UserIds": [ "S-1-1-11-1111111111-2222222222-3333333333-3333" ], "DateCreated": 1581635628.0, "DateModified": 1581635628.0 } ] }`For more information, see [Working with Access Control Rules](https://docs.aws.amazon.com/workmail/latest/adminguide/access-rules.html)in the*Amazon WorkMail Administrator Guide*.- 
                    For API details, see [ListAccessControlRules](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/workmail/list-access-control-rules.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `list-aliases`.

- **AWS CLI**
- 
            
                    **To list aliases for a member**The following `list-aliases`command lists aliases for the specified member (user or group).`aws workmail list-aliases \ --organization-id``m-d281d0a2fd824be5b6cd3d3ce909fd27`\ --entity-id`S-1-1-11-1111111111-2222222222-3333333333-3333`Output: `{ "Aliases": [ "exampleAlias@site.awsapps.com", "exampleAlias1@site.awsapps.com" ] }`- 
                    For API details, see [ListAliases](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/workmail/list-aliases.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `list-group-members`.

- **AWS CLI**
- 
            
                    **To list group members**The following `list-group-members`command lists the members of the specified group.`aws workmail list-group-members \ --organization-id``m-d281d0a2fd824be5b6cd3d3ce909fd27`\ --group-id`S-1-1-11-1122222222-2222233333-3333334444-4444`Output: `{ "Members": [ { "Id": "S-1-1-11-1111111111-2222222222-3333333333-3333", "Name": "exampleUser1", "Type": "USER", "State": "ENABLED", "EnabledDate": 1532459261.827 } ] }`- 
                    For API details, see [ListGroupMembers](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/workmail/list-group-members.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `list-groups`.

- **AWS CLI**
- 
            
                    **To retrieve a list of groups**The following `list-groups`command retrieves summaries of the groups in the specified organization.`aws workmail list-groups \ --organization-id``m-d281d0a2fd824be5b6cd3d3ce909fd27`Output: `{ "Groups": [ { "Id": "S-1-1-11-1122222222-2222233333-3333334444-4444", "Name": "exampleGroup1", "State": "DISABLED" }, { "Id": "S-4-4-44-1122222222-2222233333-3333334444-4444", "Name": "exampleGroup2", "State": "ENABLED" } ] }`- 
                    For API details, see [ListGroups](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/workmail/list-groups.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `list-mailbox-permissions`.

- **AWS CLI**
- 
            
                    **To retrieve mailbox permissions**The following `list-mailbox-permissions`command retrieves the mailbox permissions associated with the specified entity's mailbox.`aws workmail list-mailbox-permissions \ --organization-id``m-d281d0a2fd824be5b6cd3d3ce909fd27`\ --entity-id`S-1-1-11-1111111111-2222222222-3333333333-3333`Output: `{ "Permissions": [ { "GranteeId": "S-1-1-11-1122222222-2222233333-3333334444-4444", "GranteeType": "USER", "PermissionValues": [ "FULL_ACCESS" ] } ] }`- 
                    For API details, see [ListMailboxPermissions](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/workmail/list-mailbox-permissions.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `list-organizations`.

- **AWS CLI**
- 
            
                    **To retrieve a list of organizations**The following `list-organizations`command retrieves summaries of the customer's organizations.`aws workmail list-organizations`Output: `{ "OrganizationSummaries": [ { "OrganizationId": "m-d281d0a2fd824be5b6cd3d3ce909fd27", "Alias": "exampleAlias", "State": "Active" } ] }`- 
                    For API details, see [ListOrganizations](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/workmail/list-organizations.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `list-resource-delegates`.

- **AWS CLI**
- 
            
                    **To list the delegates for a resource**The following `list-resource-delegates`command retrieves the delegates associated with the specified resource.`aws workmail list-resource-delegates \ --organization-id``m-d281d0a2fd824be5b6cd3d3ce909fd27`\ --resource-id`r-68bf2d3b1c0244aab7264c24b9217443`Output: `{ "Delegates": [ { "Id": "S-1-1-11-1111111111-2222222222-3333333333-3333", "Type": "USER" } ] }`- 
                    For API details, see [ListResourceDelegates](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/workmail/list-resource-delegates.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `list-resources`.

- **AWS CLI**
- 
            
                    **To retrieve a list of resources**The following `list-resources`command retrieves summaries of the resources for the specified organization.`aws workmail list-resources \ --organization-id``m-d281d0a2fd824be5b6cd3d3ce909fd27`Output: `{ "Resources": [ { "Id": "r-7afe0efbade843a58cdc10251fce992c", "Name": "exampleRoom1", "Type": "ROOM", "State": "ENABLED" } ] }`- 
                    For API details, see [ListResources](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/workmail/list-resources.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `list-tags-for-resource`.

- **AWS CLI**
- 
            
                    **To list the tags for a resource**The following `list-tags-for-resource`example lists the tags for the specified Amazon WorkMail organization.`aws workmail list-tags-for-resource \ --resource-arn``arn:aws:workmail:us-west-2:111122223333:organization/m-n1pq2345678r901st2u3vx45x6789yza`Output: `{ "Tags": [ { "Key": "priority", "Value": "1" } ] }`For more information, see [Tagging an Organization](https://docs.aws.amazon.com/workmail/latest/adminguide/org-tag.html)in the*Amazon WorkMail Administrator Guide*.- 
                    For API details, see [ListTagsForResource](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/workmail/list-tags-for-resource.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `list-users`.

- **AWS CLI**
- 
            
                    **To retrieve a list of users**The following `list-users`command retrieves summaries of the users in the specified organization.`aws workmail list-users \ --organization-id``m-d281d0a2fd824be5b6cd3d3ce909fd27`Output: `{ "Users": [ { "Id": "S-1-1-11-1111111111-2222222222-3333333333-3333", "Email": "exampleUser1@site.awsapps.com", "Name": "exampleUser1", "State": "ENABLED", "UserRole": "USER", "EnabledDate": 1532459261.827 }, { "Id": "S-1-1-11-1122222222-2222233333-3333334444-4444", "Name": "exampleGuestUser", "State": "DISABLED", "UserRole": "SYSTEM_USER" } ] }`- 
                    For API details, see [ListUsers](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/workmail/list-users.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `put-access-control-rule`.

- **AWS CLI**
- 
            
                    **To put a new access control rule**The following `put-access-control-rule`example denies the specified user access to the specified Amazon WorkMail organization.`aws workmail put-access-control-rule \ --name``"myRule"`\ --effect`"DENY"`\ --description`"my rule"`\ --user-ids`"S-1-1-11-1111111111-2222222222-3333333333-3333"`\ --organization-id`m-n1pq2345678r901st2u3vx45x6789yza`This command produces no output. For more information, see [Working with Access Control Rules](https://docs.aws.amazon.com/workmail/latest/adminguide/access-rules.html)in the*Amazon WorkMail Administrator Guide*.- 
                    For API details, see [PutAccessControlRule](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/workmail/put-access-control-rule.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `put-mailbox-permissions`.

- **AWS CLI**
- 
            
                    **To set mailbox permissions**The following `put-mailbox-permissions`command sets full access permissions for the specified grantee (user or group). The entity represents the owner of the mailbox.`aws workmail put-mailbox-permissions \ --organization-id``m-d281d0a2fd824be5b6cd3d3ce909fd27`\ --entity-id`S-1-1-11-1111111111-2222222222-3333333333-3333`\ --grantee-id`S-1-1-11-1122222222-2222233333-3333334444-4444`\ --permission-values`FULL_ACCESS`This command produces no output. - 
                    For API details, see [PutMailboxPermissions](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/workmail/put-mailbox-permissions.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `register-to-work-mail`.

- **AWS CLI**
- 
            
                    **To register an existing or disabled entity**The following `register-to-work-mail`command enables the specified existing entity (user, group, or resource) to use Amazon WorkMail.`aws workmail register-to-work-mail \ --organization-id``m-d281d0a2fd824be5b6cd3d3ce909fd27`\ --entity-id`S-1-1-11-1122222222-2222233333-3333334444-4444`\ --email`exampleGroup1@site.awsapps.com`This command produces no output. - 
                    For API details, see [RegisterToWorkMail](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/workmail/register-to-work-mail.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `reset-password`.

- **AWS CLI**
- 
            
                    **To reset a user's password**The following `reset-password`command resets the password for the specified user.`aws workmail reset-password \ --organization-id``m-d281d0a2fd824be5b6cd3d3ce909fd27`\ --user-id`S-1-1-11-1111111111-2222222222-3333333333-3333`\ --password`examplePa$$w0rd`This command produces no output. - 
                    For API details, see [ResetPassword](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/workmail/reset-password.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `tag-resource`.

- **AWS CLI**
- 
            
                    **To apply a tag to a resource**The following `tag-resource`example applies a tag with key "priority" and value "1" to the specified Amazon WorkMail organization.`aws workmail tag-resource \ --resource-arn``arn:aws:workmail:us-west-2:111122223333:organization/m-n1pq2345678r901st2u3vx45x6789yza`\ --tags`"Key=priority,Value=1"`This command produces no output. For more information, see [Tagging an Organization](https://docs.aws.amazon.com/workmail/latest/adminguide/org-tag.html)in the*Amazon WorkMail Administrator Guide*.- 
                    For API details, see [TagResource](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/workmail/tag-resource.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `untag-resource`.

- **AWS CLI**
- 
            
                    **To untag a resource**The following `untag-resource`example removes the specified tag from the specified Amazon WorkMail organization.`aws workmail untag-resource \ --resource-arn``arn:aws:workmail:us-west-2:111122223333:organization/m-n1pq2345678r901st2u3vx45x6789yza`\ --tag-keys`"priority"`This command produces no output. For more information, see [Tagging an Organization](https://docs.aws.amazon.com/workmail/latest/adminguide/org-tag.html)in the*Amazon WorkMail Administrator Guide*.- 
                    For API details, see [UntagResource](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/workmail/untag-resource.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `update-mailbox-quota`.

- **AWS CLI**
- 
            
                    **To update a user's mailbox quota**The following `update-mailbox-quota`command changes the specified user's mailbox quota.`aws workmail update-mailbox-quota \ --organization-id``m-n1pq2345678r901st2u3vx45x6789yza`\ --user-id`S-1-1-11-1111111111-2222222222-3333333333-3333`\ --mailbox-quota`40000`This command produces no output. For more information, see [Managing User Accounts](https://docs.aws.amazon.com/workmail/latest/adminguide/manage-users.html)in the*Amazon WorkMail Administrator Guide*.- 
                    For API details, see [UpdateMailboxQuota](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/workmail/update-mailbox-quota.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `update-primary-email-address`.

- **AWS CLI**
- 
            
                    **To update a primary email address**The following `update-primary-email-address`command updates the primary email address of the specified entity (user, group, or resource).`aws workmail update-primary-email-address \ --organization-id``m-d281d0a2fd824be5b6cd3d3ce909fd27`\ --entity-id`S-1-1-11-1111111111-2222222222-3333333333-3333`\ --email`exampleUser2@site.awsapps.com`This command produces no output. - 
                    For API details, see [UpdatePrimaryEmailAddress](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/workmail/update-primary-email-address.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `update-resource`.

- **AWS CLI**
- 
            
                    **To update a resource**The following `update-resource`command updates the name of the specified resource.`aws workmail update-resource \ --organization-id``m-d281d0a2fd824be5b6cd3d3ce909fd27`\ --resource-id`r-7afe0efbade843a58cdc10251fce992c`\ --name`exampleRoom2`This command produces no output. - 
                    For API details, see [UpdateResource](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/workmail/update-resource.html)in*AWS CLI Command Reference*.
 
-