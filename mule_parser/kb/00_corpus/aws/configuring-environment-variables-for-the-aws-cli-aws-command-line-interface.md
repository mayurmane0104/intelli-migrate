# Configuring environment variables for the AWS CLI - AWS Command Line Interface

**Source:** [https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-envvars.html](https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-envvars.html)

---

Environment variables provide another way to specify configuration options and credentials, and can be useful for scripting.

###### Precedence of options

- 
            If you specify an option by using one of the environment variables described in this topic, it overrides any value loaded from a profile in the configuration file. 
- 
            If you specify an option by using a parameter on the AWS CLI command line, it overrides any value from either the corresponding environment variable or a profile in the configuration file. 

For more information about precedence and how the AWS CLI determines which credentials to
        use, see [Configuring settings for the AWS CLI](./cli-chap-configure.html).

## How to set environment variables

        The following examples show how you can configure environment variables for the default user.

`$``export AWS_ACCESS_KEY_ID=``AKIAIOSFODNN7EXAMPLE``$``export AWS_SECRET_ACCESS_KEY=``wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY``$``export AWS_DEFAULT_REGION=``us-west-2`

Setting the environment variable changes the value used until the end of your shell session, or until you set the variable to a different value. You can make the variables persistent across future sessions by setting them in your shell's startup script.

## AWS CLI supported environment variables

        The AWS CLI supports the following environment variables.

- `AWS_ACCESS_KEY_ID`
- 
                    Specifies an AWS access key associated with an IAM account. If defined, this environment variable overrides the value for the profile setting `aws_access_key_id`. You can't specify the access key ID by using a command line option.
