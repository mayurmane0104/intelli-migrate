# License Manager examples using AWS CLI - AWS Command Line Interface

**Source:** [https://docs.aws.amazon.com/cli/latest/userguide/cli_license-manager_code_examples.html](https://docs.aws.amazon.com/cli/latest/userguide/cli_license-manager_code_examples.html)

---

The following code examples show you how to perform actions and implement common scenarios by using the AWS Command Line Interface with License Manager.

*Actions* are code excerpts from larger programs and must be run in context. While actions show you how to call individual service functions, you can see actions in context in their related scenarios.

Each example includes a link to the complete source code, where you can find instructions on how to set up and run the code in context.

###### Topics

## Actions

    The following code example shows how to use `create-license-configuration`.

- **AWS CLI**
- 
            
                    **Example 1: To create a license configuration**The following `create-license-configuration`example creates a license configuration with a hard limit of 10 cores.`aws license-manager create-license-configuration --name``my-license-configuration`\ --license-counting-type`Core`\ --license-count`10`\ --license-count-hard-limitOutput: `{ "LicenseConfigurationArn": "arn:aws:license-manager:us-west-2:123456789012:license-configuration:lic-6eb6586f508a786a2ba41EXAMPLE1111" }`**Example 2: To create a license configuration**The following `create-license-configuration`example creates a license configuration with a soft limit of 100 vCPUs. It uses a rule to enable vCPU optimization.`aws license-manager create-license-configuration --name``my-license-configuration`--license-counting-type`vCPU`\ --license-count`100`\ --license-rules`"#honorVcpuOptimization=true"`Output: `{ "LicenseConfigurationArn": "arn:aws:license-manager:us-west-2:123456789012:license-configuration:lic-6eb6586f508a786a2ba41EXAMPLE2222" }`- 
                    For API details, see [CreateLicenseConfiguration](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/license-manager/create-license-configuration.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `delete-license-configuration`.

- **AWS CLI**
- 
            
                    **To delete a license configuration**The following `delete-license-configuration`example deletes the specified license configuration.`aws license-manager delete-license-configuration \ --license-configuration-arn``arn:aws:license-manager:us-west-2:123456789012:license-configuration:lic-6eb6586f508a786a2ba4f56c1EXAMPLE`This command produces no output. - 
                    For API details, see [DeleteLicenseConfiguration](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/license-manager/delete-license-configuration.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `get-license-configuration`.

- **AWS CLI**
- 
            
                    **To get license configuration information**The following `get-license-configuration`example displays details for the specified license configuration.`aws license-manager get-license-configuration \ --license-configuration-arn``arn:aws:license-manager:us-west-2:123456789012:license-configuration:lic-38b658717b87478aaa7c00883EXAMPLE`Output: `{ "LicenseConfigurationId": "lic-38b658717b87478aaa7c00883EXAMPLE", "LicenseConfigurationArn": "arn:aws:license-manager:us-west-2:123456789012:license-configuration:lic-38b658717b87478aaa7c00883EXAMPLE", "Name": "my-license-configuration", "LicenseCountingType": "vCPU", "LicenseRules": [], "LicenseCountHardLimit": false, "ConsumedLicenses": 0, "Status": "AVAILABLE", "OwnerAccountId": "123456789012", "ConsumedLicenseSummaryList": [ { "ResourceType": "EC2_INSTANCE", "ConsumedLicenses": 0 }, { "ResourceType": "EC2_HOST", "ConsumedLicenses": 0 }, { "ResourceType": "SYSTEMS_MANAGER_MANAGED_INSTANCE", "ConsumedLicenses": 0 } ], "ManagedResourceSummaryList": [ { "ResourceType": "EC2_INSTANCE", "AssociationCount": 0 }, { "ResourceType": "EC2_HOST", "AssociationCount": 0 }, { "ResourceType": "EC2_AMI", "AssociationCount": 2 }, { "ResourceType": "SYSTEMS_MANAGER_MANAGED_INSTANCE", "AssociationCount": 0 } ] }`- 
                    For API details, see [GetLicenseConfiguration](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/license-manager/get-license-configuration.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `get-service-settings`.

- **AWS CLI**
- 
            
                    **To get the License Manager settings**The following `get-service-settings`example displays the service settings for License Manager in the current Region.`aws license-manager get-service-settings`The following shows example output if cross-account resource discovery is disabled. `{ "OrganizationConfiguration": { "EnableIntegration": false }, "EnableCrossAccountsDiscovery": false }`The following shows example output if cross-account resource discovery is enabled. `{ "S3BucketArn": "arn:aws:s3:::aws-license-manager-service-c22d6279-35c4-47c4-bb", "OrganizationConfiguration": { "EnableIntegration": true }, "EnableCrossAccountsDiscovery": true }`- 
                    For API details, see [GetServiceSettings](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/license-manager/get-service-settings.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `list-associations-for-license-configuration`.

- **AWS CLI**
- 
            
                    **To get associations for a license configuration**The following `list-associations-for-license-configuration`example displays detailed information for the associations of the specified license configuration.`aws license-manager list-associations-for-license-configuration \ --license-configuration-arn``arn:aws:license-manager:us-west-2:123456789012:license-configuration:lic-38b658717b87478aaa7c00883EXAMPLE`Output: `{ "LicenseConfigurationAssociations": [ { "ResourceArn": "arn:aws:ec2:us-west-2::image/ami-1234567890abcdef0", "ResourceType": "EC2_AMI", "ResourceOwnerId": "123456789012", "AssociationTime": 1568825118.617 }, { "ResourceArn": "arn:aws:ec2:us-west-2::image/ami-0abcdef1234567890", "ResourceType": "EC2_AMI", "ResourceOwnerId": "123456789012", "AssociationTime": 1568825118.946 } ] }`- 
                    For API details, see [ListAssociationsForLicenseConfiguration](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/license-manager/list-associations-for-license-configuration.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `list-license-configurations`.

- **AWS CLI**
- 
            
                    **Example 1: To list all of your license configurations**The following `list-license-configurations`example lists all your license configurations.`aws license-manager list-license-configurations`Output: `{ "LicenseConfigurations": [ { "LicenseConfigurationId": "lic-6eb6586f508a786a2ba4f56c1EXAMPLE", "LicenseConfigurationArn": "arn:aws:license-manager:us-west-2:123456789012:license-configuration:lic-6eb6586f508a786a2ba4f56c1EXAMPLE", "Name": "my-license-configuration", "LicenseCountingType": "Core", "LicenseRules": [], "LicenseCount": 10, "LicenseCountHardLimit": true, "ConsumedLicenses": 0, "Status": "AVAILABLE", "OwnerAccountId": "123456789012", "ConsumedLicenseSummaryList": [ { "ResourceType": "EC2_INSTANCE", "ConsumedLicenses": 0 }, { "ResourceType": "EC2_HOST", "ConsumedLicenses": 0 }, { "ResourceType": "SYSTEMS_MANAGER_MANAGED_INSTANCE", "ConsumedLicenses": 0 } ], "ManagedResourceSummaryList": [ { "ResourceType": "EC2_INSTANCE", "AssociationCount": 0 }, { "ResourceType": "EC2_HOST", "AssociationCount": 0 }, { "ResourceType": "EC2_AMI", "AssociationCount": 0 }, { "ResourceType": "SYSTEMS_MANAGER_MANAGED_INSTANCE", "AssociationCount": 0 } ] }, { ... } ] }`**Example 2: To list a specific license configuration**The following `list-license-configurations`example lists only the specified license configuration.`aws license-manager list-license-configurations \ --license-configuration-arns``arn:aws:license-manager:us-west-2:123456789012:license-configuration:lic-38b658717b87478aaa7c00883EXAMPLE`- 
                    For API details, see [ListLicenseConfigurations](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/license-manager/list-license-configurations.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `list-license-specifications-for-resource`.

- **AWS CLI**
- 
            
                    **To list the license configurations for a resource**The following `list-license-specifications-for-resource`example lists the license configurations associated with the specified Amazon Machine Image (AMI).`aws license-manager list-license-specifications-for-resource \ --resource-arn``arn:aws:ec2:us-west-2::image/ami-1234567890abcdef0`Output: `{ "LicenseConfigurationArn": "arn:aws:license-manager:us-west-2:123456789012:license-configuration:lic-38b658717b87478aaa7c00883EXAMPLE" }`- 
                    For API details, see [ListLicenseSpecificationsForResource](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/license-manager/list-license-specifications-for-resource.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `list-resource-inventory`.

- **AWS CLI**
- 
            
                    **To list resources in the resource inventory**The following `list-resource-inventory`example lists the resources managed using Systems Manager inventory.`aws license-manager list-resource-inventory`Output: `{ "ResourceInventoryList": [ { "Platform": "Red Hat Enterprise Linux Server", "ResourceType": "EC2Instance", "PlatformVersion": "7.4", "ResourceArn": "arn:aws:ec2:us-west-2:1234567890129:instance/i-05d3cdfb05bd36376", "ResourceId": "i-05d3cdfb05bd36376", "ResourceOwningAccountId": "1234567890129" }, { "Platform": "Amazon Linux", "ResourceType": "EC2Instance", "PlatformVersion": "2", "ResourceArn": "arn:aws:ec2:us-west-2:1234567890129:instance/i-0b1d036cfd4594808", "ResourceId": "i-0b1d036cfd4594808", "ResourceOwningAccountId": "1234567890129" }, { "Platform": "Microsoft Windows Server 2019 Datacenter", "ResourceType": "EC2Instance", "PlatformVersion": "10.0.17763", "ResourceArn": "arn:aws:ec2:us-west-2:1234567890129:instance/i-0cdb3b54a2a8246ad", "ResourceId": "i-0cdb3b54a2a8246ad", "ResourceOwningAccountId": "1234567890129" } ] }`- 
                    For API details, see [ListResourceInventory](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/license-manager/list-resource-inventory.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `list-tags-for-resource`.

- **AWS CLI**
- 
            
                    **To list the tags for a license configuration**The following `list-tags-for-resource`example lists the tags for the specified license configuration.`aws license-manager list-tags-for-resource \ --resource-arn``arn:aws:license-manager:us-west-2:123456789012:license-configuration:lic-6eb6586f508a786a2ba4f56c1EXAMPLE`Output: `{ "Tags": [ { "Key": "project", "Value": "lima" } ] }`- 
                    For API details, see [ListTagsForResource](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/license-manager/list-tags-for-resource.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `list-usage-for-license-configuration`.

- **AWS CLI**
- 
            
                    **To list the licenses in use for a license configuration**The following `list-usage-for-license-configuration`example lists information about the resources using licenses for the specified license configuration. For example, if the license type is vCPU, any instances consume one license per vCPU.`aws license-manager list-usage-for-license-configuration \ --license-configuration-arn``arn:aws:license-manager:us-west-2:123456789012:license-configuration:lic-38b658717b87478aaa7c00883EXAMPLE`Output: `{ "LicenseConfigurationUsageList": [ { "ResourceArn": "arn:aws:ec2:us-west-2:123456789012:instance/i-04a636d18e83cfacb", "ResourceType": "EC2_INSTANCE", "ResourceStatus": "running", "ResourceOwnerId": "123456789012", "AssociationTime": 1570892850.519, "ConsumedLicenses": 2 } ] }`- 
                    For API details, see [ListUsageForLicenseConfiguration](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/license-manager/list-usage-for-license-configuration.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `tag-resource`.

- **AWS CLI**
- 
            
                    **To add a tag a license configuration**The following `tag-resource`example adds the specified tag (key name and value) to the specified license configuration.`aws license-manager tag-resource \ --tags``Key=project,Value=lima`\ --resource-arn`arn:aws:license-manager:us-west-2:123456789012:license-configuration:lic-6eb6586f508a786a2ba4f56c1EXAMPLE`This command produces no output. - 
                    For API details, see [TagResource](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/license-manager/tag-resource.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `untag-resource`.

- **AWS CLI**
- 
            
                    **To remove tags from a license configuration**The following `untag-resource`example removes the specified tag (key name and resource) from the specified license configuration.`aws license-manager untag-resource \ --tag-keys``project`\ --resource-arn`arn:aws:license-manager:us-west-2:123456789012:license-configuration:lic-6eb6586f508a786a2ba4f56c1EXAMPLE`This command produces no output. - 
                    For API details, see [UntagResource](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/license-manager/untag-resource.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `update-license-configuration`.

- **AWS CLI**
- 
            
                    **To update a license configuration**The following `update-license-configuration`example updates the specified license configuration to remove the hard limit.`aws license-manager update-license-configuration \ --no-license-count-hard-limit \ --license-configuration-arn``arn:aws:license-manager:us-west-2:880185128111:license-configuration:lic-6eb6586f508a786a2ba4f56c1EXAMPLE`This command produces no output. The following `update-license-configuration`example updates the specified license configuration to change its status to`DISABLED`.`aws license-manager update-license-configuration \ --license-configuration-status``DISABLED`--license-configuration-arn`arn:aws:license-manager:us-west-2:880185128111:license-configuration:lic-6eb6586f508a786a2ba4f56c1EXAMPLE`This command produces no output. - 
                    For API details, see [UpdateLicenseConfiguration](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/license-manager/update-license-configuration.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `update-license-specifications-for-resource`.

- **AWS CLI**
- 
            
                    **To update the license configurations for a resource**The following `update-license-specifications-for-resource`example replaces the license configuration associated with the specified Amazon Machine Image (AMI) by removing one license configuration and adding another.`aws license-manager update-license-specifications-for-resource \ --resource-arn``arn:aws:ec2:us-west-2::image/ami-1234567890abcdef0`\ --remove-license-specifications`LicenseConfigurationArn=arn:aws:license-manager:us-west-2:123456789012:license-configuration:lic-38b658717b87478aaa7c00883EXAMPLE`\ --add-license-specifications`LicenseConfigurationArn=arn:aws:license-manager:us-west-2:123456789012:license-configuration:lic-42b6deb06e5399a980d555927EXAMPLE`This command produces no output. - 
                    For API details, see [UpdateLicenseSpecificationsForResource](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/license-manager/update-license-specifications-for-resource.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `update-service-settings`.

- **AWS CLI**
- 
            
                    **To update the License Manager settings**The following `update-service-settings`example enables cross-account resource discovery for License Manager in the current AWS Region. The Amazon S3 bucket is the Resource Data Sync required for Systems Manager inventory.`aws license-manager update-service-settings \ --organization-configuration``EnableIntegration=true`\ --enable-cross-accounts-discovery \ --s3-bucket-arn`arn:aws:s3:::aws-license-manager-service-abcd1234EXAMPLE`This command produces no output. - 
                    For API details, see [UpdateServiceSettings](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/license-manager/update-service-settings.html)in*AWS CLI Command Reference*.
 
-