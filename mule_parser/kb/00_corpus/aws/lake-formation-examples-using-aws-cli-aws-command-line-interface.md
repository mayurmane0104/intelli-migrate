# Lake Formation examples using AWS CLI - AWS Command Line Interface

**Source:** [https://docs.aws.amazon.com/cli/latest/userguide/cli_lakeformation_code_examples.html](https://docs.aws.amazon.com/cli/latest/userguide/cli_lakeformation_code_examples.html)

---

The following code examples show you how to perform actions and implement common scenarios by using the AWS Command Line Interface with Lake Formation.

*Actions* are code excerpts from larger programs and must be run in context. While actions show you how to call individual service functions, you can see actions in context in their related scenarios.

Each example includes a link to the complete source code, where you can find instructions on how to set up and run the code in context.

###### Topics

## Actions

    The following code example shows how to use `add-lf-tags-to-resource`.

- **AWS CLI**
- 
            
                    **To attach one or more LF-tags to an existing resource**The following `add-lf-tags-to-resource`example attaches given LF-tag to the table resource.`aws lakeformation add-lf-tags-to-resource \ --cli-input-json``file://input.json`Contents of `input.json`:`{ "CatalogId": "123456789111", "Resource": { "Table": { "CatalogId": "123456789111", "DatabaseName": "tpc", "Name": "dl_tpc_promotion" } }, "LFTags": [{ "CatalogId": "123456789111", "TagKey": "usergroup", "TagValues": [ "analyst" ] }] }`Output: `{ "Failures": [] }`For more information, see [Assigning LF-Tags to Data Catalog resources](https://docs.aws.amazon.com/lake-formation/latest/dg/TBAC-assigning-tags.html)in the*AWS Lake Formation Developer Guide*.- 
                    For API details, see [AddLfTagsToResource](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lakeformation/add-lf-tags-to-resource.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `batch-grant-permissions`.

- **AWS CLI**
- 
            
                    **To bulk grant permissions on resources to the principals**The following `batch-grant-permissions`example bulk grants access on specified resources to the principals.`aws lakeformation batch-grant-permissions \ --cli-input-json``file://input.json`Contents of `input.json`:`{ "CatalogId": "123456789111", "Entries": [{ "Id": "1", "Principal": { "DataLakePrincipalIdentifier": "arn:aws:iam::123456789111:user/lf-developer" }, "Resource": { "Table": { "CatalogId": "123456789111", "DatabaseName": "tpc", "Name": "dl_tpc_promotion" } }, "Permissions": [ "ALL" ], "PermissionsWithGrantOption": [ "ALL" ] }, { "Id": "2", "Principal": { "DataLakePrincipalIdentifier": "arn:aws:iam::123456789111:user/lf-developer" }, "Resource": { "Table": { "CatalogId": "123456789111", "DatabaseName": "tpc", "Name": "dl_tpc_customer" } }, "Permissions": [ "ALL" ], "PermissionsWithGrantOption": [ "ALL" ] }, { "Id": "3", "Principal": { "DataLakePrincipalIdentifier": "arn:aws:iam::123456789111:user/lf-business-analyst" }, "Resource": { "Table": { "CatalogId": "123456789111", "DatabaseName": "tpc", "Name": "dl_tpc_promotion" } }, "Permissions": [ "ALL" ], "PermissionsWithGrantOption": [ "ALL" ] }, { "Id": "4", "Principal": { "DataLakePrincipalIdentifier": "arn:aws:iam::123456789111:user/lf-developer" }, "Resource": { "DataCellsFilter": { "TableCatalogId": "123456789111", "DatabaseName": "tpc", "TableName": "dl_tpc_item", "Name": "developer_item" } }, "Permissions": [ "SELECT" ], "PermissionsWithGrantOption": [] } ] }`Output: `{ "Failures": [] }`For more information, see [Granting and revoking permissions on Data Catalog resources](https://docs.aws.amazon.com/lake-formation/latest/dg/granting-catalog-permissions.html)in the*AWS Lake Formation Developer Guide*.- 
                    For API details, see [BatchGrantPermissions](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lakeformation/batch-grant-permissions.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `batch-revoke-permissions`.

- **AWS CLI**
- 
            
                    **To bulk revoke permissions on resources from the principals**The following `batch-revoke-permissions`example bulk revokes access on specified resources from the principals.`aws lakeformation batch-revoke-permissions \ --cli-input-json``file://input.json`Contents of `input.json`:`{ "CatalogId": "123456789111", "Entries": [{ "Id": "1", "Principal": { "DataLakePrincipalIdentifier": "arn:aws:iam::123456789111:user/lf-developer" }, "Resource": { "Table": { "CatalogId": "123456789111", "DatabaseName": "tpc", "Name": "dl_tpc_promotion" } }, "Permissions": [ "ALL" ], "PermissionsWithGrantOption": [ "ALL" ] }, { "Id": "2", "Principal": { "DataLakePrincipalIdentifier": "arn:aws:iam::123456789111:user/lf-business-analyst" }, "Resource": { "Table": { "CatalogId": "123456789111", "DatabaseName": "tpc", "Name": "dl_tpc_promotion" } }, "Permissions": [ "ALL" ], "PermissionsWithGrantOption": [ "ALL" ] } ] }`Output: `{ "Failures": [] }`For more information, see [Granting and revoking permissions on Data Catalog resources](https://docs.aws.amazon.com/lake-formation/latest/dg/granting-catalog-permissions.html)in the*AWS Lake Formation Developer Guide*.- 
                    For API details, see [BatchRevokePermissions](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lakeformation/batch-revoke-permissions.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `cancel-transaction`.

- **AWS CLI**
- 
            
                    **To cancel a transaction**The following `cancel-transaction`example cancels the transaction.`aws lakeformation cancel-transaction \ --transaction-id='b014d972ca8347b89825e33c5774aec4'`This command produces no output. For more information, see [Reading from and writing to the data lake within transactions](https://docs.aws.amazon.com/lake-formation/latest/dg/transaction-ops.html)in the*AWS Lake Formation Developer Guide*.- 
                    For API details, see [CancelTransaction](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lakeformation/cancel-transaction.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `commit-transaction`.

- **AWS CLI**
- 
            
                    **To commit transaction**The following `commit-transaction`example commits the transaction.`aws lakeformation commit-transaction \ --transaction-id='b014d972ca8347b89825e33c5774aec4'`Output: `{ "TransactionStatus": "committed" }`For more information, see [Reading from and writing to the data lake within transactions](https://docs.aws.amazon.com/lake-formation/latest/dg/transaction-ops.html)in the*AWS Lake Formation Developer Guide*.- 
                    For API details, see [CommitTransaction](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lakeformation/commit-transaction.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `create-data-cells-filter`.

- **AWS CLI**
- 
            
                    **Example 1: To create data cell filter**The following `create-data-cells-filter`example creates a data cell filter to allow one to grant access to certain columns based on row condition.`aws lakeformation create-data-cells-filter \ --cli-input-json``file://input.json`Contents of `input.json`:`{ "TableData": { "ColumnNames": ["p_channel_details", "p_start_date_sk", "p_promo_name"], "DatabaseName": "tpc", "Name": "developer_promotion", "RowFilter": { "FilterExpression": "p_promo_name='ese'" }, "TableCatalogId": "123456789111", "TableName": "dl_tpc_promotion" } }`This command produces no output. For more information, see [Data filtering and cell-level security in Lake Formation](https://docs.aws.amazon.com/lake-formation/latest/dg/data-filtering.html)in the*AWS Lake Formation Developer Guide*.**Example 2: To create column filter**The following `create-data-cells-filter`example creates a data filter to allow one to grant access to certain columns.`aws lakeformation create-data-cells-filter \ --cli-input-json``file://input.json`Contents of `input.json`:`{ "TableData": { "ColumnNames": ["p_channel_details", "p_start_date_sk", "p_promo_name"], "DatabaseName": "tpc", "Name": "developer_promotion_allrows", "RowFilter": { "AllRowsWildcard": {} }, "TableCatalogId": "123456789111", "TableName": "dl_tpc_promotion" } }`This command produces no output. For more information, see [Data filtering and cell-level security in Lake Formation](https://docs.aws.amazon.com/lake-formation/latest/dg/data-filtering.html)in the*AWS Lake Formation Developer Guide*.**Example 3: To create data filter with exclude columns**The following `create-data-cells-filter`example creates a data filter to allow one to grant access all except the mentioned columns.`aws lakeformation create-data-cells-filter \ --cli-input-json``file://input.json`Contents of `input.json`:`{ "TableData": { "ColumnWildcard": { "ExcludedColumnNames": ["p_channel_details", "p_start_date_sk"] }, "DatabaseName": "tpc", "Name": "developer_promotion_excludecolumn", "RowFilter": { "AllRowsWildcard": {} }, "TableCatalogId": "123456789111", "TableName": "dl_tpc_promotion" } }`This command produces no output. For more information, see [Data filtering and cell-level security in Lake Formation](https://docs.aws.amazon.com/lake-formation/latest/dg/data-filtering.html)in the*AWS Lake Formation Developer Guide*.- 
                    For API details, see [CreateDataCellsFilter](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lakeformation/create-data-cells-filter.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `create-lf-tag`.

- **AWS CLI**
- 
            
                    **To create LF-Tag**The following `create-lf-tag`example creates an LF-Tag with the specified name and values.`aws lakeformation create-lf-tag \ --catalog-id '``123456789111`' \ --tag-key '`usergroup`' \ --tag-values '`["developer","analyst","campaign"]`'This command produces no output. For more information, see [Managing LF-Tags for metadata access control](https://docs.aws.amazon.com/lake-formation/latest/dg/managing-tags.html)in the*AWS Lake Formation Developer Guide*.- 
                    For API details, see [CreateLfTag](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lakeformation/create-lf-tag.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `delete-data-cells-filter`.

- **AWS CLI**
- 
            
                    **To delete data cell filter**The following `delete-data-cells-filter`example deletes given data cell filter.`aws lakeformation delete-data-cells-filter \ --cli-input-json``file://input.json`Contents of `input.json`:`{ "TableCatalogId": "123456789111", "DatabaseName": "tpc", "TableName": "dl_tpc_promotion", "Name": "developer_promotion" }`This command produces no output. For more information, see [Data filtering and cell-level security in Lake Formation](https://docs.aws.amazon.com/lake-formation/latest/dg/data-filtering.html)in the*AWS Lake Formation Developer Guide*.- 
                    For API details, see [DeleteDataCellsFilter](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lakeformation/delete-data-cells-filter.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `delete-lf-tag`.

- **AWS CLI**
- 
            
                    **To delete LF-Tag definition**The following `delete-lf-tag`example deletes LF-Tag definition.`aws lakeformation delete-lf-tag \ --catalog-id '``123456789111`' \ --tag-key '`usergroup`'This command produces no output. For more information, see [Managing LF-Tags for metadata access control](https://docs.aws.amazon.com/lake-formation/latest/dg/managing-tags.html)in the*AWS Lake Formation Developer Guide*.- 
                    For API details, see [DeleteLfTag](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lakeformation/delete-lf-tag.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `delete-objects-on-cancel`.

- **AWS CLI**
- 
            
                    **To delete object when transaction is cancelled**The following `delete-objects-on-cancel`example deletes the listed s3 object when the transaction is cancelled.`aws lakeformation delete-objects-on-cancel \ --cli-input-json``file://input.json`Contents of `input.json`:`{ "CatalogId": "012345678901", "DatabaseName": "tpc", "TableName": "dl_tpc_household_demographics_gov", "TransactionId": "1234d972ca8347b89825e33c5774aec4", "Objects": [{ "Uri": "s3://lf-data-lake-012345678901/target/dl_tpc_household_demographics_gov/run-unnamed-1-part-block-0-r-00000-snappy-ff26b17504414fe88b302cd795eabd00.parquet", "ETag": "1234ab1fc50a316b149b4e1f21a73800" }] }`This command produces no output. For more information, see [Reading from and writing to the data lake within transactions](https://docs.aws.amazon.com/lake-formation/latest/dg/transaction-ops.html)in the*AWS Lake Formation Developer Guide*.- 
                    For API details, see [DeleteObjectsOnCancel](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lakeformation/delete-objects-on-cancel.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `deregister-resource`.

- **AWS CLI**
- 
            
                    **To deregister data lake storage**The following `deregister-resource`example deregisters the resource as managed by the Lake Formation.`aws lakeformation deregister-resource \ --cli-input-json``file://input.json`Contents of `input.json`:`{ "ResourceArn": "arn:aws:s3:::lf-emr-athena-result-123" }`This command produces no output. For more information, see [Adding an Amazon S3 location to your data lake](https://docs.aws.amazon.com/lake-formation/latest/dg/register-data-lake.html)in the*AWS Lake Formation Developer Guide*.- 
                    For API details, see [DeregisterResource](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lakeformation/deregister-resource.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `describe-transaction`.

- **AWS CLI**
- 
            
                    **To retrieve a transaction details**The following `describe-transaction`example returns the details of a single transaction.`aws lakeformation describe-transaction \ --transaction-id='8cb4b1a7cc8d486fbaca9a64e7d9f5ce'`Output: `{ "TransactionDescription": { "TransactionId": "12345972ca8347b89825e33c5774aec4", "TransactionStatus": "committed", "TransactionStartTime": "2022-08-10T14:29:04.046000+00:00", "TransactionEndTime": "2022-08-10T14:29:09.681000+00:00" } }`For more information, see [Reading from and writing to the data lake within transactions](https://docs.aws.amazon.com/lake-formation/latest/dg/transaction-ops.html)in the*AWS Lake Formation Developer Guide*.- 
                    For API details, see [DescribeTransaction](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lakeformation/describe-transaction.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `extend-transaction`.

- **AWS CLI**
- 
            
                    **To extend a transaction**The following `extend-transaction`example extends the transaction.`aws lakeformation extend-transaction \ --transaction-id='8cb4b1a7cc8d486fbaca9a64e7d9f5ce'`This command produces no output. For more information, see [Reading from and writing to the data lake within transactions](https://docs.aws.amazon.com/lake-formation/latest/dg/transaction-ops.html)in the*AWS Lake Formation Developer Guide*.- 
                    For API details, see [ExtendTransaction](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lakeformation/extend-transaction.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `get-data-lake-settings`.

- **AWS CLI**
- 
            
                    **To retrieve AWS Lake Formation-managed data lake settings**The following `get-data-lake-settings`example retrieves the list of data lake administrators and other data lake settings.`aws lakeformation get-data-lake-settings \ --cli-input-json``file://input.json`Contents of `input.json`:`{ "CatalogId": "123456789111" }`Output: `{ "DataLakeSettings": { "DataLakeAdmins": [{ "DataLakePrincipalIdentifier": "arn:aws:iam::123456789111:user/lf-admin" }], "CreateDatabaseDefaultPermissions": [], "CreateTableDefaultPermissions": [ { "Principal": { "DataLakePrincipalIdentifier": "IAM_ALLOWED_PRINCIPALS" }, "Permissions": [ "ALL" ] } ], "TrustedResourceOwners": [], "AllowExternalDataFiltering": true, "ExternalDataFilteringAllowList": [{ "DataLakePrincipalIdentifier": "123456789111" }], "AuthorizedSessionTagValueList": [ "Amazon EMR" ] } }`For more information, see [Changing the default security settings for your data lake](https://docs.aws.amazon.com/lake-formation/latest/dg/change-settings.html)in the*AWS Lake Formation Developer Guide*.- 
                    For API details, see [GetDataLakeSettings](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lakeformation/get-data-lake-settings.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `get-effective-permissions-for-path`.

- **AWS CLI**
- 
            
                    **To retrieve permissions on resources located at specific path**The following `get-effective-permissions-for-path`example returns the Lake Formation permissions for a specified table or database resource located at a path in Amazon S3.`aws lakeformation get-effective-permissions-for-path \ --cli-input-json``file://input.json`Contents of `input.json`:`{ "CatalogId": "123456789111", "ResourceArn": "arn:aws:s3:::lf-data-lake-123456789111" }`Output: `{ "Permissions": [{ "Principal": { "DataLakePrincipalIdentifier": "arn:aws:iam::123456789111:user/lf-campaign-manager" }, "Resource": { "Database": { "Name": "tpc" } }, "Permissions": [ "DESCRIBE" ], "PermissionsWithGrantOption": [] }, { "Principal": { "DataLakePrincipalIdentifier": "arn:aws:iam::123456789111:role/EMR-RuntimeRole" }, "Resource": { "Database": { "Name": "tpc" } }, "Permissions": [ "ALL" ], "PermissionsWithGrantOption": [] }, { "Principal": { "DataLakePrincipalIdentifier": "arn:aws:iam::123456789111:saml-provider/oktaSAMLProvider:user/emr-developer" }, "Resource": { "Database": { "Name": "tpc" } }, "Permissions": [ "ALL", "DESCRIBE" ], "PermissionsWithGrantOption": [] }, { "Principal": { "DataLakePrincipalIdentifier": "arn:aws:iam::123456789111:user/lf-admin" }, "Resource": { "Database": { "Name": "tpc" } }, "Permissions": [ "ALL", "ALTER", "CREATE_TABLE", "DESCRIBE", "DROP" ], "PermissionsWithGrantOption": [ "ALL", "ALTER", "CREATE_TABLE", "DESCRIBE", "DROP" ] }, { "Principal": { "DataLakePrincipalIdentifier": "arn:aws:iam::123456789111:role/LF-GlueServiceRole" }, "Resource": { "Database": { "Name": "tpc" } }, "Permissions": [ "CREATE_TABLE" ], "PermissionsWithGrantOption": [] } ], "NextToken": "E5SlJDSTZleUp6SWpvaU9UQTNORE0zTXpFeE5Ua3pJbjE5TENKbGVIQnBjbUYwYVc5dUlqcDdJbk5sWTI5dVpITWlPakUyTm==" }`For more information, see [Managing Lake Formation permissions](https://docs.aws.amazon.com/lake-formation/latest/dg/managing-permissions.html)in the*AWS Lake Formation Developer Guide*.- 
                    For API details, see [GetEffectivePermissionsForPath](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lakeformation/get-effective-permissions-for-path.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `get-lf-tag`.

- **AWS CLI**
- 
            
                    **To retrieve LF-tag definition**The following `get-lf-tag`example retrieves LF-tag definition.`aws lakeformation get-lf-tag \ --catalog-id '``123456789111`' \ --tag-key '`usergroup`'Output: `{ "CatalogId": "123456789111", "TagKey": "usergroup", "TagValues": [ "analyst", "campaign", "developer" ] }`For more information, see [Managing LF-Tags for metadata access control](https://docs.aws.amazon.com/lake-formation/latest/dg/managing-tags.html)in the*AWS Lake Formation Developer Guide*.- 
                    For API details, see [GetLfTag](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lakeformation/get-lf-tag.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `get-query-state`.

- **AWS CLI**
- 
            
                    **To retrieve state of a submitted query**The following `get-query-state`example returns the state of a query previously submitted.`aws lakeformation get-query-state \ --query-id='1234273f-4a62-4cda-8d98-69615ee8be9b'`Output: `{ "State": "FINISHED" }`For more information, see [Transactional data operations](https://docs.aws.amazon.com/lake-formation/latest/dg/transactions-data-operations.html)in the*AWS Lake Formation Developer Guide*.- 
                    For API details, see [GetQueryState](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lakeformation/get-query-state.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `get-query-statistics`.

- **AWS CLI**
- 
            
                    **To retrieve query statistics**The following `get-query-statistics`example retrieves statistics on the planning and execution of a query.`aws lakeformation get-query-statistics \ --query-id='1234273f-4a62-4cda-8d98-69615ee8be9b'`Output: `{ "ExecutionStatistics": { "AverageExecutionTimeMillis": 0, "DataScannedBytes": 0, "WorkUnitsExecutedCount": 0 }, "PlanningStatistics": { "EstimatedDataToScanBytes": 43235, "PlanningTimeMillis": 2377, "QueueTimeMillis": 440, "WorkUnitsGeneratedCount": 1 }, "QuerySubmissionTime": "2022-08-11T02:14:38.641870+00:00" }`For more information, see [Transactional data operations](https://docs.aws.amazon.com/lake-formation/latest/dg/transactions-data-operations.html)in the*AWS Lake Formation Developer Guide*.- 
                    For API details, see [GetQueryStatistics](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lakeformation/get-query-statistics.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `get-table-objects`.

- **AWS CLI**
- 
            
                    **To list objects of governed table**The following `get-table-objects`example returns the set of Amazon S3 objects that make up the specified governed table.`aws lakeformation get-table-objects \ --cli-input-json``file://input.json`Contents of `input.json`:`{ "CatalogId": "012345678901", "DatabaseName": "tpc", "TableName": "dl_tpc_household_demographics_gov", "QueryAsOfTime": "2022-08-10T15:00:00" }`Output: `{ "Objects": [{ "PartitionValues": [], "Objects": [{ "Uri": "s3://lf-data-lake-012345678901/target/dl_tpc_household_demographics_gov/run-unnamed-1-part-block-0-r-00000-snappy-ff26b17504414fe88b302cd795eabd00.parquet", "ETag": "12345b1fc50a316b149b4e1f21a73800", "Size": 43235 }] }] }`For more information, see [Reading from and writing to the data lake within transactions](https://docs.aws.amazon.com/lake-formation/latest/dg/transaction-ops.html)in the*AWS Lake Formation Developer Guide*.- 
                    For API details, see [GetTableObjects](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lakeformation/get-table-objects.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `get-work-unit-results`.

- **AWS CLI**
- 
            
                    **To retrieve work units of given query**The following `get-work-unit-results`example returns the work units resulting from the query.`aws lakeformation get-work-units \ --query-id='1234273f-4a62-4cda-8d98-69615ee8be9b' \ --work-unit-id '``0`' \ --work-unit-token '`B2fMSdmQXe9umX8Ux8XCo4=`'`outfile`Output: `outfile with Blob content.`For more information, see [Transactional data operations](https://docs.aws.amazon.com/lake-formation/latest/dg/transactions-data-operations.html)in the*AWS Lake Formation Developer Guide*.- 
                    For API details, see [GetWorkUnitResults](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lakeformation/get-work-unit-results.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `get-work-units`.

- **AWS CLI**
- 
            
                    **To retrieve work units**The following `get-work-units`example retrieves the work units generated by the StartQueryPlanning operation.`aws lakeformation get-work-units \ --query-id='1234273f-4a62-4cda-8d98-69615ee8be9b'`Output: `{ "WorkUnitRanges": [{ "WorkUnitIdMax": 0, "WorkUnitIdMin": 0, "WorkUnitToken": "1234eMAk4kLO4umqEL4Z5WuxL04AXwABABVhd3MtY3J5cHRvLXB1YmxpYy1rZXkAREEwYm9QbkhINmFYTWphbmMxZW1PQmEyMGlUb0JFbXNlWmRYc0NmckRIR1dmQ0hjY2YzNFdMcmNXb2JGZmhEK0QvZz09AAEAB2F3cy1rbXMAS2Fybjphd3M6a21zOnVzLWVhc3QtMTo3MDkxNTAyNDkyNDk6a2V5L2VmYmI3NDUyLTY1MjYtNGJiOS1iNmZhLTEzYzJkMTM3MmU2OQC4AQIBAHg6eWNF2ZrQATTAuPDJVCEAQSyIF67vX+f88jzGrYq22gE6jkQlpOB+Oet2eqNUmFudAAAAfjB8BgkqhkiG9w0BBwagbzBtAgEAMGgGCSqGSIb3DQEHATAeBglghkgBZQMEAS4wEQQMCOEWRdafowek3RUmAgEQgDsYZZE84nnnbNmvsqCBPLh19nLQ10mUWOg9IfiaOwefEn6L920V0x1LpJACo7MtIBLXnbGcz2dFDZjFygIAAAAADAAAEAAAAAAAAAAAAAAAAAAQSQf8XDSI5pvR4Fx4JsrS/////wAAAAEAAAAAAAAAAAAAAAEAAACX3/w5h75QAPomfKH+cyEKYU1yccUmBl+VSojiGOtdsUk7vcjYXUUboYm3dvqRqX2s4gROMOn+Ij8R0/8jYmnHkpvyAFNVRPyETyIKg7k5Z9+5I1c2d3446Jw/moWGGxjH8AEG9h27ytmOhozxDOEi/F2ZoXz6wlGDfGUo/2WxCkYOhTyNaw6TM+7drTM7yrW4iNVLUM0LX0xnFjIAhLhooWJek6vjQZUAZzBlAjBH8okRtYP8R7AY2Wls/hqFBhG0V4l42AC0LxsuZbMQrE2SzWZUZ0E9Uew7/n0cyX4CMQDR79INyv4ysMByW9kKGGKyba+cCNklExMR+btBQBmMuB2fMSdmQXe9umX8Ux8XCo4=" }], "QueryId": "1234273f-4a62-4cda-8d98-69615ee8be9b" }`For more information, see [Transactional data operations](https://docs.aws.amazon.com/lake-formation/latest/dg/transactions-data-operations.html)in the*AWS Lake Formation Developer Guide*.- 
                    For API details, see [GetWorkUnits](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lakeformation/get-work-units.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `grant-permissions`.

- **AWS CLI**
- 
            
                    **Example 1: To grant permissions to the principal on resources using LF-Tags**The following `grant-permissions`example grants ALL permissions to the principal on database resource that matches the LF-Tag policy.`aws lakeformation grant-permissions \ --cli-input-json``file://input.json`Contents of `input.json`:`{ "CatalogId": "123456789111", "Principal": { "DataLakePrincipalIdentifier": "arn:aws:iam::123456789111:user/lf-admin" }, "Resource": { "LFTagPolicy": { "CatalogId": "123456789111", "ResourceType": "DATABASE", "Expression": [{ "TagKey": "usergroup", "TagValues": [ "analyst", "developer" ] }] } }, "Permissions": [ "ALL" ], "PermissionsWithGrantOption": [ "ALL" ] }`This command produces no output. For more information, see [Granting and revoking permissions on Data Catalog resources](https://docs.aws.amazon.com/lake-formation/latest/dg/granting-catalog-permissions.html)in the*AWS Lake Formation Developer Guide*.**Example 2: To grant column level permissions to the principal**The following `grant-permissions`example grants permission to select specific column to the principal.`aws lakeformation grant-permissions \ --cli-input-json``file://input.json`Contents of `input.json`:`{ "CatalogId": "123456789111", "Principal": { "DataLakePrincipalIdentifier": "arn:aws:iam::123456789111:user/lf-developer" }, "Resource": { "TableWithColumns": { "CatalogId": "123456789111", "ColumnNames": ["p_end_date_sk"], "DatabaseName": "tpc", "Name": "dl_tpc_promotion" } }, "Permissions": [ "SELECT" ], "PermissionsWithGrantOption": [] }`This command produces no output. For more information, see [Granting and revoking permissions on Data Catalog resources](https://docs.aws.amazon.com/lake-formation/latest/dg/granting-catalog-permissions.html)in the*AWS Lake Formation Developer Guide*.**Example 3: To grant table permissions to the principal**The following `grant-permissions`example grants select permission on all tables of given database to the principal.`aws lakeformation grant-permissions \ --cli-input-json``file://input.json`Contents of `input.json`:`{ "CatalogId": "123456789111", "Principal": { "DataLakePrincipalIdentifier": "arn:aws:iam::123456789111:user/lf-developer" }, "Resource": { "Table": { "CatalogId": "123456789111", "DatabaseName": "tpc", "TableWildcard": {} } }, "Permissions": [ "SELECT" ], "PermissionsWithGrantOption": [] }`This command produces no output. For more information, see [Granting and revoking permissions on Data Catalog resources](https://docs.aws.amazon.com/lake-formation/latest/dg/granting-catalog-permissions.html)in the*AWS Lake Formation Developer Guide*.**Example 4: To grant permissions on LF-Tags to the principal**The following `grant-permissions`example grants associate permission on LF-Tags to the principal.`aws lakeformation grant-permissions \ --cli-input-json``file://input.json`Contents of `input.json`:`{ "CatalogId": "123456789111", "Principal": { "DataLakePrincipalIdentifier": "arn:aws:iam::123456789111:user/lf-developer" }, "Resource": { "LFTag": { "CatalogId": "123456789111", "TagKey": "category", "TagValues": [ "private", "public" ] } }, "Permissions": [ "ASSOCIATE" ], "PermissionsWithGrantOption": [] }`This command produces no output. For more information, see [Granting and revoking permissions on Data Catalog resources](https://docs.aws.amazon.com/lake-formation/latest/dg/granting-catalog-permissions.html)in the*AWS Lake Formation Developer Guide*.**Example 5: To grant permissions on data locations to the principal**The following `grant-permissions`example grants permission on data location to the principal.`aws lakeformation grant-permissions \ --cli-input-json``file://input.json`Contents of `input.json`:`{ "CatalogId": "123456789111", "Principal": { "DataLakePrincipalIdentifier": "arn:aws:iam::123456789111:user/lf-developer" }, "Resource": { "DataLocation": { "CatalogId": "123456789111", "ResourceArn": "arn:aws:s3:::lf-data-lake-123456789111" } }, "Permissions": [ "DATA_LOCATION_ACCESS" ], "PermissionsWithGrantOption": [] }`This command produces no output. For more information, see [Granting and revoking permissions on Data Catalog resources](https://docs.aws.amazon.com/lake-formation/latest/dg/granting-catalog-permissions.html)in the*AWS Lake Formation Developer Guide*.- 
                    For API details, see [GrantPermissions](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lakeformation/grant-permissions.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `list-data-cells-filter`.

- **AWS CLI**
- 
            
                    **To list data cell filters**The following `list-data-cells-filter`example list data cell filter for given table.`aws lakeformation list-data-cells-filter \ --cli-input-json``file://input.json`Contents of `input.json`:`{ "MaxResults": 2, "Table": { "CatalogId": "123456789111", "DatabaseName": "tpc", "Name": "dl_tpc_promotion" } }`Output: `{ "DataCellsFilters": [{ "TableCatalogId": "123456789111", "DatabaseName": "tpc", "TableName": "dl_tpc_promotion", "Name": "developer_promotion", "RowFilter": { "FilterExpression": "p_promo_name='ese'" }, "ColumnNames": [ "p_channel_details", "p_start_date_sk", "p_purpose", "p_promo_id", "p_promo_name", "p_end_date_sk", "p_discount_active" ] }, { "TableCatalogId": "123456789111", "DatabaseName": "tpc", "TableName": "dl_tpc_promotion", "Name": "developer_promotion_allrows", "RowFilter": { "FilterExpression": "TRUE", "AllRowsWildcard": {} }, "ColumnNames": [ "p_channel_details", "p_start_date_sk", "p_promo_name" ] } ], "NextToken": "2MDA2MTgwNiwibmFub3MiOjE0MDAwMDAwMH19" }`For more information, see [Data filtering and cell-level security in Lake Formation](https://docs.aws.amazon.com/lake-formation/latest/dg/data-filtering.html)in the*AWS Lake Formation Developer Guide*.- 
                    For API details, see [ListDataCellsFilter](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lakeformation/list-data-cells-filter.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `list-lf-tags`.

- **AWS CLI**
- 
            
                    **To list LF-tags**The following `list-lf-tags`example returns list of LF-tags that the requester has permission to view.`aws lakeformation list-lf-tags \ --cli-input-json``file://input.json`Contents of `input.json`:`{ "CatalogId": "123456789111", "ResourceShareType": "ALL", "MaxResults": 2 }`Output: `{ "LFTags": [{ "CatalogId": "123456789111", "TagKey": "category", "TagValues": [ "private", "public" ] }, { "CatalogId": "123456789111", "TagKey": "group", "TagValues": [ "analyst", "campaign", "developer" ] }], "NextToken": "kIiwiZXhwaXJhdGlvbiI6eyJzZWNvbmRzIjoxNjYwMDY4dCI6ZmFsc2V9" }`For more information, see [Managing LF-Tags for metadata access control](https://docs.aws.amazon.com/lake-formation/latest/dg/managing-tags.html)in the*AWS Lake Formation Developer Guide*.- 
                    For API details, see [ListLfTags](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lakeformation/list-lf-tags.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `list-permissions`.

- **AWS CLI**
- 
            
                    **Example 1: To retrieve list of principal permissions on the resource**The following `list-permissions`example returns a list of principal permissions on the database resources.`aws lakeformation list-permissions \ --cli-input-json``file://input.json`Contents of `input.json`:`{ "CatalogId": "123456789111", "ResourceType": "DATABASE", "MaxResults": 2 }`Output: `{ "PrincipalResourcePermissions": [{ "Principal": { "DataLakePrincipalIdentifier": "arn:aws:iam::123456789111:user/lf-campaign-manager" }, "Resource": { "Database": { "CatalogId": "123456789111", "Name": "tpc" } }, "Permissions": [ "DESCRIBE" ], "PermissionsWithGrantOption": [] }], "NextToken": "E5SlJDSTZleUp6SWpvaU9UQTNORE0zTXpFeE5Ua3pJbjE5TENKbGVIQnBjbUYwYVc5dUlqcDdJbk5sWTI5dVpITWlPakUyTm" }`For more information, see [Managing Lake Formation permissions](https://docs.aws.amazon.com/lake-formation/latest/dg/managing-permissions.html)in the*AWS Lake Formation Developer Guide*.**Example 2: To retrieve list of principal permissions on the table with data filters**The following `list-permissions`example list the permissions on the table with related data filters granted to the principal.`aws lakeformation list-permissions \ --cli-input-json``file://input.json`Contents of `input.json`:`{ "CatalogId": "123456789111", "Resource": { "Table": { "CatalogId": "123456789111", "DatabaseName": "tpc", "Name": "dl_tpc_customer" } }, "IncludeRelated": "TRUE", "MaxResults": 10 }`Output: `{ "PrincipalResourcePermissions": [{ "Principal": { "DataLakePrincipalIdentifier": "arn:aws:iam::123456789111:role/Admin" }, "Resource": { "Table": { "CatalogId": "123456789111", "DatabaseName": "customer", "Name": "customer_invoice" } }, "Permissions": [ "ALL", "ALTER", "DELETE", "DESCRIBE", "DROP", "INSERT" ], "PermissionsWithGrantOption": [ "ALL", "ALTER", "DELETE", "DESCRIBE", "DROP", "INSERT" ] }, { "Principal": { "DataLakePrincipalIdentifier": "arn:aws:iam::123456789111:role/Admin" }, "Resource": { "TableWithColumns": { "CatalogId": "123456789111", "DatabaseName": "customer", "Name": "customer_invoice", "ColumnWildcard": {} } }, "Permissions": [ "SELECT" ], "PermissionsWithGrantOption": [ "SELECT" ] }, { "Principal": { "DataLakePrincipalIdentifier": "arn:aws:iam::123456789111:role/Admin" }, "Resource": { "DataCellsFilter": { "TableCatalogId": "123456789111", "DatabaseName": "customer", "TableName": "customer_invoice", "Name": "dl_us_customer" } }, "Permissions": [ "DESCRIBE", "SELECT", "DROP" ], "PermissionsWithGrantOption": [] } ], "NextToken": "VyeUFjY291bnRQZXJtaXNzaW9ucyI6ZmFsc2V9" }`For more information, see [Managing Lake Formation permissions](https://docs.aws.amazon.com/lake-formation/latest/dg/managing-permissions.html)in the*AWS Lake Formation Developer Guide*.**Example 3: To retrieve list of principal permissions on the LF-Tags**The following `list-permissions`example list the permissions on the LF-Tags granted to the principal.`aws lakeformation list-permissions \ --cli-input-json``file://input.json`Contents of `input.json`:`{ "CatalogId": "123456789111", "Resource": { "LFTag": { "CatalogId": "123456789111", "TagKey": "category", "TagValues": [ "private" ] } }, "MaxResults": 10 }`Output: `{ "PrincipalResourcePermissions": [{ "Principal": { "DataLakePrincipalIdentifier": "arn:aws:iam::123456789111:user/lf-admin" }, "Resource": { "LFTag": { "CatalogId": "123456789111", "TagKey": "category", "TagValues": [ "*" ] } }, "Permissions": [ "DESCRIBE" ], "PermissionsWithGrantOption": [ "DESCRIBE" ] }, { "Principal": { "DataLakePrincipalIdentifier": "arn:aws:iam::123456789111:user/lf-admin" }, "Resource": { "LFTag": { "CatalogId": "123456789111", "TagKey": "category", "TagValues": [ "*" ] } }, "Permissions": [ "ASSOCIATE" ], "PermissionsWithGrantOption": [ "ASSOCIATE" ] } ], "NextToken": "EJwY21GMGFXOXVJanA3SW5Ocm1pc3Npb25zIjpmYWxzZX0=" }`For more information, see [Managing Lake Formation permissions](https://docs.aws.amazon.com/lake-formation/latest/dg/managing-permissions.html)in the*AWS Lake Formation Developer Guide*.- 
                    For API details, see [ListPermissions](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lakeformation/list-permissions.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `list-resources`.

- **AWS CLI**
- 
            
                    **To lists the resources managed by the Lake Formation**The following `list-resources`example lists the resources matching the condition that is managed by the Lake Formation.`aws lakeformation list-resources \ --cli-input-json``file://input.json`Contents of `input.json`:`{ "FilterConditionList": [{ "Field": "ROLE_ARN", "ComparisonOperator": "CONTAINS", "StringValueList": [ "123456789111" ] }], "MaxResults": 10 }`Output: `{ "ResourceInfoList": [{ "ResourceArn": "arn:aws:s3:::lf-data-lake-123456789111", "RoleArn": "arn:aws:iam::123456789111:role/LF-GlueServiceRole", "LastModified": "2022-07-21T02:12:46.669000+00:00" }, { "ResourceArn": "arn:aws:s3:::lf-emr-test-123456789111", "RoleArn": "arn:aws:iam::123456789111:role/EMRLFS3Role", "LastModified": "2022-07-29T16:22:03.211000+00:00" } ] }`For more information, see [Managing Lake Formation permissions](https://docs.aws.amazon.com/lake-formation/latest/dg/managing-permissions.html)in the*AWS Lake Formation Developer Guide*.- 
                    For API details, see [ListResources](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lakeformation/list-resources.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `list-transactions`.

- **AWS CLI**
- 
            
                    **To list all transactions details**The following `list-transactions`example returns metadata about transactions and their status.`aws lakeformation list-transactions \ --cli-input-json``file://input.json`Contents of `input.json`:`{ "CatalogId": "123456789111", "StatusFilter": "ALL", "MaxResults": 3 }`Output: `{ "Transactions": [{ "TransactionId": "1234569f08804cb790d950d4d0fe485e", "TransactionStatus": "committed", "TransactionStartTime": "2022-08-10T14:32:29.220000+00:00", "TransactionEndTime": "2022-08-10T14:32:33.751000+00:00" }, { "TransactionId": "12345972ca8347b89825e33c5774aec4", "TransactionStatus": "committed", "TransactionStartTime": "2022-08-10T14:29:04.046000+00:00", "TransactionEndTime": "2022-08-10T14:29:09.681000+00:00" }, { "TransactionId": "12345daf6cb047dbba8ad9b0414613b2", "TransactionStatus": "committed", "TransactionStartTime": "2022-08-10T13:56:51.261000+00:00", "TransactionEndTime": "2022-08-10T13:56:51.547000+00:00" } ], "NextToken": "77X1ebypsI7os+X2lhHsZLGNCDK3nNGpwRdFpicSOHgcX1/QMoniUAKcpR3kj3ts3PVdMA==" }`For more information, see [Reading from and writing to the data lake within transactions](https://docs.aws.amazon.com/lake-formation/latest/dg/transaction-ops.html)in the*AWS Lake Formation Developer Guide*.- 
                    For API details, see [ListTransactions](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lakeformation/list-transactions.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `put-data-lake-settings`.

- **AWS CLI**
- 
            
                    **To set AWS Lake Formation-managed data lake settings**The following `put-data-lake-settings`example sets the list of data lake administrators and other data lake settings.`aws lakeformation put-data-lake-settings \ --cli-input-json``file://input.json`Contents of `input.json`:`{ "DataLakeSettings": { "DataLakeAdmins": [{ "DataLakePrincipalIdentifier": "arn:aws:iam::123456789111:user/lf-admin" } ], "CreateDatabaseDefaultPermissions": [], "CreateTableDefaultPermissions": [], "TrustedResourceOwners": [], "AllowExternalDataFiltering": true, "ExternalDataFilteringAllowList": [{ "DataLakePrincipalIdentifier ": "123456789111" }], "AuthorizedSessionTagValueList": ["Amazon EMR"] } }`This command produces no output. For more information, see [Changing the default security settings for your data lake](https://docs.aws.amazon.com/lake-formation/latest/dg/change-settings.html)in the*AWS Lake Formation Developer Guide*.- 
                    For API details, see [PutDataLakeSettings](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lakeformation/put-data-lake-settings.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `register-resource`.

- **AWS CLI**
- 
            
                    **Example 1: To register data lake storage using Service Linked Role**The following `register-resource`example registers the resource as managed by the Lake Formation using Service linked role.`aws lakeformation register-resource \ --cli-input-json``file://input.json`Contents of `input.json`:`{ "ResourceArn": "arn:aws:s3:::lf-emr-athena-result-123", "UseServiceLinkedRole": true }`This command produces no output. For more information, see [Adding an Amazon S3 location to your data lake](https://docs.aws.amazon.com/lake-formation/latest/dg/register-data-lake.html)in the*AWS Lake Formation Developer Guide*.**Example 2: To register data lake storage using custom role**The following `register-resource`example registers the resource as managed by the Lake Formation using custom role.`aws lakeformation register-resource \ --cli-input-json``file://input.json`Contents of `input.json`:`{ "ResourceArn": "arn:aws:s3:::lf-emr-athena-result-123", "UseServiceLinkedRole": false, "RoleArn": "arn:aws:iam::123456789111:role/LF-GlueServiceRole" }`This command produces no output. For more information, see [Adding an Amazon S3 location to your data lake](https://docs.aws.amazon.com/lake-formation/latest/dg/register-data-lake.html)in the*AWS Lake Formation Developer Guide*.- 
                    For API details, see [RegisterResource](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lakeformation/register-resource.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `remove-lf-tags-from-resource`.

- **AWS CLI**
- 
            
                    **To remove LF-Tag from a resource**The following `remove-lf-tags-from-resource`example removes the LF-Tag association with the table resource.`aws lakeformation remove-lf-tags-from-resource \ --cli-input-json``file://input.json`Contents of `input.json`:`{ "CatalogId": "123456789111", "Resource": { "Table": { "CatalogId": "123456789111", "DatabaseName": "tpc", "Name": "dl_tpc_promotion" } }, "LFTags": [{ "CatalogId": "123456789111", "TagKey": "usergroup", "TagValues": [ "developer" ] }] }`Output: `{ "Failures": [] }`For more information, see [Assigning LF-Tags to Data Catalog resources](https://docs.aws.amazon.com/lake-formation/latest/dg/TBAC-assigning-tags.html)in the*AWS Lake Formation Developer Guide*.- 
                    For API details, see [RemoveLfTagsFromResource](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lakeformation/remove-lf-tags-from-resource.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `revoke-permissions`.

- **AWS CLI**
- 
            
                    **To revoke permissions on resources from the principal**The following `revoke-permissions`example revoke principal access to specific table of a given database.`aws lakeformation revoke-permissions \ --cli-input-json``file://input.json`Contents of `input.json`:`{ "CatalogId": "123456789111", "Principal": { "DataLakePrincipalIdentifier": "arn:aws:iam::123456789111:user/lf-developer" }, "Resource": { "Table": { "CatalogId": "123456789111", "DatabaseName": "tpc", "Name": "dl_tpc_promotion" } }, "Permissions": [ "ALL" ], "PermissionsWithGrantOption": [] }`This command produces no output. For more information, see [Granting and revoking permissions on Data Catalog resources](https://docs.aws.amazon.com/lake-formation/latest/dg/granting-catalog-permissions.html)in the*AWS Lake Formation Developer Guide*.- 
                    For API details, see [RevokePermissions](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lakeformation/revoke-permissions.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `search-databases-by-lf-tags`.

- **AWS CLI**
- 
            
                    **To search on database resources by LFTags**The following `search-databases-by-lf-tags`example search on database resources matching LFTag expression.`aws lakeformation search-databases-by-lf-tags \ --cli-input-json``file://input.json`Contents of `input.json`:`{ "MaxResults": 1, "CatalogId": "123456789111", "Expression": [{ "TagKey": "usergroup", "TagValues": [ "developer" ] }] }`Output: `{ "DatabaseList": [{ "Database": { "CatalogId": "123456789111", "Name": "tpc" }, "LFTags": [{ "CatalogId": "123456789111", "TagKey": "usergroup", "TagValues": [ "developer" ] }] }] }`For more information, see [Viewing the resources that a LF-Tag is assigned to](https://docs.aws.amazon.com/lake-formation/latest/dg/TBAC-view-tag-resources.html)in the*AWS Lake Formation Developer Guide*.- 
                    For API details, see [SearchDatabasesByLfTags](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lakeformation/search-databases-by-lf-tags.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `search-tables-by-lf-tags`.

- **AWS CLI**
- 
            
                    **To search on table resources by LFTags**The following `search-tables-by-lf-tags`example search on table resources matching LFTag expression.`aws lakeformation search-tables-by-lf-tags \ --cli-input-json``file://input.json`Contents of `input.json`:`{ "MaxResults": 2, "CatalogId": "123456789111", "Expression": [{ "TagKey": "usergroup", "TagValues": [ "developer" ] }] }`Output: `{ "NextToken": "c2VhcmNoQWxsVGFnc0luVGFibGVzIjpmYWxzZX0=", "TableList": [{ "Table": { "CatalogId": "123456789111", "DatabaseName": "tpc", "Name": "dl_tpc_item" }, "LFTagOnDatabase": [{ "CatalogId": "123456789111", "TagKey": "usergroup", "TagValues": [ "developer" ] }], "LFTagsOnTable": [{ "CatalogId": "123456789111", "TagKey": "usergroup", "TagValues": [ "developer" ] }], "LFTagsOnColumns": [{ "Name": "i_item_desc", "LFTags": [{ "CatalogId": "123456789111", "TagKey": "usergroup", "TagValues": [ "developer" ] }] }, { "Name": "i_container", "LFTags": [{ "CatalogId": "123456789111", "TagKey": "usergroup", "TagValues": [ "developer" ] }] }, { "Name": "i_wholesale_cost", "LFTags": [{ "CatalogId": "123456789111", "TagKey": "usergroup", "TagValues": [ "developer" ] }] }, { "Name": "i_manufact_id", "LFTags": [{ "CatalogId": "123456789111", "TagKey": "usergroup", "TagValues": [ "developer" ] }] }, { "Name": "i_brand_id", "LFTags": [{ "CatalogId": "123456789111", "TagKey": "usergroup", "TagValues": [ "developer" ] }] }, { "Name": "i_formulation", "LFTags": [{ "CatalogId": "123456789111", "TagKey": "usergroup", "TagValues": [ "developer" ] }] }, { "Name": "i_current_price", "LFTags": [{ "CatalogId": "123456789111", "TagKey": "usergroup", "TagValues": [ "developer" ] }] }, { "Name": "i_size", "LFTags": [{ "CatalogId": "123456789111", "TagKey": "usergroup", "TagValues": [ "developer" ] }] }, { "Name": "i_rec_start_date", "LFTags": [{ "CatalogId": "123456789111", "TagKey": "usergroup", "TagValues": [ "developer" ] }] }, { "Name": "i_manufact", "LFTags": [{ "CatalogId": "123456789111", "TagKey": "usergroup", "TagValues": [ "developer" ] }] }, { "Name": "i_item_sk", "LFTags": [{ "CatalogId": "123456789111", "TagKey": "usergroup", "TagValues": [ "developer" ] }] }, { "Name": "i_manager_id", "LFTags": [{ "CatalogId": "123456789111", "TagKey": "usergroup", "TagValues": [ "developer" ] }] }, { "Name": "i_item_id", "LFTags": [{ "CatalogId": "123456789111", "TagKey": "usergroup", "TagValues": [ "developer" ] }] }, { "Name": "i_class_id", "LFTags": [{ "CatalogId": "123456789111", "TagKey": "usergroup", "TagValues": [ "developer" ] }] }, { "Name": "i_class", "LFTags": [{ "CatalogId": "123456789111", "TagKey": "usergroup", "TagValues": [ "developer" ] }] }, { "Name": "i_category", "LFTags": [{ "CatalogId": "123456789111", "TagKey": "usergroup", "TagValues": [ "developer" ] }] }, { "Name": "i_category_id", "LFTags": [{ "CatalogId": "123456789111", "TagKey": "usergroup", "TagValues": [ "developer" ] }] }, { "Name": "i_brand", "LFTags": [{ "CatalogId": "123456789111", "TagKey": "usergroup", "TagValues": [ "developer" ] }] }, { "Name": "i_units", "LFTags": [{ "CatalogId": "123456789111", "TagKey": "usergroup", "TagValues": [ "developer" ] }] }, { "Name": "i_rec_end_date", "LFTags": [{ "CatalogId": "123456789111", "TagKey": "usergroup", "TagValues": [ "developer" ] }] }, { "Name": "i_color", "LFTags": [{ "CatalogId": "123456789111", "TagKey": "usergroup", "TagValues": [ "developer" ] }] }, { "Name": "i_product_name", "LFTags": [{ "CatalogId": "123456789111", "TagKey": "usergroup", "TagValues": [ "developer" ] }] } ] }] }`For more information, see [Viewing the resources that a LF-Tag is assigned to](https://docs.aws.amazon.com/lake-formation/latest/dg/TBAC-view-tag-resources.html)in the*AWS Lake Formation Developer Guide*.- 
                    For API details, see [SearchTablesByLfTags](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lakeformation/search-tables-by-lf-tags.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `start-query-planning`.

- **AWS CLI**
- 
            
                    **To process query statement**The following `start-query-planning`example submits a request to process a query statement.`aws lakeformation start-query-planning \ --cli-input-json``file://input.json`Contents of `input.json`:`{ "QueryPlanningContext": { "CatalogId": "012345678901", "DatabaseName": "tpc" }, "QueryString": "select * from dl_tpc_household_demographics_gov where hd_income_band_sk=9" }`Output: `{ "QueryId": "772a273f-4a62-4cda-8d98-69615ee8be9b" }`For more information, see [Reading from and writing to the data lake within transactions](https://docs.aws.amazon.com/lake-formation/latest/dg/transaction-ops.html)in the*AWS Lake Formation Developer Guide*.- 
                    For API details, see [StartQueryPlanning](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lakeformation/start-query-planning.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `start-transaction`.

- **AWS CLI**
- 
            
                    **To start new transaction**The following `start-transaction`example starts a new transaction and returns its transaction ID.`aws lakeformation start-transaction \ --transaction-type``=`'`READ_AND_WRITE`'Output: `{ "TransactionId": "b014d972ca8347b89825e33c5774aec4" }`For more information, see [Reading from and writing to the data lake within transactions](https://docs.aws.amazon.com/lake-formation/latest/dg/transaction-ops.html)in the*AWS Lake Formation Developer Guide*.- 
                    For API details, see [StartTransaction](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lakeformation/start-transaction.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `update-lf-tag`.

- **AWS CLI**
- 
            
                    **To update LF-Tag definition**The following `update-lf-tag`example updates LF-Tag definition.`aws lakeformation update-lf-tag \ --catalog-id '``123456789111`' \ --tag-key '`usergroup`' \ --tag-values-to-add '`["admin"]`'This command produces no output. For more information, see [Managing LF-Tags for metadata access control](https://docs.aws.amazon.com/lake-formation/latest/dg/managing-tags.html)in the*AWS Lake Formation Developer Guide*.- 
                    For API details, see [UpdateLfTag](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lakeformation/update-lf-tag.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `update-table-objects`.

- **AWS CLI**
- 
            
                    **To modify objects of governed table**The following `update-table-objects`example adds provided S3 objects to the specified governed table.`aws lakeformation update-table-objects \ --cli-input-json``file://input.json`Contents of `input.json`:`{ "CatalogId": "012345678901", "DatabaseName": "tpc", "TableName": "dl_tpc_household_demographics_gov", "TransactionId": "12347a9f75424b9b915f6ff201d2a190", "WriteOperations": [{ "AddObject": { "Uri": "s3://lf-data-lake-012345678901/target/dl_tpc_household_demographics_gov/run-unnamed-1-part-block-0-r-00000-snappy-ff26b17504414fe88b302cd795eabd00.parquet", "ETag": "1234ab1fc50a316b149b4e1f21a73800", "Size": 42200 } }] }`This command produces no output. For more information, see [Reading from and writing to the data lake within transactions](https://docs.aws.amazon.com/lake-formation/latest/dg/transaction-ops.html)in the*AWS Lake Formation Developer Guide*.- 
                    For API details, see [UpdateTableObjects](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lakeformation/update-table-objects.html)in*AWS CLI Command Reference*.
 
-