- `AWS_ACCOUNT_ID`
- 
                    
                    Specifies the AWS account-based endpoint ID to use for calls to supported AWS services. For more information on account-based endpoints, see [Account-based endpoints](./cli-configure-endpoints.html#endpoints-accountid).This setting overrides the [aws_account_id](./cli-configure-files.html#cli-config-aws_account_id)[AWS_ACCOUNT_ID_ENDPOINT_MODE](#envvars-list-AWS_ACCOUNT_ID_ENDPOINT_MODE)[account_id_endpoint_mode](./cli-configure-files.html#cli-config-account_id_endpoint_mode)`preferred`or`required`to use this setting.###### Endpoint precedenceEndpoint configuration settings are located in multiple places, such as the system or user environment variables, local AWS configuration files, or explicitly declared on the command line as a parameter. The AWS CLI checks these endpoint settings in a particular order, and uses the endpoint setting with the highest precedence. For the endpoint precedence list, see [Endpoint configuration and settings precedence](./cli-configure-endpoints.html#endpoints-precedence).
- `AWS_ACCOUNT_ID_ENDPOINT_MODE`
- 
                    
                    Specifies whether to use AWS account-based endpoint IDs for calls to supported AWS services. For more information on account-based endpoints, see [Account-based endpoints](./cli-configure-endpoints.html#endpoints-accountid).This setting can be set to the following: - 
                            **(default)**`preferred`
- 
                            `disabled`
- 
                            `required`
 This setting overrides the [account_id_endpoint_mode](./cli-configure-files.html#cli-config-account_id_endpoint_mode)[AWS_ACCOUNT_ID](#envvars-list-AWS_ACCOUNT_ID)[aws_account_id](./cli-configure-files.html#cli-config-aws_account_id)###### Endpoint precedenceEndpoint configuration settings are located in multiple places, such as the system or user environment variables, local AWS configuration files, or explicitly declared on the command line as a parameter. The AWS CLI checks these endpoint settings in a particular order, and uses the endpoint setting with the highest precedence. For the endpoint precedence list, see [Endpoint configuration and settings precedence](./cli-configure-endpoints.html#endpoints-precedence).
- 
                            
- `AWS_CA_BUNDLE`
- 
                    Specifies the path to a certificate bundle to use for HTTPS certificate validation. If defined, this environment variable overrides the value for the profile setting [ca_bundle](./cli-configure-files.html#cli-config-ca_bundle)[--ca-bundle](./cli-configure-options.html#cli-configure-options-ca-bundle)
- `AWS_CLI_AUTO_PROMPT`
- 
                    Enables the auto-prompt for the AWS CLI version 2. There are two settings that can be used: - 
                            `on``aws`command. This includes pressing**ENTER**after both a complete command or incomplete command.
- 
                            `on-partial`
 If defined, this environment variable overrides the value for the [cli_auto_prompt](./cli-configure-files.html#cli-config-cli_auto_prompt)[--cli-auto-prompt](./cli-configure-options.html#cli-configure-options-cli-auto-prompt)[--no-cli-auto-prompt](./cli-configure-options.html#cli-configure-options-no-cli-auto-prompt)For information on the AWS CLI version 2 auto-prompt feature, see [Enabling and using command prompts in the AWS CLI](./cli-usage-parameters-prompting.html).
- 
                            
- `AWS_CLI_FILE_ENCODING`
- 
                    Specifies the encoding used for text files. By default encoding matches your locale. To set encoding different from the locale, use the `aws_cli_file_encoding`environment variable. For example, if you use Windows with default encoding`CP1252`, setting`aws_cli_file_encoding=UTF-8`sets the CLI to open text files using`UTF-8`.
- `AWS_CLI_HISTORY_FILE`
- 
                    Overrides the default location for storing command history when the `cli_history`feature is enabled. The default path is`~/.aws/cli/history/history.db`. You can use this variable to specify an alternative storage location.
- `AWS_CLI_S3_MV_VALIDATE_SAME_S3_PATHS`
- 
                    If the source and destination buckets are the same when using the `s3 mv`command, the source file or object can be moved onto itself, which can result in accidental deletion of your source file or object. The`AWS_CLI_S3_MV_VALIDATE_SAME_S3_PATHS`environment variable and`--validate-same-s3-paths`option specifies whether to validate your access point ARNs or access point aliases in your Amazon S3 source or destination URIs.###### NotePath validation for `s3 mv`requires additional API calls.
- `AWS_S3_DISABLE_EXPRESS_SESSION_AUTH`
- 
                    Whether to disable S3 Express session authentication. The value must be a boolean. Defaults to false. If set to true, the client will NOT use S3 Express session authentication. If defined, this environment variable overrides the value for the profile S3 setting `disable_s3_express_session_auth`.
- `AWS_CONFIG_FILE`
- 
                    Specifies the location of the file that the AWS CLI uses to store configuration profiles. The default path is `~/.aws/config`.You can't specify this value in a named profile setting or by using a command line parameter. 
- `AWS_DATA_PATH`
- 
                    A list of additional directories to check outside of the built-in search path of `~/.aws/models`when loading AWS CLI data. Setting this environment variable indicates additional directories to check first before falling back to the built-in search path. Multiple entries should be separated with the`os.pathsep`character, which is`:`on Linux or macOS and`;`on Windows.
- `AWS_DEFAULT_OUTPUT`
- 
                    Specifies the [output format](./cli-usage-output.html)to use.If defined, this environment variable overrides the value for the profile setting `output`. You can override this environment variable by using the`--output`command line parameter.
- `AWS_DEFAULT_REGION`
- 
                    The `Default region name`identifies the AWS Region whose servers you want to send your requests to by default. This is typically the Region closest to you, but it can be any Region. For example, you can type`us-west-2`to use US West (Oregon). This is the Region that all later requests are sent to, unless you specify otherwise in an individual command.###### NoteYou must specify an AWS Region when using the AWS CLI, either explicitly or by setting a default Region. For a list of the available Regions, see [Regions and Endpoints](https://docs.aws.amazon.com/general/latest/gr/rande.html). The Region designators used by the AWS CLI are the same names that you see in AWS Management Console URLs and service endpoints.If defined, this environment variable overrides the value for the profile setting `region`. You can override this environment variable by using the`--region`command line parameter and the AWS SDK compatible`AWS_REGION`environment variable.
- `AWS_EC2_METADATA_DISABLED`
- 
                    Disables the use of the Amazon EC2 instance metadata service (IMDS). If set to true, user credentials or configuration (like the Region) are not requested from IMDS. 
- `AWS_ENDPOINT_URL`
- 
                    Specifies the endpoint that is used for all service requests. For more information, see [Set global endpoint for all AWS services](./cli-configure-endpoints.html#endpoints-global).###### Endpoint precedenceEndpoint configuration settings are located in multiple places, such as the system or user environment variables, local AWS configuration files, or explicitly declared on the command line as a parameter. The AWS CLI checks these endpoint settings in a particular order, and uses the endpoint setting with the highest precedence. For the endpoint precedence list, see [Endpoint configuration and settings precedence](./cli-configure-endpoints.html#endpoints-precedence).
- `AWS_ENDPOINT_URL_<SERVICE>`
- 
                    Specifies a custom endpoint that is used for a specific service, where `<SERVICE>`is replaced with the AWS service identifier. For example, Amazon DynamoDB has a`serviceId`of`DynamoDB``AWS_ENDPOINT_URL_DYNAMODB`.For a list of all service-specific environment variables, see [List of service-specific identifiers](./cli-configure-endpoints.html#endpoints-service-specific-table).###### Endpoint precedenceEndpoint configuration settings are located in multiple places, such as the system or user environment variables, local AWS configuration files, or explicitly declared on the command line as a parameter. The AWS CLI checks these endpoint settings in a particular order, and uses the endpoint setting with the highest precedence. For the endpoint precedence list, see [Endpoint configuration and settings precedence](./cli-configure-endpoints.html#endpoints-precedence).
- `AWS_IGNORE_CONFIGURED_ENDPOINT_URLS`
- 
                    If enabled, the AWS CLI ignores all custom endpoint configurations. Valid values are **true****false**[Set global endpoint for all AWS services](./cli-configure-endpoints.html#endpoints-global).Endpoint configuration settings are located in multiple places, such as the system or user environment variables, local AWS configuration files, or explicitly declared on the command line as a parameter. For endpoint precedence, see [Endpoint configuration and settings precedence](./cli-configure-endpoints.html#endpoints-precedence).###### Endpoint precedenceEndpoint configuration settings are located in multiple places, such as the system or user environment variables, local AWS configuration files, or explicitly declared on the command line as a parameter. The AWS CLI checks these endpoint settings in a particular order, and uses the endpoint setting with the highest precedence. For the endpoint precedence list, see [Endpoint configuration and settings precedence](./cli-configure-endpoints.html#endpoints-precedence).
- [AWS_MAX_ATTEMPTS](./cli-configure-files.html#cli-config-max_attempts)
- 
                    Specifies a value of maximum retry attempts the AWS CLI retry handler uses, where the initial call counts toward the value that you provide. For more information on retries, see [AWS CLI retries in the AWS CLI](./cli-configure-retries.html).If defined, this environment variable overrides the value for the profiles setting `max_attempts`.
- `AWS_METADATA_SERVICE_NUM_ATTEMPTS`
- 
                    When attempting to retrieve credentials on an Amazon EC2 instance that has been configured with an IAM role, the AWS CLI attempts to retrieve credentials once from the instance metadata service before stopping. If you know your commands will run on an Amazon EC2 instance, you can increase this value to make AWS CLI retry multiple times before giving up. 
- `AWS_METADATA_SERVICE_TIMEOUT`
- 
                    The number of seconds before a connection to the instance metadata service should time out. When attempting to retrieve credentials on an Amazon EC2 instance that is configured with an IAM role, a connection to the instance metadata service times out after 1 second by default. If you know you're running on an Amazon EC2 instance with an IAM role configured, you can increase this value if needed. 
- [AWS_PAGER](./cli-configure-files.html#cli-config-cli_pager)
- 
                    Specifies the pager program used for output. By default, AWS CLI version 2 returns all output through your operating system’s default pager program. To disable all use of an external paging program, set the variable to an empty string. If defined, this environment variable overrides the value for the profile setting `cli_pager`.
- [AWS_PROFILE](./cli-configure-files.html#cli-configure-files-using-profiles)
- 
                    Specifies the name of the AWS CLI profile with the credentials and options to use. This can be the name of a profile stored in a `credentials`or`config`file, or the value`default`to use the default profile.If defined, this environment variable overrides the behavior of using the profile named `[default]`in the configuration file. You can override this environment variable by using the`--profile`command line parameter.
- `AWS_REGION`
- 
                    The AWS SDK compatible environment variable that specifies the AWS Region to send the request to. If defined, this environment variable overrides the values in the environment variable `AWS_DEFAULT_REGION`and the profile setting`region`. You can override this environment variable by using the`--region`command line parameter.
- `AWS_REQUEST_CHECKSUM_CALCULATION`
- 
                    Specifies when a checksum is calculated for request payloads, and has the following options: - 
                            `when_supported`–**(Default)**The request payload checksum is calculated when an operation either specifies a checksum algorithm in its service model or requires request checksums.
- 
                            `when_required`– The request payload checksum is calculated when an operation requires request checksums or when a user provides a`requestAlgorithmMember`that is modeled by the AWS service.
 If defined, this environment variable overrides the value for the profiles setting [request_checksum_calculation](./cli-configure-files.html#cli-config-request_checksum_calculation).
- 
                            
- `AWS_RESPONSE_CHECKSUM_VALIDATION`
- 
                    Specifies when checksum validation is performed for response payloads, and has the following options: - 
                            `when_supported`–**(Default)**The response payload checksum validation is performed when an operation specifies a response algorithm in its service model that the AWS CLI supports.
- 
                            `when_required`– The response payload checksum validation is performed when an operation specifies a response algorithm in its service model that the AWS CLI supports, and you set the modeled`requestValidationModeMember`to`ENABLED`in the operation input.
 If defined, this environment variable overrides the value for the profiles setting [response_checksum_validation](./cli-configure-files.html#cli-config-response_checksum_validation).
- 
                            
- [AWS_RETRY_MODE](./cli-configure-files.html#cli-config-retry_mode)
- 
                    Specifies which retry mode AWS CLI uses. There are three retry modes available: legacy (default), standard, and adaptive. For more information on retries, see [AWS CLI retries in the AWS CLI](./cli-configure-retries.html).If defined, this environment variable overrides the value for the profiles setting `retry_mode`.
- `AWS_ROLE_ARN`
- 
                    Specifies the Amazon Resource Name (ARN) of an IAM role with a web identity provider that you want to use to run the AWS CLI commands. Used with the `AWS_WEB_IDENTITY_TOKEN_FILE`and`AWS_ROLE_SESSION_NAME`environment variables.If defined, this environment variable overrides the value for the profile setting [role_arn](./cli-configure-files.html#cli-config-role_arn). You can't specify a role session name as a command line parameter.###### NoteThis environment variable only applies to an assumed role with web identity provider it does not apply to the general assume role provider configuration. For more information on using web identities, see [Assume role with web identity](./cli-configure-role.html#cli-configure-role-oidc).
- `AWS_ROLE_SESSION_NAME`
- 
                    Specifies the name to attach to the role session. This value is provided to the `RoleSessionName`parameter when the AWS CLI calls the`AssumeRole`operation, and becomes part of the assumed role user ARN:`arn:aws:sts::`. This is an optional parameter. If you do not provide this value, a session name is generated automatically. This name appears in AWS CloudTrail logs for entries associated with this session.`123456789012`:assumed-role/`role_name`/`role_session_name`If defined, this environment variable overrides the value for the profile setting [role_session_name](./cli-configure-files.html#cli-config-role_session_name).Used with the `AWS_ROLE_ARN`and`AWS_WEB_IDENTITY_TOKEN_FILE`environment variables.For more information on using web identities, see [Assume role with web identity](./cli-configure-role.html#cli-configure-role-oidc).###### NoteThis environment variable only applies to an assumed role with web identity provider it does not apply to the general assume role provider configuration. 
- `AWS_SDK_UA_APP_ID`
- 
                    A single AWS account can be used by multiple customer applications to make calls to AWS services. Application ID identifies which source application made a set of calls using an AWS service. AWS SDKs and services don't use or interpret this value other than to surface it back in customer communications. For example, this value can be included in operational emails to uniquely identify which of your applications is associated with the notification. By default, there is no value. The Application ID is a string with maximum length of 50 characters. Letters, numbers and the following special characters are allowed: `! $ % & * + - . , ^ _ ` | ~`If defined, this environment variable overrides the value for the profile setting [sdk_ua_app_id](./cli-configure-files.html#cli-config-sdk_ua_app_id). You can't specify Application ID as a command line option.
- `AWS_SECRET_ACCESS_KEY`
- 
                    Specifies the secret key associated with the access key. This is essentially the "password" for the access key. If defined, this environment variable overrides the value for the profile setting `aws_secret_access_key`. You can't specify the secret access key ID as a command line option.
- `AWS_SESSION_TOKEN`
- 
                    Specifies the session token value that is required if you are using temporary security credentials that you retrieved directly from AWS STS operations. For more information, see the [Output section of the assume-role command](https://docs.aws.amazon.com/cli/latest/reference/sts/assume-role.html#output)in the*AWS CLI Command Reference*.If defined, this environment variable overrides the value for the profile setting `aws_session_token`.
- `AWS_SHARED_CREDENTIALS_FILE`
- 
                    Specifies the location of the file that the AWS CLI uses to store access keys. The default path is `~/.aws/credentials`.You can't specify this value in a named profile setting or by using a command line parameter. 
- `AWS_SIGV4A_SIGNING_REGION_SET`
- 
                    Specifies the regions to use when signing with SigV4a using a comma-delimited list. If this variable is not set, the AWS CLI uses the default used by the AWS service. If the AWS service has no default, the request signature becomes valid in all regions using a value of `*`.For more information on SigV4a, see [AWS Signature Version 4 for API requests](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_sigv.html)in the*IAM User Guide*If defined, this environment variable overrides the value for the profile setting [sigv4a_signing_region_set](./cli-configure-files.html#cli-config-sigv4a_signing_region_set).
- `AWS_USE_DUALSTACK_ENDPOINT`
- 
                    Enables the use of dual-stack endpoints to send AWS requests. To learn more about dual-stack endpoints, which support both IPv4 and IPv6 traffic, see [Using Amazon S3 dual-stack endpoints](https://docs.aws.amazon.com/AmazonS3/latest/userguide/dual-stack-endpoints.html)in the*Amazon Simple Storage Service User Guide*. Dual-stack endpoints are available for some services in some regions. If a dual-stack endpoint does not exist for the service or AWS Region, the request fails. This is disabled by default. For more information, see[Set to use dual-stack endpoints for all AWS services](./cli-configure-endpoints.html#endpoints-dual-stack).###### Endpoint precedenceEndpoint configuration settings are located in multiple places, such as the system or user environment variables, local AWS configuration files, or explicitly declared on the command line as a parameter. The AWS CLI checks these endpoint settings in a particular order, and uses the endpoint setting with the highest precedence. For the endpoint precedence list, see [Endpoint configuration and settings precedence](./cli-configure-endpoints.html#endpoints-precedence).
- `AWS_USE_FIPS_ENDPOINT`
- 
                    Some AWS services offer endpoints that support [Federal Information Processing Standard (FIPS) 140-2](http://aws.amazon.com/compliance/fips/)in some AWS Regions. When the AWS service supports FIPS, this setting specifies what FIPS endpoint the AWS CLI should use . Unlike standard AWS endpoints, FIPS endpoints use a TLS software library that complies with FIPS 140-2. These endpoints might be required by enterprises that interact with the United States government. For more information see,[Set to use FIPs endpoints for all AWS services](./cli-configure-endpoints.html#endpoints-fips).If this setting is enabled, but a FIPS endpoint does not exist for the service in your AWS Region, the AWS command may fail. In this case, manually specify the endpoint to use in the command using the [--endpoint-url](./cli-configure-options.html#cli-configure-options-endpoint-url)[service-specific endpoints](./cli-configure-endpoints.html#endpoints-service-specific).###### Endpoint precedenceEndpoint configuration settings are located in multiple places, such as the system or user environment variables, local AWS configuration files, or explicitly declared on the command line as a parameter. The AWS CLI checks these endpoint settings in a particular order, and uses the endpoint setting with the highest precedence. For the endpoint precedence list, see [Endpoint configuration and settings precedence](./cli-configure-endpoints.html#endpoints-precedence).
- [AWS_WEB_IDENTITY_TOKEN_FILE](./cli-configure-envvars.html)
- 
                    Specifies the path to a file that contains an OAuth 2.0 access token or OpenID Connect ID token that is provided by an identity provider. The AWS CLI loads the contents of this file and passes it as the `WebIdentityToken`argument to the`AssumeRoleWithWebIdentity`operation.Used with the `AWS_ROLE_ARN`and`AWS_ROLE_SESSION_NAME`environment variables.If defined, this environment variable overrides the value for the profile setting `web_identity_token_file`.For more information on using web identities, see [Assume role with web identity](./cli-configure-role.html#cli-configure-role-oidc).###### NoteThis environment variable only applies to an assumed role with web identity provider it does not apply to the general assume role provider configuration.