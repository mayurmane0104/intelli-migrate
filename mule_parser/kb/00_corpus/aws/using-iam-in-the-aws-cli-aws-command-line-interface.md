# Using IAM in the AWS CLI - AWS Command Line Interface

**Source:** [https://docs.aws.amazon.com/cli/latest/userguide/cli-services-iam.html](https://docs.aws.amazon.com/cli/latest/userguide/cli-services-iam.html)

---

| An introduction to AWS Identity and Access Management | 
|---|
|  | 

You can access the features of AWS Identity and Access Management (IAM) using the AWS Command Line Interface (AWS CLI). To list the AWS CLI commands for IAM, use the following command.

`aws iam help`

This topic shows examples of AWS CLI commands that perform common tasks for IAM.

Before you run any commands, set your default credentials. For more information, see [Configuring settings for the AWS CLI](./cli-chap-configure.html).

For more information on the IAM service, see the [AWS Identity and Access Management User Guide](https://docs.aws.amazon.com/IAM/latest/UserGuide/introduction.html).

###### Topics

## Creating IAM users and groups

  
  ###### To create a group and add a new user to it

- 
      Use the `create-group``$``aws iam create-group --group-name``MyIamGroup``{ "Group": { "GroupName": "MyIamGroup", "CreateDate": "2018-12-14T03:03:52.834Z", "GroupId": "AGPAJNUJ2W4IJVEXAMPLE", "Arn": "arn:aws:iam::123456789012:group/``MyIamGroup`", "Path": "/" } }
- 
      Use the `create-user``$``aws iam create-user --user-name``MyUser``{ "User": { "UserName": "``MyUser`", "Path": "/", "CreateDate": "2018-12-14T03:13:02.581Z", "UserId": "AIDAJY2PE5XUZ4EXAMPLE", "Arn": "arn:aws:iam::123456789012:user/`MyUser`" } }
- 
      Use the `add-user-to-group``$``aws iam add-user-to-group --user-name``MyUser`--group-name`MyIamGroup`
- 
      To verify that the `MyIamGroup`group contains the`MyUser`, use the`get-group``$``aws iam get-group --group-name``MyIamGroup``{ "Group": { "GroupName": "``MyIamGroup`", "CreateDate": "2018-12-14T03:03:52Z", "GroupId": "AGPAJNUJ2W4IJVEXAMPLE", "Arn": "arn:aws:iam::123456789012:group/`MyIamGroup`", "Path": "/" }, "Users": [ { "UserName": "`MyUser`", "Path": "/", "CreateDate": "2018-12-14T03:13:02Z", "UserId": "AIDAJY2PE5XUZ4EXAMPLE", "Arn": "arn:aws:iam::123456789012:user/`MyUser`" } ], "IsTruncated": "false" }

## Attaching an IAM managed policy to a user

  The policy in this example provides the user with "Power User Access".

###### To attach an IAM managed policy to a user

- 
      Determine the Amazon Resource Name (ARN) of the policy to attach. The following command uses `list-policies`to find the ARN of the policy with the name`PowerUserAccess`. It then stores that ARN in an environment variable.`$``export``POLICYARN`=$(aws iam list-policies --query 'Policies[?PolicyName==`PowerUserAccess`].{ARN:Arn}' --output text) ~`$``echo $``POLICYARN``arn:aws:iam::aws:policy/PowerUserAccess`
- 
      To attach the policy, use the `attach-user-policy``$``aws iam attach-user-policy --user-name``MyUser`--policy-arn $`POLICYARN`
- 
      Verify that the policy is attached to the user by running the `list-attached-user-policies``$``aws iam list-attached-user-policies --user-name``MyUser``{ "AttachedPolicies": [ { "PolicyName": "PowerUserAccess", "PolicyArn": "arn:aws:iam::aws:policy/PowerUserAccess" } ] }`

For more information, see [Access Management Resources](https://docs.aws.amazon.com/IAM/latest/UserGuide/policies-additional-resources.html). This topic provides links to an overview of
        permissions and policies, and links to examples of policies for accessing Amazon S3, Amazon EC2, and
        other services.

## Setting an initial password for an IAM user

  The following command uses
        [create-login-profile](https://docs.aws.amazon.com/cli/latest/reference/iam/create-login-profile.html)

`$``aws iam create-login-profile --user-name``MyUser`--password`My!User1Login8P@ssword`--password-reset-required`{ "LoginProfile": { "UserName": "``MyUser`", "CreateDate": "2018-12-14T17:27:18Z", "PasswordResetRequired": true } }

You can use the `update-login-profile` command to *change* the password for a user.

`$``aws iam update-login-profile --user-name``MyUser`--password`My!User1ADifferentP@ssword`

## Creating an access key for an IAM user

  You can use the
      [ create-access-key](https://docs.aws.amazon.com/cli/latest/reference/iam/create-access-key.html) command to create an access key for a user. An
    access key is a set of security credentials that consists of an access key ID and a secret key. 

A user can create only two access keys at one time. If you try to create a third set, the
    command returns a `LimitExceeded` error.

`$``aws iam create-access-key --user-name``MyUser``{ "AccessKey": { "UserName": "``MyUser`", "AccessKeyId": "AKIAIOSFODNN7EXAMPLE", "Status": "Active", "SecretAccessKey": "wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY", "CreateDate": "2018-12-14T17:34:16Z" } }

Use the
      [ delete-access-key](https://docs.aws.amazon.com/cli/latest/reference/iam/delete-access-key.html) command to delete an access key for a user. Specify
    which access key to delete by using the access key ID.

`$``aws iam delete-access-key --user-name``MyUser`--access-key-id AKIAIOSFODNN7EXAMPLE