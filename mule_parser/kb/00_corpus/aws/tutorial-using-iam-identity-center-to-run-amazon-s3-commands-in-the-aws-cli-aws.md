# Tutorial: Using IAM Identity Center to run Amazon S3 commands in the AWS CLI - AWS Command Line Interface

**Source:** [https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-sso-tutorial.html](https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-sso-tutorial.html)

---

This topic describes how to configure the AWS CLI to authenticate users with current AWS IAM Identity Center (IAM Identity Center) to retrieve credentials to run AWS Command Line Interface (AWS CLI) commands for Amazon Simple Storage Service (Amazon S3).

###### Topics

## Step 1: Authentication in IAM Identity Center

        Gain access to SSO authentication within IAM Identity Center. Choose one of the following methods to access your AWS credentials.

Follow the instructions in [Getting started](https://docs.aws.amazon.com/singlesignon/latest/userguide/getting-started.html) in the *AWS IAM Identity Center User Guide*. This
                process activates IAM Identity Center, creates an administrative user, and adds an appropriate
                least-privilege permission set.

###### Note

Create a permission set that applies least-privilege permissions. We
                    recommend using the predefined `PowerUserAccess` permission set,
                    unless your employer has created a custom permission set for this purpose.
                

Exit the portal and sign in again to see your AWS accounts, programmatic
                access details, and options for `Administrator` or
                `PowerUserAccess`. Select `PowerUserAccess` when
                working with the SDK.

Sign in to AWS through your identity provider’s portal. If your Cloud
                Administrator has granted you `PowerUserAccess` (developer)
                permissions, you see the AWS accounts that you have access to and your
                permission set. Next to the name of your permission set, you see options to
                access the accounts manually or programmatically using that permission set. 

Custom implementations might result in different experiences, such as different permission set names. If you're not sure which permission set to use, contact your IT team for help.

Sign in to AWS through your AWS access portal. If your Cloud Administrator
                has granted you `PowerUserAccess` (developer) permissions, you see
                the AWS accounts that you have access to and your permission set. Next to the
                name of your permission set, you see options to access the accounts manually or
                programmatically using that permission set. 

Contact your IT team for help.

## Step 2: Gather your IAM Identity Center information

        After gaining access to AWS, gather your IAM Identity Center information by performing the following:

- 
                Gather your `SSO Start URL`and`SSO Region`values that you need to run`aws configure sso`- 
                        In your AWS access portal, select the permission set you use for development, and select the **Access keys**link.
- 
                        In the **Get credentials**dialog box, choose the tab that matches your operating system.
- 
                        Choose the **IAM Identity Center credentials**method to get the`SSO Start URL`and`SSO Region`values.
 
- 
                        
- 
                Alternatively, starting with version 2.22.0, you can use the new Issuer URL instead of the Start URL. The Issuer URL is located in the AWS IAM Identity Center console in one of the following locations: - 
                        On the **Dashboard**page, the Issuer URL is in the settings summary.
- 
                        On the **Settings**page, the Issuer URL is in the**Identity source**settings.
 
- 
                        
- 
                For information on which scopes value to register, see [OAuth 2.0 Access scopes](https://docs.aws.amazon.com/singlesignon/latest/userguide/customermanagedapps-saml2-oauth2.html#oidc-concept)in the*IAM Identity Center User Guide*.

## Step 3: Create Amazon S3 buckets

        Sign in to the AWS Management Console and open the Amazon S3 console at
         [https://console.aws.amazon.com/s3/](https://console.aws.amazon.com/s3/).

For this tutorial, create a few buckets to be later retrieved in a list.

## Step 4: Install the AWS CLI

        Install the AWS CLI following the instructions for your operating system. For more
            information, see [Installing or updating to the latest version of the AWS CLI](./getting-started-install.html).

Once installed, you can verify the installation by opening your preferred terminal and running the following command. This should display your installed version of the AWS CLI.

`$ ``aws --version`## Step 5: Configure your AWS CLI profile

        Configure your profile using one of the following methods

The `sso-session` section of the `config` file
                    is used to group configuration variables for acquiring SSO access tokens, which
                    can then be used to acquire AWS credentials. The following settings are
                    used:

- 
                        **(Required)**[sso_start_url](./cli-configure-files.html#cli-config-sso_start_url)
- 
                        **(Required)**[sso_region](./cli-configure-files.html#cli-config-sso_region)

You define an `sso-session` section and associate it to a profile.
                    The `sso_region` and `sso_start_url` settings must be set
                    within the `sso-session` section. Typically,
                        `sso_account_id` and `sso_role_name` must be set in
                    the `profile` section so that the SDK can request SSO credentials. 

The following example configures the SDK to request SSO credentials and supports automated token refresh:

`$ ``aws configure sso`
`SSO session name (Recommended): ``my-sso``SSO start URL [None]: ``https://my-sso-portal.awsapps.com/start``SSO region [None]: ``us-east-1``SSO registration scopes [None]: ``sso:account:access`For dual-stack support, you can use the dual-stack SSO start URL format:

`$ ``aws configure sso`
`SSO session name (Recommended): ``my-sso``SSO start URL [None]: ``https://ssoins-1234567890abcdef.portal.us-east-1.app.aws``SSO region [None]: ``us-east-1``SSO registration scopes [None]: ``sso:account:access`Proof Key for Code Exchange (PKCE) authorization is used by default for the
                    AWS CLI starting with version 2.22.0 and must be used on devices with a browser.
                    To continue to use Device authorization, append the
                        `--use-device-code` option.

`$ ``aws configure sso ``--use-device-code`The `sso-session` section of the `config` file
                    is used to group configuration variables for acquiring SSO access tokens, which
                    can then be used to acquire AWS credentials. The following settings are
                    used:

- 
                        **(Required)**[sso_start_url](./cli-configure-files.html#cli-config-sso_start_url)
- 
                        **(Required)**[sso_region](./cli-configure-files.html#cli-config-sso_region)

You define an `sso-session` section and associate it to a profile.
                        `sso_region` and `sso_start_url` must be set within
                    the `sso-session` section. Typically, `sso_account_id` and
                        `sso_role_name` must be set in the `profile` section
                    so that the SDK can request SSO credentials. 

The following example configures the SDK to request SSO credentials and supports automated token refresh:

`[profile``my-dev-profile`] sso_session =`my-sso`sso_account_id =`111122223333`sso_role_name =`SampleRole`[sso-session`my-sso`] sso_region =`us-east-1`sso_start_url =`https://my-sso-portal.awsapps.com/start`sso_registration_scopes =`sso:account:access`

For dual-stack support, use the dual-stack SSO start URL format:

`[profile``my-dev-profile`] sso_session =`my-sso`sso_account_id =`111122223333`sso_role_name =`SampleRole`[sso-session`my-sso`] sso_region =`us-east-1`sso_start_url =`https://ssoins-1234567890abcdef.portal.us-east-1.app.aws`sso_registration_scopes =`sso:account:access`

The authentication token is cached to disk under the
                        `~/.aws/sso/cache` directory with a filename based on the
                    session name. 

## Step 6: Log in to IAM Identity Center

        ###### Note

The sign in process may prompt you to allow the AWS CLI access to your data. Since
                the AWS CLI is built on top of the SDK for Python, permission messages may contain
                variations of the `botocore` name.

To retrieve and cache your IAM Identity Center credentials, run the following command for the AWS CLI to open your default browser and verify your IAM Identity Center log in.

`$ ``aws sso login --profile ``my-dev-profile`Starting with version 2.22.0, PKCE authorization is the default. To use device
            authorization for signing in, add the `--use-device-code` option.

`$ ``aws sso login --profile ``my-dev-profile` --use-device-code## Step 7: Run Amazon S3 commands

        To list the buckets you created earlier, use the [ aws s3
                ls](https://docs.aws.amazon.com/cli/latest/reference/s3/ls.html) command. The following example lists all of your Amazon S3
            buckets.

`$``aws s3 ls``2018-12-11 17:08:50 my-bucket 2018-12-14 14:55:44 my-bucket2`

## Step 8: Log out of IAM Identity Center

        When you are done using your IAM Identity Center profile, run the following command to delete your cached credentials.

`$``aws sso logout``Successfully signed out of all SSO profiles.`

## Step 9: Clean up resources

        After you're done with this tutorial, clean up any resources you created during this tutorial that you no longer need, including Amazon S3 buckets.

## Troubleshooting

        If you come across issues using the AWS CLI, see [Troubleshooting errors for the AWS CLI](./cli-chap-troubleshooting.html) for common troubleshooting steps.

## Additional resources

        Additional resources are as follows.

- 
                [Configuring IAM Identity Center authentication with the AWS CLI](./cli-configure-sso.html)
- 
                `aws configure sso`*AWS CLI version 2 Reference*
- 
                `aws configure sso-session`*AWS CLI version 2 Reference*
- 
                `aws sso login`*AWS CLI version 2 Reference*
- 
                `aws sso logout`*AWS CLI version 2 Reference*
- 
                [Setting up to use the AWS CLI with CodeCatalyst](https://docs.aws.amazon.com/codecatalyst/latest/userguide/set-up-cli.html)in the*Amazon CodeCatalyst User Guide*
- 
                [OAuth 2.0 Access scopes](https://docs.aws.amazon.com/singlesignon/latest/userguide/customermanagedapps-saml2-oauth2.html#oidc-concept)in the*IAM Identity Center User Guide*
- 
                [Getting started tutorials](https://docs.aws.amazon.com/singlesignon/latest/userguide/tutorials.html)in the*IAM Identity Center User Guide*