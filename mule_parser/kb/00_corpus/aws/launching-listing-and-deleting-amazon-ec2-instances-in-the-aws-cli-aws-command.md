# Launching, listing, and deleting Amazon EC2 instances in the AWS CLI - AWS Command Line Interface

**Source:** [https://docs.aws.amazon.com/cli/latest/userguide/cli-services-ec2-instances.html](https://docs.aws.amazon.com/cli/latest/userguide/cli-services-ec2-instances.html)

---

You can use the AWS Command Line Interface (AWS CLI) to launch, list, and delete Amazon Elastic Compute Cloud (Amazon EC2) instances. If you launch an instance that isn't within the AWS Free Tier, you are billed after you launch the instance and charged for the time that the instance is running, even if it remains idle.

###### Note

For additional command examples, see the
                [AWS CLI reference
                guide](https://docs.aws.amazon.com/cli/latest/reference/index.html).

###### Topics

## Prerequisites

        To run the `ec2` commands in this topic, you need to:

- Install and configure the AWS CLI. For more information, see - [Installing or updating to the latest version of the AWS CLI](./getting-started-install.html)and- [Authentication and access credentials for the AWS CLI](./cli-chap-authentication.html).
- 
                Set your IAM permissions to allow for Amazon EC2 access. For more information about IAM permissions for Amazon EC2, see [IAM policies for Amazon EC2](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/iam-policies-for-amazon-ec2.html)in the*Amazon EC2 User Guide*.
- 
                Create a [key pair](./cli-services-ec2-keypairs.html)and a[security group](./cli-services-ec2-sg.html).
- 
                Select an Amazon Machine Image (AMI) and note the AMI ID. For more information, see [Finding a Suitable AMI](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/finding-an-ami.html)in the*Amazon EC2 User Guide*.

## Launch your instance

        To launch an Amazon EC2 instance using the AMI you selected, use the
                    [aws ec2
                    run-instances](https://docs.aws.amazon.com/cli/latest/reference/ec2/run-instances.html)

Initially, your instance appears in the `pending` state, but changes to the
                `running` state after a few minutes.

The following example shows how to launch a `t2.micro` instance in the
                specified subnet of a VPC. Replace the `italicized`
                parameter values with your own.

`$``aws ec2 run-instances --image-id``ami-xxxxxxxx`--count 1 --instance-type t2.micro --key-name`MyKeyPair`--security-group-ids`sg-903004f8`--subnet-id`subnet-6e7f829e``{ "OwnerId": "123456789012", "ReservationId": "r-5875ca20", "Groups": [ { "GroupName": "my-sg", "GroupId": "sg-903004f8" } ], "Instances": [ { "Monitoring": { "State": "disabled" }, "PublicDnsName": null, "Platform": "windows", "State": { "Code": 0, "Name": "pending" }, "EbsOptimized": false, "LaunchTime": "2013-07-19T02:42:39.000Z", "PrivateIpAddress": "10.0.1.114", "ProductCodes": [], "VpcId": "vpc-1a2b3c4d", "InstanceId": "i-5203422c", "ImageId": "ami-173d747e", "PrivateDnsName": "ip-10-0-1-114.ec2.internal", "KeyName": "MyKeyPair", "SecurityGroups": [ { "GroupName": "my-sg", "GroupId": "sg-903004f8" } ], "ClientToken": null, "SubnetId": "subnet-6e7f829e", "InstanceType": "t2.micro", "NetworkInterfaces": [ { "Status": "in-use", "SourceDestCheck": true, "VpcId": "vpc-1a2b3c4d", "Description": "Primary network interface", "NetworkInterfaceId": "eni-a7edb1c9", "PrivateIpAddresses": [ { "PrivateDnsName": "ip-10-0-1-114.ec2.internal", "Primary": true, "PrivateIpAddress": "10.0.1.114" } ], "PrivateDnsName": "ip-10-0-1-114.ec2.internal", "Attachment": { "Status": "attached", "DeviceIndex": 0, "DeleteOnTermination": true, "AttachmentId": "eni-attach-52193138", "AttachTime": "2013-07-19T02:42:39.000Z" }, "Groups": [ { "GroupName": "my-sg", "GroupId": "sg-903004f8" } ], "SubnetId": "subnet-6e7f829e", "OwnerId": "123456789012", "PrivateIpAddress": "10.0.1.114" } ], "SourceDestCheck": true, "Placement": { "Tenancy": "default", "GroupName": null, "AvailabilityZone": "us-west-2b" }, "Hypervisor": "xen", "BlockDeviceMappings": [ { "DeviceName": "/dev/sda1", "Ebs": { "Status": "attached", "DeleteOnTermination": true, "VolumeId": "vol-877166c8", "AttachTime": "2013-07-19T02:42:39.000Z" } } ], "Architecture": "x86_64", "StateReason": { "Message": "pending", "Code": "pending" }, "RootDeviceName": "/dev/sda1", "VirtualizationType": "hvm", "RootDeviceType": "ebs", "Tags": [ { "Value": "MyInstance", "Key": "Name" } ], "AmiLaunchIndex": 0 } ] }`

## Add a block device to your instance

    Each instance that you launch has an associated root device volume. You can use block device mapping to specify additional Amazon Elastic Block Store (Amazon EBS) volumes or instance store volumes to attach to an instance when it's launched.

To add a block device to your instance, specify the `--block-device-mappings`
      option when you use `run-instances`.

The following example parameter provisions a standard Amazon EBS volume that is 20 GB in size,
      and maps it to your instance using the identifier `/dev/sdf`.

`--block-device-mappings "[{\"DeviceName\":\"``/dev/sdf`\",\"Ebs\":{\"VolumeSize\":`20`,\"DeleteOnTermination\":false}}]"

The following example adds an Amazon EBS volume, mapped to `/dev/sdf`, based
      on an existing snapshot. A snapshot represents an image that is loaded onto the volume for
      you. When you specify a snapshot, you don't have to specify a volume size; it will be large
      enough to hold your image. However, if you do specify a size, it must be greater than or equal
      to the size of the snapshot.

`--block-device-mappings "[{\"DeviceName\":\"``/dev/sdf`\",\"Ebs\":{\"SnapshotId\":\"`snap-a1b2c3d4`\"}}]"

The following example adds two volumes to your instance. The number of volumes available to your instance depends on its instance type.

`--block-device-mappings "[{\"DeviceName\":\"``/dev/sdf`\",\"VirtualName\":\"`ephemeral0`\"},{\"DeviceName\":\"`/dev/sdg`\",\"VirtualName\":\"`ephemeral1`\"}]"

The following example creates the mapping (`/dev/sdj`), but doesn't
      provision a volume for the instance.

`--block-device-mappings "[{\"DeviceName\":\"``/dev/sdj`\",\"NoDevice\":\"\"}]"

For more information, see [Block Device Mapping](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/block-device-mapping-concepts.html) in the *Amazon EC2 User Guide*.

## Add a tag to your instance

    A tag is a label that you assign to an AWS resource. It enables you to add metadata to
            your resources that you can use for a variety of purposes. For more information, see
                [Tagging Your Resources](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/Using_Tags.html) in the
                *Amazon EC2 User Guide*.

The following example shows how to add a tag with the key name "`Name`" and the
            value "`MyInstance`" to the specified instance, by using the
                    [aws ec2
                    create-tags](https://docs.aws.amazon.com/cli/latest/reference/ec2/create-tags.html)

`$``aws ec2 create-tags --resources``i-5203422c`--tags Key=`Name`,Value=`MyInstance`

## Connect to your instance

    When your instance is running, you can connect to it and use it just as you'd use a
      computer sitting in front of you. For more information, see [Connect to Your Amazon EC2 Instance](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/connect-to-linux-instance.html) in the
        *Amazon EC2 User Guide*.

## List your instances

    You can use the AWS CLI to list your instances and view information about them. You can list all your instances, or filter the results based on the instances that you're interested in.

The following examples show how to use the
                    [aws ec2
                    describe-instances](https://docs.aws.amazon.com/cli/latest/reference/ec2/describe-instances.html)

The following command lists all your instances.

`$``aws ec2 describe-instances`

The following command filters the list to only your `t2.micro` instances and
      outputs only the `InstanceId` values for each match.

`$``aws ec2 describe-instances --filters "Name=instance-type,Values=t2.micro" --query "Reservations[].Instances[].InstanceId"``[ "i-05e998023d9c69f9a" ]`

The following command lists any of your instances that have the tag
        `Name=MyInstance`.

`$``aws ec2 describe-instances --filters "Name=tag:``Name`,Values=`MyInstance`"

The following command lists your instances that were launched using any of the following
      AMIs: `ami-x0123456`, `ami-y0123456`, and
      `ami-z0123456`.

`$``aws ec2 describe-instances --filters "Name=image-id,Values=``ami-x0123456`,`ami-y0123456`,`ami-z0123456`"

## Delete your instance

        You can use the AWS CLI to terminate (delete) an Amazon EC2 instance when you no longer need it.

###### Important

**Terminating an instance is permanent and irreversible.**

After you terminate an instance, you can no longer connect to it, and it can't be recovered. 
              All attached Amazon EBS volumes that are configured to be deleted on termination are also permanently 
              deleted and can't be recovered. All data stored on instance store volumes is permanently lost. 
              For more information, see [
                  How instance termination works](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/how-ec2-instance-termination-works.html).

Before you terminate an instance, ensure that you have backed up all data that you need to retain after the termination to persistent storage.

As soon as the state of the instance changes to `shutting-down` or
        `terminated`, you stop incurring charges for that instance. If you want to
      reconnect to an instance later, use [stop-instances](https://docs.aws.amazon.com/cli/v1/reference/ec2/stop-instances.html) instead of `terminate-instances`. For more information,
      see [Terminate Your Instance](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/terminating-instances.html) in
      the *Amazon EC2 User Guide*.

The following example shows how to delete an instance using the 
                    [aws
                    ec2 terminate-instances](https://docs.aws.amazon.com/cli/latest/reference/ec2/terminate-instances.html)

`$``aws ec2 terminate-instances --instance-ids``i-5203422c``{ "TerminatingInstances": [ { "InstanceId": "i-5203422c", "CurrentState": { "Code": 32, "Name": "shutting-down" }, "PreviousState": { "Code": 16, "Name": "running" } } ] }`

## References

        **AWS CLI reference:**

**Other reference:**

- 
                To view and contribute to AWS SDK and AWS CLI code examples, see the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/)on*GitHub*.