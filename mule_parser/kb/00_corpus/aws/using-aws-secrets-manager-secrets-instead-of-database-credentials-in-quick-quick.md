# Using AWS Secrets Manager secrets instead of database credentials in Quick - Amazon Quick

**Source:** [https://docs.aws.amazon.com/quick/latest/userguide/secrets-manager-integration.html](https://docs.aws.amazon.com/quick/latest/userguide/secrets-manager-integration.html)

---

| Intended audience: Amazon Quick Administrators and Amazon Quick developers | 

AWS Secrets Manager is a secret storage service that you can use to protect database
            credentials, API keys, and other secret information. Using a key helps you ensure that
            the secret can't be compromised by someone examining your code, because the secret isn't
            stored in the code. For an overview, see the [AWS Secrets Manager User Guide](https://docs.aws.amazon.com/secretsmanager/latest/userguide).

Quick administrators can grant Amazon Quick read-only access to secrets they create in Secrets Manager. These secrets can be used in place of database credentials when creating and editing data sources using the Quick API.

Quick supports using secrets with data source types that support credential pair authentication. Jira and ServiceNow are not currently supported.

###### Note

If you use AWS Secrets Manager with Quick, you are billed for access and
                maintenance as described in the [AWS Secrets Manager Pricing
                page](https://aws.amazon.com/secrets-manager/pricing). In your billing statement, the costs are itemized under Secrets Manager and not
                under Amazon Quick.

Use the procedures described in the following sections to integrate Secrets Manager with Amazon Quick.

###### Topics

## Granting Amazon Quick access to Secrets Manager and selected secrets

            If you're an administrator and you have secrets in Secrets Manager, you can grant Amazon Quick read-only access to selected secrets.

###### To grant Amazon Quick access to Secrets Manager and selected secrets

- 
                    In Amazon Quick, choose your user icon on the upper right, and then choose **Manage Quick**.
- 
                    Choose **Security & permissions**on the left.
- 
                    Choose **Manage**in**Amazon Quick access to AWS resources**.
- 
                    In **Allow access and autodiscovery for these resources**, choose**AWS Secrets Manager**,**Select secrets**.The **AWS Secrets Manager secrets**page opens.
- 
                    Select the secrets that you want to grant Amazon Quick read-only access to. Secrets in your Amazon Quick sign-up Region are shown automatically. To select secrets outside your home Region, choose **Secrets in Other AWS Regions**, and then enter the Amazon Resource Names (ARNs) for those secrets.
- 
                    When you're done, choose **Finish**.Amazon Quick creates an IAM role called `aws-quicksight-secretsmanager-role-v0`in your account. It grants users in the account read-only access to the specified secrets and looks similar to the following:When Amazon Quick users create analyses from or view dashboards that use a data source with secrets, Amazon Quick assumes this Secrets Manager IAM role. For more information about secret permissions policies, see [Authentication and access control for AWS Secrets Manager](https://docs.aws.amazon.com/secretsmanager/latest/userguide/auth-and-access.html)in the*AWS Secrets Manager User Guide*.The specified secret in the Amazon Quick IAM role may have an additional resource policy that denies access. For more information, see [Attach a permissions policy to a secret](https://docs.aws.amazon.com/secretsmanager/latest/userguide/auth-and-access_resource-policies.html)in the*AWS Secrets Manager User Guide*.If you're using an AWS managed AWS KMS key to encrypt your secret, Amazon Quick doesn't require any additional permissions setup in Secrets Manager. If you're using a customer managed key to encrypt your secret, ensure that the Amazon Quick IAM role, `aws-quicksight-secretsmanager-role-v0`has`kms:Decrypt`permissions. For more information, see[Permissions for the KMS key](https://docs.aws.amazon.com/secretsmanager/latest/userguide/security-encryption.html#security-encryption-authz)in the*AWS Secrets Manager User Guide*.For more information about the types of keys used in AWS Key Management Service, see [Customer keys and AWS keys](https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#key-mgmt)in the*AWS Key Management Service guide*.

## Creating or updating a data source with secret credentials using the Amazon Quick API

            After the Amazon Quick administrator has granted Amazon Quick read-only access to Secrets Manager, you can create and update data sources in the API using a secret the administrator selected as credentials.

Following is an example API call to create a data source in Amazon Quick. This
                example uses the `create-data-source` API operation. You can also use the
                    `update-data-source` operation. For more information, see [CreateDataSource](https://docs.aws.amazon.com/quicksight/latest/APIReference/API_CreateDataSource.html) and [UpdateDataSource](https://docs.aws.amazon.com/quicksight/latest/APIReference/API_UpdateDataSource.html) in the *Amazon Quick API Reference*.

The user specified in the permissions in the following API call example can delete, view, and edit data sources for the specified MySQL data source in Amazon Quick. They can also view and update the data source permissions. Instead of a Amazon Quick username and password, a secret ARN is used as credentials for the data source.

`aws quicksight create-data-source --aws-account-id``AWSACCOUNTID`\ --data-source-id`DATASOURCEID`\ --name`NAME`\ --type`MYSQL`\ --permissions '[{"Principal": "arn:aws:quicksight:`region`:`accountID`:user/namespace/`username`", "Actions": ["quicksight:DeleteDataSource", "quicksight:DescribeDataSource", "quicksight:DescribeDataSourcePermissions", "quicksight:PassDataSource", "quicksight:UpdateDataSource", "quicksight:UpdateDataSourcePermissions"]}]' \ --data-source-parameters='{"MySQLParameters":{"Database": "`database`", "Host":"`hostURL`", "Port":"`port`"}}' \ --credentials='{"SecretArn":"arn:aws:secretsmanager:`region`:`accountID`:secret:`secretname`"}' \ --region`us-west-2`

In this call, Amazon Quick authorizes `secretsmanager:GetSecretValue`
                access to the secret based on the API caller's IAM policy, not the IAM service
                role's policy. The IAM service role acts on the account level and is used when an
                analysis or dashboard is viewed by a user. It cannot be used to authorize secret
                access when a user creates or updates the data source. 

When they edit a data source in the Amazon Quick UI, users can view the secret ARN
                for data sources that use AWS Secrets Manager as the credential type. However, they can't edit
                the secret, or select a different secret. If they need to make changes, for example
                to the database server or port, users first need to choose **Credential
                    pair** and enter their Amazon Quick account username and
                password.

Secrets are automatically removed from a data source when the data source is
                altered in the UI. To restore the secret to the data source, use the
                    `update-data-source` API operation.

## What's in the secret

            Amazon Quick requires the following JSON format to access your secret:

```
{
  "username": "
```
`username`",
  "password": "`password`"
}The `username` and `password` fields are required for
                Amazon Quick to access secrets. All other fields are optional and are ignored by
                Amazon Quick.

The JSON format may vary depending on the type of database. For more information,
                see [JSON
                    structure of AWS Secrets Manager database credential secrets](https://docs.aws.amazon.com/secretsmanager/latest/userguide/reference_secret_json_structure.html) in the
                    *AWS Secrets Manager User Guide*.

## Modify a secret

            To modify a secret, you use Secrets Manager. After you make changes to a secret, the updates become available the next time Amazon Quick requests access to the secret.