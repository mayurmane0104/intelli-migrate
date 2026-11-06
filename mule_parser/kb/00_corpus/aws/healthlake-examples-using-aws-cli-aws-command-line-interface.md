# HealthLake examples using AWS CLI - AWS Command Line Interface

**Source:** [https://docs.aws.amazon.com/cli/latest/userguide/cli_healthlake_code_examples.html](https://docs.aws.amazon.com/cli/latest/userguide/cli_healthlake_code_examples.html)

---

The following code examples show you how to perform actions and implement common scenarios by using the AWS Command Line Interface with HealthLake.

*Actions* are code excerpts from larger programs and must be run in context. While actions show you how to call individual service functions, you can see actions in context in their related scenarios.

Each example includes a link to the complete source code, where you can find instructions on how to set up and run the code in context.

###### Topics

## Actions

    The following code example shows how to use `create-fhir-datastore`.

- **AWS CLI**
- 
            
                    **Example 1: Create a SigV4-enabled HealthLake data store**The following `create-fhir-datastore`example demonstrates how to create a new data store in AWS HealthLake.`aws healthlake create-fhir-datastore \ --datastore-type-version``R4`\ --datastore-name`"FhirTestDatastore"`Output: `{ "DatastoreEndpoint": "https://healthlake.us-east-1.amazonaws.com/datastore/(Data store ID)/r4/", "DatastoreArn": "arn:aws:healthlake:us-east-1:(AWS Account ID):datastore/(Data store ID)", "DatastoreStatus": "CREATING", "DatastoreId": "(Data store ID)" }`**Example 2: Create a SMART on FHIR-enabled HealthLake data store**The following `create-fhir-datastore`example demonstrates how to create a new SMART on FHIR-enabled data store in AWS HealthLake.`aws healthlake create-fhir-datastore \ --datastore-name``"your-data-store-name"`\ --datastore-type-version`R4`\ --preload-data-config PreloadDataType="SYNTHEA" \ --sse-configuration '`{ "KmsEncryptionConfig": { "CmkType": "CUSTOMER_MANAGED_KMS_KEY", "KmsKeyId": "arn:aws:kms:us-east-1:your-account-id:key/your-key-id" } }`' \ --identity-provider-configuration`file://identity_provider_configuration.json`Contents of `identity_provider_configuration.json`:`{ "AuthorizationStrategy": "SMART_ON_FHIR_V1", "FineGrainedAuthorizationEnabled": true, "IdpLambdaArn": "arn:aws:lambda:your-region:your-account-id:function:your-lambda-name", "Metadata": "{\"issuer\":\"https://ehr.example.com\", \"jwks_uri\":\"https://ehr.example.com/.well-known/jwks.json\",\"authorization_endpoint\":\"https://ehr.example.com/auth/authorize\",\"token_endpoint\":\"https://ehr.token.com/auth/token\",\"token_endpoint_auth_methods_supported\":[\"client_secret_basic\",\"foo\"],\"grant_types_supported\":[\"client_credential\",\"foo\"],\"registration_endpoint\":\"https://ehr.example.com/auth/register\",\"scopes_supported\":[\"openId\",\"profile\",\"launch\"],\"response_types_supported\":[\"code\"],\"management_endpoint\":\"https://ehr.example.com/user/manage\",\"introspection_endpoint\":\"https://ehr.example.com/user/introspect\",\"revocation_endpoint\":\"https://ehr.example.com/user/revoke\",\"code_challenge_methods_supported\":[\"S256\"],\"capabilities\":[\"launch-ehr\",\"sso-openid-connect\",\"client-public\"]}" }`Output: `{ "DatastoreEndpoint": "https://healthlake.us-east-1.amazonaws.com/datastore/(Data store ID)/r4/", "DatastoreArn": "arn:aws:healthlake:us-east-1:(AWS Account ID):datastore/(Data store ID)", "DatastoreStatus": "CREATING", "DatastoreId": "(Data store ID)" }`For more information, see [Creating and monitoring a FHIR data store](https://docs.aws.amazon.com/healthlake/latest/devguide/working-with-FHIR-healthlake.html)in the*AWS HealthLake Developer Guide*.- 
                    For API details, see [CreateFHIRDatastore](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/healthlake/create-fhir-datastore.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `delete-fhir-datastore`.

- **AWS CLI**
- 
            
                    **To delete a FHIR data store**The following `delete-fhir-datastore`example demonstrates how to delete a data store and all of its contents in AWS HealthLake.`aws healthlake delete-fhir-datastore \ --datastore-id``(Data``store``ID)`Output: `{ "DatastoreEndpoint": "https://healthlake.us-east-1.amazonaws.com/datastore/(Data store ID)/r4/", "DatastoreArn": "arn:aws:healthlake:us-east-1:(AWS Account ID):datastore/(Data store ID)", "DatastoreStatus": "DELETING", "DatastoreId": "(Data store ID)" }`For more information, see Creating and monitoring a FHIR data store <https://docs.aws.amazon.com/healthlake/latest/devguide/working-with-FHIR-healthlake.html> in the *AWS HealthLake Developer Guide*.- 
                    For API details, see [DeleteFHIRDatastore](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/healthlake/delete-fhir-datastore.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `describe-fhir-datastore`.

- **AWS CLI**
- 
            
                    **To describe a FHIR data store**The following `describe-fhir-datastore`example demonstrates how to find the properties of a data store in AWS HealthLake.`aws healthlake describe-fhir-datastore \ --datastore-id``"1f2f459836ac6c513ce899f9e4f66a59"`Output: `{ "DatastoreProperties": { "PreloadDataConfig": { "PreloadDataType": "SYNTHEA" }, "SseConfiguration": { "KmsEncryptionConfig": { "CmkType": "CUSTOMER_MANAGED_KMS_KEY", "KmsKeyId": "arn:aws:kms:us-east-1:123456789012:key/a1b2c3d4-5678-90ab-cdef-EXAMPLE11111" } }, "DatastoreName": "Demo", "DatastoreArn": "arn:aws:healthlake:us-east-1:<AWS Account ID>:datastore/<Data store ID>", "DatastoreEndpoint": "https://healthlake.us-east-1.amazonaws.com/datastore/<Data store ID>/r4/", "DatastoreStatus": "ACTIVE", "DatastoreTypeVersion": "R4", "CreatedAt": 1603761064.881, "DatastoreId": "<Data store ID>", "IdentityProviderConfiguration": { "AuthorizationStrategy": "AWS_AUTH", "FineGrainedAuthorizationEnabled": false } } }`For more information, see [Creating and monitoring a FHIR data stores](https://docs.aws.amazon.com/healthlake/latest/devguide/working-with-FHIR-healthlake.html)in the*AWS HealthLake Developer Guide*.- 
                    For API details, see [DescribeFHIRDatastore](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/healthlake/describe-fhir-datastore.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `describe-fhir-export-job`.

- **AWS CLI**
- 
            
                    **To describe a FHIR export job**The following `describe-fhir-export-job`example shows how to find the properties of a FHIR export job in AWS HealthLake.`aws healthlake describe-fhir-export-job \ --datastore-id``(Data``store``ID)`\ --job-id`9b9a51943afaedd0a8c0c26c49135a31`Output: `{ "ExportJobProperties": { "DataAccessRoleArn": "arn:aws:iam::(AWS Account ID):role/(Role Name)", "JobStatus": "IN_PROGRESS", "JobId": "9009813e9d69ba7cf79bcb3468780f16", "SubmitTime": "2024-11-20T11:31:46.672000-05:00", "EndTime": "2024-11-20T11:34:01.636000-05:00", "OutputDataConfig": { "S3Configuration": { "S3Uri": "s3://(Bucket Name)/(Prefix Name)/", "KmsKeyId": "arn:aws:kms:us-east-1:012345678910:key/d330e7fc-b56c-4216-a250-f4c43ef46e83" } }, "DatastoreId": "(Data store ID)" } }`For more information, see [Exporting files from a FHIR data store](https://docs.aws.amazon.com/healthlake/latest/devguide/export-datastore.html)in the*AWS HealthLake Developer Guide*.- 
                    For API details, see [DescribeFHIRExportJob](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/healthlake/describe-fhir-export-job.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `describe-fhir-import-job`.

- **AWS CLI**
- 
            
                    **To describe a FHIR import job**The following `describe-fhir-import-job`example shows how to learn the properties of a FHIR import job using AWS HealthLake.`aws healthlake describe-fhir-import-job \ --datastore-id``(Data``store``ID)`\ --job-id`c145fbb27b192af392f8ce6e7838e34f`Output: `{ "ImportJobProperties": { "InputDataConfig": { "S3Uri": "s3://(Bucket Name)/(Prefix Name)/" { "arrayitem2": 2 } }, "DataAccessRoleArn": "arn:aws:iam::(AWS Account ID):role/(Role Name)", "JobStatus": "COMPLETED", "JobId": "c145fbb27b192af392f8ce6e7838e34f", "SubmitTime": 1606272542.161, "EndTime": 1606272609.497, "DatastoreId": "(Data store ID)" } }`For more information, see [Importing files to a FHIR data store](https://docs.aws.amazon.com/healthlake/latest/devguide/import-datastore.html)in the*AWS HealthLake Developer Guide*.- 
                    For API details, see [DescribeFHIRImportJob](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/healthlake/describe-fhir-import-job.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `list-fhir-datastores`.

- **AWS CLI**
- 
            
                    **To list FHIR data stores**The following `list-fhir-datastores`example shows to how to use the command and how users can filter results based on data store status in AWS HealthLake.`aws healthlake list-fhir-datastores \ --filter``DatastoreStatus=ACTIVE`Output: `{ "DatastorePropertiesList": [ { "PreloadDataConfig": { "PreloadDataType": "SYNTHEA" }, "SseConfiguration": { "KmsEncryptionConfig": { "CmkType": "CUSTOMER_MANAGED_KMS_KEY", "KmsKeyId": "arn:aws:kms:us-east-1:123456789012:key/a1b2c3d4-5678-90ab-cdef-EXAMPLE11111" } }, "DatastoreName": "Demo", "DatastoreArn": "arn:aws:healthlake:us-east-1:<AWS Account ID>:datastore/<Data store ID>", "DatastoreEndpoint": "https://healthlake.us-east-1.amazonaws.com/datastore/<Data store ID>/r4/", "DatastoreStatus": "ACTIVE", "DatastoreTypeVersion": "R4", "CreatedAt": 1603761064.881, "DatastoreId": "<Data store ID>", "IdentityProviderConfiguration": { "AuthorizationStrategy": "AWS_AUTH", "FineGrainedAuthorizationEnabled": false } } ] }`For more information, see [Creating and monitoring a FHIR data store](https://docs.aws.amazon.com/healthlake/latest/devguide/working-with-FHIR-healthlake.html)in the*AWS HealthLake Developer Guide*.- 
                    For API details, see [ListFHIRDatastores](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/healthlake/list-fhir-datastores.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `list-fhir-export-jobs`.

- **AWS CLI**
- 
            
                    **To list all FHIR export jobs**The following `list-fhir-export-jobs`example shows how to use the command to view a list of export jobs associated with an account.`aws healthlake list-fhir-export-jobs \ --datastore-id``(Data``store``ID)`\ --submitted-before`(DATE``like``2024-10-13T19:00:00Z)`\ --submitted-after`(DATE``like``2020-10-13T19:00:00Z``)`\ --job-name`"FHIR-EXPORT"`\ --job-status`SUBMITTED`\ --max-results`(Integer``between``1``and``500)`Output: `{ "ExportJobPropertiesList": [ { "ExportJobProperties": { "OutputDataConfig": { "S3Uri": "s3://(Bucket Name)/(Prefix Name)/", "S3Configuration": { "S3Uri": "s3://(Bucket Name)/(Prefix Name)/", "KmsKeyId": "(KmsKey Id)" } }, "DataAccessRoleArn": "arn:aws:iam::(AWS Account ID):role/(Role Name)", "JobStatus": "COMPLETED", "JobId": "c145fbb27b192af392f8ce6e7838e34f", "JobName": "FHIR-EXPORT", "SubmitTime": "2024-11-20T11:31:46.672000-05:00", "EndTime": "2024-11-20T11:34:01.636000-05:00", "DatastoreId": "(Data store ID)" } } ] }`For more information, see [Exporting files from a FHIR data store](https://docs.aws.amazon.com/healthlake/latest/devguide/export-datastore.html)in the AWS HealthLake Developer Guide.- 
                    For API details, see [ListFHIRExportJobs](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/healthlake/list-fhir-export-jobs.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `list-fhir-import-jobs`.

- **AWS CLI**
- 
            
                    **To list all FHIR import jobs**The following `list-fhir-import-jobs`example shows how to use the command to view a list of all import jobs associated with an account.`aws healthlake list-fhir-import-jobs \ --datastore-id``(Data``store``ID)`\ --submitted-before`(DATE``like``2024-10-13T19:00:00Z)`\ --submitted-after`(DATE``like``2020-10-13T19:00:00Z``)`\ --job-name`"FHIR-IMPORT"`\ --job-status`SUBMITTED`\`-max-results``(Integer``between``1``and``500)`Output: `{ "ImportJobPropertiesList": [ { "JobId": "c0fddbf76f238297632d4aebdbfc9ddf", "JobStatus": "COMPLETED", "SubmitTime": "2024-11-20T10:08:46.813000-05:00", "EndTime": "2024-11-20T10:10:09.093000-05:00", "DatastoreId": "(Data store ID)", "InputDataConfig": { "S3Uri": "s3://(Bucket Name)/(Prefix Name)/" }, "JobOutputDataConfig": { "S3Configuration": { "S3Uri": "s3://(Bucket Name)/import/6407b9ae4c2def3cb6f1a46a0c599ec0-FHIR_IMPORT-c0fddbf76f238297632d4aebdbfc9ddf/", "KmsKeyId": "arn:aws:kms:us-east-1:123456789012:key/b7f645cb-e564-4981-8672-9e012d1ff1a0" } }, "JobProgressReport": { "TotalNumberOfScannedFiles": 1, "TotalSizeOfScannedFilesInMB": 0.001798, "TotalNumberOfImportedFiles": 1, "TotalNumberOfResourcesScanned": 1, "TotalNumberOfResourcesImported": 1, "TotalNumberOfResourcesWithCustomerError": 0, "TotalNumberOfFilesReadWithCustomerError": 0, "Throughput": 0.0 }, "DataAccessRoleArn": "arn:aws:iam::(AWS Account ID):role/(Role Name)" } ] }`For more information, see [Importing files to FHIR data store](https://docs.aws.amazon.com/healthlake/latest/devguide/import-examples.html)in the AWS HealthLake Developer Guide.- 
                    For API details, see [ListFHIRImportJobs](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/healthlake/list-fhir-import-jobs.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `list-tags-for-resource`.

- **AWS CLI**
- 
            
                    **To list tags for a data store**The following `list-tags-for-resource`example lists the tags associated with the specified data store.:`aws healthlake list-tags-for-resource \ --resource-arn``"arn:aws:healthlake:us-east-1:123456789012:datastore/fhir/0725c83f4307f263e16fd56b6d8ebdbe"`Output: `{ "tags": { "key": "value", "key1": "value1" } }`For more information, see [Tagging resources in AWS HealthLake](https://docs.aws.amazon.com/healthlake/latest/devguide/tagging.html)in the AWS HealthLake Developer Guide.- 
                    For API details, see [ListTagsForResource](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/healthlake/list-tags-for-resource.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `start-fhir-export-job`.

- **AWS CLI**
- 
            
                    **To start a FHIR export job**The following `start-fhir-export-job`example shows how to start a FHIR export job using AWS HealthLake.`aws healthlake start-fhir-export-job \ --output-data-config '``{"S3Configuration": {"S3Uri":"s3://(Bucket Name)/(Prefix Name)/","KmsKeyId":"arn:aws:kms:us-east-1:012345678910:key/d330e7fc-b56c-4216-a250-f4c43ef46e83"}}`' \ --datastore-id`(Data``store``ID)`\ --data-access-role-arn`arn:aws:iam::(AWS``Account``ID):role/(Role``Name)`Output: `{ "DatastoreId": "(Data store ID)", "JobStatus": "SUBMITTED", "JobId": "9b9a51943afaedd0a8c0c26c49135a31" }`For more information, see [Exporting files from a FHIR data store](https://docs.aws.amazon.com/healthlake/latest/devguide/export-datastore.html)in the*AWS HealthLake Developer Guide*.- 
                    For API details, see [StartFHIRExportJob](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/healthlake/start-fhir-export-job.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `start-fhir-import-job`.

- **AWS CLI**
- 
            
                    **To start a FHIR import job**The following `start-fhir-import-job`example shows how to start a FHIR import job using AWS HealthLake.`aws healthlake start-fhir-import-job \ --input-data-config S3Uri="s3://(Bucket Name)/(Prefix Name)/" \ --job-output-data-config '``{"S3Configuration": {"S3Uri":"s3://(Bucket Name)/(Prefix Name)/","KmsKeyId":"arn:aws:kms:us-east-1:012345678910:key/d330e7fc-b56c-4216-a250-f4c43ef46e83"}}`' \ --datastore-id`(Data``store``ID)`\ --data-access-role-arn`"arn:aws:iam::(AWS Account ID):role/(Role Name)"`Output: `{ "DatastoreId": "(Data store ID)", "JobStatus": "SUBMITTED", "JobId": "c145fbb27b192af392f8ce6e7838e34f" }`For more information, see [Importing files to a FHIR data store](https://docs.aws.amazon.com/healthlake/latest/devguide/import-datastore.html)in the*AWS HealthLake Developer Guide*.- 
                    For API details, see [StartFHIRImportJob](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/healthlake/start-fhir-import-job.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `tag-resource`.

- **AWS CLI**
- 
            
                    **To add a tag to data store**The following `tag-resource`example shows how to add a tag to a data store.`aws healthlake tag-resource \ --resource-arn``"arn:aws:healthlake:us-east-1:123456789012:datastore/fhir/0725c83f4307f263e16fd56b6d8ebdbe"`\ --tags '`[{"Key": "key1", "Value": "value1"}]`'This command produces no output. For more information, see [Adding a tag to a data store](https://docs.aws.amazon.com/healthlake/latest/devguide/add-a-tag.html)in the*AWS HealthLake Developer Guide.*.- 
                    For API details, see [TagResource](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/healthlake/tag-resource.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `untag-resource`.

- **AWS CLI**
- 
            
                    **To remove tags from a data store.**The following `untag-resource`example shows how to remove tags from a data store.`aws healthlake untag-resource \ --resource-arn``"arn:aws:healthlake:us-east-1:123456789012:datastore/fhir/b91723d65c6fdeb1d26543a49d2ed1fa"`\ --tag-keys '`["key1"]`'This command produces no output. For more information, see [Removing tags from a data store](https://docs.aws.amazon.com/healthlake/latest/devguide/remove-tags.html)in the*AWS HealthLake Developer Guide*.- 
                    For API details, see [UntagResource](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/healthlake/untag-resource.html)in*AWS CLI Command Reference*.
 
-