# Troubleshooting errors for the AWS CLI - AWS Command Line Interface

**Source:** [https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-troubleshooting.html](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-troubleshooting.html)

---

This section covers common errors and
        troubleshooting steps to follow to resolve your issue. We suggest following the [general troubleshooting](#tshoot-general) first.

###### Contents

## General troubleshooting to try first

        If you receive an error or encounter an issue with the AWS CLI, we suggest the following general tips to help you troubleshoot.

### Check your AWS CLI command formatting

If you receive an error that indicates that a command doesn't exist, or that it
                doesn't recognize a parameter (`Parameter validation failed`) that the
                documentation says is available , then your command might be formatted incorrectly.
                We suggest that you check the following:

- 
                    Check your command for spelling and formatting errors. 
- 
                    Confirm all [quotes and escaping appropriate for your terminal](./cli-usage-parameters-quoting-strings.html)is correct in your command.
- 
                    Generate an [AWS CLI skeleton](./cli-usage-skeleton.html)to confirm your command structure.
- 
                    For JSON, see the additional [troubleshooting for JSON values](#tshoot-invalid-json). If you're having issues with your terminal processing JSON formatting, we suggest skipping past the terminal's quoting rules by using[Blobs to pass JSON data directly to the AWS CLI](./cli-usage-parameters-types.html#parameter-type-blob).

For more information on how a specific command should be structured, see the
                    [AWS CLI version 2 reference
                    guide](https://docs.aws.amazon.com/cli/latest/reference/index.html).

### Check the AWS Region your AWS CLI command is using

###### Note

You must specify an AWS Region when using the AWS CLI, either explicitly or by
                    setting a default Region. For a list of all of the AWS Regions that you can
                    specify, see [AWS Regions and Endpoints](https://docs.aws.amazon.com/general/latest/gr/rande.html)
                    in the *Amazon Web Services General Reference*. The AWS Region designators used
                    by the AWS CLI are the same names that you see in AWS Management Console URLs and service
                    endpoints.

Errors or unexpected results might occur if an AWS service isn't available for your specified AWS Region or your resources are located in a different AWS Region. In order of precedence, the AWS Region is set in the following ways:

- 
                    The `--region`command line option.
- 
                    The SDK compatible [AWS_REGION](./cli-configure-envvars.html#envvars-list-AWS_REGION)
- 
                    The [AWS_DEFAULT_REGION](./cli-configure-envvars.html#envvars-list-AWS_DEFAULT_REGION)
- 
                    The [region](./cli-configure-files.html#cli-config-region)profile setting.

Confirm you're using the correct AWS Region for your resources.

### Confirm that you're running a recent version of the AWS CLI

If you receive an error that indicates that a command doesn't exist, or that it
                doesn't recognize a parameter that the
                    [AWS CLI version 2 reference
                    guide](https://docs.aws.amazon.com/cli/latest/reference/index.html) says is available, first confirm that your command is correctly
                formatted. If the formatting is correct, then we recommend that you upgrade to the
                most recent version of the AWS CLI. Updated versions of the AWS CLI are released almost
                every business day. New AWS services, features, and parameters are introduced in
                those new versions of the AWS CLI. The only way to get access to those new services,
                features, or parameters is to upgrade to a version that was released after that
                element was first introduced.

How you update your version of the AWS CLI depends on how you originally installed
                it as described in
                    [Installing or updating to the latest version of the AWS CLI](./getting-started-install.html).

If you used one of the bundled installers, you might need to remove the existing installation before you download and install the latest version for your operating system.

### Use the `--debug` option

            When the AWS CLI reports an error that you don't immediately understand, or produces
                results that you don't expect, you can get more detail about the error by running
                the command again with the `--debug` option. With this option, the AWS CLI
                outputs details about every step it takes to process your command. The details in
                the output can help you to determine when the error occurs and provides clues about
                where it started.

You can send the output to a text file for later review, or to send to AWS Support when asked for it.

When you include the `--debug` option, some of the details
                include:

- 
                    Looking for credentials 
- 
                    Parsing the provided parameters 
- 
                    Constructing the request sent to AWS servers 
- 
                    The contents of the request sent to AWS 
- 
                    The contents of the raw response 
- 
                    The formatted output 

Here's an example of a command run with and without the `--debug`
                option.

`$ ``aws iam list-groups --profile MyTestProfile````
{
    "Groups": [
        {
            "Path": "/",
            "GroupName": "MyTestGroup",
            "GroupId": "AGPA0123456789EXAMPLE",
            "Arn": "arn:aws:iam::123456789012:group/MyTestGroup",
            "CreateDate": "2019-08-12T19:34:04Z"
        }
    ]
}
```
`$ ``aws iam list-groups --profile MyTestProfile --debug````
2019-08-12 12:36:18,305 - MainThread - awscli.clidriver - DEBUG - CLI version: aws-cli/1.16.215 Python/3.7.3 Linux/4.14.133-113.105.amzn2.x86_64 botocore/1.12.205
2019-08-12 12:36:18,305 - MainThread - awscli.clidriver - DEBUG - Arguments entered to CLI: ['iam', 'list-groups', '--debug']
2019-08-12 12:36:18,305 - MainThread - botocore.hooks - DEBUG - Event session-initialized: calling handler <function add_scalar_parsers at 0x7fdf173161e0>
2019-08-12 12:36:18,305 - MainThread - botocore.hooks - DEBUG - Event session-initialized: calling handler <function register_uri_param_handler at 0x7fdf17dec400>
2019-08-12 12:36:18,305 - MainThread - botocore.hooks - DEBUG - Event session-initialized: calling handler <function inject_assume_role_provider_cache at 0x7fdf17da9378>
2019-08-12 12:36:18,307 - MainThread - botocore.credentials - DEBUG - Skipping environment variable credential check because profile name was explicitly set.
2019-08-12 12:36:18,307 - MainThread - botocore.hooks - DEBUG - Event session-initialized: calling handler <function attach_history_handler at 0x7fdf173ed9d8>
2019-08-12 12:36:18,308 - MainThread - botocore.loaders - DEBUG - Loading JSON file: /home/ec2-user/venv/lib/python3.7/site-packages/botocore/data/iam/2010-05-08/service-2.json
2019-08-12 12:36:18,317 - MainThread - botocore.hooks - DEBUG - Event building-command-table.iam: calling handler <function add_waiters at 0x7fdf1731a840>
2019-08-12 12:36:18,320 - MainThread - botocore.loaders - DEBUG - Loading JSON file: /home/ec2-user/venv/lib/python3.7/site-packages/botocore/data/iam/2010-05-08/waiters-2.json
2019-08-12 12:36:18,321 - MainThread - awscli.clidriver - DEBUG - OrderedDict([('path-prefix', <awscli.arguments.CLIArgument object at 0x7fdf171ac780>), ('marker', <awscli.arguments.CLIArgument object at 0x7fdf171b09e8>), ('max-items', <awscli.arguments.CLIArgument object at 0x7fdf171b09b0>)])
2019-08-12 12:36:18,322 - MainThread - botocore.hooks - DEBUG - Event building-argument-table.iam.list-groups: calling handler <function add_streaming_output_arg at 0x7fdf17316510>
2019-08-12 12:36:18,322 - MainThread - botocore.hooks - DEBUG - Event building-argument-table.iam.list-groups: calling handler <function add_cli_input_json at 0x7fdf17da9d90>
2019-08-12 12:36:18,322 - MainThread - botocore.hooks - DEBUG - Event building-argument-table.iam.list-groups: calling handler <function unify_paging_params at 0x7fdf17328048>
2019-08-12 12:36:18,326 - MainThread - botocore.loaders - DEBUG - Loading JSON file: /home/ec2-user/venv/lib/python3.7/site-packages/botocore/data/iam/2010-05-08/paginators-1.json
2019-08-12 12:36:18,326 - MainThread - awscli.customizations.paginate - DEBUG - Modifying paging parameters for operation: ListGroups
2019-08-12 12:36:18,326 - MainThread - botocore.hooks - DEBUG - Event building-argument-table.iam.list-groups: calling handler <function add_generate_skeleton at 0x7fdf1737eae8>
2019-08-12 12:36:18,326 - MainThread - botocore.hooks - DEBUG - Event before-building-argument-table-parser.iam.list-groups: calling handler <bound method OverrideRequiredArgsArgument.override_required_args of <awscli.customizations.cliinputjson.CliInputJSONArgument object at 0x7fdf171b0a58>>
2019-08-12 12:36:18,327 - MainThread - botocore.hooks - DEBUG - Event before-building-argument-table-parser.iam.list-groups: calling handler <bound method GenerateCliSkeletonArgument.override_required_args of <awscli.customizations.generatecliskeleton.GenerateCliSkeletonArgument object at 0x7fdf171c5978>>
2019-08-12 12:36:18,327 - MainThread - botocore.hooks - DEBUG - Event operation-args-parsed.iam.list-groups: calling handler functools.partial(<function check_should_enable_pagination at 0x7fdf17328158>, ['marker', 'max-items'], {'max-items': <awscli.arguments.CLIArgument object at 0x7fdf171b09b0>}, OrderedDict([('path-prefix', <awscli.arguments.CLIArgument object at 0x7fdf171ac780>), ('marker', <awscli.arguments.CLIArgument object at 0x7fdf171b09e8>), ('max-items', <awscli.customizations.paginate.PageArgument object at 0x7fdf171c58d0>), ('cli-input-json', <awscli.customizations.cliinputjson.CliInputJSONArgument object at 0x7fdf171b0a58>), ('starting-token', <awscli.customizations.paginate.PageArgument object at 0x7fdf171b0a20>), ('page-size', <awscli.customizations.paginate.PageArgument object at 0x7fdf171c5828>), ('generate-cli-skeleton', <awscli.customizations.generatecliskeleton.GenerateCliSkeletonArgument object at 0x7fdf171c5978>)]))
2019-08-12 12:36:18,328 - MainThread - botocore.hooks - DEBUG - Event load-cli-arg.iam.list-groups.path-prefix: calling handler <awscli.paramfile.URIArgumentHandler object at 0x7fdf1725c978>
2019-08-12 12:36:18,328 - MainThread - botocore.hooks - DEBUG - Event load-cli-arg.iam.list-groups.marker: calling handler <awscli.paramfile.URIArgumentHandler object at 0x7fdf1725c978>
2019-08-12 12:36:18,328 - MainThread - botocore.hooks - DEBUG - Event load-cli-arg.iam.list-groups.max-items: calling handler <awscli.paramfile.URIArgumentHandler object at 0x7fdf1725c978>
2019-08-12 12:36:18,328 - MainThread - botocore.hooks - DEBUG - Event load-cli-arg.iam.list-groups.cli-input-json: calling handler <awscli.paramfile.URIArgumentHandler object at 0x7fdf1725c978>
2019-08-12 12:36:18,328 - MainThread - botocore.hooks - DEBUG - Event load-cli-arg.iam.list-groups.starting-token: calling handler <awscli.paramfile.URIArgumentHandler object at 0x7fdf1725c978>
2019-08-12 12:36:18,328 - MainThread - botocore.hooks - DEBUG - Event load-cli-arg.iam.list-groups.page-size: calling handler <awscli.paramfile.URIArgumentHandler object at 0x7fdf1725c978>
2019-08-12 12:36:18,328 - MainThread - botocore.hooks - DEBUG - Event load-cli-arg.iam.list-groups.generate-cli-skeleton: calling handler <awscli.paramfile.URIArgumentHandler object at 0x7fdf1725c978>
2019-08-12 12:36:18,329 - MainThread - botocore.hooks - DEBUG - Event calling-command.iam.list-groups: calling handler <bound method CliInputJSONArgument.add_to_call_parameters of <awscli.customizations.cliinputjson.CliInputJSONArgument object at 0x7fdf171b0a58>>
2019-08-12 12:36:18,329 - MainThread - botocore.hooks - DEBUG - Event calling-command.iam.list-groups: calling handler <bound method GenerateCliSkeletonArgument.generate_json_skeleton of <awscli.customizations.generatecliskeleton.GenerateCliSkeletonArgument object at 0x7fdf171c5978>>
2019-08-12 12:36:18,329 - MainThread - botocore.credentials - DEBUG - Looking for credentials via: assume-role
2019-08-12 12:36:18,329 - MainThread - botocore.credentials - DEBUG - Looking for credentials via: assume-role-with-web-identity
2019-08-12 12:36:18,329 - MainThread - botocore.credentials - DEBUG - Looking for credentials via: shared-credentials-file
2019-08-12 12:36:18,329 - MainThread - botocore.credentials - INFO - Found credentials in shared credentials file: ~/.aws/credentials
2019-08-12 12:36:18,330 - MainThread - botocore.loaders - DEBUG - Loading JSON file: /home/ec2-user/venv/lib/python3.7/site-packages/botocore/data/endpoints.json
2019-08-12 12:36:18,334 - MainThread - botocore.hooks - DEBUG - Event choose-service-name: calling handler <function handle_service_name_alias at 0x7fdf1898eb70>
2019-08-12 12:36:18,337 - MainThread - botocore.hooks - DEBUG - Event creating-client-class.iam: calling handler <function add_generate_presigned_url at 0x7fdf18a028c8>
2019-08-12 12:36:18,337 - MainThread - botocore.regions - DEBUG - Using partition endpoint for iam, us-west-2: aws-global
2019-08-12 12:36:18,337 - MainThread - botocore.args - DEBUG - The s3 config key is not a dictionary type, ignoring its value of: None
2019-08-12 12:36:18,340 - MainThread - botocore.endpoint - DEBUG - Setting iam timeout as (60, 60)
2019-08-12 12:36:18,341 - MainThread - botocore.loaders - DEBUG - Loading JSON file: /home/ec2-user/venv/lib/python3.7/site-packages/botocore/data/_retry.json
2019-08-12 12:36:18,341 - MainThread - botocore.client - DEBUG - Registering retry handlers for service: iam
2019-08-12 12:36:18,342 - MainThread - botocore.hooks - DEBUG - Event before-parameter-build.iam.ListGroups: calling handler <function generate_idempotent_uuid at 0x7fdf189b10d0>
2019-08-12 12:36:18,342 - MainThread - botocore.hooks - DEBUG - Event before-call.iam.ListGroups: calling handler <function inject_api_version_header_if_needed at 0x7fdf189b2a60>
2019-08-12 12:36:18,343 - MainThread - botocore.endpoint - DEBUG - Making request for OperationModel(name=ListGroups) with params: {'url_path': '/', 'query_string': '', 'method': 'POST', 'headers': {'Content-Type': 'application/x-www-form-urlencoded; charset=utf-8', 'User-Agent': 'aws-cli/1.16.215 Python/3.7.3 Linux/4.14.133-113.105.amzn2.x86_64 botocore/1.12.205'}, 'body': {'Action': 'ListGroups', 'Version': '2010-05-08'}, 'url': 'https://iam.amazonaws.com/', 'context': {'client_region': 'aws-global', 'client_config': <botocore.config.Config object at 0x7fdf16e9a4a8>, 'has_streaming_input': False, 'auth_type': None}}
2019-08-12 12:36:18,343 - MainThread - botocore.hooks - DEBUG - Event request-created.iam.ListGroups: calling handler <bound method RequestSigner.handler of <botocore.signers.RequestSigner object at 0x7fdf16e9a470>>
2019-08-12 12:36:18,343 - MainThread - botocore.hooks - DEBUG - Event choose-signer.iam.ListGroups: calling handler <function set_operation_specific_signer at 0x7fdf18996f28>
2019-08-12 12:36:18,343 - MainThread - botocore.auth - DEBUG - Calculating signature using v4 auth.
2019-08-12 12:36:18,343 - MainThread - botocore.auth - DEBUG - CanonicalRequest:
POST
/
content-type:application/x-www-form-urlencoded; charset=utf-8
host:iam.amazonaws.com
x-amz-date:20190812T193618Z
content-type;host;x-amz-date
5f776d91EXAMPLE9b8cb5eb5d6d4a787a33ae41c8cd6eEXAMPLEca69080e1e1f
2019-08-12 12:36:18,344 - MainThread - botocore.auth - DEBUG - StringToSign:
AWS4-HMAC-SHA256
20190812T193618Z
20190812/us-east-1/iam/aws4_request
ab7e367eEXAMPLE2769f178ea509978cf8bfa054874b3EXAMPLE8d043fab6cc9
2019-08-12 12:36:18,344 - MainThread - botocore.auth - DEBUG - Signature:
d85a0EXAMPLEb40164f2f539cdc76d4f294fe822EXAMPLE18ad1ddf58a1a3ce7
2019-08-12 12:36:18,344 - MainThread - botocore.endpoint - DEBUG - Sending http request: <AWSPreparedRequest stream_output=False, method=POST, url=https://iam.amazonaws.com/, headers={'Content-Type': b'application/x-www-form-urlencoded; charset=utf-8', 'User-Agent': b'aws-cli/1.16.215 Python/3.7.3 Linux/4.14.133-113.105.amzn2.x86_64 botocore/1.12.205', 'X-Amz-Date': b'20190812T193618Z', 'Authorization': b'AWS4-HMAC-SHA256 Credential=AKIA01234567890EXAMPLE-east-1/iam/aws4_request, SignedHeaders=content-type;host;x-amz-date, Signature=d85a07692aceb401EXAMPLEa1b18ad1ddf58a1a3ce7EXAMPLE', 'Content-Length': '36'}>
2019-08-12 12:36:18,344 - MainThread - urllib3.util.retry - DEBUG - Converted retries value: False -> Retry(total=False, connect=None, read=None, redirect=0, status=None)
2019-08-12 12:36:18,344 - MainThread - urllib3.connectionpool - DEBUG - Starting new HTTPS connection (1): iam.amazonaws.com:443
2019-08-12 12:36:18,664 - MainThread - urllib3.connectionpool - DEBUG - https://iam.amazonaws.com:443 "POST / HTTP/1.1" 200 570
2019-08-12 12:36:18,664 - MainThread - botocore.parsers - DEBUG - Response headers: {'x-amzn-RequestId': '74c11606-bd38-11e9-9c82-559da0adb349', 'Content-Type': 'text/xml', 'Content-Length': '570', 'Date': 'Mon, 12 Aug 2019 19:36:18 GMT'}
2019-08-12 12:36:18,664 - MainThread - botocore.parsers - DEBUG - Response body:
b'<ListGroupsResponse xmlns="https://iam.amazonaws.com/doc/2010-05-08/">\n  <ListGroupsResult>\n    <IsTruncated>false</IsTruncated>\n    <Groups>\n      <member>\n        <Path>/</Path>\n        <GroupName>MyTestGroup</GroupName>\n        <Arn>arn:aws:iam::123456789012:group/MyTestGroup</Arn>\n        <GroupId>AGPA1234567890EXAMPLE</GroupId>\n        <CreateDate>2019-08-12T19:34:04Z</CreateDate>\n      </member>\n    </Groups>\n  </ListGroupsResult>\n  <ResponseMetadata>\n    <RequestId>74c11606-bd38-11e9-9c82-559da0adb349</RequestId>\n  </ResponseMetadata>\n</ListGroupsResponse>\n'
2019-08-12 12:36:18,665 - MainThread - botocore.hooks - DEBUG - Event needs-retry.iam.ListGroups: calling handler <botocore.retryhandler.RetryHandler object at 0x7fdf16e9a780>
2019-08-12 12:36:18,665 - MainThread - botocore.retryhandler - DEBUG - No retry needed.
2019-08-12 12:36:18,665 - MainThread - botocore.hooks - DEBUG - Event after-call.iam.ListGroups: calling handler <function json_decode_policies at 0x7fdf189b1d90>
{
    "Groups": [
        {
            "Path": "/",
            "GroupName": "MyTestGroup",
            "GroupId": "AGPA123456789012EXAMPLE",
            "Arn": "arn:aws:iam::123456789012:group/MyTestGroup",
            "CreateDate": "2019-08-12T19:34:04Z"
        }
    ]
}
```
### Enable and review the AWS CLI command history logs

You can enable the AWS CLI command history logs using the [cli_history](./cli-configure-files.html#cli-config-cli_history)`aws`
                commands.

You can this list your history using the `aws history list` command,
                and use the resulting command_ids in the `aws history show` command for
                details. For more information see
                    [ aws
                        history](https://docs.aws.amazon.com/cli/latest/reference/history/index.html) in the 

*AWS CLI reference guide*.

When you include the `--debug` option, some of the details
                include:

- 
                    API calls made to botocore 
- 
                    Status codes 
- 
                    HTTP responses 
- 
                    Headers 
- 
                    Return codes 

You can use this information to confirm paramater data and API calls are behaving in the way you expect, and can then deduce at what step in the process your command is failing.

### Confirm that your AWS CLI is configured

Various errors can occur if your `config` and
                    `credentials` files or your IAM user or role is not
                configured correctly. For more information on resolving errors with
                    `config` and `credentials` files or your
                IAM user or roles, see [Access denied errors](#tshoot-access-denied) and [Invalid credentials and key errors](#tshoot-permissions-wrongcreds).

## Command not found errors

        This error means that the operating system can't find the AWS CLI command. The installation might be incomplete or requires updating.

- **Possible cause: You're trying to use an AWS CLI feature newer than your installed version, or have incorrect formatting**
- 
                    *Example error text:*`$``aws s3 copy``aws: [ERROR]: argument operation: Found invalid choice 'copy' usage: aws [options] <command> <subcommand> [<subcommand> ...] [parameters] To see help text, you can run: aws help aws <command> help aws <command> <subcommand> help`Various errors can occur if your command is formatted incorrectly or you are using an earlier version from before the feature was released. For more information on resolving errors around these two issues, see [Check your AWS CLI command formatting](#general-formatting)and[Confirm that you're running a recent version of the AWS CLI](#general-latest).
- **Possible cause: The terminal needs to be restarted after installation**
- 
                    *Example error text:*`$``aws --version``command not found: aws`If the `aws`command cannot be found after first installing or updating the AWS CLI, you might need to restart your terminal for it to recognize any`PATH`updates.
- **Possible cause: The AWS CLI did not fully install**
- 
                    *Example error text:*`$``aws --version``command not found: aws`If the `aws`command cannot be found after first installing or updating the AWS CLI, it might not have been fully installed. Try reinstalling by following the steps for your platform in[Installing or updating to the latest version of the AWS CLI](./getting-started-install.html).
- **Possible cause: The AWS CLI does not have permissions (Linux)**
- 
                    If the `aws`command cannot be found after first installing or updating the AWS CLI on Linux, it might not have`execute`permissions for the folder it installed in. Run the following command with the`PATH`to your AWS CLI installation,to provide[chmod](https://en.wikipedia.org/wiki/Chmod)`$``sudo chmod -R 755``/usr/local/aws-cli/`
- **Possible cause: The operating system**- `PATH`was not updated during installation
- 
                    *Example error text:*`$``aws --version``command not found: aws`You might need to add the `aws`executable to your operating system's`PATH`environment variable. To add the AWS CLI to your`PATH`, use the following instructions for your operating system.- 
                                        Find your shell's profile script in your user directory. If you're not sure which shell you have, run `echo $SHELL`.`$``ls -a ~``. .. .bash_logout .bash_profile .bashrc Desktop Documents Downloads`- 
                                                Bash – `.bash_profile`,`.profile`, or`.bash_login`
- 
                                                Zsh – `.zshrc`
- 
                                                Tcsh – `.tcshrc`,`.cshrc`, or`.login`
 
- 
                                                
- 
                                        Add an export command to your profile script. The following command adds your local bin to the current `PATH`variable.`export PATH=``/usr/local/bin`:$PATH
- 
                                        Reload the updated profile into your current session. `$``source ~/``.bash_profile`
 

## The "`aws --version`" command returns a different version than you installed

        Your terminal might be returning a different `PATH` for the AWS CLI than you
            expect.

- **Possible cause: The terminal needs to be restarted after installing**
- 
                    If the `aws`command shows the wrong version, you might need to restart your terminal for it to recognize any`PATH`updates. All open terminals needs to be closed, not just your active terminal.
- **Possible cause: The system needs to be restarted after installing**
- 
                    If the `aws`command shows the wrong version and restarting the terminal didn't work, you might need to restart your system for it to recognize your`PATH`updates.
- **Possible cause: You have multiple versions of the AWS CLI**
- 
                    If you updated the AWS CLI and used a different install method than your pre-existing installation, it might cause multiple versions to be installed. For example, if on Linux or macOS you used `pip`for your current install, but tried to update using the`.pkg`install file, this could cause some conflicts especially with your`PATH`pointing to the old version.To resolve this, [uninstall all versions of the AWS CLI](#tshoot-uninstall-multiple-version)and perform a clean install.After uninstalling all versions, follow instructions appropriate for your operating system to install your desired version of the [AWS CLI version 1](https://docs.aws.amazon.com/cli/v1/userguide/cli-chap-install.html)or[AWS CLI version 2](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html).###### NoteIf this is happening after you installed the AWS CLI version 2 with a pre-existing install of AWS CLI version 1, follow the migration instructions in [Installing AWS CLI version 2 from AWS CLI version 1](./cliv2-migration-instructions.html).

## The "`aws --version`" command returns a version after uninstalling the AWS CLI

        This often occurs when there is still an AWS CLI installed somewhere on your system.

- **Possible cause: The terminal needs to be restarted after uninstalling**
- 
                    If the `aws --version`command still works, you might need to restart your terminal for it to recognize any terminal updates.
- **Possible cause: You have multiple versions of the AWS CLI on your system, or didn't use the same uninstall method that you used to originally install the AWS CLI**
- 
                    The AWS CLI might not uninstall correctly if you uninstalled the AWS CLI using a different method than you used to install it, or if you installed multiple versions. For example, if you used `pip`for your current install, you must use`pip`to uninstall it. To resolve this, uninstall AWS CLI using the same method that you used to install it.- 
                            Follow the instructions appropriate for your operating system and your original installation method to uninstall the [AWS CLI version 1](https://docs.aws.amazon.com/cli/v1/userguide/cli-chap-install.html)and[AWS CLI version 2](https://docs.aws.amazon.com/cli/latest/userguide/uninstall.html).
- 
                            Close all terminals you have open. 
- 
                            Open your preferred terminal, enter in the following command and confirm that no version is returned. `$``aws --version``command not found: aws`If you still have a version listed in the output, the AWS CLI was most likely installed using a different method or there are multiple versions. If you don't know which method you installed the AWS CLI, follow the instructions for each uninstall method for the [AWS CLI version 1](https://docs.aws.amazon.com/cli/v1/userguide/cli-chap-install.html)and[AWS CLI version 2](https://docs.aws.amazon.com/cli/latest/userguide/uninstall.html)appropriate to your operating system until no version output is received.###### NoteIf you used a package manager to install the AWS CLI ( `pip`,`apt`,`brew`, etc.), you must use the same package manager to uninstall it. Be sure to follow the instructions provided by the package manager on how to uninstall all versions of a package.
 
- 
                            

## The AWS CLI processed a command with an incomplete parameter name

        - **Possible cause: You used a recognized abbreviation of the AWS CLI parameter**
- 
                    Since the AWS CLI is built using Python, the AWS CLI uses the Python `argparse`library, including the`allow_abbrev`The following `create-change-set``--change-set-n`is recognized as an abbreviation of`--change-set-name`, and the AWS CLI processes the command.`$``aws cloudformation create-change-set --stack-name my-stack``--change-set-n`my-change-setWhen your abbreviation could be multiple commands, the parameter will not be recognized as an abbreviation. The following `create-change-set``--change-set-`is**not**recognized as an abbreviation, as there are there are multiple parameters it could be an abbreviation of, such as`--change-set-name`and`--change-set-type`. Therefore the AWS CLI does**not**process the command.`$``aws cloudformation create-change-set --stack-name my-stack``--change-set-`my-change-set###### Warning**Do not**purposefully use parameter abbreviations. They are unreliable and are not backwards compatible. If any new parameters are added to a command that confuse your abbreviations, it will break your commands.Additionally, if the parameter is a single-value argument, it can cause unexpected behavior with your commands. If multiple instances of a single-value argument is passed, only the last instance will run. In the following example, the parameter `--filters`is a single-valued argument. The parameters`--filters`and`--filter`are specified. The`--filter`parameter is an abbreviation of`--filters`. This cause two instances of`--filters`being applied and only the last`--filter`argument applies.`$``aws ec2 describe-vpc-peering-connections \``--filters`Name=tag:TagName,Values=VpcPeeringConnection \`--filter`Name=status-code,Values=activeConfirm you are using valid parameters before running a command to prevent unexpected behavior. 

## Access denied errors

        - **Possible cause: The AWS CLI program file doesn't have "run" permission**
- 
                    On Linux or macOS, make sure that the `aws`program has run permissions for the calling user. Typically, the permissions are set to`755`.To add run permission for your user, run the following command, substituting `~/.local/bin/aws`with the path to the program on your computer.`$``chmod +x``~/.local/bin/aws`
- **Possible cause: Your IAM identity doesn't have permission to perform the operation**
- 
                    *Example error text:*`$``aws s3 ls``An error occurred (AcessDenied) when calling the ListBuckets operation: Access denied.`When you run a AWS CLI command, AWS operations are performed on your behalf, using credentials that associate you with an IAM account or role. The policies attached must grant you permission to call the API actions that correspond to the commands that you run with the AWS CLI. Most commands call a single action with a name that matches the command name. However, custom commands like `aws s3 sync`call multiple APIs. You can see which APIs a command calls by using the`--debug`option.If you are sure that the user or role has the proper permissions assigned by policy, make sure that your AWS CLI command is using the credentials you expect. See the [next section about credentials](#tshoot-permissions-wrongcreds)to verify that the credentials the AWS CLI is using are the ones that you expect.For information about assigning IAM permissions, see [Overview of Access Management: Permissions and Policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/introduction_access-management.html)in the*IAM User Guide*.

## Invalid credentials and key errors

        *Example error text:*

`$``aws s3 ls``An error occurred (InvalidAccessKeyId) when calling the ListBuckets operation: The AWS Access Key Id you provided does not exist in our records.`

`$``aws s3 ls``An error occurred (InvalidClientTokenId) when calling the ListBuckets operation: The security token included in the request is invalid.`

- **Possible cause: The AWS CLI is reading incorrect credentials or from an unexpected location**
- 
                    The AWS CLI might be reading credentials from a different location than you expect, or your key pair information is incorrect. You can run `aws configure list`to confirm which credentials are used.The following example shows how to check the credentials used for the default profile. `$``aws configure list``NAME : VALUE : TYPE : LOCATION profile : <not set> : None : None access_key : ****************ABCD : shared-credentials-file : secret_key : ****************ABCD : shared-credentials-file : region : us-west-2 : env : AWS_DEFAULT_REGION`The following example shows how to check the credentials of a named profile. `$``aws configure list --profile dev01``NAME : VALUE : TYPE : LOCATION profile : dev01 : None : --profile access_key : ****************ABCD : shared-credentials-file : secret_key : ****************ABCD : shared-credentials-file : region : us-west-2 : config-file : ~/.aws/config`To confirm your key pair details, check your `config`and`credentials`files. For more information on`config`and`credentials`files, see[Configuration and credential file settings in the AWS CLI](./cli-configure-files.html). For more information on credentials and authentication, including credentials precedence, see[Authentication and access credentials for the AWS CLI](./cli-chap-authentication.html).
- **Possible cause: Your computer's clock is out of sync**
- 
                    If you are using valid credentials, your clock might be out of sync. On Linux or macOS, run `date`to check the time.`$``date`If your system clock is not correct within a few minutes, use `ntpd`to sync it.`$``sudo service ntpd stop``$``sudo ntpdate time.nist.gov``$``sudo service ntpd start``$``ntpstat`On Windows, use the date and time options in the Control Panel to configure your system clock. 

## Signature does not match errors

        *Example error text:*

`$``aws s3 ls``An error occurred (SignatureDoesNotMatch) when calling the ListBuckets operation: The request signature we calculated does not match the signature you provided. Check your key and signing method.`

When the AWS CLI runs a command, it sends an encrypted request to the AWS servers to perform the appropriate AWS service operations. Your credentials (the access key and secret key) are involved in the encryption and enable AWS to authenticate the person making the request. There are several things that can interfere with the correct operation of this process, as follows.

- **Possible cause: Your clock is out of sync with the AWS servers**
- 
                    To help protect against [replay attacks](https://wikipedia.org/wiki/Replay_attack), the current time can be used during the encryption/decryption process. If the time of the client and server disagree by more than the allowed amount, the process can fail and the request is rejected. This can also happen when you run a command in a virtual machine whose clock is out of sync with the host machine's clock. One possible cause is when the virtual machine hibernates and takes some time after waking up to sync the clock with the host machine.On Linux or macOS, run `date`to check the time.`$``date`If your system clock is not correct within a few minutes, use `ntpd`to sync it.`$``sudo service ntpd stop``$``sudo ntpdate time.nist.gov``$``sudo service ntpd start``$``ntpstat`On Windows, use the date and time options in the Control Panel to configure your system clock. 
- **Possible cause: Your operating system is mishandling AWS keys that contain certain special characters**
- 
                    If your AWS keys include certain special characters, such as `-`,`+`,`/`, or`%`, some operating system variants process the string improperly and cause the key string to be interpreted incorrectly.If you process your keys using other tools or scripts, such as tools that build the credentials file on a new instance as part of its creation, those tools and scripts might have their own handling of special characters that causes them to be transformed into something that AWS no longer recognizes. We suggest regenerating the secret key to get one that does not include the special character causing issues. 

## SSL certificate errors

        - **Possible cause: The AWS CLI doesn't trust your proxy's certificate**
- 
                    *Example error text:*`$``aws s3 ls``[SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed`When you use a AWS CLI command, you receive an `[SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed`error message. This is caused by the AWS CLI not trusting your proxy's certificate due to factors such as your proxy's certificate being self-signed, with your company set as the Certification Authority (CA). This prevents the AWS CLI from finding your companies CA root certificate in the local CA registry.To fix this, instruct the AWS CLI where to find your companies `.pem`file using the[ca_bundle](./cli-configure-files.html#cli-config-ca_bundle)[--ca-bundle](./cli-configure-options.html#cli-configure-options-ca-bundle)[AWS_CA_BUNDLE](./cli-configure-envvars.html#envvars-list-AWS_CA_BUNDLE)
- **Possible cause: Your configuration isn't pointing to the correct CA root certificate location**
- 
                    *Example error text:*`$``aws s3 ls``SSL validation failed for``regionname`[Errno 2] No such file or directoryThis is caused by your Certification Authority (CA) bundle file location being configured incorrectly in the AWS CLI. To fix this, confirm where your companies `.pem`file is located and update the AWS CLI configuration by using the[ca_bundle](./cli-configure-files.html#cli-config-ca_bundle)[--ca-bundle](./cli-configure-options.html#cli-configure-options-ca-bundle)[AWS_CA_BUNDLE](./cli-configure-envvars.html#envvars-list-AWS_CA_BUNDLE)
- **Possible cause: Your configuration isn't using the correct AWS Region**
- 
                    *Example error text:*`$``aws s3 ls``[SSL: CERTIFICATE_ VERIFY_FAILED] certificate verify failed`Errors or unexpected results might occur if an AWS service isn't available for your specified AWS Region or your resources are located in a different AWS Region. For troubleshooting steps, see [Check the AWS Region your AWS CLI command is using](#general-region).
- **Possible cause: Your TLS version needs to be updated**
- 
                    *Example error text:*`$``aws s3 ls``[SSL: UNSAFE_LEGACY_RENEGOTIATION_DISABLED] unsafe legacy renegotiation disabled`The AWS service is using a version of TLS that is incompatible with your device's TLS version. To resolve this issue, update to a supported TLS version. For more information, see [Enforcing a minimum version of TLS for the AWS CLI](./cli-security-enforcing-tls.html).

## Invalid JSON errors

        *Example error text:*

`$``aws dynamodb update-table \ --provisioned-throughput``'{"ReadCapacityUnits":15,WriteCapacityUnits":10}'`\ --table-name MyDDBTable`Error parsing parameter '--provisioned-throughput': Invalid JSON: Expecting property name enclosed in double quotes: line 1 column 25 (char 24) JSON received: {"ReadCapacityUnits":15,WriteCapacityUnits":10}`

When you use an AWS CLI command, you receive a "`Invalid JSON`" error
            message. This is usually an error seen when you enter a command with an expected JSON
            format and the AWS CLI cannot read your JSON correctly.

- **Possible cause: You did not enter valid JSON for the AWS CLI to use**
- 
                    Confirm you have valid JSON entered for your command. We suggest using a JSON validator for JSON you're having issues formatting. For more advanced JSON usage in the command line, consider using a command line JSON processor, like `jq`, to create JSON strings. For more information on`jq`, see the[jq repository](http://stedolan.github.io/jq/)on*GitHub*.
- **Possible cause: Your terminal's quoting rules are preventing valid JSON being sent to the AWS CLI**
- 
                    Before the AWS CLI receives anything from a command, your terminal processes the command using it's own quoting and escaping rules. Due to a terminal's formatting rules, some of your JSON content may be stripped before the command is passed to the AWS CLI. When formulating commands, be sure to use your [terminal's quoting rules](./cli-usage-parameters-quoting-strings.html).To troubleshoot, use the `echo`command to see how the shell is handling your parameters:`$``echo {"ReadCapacityUnits":15,"WriteCapacityUnits":10}``ReadCapacityUnits:15 WriteCapacityUnits:10``$``echo '{"ReadCapacityUnits":15,"WriteCapacityUnits":10}'``{"ReadCapacityUnits":15,"WriteCapacityUnits":10}`Modify your command until your until valid JSON is returned. For more in-depth troubleshooting, use the `--debug`parameter to view the debug logs as they'll display exactly what got passed to the AWS CLI:`$``aws dynamodb update-table \ --provisioned-throughput``'{"ReadCapacityUnits":15,WriteCapacityUnits":10}'`\ --table-name MyDDBTable \ --debug`2022-07-19 22:25:07,741 - MainThread - awscli.clidriver - DEBUG - CLI version: aws-cli/1.18.147 Python/2.7.18 Linux/5.4.196-119.356.amzn2int.x86_64 botocore/1.18.6 2022-07-19 22:25:07,741 - MainThread - awscli.clidriver - DEBUG - Arguments entered to CLI: ['dynamodb', 'update-table', '--provisioned-throughput', '{"ReadCapacityUnits":15,WriteCapacityUnits":10}', '--table-name', 'MyDDBTable', '--debug']`Use your terminal's quoting rules to fix any issues your JSON input has when being sent to the AWS CLI. For more information on quoting rules, see [Using quotation marks and literals with strings in the AWS CLI](./cli-usage-parameters-quoting-strings.html).###### NoteIf you're having issues with getting valid JSON to the AWS CLI, we recommend to bypass a terminal's quoting rules for JSON data input by using Blobs to pass your JSON data directly to the AWS CLI. For more information on Blobs, see [Blob](./cli-usage-parameters-types.html#parameter-type-blob).

## Additional resources

        For additional help with your AWS CLI issues, visit the [AWS CLI community](https://github.com/aws/aws-cli/issues) on 

*GitHub*or the

[AWS re:Post community](https://repost.aws/).