# Using shorthand syntax in the AWS CLI - AWS Command Line Interface

**Source:** [https://docs.aws.amazon.com/cli/latest/userguide/cli-usage-shorthand.html](https://docs.aws.amazon.com/cli/latest/userguide/cli-usage-shorthand.html)

---

The AWS Command Line Interface (AWS CLI) can accept many of its option parameters in JSON format. However, it can be tedious to enter large JSON lists or structures on the command line. To make this easier, the AWS CLI also supports a shorthand syntax that enables a simpler representation of your option parameters than using the full JSON format.

###### Topics

## Structure parameters with key-value pairs

    The shorthand syntax in the AWS CLI makes it easier for users to input parameters that are
      flat (non-nested structures). The format is a comma-separated list of key-value pairs. Be sure
      to use the [quoting](./cli-usage-parameters-quoting-strings.html) and escaping
      rules appropriate for your terminal as shorthand syntax are strings.

`--option``key1=value1,key2=value2,key3=value3`

Is equivalent to the following example, formatted in JSON.

`--option``'{"key1":"value1","key2":"value2","key3":"value3"}'`

There must be no white space between each comma-separated key-value pair. Here is an
      example of the Amazon DynamoDB `update-table` command with the
        `--provisioned-throughput` option specified in shorthand.

`$``aws dynamodb update-table \ --provisioned-throughput``ReadCapacityUnits=15,WriteCapacityUnits=10`\ --table-name MyDDBTable

This is equivalent to the following example formatted in JSON.

`$``aws dynamodb update-table \ --provisioned-throughput``'{"ReadCapacityUnits":15,"WriteCapacityUnits":10}'`\ --table-name MyDDBTable

## Loading a file as a shorthand syntax value

    When a value is large or complex, it is often easier to load in as a value. To load a file
      as a shorthand syntax value, the formatting will change slightly. Instead of
        `key=value` you'll use the `@=` operator instead of the `=`
      operator. The `@=` signifies to the AWS CLI that the value should be read as a file
      path and not a string. When loading files in shorthand syntax, the usual [AWS CLI file formatting rules apply](./cli-usage-parameters-file.html). The following
      example shows a key-value pair loading a file for its value.

`--option``key@=file://template.txt`

The following example demonstrates loading a certificate file for the ```
aws
        rolesanywhere create-trust-anchor
```
 command.

`$``aws rolesanywhere create-trust-anchor --name TrustAnchor \ --source sourceData={``x509CertificateData@=file://root-ca.crt`},sourceType="CERTIFICATE_BUNDLE" \ --enabled

## Using shorthand syntax with the AWS CLI

    You can specify Input parameters in a list form in two ways: JSON or shorthand. The AWS CLI shorthand syntax is designed to make it easier to pass in lists with number, string, or non-nested structures.

The basic format is shown here, where values in the list are separated by a single space.

`--option``value1 value2 value3`

This is equivalent to the following example, formatted in JSON.

`--option``'[value1,value2,value3]'`

As previously mentioned, you can specify a list of numbers, a list of strings, or a list
      of non-nested structures in shorthand. The following is an example of the
        `stop-instances` command for Amazon Elastic Compute Cloud (Amazon EC2), where the input parameter (list
      of strings) for the `--instance-ids` option is specified in shorthand.

`$``aws ec2 stop-instances \ --instance-ids``i-1486157a i-1286157c i-ec3a7e87`

This is equivalent to the following example formatted in JSON.

`$``aws ec2 stop-instances \ --instance-ids``'["i-1486157a","i-1286157c","i-ec3a7e87"]'`

The following example shows the Amazon EC2 `create-tags` command, which takes a list
      of non-nested structures for the `--tags` option. The `--resources`
      option specifies the ID of the instance to tag.

`$``aws ec2 create-tags \ --resources i-1286157c \ --tags``Key=My1stTag,Value=Value1 Key=My2ndTag,Value=Value2 Key=My3rdTag,Value=Value3`

This is equivalent to the following example, formatted in JSON. The JSON parameter is written over multiple lines for readability.

`$``aws ec2 create-tags \ --resources i-1286157c \ --tags``'[ {"Key": "My1stTag", "Value": "Value1"}, {"Key": "My2ndTag", "Value": "Value2"}, {"Key": "My3rdTag", "Value": "Value3"} ]'`