# Amazon EFS examples using AWS CLI - AWS Command Line Interface

**Source:** [https://docs.aws.amazon.com/cli/latest/userguide/cli_efs_code_examples.html](https://docs.aws.amazon.com/cli/latest/userguide/cli_efs_code_examples.html)

---

The following code examples show you how to perform actions and implement common scenarios by using the AWS Command Line Interface with Amazon EFS.

*Actions* are code excerpts from larger programs and must be run in context. While actions show you how to call individual service functions, you can see actions in context in their related scenarios.

Each example includes a link to the complete source code, where you can find instructions on how to set up and run the code in context.

###### Topics

## Actions

    The following code example shows how to use `create-file-system`.

- **AWS CLI**
- 
            
                    **To create an encrypted file system**The following `create-file-system`example creates an encrypted file system using the default CMK. It also adds the tag`Name=my-file-system`.`aws efs create-file-system \ --performance-mode``generalPurpose`\ --throughput-mode`bursting`\ --encrypted \ --tags`Key=Name,Value=my-file-system`Output: `{ "OwnerId": "123456789012", "CreationToken": "console-d7f56c5f-e433-41ca-8307-9d9c0example", "FileSystemId": "fs-c7a0456e", "FileSystemArn": "arn:aws:elasticfilesystem:us-west-2:123456789012:file-system/fs-48499b4d", "CreationTime": 1595286880.0, "LifeCycleState": "creating", "Name": "my-file-system", "NumberOfMountTargets": 0, "SizeInBytes": { "Value": 0, "ValueInIA": 0, "ValueInStandard": 0 }, "PerformanceMode": "generalPurpose", "Encrypted": true, "KmsKeyId": "arn:aws:kms:us-west-2:123456789012:key/a59b3472-e62c-42e4-adcf-30d92example", "ThroughputMode": "bursting", "Tags": [ { "Key": "Name", "Value": "my-file-system" } ] }`For more information, see [Creating Amazon EFS file systems](https://docs.aws.amazon.com/efs/latest/ug/creating-using-create-fs.html)in the*Amazon Elastic File System User Guide*.- 
                    For API details, see [CreateFileSystem](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/efs/create-file-system.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `create-mount-target`.

- **AWS CLI**
- 
            
                    **To create a mount target**The following `create-mount-target`example creates a mount target for the specified file system.`aws efs create-mount-target \ --file-system-id``fs-c7a0456e`\ --subnet-id`subnet-02bf4c428bexample`\ --security-groups`sg-068f739363example`Output: `{ "OwnerId": "123456789012", "MountTargetId": "fsmt-f9a14450", "FileSystemId": "fs-c7a0456e", "SubnetId": "subnet-02bf4c428bexample", "LifeCycleState": "creating", "IpAddress": "10.0.1.24", "NetworkInterfaceId": "eni-02d542216aexample", "AvailabilityZoneId": "use2-az2", "AvailabilityZoneName": "us-east-2b", "VpcId": "vpc-0123456789abcdef0" }`For more information, see [Creating mount targets](https://docs.aws.amazon.com/efs/latest/ug/accessing-fs.html)in the*Amazon Elastic File System User Guide*.- 
                    For API details, see [CreateMountTarget](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/efs/create-mount-target.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `delete-file-system`.

- **AWS CLI**
- 
            
                    **To delete a file system**The following `delete-file-system`example deletes the specified file system.`aws efs delete-file-system \ --file-system-id``fs-c7a0456e`This command produces no output. For more information, see [Deleting an Amazon EFS file system](https://docs.aws.amazon.com/efs/latest/ug/delete-efs-fs.html)in the*Amazon Elastic File System User Guide*.- 
                    For API details, see [DeleteFileSystem](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/efs/delete-file-system.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `delete-mount-target`.

- **AWS CLI**
- 
            
                    **To delete a mount target**The following `delete-mount-target`example deletes the specified mount target.`aws efs delete-mount-target \ --mount-target-id``fsmt-f9a14450`This command produces no output. For more information, see [Creating mount targets](https://docs.aws.amazon.com/efs/latest/ug/accessing-fs.html)in the*Amazon Elastic File System User Guide*.- 
                    For API details, see [DeleteMountTarget](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/efs/delete-mount-target.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `describe-file-systems`.

- **AWS CLI**
- 
            
                    **To describe a file system**The following `describe-file-systems`example describes the specified file system.`aws efs describe-file-systems \ --file-system-id``fs-c7a0456e`Output: `{ "FileSystems": [ { "OwnerId": "123456789012", "CreationToken": "console-d7f56c5f-e433-41ca-8307-9d9c0example", "FileSystemId": "fs-c7a0456e", "FileSystemArn": "arn:aws:elasticfilesystem:us-west-2:123456789012:file-system/fs-48499b4d", "CreationTime": 1595286880.0, "LifeCycleState": "available", "Name": "my-file-system", "NumberOfMountTargets": 3, "SizeInBytes": { "Value": 6144, "Timestamp": 1600991437.0, "ValueInIA": 0, "ValueInStandard": 6144 }, "PerformanceMode": "generalPurpose", "Encrypted": true, "KmsKeyId": "arn:aws:kms:us-west-2:123456789012:key/a59b3472-e62c-42e4-adcf-30d92example", "ThroughputMode": "bursting", "Tags": [ { "Key": "Name", "Value": "my-file-system" } ] } ] }`For more information, see [Managing Amazon EFS file systems](https://docs.aws.amazon.com/efs/latest/ug/managing.html)in the*Amazon Elastic File System User Guide*.- 
                    For API details, see [DescribeFileSystems](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/efs/describe-file-systems.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `describe-mount-targets`.

- **AWS CLI**
- 
            
                    **To describe a mount target**The following `describe-mount-targets`example describes the specified mount target.`aws efs describe-mount-targets \ --mount-target-id``fsmt-f9a14450`Output: `{ "MountTargets": [ { "OwnerId": "123456789012", "MountTargetId": "fsmt-f9a14450", "FileSystemId": "fs-c7a0456e", "SubnetId": "subnet-02bf4c428bexample", "LifeCycleState": "creating", "IpAddress": "10.0.1.24", "NetworkInterfaceId": "eni-02d542216aexample", "AvailabilityZoneId": "use2-az2", "AvailabilityZoneName": "us-east-2b", "VpcId": "vpc-0123456789abcdef0" } ] }`For more information, see [Creating mount targets](https://docs.aws.amazon.com/efs/latest/ug/accessing-fs.html)in the*Amazon Elastic File System User Guide*.- 
                    For API details, see [DescribeMountTargets](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/efs/describe-mount-targets.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `describe-tags`.

- **AWS CLI**
- 
            
                    **To describe the tags for a file system**The following `describe-tags`example describes the tags for the specified file system.`aws efs describe-tags \ --file-system-id``fs-c7a0456e`Output: `{ "Tags": [ { "Key": "Name", "Value": "my-file-system" }, { "Key": "Department", "Value": "Business Intelligence" } ] }`For more information, see [Managing file system tags](https://docs.aws.amazon.com/efs/latest/ug/manage-fs-tags.html)in the*Amazon Elastic File System User Guide*.- 
                    For API details, see [DescribeTags](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/efs/describe-tags.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `list-tags-for-resource`.

- **AWS CLI**
- 
            
                    **To retrieve the tags for a resource**The following `list-tags-for-resource`example retrieves the tags associated with the specified file system.`aws efs list-tags-for-resource \ --resource-id``fs-c7a0456e`Output: `{ "Tags": [ { "Key": "Name", "Value": "my-file-system" }, { "Key": "Department", "Value": "Business Intelligence" } ] }`For more information, see [Managing file system tags](https://docs.aws.amazon.com/efs/latest/ug/manage-fs-tags.html)in the*Amazon Elastic File System User Guide*.- 
                    For API details, see [ListTagsForResource](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/efs/list-tags-for-resource.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `tag-resource`.

- **AWS CLI**
- 
            
                    **To tag a resource**The following `tag-resource`example adds the tag`Department=Business Intelligence`to the specified file system.`aws efs tag-resource \ --resource-id``fs-c7a0456e`\ --tags Key=Department,Value="Business Intelligence"This command produces no output. For more information, see [Managing file system tags](https://docs.aws.amazon.com/efs/latest/ug/manage-fs-tags.html)in the*Amazon Elastic File System User Guide*.- 
                    For API details, see [TagResource](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/efs/tag-resource.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `untag-resource`.

- **AWS CLI**
- 
            
                    **To remove a tag from a resource**The following `untag-resource`example removes the tag with the`Department`tag key from the specified file system.`aws efs untag-resource \ --resource-id``fs-c7a0456e`\ --tag-keys`Department`This command produces no output. For more information, see [Managing file system tags](https://docs.aws.amazon.com/efs/latest/ug/manage-fs-tags.html)in the*Amazon Elastic File System User Guide*.- 
                    For API details, see [UntagResource](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/efs/untag-resource.html)in*AWS CLI Command Reference*.
 
-