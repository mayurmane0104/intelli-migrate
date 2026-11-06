# Setting up IdP federation using IAM and Amazon Quick - Amazon Quick

**Source:** [https://docs.aws.amazon.com/quick/latest/userguide/external-identity-providers-setting-up-saml.html](https://docs.aws.amazon.com/quick/latest/userguide/external-identity-providers-setting-up-saml.html)

---

| Applies
                    to:Enterprise Edition and Standard Edition | 

| Intended audience: System administrators | 

###### Note

IAM identity federation doesn't support syncing identity provider groups with Amazon Quick.

You can use an AWS Identity and Access Management (IAM) role and a relay state URL to configure an identity provider (IdP) that is compliant with SAML 2.0. The role grants users permissions to access Amazon Quick. The relay state is the portal that the user is forwarded to, after successful authentication by AWS.

###### Topics

## Prerequisites

            Before configuring your SAML 2.0 connection, do the following:

- 
                    Configure your IdP to establish a trust relationship with AWS: - 
                            Inside your organization's network, configure your identity store, such as Windows Active Directory, to work with a SAML-based IdP. SAML-based IdPs include Active Directory Federation Services, Shibboleth, and so on. 
- 
                            Using your IdP, generate a metadata document that describes your organization as an identity provider. 
- 
                            Set up SAML 2.0 authentication, using the same steps as for the AWS Management Console. When this process is complete, you can configure your relay state to match the relay state of Quick. For more information, see [Configure the relay state of your federation](https://docs.aws.amazon.com/quicksight/latest/user/external-identity-providers-setting-up-saml.html#external-identity-providers-relay-state).
 
- 
                            
- 
                    Create an Amazon Quick account and note the name to use when you configure your IAM policy and IdP. For more information on creating an Amazon Quick account, see [Signing up for an Amazon Quick subscription](https://docs.aws.amazon.com/quicksight/latest/user/signing-up.html).

After you create the setup to federate to the AWS Management Console as outlined in the tutorial, you can edit the relay state provided in the tutorial. You do so with the relay state of Amazon Quick, described in step 5 following.

For more information, see the following resources:

- 
                    [Integrating Third-Party SAML Solution Providers with AWS](https://docs.aws.amazon.com/singlesignon/latest/userguide/)in the*IAM User Guide*.
- 
                    [Troubleshooting SAML 2.0 federation with AWS](https://docs.aws.amazon.com/IAM/latest/UserGuide/troubleshoot_saml.html), also in the*IAM User Guide*.
- 
                    [Setting up trust between ADFS and AWS and using Active Directory credentials to connect to Amazon Athena with ODBC driver](https://aws.amazon.com/blogs/big-data/setting-up-trust-between-adfs-and-aws-and-using-active-directory-credentials-to-connect-to-amazon-athena-with-odbc-driver/)– This walkthrough article is helpful, although you don't need to set up Athena in order to use Amazon Quick.

## Step 1: Create a SAML provider in AWS

            Your SAML identity provider defines your organization's IdP to AWS. It does so by using the metadata document that you previously generated using your IdP.

###### To create a SAML provider in AWS

- Sign in to the AWS Management Console and open the IAM console at - [https://console.aws.amazon.com/iam/](https://console.aws.amazon.com/iam/).
- 
                    Create a new SAML provider, which is an entity in IAM that holds information about your organization's identity provider. For more information, see [Creating SAML Identity Providers](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_providers_create_saml.html)in the*IAM User Guide*.
- 
                    As part of this process, upload the metadata document produced by the IdP software in your organization noted in the previous section. 

## Step 2: Configure permissions in AWS for your federated users

            Next, create an IAM role that establishes a trust relationship between IAM and
                your organization's IdP. This role identifies your IdP as a principal (trusted
                entity) for the purposes of federation. The role also defines which users
                authenticated by your organization's IdP are allowed to access Amazon Quick. For
                more information about creating a role for a SAML IdP, see [Creating a Role for SAML 2.0 Federation](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_create_for-idp_saml.html) in the
                    *IAM User Guide*.

After you have created the role, you can limit the role to have permissions only to Amazon Quick by attaching an inline policy to the role. The following sample policy document provides access to Amazon Quick. This policy allows the user access to Amazon Quick and allows them to create both author accounts and reader accounts.

###### Note

In the following example, replace
                        `<YOUR_AWS_ACCOUNT_ID>` with your 12-digit
                    AWS account ID (with no hyphens ‘‐’).

```
    {
    "Statement": [
        {
            "Action": [
                "quicksight:CreateUser"
            ],
            "Effect": "Allow",
            "Resource": [
                "arn:aws:quicksight::
```
`<YOUR_AWS_ACCOUNT_ID>`:user/${aws:userid}"
            ]
        }
    ],
    "Version": "2012-10-17"
    }
    If you want to provide access to Amazon Quick and also the ability to create Amazon Quick admins, authors (standard users), and readers, you can use the following policy example.

```
    {
    "Statement": [
        {
            "Action": [
                "quicksight:CreateAdmin"
            ],
            "Effect": "Allow",
            "Resource": [
                "arn:aws:quicksight::
```
`<YOUR_AWS_ACCOUNT_ID>`:user/${aws:userid}"
            ]
        }
    ],
    "Version": "2012-10-17"
    }
                You can view account details in the AWS Management Console.

After you have set up SAML and the IAM policy or policies, you don't need to
                invite users manually. The first time that users open Amazon Quick, they are
                provisioned automatically, using the highest level permissions in the policy. For
                example, if they have permissions to both `quicksight:CreateUser` and
                    `quicksight:CreateReader`, they are provisioned as authors. If they
                also have permissions to `quicksight:CreateAdmin`, they are provisioned
                as admins. Each permission level includes the ability to create the same level user
                and below. For example, an author can add other authors or readers. 

Users who are invited manually are created in the role assigned by the person who invited them. They don't need to have policies that grant them permissions.

## Step 3: Configure the SAML IdP

            After you create the IAM role, update your SAML IdP about AWS as a service
                provider. To do so, install the `saml-metadata.xml` file found at
                    [https://signin.aws.amazon.com/static/saml-metadata.xml](https://signin.aws.amazon.com/static/saml-metadata.xml). 

To update the IdP metadata, see the instructions provided by your IdP. Some providers give you the option to type the URL, after which the IdP gets and installs the file for you. Others require you to download the file from the URL and then provide it as a local file.

For more information, see your IdP documentation.

## Step 4: Create assertions for the SAML authentication response

            Next, configure the information that the IdP passes as SAML attributes to AWS as
                part of the authentication response. For more information, see [Configuring SAML Assertions for the Authentication Response](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_providers_create_saml_assertions.html) in the
                    *IAM User Guide*.

## Step 5: Configure the relay state of your federation

            Finally, configure the relay state of your federation to point to the Amazon Quick relay state URL. After successful authentication by AWS, the user is directed to Amazon Quick, defined as the relay state in the SAML authentication response.

The relay state URL for Amazon Quick is as follows.

`https://quicksight.aws.amazon.com`