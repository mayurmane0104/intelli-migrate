# Controlling command output in the AWS CLI - AWS Command Line Interface

**Source:** [https://docs.aws.amazon.com/cli/latest/userguide/cli-usage-output.html](https://docs.aws.amazon.com/cli/latest/userguide/cli-usage-output.html)

---

This section describes the different ways to control the output from the AWS Command Line Interface (AWS CLI). Customizing the AWS CLI output in your terminal can improve readability, streamline scripting automation and provide easier navigation through larger data sets.

The AWS CLI supports multiple [output formats](./cli-usage-output-format.html),
        including [json](./cli-usage-output-format.html#json-output), [text](./cli-usage-output-format.html#text-output),
            [yaml](./cli-usage-output-format.html#yaml-output), [off](./cli-usage-output-format.html#off-output), and [table](./cli-usage-output-format.html#table-output). Some services have server-side [pagination](./cli-usage-pagination.html) for their data
            and the AWS CLI provides it's own client-side features for additional pagination
            options.

Lastly, the AWS CLI has both[ server-side and client-side
            filtering](./cli-usage-filter.html) that you can use individually or together to filter your AWS CLI
        output.

###### Topics

## Sensitive output

        Some operations of the AWS CLI might return information that could be considered sensitive, including information from environment variables. The exposure of this information might represent a security risk in certain scenarios; for example, the information could be included in continuous integration and continuous deployment (CI/CD) logs. It is therefore important that you review when you are including such output as part of your logs, and suppress the output when not needed.

For additional information about protecting sensitive data, see [Data protection in the AWS CLI](./data-protection.html).

Consider the following best practices:

- 
                Consider programmatically retrieving your secrets from a secrets store, such as AWS Secrets Manager. 
- 
                Review the contents of your build logs to ensure they do not contain sensitive information. Consider approaches such as piping to `/dev/null`or capturing the output as a bash or PowerShell variable to suppress command outputs.The following is a bash example for redirecting output, but not errors, to `/dev/null`:`$``aws s3 ls > /dev/null`For specifics on suppressing output for your terminal, see the user documentation of the terminal you use. 
- 
                Consider the access of your logs and scope the access appropriately for your use case. 

## Server-side vs client-side output options

        The AWS CLI has both[ server-side and client-side
                filtering](./cli-usage-filter.html) that you can use individually or together to filter your AWS CLI
            output. Server-side filtering is processed first and returns your output for client-side
            filtering. Server-side filtering is supported by the service API. Client-side filtering
            is supported by the AWS CLI client using the `--query` parameter.

**Server-side** output options are features directly
            supported by the AWS service API. Any data that is filtered or paged out is not sent
            to the client, which can speed up HTTP response times and improve bandwidth for larger
            data sets.

**Client-side** output options are features created by
            the AWS CLI. All data is sent to the client, then the AWS CLI filters or pages the content
            displayed. Client-side operations do not save on speed or bandwidth for larger
            datasets.

When server-side and client-side options are used together, server-side operations are completed first and then sent to the client for client-side operations. This uses the potential speed and bandwidth savings of server-side options, while using additional AWS CLI features to get your desired output.