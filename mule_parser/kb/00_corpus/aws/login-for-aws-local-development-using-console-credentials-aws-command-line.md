# Login for AWS local development using console credentials - AWS Command Line Interface

**Source:** [https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-sign-in.html](https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-sign-in.html)

---

You can use your existing AWS Management Console sign-in credentials for programmatic access to AWS services. After a browser-based authentication flow, AWS generates temporary credentials that work across local development tools like the AWS CLI, AWS Tools for PowerShell and AWS SDKs. This feature simplifies the process of configuring and managing AWS CLI credentials, especially if you prefer interactive authentication over managing long-term access keys.

With this process, you can authenticate using root credentials created during initial account set up, an IAM user, or a federated identity from your identity provider, and the AWS CLI automatically manages the temporary credentials for you. This approach enhances security by eliminating the need to store long-term credentials locally.

When you run the `aws login` command, you can select from your active console sessions, or sign in through the 
    browser-based authentication flow and this will automatically generate temporary credentials. The CLI will automatically 
    refresh these credentials for up to 12 hours.

Once configured, your session can be used in the AWS CLI and other AWS SDKs and Tools.

###### Topics

## Prerequisites

    - 
        Install the AWS CLI. For more information, see [Installing or updating to the latest version of the AWS CLI](./getting-started-install.html). A minimum version of 2.32.0 is required to use the`aws login`command.
- 
        Access to sign into the AWS Management Console as a root user, IAM user, or through federation with IAM. If you use IAM Identity Center, go to [Configuring IAM Identity Center authentication with the AWS CLI](./cli-configure-sso.html)instead.
