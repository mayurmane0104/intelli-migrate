# Using upgrade debug mode to upgrade AWS CLI version 1 to AWS CLI version 2 - AWS Command Line Interface

**Source:** [https://docs.aws.amazon.com/cli/latest/userguide/cli-upgrade-debug-mode.html](https://docs.aws.amazon.com/cli/latest/userguide/cli-upgrade-debug-mode.html)

---

This topic describes the upgrade debug mode in AWS CLI version 1.

We recommend that users of AWS CLI version 1 upgrade to AWS CLI version 2 to access new features and enhanced performance. There are changes in behavior between AWS CLI version 1 and AWS CLI version 2 that might require you to update your scripts or commands to get the same behavior. The upgrade debug mode in AWS CLI version 1 outputs warnings when you use features that have different behavior in AWS CLI version 2. This feature improves the upgrade experience by automatically detecting which of your AWS CLI version 1 commands need to be modified before upgrading to AWS CLI version 2 to prevent unexpected issues.

For more details, see [Breaking changes between AWS CLI version 1 and AWS CLI version 2](./cliv2-migration-changes.html#cliv2-migration-changes-breaking) 
    in [New features and changes in the AWS CLI version 2](./cliv2-migration-changes.html).

## Prerequisites

    The upgrade debug mode feature was introduced to the AWS CLI in version `1.44.0`.

Using AWS CLI version 1, run `aws --version`, and verify that the AWS CLI version is `1.44.0` or higher.

If the version is less than `1.44.0`, see 
    [Installing, updating, and uninstalling the AWS CLI](https://docs.aws.amazon.com/cli/v1/userguide/cli-chap-install.html).

## How it works

    If enabled, the upgrade debug mode detects usage of features that were updated with breaking changes in AWS CLI version 2. 
      If you use a command or feature listed in our [Breaking changes between AWS CLI version 1 and AWS CLI version 2](./cliv2-migration-changes.html#cliv2-migration-changes-breaking) 
      after upgrading to AWS CLI version 2, a warning will be shown in the output. Breaking change detection is based on the command used, the arguments 
      supplied, the execution environment (e.g. environment variables, configuration settings, etc.), and for a few cases, the content or configuration of 
      resources in the AWS account being used.

The warnings describe actions to prevent unexpected issues of upgrading to AWS CLI version 2. After making the changes recommended by a warning message, you can confirm the command has been updated successfully by re-running the command to verify the warning is no longer shown. Warnings being resolved signals that the command is no longer likely to experience the breaking change described upon upgrading to AWS CLI version 2.

The following example demonstrates what these warnings look like. This command demonstrates an example warning. All warning text starts with 
      "AWS CLI V2 UPGRADE WARNING," followed by the specific warning message. In this case, a warning is output because the command relies on the AWS 
      CLI to retrieve the contents of the URL and use the contents as the `--template-body` parameter value, which was a feature removed in AWS 
      CLI version 2.

```
$ aws cloudformation create-stack \
  --stack-name "stack012345" \
  --template-body "https://s3.amazonaws.com/amzn-s3-demo-bucket/template.json"
AWS CLI v2 UPGRADE WARNING: For input parameters that have a prefix of http:// or 
https://, AWS CLI v2 will not automatically request the content of the URL for 
the parameter, and the `cli_follow_urlparam` option has been removed. See 
https://docs.aws.amazon.com/cli/latest/userguide/cliv2-migration-changes.html#cliv2-migration-paramfile.
```
The following table of all breaking changes, and how to avoid facing a breaking change in AWS CLI version 2. Remediation actions that resolve the warnings in debug mode are in bold.

| Breaking change | On v1, migrate to v2 behavior | On v2, retain v1 behavior | 
|---|---|---|
| [Environment variable added to set text file encoding](./cliv2-migration-changes.html#cliv2-migration-encodingenvvar) | Unset the `PYTHONUTF8`and`PYTHONIOENCODING`environment variables. | Set the `AWS_CLI_FILE_ENCODING`environment
                variable to the encoding specified in v1. | 
| [Binary parameters are passed as base64-encoded strings by default](./cliv2-migration-changes.html#cliv2-migration-binaryparam) | Encode the value of the parameter with base64. If the parameter is being loaded from a file, encode the file contents with base64. | Set the `cli_binary_format`setting to`raw-in-base64-out`. | 
| [Improved Amazon S3 handling of file properties and tags for multipart copies](./cliv2-migration-changes.html#cliv2-migration-s3-copy-metadata) | N/A. Cannot migrate to version 2 behavior in version 1. | Use the `--copy-props none`parameter. | 
| [No automatic retrieval of http:// or https:// URLs for parameters](./cliv2-migration-changes.html#cliv2-migration-paramfile) | Use curl (or alternative tools) to download the contents of the URLs to a local file. 
                Then, load the file contents to the parameter with [file://](https://docs.aws.amazon.com/cli/v1/userguide/cli-usage-parameters-file.html). 
                Alternatively, configure`cli_follow_urlparam`to false to specify the raw URL as the paramater value. | N/A. Impossible to retain version 1 behavior in version 2. | 
| [Pager used for all output by default](./cliv2-migration-changes.html#cliv2-migration-output-pager) | N/A. Cannot migrate to version 2 behavior in version 1. | Set the `cli_pager`setting or`AWS_PAGER`variable to an empty string. | 
| [Timestamp output values are standardized to ISO 8601 format](./cliv2-migration-changes.html#cliv2-migration-timestamp) | Set the `cli_timestamp`_format setting to`iso8601`. | Set the `cli_timestamp_format`setting to wire. | 
| [Improved handling of CloudFormation deployments that result in no changes](./cliv2-migration-changes.html#cliv2-migration-cfn) | Use the `--no-fail-on-empty-changeset`parameter. | Use the `--fail-on-empty-changeset`parameter. | 
| [Changed default behavior for Regional Amazon S3 endpoint for us-east-1 Region](./cliv2-migration-changes.html#cliv2-migration-s3-regional-endpoint) | Set the `AWS_ENDPOINT_URL_S3`environment variable or the`--endpoint-url`command line option to the us-east-1[regional URL](https://docs.aws.amazon.com/general/latest/gr/s3.html#s3_region). | Use the `--region aws-global`command line option. | 
| [ecr get-login removed and replaced with ecr get-login-password](./cliv2-migration-changes.html#cliv2-migration-ecr-get-login) | (1.17.10 or later) Use [ecr get-login removed and replaced with ecr get-login-password](./cliv2-migration-changes.html#cliv2-migration-ecr-get-login)and pipe the output into a docker command. | N/A. Impossible to retain version 1 behavior in version 2. | 
| [AWS CLI version 2 support for plugins is changing](./cliv2-migration-changes.html#cliv2-migration-profile-plugins) | N/A. Cannot migrate to version 2 behavior in version 1. | Configure the [cli_legacy_plugin_path](https://docs.aws.amazon.com/cli/latest/topic/config-vars.html#plugins)to the`[plugins]`section of the configuration file. Test plugins in version 2, lock your version 2 version, and test your plugins each time you upgrade. | 
| [Hidden alias support removed](./cliv2-migration-changes.html#cliv2-migration-aliases) | Switch from using the obsolete hidden alias to [Hidden alias support removed](./cliv2-migration-changes.html#cliv2-migration-aliases)that works in all versions. | N/A. Impossible to retain version 1 behavior in version 2. | 
| [The api_versions configuration file setting is not supported](./cliv2-migration-changes.html#cliv2-migration-api-versions) | Migrate and test your usage of older API versions to the latest API version, 
                and remove [api_versions](https://docs.aws.amazon.com/cli/v1/userguide/cli-configure-files.html#cli-config-api_versions)from your configuration settings. | N/A. Impossible to retain version 1 behavior in version 2. | 
| [AWS CLI version 2 uses only Signature v4 to authenticate Amazon S3 requests](./cliv2-migration-changes.html#cliv2-migration-sigv4) | Specify the Signature Version to version 4 (see [Specifying the Signature Version 
                  in request authentication)](https://docs.aws.amazon.com/AmazonS3/latest/API/specify-signature-version.html). | N/A. Impossible to retain version 1 behavior in version 2. | 
| [AWS CLI version 2 is more consistent with paging parameters](./cliv2-migration-changes.html#cliv2-migration-skeleton-paging) | Move the pagination parameters in the input JSON parameter to the command itself. | Remove the pagination parameters from the input JSON parameter. | 
| [AWS CLI version 2 provides more consistent return codes across all commands](./cliv2-migration-changes.html#cliv2-migration-return-codes) | N/A. Cannot migrate to version 2 behavior in version 1. | N/A. Impossible to retain version 1 behavior in version 2. | 
| [AWS CLI version 2 uses CRC64NVME checksums by default for high-level Amazon S3 uploads](./cliv2-migration-changes.html#cliv2-migration-checksums) | (1.37.0 or later) Use `--checksum-algorithm CRC64NVME`command line option. (CRT required). | (2.23.0 or later) Use `--checksum-algorithm CRC32`command line option. | 

## Limitations

    We strongly recommend customers review our [Breaking changes between AWS CLI version 1 and AWS CLI version 2](./cliv2-migration-changes.html#cliv2-migration-changes-breaking).

### Unsupported Breaking Change Detection

The upgrade debug mode feature supports every breaking change except that [AWS CLI version 2 provides more consistent return codes across all commands](./cliv2-migration-changes.html#cliv2-migration-return-codes). 
        This mode cannot account for how you use the error codes returned by the AWS CLI downstream.

### Conditional Breaking Change Detection

Detection of [Timestamp output values are standardized to ISO 8601 format](./cliv2-migration-changes.html#cliv2-migration-timestamp) is the only case where detection depends on the state of the AWS account, and may be subject 
        to breaking changes if the account resources are updated later. If no timestamps are included in the API response from the service, no detections will be made for this breaking change.

If you rely on the timestamp format returned by AWS CLI commands and have not already configured the AWS CLI to use ISO 8601, take extra precaution to ensure your processing of the timestamp will not break after upgrading to version 2.

### Unresolvable Breaking Change Detection

Some warnings output by upgrade debug mode cannot be resolved by modifying the command or environment. The following cases are cases where warnings would always be output by upgrade debug mode as long as you use the corresponding feature:

- 
          [AWS CLI version 2 support for plugins is changing](./cliv2-migration-changes.html#cliv2-migration-profile-plugins)- if you rely on plugins in your[configuration file](https://docs.aws.amazon.com/cli/v1/userguide/cli-configure-files.html), the upgrade debug mode will always output a warning that cannot be resolved. This mode cannot guarantee whether any of your plugins will work in AWS CLI version 2.
- 
          [Improved Amazon S3 handling of file properties and tags for multipart copies](./cliv2-migration-changes.html#cliv2-migration-s3-copy-metadata)- if`aws s3`is used to perform a bucket-to-bucket Amazon Amazon S3 copy, the upgrade debug mode will always output a warning that cannot be resolved.

### False detections

Warnings output by the upgrade debug mode do not guarantee that breaking changes will be faced after upgrading to AWS CLI v2. Below are cases where warnings would be output by upgrade debug mode, despite there being no breaking change introduced in AWS CLI v2:

- 
          [Environment variable added to set text file encoding](./cliv2-migration-changes.html#cliv2-migration-encodingenvvar)- if the`PYTHONUTF8`or`PYTHONIOENCODING`environment variables are specified to set the text file encoding, and the specified encoding already matches the installed locale, the warning might be a false detection since debug mode does not check if the encoding matches the installed locale.
- 
          [Improved Amazon S3 handling of file properties and tags for multipart copies](./cliv2-migration-changes.html#cliv2-migration-s3-copy-metadata)- if`aws s3`is used to perform a bucket-to-bucket Amazon Amazon S3 copy, and the copy is not multipart due to the source object being under the[multipart threshold size](https://docs.aws.amazon.com/cli/latest/topic/s3-config.html#multipart-threshold), a false detection will be output.
- 
          [Timestamp output values are standardized to ISO 8601 format](./cliv2-migration-changes.html#cliv2-migration-timestamp)- if the cli_timestamp_format configuration setting is set to wire (default), and a timestamp in ISO 8601 format is returned by the service.
- 
          [Improved handling of CloudFormation deployments that result in no changes](./cliv2-migration-changes.html#cliv2-migration-cfn)- if the`--fail-on-empty-changeset`flag is used with the`aws cloudformation deploy`command, and the resulting changeset is empty, a false detection will be output. Also, if the changeset is non-empty, and`--no-fail-on-empty-changeset`is not used, a false detection will be output.
- 
          [Changed default behavior for Regional Amazon S3 endpoint for us-east-1 Region](./cliv2-migration-changes.html#cliv2-migration-s3-regional-endpoint)- if`aws s3`or`aws s3api`is used to perform an Amazon Amazon S3 operation, and the region is configured to`us-east-1`, and the`s3.us_east_1_regional_endpoint`configuration is not configured to regional, and the global Amazon S3 endpoint is used for the request due to the[endpoint configuration settings](https://docs.aws.amazon.com/cli/v1/userguide/cli-configure-endpoints.html#endpoints-precedence), then the warning might be a false detection, since debug mode does not check configured endpoint settings.

## Configure upgrade debug mode

    
    You can enable or disable upgrade debug mode using the following methods, listed in order of precedence:

- 
        Command line options enable or disable upgrade debug mode for a single command. Use [--v2-debug](https://docs.aws.amazon.com/cli//latest/userguide/cli-configure-options.html#cli-configure-options-v2-debug)to use upgrade debug mode.
- 
        Environment variables use the [AWS_CLI_UPGRADE_DEBUG_MODE](https://docs.aws.amazon.com/cli//latest/userguide/cli-configure-envvars.html#envvars-list-aws_cli_upgrade_debug_mode)variable.