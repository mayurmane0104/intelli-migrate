# Authenticating using IAM user credentials for the AWS CLI - AWS Command Line Interface

**Source:** [https://docs.aws.amazon.com/cli/latest/userguide/cli-authentication-user.html](https://docs.aws.amazon.com/cli/latest/userguide/cli-authentication-user.html)

---

###### Warning

To avoid security risks, don't use IAM users for authentication when developing purpose-built software
	   or working with real data. Instead, use federation with an identity provider such as
	   [AWS IAM Identity Center](https://docs.aws.amazon.com/singlesignon/latest/userguide/what-is.html).

This section explains how to  configure basic settings with an IAM user. These include
        your security credentials using the `config` and
            `credentials` files.
            To instead see configuration instructions for
            AWS IAM Identity Center, see [Configuring IAM Identity Center authentication with the AWS CLI](./cli-configure-sso.html).

###### Topics

## Step 1: Create your IAM user

        Create your IAM user by following the [Creating IAM users (console)](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_users_create.html#id_users_create_console) procedure in the *IAM User Guide*. 

- 
                For **Permission options**, choose**Attach policies directly**for how you want to assign permissions to this user.
- 
                Most "Getting Started" SDK tutorials use the Amazon S3 service as an example. To provide your application with full access to Amazon S3, select the `AmazonS3FullAccess`policy to attach to this user.

## Step 2: Get your access keys

        - Sign in to the AWS Management Console and open the IAM console at - [https://console.aws.amazon.com/iam/](https://console.aws.amazon.com/iam/).
- 
                In the navigation pane of the IAM console, select **Users**and then select the`User name`
- 
                On the user's page, select the **Security credentials**page. Then, under**Access keys**, select**Create access key**.
- 
                For **Create access key Step 1**, choose**Command Line Interface (CLI)**.
- 
                For **Create access key Step 2**, enter an optional tag and select**Next**.
- 
                For **Create access key Step 3**, select**Download .csv file**to save a`.csv`file with your IAM user's access key and secret access key. You need this information for later.
- 
                Select Done. 

## Step 3: Configure the AWS CLI

        For general use, the AWS CLI needs the following pieces of information:

- 
                Access key ID 
- 
                Secret access key 
- 
                AWS Region 
- 
                Output format 

The AWS CLI stores this information in a *profile* (a
            collection of settings) named `default` in the
                `credentials` file. By default, the information in this profile
            is used when you run an AWS CLI command that doesn't explicitly specify a profile to use.
            For more information on the `credentials` file, see [Configuration and credential file settings in the AWS CLI](./cli-configure-files.html).

To configure the AWS CLI, use one of the following procedures:

###### Topics

### Using `aws configure`

            For general use, the `aws configure` command is the fastest way to set
                up your AWS CLI installation. This configure wizard prompts you for each piece of
                information you need to get started. Unless otherwise specified by using the
                    `--profile` option, the AWS CLI stores this information in the
                    `default` profile.

The following example configures a `default` profile using sample
                values. Replace them with your own values as described in the following
                sections.

`$``aws configure``AWS Access Key ID [None]:``AWS Secret Access Key [None]:``AKIAIOSFODNN7EXAMPLE``Default region name [None]:``wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY``Default output format [None]:``us-west-2``json`

The following example configures a profile named `userprod` using
                sample values. Replace them with your own values as described in the following
                sections.

`$``aws configure --profile``userprod``AWS Access Key ID [None]:``AWS Secret Access Key [None]:``AKIAIOSFODNN7EXAMPLE``Default region name [None]:``wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY``Default output format [None]:``us-west-2``json`

### Importing access keys via .CSV file

Instead of using `aws configure` to enter in access keys, you can
                import the plain text `.csv` file you downloaded after you
                created your access keys. 

The `.csv` file must contain the following headers.

- 
                    User Name - This column must be added to your `.csv`. This is used to create the profile name used in the the`config`and`credentials`files when you import.
- 
                    Access key ID 
- 
                    Secret access key 

###### Note

During initial access keys creation, once you close the **Download
                        .csv file** dialog box, you cannot access your secret access key
                    after you close the dialog box. If you need a `.csv` file,
                    you'll need to create one yourself with the required headers and your stored
                    access keys information. If you do not have access to your access keys
                    information, you need to create a new access keys.

To import the `.csv` file, use the ```
aws configure
                    import
```
 command with the `--csv` option as follows:

`$``aws configure import --csv``file://credentials.csv`

For more information, see [aws_configure_import](./cli-configure-files.html#cli-config-aws_configure_import)

### Directly editing the `config` and `credentials` files

            To directly edit the `config` and
                    `credentials` files, perform the following.

- 
                    Create or open the shared AWS `credentials`file. This file is`~/.aws/credentials`on Linux and macOS systems, and`%USERPROFILE%\.aws\credentials`on Windows. For more information, see[Configuration and credential file settings in the AWS CLI](./cli-configure-files.html).
- 
                    Add the following text to the shared `credentials`file. Replace the sample values in the`.csv`file that you downloaded earlier and save the file.`[default] aws_access_key_id = AKIAIOSFODNN7EXAMPLE aws_secret_access_key = wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY`

## (Optional) Using multi-factor authentication with your IAM user credentials

        For additional security, you can use a one-time key generated from a multi-factor authentication (MFA) device, a U2F device, or mobile app when you attempt to make a call.

With your MFA enabled IAM user, run the [ aws
                    configure mfa-login](https://docs.aws.amazon.com/cli/latest/reference/configure/mfa-login.html) command to configure a new profile to use
            with multi-factor authentication (MFA) for the specified profile. If no profile is
            specified, the MFA is based on the 

`default` profile. If no default profile
            is configured, the `mfa-login` command prompts you for you AWS credentials
            before asking for your MFA information. The following command example uses your default
            configuration and creates an MFA profile.`$ ``aws configure mfa-login`
`MFA serial number or ARN: ``arn:aws:iam::123456789012:mfa/MFADeviceName``MFA token code: ``123456````
Profile to update [session-MFADeviceName]:
Temporary credentials written to profile 'session-MFADeviceName'
Credentials will expire at 2023-05-19 18:06:10 UTC
To use these credentials, specify --profile session-MFADeviceName when running AWS CLI commands
```
To update an existing profile, use the `--update-profile` parameter.

`$ ``aws configure mfa-login --profile ``myprofile` --update-profile `mfaprofile`
`MFA token code: ``123456````
Temporary credentials written to profile 'mfaprofile'
Credentials will expire at 2023-05-19 18:06:10 UTC
To use these credentials, specify --profile mfaprofile when running AWS CLI commands
```
This command currently supports only hardware or software based one-time password (OTP) authenticators. Passkeys and U2F devices are not currently supported with this command.

To use your MFA profile, use the `--profile` option with your
            commands.

`$ ``aws s3 ls --profile ``mfaprofile`For more information on using MFA with IAM, including how to assign MFA to an
            IAM user, see [AWS Multi-factor authentication in IAM ](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_mfa.html) in the
                *AWS Identity and Access Management User
            Guide*.