- 
        Ensure the IAM identity has the appropriate permissions. Attach the [SignInLocalDevelopmentAccess](https://docs.aws.amazon.com/signin/latest/userguide/security-iam-awsmanpol.html)managed policy to your IAM user, role, or group. If you sign in as a root user, no additional permissions are required.

## Log in to the AWS CLI with the `aws login` command.

    Run the `aws login` command to authenticate using your existing AWS Management Console credentials. If you have not previously configured a profile, you're prompted for additional information. To sign in or configure a profile follow the below steps.

- 
        In your preferred terminal, run the `aws login`command.`$ aws login`To sign in to a named profile or create a new one, use the `--profile`option.`$ aws login --profile my-dev-profile`- 
            If this is a new profile or no AWS Region has been specified, the AWS CLI prompts you to provide a region. `No AWS region has been configured. The AWS region is the geographic location of your AWS resources. If you've used AWS before and already have resources in your account, tell us which region they were created in. If you haven't created resources in your account before, you can pick the region closest to you: https://docs.aws.amazon.com/global-infrastructure/latest/regions/aws-regions.html. You are able to change the region in the CLI at any time with the command `aws configure set region NEW_REGION`. AWS Region [us-east-1]:`
- 
            If the device using the AWS CLI does not have a browser, you can use the `--remote`option to provide a url for you to open on a browser-enabled device.`$ aws login --remote`###### NoteYou can control access to same-device ( `aws login`) and cross-device (`aws login --remote`) authentication. Use the following resource ARNs in any relevant IAM policy.- 
                        `arn:aws:signin:`— Use this ARN for same-device authentication with`region`:`account-id`:oauth2/public-client/localhost`aws login`.
- 
                        `arn:aws:signin:`— Use this ARN for cross-device authentication with`region`:`account-id`:oauth2/public-client/remote`aws login --remote`.
 
- 
                        
 
- 
            
- 
        The AWS CLI attempts to open your default browser for the sign in process of your AWS account. `Attempting to open the login page for `us-east-1` in your default browser. If the browser does not open, use the following URL to complete your login: https://signin.us-east-1.amazonaws.com/authorize?<abbreviated> If you cannot connect to this URL, make sure that you have specified a valid region.`- 
            If you used the `--remote`option, instructions to manually start the sign in process are displayed based on the type of authorization you are using. The URL displayed is a unique URL starting with: https://us-east-1.signin.amazonaws.com/authorize. Once you complete the browser log in, you will need to copy and paste the resulting authorization code back in the CLI.`Browser will not be automatically opened. Please visit the following URL: https://``region`.signin.amazonaws.com/authorize?<abbreviated> Please enter the authorization code displayed in the browser:
 
- 
            
- 
        In the browser, select your credentials to use from the displayed list and then return to your terminal. - 
            If the profile you are configuring has a previously configured login session that does not match your new session, the AWS CLI prompts you to confirm that you are switching the session that corresponds to the existing profile. `Profile signin is already configured to use session arn:aws:iam::``0123456789012`:`user/ReadOnly`. Do you want to overwrite it to use arn:aws:iam::`0123456789012`:`user/Admin`instead? (y/n):.
 
- 
            
- 
        A final message describes the completed profile configuration. You can now use this profile to request credentials. Use the `aws login`command to request and retrieve the credentials needed to run commands.The authentication token is cached to disk under the `.aws/login/cache`directory with a filename based on the resolved profile.

### Generated configuration file

These steps result in creating the `default` profile in
        the `config` file that looks like the following:

`[default] login_session = arn:aws:iam::``0123456789012`:`user/username`region = us-east-1

## Run a command with your profile

    Once signed in, you can use your credentials to invoke AWS CLI commands with the
      associated profile. The following example calls the `get-caller-identity`
      command using the `default` profile:

`$ aws sts get-caller-identity`To sign in to a specific session, use the `--profile` option.

`$ aws sts get-caller-identity --profile``my`-dev-profile

The AWS CLI and SDKs will automatically refresh the cached credentials every 15 minutes as needed. 
      The overall session will be valid for up to the set session duration of the IAM principal (maximum of 12 hours), 
      after which you must run `aws login` again.

## Sign out of your session using the aws logout command

    When you are done using your session, you can let your credentials expire, or run the `aws logout` command to delete your cached credentials. 
      If no profile is specified on the command line or in the `AWS_PROFILE` environment variable, 
      the command signs you out of your default profile. The following example signs you out of your default profile.

`$ aws logout`To sign out of a specific session, use the `--profile` option.

`$ aws logout --profile``my`-dev-profile

To sign out of all profiles that use login credentials, use the `--all` option.

`$ aws logout --all`### Cached Credentials

The temporary cached credentials, as well as the metadata required to refresh them are stored by default in `~/.aws/login/cache` on Linux and macOS, or `%USERPROFILE%\.aws\login\cache` on Windows.

To store the short-term credentails cache in an alternative location, set the `AWS_LOGIN_CACHE_DIRECTORY` environment variable.

#### Sharing Login credentials as process credentials

Older versions of the AWS SDKs or other development tools may not support console credentials yet. As a workaround, you can configure the AWS CLI to serve as a process credentials provider. The CLI will continue to refresh the credentials as needed, while sharing them with tools configured to use the credential_process profile.

In this example, use the AWS CLI to login first for profile signin:

`$ aws login --profile signin`Then, manually configure a profile with the credential_process option, which points back at the signin profile. Now you can configure SDKs or tools to use the process profile, which will invoke the CLI to share the credentials from the signin profile.

`[profile signin] login_session = arn:aws:iam::``0123456789012`:`user/username`region = us-east-1 [profile process] credential_process = aws configure export-credentials --profile signin --format process region = us-east-1

## Troubleshooting

    This page contains recommendations for toubleshooting issues with logging in for AWS local development using console credentials for the AWS CLI.

###### Note

To troubleshoot other issues you may come across using the AWS CLI, see 
        [Troubleshooting errors for the AWS CLI](./cli-chap-troubleshooting.html).

### ExpiredToken or AccessDeniedException errors after using "aws login"

When running an AWS CLI command after running `aws login` for a given
        profile, you may encounter an expired or invalid credentials error.

```
$ aws s3 ls
An error occurred (ExpiredToken) when calling the ListBuckets operation: The provided token has expired.
```
**Possible cause:** You have a mix of existing credentials and the new login credentials in that profile

Run `aws configure list` or `aws configure list --profile <profile name>` to print where the CLI is resolving credentials from for either the default or the given profile.

If the TYPE column is something other than login, this means that there is still a different type of credentials set in the target profile.

In this example, credentials are being resolved from the shared credentials file in your home directory, which has precedence over the login credentials.

```
$  aws configure list
NAME       : VALUE                    : TYPE             : LOCATION
profile    : <not set>                : None             : None
access_key : ****************MPLE     : shared-credentials-file :
secret_key : ****************EKEY     : shared-credentials-file :
region     : us-east-1                : config-file      : ~/.aws/config
```
To address this, manually remove any existing credentials from your config and credentials file for the target profile. Once you do so, you should see login credentials when running `aws configure list` again.

```
$  aws configure list
NAME       : VALUE                    : TYPE             : LOCATION
profile    : <not set>                : None             : None
access_key : ****************MPLE     : login            :
secret_key : ****************EKEY     : login            :
region     : us-east-1                : config-file      : ~/.aws/config
```
Alternatively using the `--debug` option will show where the CLI is resolving credentials from.

### Firewall blocking network access when running "aws login"

When running `aws login` you may encounter a popup or message from your firewall software that prevents the AWS CLI from accessing your network

**Possible cause:** Your firewall or security software is preventing the AWS CLI from opening the port used to handle the OAuth callback.

To avoid this issue, use the `--remote` option instead. This will prompt you to copy and paste the authorization code instead of using the OAuth callback.

`$ aws login --remote`## Related resources

    Additional resources are as follows.