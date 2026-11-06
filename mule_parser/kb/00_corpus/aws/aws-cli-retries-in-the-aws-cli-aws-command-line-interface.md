# AWS CLI retries in the AWS CLI - AWS Command Line Interface

**Source:** [https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-retries.html](https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-retries.html)

---

This topic describes how the AWS CLI might see calls to AWS services fail due to unexpected issues. These issues can occur on the server side or might fail due to rate limiting from the AWS service you're attempting to call. These kinds of failures usually don’t require special handling and the call is automatically made again, often after a brief waiting period. The AWS CLI provides many features to assist in retrying client calls to AWS services when these kinds of errors or exceptions are experienced.

## Available retry modes

    ###### The AWS CLI has multiple modes to choose from depending on your version:

### Standard retry mode (default)

`Standard` mode is a standard set of retry rules across the AWS SDKs with
        more functionality than legacy and is the default mode is the default for AWS CLI. Standard
        mode was created for the AWS CLI version 2 and is backported to AWS CLI version 1. Standard mode’s functionality
        includes:

- 
          A default value of 2 for maximum retry attempts, making a total of 3 call attempts. This value can be overwritten through the `max_attempts`configuration parameter.
- 
          Retry attempts for the following expanded list of errors/exceptions: - 
              Transient errors/exceptions - 
                  `RequestTimeout`
- 
                  `RequestTimeoutException`
- 
                  `PriorRequestNotComplete`
- 
                  `ConnectionError`
- 
                  `HTTPClientError`
 
- 
                  
- 
              Service-side throttling/limit errors and exceptions: - 
                  `Throttling`
- 
                  `ThrottlingException`
- 
                  `ThrottledException`
- 
                  `RequestThrottledException`
- 
                  `TooManyRequestsException`
- 
                  `ProvisionedThroughputExceededException`
- 
                  `TransactionInProgressException`
- 
                  `RequestLimitExceeded`
- 
                  `BandwidthLimitExceeded`
- 
                  `LimitExceededException`
- 
                  `RequestThrottled`
- 
                  `SlowDown`
- 
                  `EC2ThrottledException`
 
- 
                  
 
- 
              

- 
          Retry attempts on nondescriptive, transient error codes. Specifically, these HTTP status codes: 500, 502, 503, 504. 
- 
          Any retry attempt will include an exponential backoff by a base factor of 2 for a maximum backoff time of 20 seconds. 

### Legacy retry mode

`Legacy` mode uses an older retry handler that has limited functionality
        which includes:

- 
          A default value of 4 for maximum retry attempts, making a total of 5 call attempts. This value can be overwritten through the `max_attempts`configuration parameter.
- 
          DynamoDB has a default value of 9 for maximum retry attempts, making a total of 10 call attempts. This value can be overwritten through the `max_attempts`configuration parameter.
- 
          Retry attempts for the following limited number of errors/exceptions: - 
              General socket/connection errors: - 
                  `ConnectionError`
- 
                  `ConnectionClosedError`
- 
                  `ReadTimeoutError`
- 
                  `EndpointConnectionError`
 
- 
                  
- 
              Service-side throttling/limit errors and exceptions: - 
                  `Throttling`
- 
                  `ThrottlingException`
- 
                  `ThrottledException`
- 
                  `RequestThrottledException`
- 
                  `ProvisionedThroughputExceededException`
 
- 
                  
 
- 
              
- 
          Retry attempts on several HTTP status codes, including 429, 500, 502, 503, 504, and 509. 
- 
          Any retry attempt will include an exponential backoff by a base factor of 2. 

### Adaptive retry mode

###### Warning

Adaptive mode is an experimental mode and is subject to change, both in features and behavior.

`Adaptive` retry mode is an experimental retry mode that includes all the
        features of standard mode. In addition to the standard mode features, adaptive mode also
        introduces client-side rate limiting through the use of a token bucket and rate-limit
        variables that are dynamically updated with each retry attempt. This mode offers flexibility
        in client-side retries that adapts to the error/exception state response from an AWS
        service.

With each new retry attempt, adaptive mode modifies the rate-limit variables based on the error, exception, or HTTP status code presented in the response from the AWS service. These rate-limit variables are then used to calculate a new call rate for the client. Each exception/error or non-success HTTP response (provided in the list above) from an AWS service updates the rate-limit variables as retries occur until success is reached, the token bucket is exhausted, or the configured maximum attempts value is reached.

## Configuring a retry mode

    The AWS CLI includes a variety of both retry configurations as well as configuration methods to consider when creating your client object.

### Available configuration methods

In the AWS CLI, users can configure retries in the following ways:

- 
          Environment variables 
- 
          AWS CLI configuration file 

Users can customize the following retry options:

- 
          Retry mode - Specifies which retry mode the AWS CLI uses. As described previously, there are three retry modes available: legacy, standard, and adaptive. The default value for the AWS CLI version 2 is standard. 
- 
          Max attempts - Specifies the value of maximum retry attempts the AWS CLI retry handler uses, where the initial call counts toward the value that you provide. The default value is based on your retry mode. 

### Defining a retry configuration in your environment variables

To define your retry configuration for the AWS CLI, update your operating system's environment variables.

The retry environment variables are:

- 
          `AWS_RETRY_MODE`
- 
          `AWS_MAX_ATTEMPTS`

For more information on environment variables, see [Configuring environment variables for the AWS CLI](./cli-configure-envvars.html).

### Defining a retry configuration in your AWS configuration file

To change your retry configuration, update your global AWS configuration file. The default location for your AWS config file is ~/.aws/config.

The following is an example of an AWS config file:

```
[default]
retry_mode = standard
max_attempts = 6
```
For more information on configuration files, see [Configuration and credential file settings in the AWS CLI](./cli-configure-files.html).

## Viewing logs of retry attempts

    The AWS CLI uses Boto3's retry methodology and logging. You can use the `--debug`
      option on any command to receive debug logs. For more information on how to use the
        `--debug` option, see [Command line options in the AWS CLI](./cli-configure-options.html).

If you search for "retry" in your debug logs, you'll find the retry information you need. The client log entries for retry attempts depend on which retry mode you’ve enabled.

**Legacy mode:**

Retry messages are generated by botocore.retryhandler. You’ll see one of three messages:

- 
        `No retry needed`
- 
        `Retry needed, action of:``<action_name>`
- 
        `Reached the maximum number of retry attempts:``<attempt_number>`

**Standard or adaptive mode:**

Retry messages are generated by botocore.retries.standard. You’ll see one of three messages:

- 
        `No retrying request`
- 
        `Retry needed, retrying request after delay of:``<delay_value>`
- 
        `Retry needed but retry quota reached, not retrying request`

For the full definition file of botocore retries, see [_retry.json](https://github.com/boto/botocore/blob/develop/botocore/data/_retry.json) on the 

*botocore GitHub Repository*.