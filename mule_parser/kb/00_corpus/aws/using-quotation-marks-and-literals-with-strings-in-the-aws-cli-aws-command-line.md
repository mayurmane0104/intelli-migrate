# Using quotation marks and literals with strings in the AWS CLI - AWS Command Line Interface

**Source:** [https://docs.aws.amazon.com/cli/latest/userguide/cli-usage-parameters-quoting-strings.html](https://docs.aws.amazon.com/cli/latest/userguide/cli-usage-parameters-quoting-strings.html)

---

There are primarily two ways single and double quotes are used in the AWS CLI.

## Using quotation marks around strings that contain white spaces

        Parameter names and their values are separated by spaces on the command line. If a string value contains an embedded space, then you must surround the entire string with quotation marks to prevent the AWS CLI from misinterpreting the space as a divider between the value and the next parameter name. Which type of quotation mark you use depends on the operating system you are running the AWS CLI on.

Use single quotation marks  `' '`
                    

`$`aws ec2 create-key-pair`--key-name 'my key pair'`

For more information on using quotes, see the user documentation for your preferred shell.

Optionally, you can separate the parameter name from the value with an equals sign
                `=` instead of a space. This is typically necessary only if the value of
            the parameter starts with a hyphen.

`$`aws ec2 delete-key-pair`--key-name=-mykey`

## Using quotation marks inside strings

        Strings might contain quotation marks, and your shell might require escaping quotations
            for them to work properly. One of the common parameter value types is a JSON string.
            This is complex since it includes spaces and double quotation marks `" "`
            around each element name and value in the JSON structure. The way you enter
            JSON-formatted parameters on the command line differs depending on your operating
            system. 

For more advanced JSON usage in the command line, consider using a command line JSON
            processor, like `jq`, to create JSON strings. For more information on
                `jq`, see the [jq
                repository](http://stedolan.github.io/jq/) on 

*GitHub*.

For Linux and macOS to interpret strings literally use single quotation
                        marks `' '` to enclose the JSON data structure, as in the
                        following example. You do not need to escape double quotation marks embedded
                        in the JSON string, as they are being treated literally. Since the JSON is
                        enclosed in single quotation marks, any single quotation marks in the string
                        will need to be escaped, this is usually accomplished using a backslash
                        before the single quote `\'`.

`$``aws ec2 run-instances \ --image-id ami-12345678 \ --block-device-mappings``'`[{"DeviceName":"/dev/sdb","Ebs":{"VolumeSize":20,"DeleteOnTermination":false,"VolumeType":"standard"}}]`'`

For more information on using quotes, see the user documentation for your preferred shell.