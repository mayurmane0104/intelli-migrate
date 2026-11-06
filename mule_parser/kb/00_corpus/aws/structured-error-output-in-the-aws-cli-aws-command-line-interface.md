# Structured error output in the AWS CLI - AWS Command Line Interface

**Source:** [https://docs.aws.amazon.com/cli/latest/userguide/cli-usage-error-format.html](https://docs.aws.amazon.com/cli/latest/userguide/cli-usage-error-format.html)

---

This topic describes the structured error output formats for the AWS Command Line Interface (AWS CLI). The CLI writes errors to stderr and supports the following formats:

- 
            [enhanced](#cli-error-format-enhanced)
- 
            [json](#cli-error-format-json)[JSON](https://json.org/)string with all error fields. Use for automation and scripting.
- 
            [yaml](#cli-error-format-yaml)[YAML](https://yaml.org/)string with all error fields. Use for automation and scripting.
- 
            [text](#cli-error-format-text)
- 
            [table](#cli-error-format-table)
- 
            [legacy](#cli-error-format-legacy)

## Configuring error format

        You can configure the error format using any of the following methods:

- Command-line flag
- 
                    `$``aws``<command>`--cli-error-format json
- Configuration file (`~/.aws/config`)
- 
                    `[default] cli_error_format = json`
- Environment variable
- 
                    `$``export AWS_CLI_ERROR_FORMAT=yaml`

## Error output formats

        The following sections describe each format:

### Enhanced format (default)

The enhanced format displays error messages with additional details inline for simple values. For complex structures, the format provides a hint to use JSON or YAML.

**Example: Missing region configuration**

`aws: [ERROR]: An error occurred (NoRegion): You must specify a region. You can also configure your region by running "aws configure".`**Example: Nonexistent Lambda function with additional fields**

```
aws: [ERROR]: An error occurred (ResourceNotFoundException) when calling the GetFunction operation: Function not found: arn:aws:lambda:us-west-2:123456789012:function:nonexistent-function-12345
Additional error details:
Type: User
```
The "Additional error details" section displays only fields that are defined in the service's error shape model. Unmodeled fields from the error response are not shown.

**Example: Complex error fields**

```
An error occurred (TransactionCanceledException) when calling the TransactWriteItems operation: Transaction cancelled, please refer cancellation reasons for specific reasons [ConditionalCheckFailed, None]
Additional error details:
CancellationReasons: <complex value>
Use "--cli-error-format json" or another error format to see the full details.
```
### JSON format

The JSON format provides a structured representation with all error fields.

**Example: Missing region configuration**

```
{
    "Code": "NoRegion",
    "Message": "You must specify a region. You can also configure your region by running \"aws configure\"."
}
```
**Example: Nonexistent Lambda function**

```
{
    "Code": "ResourceNotFoundException",
    "Message": "Function not found: arn:aws:lambda:us-west-2:123456789012:function:nonexistent-function-12345",
    "Type": "User"
}
```
### YAML format

The YAML format provides a structured representation with all error fields.

**Example: Missing region configuration**

```
Code: NoRegion
Message: You must specify a region. You can also configure your region by running "aws configure".
```
**Example: Nonexistent Lambda function**

```
Code: ResourceNotFoundException
Message: "Function not found: arn:aws:lambda:us-west-2:123456789012:function:nonexistent-function-12345"
Type: User
```
### Text format

The text format uses the same formatter as successful command output.

**Example: Nonexistent Lambda function**

`ResourceNotFoundException    Function not found: arn:aws:lambda:us-west-2:123456789012:function:nonexistent-function-12345    User`### Table format

The table format uses the same formatter as successful command output.

**Example: Nonexistent Lambda function**

```
------------------------------------------------------------------------------------------------------------------------------------|
|                                                              error                                                                 |
+----------------------------+--------------------------------------------------------------------------------------------------+------+
|            Code            |                              Message                                                             | Type |
+----------------------------+--------------------------------------------------------------------------------------------------+------+
|  ResourceNotFoundException |  Function not found: arn:aws:lambda:us-west-2:123456789012:function:nonexistent-function-12345   | User |
+----------------------------+--------------------------------------------------------------------------------------------------+------+
```
### Legacy format

The legacy format provides the original error format without structured details. This format does not include the "An error occurred (ErrorCode):" prefix for CLI exceptions.

**Example: Missing region configuration**

`aws: [ERROR]: You must specify a region. You can also configure your region by running "aws configure".`**Example: Nonexistent Lambda function**

`An error occurred (ResourceNotFoundException) when calling the GetFunction operation: Function not found: arn:aws:lambda:us-west-2:123456789012:function:nonexistent-function-12345`###### Note

Errors now consistently include the `aws: [ERROR]:` prefix for 
                    CLI exceptions. Earlier versions did not always include this prefix.

The following exceptions always use the legacy format regardless of the configured error format:

- 
                        `UnknownArgumentError`– Displays usage information
- 
                        Keyboard interrupts ( `KeyboardInterrupt`)

## Complete example

        The following example shows a command with JSON error formatting:

`$``aws lambda get-function \ --function-name nonexistent-function-12345 \ --cli-error-format json`

Output (stderr):

```
{
    "Code": "ResourceNotFoundException",
    "Message": "Function not found: arn:aws:lambda:us-west-2:123456789012:function:nonexistent-function-12345",
    "Type": "User"
}
```
The `Type` field is a modeled error member defined in the Lambda service's error shape. 
            Only fields defined in the service's error model are included in the structured error output.