# Authenticating with short-term credentials for the AWS CLI - AWS Command Line Interface

**Source:** [https://docs.aws.amazon.com/cli/latest/userguide/cli-authentication-short-term.html](https://docs.aws.amazon.com/cli/latest/userguide/cli-authentication-short-term.html)

---

We recommend configuring your SDK or tool to use [IAM Identity
            Center authentication](https://docs.aws.amazon.com/sdkref/latest/guide/access-sso.html) with extended session duration options. However, you can
        copy and use temporary credentials that are available in the AWS access portal. New
        credentials will need to be copied when these expire. You can use the temporary credentials
        in a profile or use them as values for system properties and environment variables.

- 
            Follow [these instructions](https://docs.aws.amazon.com/singlesignon/latest/userguide/howtogetcredentials.html)to copy IAM role credentials from the AWS access portal.- 
                    For step 2 in the linked instructions, choose the AWS account and IAM role name that grants access for your development needs. This role typically has a name like **PowerUserAccess**or**Developer**.
- 
                    For step 4, select the **Add a profile to your AWS credentials file**option and copy the contents.
 
- 
                    
- 
            Create or open the shared `credentials`file. This file is`~/.aws/credentials`on Linux and macOS systems, and`%USERPROFILE%\.aws\credentials`on Windows. For more information, see[Configuration and credential file settings in the AWS CLI](./cli-configure-files.html).
- 
            Add the following text to the shared `credentials`file. Replace the sample values with the credentials you copied.`[default] aws_access_key_id = AKIAIOSFODNN7EXAMPLE aws_secret_access_key = wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY aws_session_token = IQoJb3JpZ2luX2IQoJb3JpZ2luX2IQoJb3JpZ2luX2IQoJb3JpZ2luX2IQoJb3JpZVERYLONGSTRINGEXAMPLE`
- 
            Add your preferred default region and format to the shared `config`file.`[default] region=``us-west-2`output=`json`[profile user1] region=`us-east-1`output=`text`

When the SDK creates a service client, it will access these temporary credentials and
        use them for each request. The settings for the IAM role chosen in step 2a determine
            [how long the temporary credentials are valid](https://docs.aws.amazon.com/singlesignon/latest/userguide/howtosessionduration.html). The maximum duration is twelve
        hours.

Repeat these steps each time your credentials expire.