# Amazon EC2 Instance Connect examples using AWS CLI - AWS Command Line Interface

**Source:** [https://docs.aws.amazon.com/cli/latest/userguide/cli_ec2-instance-connect_code_examples.html](https://docs.aws.amazon.com/cli/latest/userguide/cli_ec2-instance-connect_code_examples.html)

---

The following code examples show you how to perform actions and implement common scenarios by using the AWS Command Line Interface with Amazon EC2 Instance Connect.

*Actions* are code excerpts from larger programs and must be run in context. While actions show you how to call individual service functions, you can see actions in context in their related scenarios.

Each example includes a link to the complete source code, where you can find instructions on how to set up and run the code in context.

###### Topics

## Actions

    The following code example shows how to use `send-ssh-public-key`.

- **AWS CLI**
- 
            
                    **To send a an SSH public key to an instance**The following `send-ssh-public-key`example sends the specified SSH public key to the specified instance. The key is used to authenticate the specified user.`aws ec2-instance-connect send-ssh-public-key \ --instance-id``i-1234567890abcdef0`\ --instance-os-user`ec2-user`\ --availability-zone`us-east-2b`\ --ssh-public-key`file://path/my-rsa-key.pub`This command produces no output. - 
                    For API details, see [SendSshPublicKey](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2-instance-connect/send-ssh-public-key.html)in*AWS CLI Command Reference*.
 
-