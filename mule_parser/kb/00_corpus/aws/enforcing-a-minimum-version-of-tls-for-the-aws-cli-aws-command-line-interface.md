# Enforcing a minimum version of TLS for the AWS CLI - AWS Command Line Interface

**Source:** [https://docs.aws.amazon.com/cli/latest/userguide/cli-security-enforcing-tls.html](https://docs.aws.amazon.com/cli/latest/userguide/cli-security-enforcing-tls.html)

---

When using the AWS Command Line Interface (AWS CLI), the Transport Layer Security (TLS) protocol plays a
        crucial role in securing communication between the AWS CLI and AWS services. To add
        increased security when communicating with AWS services, you should use TLS 1.2 or
        later. TLS 1.3 is a prerequisite to enable post-quantum cryptography, which may require 
        additional actions or configurations. To learn more, see 
        [Enabling hybrid 
        post-quantum TLS](https://docs.aws.amazon.com/sdkref/latest/guide/pqtls-details.html).

AWS CLI version 2 uses an internal Python script that's compiled to use a minimum of TLS 1.2
            when the service it's talking to supports it. As long as you use version 2 of the AWS CLI,
            no further steps are needed to enforce this minimum. Additionally, to enforce a minimum of 
            TLS 1.3 on Linux, you can install AWS CLI version `2.34.54` or higher using the 
            [AWS CLI installer](./getting-started-install.html#getting-started-install.title) for Linux. To ensure 
            you're getting increased security, be sure to update to a recent version of the AWS CLI.

The AWS CLI and AWS service can exchange data securely, with the TLS protocol providing encryption, authentication, and data integrity. By leveraging the TLS protocol, the AWS CLI ensures that your interactions with AWS services are protected from unauthorized access and data breaches, enhancing the overall security of your AWS ecosystem.

The AWS [shared responsibility model](https://aws.amazon.com/compliance/shared-responsibility-model/) applies to data protection in AWS Command Line Interface. As described in this
        model, AWS is responsible for protecting the global infrastructure that runs all of the
        AWS services. You are responsible for maintaining control over your content that is hosted
        on this infrastructure. You are also responsible for the security configuration and
        management tasks for the AWS services that you use. For more information about data
        protection, see 

[Data protection in the AWS CLI](./data-protection.html).