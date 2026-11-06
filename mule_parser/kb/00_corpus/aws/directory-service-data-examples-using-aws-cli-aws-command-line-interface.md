# Directory Service Data examples using AWS CLI - AWS Command Line Interface

**Source:** [https://docs.aws.amazon.com/cli/latest/userguide/cli_directory-service-data_code_examples.html](https://docs.aws.amazon.com/cli/latest/userguide/cli_directory-service-data_code_examples.html)

---

The following code examples show you how to perform actions and implement common scenarios by using the AWS Command Line Interface with Directory Service Data.

*Actions* are code excerpts from larger programs and must be run in context. While actions show you how to call individual service functions, you can see actions in context in their related scenarios.

Each example includes a link to the complete source code, where you can find instructions on how to set up and run the code in context.

###### Topics

## Actions

    The following code example shows how to use `add-group-member`.

- **AWS CLI**
- 
            
                    **To add a group member to a directory**The following `add-group-member`example adds the specified user to the specified group in the specified directory.`aws ds-data add-group-member \ --directory-id``d-1234567890`\ --group-name '`sales`' \ --member-name '`john.doe`'This command produces no output. For more information, see [Adding or removing AWS Managed Microsoft AD members to groups and groups to groups](https://docs.aws.amazon.com/directoryservice/latest/admin-guide/ms_ad_add_remove_user_group.html)in the*AWS Directory Service Administration Guide*.- 
                    For API details, see [AddGroupMember](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/directory-service-data/add-group-member.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `create-group`.

- **AWS CLI**
- 
            
                    **To list the available widgets**The following `create-group`example creates a group in a specified directory.`aws ds-data create-group \ --directory-id``d-1234567890`\ --sam-account-name`"sales"`Output: `{ "DirectoryId": "d-1234567890", "SAMAccountName": "sales", "SID": "S-1-2-34-5567891234-5678912345-67891234567-8912" }`For more information, see [Creating an AWS Managed Microsoft AD group](https://docs.aws.amazon.com/directoryservice/latest/admin-guide/ms_ad_create_group.html)in the*AWS Directory Service Administration Guide*.- 
                    For API details, see [CreateGroup](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/directory-service-data/create-group.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `create-user`.

- **AWS CLI**
- 
            
                    **To create a user**The following `create-user`example creates a user in the specified directory.`aws ds-data create-user \ --directory-id``d-1234567890`\ --sam-account-name '`john.doe`'Output: `{ "DirectoryId": "d-1234567890", "SAMAccountName": "john.doe", "SID": "S-1-2-34-5567891234-5678912345-67891234567-8912" }`For more information, see [Creating an AWS Managed Microsoft AD user](https://docs.aws.amazon.com/directoryservice/latest/admin-guide/ms_ad_create_user.html)in the*AWS Directory Service Administration Guide*.- 
                    For API details, see [CreateUser](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/directory-service-data/create-user.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `delete-group`.

- **AWS CLI**
- 
            
                    **To delete a group**The following `delete-group`example deletes the specified group from the specified directory.`aws ds-data delete-group \ --directory-id``d-1234567890`\ --sam-account-name '`sales`'This command produces no output. For more information, see [Deleting an AWS Managed Microsoft AD group](https://docs.aws.amazon.com/directoryservice/latest/admin-guide/ms_ad_delete_group.html)in the*AWS Directory Service Administration Guide*.- 
                    For API details, see [DeleteGroup](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/directory-service-data/delete-group.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `delete-user`.

- **AWS CLI**
- 
            
                    **To delete a user**The following `delete-user`example deletes the specified user from the specified directory.`aws ds-data delete-user \ --directory-id``d-1234567890`\ --sam-account-name '`john.doe`'This command produces no output. For more information, see [Deleting an AWS Managed Microsoft AD user](https://docs.aws.amazon.com/directoryservice/latest/admin-guide/ms_ad_delete_user.html)in the*AWS Directory Service Administration Guide*.- 
                    For API details, see [DeleteUser](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/directory-service-data/delete-user.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `describe-group`.

- **AWS CLI**
- 
            
                    **To list details of a group**The following `describe-group`example gets information for the specified group in the specified directory.`aws ds-data describe-group \ --directory-id``d-1234567890`\ --sam-account-name '`sales`'Output: `{ "DirectoryId": "d-1234567890", "DistinguishedName": "CN=sales,OU=Users,OU=CORP,DC=corp,DC=example,DC=com", "GroupScope": "Global", "GroupType": "Security", "Realm": "corp.example.com", "SAMAccountName": "sales", "SID": "S-1-2-34-5567891234-5678912345-67891234567-8912" }`For more information, see [Viewing and updating an AWS Managed Microsoft AD group's details](https://docs.aws.amazon.com/directoryservice/latest/admin-guide/ms_ad_view_update_group.html)in the*AWS Directory Service Administration Guide*.- 
                    For API details, see [DescribeGroup](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/directory-service-data/describe-group.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `describe-user`.

- **AWS CLI**
- 
            
                    **To list information for a user**The following `describe-user`example gets information for the specified user in the specified directory.`aws ds-data describe-user``command-name`\ --directory-id`d-1234567890`\ --sam-account-name '`john.doe`'Output: `{ "DirectoryId": "d-1234567890", "DistinguishedName": "CN=john.doe,OU=Users,OU=CORP,DC=corp,DC=example,DC=com", "Enabled": false, "Realm": "corp.example.com", "SAMAccountName": "john.doe", "SID": "S-1-2-34-5678901234-5678901234-5678910123-4567", "UserPrincipalName": "john.doe@CORP.EXAMPLE.COM" }`For more information, see [Viewing and updating an AWS Managed Microsoft AD user](https://docs.aws.amazon.com/directoryservice/latest/admin-guide/ms_ad_view_update_user.html)in the*AWS Directory Service Administration Guide*.- 
                    For API details, see [DescribeUser](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/directory-service-data/describe-user.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `disable-directory-data-access`.

- **AWS CLI**
- 
            
                    **To disable Directory Service Data API for a directory**The following `disable-directory-data-access`example disables the Directory Service Data API for the specified directory.`aws ds disable-directory-data-access \ --directory-id``d-1234567890`This command produces no output. For more information, see [Enabling or disabling user and group management or AWS Directory Service Data](https://docs.aws.amazon.com/directoryservice/latest/admin-guide/ms_ad_users_groups_mgmt_enable_disable.html)in the*AWS Directory Service Administration Guide*.- 
                    For API details, see [DisableDirectoryDataAccess](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/directory-service-data/disable-directory-data-access.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `disable-user`.

- **AWS CLI**
- 
            
                    **To disable a user**The following `disable-user`example disables the specified user in the specified directory.`aws ds-data disable-user \ --directory-id``d-1234567890`\ --sam-account-name '`john.doe`'This command produces no output. For more information, see [Disabling an AWS Managed Microsoft AD user](https://docs.aws.amazon.com/directoryservice/latest/admin-guide/ms_ad_disable_user.html)in the*AWS Directory Service Administration Guide*.- 
                    For API details, see [DisableUser](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/directory-service-data/disable-user.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `enable-directory-data-access`.

- **AWS CLI**
- 
            
                    **To enable Directory Service Data API for a directory**The following `enable-directory-data-access`example enables the Directory Service Data API for the specified directory.`aws ds enable-directory-data-access \ --directory-id``d-1234567890`This command produces no output. For more information, see [Enabling or disabling user and group management or AWS Directory Service Data](https://docs.aws.amazon.com/directoryservice/latest/admin-guide/ms_ad_users_groups_mgmt_enable_disable.html)in the*AWS Directory Service Administration Guide*.- 
                    For API details, see [EnableDirectoryDataAccess](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/directory-service-data/enable-directory-data-access.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `list-group-members`.

- **AWS CLI**
- 
            
                    **To list a directory's group members**The following `list-group-members`example lists the group members for the specified group in the specified directory.`aws ds-data list-group-members \ --directory-id``d-1234567890`\ --sam-account-name '`sales`'Output: `{ "Members": [ { "MemberType": "USER", "SAMAccountName": "Jane Doe", "SID": "S-1-2-34-5678901234-5678901234-5678910123-4568" }, { "MemberType": "USER", "SAMAccountName": "John Doe", "SID": "S-1-2-34-5678901234-5678901234-5678910123-4569" } ], "DirectoryId": "d-1234567890", "MemberRealm": "corp.example.com", "Realm": "corp.example.com" }`For more information, see [Viewing and updating an AWS Managed Microsoft AD group's details](https://docs.aws.amazon.com/directoryservice/latest/admin-guide/ms_ad_view_update_group.html)in the*AWS Directory Service Administration Guide*.- 
                    For API details, see [ListGroupMembers](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/directory-service-data/list-group-members.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `list-groups-for-member`.

- **AWS CLI**
- 
            
                    **To list a directory's group membership**The following `list-groups-for-member`example lists group membership for the specified user in the specified directory.`aws ds-data list-groups-for-member \ --directory-id``d-1234567890`\ --sam-account-name '`john.doe`'Output: `{ "Groups": [ { "GroupScope": "Global", "GroupType": "Security", "SAMAccountName": "Domain Users", "SID": "S-1-2-34-5678901234-5678901234-5678910123-4567" } ], "DirectoryId": "d-1234567890", "MemberRealm": "corp.example.com", "Realm": "corp.example.com" }`For more information, see [Viewing and updating an AWS Managed Microsoft AD user](https://docs.aws.amazon.com/directoryservice/latest/admin-guide/ms_ad_view_update_user.html)in the*AWS Directory Service Administration Guide*.- 
                    For API details, see [ListGroupsForMember](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/directory-service-data/list-groups-for-member.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `list-groups`.

- **AWS CLI**
- 
            
                    **To list a directory's groups**The following `list-groups`example lists groups in the specified directory.`aws ds-data list-groups \ --directory-id``d-1234567890`Output: `{ "Groups": [ { "GroupScope": "BuiltinLocal", "GroupType": "Security", "SAMAccountName": "Administrators", "SID": "S-1-2-33-441" }, { "GroupScope": "BuiltinLocal", "GroupType": "Security", "SAMAccountName": "Users", "SID": "S-1-2-33-442" }, { "GroupScope": "BuiltinLocal", "GroupType": "Security", "SAMAccountName": "Guests", "SID": "S-1-2-33-443" }, { "GroupScope": "BuiltinLocal", "GroupType": "Security", "SAMAccountName": "Print Operators", "SID": "S-1-2-33-444" }, { "GroupScope": "BuiltinLocal", "GroupType": "Security", "SAMAccountName": "Backup Operators", "SID": "S-1-2-33-445" }, { "GroupScope": "BuiltinLocal", "GroupType": "Security", "SAMAccountName": "Replicator", "SID": "S-1-2-33-446" }, { "GroupScope": "BuiltinLocal", "GroupType": "Security", "SAMAccountName": "Remote Desktop Users", "SID": "S-1-2-33-447" }, { "GroupScope": "BuiltinLocal", "GroupType": "Security", "SAMAccountName": "Network Configuration Operators", "SID": "S-1-2-33-448" }, { "GroupScope": "BuiltinLocal", "GroupType": "Security", "SAMAccountName": "Performance Monitor Users", "SID": "S-1-2-33-449" }, { "GroupScope": "BuiltinLocal", "GroupType": "Security", "SAMAccountName": "Performance Log Users", "SID": "S-1-2-33-450" }, { "GroupScope": "BuiltinLocal", "GroupType": "Security", "SAMAccountName": "Distributed COM Users", "SID": "S-1-2-33-451" }, { "GroupScope": "BuiltinLocal", "GroupType": "Security", "SAMAccountName": "IIS_IUSRS", "SID": "S-1-2-33-452" }, { "GroupScope": "BuiltinLocal", "GroupType": "Security", "SAMAccountName": "Cryptographic Operators", "SID": "S-1-2-33-453" }, { "GroupScope": "BuiltinLocal", "GroupType": "Security", "SAMAccountName": "Event Log Readers", "SID": "S-1-2-33-454" }, { "GroupScope": "BuiltinLocal", "GroupType": "Security", "SAMAccountName": "Certificate Service DCOM Access", "SID": "S-1-2-33-456" }, { "GroupScope": "BuiltinLocal", "GroupType": "Security", "SAMAccountName": "RDS Remote Access Servers", "SID": "S-1-2-33-457" }, { "GroupScope": "BuiltinLocal", "GroupType": "Security", "SAMAccountName": "RDS Endpoint Servers", "SID": "S-1-2-33-458" }, { "GroupScope": "BuiltinLocal", "GroupType": "Security", "SAMAccountName": "RDS Management Servers", "SID": "S-1-2-33-459" }, { "GroupScope": "BuiltinLocal", "GroupType": "Security", "SAMAccountName": "Hyper-V Administrators", "SID": "S-1-2-33-460" }, { "GroupScope": "BuiltinLocal", "GroupType": "Security", "SAMAccountName": "Access Control Assistance Operators", "SID": "S-1-2-33-461" }, { "GroupScope": "BuiltinLocal", "GroupType": "Security", "SAMAccountName": "Remote Management Users", "SID": "S-1-2-33-462" }, { "GroupScope": "BuiltinLocal", "GroupType": "Security", "SAMAccountName": "Storage Replica Administrators", "SID": "S-1-2-33-463" }, { "GroupScope": "Global", "GroupType": "Security", "SAMAccountName": "Domain Computers", "SID": "S-1-2-34-56789123456-7891012345-6789123486-789" }, { "GroupScope": "Global", "GroupType": "Security", "SAMAccountName": "Domain Controllers", "SID": "S-1-2-34-56789123456-7891012345-6789123486-790" }, { "GroupScope": "Universal", "GroupType": "Security", "SAMAccountName": "Schema Admins", "SID": "S-1-2-34-56789123456-7891012345-6789123486-791" }, { "GroupScope": "Universal", "GroupType": "Security", "SAMAccountName": "Enterprise Admins", "SID": "S-1-2-34-56789123456-7891012345-6789123486-792" }, { "GroupScope": "DomainLocal", "GroupType": "Security", "SAMAccountName": "Cert Publishers", "SID": "S-1-2-34-56789123456-7891012345-6789123486-793" }, { "GroupScope": "Global", "GroupType": "Security", "SAMAccountName": "Domain Admins", "SID": "S-1-2-34-56789123456-7891012345-6789123486-794" }, { "GroupScope": "Global", "GroupType": "Security", "SAMAccountName": "Domain Users", "SID": "S-1-2-34-56789123456-7891012345-6789123486-795" }, { "GroupScope": "Global", "GroupType": "Security", "SAMAccountName": "Domain Guests", "SID": "S-1-2-34-56789123456-7891012345-6789123486-796" }, { "GroupScope": "Global", "GroupType": "Security", "SAMAccountName": "Group Policy Creator Owners", "SID": "S-1-2-34-56789123456-7891012345-6789123486-797" }, { "GroupScope": "DomainLocal", "GroupType": "Security", "SAMAccountName": "RAS and IAS Servers", "SID": "S-1-2-34-56789123456-7891012345-6789123486-798" }, { "GroupScope": "BuiltinLocal", "GroupType": "Security", "SAMAccountName": "Server Operators", "SID": "S-1-2-33-464" }, { "GroupScope": "BuiltinLocal", "GroupType": "Security", "SAMAccountName": "Account Operators", "SID": "S-1-2-33-465" }, { "GroupScope": "BuiltinLocal", "GroupType": "Security", "SAMAccountName": "Pre-Windows 2000 Compatible Access", "SID": "S-1-2-33-466" }, { "GroupScope": "BuiltinLocal", "GroupType": "Security", "SAMAccountName": "Incoming Forest Trust Builders", "SID": "S-1-2-33-467" }, { "GroupScope": "BuiltinLocal", "GroupType": "Security", "SAMAccountName": "Windows Authorization Access Group", "SID": "S-1-2-33-468" }, { "GroupScope": "BuiltinLocal", "GroupType": "Security", "SAMAccountName": "Terminal Server License Servers", "SID": "S-1-2-33-469" }, { "GroupScope": "DomainLocal", "GroupType": "Security", "SAMAccountName": "Allowed RODC Password Replication Group", "SID": "S-1-2-34-56789123456-7891012345-6789123486-798" }, { "GroupScope": "DomainLocal", "GroupType": "Security", "SAMAccountName": "Denied RODC Password Replication Group", "SID": "S-1-2-34-56789123456-7891012345-6789123486-799" }, { "GroupScope": "Global", "GroupType": "Security", "SAMAccountName": "Read-only Domain Controllers", "SID": "S-1-2-34-56789123456-7891012345-6789123486-800" }, { "GroupScope": "Universal", "GroupType": "Security", "SAMAccountName": "Enterprise Read-only Domain Controllers", "SID": "S-1-2-34-56789123456-7891012345-6789123486-801" }, { "GroupScope": "Global", "GroupType": "Security", "SAMAccountName": "Cloneable Domain Controllers", "SID": "S-1-2-34-56789123456-7891012345-6789123486-802" }, { "GroupScope": "Global", "GroupType": "Security", "SAMAccountName": "Protected Users", "SID": "S-1-2-34-56789123456-7891012345-6789123486-803" }, { "GroupScope": "Global", "GroupType": "Security", "SAMAccountName": "Key Admins", "SID": "S-1-2-34-56789123456-7891012345-6789123486-804" }, { "GroupScope": "Universal", "GroupType": "Security", "SAMAccountName": "Enterprise Key Admins", "SID": "S-1-2-34-56789123456-7891012345-6789123486-805" }, { "GroupScope": "DomainLocal", "GroupType": "Security", "SAMAccountName": "DnsAdmins", "SID": "S-1-2-34-5678901234-5678901234-5678910123-4567" }, { "GroupScope": "Global", "GroupType": "Security", "SAMAccountName": "DnsUpdateProxy", "SID": "S-1-2-34-5678901234-5678901234-5678910123-4568" }, { "GroupScope": "DomainLocal", "GroupType": "Security", "SAMAccountName": "Admins", "SID": "S-1-2-34-5678901234-5678901234-5678910123-4569" }, { "GroupScope": "DomainLocal", "GroupType": "Security", "SAMAccountName": "AWSAdministrators", "SID": "S-1-2-34-5678901234-5678901234-5678910123-4570" }, { "GroupScope": "DomainLocal", "GroupType": "Security", "SAMAccountName": "AWS Object Management Service Accounts", "SID": "S-1-2-34-5678901234-5678901234-5678910123-4571" }, { "GroupScope": "DomainLocal", "GroupType": "Security", "SAMAccountName": "AWS Private CA Connector for AD Delegated Group", "SID": "S-1-2-34-5678901234-5678901234-5678910123-4572" }, { "GroupScope": "DomainLocal", "GroupType": "Security", "SAMAccountName": "AWS Application and Service Delegated Group", "SID": "S-1-2-34-5678901234-5678901234-5678910123-4573" }, { "GroupScope": "DomainLocal", "GroupType": "Security", "SAMAccountName": "AWS Delegated Administrators", "SID": "S-1-2-34-5678901234-5678901234-5678910123-4574" }, { "GroupScope": "DomainLocal", "GroupType": "Security", "SAMAccountName": "AWS Delegated FSx Administrators", "SID": "S-1-2-34-5678901234-5678901234-5678910123-4575" }, { "GroupScope": "DomainLocal", "GroupType": "Security", "SAMAccountName": "AWS Delegated Account Operators", "SID": "S-1-2-34-5678901234-5678901234-5678910123-4576" }, { "GroupScope": "DomainLocal", "GroupType": "Security", "SAMAccountName": "AWS Delegated Active Directory Based Activation Administrators", "SID": "S-1-2-34-5678901234-5678901234-5678910123-4577" }, { "GroupScope": "DomainLocal", "GroupType": "Security", "SAMAccountName": "AWS Delegated Allowed to Authenticate Objects", "SID": "S-1-2-34-5678901234-5678901234-5678910123-4578" }, { "GroupScope": "DomainLocal", "GroupType": "Security", "SAMAccountName": "AWS Delegated Allowed to Authenticate to Domain Controllers", "SID": "S-1-2-34-5678901234-5678901234-5678910123-4579" }, { "GroupScope": "DomainLocal", "GroupType": "Security", "SAMAccountName": "AWS Delegated Deleted Object Lifetime Administrators", "SID": "S-1-2-34-5678901234-5678901234-5678910123-4580" }, { "GroupScope": "DomainLocal", "GroupType": "Security", "SAMAccountName": "AWS Delegated Distributed File System Administrators", "SID": "S-1-2-34-5678901234-5678901234-5678910123-4581" }, { "GroupScope": "DomainLocal", "GroupType": "Security", "SAMAccountName": "AWS Delegated Dynamic Host Configuration Protocol Administrators", "SID": "S-1-2-34-5678901234-5678901234-5678910123-4582" }, { "GroupScope": "DomainLocal", "GroupType": "Security", "SAMAccountName": "AWS Delegated Enterprise Certificate Authority Administrators", "SID": "S-1-2-34-5678901234-5678901234-5678910123-4583" }, { "GroupScope": "DomainLocal", "GroupType": "Security", "SAMAccountName": "AWS Delegated Fine Grained Password Policy Administrators", "SID": "S-1-2-34-5678901234-5678901234-5678910123-4584" }, { "GroupScope": "DomainLocal", "GroupType": "Security", "SAMAccountName": "AWS Delegated Group Policy Administrators", "SID": "S-1-2-34-5678901234-5678901234-5678910123-4585" }, { "GroupScope": "DomainLocal", "GroupType": "Security", "SAMAccountName": "AWS Delegated Managed Service Account Administrators", "SID": "S-1-2-34-5678901234-5678901234-5678910123-4586" }, { "GroupScope": "DomainLocal", "GroupType": "Security", "SAMAccountName": "AWS Delegated Read Foreign Security Principals", "SID": "S-1-2-34-5678901234-5678901234-5678910123-4587" }, { "GroupScope": "DomainLocal", "GroupType": "Security", "SAMAccountName": "AWS Delegated Remote Access Service Administrators", "SID": "S-1-2-34-5678901234-5678901234-5678910123-4588" }, { "GroupScope": "DomainLocal", "GroupType": "Security", "SAMAccountName": "AWS Delegated Replicate Directory Changes Administrators", "SID": "S-1-2-34-5678901234-5678901234-5678910123-4588" }, { "GroupScope": "DomainLocal", "GroupType": "Security", "SAMAccountName": "AWS Delegated Sites and Services Administrators", "SID": "S-1-2-34-5678901234-5678901234-5678910123-4589" }, { "GroupScope": "DomainLocal", "GroupType": "Security", "SAMAccountName": "AWS Delegated System Management Administrators", "SID": "S-1-2-34-5678901234-5678901234-5678910123-4590" }, { "GroupScope": "DomainLocal", "GroupType": "Security", "SAMAccountName": "AWS Delegated Terminal Server Licensing Administrators", "SID": "S-1-2-34-5678901234-5678901234-5678910123-4591" }, { "GroupScope": "DomainLocal", "GroupType": "Security", "SAMAccountName": "AWS Delegated User Principal Name Suffix Administrators", "SID": "S-1-2-34-5678901234-5678901234-5678910123-4592" }, { "GroupScope": "DomainLocal", "GroupType": "Security", "SAMAccountName": "AWS Delegated Add Workstations To Domain Users", "SID": "S-1-2-34-5678901234-5678901234-5678910123-4593" }, { "GroupScope": "DomainLocal", "GroupType": "Security", "SAMAccountName": "AWS Delegated Domain Name System Administrators", "SID": "S-1-2-34-5678901234-5678901234-5678910123-4594" }, { "GroupScope": "DomainLocal", "GroupType": "Security", "SAMAccountName": "AWS Delegated Kerberos Delegation Administrators", "SID": "S-1-2-34-5678901234-5678901234-5678910123-4595" }, { "GroupScope": "DomainLocal", "GroupType": "Security", "SAMAccountName": "AWS Delegated Server Administrators", "SID": "S-1-2-34-5678901234-5678901234-5678910123-4596" }, { "GroupScope": "DomainLocal", "GroupType": "Security", "SAMAccountName": "AWS Delegated MS-NPRC Non-Compliant Devices", "SID": "S-1-2-34-5678901234-5678901234-5678910123-4597" }, { "GroupScope": "Global", "GroupType": "Security", "SAMAccountName": "Remote Access", "SID": "S-1-2-34-5678901234-5678901234-5678910123-4598" }, { "GroupScope": "Global", "GroupType": "Security", "SAMAccountName": "Accounting", "SID": "S-1-2-34-5678901234-5678901234-5678910123-4599" }, { "GroupScope": "Global", "GroupType": "Distribution", "SAMAccountName": "sales", "SID": "S-1-2-34-5678901234-5678901234-5678910123-4567" } ], "DirectoryId": "d-1234567890", "Realm": "corp.example.com" }`For more information, see [Viewing and updating an AWS Managed Microsoft AD group's details](https://docs.aws.amazon.com/directoryservice/latest/admin-guide/ms_ad_view_update_group.html)in the*AWS Directory Service Administration Guide*.- 
                    For API details, see [ListGroups](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/directory-service-data/list-groups.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `list-users`.

- **AWS CLI**
- 
            
                    **To list a directory's users**The following `list-users`example lists users in the specified directory.`aws ds-data list-users \ --directory-id``d-1234567890`Output: `{ "Users": [ { "Enabled": true, "SAMAccountName": "Administrator", "SID": "S-1-2-34-5678910123-4567895012-3456789012-345" }, { "Enabled": false, "SAMAccountName": "Guest", "SID": "S-1-2-34-5678910123-4567895012-3456789012-345" }, { "Enabled": false, "SAMAccountName": "krbtgt", "SID": "S-1-2-34-5678910123-4567895012-3456789012-346" }, { "Enabled": true, "SAMAccountName": "Admin", "SID": "S-1-2-34-5678910123-4567895012-3456789012-347" }, { "Enabled": true, "SAMAccountName": "Richard Roe", "SID": "S-1-2-34-5678910123-4567895012-3456789012-348" }, { "Enabled": true, "SAMAccountName": "Jane Doe", "SID": "S-1-2-34-5678910123-4567895012-3456789012-349" }, { "Enabled": true, "SAMAccountName": "AWS_WGnzYlN6YyY", "SID": "S-1-2-34-5678901234-5678901234-5678910123-4567" }, { "Enabled": true, "SAMAccountName": "john.doe", "SID": "S-1-2-34-5678901234-5678901234-5678910123-4568" } ], "DirectoryId": "d-1234567890", "Realm": "corp.example.com" }`For more information, see [Viewing and updating an AWS Managed Microsoft AD user](https://docs.aws.amazon.com/directoryservice/latest/admin-guide/ms_ad_view_update_user.html)in the*AWS Directory Service Administration Guide*.- 
                    For API details, see [ListUsers](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/directory-service-data/list-users.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `remove-group-member`.

- **AWS CLI**
- 
            
                    **To remove a group member from a directory**The following `remove-group-member`example removes the specified group member from the specified group in the specified directory.`aws ds-data remove-group-member \ --directory-id``d-1234567890`\ --group-name '`sales`' \ --member-name '`john.doe`'This command produces no output. For more information, see [Adding and removing AWS Managed Microsoft AD members to groups and groups to groups](https://docs.aws.amazon.com/directoryservice/latest/admin-guide/ms_ad_add_remove_user_group.html)in the*AWS Directory Service Administration Guide*.- 
                    For API details, see [RemoveGroupMember](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/directory-service-data/remove-group-member.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `reset-user-password`.

- **AWS CLI**
- 
            
                    **To reset a user password in a directory**The following `reset-user-password`example resets and enables the specified user in the specified directory.`aws ds reset-user-password \ --directory-id``d-1234567890`\ --user-name '`john.doe`' \ --new-`password`'password'This command produces no output. For more information, see [Resetting and enabling an AWS Managed Microsoft AD user's password](https://docs.aws.amazon.com/directoryservice/latest/admin-guide/ms_ad_reset_user_pswd.html)in the*AWS Directory Service Administration Guide*.- 
                    For API details, see [ResetUserPassword](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/directory-service-data/reset-user-password.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `search-groups`.

- **AWS CLI**
- 
            
                    **To search for a group in a directory**The following `search-groups`example searches for the specified group in the specified directory.`aws ds-data search-groups \ --directory-id``d-1234567890`\ --search-attributes '`SamAccountName`' \ --search-string '`sales`'Output: `{ "Groups": [ { "GroupScope": "Global", "GroupType": "Distribution", "SAMAccountName": "sales", "SID": "S-1-2-34-5678901234-5678901234-5678910123-4567" } ], "DirectoryId": "d-1234567890", "Realm": "corp.example.com" }`For more information, see [Viewing and updating an AWS Managed Microsoft AD group's details](https://docs.aws.amazon.com/directoryservice/latest/admin-guide/ms_ad_view_update_group.html)in the*AWS Directory Service Administration Guide*.- 
                    For API details, see [SearchGroups](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/directory-service-data/search-groups.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `search-users`.

- **AWS CLI**
- 
            
                    **To search for a user in a directory**The following `search-users`example searches for the specified user in the specified directory.`aws ds-data search-users \ --directory-id``d-1234567890`\ --search-attributes '`SamAccountName`' \ --search-string '`john.doe`'Output: `{ "Users": [ { "Enabled": true, "SAMAccountName": "john.doe", "SID": "S-1-2-34-5678901234-5678901234-5678910123-4567" } ], "DirectoryId": "d-1234567890", "Realm": "corp.example.com" }`For more information, see [Viewing and updating an AWS Managed Microsoft AD user](https://docs.aws.amazon.com/directoryservice/latest/admin-guide/ms_ad_view_update_user.html)in the*AWS Directory Service Administration Guide*.- 
                    For API details, see [SearchUsers](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/directory-service-data/search-users.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `update-group`.

- **AWS CLI**
- 
            
                    **To update a group's attribute in a directory**The following `update-group`example updates the specified attribute for the specified group in the specified directory.`aws ds-data update-group \ --directory-id``d-1234567890`\ --sam-account-name '`sales`' \ --update-type '`REPLACE`' \ --group-type '`Distribution`'This command produces no output. For more information, see [Viewing and updating an AWS Managed Microsoft AD group's details](https://docs.aws.amazon.com/directoryservice/latest/admin-guide/ms_ad_view_update_group.html)in the*AWS Directory Service Administration Guide*.- 
                    For API details, see [UpdateGroup](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/directory-service-data/update-group.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `update-user`.

- **AWS CLI**
- 
            
                    **To update a user's attribute in a directory**The following `update-user`example updates the specified attribute for the specified user in the specified directory.`aws ds-data update-user \ --directory-id``d-1234567890`\ --sam-account-name '`john.doe`' \ --update-type '`ADD`' \ --email-address '`example.corp.com`'This command produces no output. For more information, see [Viewing and updating an AWS Managed Microsoft AD user](https://docs.aws.amazon.com/directoryservice/latest/admin-guide/ms_ad_view_update_user.html)in the*AWS Directory Service Administration Guide*.- 
                    For API details, see [UpdateUser](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/directory-service-data/update-user.html)in*AWS CLI Command Reference*.
 
-