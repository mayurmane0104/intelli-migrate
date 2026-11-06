# Command structure in the AWS CLI - AWS Command Line Interface

**Source:** [https://docs.aws.amazon.com/cli/latest/userguide/cli-usage-commandstructure.html](https://docs.aws.amazon.com/cli/latest/userguide/cli-usage-commandstructure.html)

---

This topic covers how AWS Command Line Interface (AWS CLI) command is structured, and how to use wait commands.

## Command structure

    The AWS CLI uses a multipart structure on the command line that must be specified in this order:

- 
        The base call to the `aws`program.
- 
        The top-level *command*, which typically corresponds to an AWS service supported by the AWS CLI.
- 
        The *subcommand*that specifies which operation to perform.
- 
        General AWS CLI options or parameters required by the operation. You can specify these in any order as long as they follow the first three parts. If an exclusive parameter is specified multiple times, only the *last value*applies.

`$``aws <``command`> <`subcommand`> [`options and parameters`]

Parameters can take various types of input values, such as numbers, strings, lists, maps, and JSON structures. What is supported is dependent upon the command and subcommand you specify.

**Amazon S3**

The following example lists all of your Amazon S3 buckets.

`$``aws s3 ls``2018-12-11 17:08:50 amzn-s3-demo-bucket1 2018-12-14 14:55:44 amzn-s3-demo-bucket2`

For more information on the Amazon S3 commands, see
            [ aws s3](https://docs.aws.amazon.com/cli/latest/reference/s3/index.html)
          in the 

*AWS CLI Command Reference*.

**AWS CloudFormation**

The following
            [ create-change-set](https://docs.aws.amazon.com/cli/latest/reference/cloudformation/create-change-set.html)command example changes the cloudformation
          stack name to 

`my-change-set`.`$``aws cloudformation create-change-set --stack-name``my-stack`--change-set-name`my-change-set`

For more information on the AWS CloudFormation commands, see
            [ aws
              cloudformation](https://docs.aws.amazon.com/cli/latest/reference/cloudformation/index.html) in the 

*AWS CLI Command Reference*.

## Wait commands

    Some AWS services have `wait` commands available. Any command that uses
        `aws wait` usually waits until a command is complete before it moves on to the
      next step. This is especially useful for multipart commands or scripting, as you can use a
      wait command to prevent moving to subsequent steps if the wait command fails.

The AWS CLI uses a multipart structure on the command line for the `wait` command
      that must be specified in this order:

- 
        The base call to the `aws`program.
- 
        The top-level *command*, which typically corresponds to an AWS service supported by the AWS CLI.
- 
        The `wait`command.
- 
        The *subcommand*that specifies which operation to perform.
- 
        General CLI options or parameters required by the operation. You can specify these in any order as long as they follow the first three parts. If an exclusive parameter is specified multiple times, only the *last value*applies.

`$``aws <``command`> wait <`subcommand`> [`options and parameters`]

Parameters can take various types of input values, such as numbers, strings, lists, maps, and JSON structures. What is supported is dependent upon the command and subcommand you specify.

###### Note

Not every AWS service supports `wait` commands. See the
          [AWS CLI version 2 reference guide](https://docs.aws.amazon.com/cli/latest/reference/index.html) to
        see if your service supports `wait` commands.

**AWS CloudFormation**

The following
            [ wait change-set-create-complete](https://docs.aws.amazon.com/cli/latest/reference/cloudformation/wait/change-set-create-complete.html) command
          examples pauses and resumes only after it can confirm that the
            

`my-change-set` change set in the
            `my-stack` stack is ready to run.`$``aws cloudformation wait change-set-create-complete --stack-name``my-stack`--change-set-name`my-change-set`

For more information on the AWS CloudFormation `wait` commands, see
            [ wait](https://docs.aws.amazon.com/cli/latest/reference/cloudformation/wait/index.html) in the 

*AWS CLI Command Reference*.

**AWS CodeDeploy**

The following
            [ wait
              deployment-successful](https://docs.aws.amazon.com/cli/latest/reference/cloudformation/wait/change-set-create-complete.html) command examples pauses until the
            

`d-A1B2C3111` deployment completes successfully.`$``aws deploy wait deployment-successful --deployment-id``d-A1B2C3111`

For more information on the AWS CodeDeploy `wait` commands, see
            [ wait](https://docs.aws.amazon.com/cli/latest/reference/cloudformation/wait/index.html) in the 

*AWS CLI Command Reference*.