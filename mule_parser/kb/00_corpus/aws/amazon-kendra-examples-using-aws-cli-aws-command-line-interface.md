# Amazon Kendra examples using AWS CLI - AWS Command Line Interface

**Source:** [https://docs.aws.amazon.com/cli/latest/userguide/cli_kendra_code_examples.html](https://docs.aws.amazon.com/cli/latest/userguide/cli_kendra_code_examples.html)

---

The following code examples show you how to perform actions and implement common scenarios by using the AWS Command Line Interface with Amazon Kendra.

*Actions* are code excerpts from larger programs and must be run in context. While actions show you how to call individual service functions, you can see actions in context in their related scenarios.

Each example includes a link to the complete source code, where you can find instructions on how to set up and run the code in context.

###### Topics

## Actions

    The following code example shows how to use `create-data-source`.

- **AWS CLI**
- 
            
                    **To create an Amazon Kendra data source connector**The following `create-data-source`creates and configures an Amazon Kendra data source connector. You can use`describe-data-source`to view the status of a data source connector, and read any error messages if the status shows a data source connector "FAILED" to completely create.`aws kendra create-data-source \ --name``"example data source 1"`\ --description`"Example data source 1 for example index 1 contains the first set of example documents"`\ --tags '`{"Key": "test resources", "Value": "kendra"}, {"Key": "test resources", "Value": "aws"}`' \ --role-arn`"arn:aws:iam::my-account-id:role/KendraRoleForS3TemplateConfigDataSource"`\ --index-id`exampleindex1`\ --language-code`"es"`\ --schedule`"0 0 18 ? * TUE,MON,WED,THU,FRI,SAT *"`\ --configuration '`{"TemplateConfiguration": {"Template": file://s3schemaconfig.json}}`' \ --type`"TEMPLATE"`\ --custom-document-enrichment-configuration '`{"PostExtractionHookConfiguration": {"LambdaArn": "arn:aws:iam::my-account-id:function/my-function-ocr-docs", "S3Bucket": "s3://amzn-s3-demo-bucket/scanned-image-text-example-docs"}, "RoleArn": "arn:aws:iam:my-account-id:role/KendraRoleForCDE"}`' \ --vpc-configuration '`{"SecurityGroupIds": ["sg-1234567890abcdef0"], "SubnetIds": ["subnet-1c234","subnet-2b134"]}`'Output: `{ "Id": "exampledatasource1" }`For more information, see [Getting started with an Amazon Kendra index and data source connector](https://docs.aws.amazon.com/kendra/latest/dg/getting-started.html)in the*Amazon Kendra Developer Guide*.- 
                    For API details, see [CreateDataSource](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/kendra/create-data-source.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `create-index`.

- **AWS CLI**
- 
            
                    **To create an Amazon Kendra index**The following `create-index`creates and configures an Amazon Kendra index. You can use`describe-index`to view the status of an index, and read any error messages if the status shows an index "FAILED" to completely create.`aws kendra create-index \ --name``"example index 1"`\ --description`"Example index 1 contains the first set of example documents"`\ --tags '`{"Key": "test resources", "Value": "kendra"}, {"Key": "test resources", "Value": "aws"}`' \ --role-arn`"arn:aws:iam::my-account-id:role/KendraRoleForExampleIndex"`\ --edition`"DEVELOPER_EDITION"`\ --server-side-encryption-configuration '`{"KmsKeyId": "my-kms-key-id"}`' \ --user-context-policy`"USER_TOKEN"`\ --user-token-configurations '`{"JsonTokenTypeConfiguration": {"GroupAttributeField": "groupNameField", "UserNameAttributeField": "userNameField"}}`'Output: `{ "Id": index1 }`For more information, see [Getting started with an Amazon Kendra index and data source connector](https://docs.aws.amazon.com/kendra/latest/dg/getting-started.html)in the*Amazon Kendra Developer Guide*.- 
                    For API details, see [CreateIndex](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/kendra/create-index.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `describe-data-source`.

- **AWS CLI**
- 
            
                    **To get information about an Amazon Kendra data source connector**The following `describe-data-source`gets information about an Amazon Kendra data source connector. You can view the configuration of a data source connector, and read any error messages if the status shows a data source connector "FAILED" to completely create.`aws kendra describe-data-source \ --id``exampledatasource1`\ --index-id`exampleindex1`Output: `{ "Configuration": { "TemplateConfiguration": { "Template": { "connectionConfiguration": { "repositoryEndpointMetadata": { "BucketName": "amzn-s3-demo-bucket" } }, "repositoryConfigurations": { "document":{ "fieldMappings": [ { "indexFieldName":"_document_title", "indexFieldType":"STRING", "dataSourceFieldName": "title" }, { "indexFieldName":"_last_updated_at", "indexFieldType":"DATE", "dataSourceFieldName": "modified_date" } ] } }, "additionalProperties": { "inclusionPatterns": [ "*.txt", "*.doc", "*.docx" ], "exclusionPatterns": [ "*.json" ], "inclusionPrefixes": [ "PublicExampleDocsFolder" ], "exclusionPrefixes": [ "PrivateDocsFolder/private" ], "aclConfigurationFilePath": "ExampleDocsFolder/AclConfig.json", "metadataFilesPrefix": "metadata" }, "syncMode": "FULL_CRAWL", "type" : "S3", "version": "1.0.0" } } }, "CreatedAt": 2024-02-25T13:30:10+00:00, "CustomDocumentEnrichmentConfiguration": { "PostExtractionHookConfiguration": { "LambdaArn": "arn:aws:iam::my-account-id:function/my-function-ocr-docs", "S3Bucket": "s3://amzn-s3-demo-bucket/scanned-image-text-example-docs/function" }, "RoleArn": "arn:aws:iam:my-account-id:role/KendraRoleForCDE" } "Description": "Example data source 1 for example index 1 contains the first set of example documents", "Id": exampledatasource1, "IndexId": exampleindex1, "LanguageCode": "en", "Name": "example data source 1", "RoleArn": "arn:aws:iam::my-account-id:role/KendraRoleForS3TemplateConfigDataSource", "Schedule": "0 0 18 ? * TUE,MON,WED,THU,FRI,SAT *", "Status": "ACTIVE", "Type": "TEMPLATE", "UpdatedAt": 1709163615, "VpcConfiguration": { "SecurityGroupIds": ["sg-1234567890abcdef0"], "SubnetIds": ["subnet-1c234","subnet-2b134"] } }`For more information, see [Getting started with an Amazon Kendra index and data source connector](https://docs.aws.amazon.com/kendra/latest/dg/getting-started.html)in the*Amazon Kendra Developer Guide*.- 
                    For API details, see [DescribeDataSource](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/kendra/describe-data-source.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `describe-index`.

- **AWS CLI**
- 
            
                    **To get information about an Amazon Kendra index**The following `describe-index`gets information about an Amazon Kendra index. You can view the configuration of an index, and read any error messages if the status shows an index "FAILED" to completely create.`aws kendra describe-index \ --id``exampleindex1`Output: `{ "CapacityUnits": { "QueryCapacityUnits": 0, "StorageCapacityUnits": 0 }, "CreatedAt": 2024-02-25T12:30:10+00:00, "Description": "Example index 1 contains the first set of example documents", "DocumentMetadataConfigurations": [ { "Name": "_document_title", "Relevance": { "Importance": 8 }, "Search": { "Displayable": true, "Facetable": false, "Searchable": true, "Sortable": false }, "Type": "STRING_VALUE" }, { "Name": "_document_body", "Relevance": { "Importance": 5 }, "Search": { "Displayable": true, "Facetable": false, "Searchable": true, "Sortable": false }, "Type": "STRING_VALUE" }, { "Name": "_last_updated_at", "Relevance": { "Importance": 6, "Duration": "2628000s", "Freshness": true }, "Search": { "Displayable": true, "Facetable": false, "Searchable": true, "Sortable": true }, "Type": "DATE_VALUE" }, { "Name": "department_custom_field", "Relevance": { "Importance": 7, "ValueImportanceMap": { "Human Resources" : 4, "Marketing and Sales" : 2, "Research and innvoation" : 3, "Admin" : 1 } }, "Search": { "Displayable": true, "Facetable": true, "Searchable": true, "Sortable": true }, "Type": "STRING_VALUE" } ], "Edition": "DEVELOPER_EDITION", "Id": "index1", "IndexStatistics": { "FaqStatistics": { "IndexedQuestionAnswersCount": 10 }, "TextDocumentStatistics": { "IndexedTextBytes": 1073741824, "IndexedTextDocumentsCount": 1200 } }, "Name": "example index 1", "RoleArn": "arn:aws:iam::my-account-id:role/KendraRoleForExampleIndex", "ServerSideEncryptionConfiguration": { "KmsKeyId": "my-kms-key-id" }, "Status": "ACTIVE", "UpdatedAt": 1709163615, "UserContextPolicy": "USER_TOKEN", "UserTokenConfigurations": [ { "JsonTokenTypeConfiguration": { "GroupAttributeField": "groupNameField", "UserNameAttributeField": "userNameField" } } ] }`For more information, see [Getting started with an Amazon Kendra index and data source connector](https://docs.aws.amazon.com/kendra/latest/dg/getting-started.html)in the*Amazon Kendra Developer Guide*.- 
                    For API details, see [DescribeIndex](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/kendra/describe-index.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `update-data-source`.

- **AWS CLI**
- 
            
                    **To update an Amazon Kendra data source connector**The following `update-data-source`updates the configuration of an Amazon Kendra data source connector. If the action is successful, the service either sends back no output, the HTTP status code 200, or the AWS CLI return code 0. You can use`describe-data-source`to view the configuration and status of a data source connector.`aws kendra update-data-source \ --id``exampledatasource1`\ --index-id`exampleindex1`\ --name`"new name for example data source 1"`\ --description`"new description for example data source 1"`\ --role-arn`arn:aws:iam::my-account-id:role/KendraNewRoleForExampleDataSource`\ --configuration '`{"TemplateConfiguration": {"Template": file://s3schemanewconfig.json}}`' \ --custom-document-enrichment-configuration '`{"PostExtractionHookConfiguration": {"LambdaArn": "arn:aws:iam::my-account-id:function/my-function-ocr-docs", "S3Bucket": "s3://amzn-s3-demo-bucket/scanned-image-text-example-docs"}, "RoleArn": "arn:aws:iam:my-account-id:role/KendraNewRoleForCDE"}`' \ --language-code`"es"`\ --schedule`"0 0 18 ? * MON,WED,FRI *"`\ --vpc-configuration '`{"SecurityGroupIds": ["sg-1234567890abcdef0"], "SubnetIds": ["subnet-1c234","subnet-2b134"]}`'This command produces no output. For more information, see [Getting started with an Amazon Kendra index and data source connector](https://docs.aws.amazon.com/kendra/latest/dg/getting-started.html)in the*Amazon Kendra Developer Guide*.- 
                    For API details, see [UpdateDataSource](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/kendra/update-data-source.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `update-index`.

- **AWS CLI**
- 
            
                    **To update an Amazon Kendra index**The following `update-index`updates the configuration of an Amazon Kendra index. If the action is successful, the service either sends back no output, the HTTP status code 200, or the AWS CLI return code 0. You can use`describe-index`to view the configuration and status of an index.`aws kendra update-index \ --id``enterpriseindex1`\ --name`"new name for Enterprise Edition index 1"`\ --description`"new description for Enterprise Edition index 1"`\ --role-arn`arn:aws:iam::my-account-id:role/KendraNewRoleForEnterpriseIndex`\ --capacity-units '`{"QueryCapacityUnits": 2, "StorageCapacityUnits": 1}`' \ --document-metadata-configuration-updates '`{"Name": "_document_title", "Relevance": {"Importance": 6}}, {"Name": "_last_updated_at", "Relevance": {"Importance": 8}}`' \ --user-context-policy`"USER_TOKEN"`\ --user-token-configurations '`{"JsonTokenTypeConfiguration": {"GroupAttributeField": "groupNameField", "UserNameAttributeField": "userNameField"}}`'This command produces no output. For more information, see [Getting started with an Amazon Kendra index and data source connector](https://docs.aws.amazon.com/kendra/latest/dg/getting-started.html)in the*Amazon Kendra Developer Guide*.- 
                    For API details, see [UpdateIndex](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/kendra/update-index.html)in*AWS CLI Command Reference*.
 
-