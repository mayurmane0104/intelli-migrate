# Secrets Manager examples using AWS CLI - AWS Command Line Interface

**Source:** [https://docs.aws.amazon.com/cli/latest/userguide/cli_secrets-manager_code_examples.html](https://docs.aws.amazon.com/cli/latest/userguide/cli_secrets-manager_code_examples.html)

---

The following code examples show you how to perform actions and implement common scenarios by using the AWS Command Line Interface with Secrets Manager.

*Actions* are code excerpts from larger programs and must be run in context. While actions show you how to call individual service functions, you can see actions in context in their related scenarios.

Each example includes a link to the complete source code, where you can find instructions on how to set up and run the code in context.

###### Topics

## Actions

    The following code example shows how to use `batch-get-secret-value`.

- **AWS CLI**
- 
            
                    **Example 1: To retrieve the secret value for a group of secrets listed by name**The following `batch-get-secret-value`example gets the secret value secrets for three secrets.`aws secretsmanager batch-get-secret-value \ --secret-id-list``MySecret1``MySecret2``MySecret3`Output: `{ "SecretValues": [ { "ARN": "arn:aws:secretsmanager:us-west-2:123456789012:secret:MySecret1-a1b2c3", "Name": "MySecret1", "VersionId": "a1b2c3d4-5678-90ab-cdef-EXAMPLEaaaaa", "SecretString": "{\"username\":\"diego_ramirez\",\"password\":\"EXAMPLE-PASSWORD\",\"engine\":\"mysql\",\"host\":\"secretsmanagertutorial.cluster.us-west-2.rds.amazonaws.com\",\"port\":3306,\"dbClusterIdentifier\":\"secretsmanagertutorial\"}", "VersionStages": [ "AWSCURRENT" ], "CreatedDate": "1523477145.729" }, { "ARN": "arn:aws:secretsmanager:us-west-2:123456789012:secret:MySecret2-a1b2c3", "Name": "MySecret2", "VersionId": "a1b2c3d4-5678-90ab-cdef-EXAMPLEbbbbb", "SecretString": "{\"username\":\"akua_mansa\",\"password\":\"EXAMPLE-PASSWORD\"", "VersionStages": [ "AWSCURRENT" ], "CreatedDate": "1673477781.275" }, { "ARN": "arn:aws:secretsmanager:us-west-2:123456789012:secret:MySecret3-a1b2c3", "Name": "MySecret3", "VersionId": "a1b2c3d4-5678-90ab-cdef-EXAMPLEccccc", "SecretString": "{\"username\":\"jie_liu\",\"password\":\"EXAMPLE-PASSWORD\"", "VersionStages": [ "AWSCURRENT" ], "CreatedDate": "1373477721.124" } ], "Errors": [] }`For more information, see [Retrieve a group of secrets in a batch](https://docs.aws.amazon.com/secretsmanager/latest/userguide/retrieving-secrets_batch.html)in the*AWS Secrets Manager User Guide*.**Example 2: To retrieve the secret value for a group of secrets selected by filter**The following `batch-get-secret-value`example gets the secret value secrets in your account that have`MySecret`in the name. Filtering by name is case sensitive.`aws secretsmanager batch-get-secret-value \ --filters Key="name",Values="MySecret"`Output: `{ "SecretValues": [ { "ARN": "arn:aws:secretsmanager:us-west-2:123456789012:secret:MySecret1-a1b2c3", "Name": "MySecret1", "VersionId": "a1b2c3d4-5678-90ab-cdef-EXAMPLEaaaaa", "SecretString": "{\"username\":\"diego_ramirez\",\"password\":\"EXAMPLE-PASSWORD\",\"engine\":\"mysql\",\"host\":\"secretsmanagertutorial.cluster.us-west-2.rds.amazonaws.com\",\"port\":3306,\"dbClusterIdentifier\":\"secretsmanagertutorial\"}", "VersionStages": [ "AWSCURRENT" ], "CreatedDate": "1523477145.729" }, { "ARN": "arn:aws:secretsmanager:us-west-2:123456789012:secret:MySecret2-a1b2c3", "Name": "MySecret2", "VersionId": "a1b2c3d4-5678-90ab-cdef-EXAMPLEbbbbb", "SecretString": "{\"username\":\"akua_mansa\",\"password\":\"EXAMPLE-PASSWORD\"", "VersionStages": [ "AWSCURRENT" ], "CreatedDate": "1673477781.275" }, { "ARN": "arn:aws:secretsmanager:us-west-2:123456789012:secret:MySecret3-a1b2c3", "Name": "MySecret3", "VersionId": "a1b2c3d4-5678-90ab-cdef-EXAMPLEccccc", "SecretString": "{\"username\":\"jie_liu\",\"password\":\"EXAMPLE-PASSWORD\"", "VersionStages": [ "AWSCURRENT" ], "CreatedDate": "1373477721.124" } ], "Errors": [] }`For more information, see [Retrieve a group of secrets in a batch](https://docs.aws.amazon.com/secretsmanager/latest/userguide/retrieving-secrets_batch.html)in the*AWS Secrets Manager User Guide*.- 
                    For API details, see [BatchGetSecretValue](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/secretsmanager/batch-get-secret-value.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `cancel-rotate-secret`.

- **AWS CLI**
- 
            
                    **To turn off automatic rotation for a secret**The following `cancel-rotate-secret`example turns off automatic rotation for a secret. To resume rotation, call`rotate-secret`.`aws secretsmanager cancel-rotate-secret \ --secret-id``MyTestSecret`Output: `{ "ARN": "arn:aws:secretsmanager:us-west-2:123456789012:secret:MyTestSecret-a1b2c3", "Name": "MyTestSecret" }`For more information, see [Rotate a secret](https://docs.aws.amazon.com/secretsmanager/latest/userguide/rotating-secrets.html)in the*Secrets Manager User Guide*.- 
                    For API details, see [CancelRotateSecret](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/secretsmanager/cancel-rotate-secret.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `create-secret`.

- **AWS CLI**
- 
            
                    **Example 1: To create a secret from credentials in a JSON file**The following `create-secret`example creates a secret from credentials in a file. For more information, see[Loading AWS CLI parameters from a file](https://docs.aws.amazon.com/cli/latest/userguide/cli-usage-parameters-file.html)in the*AWS CLI User Guide*.`aws secretsmanager create-secret \ --name``MyTestSecret`\ --secret-string`file://mycreds.json`Contents of `mycreds.json`:`{ "engine": "mysql", "username": "saanvis", "password": "EXAMPLE-PASSWORD", "host": "my-database-endpoint.us-west-2.rds.amazonaws.com", "dbname": "myDatabase", "port": "3306" }`Output: `{ "ARN": "arn:aws:secretsmanager:us-west-2:123456789012:secret:MyTestSecret-a1b2c3", "Name": "MyTestSecret", "VersionId": "a1b2c3d4-5678-90ab-cdef-EXAMPLE11111" }`For more information, see [Create a secret](https://docs.aws.amazon.com/secretsmanager/latest/userguide/manage_create-basic-secret.html)in the*Secrets Manager User Guide*.**Example 2: To create a secret**The following `create-secret`example creates a secret with two key-value pairs. When you enter commands in a command shell, there is a risk of the command history being accessed or utilities having access to your command parameters. This is a concern if the command includes the value of a secret. For more information, see[Mitigate the risks of using command-line tools to store secrets](https://docs.aws.amazon.com/secretsmanager/latest/userguide/security_cli-exposure-risks.html)in the*Secrets Manager User Guide*.`aws secretsmanager create-secret \ --name``MyTestSecret`\ --description`"My test secret created with the CLI."`\ --secret-string "{\"user\":\"diegor\",\"password\":\"EXAMPLE-PASSWORD\"}"Output: `{ "ARN": "arn:aws:secretsmanager:us-west-2:123456789012:secret:MyTestSecret-a1b2c3", "Name": "MyTestSecret", "VersionId": "EXAMPLE1-90ab-cdef-fedc-ba987EXAMPLE" }`For more information, see [Create a secret](https://docs.aws.amazon.com/secretsmanager/latest/userguide/manage_create-basic-secret.html)in the*Secrets Manager User Guide*.- 
                    For API details, see [CreateSecret](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/secretsmanager/create-secret.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `delete-resource-policy`.

- **AWS CLI**
- 
            
                    **To delete the resource-based policy attached to a secret**The following `delete-resource-policy`example deletes the resource-based policy attached to a secret.`aws secretsmanager delete-resource-policy \ --secret-id``MyTestSecret`Output: `{ "ARN": "arn:aws:secretsmanager:us-west-2:123456789012:secret:MyTestSecret-a1b2c3", "Name": "MyTestSecret" }`For more information, see [Authentication and access control](https://docs.aws.amazon.com/secretsmanager/latest/userguide/auth-and-access.html)in the*Secrets Manager User Guide*.- 
                    For API details, see [DeleteResourcePolicy](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/secretsmanager/delete-resource-policy.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `delete-secret`.

- **AWS CLI**
- 
            
                    **Example 1: To delete a secret**The following `delete-secret`example deletes a secret. You can recover the secret with`restore-secret`until the date and time in the`DeletionDate`response field. To delete a secret that is replicated to other regions, first remove its replicas with`remove-regions-from-replication`, and then call`delete-secret`.`aws secretsmanager delete-secret \ --secret-id``MyTestSecret`\ --recovery-window-in-days`7`Output: `{ "ARN": "arn:aws:secretsmanager:us-west-2:123456789012:secret:MyTestSecret-a1b2c3", "Name": "MyTestSecret", "DeletionDate": 1524085349.095 }`For more information, see [Delete a secret](https://docs.aws.amazon.com/secretsmanager/latest/userguide/manage_delete-secret.html)in the*Secrets Manager User Guide*.**Example 2: To delete a secret immediately**The following `delete-secret`example deletes a secret immediately without a recovery window. You can't recover this secret.`aws secretsmanager delete-secret \ --secret-id``MyTestSecret`\ --force-delete-without-recoveryOutput: `{ "ARN": "arn:aws:secretsmanager:us-west-2:123456789012:secret:MyTestSecret-a1b2c3", "Name": "MyTestSecret", "DeletionDate": 1508750180.309 }`For more information, see [Delete a secret](https://docs.aws.amazon.com/secretsmanager/latest/userguide/manage_delete-secret.html)in the*Secrets Manager User Guide*.- 
                    For API details, see [DeleteSecret](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/secretsmanager/delete-secret.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `describe-secret`.

- **AWS CLI**
- 
            
                    **To retrieve the details of a secret**The following `describe-secret`example shows the details of a secret.`aws secretsmanager describe-secret \ --secret-id``MyTestSecret`Output: `{ "ARN": "arn:aws:secretsmanager:us-west-2:123456789012:secret:MyTestSecret-Ca8JGt", "Name": "MyTestSecret", "Description": "My test secret", "KmsKeyId": "arn:aws:kms:us-west-2:123456789012:key/EXAMPLE1-90ab-cdef-fedc-ba987EXAMPLE", "RotationEnabled": true, "RotationLambdaARN": "arn:aws:lambda:us-west-2:123456789012:function:MyTestRotationLambda", "RotationRules": { "AutomaticallyAfterDays": 2, "Duration": "2h", "ScheduleExpression": "cron(0 16 1,15 * ? *)" }, "LastRotatedDate": 1525747253.72, "LastChangedDate": 1523477145.729, "LastAccessedDate": 1524572133.25, "Tags": [ { "Key": "SecondTag", "Value": "AnotherValue" }, { "Key": "FirstTag", "Value": "SomeValue" } ], "VersionIdsToStages": { "a1b2c3d4-5678-90ab-cdef-EXAMPLE11111": [ "AWSPREVIOUS" ], "a1b2c3d4-5678-90ab-cdef-EXAMPLE22222": [ "AWSCURRENT" ], "a1b2c3d4-5678-90ab-cdef-EXAMPLE33333": [ "AWSPENDING" ] }, "CreatedDate": 1521534252.66, "PrimaryRegion": "us-west-2", "ReplicationStatus": [ { "Region": "eu-west-3", "KmsKeyId": "alias/aws/secretsmanager", "Status": "InSync", "StatusMessage": "Replication succeeded" } ] }`For more information, see [Secret](https://docs.aws.amazon.com/secretsmanager/latest/userguide/getting-started.html#term_secret)in the*Secrets Manager User Guide*.- 
                    For API details, see [DescribeSecret](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/secretsmanager/describe-secret.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `get-random-password`.

- **AWS CLI**
- 
            
                    **To generate a random password**The following `get-random-password`example generates a random password 20 characters long that includes at least one uppercase letter, lowercase letter, number, and punctuation.`aws secretsmanager get-random-password \ --require-each-included-type \ --password-length``20`Output: `{ "RandomPassword": "EXAMPLE-PASSWORD" }`For more information, see [Create and manage secrets](https://docs.aws.amazon.com/secretsmanager/latest/userguide/managing-secrets.html)in the*Secrets Manager User Guide*.- 
                    For API details, see [GetRandomPassword](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/secretsmanager/get-random-password.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `get-resource-policy`.

- **AWS CLI**
- 
            
                    **To retrieve the resource-based policy attached to a secret**The following `get-resource-policy`example retrieves the resource-based policy attached to a secret.`aws secretsmanager get-resource-policy \ --secret-id``MyTestSecret`Output: `{ "ARN": "arn:aws:secretsmanager:us-west-2:123456789012:secret:MyTestSecret-a1b2c3", "Name": "MyTestSecret", "ResourcePolicy": "{\n\"Version\":\"2012-10-17\",\n\"Statement\":[{\n\"Effect\":\"Allow\",\n \"Principal\":{\n\"AWS\":\"arn:aws:iam::123456789012:root\"\n},\n\"Action\": \"secretsmanager:GetSecretValue\",\n\"Resource\":\"*\"\n}]\n}" }`For more information, see [Authentication and access control](https://docs.aws.amazon.com/secretsmanager/latest/userguide/auth-and-access.html)in the*Secrets Manager User Guide*.- 
                    For API details, see [GetResourcePolicy](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/secretsmanager/get-resource-policy.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `get-secret-value`.

- **AWS CLI**
- 
            
                    **Example 1: To retrieve the encrypted secret value of a secret**The following `get-secret-value`example gets the current secret value.`aws secretsmanager get-secret-value \ --secret-id``MyTestSecret`Output: `{ "ARN": "arn:aws:secretsmanager:us-west-2:123456789012:secret:MyTestSecret-a1b2c3", "Name": "MyTestSecret", "VersionId": "a1b2c3d4-5678-90ab-cdef-EXAMPLE11111", "SecretString": "{\"user\":\"diegor\",\"password\":\"EXAMPLE-PASSWORD\"}", "VersionStages": [ "AWSCURRENT" ], "CreatedDate": 1523477145.713 }`For more information, see [Retrieve a secret](https://docs.aws.amazon.com/secretsmanager/latest/userguide/retrieving-secrets.html)in the*Secrets Manager User Guide*.**Example 2: To retrieve the previous secret value**The following `get-secret-value`example gets the previous secret value.:`aws secretsmanager get-secret-value \ --secret-id``MyTestSecret`--version-stage`AWSPREVIOUS`Output: `{ "ARN": "arn:aws:secretsmanager:us-west-2:123456789012:secret:MyTestSecret-a1b2c3", "Name": "MyTestSecret", "VersionId": "a1b2c3d4-5678-90ab-cdef-EXAMPLE22222", "SecretString": "{\"user\":\"diegor\",\"password\":\"PREVIOUS-EXAMPLE-PASSWORD\"}", "VersionStages": [ "AWSPREVIOUS" ], "CreatedDate": 1523477145.713 }`For more information, see [Retrieve a secret](https://docs.aws.amazon.com/secretsmanager/latest/userguide/retrieving-secrets.html)in the*Secrets Manager User Guide*.- 
                    For API details, see [GetSecretValue](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/secretsmanager/get-secret-value.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `list-secret-version-ids`.

- **AWS CLI**
- 
            
                    **To list all of the secret versions associated with a secret**The following `list-secret-version-ids`example gets a list of all of the versions of a secret.`aws secretsmanager list-secret-version-ids \ --secret-id``MyTestSecret`Output: `{ "Versions": [ { "VersionId": "a1b2c3d4-5678-90ab-cdef-EXAMPLE11111", "VersionStages": [ "AWSPREVIOUS" ], "LastAccessedDate": 1523477145.713, "CreatedDate": 1523477145.713 }, { "VersionId": "a1b2c3d4-5678-90ab-cdef-EXAMPLE22222", "VersionStages": [ "AWSCURRENT" ], "LastAccessedDate": 1523477145.713, "CreatedDate": 1523486221.391 }, { "CreatedDate": 1.51197446236E9, "VersionId": "a1b2c3d4-5678-90ab-cdef-EXAMPLE33333;" } ], "ARN": "arn:aws:secretsmanager:us-west-2:123456789012:secret:MyTestSecret-a1b2c3", "Name": "MyTestSecret" }`For more information, see [Version](https://docs.aws.amazon.com/secretsmanager/latest/userguide/getting-started.html#term_version)in the*Secrets Manager User Guide*.- 
                    For API details, see [ListSecretVersionIds](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/secretsmanager/list-secret-version-ids.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `list-secrets`.

- **AWS CLI**
- 
            
                    **Example 1: To list the secrets in your account**The following `list-secrets`example gets a list of the secrets in your account.`aws secretsmanager list-secrets`Output: `{ "SecretList": [ { "ARN": "arn:aws:secretsmanager:us-west-2:123456789012:secret:MyTestSecret-a1b2c3", "Name": "MyTestSecret", "LastChangedDate": 1523477145.729, "SecretVersionsToStages": { "a1b2c3d4-5678-90ab-cdef-EXAMPLE11111": [ "AWSCURRENT" ] } }, { "ARN": "arn:aws:secretsmanager:us-west-2:123456789012:secret:AnotherSecret-d4e5f6", "Name": "AnotherSecret", "LastChangedDate": 1523482025.685, "SecretVersionsToStages": { "a1b2c3d4-5678-90ab-cdef-EXAMPLE22222": [ "AWSCURRENT" ] } } ] }`For more information, see [Find a secret](https://docs.aws.amazon.com/secretsmanager/latest/userguide/manage_search-secret.html)in the*Secrets Manager User Guide*.**Example 2: To filter the list of secrets in your account**The following `list-secrets`example gets a list of the secrets in your account that have`Test`in the name. Filtering by name is case sensitive.`aws secretsmanager list-secrets \ --filter Key="name",Values="Test"`Output: `{ "SecretList": [ { "ARN": "arn:aws:secretsmanager:us-west-2:123456789012:secret:MyTestSecret-a1b2c3", "Name": "MyTestSecret", "LastChangedDate": 1523477145.729, "SecretVersionsToStages": { "a1b2c3d4-5678-90ab-cdef-EXAMPLE11111": [ "AWSCURRENT" ] } } ] }`For more information, see [Find a secret](https://docs.aws.amazon.com/secretsmanager/latest/userguide/manage_search-secret.html)in the*Secrets Manager User Guide*.**Example 3: To list the secrets in your account managed by another service**The following `list-secrets`example returns the secrets in your account that are managed by Amazon RDS.`aws secretsmanager list-secrets \ --filter Key="owning-service",Values="rds"`Output: `{ "SecretList": [ { "Name": "rds!cluster-a1b2c3d4-5678-90ab-cdef-EXAMPLE11111", "Tags": [ { "Value": "arn:aws:rds:us-west-2:123456789012:cluster:database-1", "Key": "aws:rds:primaryDBClusterArn" }, { "Value": "rds", "Key": "aws:secretsmanager:owningService" } ], "RotationRules": { "AutomaticallyAfterDays": 1 }, "LastChangedDate": 1673477781.275, "LastRotatedDate": 1673477781.26, "SecretVersionsToStages": { "a1b2c3d4-5678-90ab-cdef-EXAMPLEaaaaa": [ "AWSPREVIOUS" ], "a1b2c3d4-5678-90ab-cdef-EXAMPLEbbbbb": [ "AWSCURRENT", "AWSPENDING" ] }, "OwningService": "rds", "RotationEnabled": true, "CreatedDate": 1673467300.7, "LastAccessedDate": 1673395200.0, "ARN": "arn:aws:secretsmanager:us-west-2:123456789012:secret:rds!cluster-a1b2c3d4-5678-90ab-cdef-EXAMPLE11111-a1b2c3", "Description": "Secret associated with primary RDS DB cluster: arn:aws:rds:us-west-2:123456789012:cluster:database-1" } ] }`For more information, see [Secrets managed by other services](https://docs.aws.amazon.com/secretsmanager/latest/userguide/service-linked-secrets.html)in the*Secrets Manager User Guide*.- 
                    For API details, see [ListSecrets](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/secretsmanager/list-secrets.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `put-resource-policy`.

- **AWS CLI**
- 
            
                    **To add a resource-based policy to a secret**The following `put-resource-policy`example adds a permissions policy to a secret, checking first that the policy does not provide broad access to the secret. The policy is read from a file. For more information, see[Loading AWS CLI parameters from a file](https://docs.aws.amazon.com/cli/latest/userguide/cli-usage-parameters-file.html)in the*AWS CLI User Guide*.`aws secretsmanager put-resource-policy \ --secret-id``MyTestSecret`\ --resource-policy`file://mypolicy.json`\ --block-public-policyContents of `mypolicy.json`:`{ "Version":"2012-10-17", "Statement": [ { "Effect": "Allow", "Principal": { "AWS": "arn:aws:iam::123456789012:role/MyRole" }, "Action": "secretsmanager:GetSecretValue", "Resource": "*" } ] }`Output: `{ "ARN": "arn:aws:secretsmanager:us-west-2:123456789012:secret:MyTestSecret-a1b2c3", "Name": "MyTestSecret" }`For more information, see [Attach a permissions policy to a secret](https://docs.aws.amazon.com/secretsmanager/latest/userguide/auth-and-access_resource-policies.html)in the*Secrets Manager User Guide*.- 
                    For API details, see [PutResourcePolicy](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/secretsmanager/put-resource-policy.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `put-secret-value`.

- **AWS CLI**
- 
            
                    **Example 1: To store a new secret value in a secret**The following `put-secret-value`example creates a new version of a secret with two key-value pairs.`aws secretsmanager put-secret-value \ --secret-id``MyTestSecret`\ --secret-string "{\"user\":\"diegor\",\"password\":\"EXAMPLE-PASSWORD\"}"Output: `{ "ARN": "arn:aws:secretsmanager:us-west-2:123456789012:secret:MyTestSecret-1a2b3c", "Name": "MyTestSecret", "VersionId": "a1b2c3d4-5678-90ab-cdef-EXAMPLE11111", "VersionStages": [ "AWSCURRENT" ] }`For more information, see [Modify a secret](https://docs.aws.amazon.com/secretsmanager/latest/userguide/manage_update-secret.html)in the*Secrets Manager User Guide*.**Example 2: To store a new secret value from credentials in a JSON file**The following `put-secret-value`example creates a new version of a secret from credentials in a file. For more information, see[Loading AWS CLI parameters from a file](https://docs.aws.amazon.com/cli/latest/userguide/cli-usage-parameters-file.html)in the*AWS CLI User Guide*.`aws secretsmanager put-secret-value \ --secret-id``MyTestSecret`\ --secret-string`file://mycreds.json`Contents of `mycreds.json`:`{ "engine": "mysql", "username": "saanvis", "password": "EXAMPLE-PASSWORD", "host": "my-database-endpoint.us-west-2.rds.amazonaws.com", "dbname": "myDatabase", "port": "3306" }`Output: `{ "ARN": "arn:aws:secretsmanager:us-west-2:123456789012:secret:MyTestSecret-a1b2c3", "Name": "MyTestSecret", "VersionId": "a1b2c3d4-5678-90ab-cdef-EXAMPLE11111", "VersionStages": [ "AWSCURRENT" ] }`For more information, see [Modify a secret](https://docs.aws.amazon.com/secretsmanager/latest/userguide/manage_update-secret.html)in the*Secrets Manager User Guide*.- 
                    For API details, see [PutSecretValue](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/secretsmanager/put-secret-value.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `remove-regions-from-replication`.

- **AWS CLI**
- 
            
                    **To delete a replica secret**The following `remove-regions-from-replication`example deletes a replica secret in eu-west-3. To delete a primary secret that is replicated to other regions, first delete the replicas and then call`delete-secret`.`aws secretsmanager remove-regions-from-replication \ --secret-id``MyTestSecret`\ --remove-replica-regions`eu-west-3`Output: `{ "ARN": "arn:aws:secretsmanager:us-west-2:123456789012:secret:MyTestSecret-1a2b3c", "ReplicationStatus": [] }`For more information, see [Delete a replica secret](https://docs.aws.amazon.com/secretsmanager/latest/userguide/delete-replica.html)in the*Secrets Manager User Guide*.- 
                    For API details, see [RemoveRegionsFromReplication](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/secretsmanager/remove-regions-from-replication.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `replicate-secret-to-regions`.

- **AWS CLI**
- 
            
                    **To replicate a secret to another region**The following `replicate-secret-to-regions`example replicates a secret to eu-west-3. The replica is encrypted with the AWS managed key`aws/secretsmanager`.`aws secretsmanager replicate-secret-to-regions \ --secret-id``MyTestSecret`\ --add-replica-regions`Region=eu-west-3`Output: `{ "ARN": "arn:aws:secretsmanager:us-west-2:123456789012:secret:MyTestSecret-1a2b3c", "ReplicationStatus": [ { "Region": "eu-west-3", "KmsKeyId": "alias/aws/secretsmanager", "Status": "InProgress" } ] }`For more information, see [Replicate a secret to another Region](https://docs.aws.amazon.com/secretsmanager/latest/userguide/replicate-existing-secret.html)in the*Secrets Manager User Guide*.- 
                    For API details, see [ReplicateSecretToRegions](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/secretsmanager/replicate-secret-to-regions.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `restore-secret`.

- **AWS CLI**
- 
            
                    **To restore a previously deleted secret**The following `restore-secret`example restores a secret that was previously scheduled for deletion.`aws secretsmanager restore-secret \ --secret-id``MyTestSecret`Output: `{ "ARN": "arn:aws:secretsmanager:us-west-2:123456789012:secret:MyTestSecret-a1b2c3", "Name": "MyTestSecret" }`For more information, see [Delete a secret](https://docs.aws.amazon.com/secretsmanager/latest/userguide/manage_delete-secret.html)in the*Secrets Manager User Guide*.- 
                    For API details, see [RestoreSecret](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/secretsmanager/restore-secret.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `rotate-secret`.

- **AWS CLI**
- 
            
                    **Example 1: To configure and start automatic rotation for a secret**The following `rotate-secret`example configures and starts automatic rotation for a secret. Secrets Manager rotates the secret once immediately, and then every eight hours in a two hour window. The output shows the`VersionId`of the new secret version created by rotation.`aws secretsmanager rotate-secret \ --secret-id``MyTestDatabaseSecret`\ --rotation-lambda-arn`arn:aws:lambda:us-west-2:1234566789012:function:SecretsManagerTestRotationLambda`\ --rotation-rules "{\"ScheduleExpression\": \"cron(0 8/8 * * ? *)\", \"Duration\": \"2h\"}"Output: `{ "ARN": "aws:arn:secretsmanager:us-west-2:123456789012:secret:MyTestDatabaseSecret-a1b2c3", "Name": "MyTestDatabaseSecret", "VersionId": "a1b2c3d4-5678-90ab-cdef-EXAMPLE11111" }`For more information, see [Rotate secrets](https://docs.aws.amazon.com/secretsmanager/latest/userguide/rotating-secrets.html)in the*Secrets Manager User Guide*.**Example 2: To configure and start automatic rotation on a rotation interval**The following `rotate-secret`example configures and starts automatic rotation for a secret. Secrets Manager rotates the secret once immediately, and then every 10 days. The output shows the`VersionId`of the new secret version created by rotation.`aws secretsmanager rotate-secret \ --secret-id``MyTestDatabaseSecret`\ --rotation-lambda-arn`arn:aws:lambda:us-west-2:1234566789012:function:SecretsManagerTestRotationLambda`\ --rotation-rules "{\"ScheduleExpression\": \"rate(10 days)\"}"Output: `{ "ARN": "aws:arn:secretsmanager:us-west-2:123456789012:secret:MyTestDatabaseSecret-a1b2c3", "Name": "MyTestDatabaseSecret", "VersionId": "a1b2c3d4-5678-90ab-cdef-EXAMPLE11111" }`For more information, see [Rotate secrets](https://docs.aws.amazon.com/secretsmanager/latest/userguide/rotating-secrets.html)in the*Secrets Manager User Guide*.**Example 3: To rotate a secret immediately**The following `rotate-secret`example starts an immediate rotation. The output shows the`VersionId`of the new secret version created by rotation. The secret must already have rotation configured.`aws secretsmanager rotate-secret \ --secret-id``MyTestDatabaseSecret`Output: `{ "ARN": "aws:arn:secretsmanager:us-west-2:123456789012:secret:MyTestDatabaseSecret-a1b2c3", "Name": "MyTestDatabaseSecret", "VersionId": "a1b2c3d4-5678-90ab-cdef-EXAMPLE11111" }`For more information, see [Rotate secrets](https://docs.aws.amazon.com/secretsmanager/latest/userguide/rotating-secrets.html)in the*Secrets Manager User Guide*.- 
                    For API details, see [RotateSecret](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/secretsmanager/rotate-secret.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `stop-replication-to-replica`.

- **AWS CLI**
- 
            
                    **To promote a replica secret to a primary**The following `stop-replication-to-replica`example removes the link between a replica secret to the primary. The replica secret is promoted to a primary secret in the replica region. You must call`stop-replication-to-replica`from within the replica region.`aws secretsmanager stop-replication-to-replica \ --secret-id``MyTestSecret`Output: `{ "ARN": "arn:aws:secretsmanager:us-west-2:123456789012:secret:MyTestSecret-a1b2c3" }`For more information, see [Promote a replica secret](https://docs.aws.amazon.com/secretsmanager/latest/userguide/standalone-secret.html)in the*Secrets Manager User Guide*.- 
                    For API details, see [StopReplicationToReplica](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/secretsmanager/stop-replication-to-replica.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `tag-resource`.

- **AWS CLI**
- 
            
                    **Example 1: To add a tag to a secret**The following example shows how to attach a tag with shorthand syntax. `aws secretsmanager tag-resource \ --secret-id``MyTestSecret`\ --tags`Key=FirstTag,Value=FirstValue`This command produces no output. For more information, see [Tag your secrets](https://docs.aws.amazon.com/secretsmanager/latest/userguide/managing-secrets_tagging.html)in the*Secrets Manager User Guide*.**Example 2: To add multiple tags to a secret**The following `tag-resource`example attaches two key-value tags to a secret.`aws secretsmanager tag-resource \ --secret-id``MyTestSecret`\ --tags '`[{"Key": "FirstTag", "Value": "FirstValue"}, {"Key": "SecondTag", "Value": "SecondValue"}]`'This command produces no output. For more information, see [Tag secrets](https://docs.aws.amazon.com/secretsmanager/latest/userguide/managing-secrets_tagging.html)in the*Secrets Manager User Guide*.- 
                    For API details, see [TagResource](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/secretsmanager/tag-resource.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `untag-resource`.

- **AWS CLI**
- 
            
                    **To remove tags from a secret**The following `untag-resource`example removes two tags from a secret. For each tag, both key and value are removed.`aws secretsmanager untag-resource \ --secret-id``MyTestSecret`\ --tag-keys '`[ "FirstTag", "SecondTag"]`'This command produces no output. For more information, see [Tag secrets](https://docs.aws.amazon.com/secretsmanager/latest/userguide/managing-secrets_tagging.html)in the*Secrets Manager User Guide*.- 
                    For API details, see [UntagResource](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/secretsmanager/untag-resource.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `update-secret-version-stage`.

- **AWS CLI**
- 
            
                    **Example 1: To revert a secret to the previous version**The following `update-secret-version-stage`example moves the AWSCURRENT staging label to the previous version of a secret, which reverts the secret to the previous version. To find the ID for the previous version, use`list-secret-version-ids`. For this example, the version with the AWSCURRENT label is a1b2c3d4-5678-90ab-cdef-EXAMPLE11111 and the version with the AWSPREVIOUS label is a1b2c3d4-5678-90ab-cdef-EXAMPLE22222. In this example, you move the AWSCURRENT label from version 11111 to 22222. Because the AWSCURRENT label is removed from a version,`update-secret-version-stage`automatically moves the AWSPREVIOUS label to that version (11111). The effect is that the AWSCURRENT and AWSPREVIOUS versions are swapped.`aws secretsmanager update-secret-version-stage \ --secret-id``MyTestSecret`\ --version-stage`AWSCURRENT`\ --move-to-version-id`a1b2c3d4-5678-90ab-cdef-EXAMPLE22222`\ --remove-from-version-id`a1b2c3d4-5678-90ab-cdef-EXAMPLE11111`Output: `{ "ARN": "arn:aws:secretsmanager:us-west-2:123456789012:secret:MyTestSecret-a1b2c3", "Name": "MyTestSecret" }`For more information, see [Version](https://docs.aws.amazon.com/secretsmanager/latest/userguide/getting-started.html#term_version)in the*Secrets Manager User Guide*.**Example 2: To add a staging label attached to a version of a secret**The following `update-secret-version-stage`example adds a staging label to a version of a secret. You can review the results by running`list-secret-version-ids`and viewing the`VersionStages`response field for the affected version.`aws secretsmanager update-secret-version-stage \ --secret-id``MyTestSecret`\ --version-stage`STAGINGLABEL1`\ --move-to-version-id`EXAMPLE1-90ab-cdef-fedc-ba987EXAMPLE`Output: `{ "ARN": "arn:aws:secretsmanager:us-west-2:123456789012:secret:MyTestSecret-a1b2c3", "Name": "MyTestSecret" }`For more information, see [Version](https://docs.aws.amazon.com/secretsmanager/latest/userguide/getting-started.html#term_version)in the*Secrets Manager User Guide*.**Example 3: To delete a staging label attached to a version of a secret**The following `update-secret-version-stage`example deletes a staging label that is attached to a version of a secret. You can review the results by running`list-secret-version-ids`and viewing the`VersionStages`response field for the affected version.`aws secretsmanager update-secret-version-stage \ --secret-id``MyTestSecret`\ --version-stage`STAGINGLABEL1`\ --remove-from-version-id`a1b2c3d4-5678-90ab-cdef-EXAMPLE11111`Output: `{ "ARN": "arn:aws:secretsmanager:us-west-2:123456789012:secret:MyTestSecret-a1b2c3", "Name": "MyTestSecret" }`For more information, see [Version](https://docs.aws.amazon.com/secretsmanager/latest/userguide/getting-started.html#term_version)in the*Secrets Manager User Guide*.- 
                    For API details, see [UpdateSecretVersionStage](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/secretsmanager/update-secret-version-stage.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `update-secret`.

- **AWS CLI**
- 
            
                    **Example 1: To update the description of a secret**The following `update-secret`example updates the description of a secret.`aws secretsmanager update-secret \ --secret-id``MyTestSecret`\ --description`"This is a new description for the secret."`Output: `{ "ARN": "arn:aws:secretsmanager:us-west-2:123456789012:secret:MyTestSecret-a1b2c3", "Name": "MyTestSecret" }`For more information, see [Modify a secret](https://docs.aws.amazon.com/secretsmanager/latest/userguide/manage_update-secret.html)in the*Secrets Manager User Guide*.**Example 2: To update the encryption key associated with a secret**The following `update-secret`example updates the KMS key used to encrypt the secret value. The KMS key must be in the same region as the secret.`aws secretsmanager update-secret \ --secret-id``MyTestSecret`\ --kms-key-id`arn:aws:kms:us-west-2:123456789012:key/EXAMPLE1-90ab-cdef-fedc-ba987EXAMPLE`Output: `{ "ARN": "arn:aws:secretsmanager:us-west-2:123456789012:secret:MyTestSecret-a1b2c3", "Name": "MyTestSecret" }`For more information, see [Modify a secret](https://docs.aws.amazon.com/secretsmanager/latest/userguide/manage_update-secret.html)in the*Secrets Manager User Guide*.- 
                    For API details, see [UpdateSecret](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/secretsmanager/update-secret.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `validate-resource-policy`.

- **AWS CLI**
- 
            
                    **To validate a resource policy**The following `validate-resource-policy`example checks that a resource policy doesn't grant broad access to a secret. The policy is read from a file on disk. For more information, see[Loading AWS CLI parameters from a file](https://docs.aws.amazon.com/cli/latest/userguide/cli-usage-parameters-file.html)in the*AWS CLI User Guide*.`aws secretsmanager validate-resource-policy \ --resource-policy``file://mypolicy.json`Contents of `mypolicy.json`:`{ "Version":"2012-10-17", "Statement": [ { "Effect": "Allow", "Principal": { "AWS": "arn:aws:iam::123456789012:role/MyRole" }, "Action": "secretsmanager:GetSecretValue", "Resource": "*" } ] }`Output: `{ "PolicyValidationPassed": true, "ValidationErrors": [] }`For more information, see [Permissions reference for Secrets Manager](https://docs.aws.amazon.com/secretsmanager/latest/userguide/reference_iam-permissions.html)in the*Secrets Manager User Guide*.- 
                    For API details, see [ValidateResourcePolicy](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/secretsmanager/validate-resource-policy.html)in*AWS CLI Command Reference*.
 
-