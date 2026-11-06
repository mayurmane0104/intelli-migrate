# Athena examples using AWS CLI - AWS Command Line Interface

**Source:** [https://docs.aws.amazon.com/cli/latest/userguide/cli_athena_code_examples.html](https://docs.aws.amazon.com/cli/latest/userguide/cli_athena_code_examples.html)

---

The following code examples show you how to perform actions and implement common scenarios by using the AWS Command Line Interface with Athena.

*Actions* are code excerpts from larger programs and must be run in context. While actions show you how to call individual service functions, you can see actions in context in their related scenarios.

Each example includes a link to the complete source code, where you can find instructions on how to set up and run the code in context.

###### Topics

## Actions

    The following code example shows how to use `batch-get-named-query`.

- **AWS CLI**
- 
            
                    **To return information about more than one query**The following `batch-get-named-query`example returns information about the named queries that have the specified IDs.`aws athena batch-get-named-query \ --named-query-ids``a1b2c3d4-5678-90ab-cdef-EXAMPLE11111``a1b2c3d4-5678-90ab-cdef-EXAMPLE22222``a1b2c3d4-5678-90ab-cdef-EXAMPLE33333`Output: `{ "NamedQueries": [ { "Name": "Flights Select Query", "Description": "Sample query to get the top 10 airports with the most number of departures since 2000", "Database": "sampledb", "QueryString": "SELECT origin, count(*) AS total_departures\nFROM\nflights_parquet\nWHERE year >= '2000'\nGROUP BY origin\nORDER BY total_departures DESC\nLIMIT 10;", "NamedQueryId": "a1b2c3d4-5678-90ab-cdef-EXAMPLE11111", "WorkGroup": "primary" }, { "Name": "Load flights table partitions", "Description": "Sample query to load flights table partitions using MSCK REPAIR TABLE statement", "Database": "sampledb", "QueryString": "MSCK REPAIR TABLE flights_parquet;", "NamedQueryId": "a1b2c3d4-5678-90ab-cdef-EXAMPLE22222", "WorkGroup": "primary" }, { "Name": "CloudFront Select Query", "Description": "Sample query to view requests per operating system during a particular time frame", "Database": "sampledb", "QueryString": "SELECT os, COUNT(*) count FROM cloudfront_logs WHERE date BETWEEN date '2014-07-05' AND date '2014-08-05' GROUP BY os;", "NamedQueryId": "a1b2c3d4-5678-90ab-cdef-EXAMPLE33333", "WorkGroup": "primary" } ], "UnprocessedNamedQueryIds": [] }`For more information, see [Running SQL Queries Using Amazon Athena](https://docs.aws.amazon.com/athena/latest/ug/querying-athena-tables.html)in the*Amazon Athena User Guide*.- 
                    For API details, see [BatchGetNamedQuery](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/athena/batch-get-named-query.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `batch-get-query-execution`.

- **AWS CLI**
- 
            
                    **To return information about one or more query executions**The following `batch-get-query-execution`example returns query execution information for the queries that have the specified query IDs.`aws athena batch-get-query-execution \ --query-execution-ids``a1b2c3d4-5678-90ab-cdef-EXAMPLE11111``a1b2c3d4-5678-90ab-cdef-EXAMPLE22222`Output: `{ "QueryExecutions": [ { "QueryExecutionId": "a1b2c3d4-5678-90ab-cdef-EXAMPLE11111", "Query": "create database if not exists webdata", "StatementType": "DDL", "ResultConfiguration": { "OutputLocation": "s3://amzn-s3-demo-bucket/a1b2c3d4-5678-90ab-cdef-EXAMPLE11111.txt" }, "QueryExecutionContext": {}, "Status": { "State": "SUCCEEDED", "SubmissionDateTime": 1593470720.592, "CompletionDateTime": 1593470720.902 }, "Statistics": { "EngineExecutionTimeInMillis": 232, "DataScannedInBytes": 0, "TotalExecutionTimeInMillis": 310, "ResultConfiguration": { "QueryQueueTimeInMillis": 50, "ServiceProcessingTimeInMillis": 28 }, "WorkGroup": "AthenaAdmin" }, { "QueryExecutionId": "a1b2c3d4-5678-90ab-cdef-EXAMPLE22222", "Query": "select date, location, browser, uri, status from cloudfront_logs where method = 'GET' and status = 200 and location like 'SFO%' limit 10", "StatementType": "DML", "ResultConfiguration": { "OutputLocation": "s3://amzn-s3-demo-bucket/a1b2c3d4-5678-90ab-cdef-EXAMPLE22222.csv" }, "QueryExecutionContext": { "Database": "mydatabase", "Catalog": "awsdatacatalog" }, "Status": { "State": "SUCCEEDED", "SubmissionDateTime": 1593469842.665, "CompletionDateTime": 1593469846.486 }, "Statistics": { "EngineExecutionTimeInMillis": 3600, "DataScannedInBytes": 203089, "TotalExecutionTimeInMillis": 3821, "QueryQueueTimeInMillis": 267, "QueryPlanningTimeInMillis": 1175 }, "WorkGroup": "AthenaAdmin" } ], "UnprocessedQueryExecutionIds": [] }`For more information, see [Running SQL Queries Using Amazon Athena](https://docs.aws.amazon.com/athena/latest/ug/querying-athena-tables.html)in the*Amazon Athena User Guide*.- 
                    For API details, see [BatchGetQueryExecution](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/athena/batch-get-query-execution.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `create-data-catalog`.

- **AWS CLI**
- 
            
                    **To create a data catalog**The following `create-data-catalog`example creates the`dynamo_db_catalog`data catalog.`aws athena create-data-catalog \ --name``dynamo_db_catalog`\ --type`LAMBDA`\ --description`"DynamoDB Catalog"`\ --parameters`function=arn:aws:lambda:us-west-2:111122223333:function:dynamo_db_lambda`This command produces no output. To see the result, use `aws athena get-data-catalog --name dynamo_db_catalog`.For more information, see [Registering a Catalog: create-data-catalog](https://docs.aws.amazon.com/athena/latest/ug/datastores-hive-cli.html#datastores-hive-cli-registering-a-catalog)in the*Amazon Athena User Guide*.- 
                    For API details, see [CreateDataCatalog](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/athena/create-data-catalog.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `create-named-query`.

- **AWS CLI**
- 
            
                    **To create a named query**The following `create-named-query`example creates a saved query in the`AthenaAdmin`workgroup that queries the`flights_parquet`table for flights from Seattle to New York in January, 2016 whose departure and arrival were both delayed by more than ten minutes. Because the airport code values in the table are strings that include double quotes (for example, "SEA"), they are escaped by backslashes and surrounded by single quotes.`aws athena create-named-query \ --name``"SEA to JFK delayed flights Jan 2016"`\ --description`"Both arrival and departure delayed more than 10 minutes."`\ --database`sampledb`\ --query-string "SELECT flightdate, carrier, flightnum, origin, dest, depdelayminutes, arrdelayminutes FROM sampledb.flights_parquet WHERE yr = 2016 AND month = 1 AND origin = '\"SEA\"' AND dest = '\"JFK\"' AND depdelayminutes > 10 AND arrdelayminutes > 10" \ --work-group`AthenaAdmin`Output: `{ "NamedQueryId": "a1b2c3d4-5678-90ab-cdef-EXAMPLE11111" }`For more information, see [Running SQL Queries Using Amazon Athena](https://docs.aws.amazon.com/athena/latest/ug/querying-athena-tables.html)in the*Amazon Athena User Guide*.- 
                    For API details, see [CreateNamedQuery](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/athena/create-named-query.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `create-work-group`.

- **AWS CLI**
- 
            
                    **To create a workgroup**The following `create-work-group`example creates a workgroup called`Data_Analyst_Group`that has the query results output location`s3://amzn-s3-demo-bucket`. The command creates a workgroup that overrides client configuration settings, which includes the query results output location. The command also enables CloudWatch metrics and adds three key-value tag pairs to the workgroup to distinguish it from other workgroups. Note that the`--configuration`argument has no spaces before the commas that separate its options.`aws athena create-work-group \ --name``Data_Analyst_Group`\ --configuration ResultConfiguration={OutputLocation="s3://amzn-s3-demo-bucket"},EnforceWorkGroupConfiguration="true",PublishCloudWatchMetricsEnabled="true" \ --description`"Workgroup for data analysts"`\ --tags`Key=Division,Value=West``Key=Location,Value=Seattle`Key=Team,Value="Big Data"This command produces no output. To see the results, use `aws athena get-work-group --work-group Data_Analyst_Group`.For more information, see [Managing Workgroups](https://docs.aws.amazon.com/athena/latest/ug/workgroups-create-update-delete.html)in the*Amazon Athena User Guide*.- 
                    For API details, see [CreateWorkGroup](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/athena/create-work-group.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `delete-data-catalog`.

- **AWS CLI**
- 
            
                    **To delete a data catalog**The following `delete-data-catalog`example deletes the`UnusedDataCatalog`data catalog.`aws athena delete-data-catalog \ --name``UnusedDataCatalog`This command produces no output. For more information, see [Deleting a Catalog: delete-data-catalog](https://docs.aws.amazon.com/athena/latest/ug/datastores-hive-cli.html#datastores-hive-cli-deleting-a-catalog)in the*Amazon Athena User Guide*.- 
                    For API details, see [DeleteDataCatalog](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/athena/delete-data-catalog.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `delete-named-query`.

- **AWS CLI**
- 
            
                    **To delete a named query**The following `delete-named-query`example deletes the named query that has the specified ID.`aws athena delete-named-query \ --named-query-id``a1b2c3d4-5678-90ab-cdef-EXAMPLE11111`This command produces no output. For more information, see [Running SQL Queries Using Amazon Athena](https://docs.aws.amazon.com/athena/latest/ug/querying-athena-tables.html)in the*Amazon Athena User Guide*.- 
                    For API details, see [DeleteNamedQuery](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/athena/delete-named-query.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `delete-work-group`.

- **AWS CLI**
- 
            
                    **To delete a workgroup**The following `delete-work-group`example deletes the`TeamB`workgroup.`aws athena delete-work-group \ --work-group``TeamB`This command produces no output. To confirm the deletion, use `aws athena list-work-groups`.For more information, see [Managing Workgroups](https://docs.aws.amazon.com/athena/latest/ug/workgroups-create-update-delete.html)in the*Amazon Athena User Guide*.- 
                    For API details, see [DeleteWorkGroup](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/athena/delete-work-group.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `get-data-catalog`.

- **AWS CLI**
- 
            
                    **To return information about a data catalog**The following `get-data-catalog`example returns information about the`dynamo_db_catalog`data catalog.`aws athena get-data-catalog \ --name``dynamo_db_catalog`Output: `{ "DataCatalog": { "Name": "dynamo_db_catalog", "Description": "DynamoDB Catalog", "Type": "LAMBDA", "Parameters": { "catalog": "dynamo_db_catalog", "metadata-function": "arn:aws:lambda:us-west-2:111122223333:function:dynamo_db_lambda", "record-function": "arn:aws:lambda:us-west-2:111122223333:function:dynamo_db_lambda" } } }`For more information, see [Showing Catalog Details: get-data-catalog](https://docs.aws.amazon.com/athena/latest/ug/datastores-hive-cli.html#datastores-hive-cli-showing-details-of-a-catalog)in the*Amazon Athena User Guide*.- 
                    For API details, see [GetDataCatalog](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/athena/get-data-catalog.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `get-database`.

- **AWS CLI**
- 
            
                    **To return information about a database in a data catalog**The following `get-database`example returns information about the`sampledb`database in the`AwsDataCatalog`data catalog.`aws athena get-database \ --catalog-name``AwsDataCatalog`\ --database-name`sampledb`Output: `{ "Database": { "Name": "sampledb", "Description": "Sample database", "Parameters": { "CreatedBy": "Athena", "EXTERNAL": "TRUE" } } }`For more information, see [Showing Database Details: get-database](https://docs.aws.amazon.com/athena/latest/ug/datastores-hive-cli.html#datastores-hive-cli-showing-details-of-a-database)in the*Amazon Athena User Guide*.- 
                    For API details, see [GetDatabase](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/athena/get-database.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `get-named-query`.

- **AWS CLI**
- 
            
                    **To return a named query**The following `get-named-query`example returns information about the query that has the specified ID.`aws athena get-named-query \ --named-query-id``a1b2c3d4-5678-90ab-cdef-EXAMPLE11111`Output: `{ "NamedQuery": { "Name": "CloudFront Logs - SFO", "Description": "Shows successful GET request data for SFO", "Database": "default", "QueryString": "select date, location, browser, uri, status from cloudfront_logs where method = 'GET' and status = 200 and location like 'SFO%' limit 10", "NamedQueryId": "a1b2c3d4-5678-90ab-cdef-EXAMPLE11111", "WorkGroup": "AthenaAdmin" } }`For more information, see [Running SQL Queries Using Amazon Athena](https://docs.aws.amazon.com/athena/latest/ug/querying-athena-tables.html)in the*Amazon Athena User Guide*.- 
                    For API details, see [GetNamedQuery](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/athena/get-named-query.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `get-query-execution`.

- **AWS CLI**
- 
            
                    **To return information about a query execution**The following `get-query-execution`example returns information about the query that has the specified query ID.`aws athena get-query-execution \ --query-execution-id``a1b2c3d4-5678-90ab-cdef-EXAMPLE11111`Output: `{ "QueryExecution": { "QueryExecutionId": "a1b2c3d4-5678-90ab-cdef-EXAMPLE11111", "Query": "select date, location, browser, uri, status from cloudfront_logs where method = 'GET ' and status = 200 and location like 'SFO%' limit 10", "StatementType": "DML", "ResultConfiguration": { "OutputLocation": "s3://amzn-s3-demo-bucket/a1b2c3d4-5678-90ab-cdef-EXAMPLE11111.csv" }, "QueryExecutionContext": { "Database": "mydatabase", "Catalog": "awsdatacatalog" }, "Status": { "State": "SUCCEEDED", "SubmissionDateTime": 1593469842.665, "CompletionDateTime": 1593469846.486 }, "Statistics": { "EngineExecutionTimeInMillis": 3600, "DataScannedInBytes": 203089, "TotalExecutionTimeInMillis": 3821, "QueryQueueTimeInMillis": 267, "QueryPlanningTimeInMillis": 1175 }, "WorkGroup": "AthenaAdmin" } }`For more information, see [Running SQL Queries Using Amazon Athena](https://docs.aws.amazon.com/athena/latest/ug/querying-athena-tables.html)in the*Amazon Athena User Guide*.- 
                    For API details, see [GetQueryExecution](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/athena/get-query-execution.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `get-query-results`.

- **AWS CLI**
- 
            
                    **To return the results of a query**The following `get-query-results`example returns the results of the query that has the specified query ID.`aws athena get-query-results \ --query-execution-id``a1b2c3d4-5678-90ab-cdef-EXAMPLE11111`Output: `{ "ResultSet": { "Rows": [ { "Data": [ { "VarCharValue": "date" }, { "VarCharValue": "location" }, { "VarCharValue": "browser" }, { "VarCharValue": "uri" }, { "VarCharValue": "status" } ] }, { "Data": [ { "VarCharValue": "2014-07-05" }, { "VarCharValue": "SFO4" }, { "VarCharValue": "Safari" }, { "VarCharValue": "/test-image-2.jpeg" }, { "VarCharValue": "200" } ] }, { "Data": [ { "VarCharValue": "2014-07-05" }, { "VarCharValue": "SFO4" }, { "VarCharValue": "Opera" }, { "VarCharValue": "/test-image-2.jpeg" }, { "VarCharValue": "200" } ] }, { "Data": [ { "VarCharValue": "2014-07-05" }, { "VarCharValue": "SFO4" }, { "VarCharValue": "Firefox" }, { "VarCharValue": "/test-image-3.jpeg" }, { "VarCharValue": "200" } ] }, { "Data": [ { "VarCharValue": "2014-07-05" }, { "VarCharValue": "SFO4" }, { "VarCharValue": "Lynx" }, { "VarCharValue": "/test-image-3.jpeg" }, { "VarCharValue": "200" } ] }, { "Data": [ { "VarCharValue": "2014-07-05" }, { "VarCharValue": "SFO4" }, { "VarCharValue": "IE" }, { "VarCharValue": "/test-image-2.jpeg" }, { "VarCharValue": "200" } ] }, { "Data": [ { "VarCharValue": "2014-07-05" }, { "VarCharValue": "SFO4" }, { "VarCharValue": "Opera" }, { "VarCharValue": "/test-image-1.jpeg" }, { "VarCharValue": "200" } ] }, { "Data": [ { "VarCharValue": "2014-07-05" }, { "VarCharValue": "SFO4" }, { "VarCharValue": "Chrome" }, { "VarCharValue": "/test-image-3.jpeg" }, { "VarCharValue": "200" } ] }, { "Data": [ { "VarCharValue": "2014-07-05" }, { "VarCharValue": "SFO4" }, { "VarCharValue": "Firefox" }, { "VarCharValue": "/test-image-2.jpeg" }, { "VarCharValue": "200" } ] }, { "Data": [ { "VarCharValue": "2014-07-05" }, { "VarCharValue": "SFO4" }, { "VarCharValue": "Chrome" }, { "VarCharValue": "/test-image-3.jpeg" }, { "VarCharValue": "200" } ] }, { "Data": [ { "VarCharValue": "2014-07-05" }, { "VarCharValue": "SFO4" }, { "VarCharValue": "IE" }, { "VarCharValue": "/test-image-2.jpeg" }, { "VarCharValue": "200" } ] } ], "ResultSetMetadata": { "ColumnInfo": [ { "CatalogName": "hive", "SchemaName": "", "TableName": "", "Name": "date", "Label": "date", "Type": "date", "Precision": 0, "Scale": 0, "Nullable": "UNKNOWN", "CaseSensitive": false }, { "CatalogName": "hive", "SchemaName": "", "TableName": "", "Name": "location", "Label": "location", "Type": "varchar", "Precision": 2147483647, "Data": [ "Scale": 0, "Nullable": "UNKNOWN", "CaseSensitive": true }, { "CatalogName": "hive", "SchemaName": "", "TableName": "", "Name": "browser", "Label": "browser", "Type": "varchar", "Precision": 2147483647, "Scale": 0, "Nullable": "UNKNOWN", "CaseSensitive": true }, { "CatalogName": "hive", "SchemaName": "", "TableName": "", "Name": "uri", "Label": "uri", "Type": "varchar", "Precision": 2147483647, "Scale": 0, "Nullable": "UNKNOWN", "CaseSensitive": true }, { "CatalogName": "hive", "SchemaName": "", "TableName": "", "Name": "status", "Label": "status", "Type": "integer", "Precision": 10, "Scale": 0, "Nullable": "UNKNOWN", "CaseSensitive": false } ] } }, "UpdateCount": 0 }`For more information, see [Working with Query Results, Output Files, and Query History](https://docs.aws.amazon.com/athena/latest/ug/querying.html)in the*Amazon Athena User Guide*.- 
                    For API details, see [GetQueryResults](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/athena/get-query-results.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `get-table-metadata`.

- **AWS CLI**
- 
            
                    **To return metadata information about a table**The following `get-table-metadata`example returns metadata information about the`counties`table, including including column names and their datatypes, from the`sampledb`database of the`AwsDataCatalog`data catalog.`aws athena get-table-metadata \ --catalog-name``AwsDataCatalog`\ --database-name`sampledb`\ --table-name`counties`Output: `{ "TableMetadata": { "Name": "counties", "CreateTime": 1593559968.0, "LastAccessTime": 0.0, "TableType": "EXTERNAL_TABLE", "Columns": [ { "Name": "name", "Type": "string", "Comment": "from deserializer" }, { "Name": "boundaryshape", "Type": "binary", "Comment": "from deserializer" }, { "Name": "motto", "Type": "string", "Comment": "from deserializer" }, { "Name": "population", "Type": "int", "Comment": "from deserializer" } ], "PartitionKeys": [], "Parameters": { "EXTERNAL": "TRUE", "inputformat": "com.esri.json.hadoop.EnclosedJsonInputFormat", "location": "s3://amzn-s3-demo-bucket/json", "outputformat": "org.apache.hadoop.hive.ql.io.HiveIgnoreKeyTextOutputFormat", "serde.param.serialization.format": "1", "serde.serialization.lib": "com.esri.hadoop.hive.serde.JsonSerde", "transient_lastDdlTime": "1593559968" } } }`For more information, see [Showing Table Details: get-table-metadata](https://docs.aws.amazon.com/athena/latest/ug/datastores-hive-cli.html#datastores-hive-cli-showing-details-of-a-table)in the*Amazon Athena User Guide*.- 
                    For API details, see [GetTableMetadata](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/athena/get-table-metadata.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `get-work-group`.

- **AWS CLI**
- 
            
                    **To return information about a workgroup**The following `get-work-group`example returns information about the`AthenaAdmin`workgroup.`aws athena get-work-group \ --work-group``AthenaAdmin`Output: `{ "WorkGroup": { "Name": "AthenaAdmin", "State": "ENABLED", "Configuration": { "ResultConfiguration": { "OutputLocation": "s3://amzn-s3-demo-bucket/" }, "EnforceWorkGroupConfiguration": false, "PublishCloudWatchMetricsEnabled": true, "RequesterPaysEnabled": false }, "Description": "Workgroup for Athena administrators", "CreationTime": 1573677174.105 } }`For more information, see [Managing Workgroups](https://docs.aws.amazon.com/athena/latest/ug/workgroups-create-update-delete.html)in the*Amazon Athena User Guide*.- 
                    For API details, see [GetWorkGroup](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/athena/get-work-group.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `list-data-catalogs`.

- **AWS CLI**
- 
            
                    **To list the data catalogs registered with Athena**The following `list-data-catalogs`example lists the data catalogs registered with Athena.`aws athena list-data-catalogs`Output: `{ "DataCatalogsSummary": [ { "CatalogName": "AwsDataCatalog", "Type": "GLUE" }, { "CatalogName": "cw_logs_catalog", "Type": "LAMBDA" }, { "CatalogName": "cw_metrics_catalog", "Type": "LAMBDA" } ] }`For more information, see [Listing Registered Catalogs: list-data-catalogs](https://docs.aws.amazon.com/athena/latest/ug/datastores-hive-cli.html#datastores-hive-cli-listing-registered-catalogs)in the*Amazon Athena User Guide*.- 
                    For API details, see [ListDataCatalogs](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/athena/list-data-catalogs.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `list-databases`.

- **AWS CLI**
- 
            
                    **To list the databases in a data catalog**The following `list-databases`example lists the databases in the`AwsDataCatalog`data catalog.`aws athena list-databases \ --catalog-name``AwsDataCatalog`Output: `{ "DatabaseList": [ { "Name": "default" }, { "Name": "mydatabase" }, { "Name": "newdb" }, { "Name": "sampledb", "Description": "Sample database", "Parameters": { "CreatedBy": "Athena", "EXTERNAL": "TRUE" } }, { "Name": "webdata" } ] }`For more information, see [Listing Databases in a Catalog: list-databases](https://docs.aws.amazon.com/athena/latest/ug/datastores-hive-cli.html#datastores-hive-cli-listing-databases)in the*Amazon Athena User Guide*.- 
                    For API details, see [ListDatabases](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/athena/list-databases.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `list-named-queries`.

- **AWS CLI**
- 
            
                    **To list the named queries for a workgroup**The following `list-named-queries`example lists the named queries for the`AthenaAdmin`workgroup.`aws athena list-named-queries \ --work-group``AthenaAdmin`Output: `{ "NamedQueryIds": [ "a1b2c3d4-5678-90ab-cdef-EXAMPLE11111", "a1b2c3d4-5678-90ab-cdef-EXAMPLE22222", "a1b2c3d4-5678-90ab-cdef-EXAMPLE33333" ] }`For more information, see [Running SQL Queries Using Amazon Athena](https://docs.aws.amazon.com/athena/latest/ug/querying-athena-tables.html)in the*Amazon Athena User Guide*.- 
                    For API details, see [ListNamedQueries](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/athena/list-named-queries.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `list-query-executions`.

- **AWS CLI**
- 
            
                    **To list the query IDs of the queries in a specified workgroup**The following `list-query-executions`example lists a maximum of ten of the query IDs in the`AthenaAdmin`workgroup.`aws athena list-query-executions \ --work-group``AthenaAdmin`\ --max-items`10`Output: `{ "QueryExecutionIds": [ "a1b2c3d4-5678-90ab-cdef-EXAMPLE11110", "a1b2c3d4-5678-90ab-cdef-EXAMPLE11111", "a1b2c3d4-5678-90ab-cdef-EXAMPLE22222", "a1b2c3d4-5678-90ab-cdef-EXAMPLE33333", "a1b2c3d4-5678-90ab-cdef-EXAMPLE11114", "a1b2c3d4-5678-90ab-cdef-EXAMPLE11115", "a1b2c3d4-5678-90ab-cdef-EXAMPLE11116", "a1b2c3d4-5678-90ab-cdef-EXAMPLE11117", "a1b2c3d4-5678-90ab-cdef-EXAMPLE11118", "a1b2c3d4-5678-90ab-cdef-EXAMPLE11119" ], "NextToken": "eyJOZXh0VG9rZW4iOiBudWxsLCAiYm90b190cnVuY2F0ZV9hbW91bnQiOiAxMH0=" }`For more information, see [Working with Query Results, Output Files, and Query History](https://docs.aws.amazon.com/athena/latest/ug/querying.html)in the*Amazon Athena User Guide*.- 
                    For API details, see [ListQueryExecutions](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/athena/list-query-executions.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `list-table-metadata`.

- **AWS CLI**
- 
            
                    **To list the metadata for tables in the specified database of a data catalog**The following `list-table-metadata`example returns metadata information for a maximum of two tables in the`geography`database of the`AwsDataCatalog`data catalog.`aws athena list-table-metadata \ --catalog-name``AwsDataCatalog`\ --database-name`geography`\ --max-items`2`Output: `{ "TableMetadataList": [ { "Name": "country_codes", "CreateTime": 1586553454.0, "TableType": "EXTERNAL_TABLE", "Columns": [ { "Name": "country", "Type": "string", "Comment": "geo id" }, { "Name": "alpha-2 code", "Type": "string", "Comment": "geo id2" }, { "Name": "alpha-3 code", "Type": "string", "Comment": "state name" }, { "Name": "numeric code", "Type": "bigint", "Comment": "" }, { "Name": "latitude", "Type": "bigint", "Comment": "location (latitude)" }, { "Name": "longitude", "Type": "bigint", "Comment": "location (longitude)" } ], "Parameters": { "areColumnsQuoted": "false", "classification": "csv", "columnsOrdered": "true", "delimiter": ",", "has_encrypted_data": "false", "inputformat": "org.apache.hadoop.mapred.TextInputFormat", "location": "s3://amzn-s3-demo-bucket/csv/countrycode", "outputformat": "org.apache.hadoop.hive.ql.io.HiveIgnoreKeyTextOutputFormat", "serde.param.field.delim": ",", "serde.serialization.lib": "org.apache.hadoop.hive.serde2.lazy.LazySimpleSerDe", "skip.header.line.count": "1", "typeOfData": "file" } }, { "Name": "county_populations", "CreateTime": 1586553446.0, "TableType": "EXTERNAL_TABLE", "Columns": [ { "Name": "id", "Type": "string", "Comment": "geo id" }, { "Name": "country", "Name": "id2", "Type": "string", "Comment": "geo id2" }, { "Name": "county", "Type": "string", "Comment": "county name" }, { "Name": "state", "Type": "string", "Comment": "state name" }, { "Name": "population estimate 2018", "Type": "string", "Comment": "" } ], "Parameters": { "areColumnsQuoted": "false", "classification": "csv", "columnsOrdered": "true", "delimiter": ",", "has_encrypted_data": "false", "inputformat": "org.apache.hadoop.mapred.TextInputFormat", "location": "s3://amzn-s3-demo-bucket/csv/CountyPopulation", "outputformat": "org.apache.hadoop.hive.ql.io.HiveIgnoreKeyTextOutputFormat", "serde.param.field.delim": ",", "serde.serialization.lib": "org.apache.hadoop.hive.serde2.lazy.LazySimpleSerDe", "skip.header.line.count": "1", "typeOfData": "file" } } ], "NextToken": "eyJOZXh0VG9rZW4iOiBudWxsLCAiYm90b190cnVuY2F0ZV9hbW91bnQiOiAyfQ==" }`For more information, see [Showing Metadata for All Tables in a Database: list-table-metadata](https://docs.aws.amazon.com/athena/latest/ug/datastores-hive-cli.html#datastores-hive-cli-showing-all-table-metadata)in the*Amazon Athena User Guide*.- 
                    For API details, see [ListTableMetadata](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/athena/list-table-metadata.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `list-tags-for-resource`.

- **AWS CLI**
- 
            
                    **Example 1: To list the tags for a workgroup**The following `list-tags-for-resource`example lists the tags for the`Data_Analyst_Group`workgroup.`aws athena list-tags-for-resource \ --resource-arn``arn:aws:athena:us-west-2:111122223333:workgroup/Data_Analyst_Group`Output: `{ "Tags": [ { "Key": "Division", "Value": "West" }, { "Key": "Team", "Value": "Big Data" }, { "Key": "Location", "Value": "Seattle" } ] }`**Example 2: To list the tags for a data catalog**The following `list-tags-for-resource`example lists the tags for the`dynamo_db_catalog`data catalog.`aws athena list-tags-for-resource \ --resource-arn``arn:aws:athena:us-west-2:111122223333:datacatalog/dynamo_db_catalog`Output: `{ "Tags": [ { "Key": "Division", "Value": "Mountain" }, { "Key": "Organization", "Value": "Retail" }, { "Key": "Product_Line", "Value": "Shoes" }, { "Key": "Location", "Value": "Denver" } ] }`For more information, see [Listing the tags for a resource: list-tags-for-resource](https://docs.aws.amazon.com/athena/latest/ug/tags-operations.html#tags-operations-examples-cli-list-tags-for-resource)in the*Amazon Athena User Guide*.- 
                    For API details, see [ListTagsForResource](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/athena/list-tags-for-resource.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `list-work-groups`.

- **AWS CLI**
- 
            
                    **To list workgroups**The following `list-work-groups`example lists the workgroups in the current account.`aws athena list-work-groups`Output: `{ "WorkGroups": [ { "Name": "Data_Analyst_Group", "State": "ENABLED", "Description": "", "CreationTime": 1578006683.016 }, { "Name": "AthenaAdmin", "State": "ENABLED", "Description": "", "CreationTime": 1573677174.105 }, { "Name": "primary", "State": "ENABLED", "Description": "", "CreationTime": 1567465222.723 } ] }`For more information, see [Managing Workgroups](https://docs.aws.amazon.com/athena/latest/ug/workgroups-create-update-delete.html)in the*Amazon Athena User Guide*.- 
                    For API details, see [ListWorkGroups](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/athena/list-work-groups.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `start-query-execution`.

- **AWS CLI**
- 
            
                    **Example 1: To run a query in a workgroup on the specified table in the specified database and data catalog**The following `start-query-execution`example uses the`AthenaAdmin`workgroup to run a query on the`cloudfront_logs`table in the`cflogsdatabase`in the`AwsDataCatalog`data catalog.`aws athena start-query-execution \ --query-string``"select date, location, browser, uri, status from cloudfront_logs where method = 'GET' and status = 200 and location like 'SFO%' limit 10"`\ --work-group`"AthenaAdmin"`\ --query-execution-context`Database=cflogsdatabase,Catalog=AwsDataCatalog`Output: `{ "QueryExecutionId": "a1b2c3d4-5678-90ab-cdef-EXAMPLE11111" }`For more information, see [Running SQL Queries Using Amazon Athena](https://docs.aws.amazon.com/athena/latest/ug/querying-athena-tables.html)in the*Amazon Athena User Guide*.**Example 2: To run a query that uses a specified workgroup to create a database in the specified data catalog**The following `start-query-execution`example uses the`AthenaAdmin`workgroup to create the database`newdb`in the default data catalog`AwsDataCatalog`.`aws athena start-query-execution \ --query-string``"create database if not exists newdb"`\ --work-group`"AthenaAdmin"`Output: `{ "QueryExecutionId": "a1b2c3d4-5678-90ab-cdef-EXAMPLE11112" }`For more information, see [Running SQL Queries Using Amazon Athena](https://docs.aws.amazon.com/athena/latest/ug/querying-athena-tables.html)in the*Amazon Athena User Guide*.**Example 3: To run a query that creates a view on a table in the specified database and data catalog**The following `start-query-execution`example uses a`SELECT`statement on the`cloudfront_logs`table in the`cflogsdatabase`to create the view`cf10`.`aws athena start-query-execution \ --query-string``"CREATE OR REPLACE VIEW cf10 AS SELECT * FROM cloudfront_logs limit 10"`\ --query-execution-context`Database=cflogsdatabase`Output: `{ "QueryExecutionId": "a1b2c3d4-5678-90ab-cdef-EXAMPLE11113" }`For more information, see [Running SQL Queries Using Amazon Athena](https://docs.aws.amazon.com/athena/latest/ug/querying-athena-tables.html)in the*Amazon Athena User Guide*.- 
                    For API details, see [StartQueryExecution](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/athena/start-query-execution.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `stop-query-execution`.

- **AWS CLI**
- 
            
                    **To stop a running query**The following `stop-query-execution`example stops the query that has the specified query ID.`aws athena stop-query-execution \ --query-execution-id``a1b2c3d4-5678-90ab-cdef-EXAMPLE11111`This command produces no output. For more information, see [Running SQL Queries Using Amazon Athena](https://docs.aws.amazon.com/athena/latest/ug/querying-athena-tables.html)in the*Amazon Athena User Guide*.- 
                    For API details, see [StopQueryExecution](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/athena/stop-query-execution.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `tag-resource`.

- **AWS CLI**
- 
            
                    **To add a tag to a resource**The following `tag-resource`example adds three tags to the`dynamo_db_catalog`data catalog.`aws athena tag-resource \ --resource-arn``arn:aws:athena:us-west-2:111122223333:datacatalog/dynamo_db_catalog`\ --tags`Key=Organization,Value=Retail``Key=Division,Value=Mountain``Key=Product_Line,Value=Shoes``Key=Location,Value=Denver`This command produces no output. To see the result, use `aws athena list-tags-for-resource --resource-arn arn:aws:athena:us-west-2:111122223333:datacatalog/dynamo_db_catalog`.For more information, see [Adding tags to a resource: tag-resource](https://docs.aws.amazon.com/athena/latest/ug/tags-operations.html#tags-operations-examples-cli-tag-resource)in the*Amazon Athena User Guide*.- 
                    For API details, see [TagResource](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/athena/tag-resource.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `untag-resource`.

- **AWS CLI**
- 
            
                    **To remove a tag from a resource**The following `untag-resource`example removes the`Specialization`and`Focus`keys and their associated values from the`dynamo_db_catalog`data catalog resource.`aws athena untag-resource \ --resource-arn``arn:aws:athena:us-west-2:111122223333:datacatalog/dynamo_db_catalog`\ --tag-keys`Specialization``Focus`This command produces no output. To see the results, use the `list-tags-for-resource`command.For more information, see [Removing tags from a resource: untag-resource](https://docs.aws.amazon.com/athena/latest/ug/tags-operations.html#tags-operations-examples-cli-untag-resource)in the*Amazon Athena User Guide*.- 
                    For API details, see [UntagResource](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/athena/untag-resource.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `update-data-catalog`.

- **AWS CLI**
- 
            
                    **To update a data catalog**The following `update-data-catalog`example updates the Lambda function and description of the`cw_logs_catalog`data catalog.`aws athena update-data-catalog \ --name``cw_logs_catalog`\ --type`LAMBDA`\ --description`"New CloudWatch Logs Catalog"`\ --function=arn:aws:lambda:us-west-2:111122223333:function:new_cw_logs_lambdaThis command produces no output. To see the result, use `aws athena get-data-catalog --name cw_logs_catalog`.For more information, see [Updating a Catalog: update-data-catalog](https://docs.aws.amazon.com/athena/latest/ug/datastores-hive-cli.html#datastores-hive-cli-updating-a-catalog)in the*Amazon Athena User Guide*.- 
                    For API details, see [UpdateDataCatalog](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/athena/update-data-catalog.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `update-work-group`.

- **AWS CLI**
- 
            
                    **To update a workgroup**The following `update-work-group`example disables the`Data_Analyst_Group`workgroup. Users cannot run or create queries in the disabled workgroup, but can still view metrics, data usage limit controls, workgroup settings, query history, and saved queries.`aws athena update-work-group \ --work-group``Data_Analyst_Group`\ --state`DISABLED`This command produces no output. To verify the change in state, use `aws athena get-work-group --work-group Data_Analyst_Group`and check the`State`property in the output.For more information, see [Managing Workgroups](https://docs.aws.amazon.com/athena/latest/ug/workgroups-create-update-delete.html)in the*Amazon Athena User Guide*.- 
                    For API details, see [UpdateWorkGroup](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/athena/update-work-group.html)in*AWS CLI Command Reference*.
 
-