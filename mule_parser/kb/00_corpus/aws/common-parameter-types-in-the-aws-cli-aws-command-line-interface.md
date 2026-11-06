# Common parameter types in the AWS CLI - AWS Command Line Interface

**Source:** [https://docs.aws.amazon.com/cli/latest/userguide/cli-usage-parameters-types.html](https://docs.aws.amazon.com/cli/latest/userguide/cli-usage-parameters-types.html)

---

This section describes some of the common parameter types and the typical required format.

If you are having trouble formatting a parameter for a specific command, check the help by
        entering `help` after the command name.  The help for each subcommand
        includes an option's name and description. The option's parameter type is listed in
        parentheses. For more information on viewing help, see [Accessing help and resources for the AWS CLI](./cli-usage-help.html).

###### Parameter types include:

## String

        String parameters can contain alphanumeric characters, symbols, and white spaces from
            the [ASCII](https://wikipedia.org/wiki/ASCII) character set. Strings
            that contain white spaces must be surrounded by quotation marks. We recommend that you
            don't use symbols or white spaces other than the standard space character and to observe
            your terminal's 

[quoting rules](./cli-usage-parameters-quoting-strings.html)to prevent unexpected results.

Some string parameters can accept binary data from a file. See [Binary files](./cli-usage-parameters-file.html#cli-usage-parameters-file-binary) for an example. 

## Timestamp

        Timestamps are formatted according to the [ISO 8601](https://www.iso.org/iso-8601-date-and-time-format.html)
            standard. These are often referred to as "

`DateTime`" or "`Date`"
            parameters. `$``aws ec2 describe-spot-price-history``--start-time 2014-10-13T19:00:00Z`

Acceptable formats include:

- 
                `YYYY`-`MM`-`DD`T`hh`:`mm`:`ss.sss``TZD (UTC)`, for example, 2014-10-01T20:30:00.000Z
- 
                `YYYY`-`MM`-`DD`T`hh`:`mm`:`ss.sss``TZD (with offset)`, for example, 2014-10-01T12:30:00.000-08:00
- 
                `YYYY`-`MM`-`DD`, for example, 2014-10-01
- 
                Unix time in seconds, for example, 1412195400. This is sometimes referred to as [Unix Epoch time](https://wikipedia.org/wiki/Unix_time)and represents the number of seconds since midnight, January 1, 1970 UTC.

By
            default, the AWS CLI version 2 translates all ** response** DateTime values to ISO 8601 format.

You can set the timestamp format by using the [cli_timestamp_format](./cli-configure-files.html#cli-config-cli_timestamp_format)

## List

        One or more strings separated by spaces. If any of the string items contain a space,
            you must put quotation marks around that item. Observe your terminal's [quoting rules](./cli-usage-parameters-quoting-strings.html) to prevent
            unexpected results.

`$``aws ec2 describe-spot-price-history``--instance-types m1.xlarge m1.medium`

## Boolean

        Binary flag that turns an option on or off. For example, ```
ec2
                describe-spot-price-history
```
 has a Boolean `--dry-run` parameter
            that, when specified, validates the query with the service without actually running the
            query. 

`$``aws ec2 describe-spot-price-history``--dry-run`

The output indicates whether the command was well formed. This command also includes a
                `--no-dry-run` version of the parameter that you can use to explicitly
            indicate that the command should be run normally. Including it isn't necessary because
            this is the default behavior. 

## Integer

        An unsigned, whole number.

`$``aws ec2 describe-spot-price-history``--max-items 5`

## Binary / blob (binary large object) and streaming blob

        In the AWS CLI, you can pass a binary value as a string directly on the command line. There are two types of blobs:

### Blob

To pass a value to a parameter with type `blob`, you must specify a
                path to a local file that contains the binary data using the `fileb://`
                prefix. Files referenced using the `fileb://` prefix are always treated
                as raw unencoded binary. The specified path is interpreted as being relative to the
                current working directory. For example, the `--plaintext` parameter for
                    `aws kms encrypt` is a blob.

`$``aws kms encrypt \ --key-id 1234abcd-12ab-34cd-56ef-1234567890ab \``--plaintext fileb://ExamplePlaintextFile`\ --output text \ --query CiphertextBlob | base64 \ --decode > ExampleEncryptedFile

###### Note

For backwards compatibility, you can use the `file://` prefix.
                    There are two formats used based on the file setting [cli_binary_format](./cli-configure-files.html#cli-config-cli_binary_format)[--cli-binary-format](./cli-configure-options.html#cli-configure-options-cli-binary-format)

- 
                        Default for the AWS CLI version 2. If the setting's value is `base64`, files referenced using the`file://`prefix are treated as base64-encoded text.
- 
                        Default for the AWS CLI version 1. If the setting's value is `raw-in-base64-out`, files referenced using the`file://`prefix is read as text and then the AWS CLI attempts to encode it to binary.

For more information, see the file setting [cli_binary_format](./cli-configure-files.html#cli-config-cli_binary_format)[--cli-binary-format](./cli-configure-options.html#cli-configure-options-cli-binary-format)

### Streaming blob

Streaming blobs such as `aws cloudsearchdomain upload-documents` do not
                use prefixes. Instead, streaming blob parameters are formatted using the direct file
                path. The following example uses the direct file path
                    `document-batch.json` for the ```
aws cloudsearchdomain
                    upload-documents
```
 command:

`$``aws cloudsearchdomain upload-documents \ --endpoint-url https://doc-my-domain.us-west-1.cloudsearch.amazonaws.com \ --content-type application/json \ --documents``document-batch.json`

## Map

        A set of key-value pairs specified in JSON or by using the CLI's [shorthand syntax](./cli-usage-shorthand.html). The following JSON example
            reads an item from an Amazon DynamoDB table named *my-table* with a map
            parameter, `--key`. The parameter specifies the primary key named
                *id* with a number value of *1* in a nested
            JSON structure.

For more advanced JSON usage in a command line, consider using a command line JSON
            processor, like `jq`, to create JSON strings. For more information on
                `jq`, see the [jq
                repository](http://stedolan.github.io/jq/) on 

*GitHub*.

`$``aws dynamodb get-item --table-name my-table --key '{"id": {"N":"1"}}'``{ "Item": { "name": { "S": "John" }, "id": { "N": "1" } } }`

## Document

        ###### Note

[Shorthand syntax](./cli-usage-shorthand.html) is not compatible with
                document types.

Document types are used to send data without needing to embed JSON inside strings. The document type enables services to provide arbitrary schemas for you to use more flexible data types.

This allows for sending JSON data without needing to escape values. For example, instead of using the following escaped JSON input:

`{"document": "{\"key\":true}"}`

You can use the following document type:

`{"document": {"key": true}}`

### Valid values for document types

Due to the flexible nature of document types, there are multiple valid value types. Valid values include the following:

- **String**
- 
                        `--option``'"value"'`
- **Number**
- 
                        `--option``123``--option``123.456`
- **Boolean**
- 
                        `--option``true`
- **Null**
- 
                        `--option``null`
- **Array**
- 
                        `--option``'["value1", "value2", "value3"]'``--option``'["value", 1, true, null, ["key1", 2.34], {"key2": "value2"}]'`
- **Object**
- 
                        `--option``'{"key": "value"}'``--option``'{"key1": "value1", "key2": 123, "key3": true, "key4": null, "key5": ["value3", "value4"], "key6": {"value5": "value6"}'`