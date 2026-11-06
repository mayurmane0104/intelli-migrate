# Connect Customer examples using AWS CLI - AWS Command Line Interface

**Source:** [https://docs.aws.amazon.com/cli/latest/userguide/cli_connect_code_examples.html](https://docs.aws.amazon.com/cli/latest/userguide/cli_connect_code_examples.html)

---

The following code examples show you how to perform actions and implement common scenarios by using the AWS Command Line Interface with Connect Customer.

*Actions* are code excerpts from larger programs and must be run in context. While actions show you how to call individual service functions, you can see actions in context in their related scenarios.

Each example includes a link to the complete source code, where you can find instructions on how to set up and run the code in context.

###### Topics

## Actions

    The following code example shows how to use `create-user`.

- **AWS CLI**
- 
            
                    **To create a user**The following `create-user`example adds a user with the specified attributes to the specified Amazon Connect instance.`aws connect create-user \ --username``Mary`\ --password`Pass@Word1`\ --identity-info`FirstName=Mary,LastName=Major`\ --phone-config`PhoneType=DESK_PHONE,AutoAccept=true,AfterContactWorkTimeLimit=60,DeskPhoneNumber=+15555551212`\ --security-profile-id`12345678-1111-2222-aaaa-a1b2c3d4f5g7`\ --routing-profile-id`87654321-9999-3434-abcd-x1y2z3a1b2c3`\ --instance-id`a1b2c3d4-5678-90ab-cdef-EXAMPLE11111`Output: `{ "UserId": "87654321-2222-1234-1234-111234567891", "UserArn": "arn:aws:connect:us-west-2:123456789012:instance/a1b2c3d4-5678-90ab-cdef-EXAMPLE11111/agent/87654321-2222-1234-1234-111234567891" }`For more information, see [Add Users](https://docs.aws.amazon.com/connect/latest/adminguide/user-management.html)in the*Amazon Connect Administrator Guide*.- 
                    For API details, see [CreateUser](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/connect/create-user.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `delete-user`.

- **AWS CLI**
- 
            
                    **To delete a user**The following `delete-user`example deletes the specified user from the specified Amazon Connect instance.`aws connect delete-user \ --instance-id``a1b2c3d4-5678-90ab-cdef-EXAMPLE11111`\ --user-id`87654321-2222-1234-1234-111234567891`This command produces no output. For more information, see [Manage Users](https://docs.aws.amazon.com/connect/latest/adminguide/manage-users.html)in the*Amazon Connect Administrator Guide*.- 
                    For API details, see [DeleteUser](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/connect/delete-user.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `describe-user-hierarchy-group`.

- **AWS CLI**
- 
            
                    **To display the details for a hierarchy group**The following `describe-user-hierarchy-group`example displays the details for the specified Amazon Connect hierarchy group.`aws connect describe-user-hierarchy-group \ --hierarchy-group-id``12345678-1111-2222-800e-aaabbb555gg`\ --instance-id`a1b2c3d4-5678-90ab-cdef-EXAMPLE11111`Output: `{ "HierarchyGroup": { "Id": "12345678-1111-2222-800e-a2b3c4d5f6g7", "Arn": "arn:aws:connect:us-west-2:123456789012:instance/a1b2c3d4-5678-90ab-cdef-EXAMPLE11111/agent-group/12345678-1111-2222-800e-a2b3c4d5f6g7", "Name": "Example Corporation", "LevelId": "1", "HierarchyPath": { "LevelOne": { "Id": "abcdefgh-3333-4444-8af3-201123456789", "Arn": "arn:aws:connect:us-west-2:123456789012:instance/a1b2c3d4-5678-90ab-cdef-EXAMPLE11111/agent-group/abcdefgh-3333-4444-8af3-201123456789", "Name": "Example Corporation" } } } }`For more information, see [Set Up Agent Hierarchies](https://docs.aws.amazon.com/connect/latest/adminguide/agent-hierarchy.html)in the*Amazon Connect Administrator Guide*.- 
                    For API details, see [DescribeUserHierarchyGroup](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/connect/describe-user-hierarchy-group.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `describe-user-hierarchy-structure`.

- **AWS CLI**
- 
            
                    **To display the details for a hierarchy structure**The following `describe-user-hierarchy-structure`example displays the details for the hierarchy structure for the specified Amazon Connect instance.`aws connect describe-user-hierarchy-structure \ --instance-id``a1b2c3d4-5678-90ab-cdef-EXAMPLE11111`Output: `{ "HierarchyStructure": { "LevelOne": { "Id": "12345678-1111-2222-800e-aaabbb555gg", "Arn": "arn:aws:connect:us-west-2:123456789012:instance/a1b2c3d4-5678-90ab-cdef-EXAMPLE11111/agent-group-level/1", "Name": "Corporation" }, "LevelTwo": { "Id": "87654321-2222-3333-ac99-123456789102", "Arn": "arn:aws:connect:us-west-2:123456789012:instance/a1b2c3d4-5678-90ab-cdef-EXAMPLE11111/agent-group-level/2", "Name": "Services Division" }, "LevelThree": { "Id": "abcdefgh-3333-4444-8af3-201123456789", "Arn": "arn:aws:connect:us-west-2:123456789012:instance/a1b2c3d4-5678-90ab-cdef-EXAMPLE11111/agent-group-level/3", "Name": "EU Site" } } }`For more information, see [Set Up Agent Hierarchies](https://docs.aws.amazon.com/connect/latest/adminguide/agent-hierarchy.html)in the*Amazon Connect Administrator Guide*.- 
                    For API details, see [DescribeUserHierarchyStructure](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/connect/describe-user-hierarchy-structure.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `describe-user`.

- **AWS CLI**
- 
            
                    **To display the details for a user**The following `describe-user`example displays the details for the specified Amazon Connect user.`aws connect describe-user \ --user-id``0c245dc0-0cf5-4e37-800e-2a7481cc8a60`--instance-id`40c83b68-ea62-414c-97bb-d018e39e158e`Output: `{ "User": { "Id": "0c245dc0-0cf5-4e37-800e-2a7481cc8a60", "Arn": "arn:aws:connect:us-west-2:123456789012:instance/40c83b68-ea62-414c-97bb-d018e39e158e/agent/0c245dc0-0cf5-4e37-800e-2a7481cc8a60", "Username": "Jane", "IdentityInfo": { "FirstName": "Jane", "LastName": "Doe", "Email": "example.com" }, "PhoneConfig": { "PhoneType": "SOFT_PHONE", "AutoAccept": false, "AfterContactWorkTimeLimit": 0, "DeskPhoneNumber": "" }, "DirectoryUserId": "8b444cf6-b368-4f29-ba18-07af27405658", "SecurityProfileIds": [ "b6f85a42-1dc5-443b-b621-de0abf70c9cf" ], "RoutingProfileId": "0be36ee9-2b5f-4ef4-bcf7-87738e5be0e5", "Tags": {} } }`For more information, see [Manage Users](https://docs.aws.amazon.com/connect/latest/adminguide/manage-users.html)in the*Amazon Connect Administrator Guide*.- 
                    For API details, see [DescribeUser](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/connect/describe-user.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `get-contact-attributes`.

- **AWS CLI**
- 
            
                    **To retrieve the attributes for a contact**The following `get-contact-attributes`example retrieves the attributes that were set for the specified Amazon Connect contact.`aws connect get-contact-attributes \ --instance-id``a1b2c3d4-5678-90ab-cdef-EXAMPLE11111`\ --initial-contact-id`12345678-1111-2222-800e-a2b3c4d5f6g7`Output: `{ "Attributes": { "greetingPlayed": "true" } }`For more information, see [Use Amazon Connect Contact Attributes](https://docs.aws.amazon.com/connect/latest/adminguide/connect-contact-attributes.html)in the*Amazon Connect Administrator Guide*.- 
                    For API details, see [GetContactAttributes](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/connect/get-contact-attributes.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `list-contact-flows`.

- **AWS CLI**
- 
            
                    **To list the contact flows in an instance**The following `list-contact-flows`example lists the contact flows in the specified Amazon Connect instance.`aws connect list-contact-flows \ --instance-id``a1b2c3d4-5678-90ab-cdef-EXAMPLE11111`Output: `{ "ContactFlowSummaryList": [ { "Id": "12345678-1111-2222-800e-a2b3c4d5f6g7", "Arn": "arn:aws:connect:us-west-2:123456789012:instance/a1b2c3d4-5678-90ab-cdef-EXAMPLE11111/contact-flow/12345678-1111-2222-800e-a2b3c4d5f6g7", "Name": "Default queue transfer", "ContactFlowType": "QUEUE_TRANSFER" }, { "Id": "87654321-2222-3333-ac99-123456789102", "Arn": "arn:aws:connect:us-west-2:123456789012:instance/a1b2c3d4-5678-90ab-cdef-EXAMPLE11111/contact-flow/87654321-2222-3333-ac99-123456789102", "Name": "Default agent hold", "ContactFlowType": "AGENT_HOLD" }, { "Id": "abcdefgh-3333-4444-8af3-201123456789", "Arn": "arn:aws:connect:us-west-2:123456789012:instance/a1b2c3d4-5678-90ab-cdef-EXAMPLE11111/contact-flow/abcdefgh-3333-4444-8af3-201123456789", "Name": "Default customer hold", "ContactFlowType": "CUSTOMER_HOLD" }, ] }`For more information, see [Create Amazon Connect Contact Flows](https://docs.aws.amazon.com/connect/latest/adminguide/connect-contact-flows.html)in the*Amazon Connect Administrator Guide*.- 
                    For API details, see [ListContactFlows](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/connect/list-contact-flows.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `list-hours-of-operations`.

- **AWS CLI**
- 
            
                    **To list the hours of operation in an instance**The following `list-hours-of-operations`example lists the hours of operations for the specified Amazon Connect instance.`aws connect list-hours-of-operations \ --instance-id``40c83b68-ea62-414c-97bb-d018e39e158e`Output: `{ "HoursOfOperationSummaryList": [ { "Id": "d69f1f84-7457-4924-8fbe-e64875546259", "Arn": "arn:aws:connect:us-west-2:123456789012:instance/40c83b68-ea62-414c-97bb-d018e39e158e/operating-hours/d69f1f84-7457-4924-8fbe-e64875546259", "Name": "Basic Hours" } ] }`For more information, see [Set the Hours of Operation for a Queue](https://docs.aws.amazon.com/connect/latest/adminguide/set-hours-operation.html)in the*Amazon Connect Administrator Guide*.- 
                    For API details, see [ListHoursOfOperations](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/connect/list-hours-of-operations.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `list-phone-numbers`.

- **AWS CLI**
- 
            
                    **To list the phone numbers in an instance**The following `list-phone-numbers`example lists the phone numbers in the specified Amazon Connect instance.`aws connect list-phone-numbers \ --instance-id``a1b2c3d4-5678-90ab-cdef-EXAMPLE11111`Output: `{ "PhoneNumberSummaryList": [ { "Id": "a1b2c3d4-5678-90ab-cdef-EXAMPLE11111", "Arn": "arn:aws:connect:us-west-2:123456789012:instance/a1b2c3d4-5678-90ab-cdef-EXAMPLE11111/phone-number/xyz80zxy-xyz1-80zx-zx80-11111EXAMPLE", "PhoneNumber": "+17065551212", "PhoneNumberType": "DID", "PhoneNumberCountryCode": "US" }, { "Id": "a1b2c3d4-5678-90ab-cdef-EXAMPLE22222", "Arn": "arn:aws:connect:us-west-2:123456789012:instance/a1b2c3d4-5678-90ab-cdef-EXAMPLE11111/phone-number/ccc0ccc-xyz1-80zx-zx80-22222EXAMPLE", "PhoneNumber": "+18555551212", "PhoneNumberType": "TOLL_FREE", "PhoneNumberCountryCode": "US" } ] }`For more information, see [Set Up Phone Numbers for Your Contact Center](https://docs.aws.amazon.com/connect/latest/adminguide/contact-center-phone-number.html)in the*Amazon Connect Administrator Guide*.- 
                    For API details, see [ListPhoneNumbers](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/connect/list-phone-numbers.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `list-queues`.

- **AWS CLI**
- 
            
                    **To list the queues in an instance**The following `list-queues`example lists the queues in the specified Amazon Connect instance.`aws connect list-queues \ --instance-id``a1b2c3d4-5678-90ab-cdef-EXAMPLE11111`Output: `{ "QueueSummaryList": [ { "Id": "12345678-1111-2222-800e-a2b3c4d5f6g7", "Arn": "arn:aws:connect:us-west-2:123456789012:instance/a1b2c3d4-5678-90ab-cdef-EXAMPLE11111/queue/agent/12345678-1111-2222-800e-a2b3c4d5f6g7", "QueueType": "AGENT" }, { "Id": "87654321-2222-3333-ac99-123456789102", "Arn": "arn:aws:connect:us-west-2:123456789012:instance/a1b2c3d4-5678-90ab-cdef-EXAMPLE11111/queue/agent/87654321-2222-3333-ac99-123456789102", "QueueType": "AGENT" }, { "Id": "abcdefgh-3333-4444-8af3-201123456789", "Arn": "arn:aws:connect:us-west-2:123456789012:instance/a1b2c3d4-5678-90ab-cdef-EXAMPLE11111/queue/agent/abcdefgh-3333-4444-8af3-201123456789", "QueueType": "AGENT" }, { "Id": "hgfedcba-4444-5555-a31f-123456789102", "Arn": "arn:aws:connect:us-west-2:123456789012:instance/a1b2c3d4-5678-90ab-cdef-EXAMPLE11111/queue/hgfedcba-4444-5555-a31f-123456789102", "Name": "BasicQueue", "QueueType": "STANDARD" }, ] }`For more information, see [Create a Queue](https://docs.aws.amazon.com/connect/latest/adminguide/create-queue.html)in the*Amazon Connect Administrator Guide*.- 
                    For API details, see [ListQueues](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/connect/list-queues.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `list-routing-profiles`.

- **AWS CLI**
- 
            
                    **To list the routing profiles in an instance**The following `list-routing-profiles`example lists the routing profiles in the specified Amazon Connect instance.`aws connect list-routing-profiles \ --instance-id``a1b2c3d4-5678-90ab-cdef-EXAMPLE11111`Output: `{ "RoutingProfileSummaryList": [ { "Id": "12345678-1111-2222-800e-a2b3c4d5f6g7", "Arn": "arn:aws:connect:us-west-2:123456789012:instance/a1b2c3d4-5678-90ab-cdef-EXAMPLE11111/routing-profile/12345678-1111-2222-800e-a2b3c4d5f6g7", "Name": "Basic Routing Profile" }, ] }`For more information, see [Create a Routing Profile](https://docs.aws.amazon.com/connect/latest/adminguide/routing-profiles.html)in the*Amazon Connect Administrator Guide*.- 
                    For API details, see [ListRoutingProfiles](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/connect/list-routing-profiles.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `list-security-profiles`.

- **AWS CLI**
- 
            
                    **To list the security profiles in an instance**The following `list-security-profiles`example lists the security profiles in the specified Amazon Connect instance.`aws connect list-security-profiles \ --instance-id``a1b2c3d4-5678-90ab-cdef-EXAMPLE11111`Output: `{ "SecurityProfileSummaryList": [ { "Id": "12345678-1111-2222-800e-a2b3c4d5f6g7", "Arn": "arn:aws:connect:us-west-2:123456789012:instance/a1b2c3d4-5678-90ab-cdef-EXAMPLE11111/security-profile/12345678-1111-2222-800e-a2b3c4d5f6g7", "Name": "CallCenterManager" }, { "Id": "87654321-2222-3333-ac99-123456789102", "Arn": "arn:aws:connect:us-west-2:123456789012:instance/a1b2c3d4-5678-90ab-cdef-EXAMPLE11111/security-profile/87654321-2222-3333-ac99-123456789102", "Name": "QualityAnalyst" }, { "Id": "abcdefgh-3333-4444-8af3-201123456789", "Arn": "arn:aws:connect:us-west-2:123456789012:instance/a1b2c3d4-5678-90ab-cdef-EXAMPLE11111/security-profile/abcdefgh-3333-4444-8af3-201123456789", "Name": "Agent" }, { "Id": "12345678-1111-2222-800e-x2y3c4d5fzzzz", "Arn": "arn:aws:connect:us-west-2:123456789012:instance/a1b2c3d4-5678-90ab-cdef-EXAMPLE11111/security-profile/12345678-1111-2222-800e-x2y3c4d5fzzzz", "Name": "Admin" } ] }`For more information, see [Assign Permissions: Security Profiles](https://docs.aws.amazon.com/connect/latest/adminguide/connect-security-profiles.html)in the*Amazon Connect Administrator Guide*.- 
                    For API details, see [ListSecurityProfiles](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/connect/list-security-profiles.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `list-user-hierarchy-groups`.

- **AWS CLI**
- 
            
                    **To list the user hierarchy groups in an instance**The following `list-user-hierarchy-groups`example lists the user hierarchy groups in the specified Amazon Connect instance.`aws connect list-user-hierarchy-groups \ --instance-id``40c83b68-ea62-414c-97bb-d018e39e158e`Output: `{ "UserHierarchyGroupSummaryList": [ { "Id": "0e2f6d1d-b3ca-494b-8dbc-ba81d9f8182a", "Arn": "arn:aws:connect:us-west-2:123456789012:instance/40c83b68-ea62-414c-97bb-d018e39e158e/agent-group/0e2f6d1d-b3ca-494b-8dbc-ba81d9f8182a", "Name": "Example Corporation" }, ] }`For more information, see [Set Up Agent Hierarchies](https://docs.aws.amazon.com/connect/latest/adminguide/agent-hierarchy.html)in the*Amazon Connect Administrator Guide*.- 
                    For API details, see [ListUserHierarchyGroups](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/connect/list-user-hierarchy-groups.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `list-users`.

- **AWS CLI**
- 
            
                    **To list the user hierarchy groups in an instance**The following `list-users`example lists the users in the specified Amazon Connect instance.`aws connect list-users \ --instance-id``40c83b68-ea62-414c-97bb-d018e39e158e`Output: `{ "UserSummaryList": [ { "Id": "0c245dc0-0cf5-4e37-800e-2a7481cc8a60", "Arn": "arn:aws:connect:us-west-2:123456789012:instance/40c83b68-ea62-414c-97bb-d018e39e158e/agent/0c245dc0-0cf5-4e37-800e-2a7481cc8a60", "Username": "Jane" }, { "Id": "46f0c67c-3fc7-4806-ac99-403798788c14", "Arn": "arn:aws:connect:us-west-2:123456789012:instance/40c83b68-ea62-414c-97bb-d018e39e158e/agent/46f0c67c-3fc7-4806-ac99-403798788c14", "Username": "Paulo" }, { "Id": "55a83578-95e1-4710-8af3-2b7afe310e48", "Arn": "arn:aws:connect:us-west-2:123456789012:instance/40c83b68-ea62-414c-97bb-d018e39e158e/agent/55a83578-95e1-4710-8af3-2b7afe310e48", "Username": "JohnD" }, { "Id": "703e27b5-c9f0-4f1f-a239-64ccbb160125", "Arn": "arn:aws:connect:us-west-2:123456789012:instance/40c83b68-ea62-414c-97bb-d018e39e158e/agent/703e27b5-c9f0-4f1f-a239-64ccbb160125", "Username": "JohnS" } ] }`For more information, see [Add Users](https://docs.aws.amazon.com/connect/latest/adminguide/user-management.html)in the*Amazon Connect Administrator Guide*.- 
                    For API details, see [ListUsers](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/connect/list-users.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `update-contact-attributes`.

- **AWS CLI**
- 
            
                    **To update a contact's attribute**The following `update-contact-attributes`example updates the`greetingPlayed`attribute for the specified Amazon Connect user.`aws connect update-contact-attributes \ --initial-contact-id``11111111-2222-3333-4444-12345678910`\ --instance-id`a1b2c3d4-5678-90ab-cdef-EXAMPLE11111`\ --attributes`greetingPlayed=false`This command produces no output. For more information, see [Use Amazon Connect Contact Attributes](https://docs.aws.amazon.com/connect/latest/adminguide/connect-contact-attributes.html)in the*Amazon Connect Administrator Guide*.- 
                    For API details, see [UpdateContactAttributes](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/connect/update-contact-attributes.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `update-user-hierarchy`.

- **AWS CLI**
- 
            
                    **To update a user's hierarchy**The following `update-user-hierarchy`example updates the agent hierarchy for the specified Amazon Connect user.`aws connect update-user-hierarchy \ --hierarchy-group-id``12345678-a1b2-c3d4-e5f6-123456789abc`\ --user-id`87654321-2222-1234-1234-111234567891`\ --instance-id`a1b2c3d4-5678-90ab-cdef-EXAMPLE11111`This command produces no output. For more information, see [Configure Agent Settings](https://docs.aws.amazon.com/connect/latest/adminguide/configure-agents.html)in the*Amazon Connect Administrator Guide*.- 
                    For API details, see [UpdateUserHierarchy](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/connect/update-user-hierarchy.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `update-user-identity-info`.

- **AWS CLI**
- 
            
                    **To update a user's identity information**The following `update-user-identity-info`example updates the identity information for the specified Amazon Connect user.`aws connect update-user-identity-info \ --identity-info``FirstName=Mary,LastName=Major,Email=marym@example.com`\ --user-id`87654321-2222-1234-1234-111234567891`\ --instance-id`a1b2c3d4-5678-90ab-cdef-EXAMPLE11111`This command produces no output. For more information, see [Configure Agent Settings](https://docs.aws.amazon.com/connect/latest/adminguide/configure-agents.html)in the*Amazon Connect Administrator Guide*.- 
                    For API details, see [UpdateUserIdentityInfo](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/connect/update-user-identity-info.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `update-user-phone-config`.

- **AWS CLI**
- 
            
                    **To update a user's phone configuration**The following `update-user-phone-config`example updates the phone configuration for the specified user.`aws connect update-user-phone-config \ --phone-config``PhoneType=SOFT_PHONE,AutoAccept=false,AfterContactWorkTimeLimit=60,DeskPhoneNumber=+18005551212`\ --user-id`12345678-4444-3333-2222-111122223333`\ --instance-id`a1b2c3d4-5678-90ab-cdef-EXAMPLE11111`This command produces no output. For more information, see [Configure Agent Settings](https://docs.aws.amazon.com/connect/latest/adminguide/configure-agents.html)in the*Amazon Connect Administrator Guide*.- 
                    For API details, see [UpdateUserPhoneConfig](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/connect/update-user-phone-config.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `update-user-routing-profile`.

- **AWS CLI**
- 
            
                    **To update a user's routing profile**The following `update-user-routing-profile`example updates the routing profile for the specified Amazon Connect user.`aws connect update-user-routing-profile \ --routing-profile-id``12345678-1111-3333-2222-4444EXAMPLE`\ --user-id`87654321-2222-1234-1234-111234567891`\ --instance-id`a1b2c3d4-5678-90ab-cdef-EXAMPLE11111`This command produces no output. For more information, see [Configure Agent Settings](https://docs.aws.amazon.com/connect/latest/adminguide/configure-agents.html)in the*Amazon Connect Administrator Guide*.- 
                    For API details, see [UpdateUserRoutingProfile](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/connect/update-user-routing-profile.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `update-user-security-profiles`.

- **AWS CLI**
- 
            
                    **To update a user's security profiles**The following `update-user-security-profiles`example updates the security profile for the specified Amazon Connect user.`aws connect update-user-security-profiles \ --security-profile-ids``12345678-1234-1234-1234-1234567892111`\ --user-id`87654321-2222-1234-1234-111234567891`\ --instance-id`a1b2c3d4-5678-90ab-cdef-EXAMPLE11111`This command produces no output. For more information, see [Assign Permissions: Security Profiles](https://docs.aws.amazon.com/connect/latest/adminguide/connect-security-profiles.html)in the*Amazon Connect Administrator Guide*.- 
                    For API details, see [UpdateUserSecurityProfiles](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/connect/update-user-security-profiles.html)in*AWS CLI Command Reference*.
 
-