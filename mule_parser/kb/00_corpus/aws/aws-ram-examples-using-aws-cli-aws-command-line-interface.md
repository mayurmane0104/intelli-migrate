# AWS RAM examples using AWS CLI - AWS Command Line Interface

**Source:** [https://docs.aws.amazon.com/cli/latest/userguide/cli_ram_code_examples.html](https://docs.aws.amazon.com/cli/latest/userguide/cli_ram_code_examples.html)

---

The following code examples show you how to perform actions and implement common scenarios by using the AWS Command Line Interface with AWS RAM.

*Actions* are code excerpts from larger programs and must be run in context. While actions show you how to call individual service functions, you can see actions in context in their related scenarios.

Each example includes a link to the complete source code, where you can find instructions on how to set up and run the code in context.

###### Topics

## Actions

    The following code example shows how to use `accept-resource-share-invitation`.

- **AWS CLI**
- 
            
                    **To accept a resource share invitation**The following `accept-resource-share-invitation`example accepts the specified resource share invitation. Principals in the invited account can immediately start using the resources in the share.`aws ram accept-resource-share-invitation \ --resource-share-invitation-arn``arn:aws:ram:us-west-2:111111111111:resource-share-invitation/1e3477be-4a95-46b4-bbe0-c4001EXAMPLE`Output: `{ "resourceShareInvitation": { "resourceShareInvitationArn": "arn:aws:ram:us-west-2:111111111111:resource-share-invitation/1e3477be-4a95-46b4-bbe0-c4001EXAMPLE", "resourceShareName": "MyLicenseShare", "resourceShareArn": "arn:aws:ram:us-west-2:111111111111:resource-share/27d09b4b-5e12-41d1-a4f2-19dedEXAMPLE", "senderAccountId": "111111111111", "receiverAccountId": "222222222222", "invitationTimestamp": "2021-09-22T15:07:35.620000-07:00", "status": "ACCEPTED" } }`- 
                    For API details, see [AcceptResourceShareInvitation](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ram/accept-resource-share-invitation.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `associate-resource-share-permission`.

- **AWS CLI**
- 
            
                    **To associate a RAM managed permission with a resource share**The following `associate-resource-share-permission`example replaces the existing managed permission for the relevant resource type with the specified managed permission. Access to all resources of the relevant resource type is governed by the new permission.`aws ram associate-resource-share-permission \ --permission-arn``arn:aws:ram::aws:permission/AWSRAMPermissionGlueDatabaseReadWrite`\ --replace \ --resource-share-arn`arn:aws:ram:us-west-2:123456789012:resource-share/27d09b4b-5e12-41d1-a4f2-19dedEXAMPLE`Output: `{ "returnValue": true }`- 
                    For API details, see [AssociateResourceSharePermission](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ram/associate-resource-share-permission.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `associate-resource-share`.

- **AWS CLI**
- 
            
                    **Example 1: To associate a resource with a resource share**The following `associate-resource-share`example adds a license configuration to the specified resource share.`aws ram associate-resource-share \ --resource-share``arn:aws:ram:us-west-2:123456789012:resource-share/27d09b4b-5e12-41d1-a4f2-19dedEXAMPLE`\ --resource-arns`arn:aws:license-manager:us-west-2:123456789012:license-configuration:lic-36be0485f5ae379cc74cf8e92EXAMPLE`Output: `{ "resourceShareAssociations": [ { "resourceShareArn": "arn:aws:ram:us-west-2:123456789012:resource-share/27d09b4b-5e12-41d1-a4f2-19dedEXAMPLE", "associatedEntity": "arn:aws:license-manager:us-west-2:123456789012:license-configuration:lic-36be0485f5ae379cc74cf8e92EXAMPLE", "associationType": "RESOURCE", "status": "ASSOCIATING", "external": false } ] }`**Example 2: To associate a principal with a resource share**The following `associate-resource-share`example grants access for the specified resource share to all accounts in the specified organizational unit.`aws ram associate-resource-share \ --resource-share-arn``arn:aws:ram:us-west-2:123456789012:resource-share/27d09b4b-5e12-41d1-a4f2-19dedEXAMPLE`\ --principals`arn:aws:organizations::123456789012:ou/o-63bEXAMPLE/ou-46xi-rEXAMPLE`Output: `{ "resourceShareAssociations": [ { "status": "ASSOCIATING", "associationType": "PRINCIPAL", "associatedEntity": "arn:aws:organizations::123456789012:ou/o-63bEXAMPLE/ou-46xi-rEXAMPLE", "external": false, "resourceShareArn": "arn:aws:ram:us-west-2:123456789012:resource-share/27d09b4b-5e12-41d1-a4f2-19dedEXAMPLE" } ] }`- 
                    For API details, see [AssociateResourceShare](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ram/associate-resource-share.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `create-resource-share`.

- **AWS CLI**
- 
            
                    **Example 1: To create a resource share**The following `create-resource-share`example creates an empty resource share with the specified name. You must separately add resources, principals, and permissions to the share.`aws ram create-resource-share \ --name``MyNewResourceShare`Output: `{ "resourceShare": { "resourceShareArn": "arn:aws:ram:us-west-2:123456789012:resource-share/4476c27d-8feb-4b21-afe9-7de23EXAMPLE", "name": "MyNewResourceShare", "owningAccountId": "123456789012", "allowExternalPrincipals": true, "status": "ACTIVE", "creationTime": 1634586271.302, "lastUpdatedTime": 1634586271.302 } }`**Example 2: To create a resource share with AWS accounts as principals**The following `create-resource-share`example creates a resource share and grants access to the specified AWS account (222222222222). If the specified principals are not part of the same AWS Organization, then invitations are sent and must be accepted before access is granted.`aws ram create-resource-share \ --name``MyNewResourceShare`\ --principals`222222222222`**Example 3: To create a resource share restricted to your AWS Organization**The following `create-resource-share`example creates a resource share that is restricted to accounts in the AWS Organization that your account is a member of, and adds the specified OU as a principal. All accounts in that OU can use the resources in the resource share.`aws ram create-resource-share \ --name``MyNewResourceShare`\ --no-allow-external-principals \ --principals`arn:aws:organizations::123456789012:ou/o-63bEXAMPLE/ou-46xi-rEXAMPLE`Output: `{ "resourceShare": { "resourceShareArn": "arn:aws:ram:us-west-2:123456789012:resource-share/7be8694e-095c-41ca-9ce8-7be4aEXAMPLE", "name": "MyNewResourceShare", "owningAccountId": "123456789012", "allowExternalPrincipals": false, "status": "ACTIVE", "creationTime": 1634587042.49, "lastUpdatedTime": 1634587042.49 } }`- 
                    For API details, see [CreateResourceShare](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ram/create-resource-share.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `delete-resource-share`.

- **AWS CLI**
- 
            
                    **To delete a resource share**The following `delete-resource-share`example deletes the specified resource share.`aws ram delete-resource-share \ --resource-share-arn``arn:aws:ram:us-west-2:123456789012:resource-share/7ab63972-b505-7e2a-420d-6f5d3EXAMPLE`The following output indicates success: `{ "returnValue": true }`- 
                    For API details, see [DeleteResourceShare](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ram/delete-resource-share.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `disassociate-resource-share-permission`.

- **AWS CLI**
- 
            
                    **To remove a RAM managed permission for a resource type from a resource share**The following `disassociate-resource-share-permission`example removes the RAM managed permission for Glue databases from the specified resource share.`aws ram disassociate-resource-share-permission \ --resource-share-arn``arn:aws:ram:us-west-2:123456789012:resource-share/27d09b4b-5e12-41d1-a4f2-19dedEXAMPLE`\ --permission-arn`arn:aws:ram::aws:permission/AWSRAMPermissionGlueDatabaseReadWrite`Output: `{ "returnValue": true }`- 
                    For API details, see [DisassociateResourceSharePermission](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ram/disassociate-resource-share-permission.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `disassociate-resource-share`.

- **AWS CLI**
- 
            
                    **To remove a resource from a resource share**The following `disassociate-resource-share`example removes the specified resource, in this case a VPC subnet, from the specified resource share. Any principals with access to the resource share can no longer perform operations on that resource.`aws ram disassociate-resource-share \ --resource-arns``arn:aws:ec2:us-west-2:123456789012:subnet/subnet-0250c25a1fEXAMPLE`\ --resource-share-arn`arn:aws:ram:us-west-2:123456789012:resource-share/7ab63972-b505-7e2a-420d-6f5d3EXAMPLE`Output: `{ "resourceShareAssociations": [ "resourceShareArn": "arn:aws:ram:us-west-2:123456789012:resource-share/7ab63972-b505-7e2a-420d-6f5d3EXAMPLE", "associatedEntity": "arn:aws:ec2:us-west-2:123456789012:subnet/subnet-0250c25a1fEXAMPLE", "associationType": "RESOURCE", "status": "DISASSOCIATING", "external": false ] }`- 
                    For API details, see [DisassociateResourceShare](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ram/disassociate-resource-share.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `enable-sharing-with-aws-organization`.

- **AWS CLI**
- 
            
                    **To enable resource sharing across AWS Organizations**The following `enable-sharing-with-aws-organization`example enables resource sharing across your organization and organizational units.`aws ram enable-sharing-with-aws-organization`The following output indicates success. `{ "returnValue": true }`- 
                    For API details, see [EnableSharingWithAwsOrganization](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ram/enable-sharing-with-aws-organization.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `get-permission`.

- **AWS CLI**
- 
            
                    **To retrieve the details for a RAM managed permission**The following `get-permission`example displays the details for the default version of the specified RAM managed permission.`aws ram get-permission \ --permission-arn``arn:aws:ram::aws:permission/AWSRAMPermissionGlueTableReadWriteForDatabase`Output: `{ "permission": { "arn": "arn:aws:ram::aws:permission/AWSRAMPermissionGlueTableReadWriteForDatabase", "version": "2", "defaultVersion": true, "name": "AWSRAMPermissionGlueTableReadWriteForDatabase", "resourceType": "glue:Database", "permission": "{\"Effect\":\"Allow\",\"Action\":[\"glue:GetTable\", \"glue:UpdateTable\", \"glue:DeleteTable\", \"glue:BatchDeleteTable\", \"glue:BatchDeleteTableVersion\", \"glue:GetTableVersion\", \"glue:GetTableVersions\", \"glue:GetPartition\", \"glue:GetPartitions\", \"glue:BatchGetPartition\", \"glue:BatchCreatePartition\", \"glue:CreatePartition\", \"glue:UpdatePartition\", \"glue:BatchDeletePartition\", \"glue:DeletePartition\", \"glue:GetTables\", \"glue:SearchTables\"]}", "creationTime": 1624912434.431, "lastUpdatedTime": 1624912434.431, "isResourceTypeDefault": false } }`- 
                    For API details, see [GetPermission](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ram/get-permission.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `get-resource-policies`.

- **AWS CLI**
- 
            
                    **To get the policies for a resource**The following `get-resource-policies`example displays the resource-based permission policies for the specified resource associated with a resource share.`aws ram get-resource-policies \ --resource-arns``arn:aws:ec2:us-west-2:123456789012:subnet/subnet-0250c25a1fEXAMPLE`Output: `{ "policies": [ "{\"Version\":\"2008-10-17\",\"Statement\":[{\"Sid\":\"RamStatement1\",\"Effect\":\"Allow\",\"Principal\":{\"AWS\":[]},\"Action\":[\"ec2:RunInstances\",\"ec2:CreateNetworkInterface\",\"ec2:DescribeSubnets\"],\"Resource\":\"arn:aws:ec2:us-west-2:123456789012:subnet/subnet-0250c25a1fEXAMPLE\"}]}" ] }`- 
                    For API details, see [GetResourcePolicies](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ram/get-resource-policies.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `get-resource-share-associations`.

- **AWS CLI**
- 
            
                    **Example 1: To list all resource associations for all resource types**The following `get-resource-share-associations`example lists the resource associations for all resource types across all of your resource shares.`aws ram get-resource-share-associations \ --association-type``RESOURCE`Output: `{ "resourceShareAssociations": [ { "resourceShareArn": "arn:aws:ram:us-west-2:123456789012:resource-share/7ab63972-b505-7e2a-420d-6f5d3EXAMPLE", "associatedEntity": "arn:aws:ec2:us-west-2:123456789012:subnet/subnet-0250c25a1fEXAMPLE", "resourceShareName": "MySubnetShare", "associationType": "RESOURCE", "status": "ASSOCIATED", "creationTime": 1565303590.973, "lastUpdatedTime": 1565303591.695, "external": false }, { "resourceShareArn": "arn:aws:ram:us-west-2:123456789012:resource-share/8167bdfe-4480-4a01-8632-315e0EXAMPLE", "associatedEntity": "arn:aws:license-manager:us-west-2:123456789012:license-configuration:lic-36be0485f5ae379cc74cf8e92EXAMPLE", "resourceShareName": "MyLicenseShare", "associationType": "RESOURCE", "status": "ASSOCIATED", "creationTime": 1632342958.457, "lastUpdatedTime": 1632342958.907, "external": false } ] }`**Example 2: To list principal associations for a resource share**The following `get-resource-share-associations`example lists only the principal associations for only the specified resource share.`aws ram get-resource-share-associations \ --resource-share-arns``arn:aws:ram:us-west-2:123456789012:resource-share/7be8694e-095c-41ca-9ce8-7be4aEXAMPLE`\ --association-type`PRINCIPAL`Output: `{ "resourceShareAssociations": [ { "resourceShareArn": "arn:aws:ram:us-west-2:123456789012:resource-share/7be8694e-095c-41ca-9ce8-7be4aEXAMPLE", "resourceShareName": "MyNewResourceShare", "associatedEntity": "arn:aws:organizations::123456789012:ou/o-63bEXAMPLE/ou-46xi-rEXAMPLE", "associationType": "PRINCIPAL", "status": "ASSOCIATED", "creationTime": 1634587042.49, "lastUpdatedTime": 1634587044.291, "external": false } ] }`- 
                    For API details, see [GetResourceShareAssociations](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ram/get-resource-share-associations.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `get-resource-share-invitations`.

- **AWS CLI**
- 
            
                    **To list your resource share invitations**The following `get-resource-share-invitations`example lists your current resource share invitations.`aws ram get-resource-share-invitations`Output: `{ "resourceShareInvitations": [ { "resourceShareInvitationArn": "arn:aws:ram:us-west2-1:111111111111:resource-share-invitation/32b639f0-14b8-7e8f-55ea-e6117EXAMPLE", "resourceShareName": "project-resource-share", "resourceShareArn": "arn:aws:ram:us-west-2:111111111111:resource-share/fcb639f0-1449-4744-35bc-a983fEXAMPLE", "senderAccountId": "111111111111", "receiverAccountId": "222222222222", "invitationTimestamp": 1565312166.258, "status": "PENDING" } ] }`- 
                    For API details, see [GetResourceShareInvitations](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ram/get-resource-share-invitations.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `get-resource-shares`.

- **AWS CLI**
- 
            
                    **Example 1: To list resource shares you own and share with others**The following `get-resource-shares`example lists the resource shares that created and are sharing with others.`aws ram get-resource-shares \ --resource-owner``SELF`Output: `{ "resourceShares": [ { "resourceShareArn": "arn:aws:ram:us-west-2:123456789012:resource-share/3ab63985-99d9-1cd2-7d24-75e93EXAMPLE", "name": "my-resource-share", "owningAccountId": "123456789012", "allowExternalPrincipals": false, "status": "ACTIVE", "tags": [ { "key": "project", "value": "lima" } ] "creationTime": 1565295733.282, "lastUpdatedTime": 1565295733.282 }, { "resourceShareArn": "arn:aws:ram:us-west-2:123456789012:resource-share/7ab63972-b505-7e2a-420d-6f5d3EXAMPLE", "name": "my-resource-share", "owningAccountId": "123456789012", "allowExternalPrincipals": true, "status": "ACTIVE", "creationTime": 1565295733.282, "lastUpdatedTime": 1565295733.282 } ] }`**Example 2: To list resource shares owned by others and shared with you**The following `get-resource-shares`example lists the resource shares that others created and shared with you. In this example, there are none.`aws ram get-resource-shares \ --resource-owner``OTHER-ACCOUNTS`Output: `{ "resourceShares": [] }`- 
                    For API details, see [GetResourceShares](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ram/get-resource-shares.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `list-pending-invitation-resources`.

- **AWS CLI**
- 
            
                    **To list the resources that are available in a pending resource share**The following `list-pending-invitation-resources`example lists all of the resources that are in the resource share associated with the specified invitation.`aws ram list-pending-invitation-resources \ --resource-share-invitation-arn``arn:aws:ram:us-west-2:123456789012:resource-share-invitation/1e3477be-4a95-46b4-bbe0-c4001EXAMPLE`Output: `{ "resources": [ { "arn": "arn:aws:ec2:us-west-2:123456789012:subnet/subnet-04a555b0e6EXAMPLE", "resourceShareArn": "arn:aws:ram:us-west-2:123456789012:resource-share/7be8694e-095c-41ca-9ce8-7be4aEXAMPLE", "creationTime": 1634676051.269, "lastUpdatedTime": 1634676052.07, "status": "AVAILABLE", "type": "ec2:Subnet" }, { "arn": "arn:aws:license-manager:us-west-2:123456789012:license-configuration:lic-36be0485f5ae379cc74cf8e92EXAMPLE", "resourceShareArn": "arn:aws:ram:us-west-2:123456789012:resource-share/7ab63972-b505-7e2a-420d-6f5d3EXAMPLE", "creationTime": 1624912434.431, "lastUpdatedTime": 1624912434.431, "status": "AVAILABLE", "type": "license-manager:LicenseConfiguration" } ] }`- 
                    For API details, see [ListPendingInvitationResources](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ram/list-pending-invitation-resources.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `list-permissions`.

- **AWS CLI**
- 
            
                    **To list the available RAM managed permissions**The following `list-permissions`example lists all of the RAM managed permissions available for only the AWS Glue database resource type.`aws ram list-permissions \ --resource-type``glue:Database`Output: `{ "permissions": [ { "arn": "arn:aws:ram::aws:permission/AWSRAMDefaultPermissionGlueDatabase", "version": "1", "defaultVersion": true, "name": "AWSRAMDefaultPermissionGlueDatabase", "resourceType": "glue:Database", "creationTime": 1592007820.935, "lastUpdatedTime": 1592007820.935, "isResourceTypeDefault": true }, { "arn": "arn:aws:ram::aws:permission/AWSRAMPermissionGlueAllTablesReadWriteForDatabase", "version": "2", "defaultVersion": true, "name": "AWSRAMPermissionGlueAllTablesReadWriteForDatabase", "resourceType": "glue:Database", "creationTime": 1624912413.323, "lastUpdatedTime": 1624912413.323, "isResourceTypeDefault": false }, { "arn": "arn:aws:ram::aws:permission/AWSRAMPermissionGlueDatabaseReadWrite", "version": "2", "defaultVersion": true, "name": "AWSRAMPermissionGlueDatabaseReadWrite", "resourceType": "glue:Database", "creationTime": 1624912417.4, "lastUpdatedTime": 1624912417.4, "isResourceTypeDefault": false }, { "arn": "arn:aws:ram::aws:permission/AWSRAMPermissionGlueTableReadWriteForDatabase", "version": "2", "defaultVersion": true, "name": "AWSRAMPermissionGlueTableReadWriteForDatabase", "resourceType": "glue:Database", "creationTime": 1624912434.431, "lastUpdatedTime": 1624912434.431, "isResourceTypeDefault": false } ] }`The following `list-permissions`example displays the available RAM managed permissions for all resource types.`aws ram list-permissions`Output: `{ "permissions": [ { "arn": "arn:aws:ram::aws:permission/AWSRAMBlankEndEntityCertificateAPICSRPassthroughIssuanceCertificateAuthority", "version": "1", "defaultVersion": true, "name": "AWSRAMBlankEndEntityCertificateAPICSRPassthroughIssuanceCertificateAuthority", "resourceType": "acm-pca:CertificateAuthority", "creationTime": 1623264861.085, "lastUpdatedTime": 1623264861.085, "isResourceTypeDefault": false }, { "arn": "arn:aws:ram::aws:permission/AWSRAMDefaultPermissionAppMesh", "version": "1", "defaultVersion": true, "name": "AWSRAMDefaultPermissionAppMesh", "resourceType": "appmesh:Mesh", "creationTime": 1589307188.584, "lastUpdatedTime": 1589307188.584, "isResourceTypeDefault": true }, ...TRUNCATED FOR BREVITY... { "arn": "arn:aws:ram::aws:permission/AWSRAMSubordinateCACertificatePathLen0IssuanceCertificateAuthority", "version": "1", "defaultVersion": true, "name": "AWSRAMSubordinateCACertificatePathLen0IssuanceCertificateAuthority", "resourceType": "acm-pca:CertificateAuthority", "creationTime": 1623264876.75, "lastUpdatedTime": 1623264876.75, "isResourceTypeDefault": false } ] }`- 
                    For API details, see [ListPermissions](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ram/list-permissions.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `list-principals`.

- **AWS CLI**
- 
            
                    **To list principals with access to a resource**The following `list-principals`example displays a list of the principals that can access resources of the specified type through any resource shares.`aws ram list-principals \ --resource-owner``SELF`\ --resource-type`ec2:Subnet`Output: `{ "principals": [ { "id": "arn:aws:organizations::123456789012:ou/o-gx7EXAMPLE/ou-29c5-zEXAMPLE", "resourceShareArn": "arn:aws:ram:us-west-2:123456789012:resource-share/7ab63972-b505-7e2a-420d-6f5d3EXAMPLE", "creationTime": 1565298209.737, "lastUpdatedTime": 1565298211.019, "external": false } ] }`- 
                    For API details, see [ListPrincipals](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ram/list-principals.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `list-resource-share-permissions`.

- **AWS CLI**
- 
            
                    **To list all of the RAM managed permissions currently attached to a resource share**The following `list-resource-share-permissions`example lists all of the RAM managed permissions that are attached to the specified resource share.`aws ram list-resource-share-permissions \ --resource-share-arn``arn:aws:ram:us-west-2:123456789012:resource-share/27d09b4b-5e12-41d1-a4f2-19dedEXAMPLE`Output: `{ "permissions": [ { "arn": "arn:aws:ram::aws:permission/AWSRAMDefaultPermissionLicenseConfiguration", "version": "1", "resourceType": "license-manager:LicenseConfiguration", "status": "ASSOCIATED", "lastUpdatedTime": 1632342984.234 }, { "arn": "arn:aws:ram::aws:permission/AWSRAMPermissionGlueDatabaseReadWrite", "version": "2", "resourceType": "glue:Database", "status": "ASSOCIATED", "lastUpdatedTime": 1632512462.297 } ] }`- 
                    For API details, see [ListResourceSharePermissions](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ram/list-resource-share-permissions.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `list-resource-types`.

- **AWS CLI**
- 
            
                    **To list the resource types that are supported by AWS RAM**The following `list-resource-types`example lists all of the resource types currently supported by AWS RAM.`aws ram list-resource-types`Output: `{ "resourceTypes": [ { "resourceType": "route53resolver:FirewallRuleGroup", "serviceName": "route53resolver" }, { "resourceType": "ec2:LocalGatewayRouteTable", "serviceName": "ec2" }, ...OUTPUT TRUNCATED FOR BREVITY... { "resourceType": "ec2:Subnet", "serviceName": "ec2" }, { "resourceType": "ec2:TransitGatewayMulticastDomain", "serviceName": "ec2" } ] }`- 
                    For API details, see [ListResourceTypes](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ram/list-resource-types.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `list-resources`.

- **AWS CLI**
- 
            
                    **To list the resources associated with a resource share**The following `list-resources`example lists all resources in the specified resource share that are of the specified resource type.`aws ram list-resources \ --resource-type``ec2:Subnet`\ --resource-owner`SELF`\ --resource-share-arn`arn:aws:ram:us-west-2:123456789012:resource-share/7ab63972-b505-7e2a-420d-6f5d3EXAMPLE`Output: `{ "resources": [ { "arn": "aarn:aws:ec2:us-west-2:123456789012:subnet/subnet-0250c25a1f4e15235", "type": "ec2:Subnet", "resourceShareArn": "arn:aws:ram:us-west-2:123456789012:resource-share/7ab63972-b505-7e2a-420d-6f5d3EXAMPLE", "creationTime": 1565301545.023, "lastUpdatedTime": 1565301545.947 } ] }`- 
                    For API details, see [ListResources](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ram/list-resources.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `promote-resource-share-created-from-policy`.

- **AWS CLI**
- 
            
                    **To promote a resource-policy based resource share to full functionality in AWS RAM**The following `promote-resource-share-created-from-policy`example takes a resource share that you created implicitly by attaching a resource-based policy, and converts it to be fully functional with the AWS RAM console and its CLI and API operations.`aws ram promote-resource-share-created-from-policy \ --resource-share-arn``arn:aws:ram:us-east-1:123456789012:resource-share/91fa8429-2d06-4032-909a-90909EXAMPLE`Output: `{ "returnValue": true }`- 
                    For API details, see [PromoteResourceShareCreatedFromPolicy](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ram/promote-resource-share-created-from-policy.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `reject-resource-share-invitation`.

- **AWS CLI**
- 
            
                    **To reject a resource share invitation**The following `reject-resource-share-invitation`example rejects the specified resource share invitation.`aws ram reject-resource-share-invitation \ --resource-share-invitation-arn``arn:aws:ram:us-west-2:111111111111:resource-share-invitation/32b639f0-14b8-7e8f-55ea-e6117EXAMPLE`Output: `"resourceShareInvitations": [ { "resourceShareInvitationArn": "arn:aws:ram:us-west2-1:111111111111:resource-share-invitation/32b639f0-14b8-7e8f-55ea-e6117EXAMPLE", "resourceShareName": "project-resource-share", "resourceShareArn": "arn:aws:ram:us-west-2:111111111111:resource-share/fcb639f0-1449-4744-35bc-a983fEXAMPLE", "senderAccountId": "111111111111", "receiverAccountId": "222222222222", "invitationTimestamp": 1565319592.463, "status": "REJECTED" } ]`- 
                    For API details, see [RejectResourceShareInvitation](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ram/reject-resource-share-invitation.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `tag-resource`.

- **AWS CLI**
- 
            
                    **To add tags to a resource share**The following `tag-resource`example adds a tag key`project`and associated value`lima`to the specified resource share.`aws ram tag-resource \ --tags``key=project,value=lima`\ --resource-share-arn`arn:aws:ram:us-west-2:123456789012:resource-share/7ab63972-b505-7e2a-420d-6f5d3EXAMPLE`This command produces no output. - 
                    For API details, see [TagResource](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ram/tag-resource.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `untag-resource`.

- **AWS CLI**
- 
            
                    **To remove tags from a resource share**The following `untag-resource`example removes the`project`tag key and associated value from the specified resource share.`aws ram untag-resource \ --tag-keys``project`\ --resource-share-arn`arn:aws:ram:us-west-2:123456789012:resource-share/7ab63972-b505-7e2a-420d-6f5d3EXAMPLE`This command produces no output. - 
                    For API details, see [UntagResource](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ram/untag-resource.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `update-resource-share`.

- **AWS CLI**
- 
            
                    **To update a resource share**The following `update-resource-share`example changes the specified resource share to allow external principals that are not in an AWS Organization.`aws ram update-resource-share \ --allow-external-principals \ --resource-share-arn``arn:aws:ram:us-west-2:123456789012:resource-share/7ab63972-b505-7e2a-420d-6f5d3EXAMPLE`Output: `{ "resourceShare": { "resourceShareArn": "arn:aws:ram:us-west-2:123456789012:resource-share/7ab63972-b505-7e2a-420d-6f5d3EXAMPLE", "name": "my-resource-share", "owningAccountId": "123456789012", "allowExternalPrincipals": true, "status": "ACTIVE", "creationTime": 1565295733.282, "lastUpdatedTime": 1565303080.023 } }`- 
                    For API details, see [UpdateResourceShare](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ram/update-resource-share.html)in*AWS CLI Command Reference*.
 
-