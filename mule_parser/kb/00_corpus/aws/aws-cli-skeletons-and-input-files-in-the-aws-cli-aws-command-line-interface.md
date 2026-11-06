# AWS CLI skeletons and input files in the AWS CLI - AWS Command Line Interface

**Source:** [https://docs.aws.amazon.com/cli/latest/userguide/cli-usage-skeleton.html](https://docs.aws.amazon.com/cli/latest/userguide/cli-usage-skeleton.html)

---

Most of the AWS CLI commands accept importing parameter inputs from a file. These templates
        can be generated using the `generate-cli-skeleton` option and then be imported
        using the `--cli-input-json`
            and `--cli-input-yaml` parameters.

###### Topics

## About AWS CLI skeletons and input files

        Most of the AWS Command Line Interface (AWS CLI) commands support the ability to accept parameter inputs
            from a file using the `--cli-input-json`
                and `--cli-input-yaml`
                parameters.

Those same commands use the `--generate-cli-skeleton` parameter to generate
            a file in either
            JSON or
                YAML format with all of the parameters that you can edit and fill in. Then
            you can run the command with the `--cli-input-json`
                or `--cli-input-yaml` parameter and point to the filled-in
            file.

###### Important

Custom AWS CLI commands, such as the
                    [ aws s3
                    commands](https://docs.aws.amazon.com/cli/latest/reference/s3/index.html) don't support either the 

`--generate-cli-skeleton`
                or `--cli-input-json`
                    and `--cli-input-yaml` parameters described in this topic.
                To check if a specific command supports these parameters, run the [help command](./cli-usage-help.html#cli-usage-help-command)for the command you want to use or refer to the

[AWS CLI version 2 reference guide](https://docs.aws.amazon.com/cli/latest/reference/index.html).

The `--generate-cli-skeleton` generates and displays a parameter template
            that you can customize and use as input on a command. The generated template includes
            all of the parameters that the command supports.

The `--generate-cli-skeleton` parameter accepts one of the following
            values:

- 
                `input`– The generated template includes all input parameters formatted as JSON. This is the default value.
- 
                `yaml-input`– The generated template includes all input parameters formatted as YAML.
- 
                `output`– The generated template includes all output parameters formatted as JSON. You can't currently request the output parameters as YAML.

Because the AWS CLI is essentially a "wrapper" around the service's API, the skeleton
            file expects you to reference all parameters by their underlying API parameter names.
            This is likely different from the AWS CLI parameter name. For example, an AWS CLI parameter
            named `user-name` might map to the AWS service's API parameter named
                `UserName` (notice the altered capitalization and missing dash). We
            recommend that you use the `--generate-cli-skeleton` option to generate the
            template with the "correct" parameter names to avoid errors. You can reference the API
            Reference Guide for the service to see the expected parameter names. You can delete any
            parameters from the template that are not required and for which you don't want to
            supply a value.

For example, if you run the following command, it generates the parameter template for
            the Amazon Elastic Compute Cloud (Amazon EC2) command **run-instances**.

The following example shows how to generate a template formatted in JSON
                        by using the default value (`input`) for the
                            `--generate-cli-skeleton` parameter.

`$``aws ec2 run-instances --generate-cli-skeleton`

```
{
    "DryRun": true,
    "ImageId": "",
    "MinCount": 0,
    "MaxCount": 0,
    "KeyName": "",
    "SecurityGroups": [
        ""
    ],
    "SecurityGroupIds": [
        ""
    ],
    "UserData": "",
    "InstanceType": "",
    "Placement": {
        "AvailabilityZone": "",
        "GroupName": "",
        "Tenancy": ""
    },
    "KernelId": "",
    "RamdiskId": "",
    "BlockDeviceMappings": [
        {
            "VirtualName": "",
            "DeviceName": "",
            "Ebs": {
                "SnapshotId": "",
                "VolumeSize": 0,
                "DeleteOnTermination": true,
                "VolumeType": "",
                "Iops": 0,
                "Encrypted": true
            },
            "NoDevice": ""
        }
    ],
    "Monitoring": {
        "Enabled": true
    },
    "SubnetId": "",
    "DisableApiTermination": true,
    "InstanceInitiatedShutdownBehavior": "",
    "PrivateIpAddress": "",
    "ClientToken": "",
    "AdditionalInfo": "",
    "NetworkInterfaces": [
        {
            "NetworkInterfaceId": "",
            "DeviceIndex": 0,
            "SubnetId": "",
            "Description": "",
            "PrivateIpAddress": "",
            "Groups": [
                ""
            ],
            "DeleteOnTermination": true,
            "PrivateIpAddresses": [
                {
                    "PrivateIpAddress": "",
                    "Primary": true
                }
            ],
            "SecondaryPrivateIpAddressCount": 0,
            "AssociatePublicIpAddress": true
        }
    ],
    "IamInstanceProfile": {
        "Arn": "",
        "Name": ""
    },
    "EbsOptimized": true
}
```
## Generate and import a command skeleton

        ###### To generate and use a parameter skeleton file

- 
                Run the command with the `--generate-cli-skeleton`parameter to produce either JSON or YAML and direct the output to a file to save it.`$``aws ec2 run-instances --generate-cli-skeleton input``> ec2runinst.json`
- 
                Open the parameter skeleton file in your text editor and remove any of the parameters that you don't need. For example, you might strip the template down to the following. Confirm the file is still valid JSON or YAML after you remove the elements you don't need. `{ "DryRun": true, "ImageId": "", "KeyName": "", "SecurityGroups": [ "" ], "InstanceType": "", "Monitoring": { "Enabled": true } }`In this example, we leave the `DryRun`parameter set to`true`to use the Amazon EC2 dry run feature. This feature lets you safely test the command without actually creating or modifying any resources.
- 
                Fill in the remaining values with values appropriate for your scenario. In this example, we provide the instance type, key name, security group, and identifier of the Amazon Machine Image (AMI) to use. This example assumes the default AWS Region. The AMI `ami-dfc39aef`is a 64-bit Amazon Linux image hosted in the`us-west-2`Region. If you use a different Region, you must[find the correct AMI ID to use](http://aws.amazon.com/amazon-linux-ami/).`{ "DryRun": true, "ImageId": "``ami-dfc39aef`", "KeyName": "`mykey`", "SecurityGroups": [ "`my-sg`" ], "InstanceType": "`t2.micro`", "Monitoring": { "Enabled": true } }
- 
                Run the command with the completed parameters by passing the completed template file to either the `--cli-input-json`or --`cli-input-yaml`parameter by using the`file://`prefix. The AWS CLI interprets the path to be relative to your current working directory. The following example the AWS CLI looks for the file in the current working directory.`$``aws ec2 run-instances --cli-input-json file://ec2runinst.json``A client error (DryRunOperation) occurred when calling the RunInstances operation: Request would have succeeded, but DryRun flag is set.`The dry run error indicates that the JSON or YAML is formed correctly and that the parameter values are valid. If other issues are reported in the output, fix them and repeat the previous step until the " `Request would have succeeded`" message is displayed.
- 
                Now you can set the `DryRun`parameter to`false`to disable dry run.`{ "DryRun": false, "ImageId": "ami-dfc39aef", "KeyName": "mykey", "SecurityGroups": [ "my-sg" ], "InstanceType": "t2.micro", "Monitoring": { "Enabled": true } }`
- 
                Run the command, and `run-instances`actually launches an Amazon EC2 instance and displays the details generated by the successful launch. The format of the output is controlled by the`--output`parameter, separately from the format of your input parameter template.`$``aws ec2 run-instances --cli-input-json file://ec2runinst.json --output json``{ "OwnerId": "123456789012", "ReservationId": "r-d94a2b1", "Groups": [], "Instances": [ ...`

## Combining input files and command line parameters

        An input file can be used for all parameters, or can be combined with parameters specified in the AWS CLI. You can use this feature for settings you frequently reuse in an input file, while keeping your individual settings in the command itself.

The following `aws ec2 run-instances` examples combine the use of an input
            file and parameters. We provide the instance type, key name, security group, identifier
            of the Amazon Machine Image (AMI) to use and assume the default AWS Region. The AMI
                `ami-dfc39aef` is a 64-bit Amazon Linux image hosted in the
                `us-west-2` Region. If you use a different Region, you must [find the correct AMI ID to
            use](http://aws.amazon.com/amazon-linux-ami/).

Contents of the JSON file:

```
{
    "ImageId": "
```
`ami-dfc39aef`",
    "KeyName": "`mykey`",
    "SecurityGroups": [
        "`my-sg`"
    ],
    "InstanceType": "`t2.micro`",
    "Monitoring": {
        "Enabled": true
    }
}The following example uses the input file in combination with the
                `--dry-run` parameter to perform a dry-run of the command to confirm
            whether you have the required permissions and have filled out the file with valid
            values.

`$``aws ec2 run-instances --cli-input-json file://ec2runinst.json``--dry-run`

`A client error (DryRunOperation) occurred when calling the RunInstances operation: Request would have succeeded, but DryRun flag is set.`The following example then uses the same input file, but with the
                `--no-dry-run` parameter to perform the command in full.

`$``aws ec2 run-instances --cli-input-json file://ec2runinst.json``--no-dry-run`--output json

```
{
    "OwnerId": "123456789012",
    "ReservationId": "r-d94a2b1",
    "Groups": [],
    "Instances": [
...
```