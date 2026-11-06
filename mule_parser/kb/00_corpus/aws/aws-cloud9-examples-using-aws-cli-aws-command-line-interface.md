# AWS Cloud9 examples using AWS CLI - AWS Command Line Interface

**Source:** [https://docs.aws.amazon.com/cli/latest/userguide/cli_cloud9_code_examples.html](https://docs.aws.amazon.com/cli/latest/userguide/cli_cloud9_code_examples.html)

---

The following code examples show you how to perform actions and implement common scenarios by using the AWS Command Line Interface with AWS Cloud9.

*Actions* are code excerpts from larger programs and must be run in context. While actions show you how to call individual service functions, you can see actions in context in their related scenarios.

Each example includes a link to the complete source code, where you can find instructions on how to set up and run the code in context.

###### Topics

## Actions

    The following code example shows how to use `create-environment-ec2`.

- **AWS CLI**
- 
            
                    **To create an AWS Cloud9 EC2 development environment**This following `create-environment-ec2`example creates an AWS Cloud9 development environment with the specified settings, launches an Amazon Elastic Compute Cloud (Amazon EC2) instance, and then connects from the instance to the environment.`aws cloud9 create-environment-ec2 \ --name``my-demo-env`\ --description`"My demonstration development environment."`\ --instance-type`t2.micro`--image-id`amazonlinux-2023-x86_64`\ --subnet-id`subnet-1fab8aEX`\ --automatic-stop-time-minutes`60`\ --owner-arn`arn:aws:iam::123456789012:user/MyDemoUser`Output: `{ "environmentId": "8a34f51ce1e04a08882f1e811bd706EX" }`For more information, see [Creating an EC2 Environment](https://docs.aws.amazon.com/cloud9/latest/user-guide/create-environment-main.html)in the*AWS Cloud9 User Guide*.- 
                    For API details, see [CreateEnvironmentEc2](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloud9/create-environment-ec2.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `create-environment-membership`.

- **AWS CLI**
- 
            
                    **To add an environment member to an AWS Cloud9 development environment**This example adds the specified environment member to the specified AWS Cloud9 development environment. Command: `aws cloud9 create-environment-membership --environment-id``8a34f51ce1e04a08882f1e811bd706EX`--user-arn`arn:aws:iam::123456789012:user/AnotherDemoUser`--permissions`read-write`Output: `{ "membership": { "environmentId": "8a34f51ce1e04a08882f1e811bd706EX", "userId": "AIDAJ3LOROMOUXTBSU6EX", "userArn": "arn:aws:iam::123456789012:user/AnotherDemoUser", "permissions": "read-write" } }`- 
                    For API details, see [CreateEnvironmentMembership](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloud9/create-environment-membership.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `delete-environment-membership`.

- **AWS CLI**
- 
            
                    **To delete an environment member from an AWS Cloud9 development environment**This example deletes the specified environment member from the specified AWS Cloud9 development environment. Command: `aws cloud9 delete-environment-membership --environment-id``8a34f51ce1e04a08882f1e811bd706EX`--user-arn`arn:aws:iam::123456789012:user/AnotherDemoUser`Output: `None.`- 
                    For API details, see [DeleteEnvironmentMembership](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloud9/delete-environment-membership.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `delete-environment`.

- **AWS CLI**
- 
            
                    **To delete an AWS Cloud9 development environment**This example deletes the specified AWS Cloud9 development environment. If an Amazon EC2 instance is connected to the environment, also terminates the instance. Command: `aws cloud9 delete-environment --environment-id``8a34f51ce1e04a08882f1e811bd706EX`Output: `None.`- 
                    For API details, see [DeleteEnvironment](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloud9/delete-environment.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `describe-environment-memberships`.

- **AWS CLI**
- 
            
                    **To gets information about environment members for an AWS Cloud9 development environment**This example gets information about environment members for the specified AWS Cloud9 development environment. Command: `aws cloud9 describe-environment-memberships --environment-id``8a34f51ce1e04a08882f1e811bd706EX`Output: `{ "memberships": [ { "environmentId": "8a34f51ce1e04a08882f1e811bd706EX", "userId": "AIDAJ3LOROMOUXTBSU6EX", "userArn": "arn:aws:iam::123456789012:user/AnotherDemoUser", "permissions": "read-write" }, { "environmentId": "8a34f51ce1e04a08882f1e811bd706EX", "userId": "AIDAJNUEDQAQWFELJDLEX", "userArn": "arn:aws:iam::123456789012:user/MyDemoUser", "permissions": "owner" } ] }`**To get information about the owner of an AWS Cloud9 development environment**This example gets information about the owner of the specified AWS Cloud9 development environment. Command: `aws cloud9 describe-environment-memberships --environment-id``8a34f51ce1e04a08882f1e811bd706EX`--permissions`owner`Output: `{ "memberships": [ { "environmentId": "8a34f51ce1e04a08882f1e811bd706EX", "userId": "AIDAJNUEDQAQWFELJDLEX", "userArn": "arn:aws:iam::123456789012:user/MyDemoUser", "permissions": "owner" } ] }`**To get information about an environment member for multiple AWS Cloud9 development environments**This example gets information about the specified environment member for multiple AWS Cloud9 development environments. Command: `aws cloud9 describe-environment-memberships --user-arn``arn:aws:iam::123456789012:user/MyDemoUser`Output: `{ "memberships": [ { "environmentId": "10a75714bd494714929e7f5ec4125aEX", "lastAccess": 1516213427.0, "userId": "AIDAJNUEDQAQWFELJDLEX", "userArn": "arn:aws:iam::123456789012:user/MyDemoUser", "permissions": "owner" }, { "environmentId": "1980b80e5f584920801c09086667f0EX", "lastAccess": 1516144884.0, "userId": "AIDAJNUEDQAQWFELJDLEX", "userArn": "arn:aws:iam::123456789012:user/MyDemoUser", "permissions": "owner" } ] }`- 
                    For API details, see [DescribeEnvironmentMemberships](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloud9/describe-environment-memberships.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `describe-environment-status`.

- **AWS CLI**
- 
            
                    **To get status information for an AWS Cloud9 development environment**This example gets status information for the specified AWS Cloud9 development environment. Command: `aws cloud9 describe-environment-status --environment-id``685f892f431b45c2b28cb69eadcdb0EX`Output: `{ "status": "ready", "message": "Environment is ready to use" }`- 
                    For API details, see [DescribeEnvironmentStatus](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloud9/describe-environment-status.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `describe-environments`.

- **AWS CLI**
- 
            
                    **To get information about AWS Cloud9 development environments**This example gets information about the specified AWS Cloud9 development environments. Command: `aws cloud9 describe-environments --environment-ids``685f892f431b45c2b28cb69eadcdb0EX``349c86d4579e4e7298d500ff57a6b2EX`Output: `{ "environments": [ { "id": "685f892f431b45c2b28cb69eadcdb0EX", "name": "my-demo-ec2-env", "description": "Created from CodeStar.", "type": "ec2", "arn": "arn:aws:cloud9:us-east-1:123456789012:environment:685f892f431b45c2b28cb69eadcdb0EX", "ownerArn": "arn:aws:iam::123456789012:user/MyDemoUser", "lifecycle": { "status": "CREATED" } }, { "id": "349c86d4579e4e7298d500ff57a6b2EX", "name": my-demo-ssh-env", "description": "", "type": "ssh", "arn": "arn:aws:cloud9:us-east-1:123456789012:environment:349c86d4579e4e7298d500ff57a6b2EX", "ownerArn": "arn:aws:iam::123456789012:user/MyDemoUser", "lifecycle": { "status": "CREATED" } } ] }`- 
                    For API details, see [DescribeEnvironments](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloud9/describe-environments.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `list-environments`.

- **AWS CLI**
- 
            
                    **To get a list of available AWS Cloud9 development environment identifiers**This example gets a list of available AWS Cloud9 development environment identifiers. Command: `aws cloud9 list-environments`Output: `{ "environmentIds": [ "685f892f431b45c2b28cb69eadcdb0EX", "1980b80e5f584920801c09086667f0EX" ] }`- 
                    For API details, see [ListEnvironments](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloud9/list-environments.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `update-environment-membership`.

- **AWS CLI**
- 
            
                    **To change the settings of an existing environment member for an AWS Cloud9 development environment**This example changes the settings of the specified existing environment member for the specified AWS Cloud9 development environment. Command: `aws cloud9 update-environment-membership --environment-id``8a34f51ce1e04a08882f1e811bd706EX`--user-arn`arn:aws:iam::123456789012:user/AnotherDemoUser`--permissions`read-only`Output: `{ "membership": { "environmentId": "8a34f51ce1e04a08882f1e811bd706EX", "userId": "AIDAJ3LOROMOUXTBSU6EX", "userArn": "arn:aws:iam::123456789012:user/AnotherDemoUser", "permissions": "read-only" } }`- 
                    For API details, see [UpdateEnvironmentMembership](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloud9/update-environment-membership.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `update-environment`.

- **AWS CLI**
- 
            
                    **To change the settings of an existing AWS Cloud9 development environment**This example changes the specified settings of the specified existing AWS Cloud9 development environment. Command: `aws cloud9 update-environment --environment-id``8a34f51ce1e04a08882f1e811bd706EX`--name`my-changed-demo-env`--description`"My changed demonstration development environment."`Output: `None.`- 
                    For API details, see [UpdateEnvironment](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloud9/update-environment.html)in*AWS CLI Command Reference*.
 
-