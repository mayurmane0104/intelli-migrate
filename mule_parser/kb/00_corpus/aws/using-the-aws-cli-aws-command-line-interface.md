# Using the AWS CLI - AWS Command Line Interface

**Source:** [https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-using.html](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-using.html)

---

This section provides a comprehensive overview of the  general use, common features, and
    options available in the AWS Command Line Interface (AWS CLI), going beyond the details covered in the
    Configuration [Using endpoints in the AWS CLI](./cli-configure-endpoints.html) section. 

This guide delves into the fundamental aspects of writing AWS CLI commands, including their basic structure, formatting, and filtering capabilities. By understanding these core elements, you'll be able to construct commands that precisely target the resources and actions you require, without the need to navigate complex web-based consoles.

Additionally, this highlights the help content and documentation available for the AWS CLI.
    From the built-in command line help to the comprehensive [AWS CLI version 2 reference guide](https://docs.aws.amazon.com/cli/latest/reference/), you'll have access to information to
    assist you in exploring the features and capabilities of the AWS CLI. 

For AWS service specific examples and use cases, see [Examples for the AWS CLI](./cli-chap-code-examples.html) or the [AWS CLI version 2 reference guide](https://docs.aws.amazon.com/cli/latest/reference/). These provide command specific
    information and demonstrate examples on how to leverage the AWS CLI for various
    AWS services.

###### Note

By default, the AWS CLI sends requests to AWS services by using HTTPS on TCP port 443. To ensure successful use of the AWS CLI, you must be able to make outbound connections on this port.