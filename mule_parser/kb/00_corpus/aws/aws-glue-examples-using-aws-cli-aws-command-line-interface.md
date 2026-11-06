# AWS Glue examples using AWS CLI - AWS Command Line Interface

**Source:** [https://docs.aws.amazon.com/cli/latest/userguide/cli_glue_code_examples.html](https://docs.aws.amazon.com/cli/latest/userguide/cli_glue_code_examples.html)

---

The following code examples show you how to perform actions and implement common scenarios by using the AWS Command Line Interface with AWS Glue.

*Actions* are code excerpts from larger programs and must be run in context. While actions show you how to call individual service functions, you can see actions in context in their related scenarios.

Each example includes a link to the complete source code, where you can find instructions on how to set up and run the code in context.

###### Topics

## Actions

    The following code example shows how to use `batch-stop-job-run`.

- **AWS CLI**
- 
            
                    **To stop job runs**The following `batch-stop-job-run`example stops a job runs.`aws glue batch-stop-job-run \ --job-name``"my-testing-job"`\ --job-run-id`jr_852f1de1f29fb62e0ba4166c33970803935d87f14f96cfdee5089d5274a61d3f`Output: `{ "SuccessfulSubmissions": [ { "JobName": "my-testing-job", "JobRunId": "jr_852f1de1f29fb62e0ba4166c33970803935d87f14f96cfdee5089d5274a61d3f" } ], "Errors": [], "ResponseMetadata": { "RequestId": "66bd6b90-01db-44ab-95b9-6aeff0e73d88", "HTTPStatusCode": 200, "HTTPHeaders": { "date": "Fri, 16 Oct 2020 20:54:51 GMT", "content-type": "application/x-amz-json-1.1", "content-length": "148", "connection": "keep-alive", "x-amzn-requestid": "66bd6b90-01db-44ab-95b9-6aeff0e73d88" }, "RetryAttempts": 0 } }`For more information, see [Job Runs](https://docs.aws.amazon.com/glue/latest/dg/aws-glue-api-jobs-runs.html)in the*AWS Glue Developer Guide*.- 
                    For API details, see [BatchStopJobRun](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/glue/batch-stop-job-run.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `create-connection`.

- **AWS CLI**
- 
            
                    **To create a connection for AWS Glue data stores**The following `create-connection`example creates a connection in the AWS Glue Data Catalog that provides connection information for a Kafka data store.`aws glue create-connection \ --connection-input '``{ \ "Name":"conn-kafka-custom", \ "Description":"kafka connection with ssl to custom kafka", \ "ConnectionType":"KAFKA", \ "ConnectionProperties":{ \ "KAFKA_BOOTSTRAP_SERVERS":"<Kafka-broker-server-url>:<SSL-Port>", \ "KAFKA_SSL_ENABLED":"true", \ "KAFKA_CUSTOM_CERT": "s3://bucket/prefix/cert-file.pem" \ }, \ "PhysicalConnectionRequirements":{ \ "SubnetId":"subnet-1234", \ "SecurityGroupIdList":["sg-1234"], \ "AvailabilityZone":"us-east-1a"} \ }`' \ --region`us-east-1`--endpoint`https://glue.us-east-1.amazonaws.com`This command produces no output. For more information, see [Defining Connections in the AWS Glue Data Catalog](https://docs.aws.amazon.com/glue/latest/dg/populate-add-connection.html)in the*AWS Glue Developer Guide*.- 
                    For API details, see [CreateConnection](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/glue/create-connection.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `create-database`.

- **AWS CLI**
- 
            
                    **To create a database**The following `create-database`example creates a database in the AWS Glue Data Catalog.`aws glue create-database \ --database-input "{\"Name\":\"tempdb\"}" \ --profile``my_profile`\ --endpoint`https://glue.us-east-1.amazonaws.com`This command produces no output. For more information, see [Defining a Database in Your Data Catalog](https://docs.aws.amazon.com/glue/latest/dg/define-database.html)in the*AWS Glue Developer Guide*.- 
                    For API details, see [CreateDatabase](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/glue/create-database.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `create-job`.

- **AWS CLI**
- 
            
                    **To create a job to transform data**The following `create-job`example creates a streaming job that runs a script stored in S3.`aws glue create-job \ --name``my-testing-job`\ --role`AWSGlueServiceRoleDefault`\ --command '`{ \ "Name": "gluestreaming", \ "ScriptLocation": "s3://amzn-s3-demo-bucket/folder/" \ }`' \ --region`us-east-1`\ --output`json`\ --default-arguments '`{ \ "--job-language":"scala", \ "--class":"GlueApp" \ }`' \ --profile`my-profile`\ --endpoint`https://glue.us-east-1.amazonaws.com`Contents of `test_script.scala`:`import com.amazonaws.services.glue.ChoiceOption import com.amazonaws.services.glue.GlueContext import com.amazonaws.services.glue.MappingSpec import com.amazonaws.services.glue.ResolveSpec import com.amazonaws.services.glue.errors.CallSite import com.amazonaws.services.glue.util.GlueArgParser import com.amazonaws.services.glue.util.Job import com.amazonaws.services.glue.util.JsonOptions import org.apache.spark.SparkContext import scala.collection.JavaConverters._ object GlueApp { def main(sysArgs: Array[String]) { val spark: SparkContext = new SparkContext() val glueContext: GlueContext = new GlueContext(spark) // @params: [JOB_NAME] val args = GlueArgParser.getResolvedOptions(sysArgs, Seq("JOB_NAME").toArray) Job.init(args("JOB_NAME"), glueContext, args.asJava) // @type: DataSource // @args: [database = "tempdb", table_name = "s3-source", transformation_ctx = "datasource0"] // @return: datasource0 // @inputs: [] val datasource0 = glueContext.getCatalogSource(database = "tempdb", tableName = "s3-source", redshiftTmpDir = "", transformationContext = "datasource0").getDynamicFrame() // @type: ApplyMapping // @args: [mapping = [("sensorid", "int", "sensorid", "int"), ("currenttemperature", "int", "currenttemperature", "int"), ("status", "string", "status", "string")], transformation_ctx = "applymapping1"] // @return: applymapping1 // @inputs: [frame = datasource0] val applymapping1 = datasource0.applyMapping(mappings = Seq(("sensorid", "int", "sensorid", "int"), ("currenttemperature", "int", "currenttemperature", "int"), ("status", "string", "status", "string")), caseSensitive = false, transformationContext = "applymapping1") // @type: SelectFields // @args: [paths = ["sensorid", "currenttemperature", "status"], transformation_ctx = "selectfields2"] // @return: selectfields2 // @inputs: [frame = applymapping1] val selectfields2 = applymapping1.selectFields(paths = Seq("sensorid", "currenttemperature", "status"), transformationContext = "selectfields2") // @type: ResolveChoice // @args: [choice = "MATCH_CATALOG", database = "tempdb", table_name = "my-s3-sink", transformation_ctx = "resolvechoice3"] // @return: resolvechoice3 // @inputs: [frame = selectfields2] val resolvechoice3 = selectfields2.resolveChoice(choiceOption = Some(ChoiceOption("MATCH_CATALOG")), database = Some("tempdb"), tableName = Some("my-s3-sink"), transformationContext = "resolvechoice3") // @type: DataSink // @args: [database = "tempdb", table_name = "my-s3-sink", transformation_ctx = "datasink4"] // @return: datasink4 // @inputs: [frame = resolvechoice3] val datasink4 = glueContext.getCatalogSink(database = "tempdb", tableName = "my-s3-sink", redshiftTmpDir = "", transformationContext = "datasink4").writeDynamicFrame(resolvechoice3) Job.commit() } }`Output: `{ "Name": "my-testing-job" }`For more information, see [Authoring Jobs in AWS Glue](https://docs.aws.amazon.com/glue/latest/dg/author-job.html)in the*AWS Glue Developer Guide*.- 
                    For API details, see [CreateJob](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/glue/create-job.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `create-table`.

- **AWS CLI**
- 
            
                    **Example 1: To create a table for a Kinesis data stream**The following `create-table`example creates a table in the AWS Glue Data Catalog that describes a Kinesis data stream.`aws glue create-table \ --database-name``tempdb`\ --table-input '`{"Name":"test-kinesis-input", "StorageDescriptor":{ \ "Columns":[ \ {"Name":"sensorid", "Type":"int"}, \ {"Name":"currenttemperature", "Type":"int"}, \ {"Name":"status", "Type":"string"} ], \ "Location":"my-testing-stream", \ "Parameters":{ \ "typeOfData":"kinesis","streamName":"my-testing-stream", \ "kinesisUrl":"https://kinesis.us-east-1.amazonaws.com" \ }, \ "SerdeInfo":{ \ "SerializationLibrary":"org.openx.data.jsonserde.JsonSerDe"} \ }, \ "Parameters":{ \ "classification":"json"} \ }`' \ --profile`my-profile`\ --endpoint`https://glue.us-east-1.amazonaws.com`This command produces no output. For more information, see [Defining Tables in the AWS Glue Data Catalog](https://docs.aws.amazon.com/glue/latest/dg/tables-described.html)in the*AWS Glue Developer Guide*.**Example 2: To create a table for a Kafka data store**The following `create-table`example creates a table in the AWS Glue Data Catalog that describes a Kafka data store.`aws glue create-table \ --database-name``tempdb`\ --table-input '`{"Name":"test-kafka-input", "StorageDescriptor":{ \ "Columns":[ \ {"Name":"sensorid", "Type":"int"}, \ {"Name":"currenttemperature", "Type":"int"}, \ {"Name":"status", "Type":"string"} ], \ "Location":"glue-topic", \ "Parameters":{ \ "typeOfData":"kafka","topicName":"glue-topic", \ "connectionName":"my-kafka-connection" }, \ "SerdeInfo":{ \ "SerializationLibrary":"org.apache.hadoop.hive.serde2.OpenCSVSerde"} \ }, \ "Parameters":{ \ "separatorChar":","} \ }`' \ --profile`my-profile`\ --endpoint`https://glue.us-east-1.amazonaws.com`This command produces no output. For more information, see [Defining Tables in the AWS Glue Data Catalog](https://docs.aws.amazon.com/glue/latest/dg/tables-described.html)in the*AWS Glue Developer Guide*.**Example 3: To create a table for a AWS S3 data store**The following `create-table`example creates a table in the AWS Glue Data Catalog that describes a AWS Simple Storage Service (AWS S3) data store.`aws glue create-table \ --database-name``tempdb`\ --table-input '`{"Name":"s3-output", "StorageDescriptor":{ \ "Columns":[ \ {"Name":"s1", "Type":"string"}, \ {"Name":"s2", "Type":"int"}, \ {"Name":"s3", "Type":"string"} ], \ "Location":"s3://bucket-path/", \ "SerdeInfo":{ \ "SerializationLibrary":"org.openx.data.jsonserde.JsonSerDe"} \ }, \ "Parameters":{ \ "classification":"json"} \ }`' \ --profile`my-profile`\ --endpoint`https://glue.us-east-1.amazonaws.com`This command produces no output. For more information, see [Defining Tables in the AWS Glue Data Catalog](https://docs.aws.amazon.com/glue/latest/dg/tables-described.html)in the*AWS Glue Developer Guide*.- 
                    For API details, see [CreateTable](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/glue/create-table.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `delete-job`.

- **AWS CLI**
- 
            
                    **To delete a job**The following `delete-job`example deletes a job that is no longer needed.`aws glue delete-job \ --job-name``my-testing-job`Output: `{ "JobName": "my-testing-job" }`For more information, see [Working with Jobs on the AWS Glue Console](https://docs.aws.amazon.com/glue/latest/dg/console-jobs.html)in the*AWS Glue Developer Guide*.- 
                    For API details, see [DeleteJob](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/glue/delete-job.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `get-databases`.

- **AWS CLI**
- 
            
                    **To list the definitions of some or all of the databases in the AWS Glue Data Catalog**The following `get-databases`example returns information about the databases in the Data Catalog.`aws glue get-databases`Output: `{ "DatabaseList": [ { "Name": "default", "Description": "Default Hive database", "LocationUri": "file:/spark-warehouse", "CreateTime": 1602084052.0, "CreateTableDefaultPermissions": [ { "Principal": { "DataLakePrincipalIdentifier": "IAM_ALLOWED_PRINCIPALS" }, "Permissions": [ "ALL" ] } ], "CatalogId": "111122223333" }, { "Name": "flights-db", "CreateTime": 1587072847.0, "CreateTableDefaultPermissions": [ { "Principal": { "DataLakePrincipalIdentifier": "IAM_ALLOWED_PRINCIPALS" }, "Permissions": [ "ALL" ] } ], "CatalogId": "111122223333" }, { "Name": "legislators", "CreateTime": 1601415625.0, "CreateTableDefaultPermissions": [ { "Principal": { "DataLakePrincipalIdentifier": "IAM_ALLOWED_PRINCIPALS" }, "Permissions": [ "ALL" ] } ], "CatalogId": "111122223333" }, { "Name": "tempdb", "CreateTime": 1601498566.0, "CreateTableDefaultPermissions": [ { "Principal": { "DataLakePrincipalIdentifier": "IAM_ALLOWED_PRINCIPALS" }, "Permissions": [ "ALL" ] } ], "CatalogId": "111122223333" } ] }`For more information, see [Defining a Database in Your Data Catalog](https://docs.aws.amazon.com/glue/latest/dg/define-database.html)in the*AWS Glue Developer Guide*.- 
                    For API details, see [GetDatabases](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/glue/get-databases.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `get-job-run`.

- **AWS CLI**
- 
            
                    **To get information about a job run**The following `get-job-run`example retrieves information about a job run.`aws glue get-job-run \ --job-name``"Combine legistators data"`\ --run-id`jr_012e176506505074d94d761755e5c62538ee1aad6f17d39f527e9140cf0c9a5e`Output: `{ "JobRun": { "Id": "jr_012e176506505074d94d761755e5c62538ee1aad6f17d39f527e9140cf0c9a5e", "Attempt": 0, "JobName": "Combine legistators data", "StartedOn": 1602873931.255, "LastModifiedOn": 1602874075.985, "CompletedOn": 1602874075.985, "JobRunState": "SUCCEEDED", "Arguments": { "--enable-continuous-cloudwatch-log": "true", "--enable-metrics": "", "--enable-spark-ui": "true", "--job-bookmark-option": "job-bookmark-enable", "--spark-event-logs-path": "s3://aws-glue-assets-111122223333-us-east-1/sparkHistoryLogs/" }, "PredecessorRuns": [], "AllocatedCapacity": 10, "ExecutionTime": 117, "Timeout": 2880, "MaxCapacity": 10.0, "WorkerType": "G.1X", "NumberOfWorkers": 10, "LogGroupName": "/aws-glue/jobs", "GlueVersion": "2.0" } }`For more information, see [Job Runs](https://docs.aws.amazon.com/glue/latest/dg/aws-glue-api-jobs-runs.html)in the*AWS Glue Developer Guide*.- 
                    For API details, see [GetJobRun](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/glue/get-job-run.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `get-job-runs`.

- **AWS CLI**
- 
            
                    **To get information about all job runs for a job**The following `get-job-runs`example retrieves information about job runs for a job.`aws glue get-job-runs \ --job-name``"my-testing-job"`Output: `{ "JobRuns": [ { "Id": "jr_012e176506505074d94d761755e5c62538ee1aad6f17d39f527e9140cf0c9a5e", "Attempt": 0, "JobName": "my-testing-job", "StartedOn": 1602873931.255, "LastModifiedOn": 1602874075.985, "CompletedOn": 1602874075.985, "JobRunState": "SUCCEEDED", "Arguments": { "--enable-continuous-cloudwatch-log": "true", "--enable-metrics": "", "--enable-spark-ui": "true", "--job-bookmark-option": "job-bookmark-enable", "--spark-event-logs-path": "s3://aws-glue-assets-111122223333-us-east-1/sparkHistoryLogs/" }, "PredecessorRuns": [], "AllocatedCapacity": 10, "ExecutionTime": 117, "Timeout": 2880, "MaxCapacity": 10.0, "WorkerType": "G.1X", "NumberOfWorkers": 10, "LogGroupName": "/aws-glue/jobs", "GlueVersion": "2.0" }, { "Id": "jr_03cc19ddab11c4e244d3f735567de74ff93b0b3ef468a713ffe73e53d1aec08f_attempt_2", "Attempt": 2, "PreviousRunId": "jr_03cc19ddab11c4e244d3f735567de74ff93b0b3ef468a713ffe73e53d1aec08f_attempt_1", "JobName": "my-testing-job", "StartedOn": 1602811168.496, "LastModifiedOn": 1602811282.39, "CompletedOn": 1602811282.39, "JobRunState": "FAILED", "ErrorMessage": "An error occurred while calling o122.pyWriteDynamicFrame. Access Denied (Service: Amazon S3; Status Code: 403; Error Code: AccessDenied; Request ID: 021AAB703DB20A2D; S3 Extended Request ID: teZk24Y09TkXzBvMPG502L5VJBhe9DJuWA9/TXtuGOqfByajkfL/Tlqt5JBGdEGpigAqzdMDM/U=)", "PredecessorRuns": [], "AllocatedCapacity": 10, "ExecutionTime": 110, "Timeout": 2880, "MaxCapacity": 10.0, "WorkerType": "G.1X", "NumberOfWorkers": 10, "LogGroupName": "/aws-glue/jobs", "GlueVersion": "2.0" }, { "Id": "jr_03cc19ddab11c4e244d3f735567de74ff93b0b3ef468a713ffe73e53d1aec08f_attempt_1", "Attempt": 1, "PreviousRunId": "jr_03cc19ddab11c4e244d3f735567de74ff93b0b3ef468a713ffe73e53d1aec08f", "JobName": "my-testing-job", "StartedOn": 1602811020.518, "LastModifiedOn": 1602811138.364, "CompletedOn": 1602811138.364, "JobRunState": "FAILED", "ErrorMessage": "An error occurred while calling o122.pyWriteDynamicFrame. Access Denied (Service: Amazon S3; Status Code: 403; Error Code: AccessDenied; Request ID: 2671D37856AE7ABB; S3 Extended Request ID: RLJCJw20brV+PpC6GpORahyF2fp9flB5SSb2bTGPnUSPVizLXRl1PN3QZldb+v1o9qRVktNYbW8=)", "PredecessorRuns": [], "AllocatedCapacity": 10, "ExecutionTime": 113, "Timeout": 2880, "MaxCapacity": 10.0, "WorkerType": "G.1X", "NumberOfWorkers": 10, "LogGroupName": "/aws-glue/jobs", "GlueVersion": "2.0" } ] }`For more information, see [Job Runs](https://docs.aws.amazon.com/glue/latest/dg/aws-glue-api-jobs-runs.html)in the*AWS Glue Developer Guide*.- 
                    For API details, see [GetJobRuns](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/glue/get-job-runs.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `get-job`.

- **AWS CLI**
- 
            
                    **To retrieve information about a job**The following `get-job`example retrieves information about a job.`aws glue get-job \ --job-name``my-testing-job`Output: `{ "Job": { "Name": "my-testing-job", "Role": "Glue_DefaultRole", "CreatedOn": 1602805698.167, "LastModifiedOn": 1602805698.167, "ExecutionProperty": { "MaxConcurrentRuns": 1 }, "Command": { "Name": "gluestreaming", "ScriptLocation": "s3://janetst-bucket-01/Scripts/test_script.scala", "PythonVersion": "2" }, "DefaultArguments": { "--class": "GlueApp", "--job-language": "scala" }, "MaxRetries": 0, "AllocatedCapacity": 10, "MaxCapacity": 10.0, "GlueVersion": "1.0" } }`For more information, see [Jobs](https://docs.aws.amazon.com/glue/latest/dg/aws-glue-api-jobs-job.html)in the*AWS Glue Developer Guide*.- 
                    For API details, see [GetJob](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/glue/get-job.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `get-plan`.

- **AWS CLI**
- 
            
                    **To get the generated code for mapping data from source tables to target tables**The following `get-plan`retrieves the generated code for mapping columns from the data source to the data target.`aws glue get-plan --mapping '``[ \ { \ "SourcePath":"sensorid", \ "SourceTable":"anything", \ "SourceType":"int", \ "TargetPath":"sensorid", \ "TargetTable":"anything", \ "TargetType":"int" \ }, \ { \ "SourcePath":"currenttemperature", \ "SourceTable":"anything", \ "SourceType":"int", \ "TargetPath":"currenttemperature", \ "TargetTable":"anything", \ "TargetType":"int" \ }, \ { \ "SourcePath":"status", \ "SourceTable":"anything", \ "SourceType":"string", \ "TargetPath":"status", \ "TargetTable":"anything", \ "TargetType":"string" \ }]`' \ --source '`{ \ "DatabaseName":"tempdb", \ "TableName":"s3-source" \ }`' \ --sinks '`[ \ { \ "DatabaseName":"tempdb", \ "TableName":"my-s3-sink" \ }]`' --language`"scala"`--endpoint`https://glue.us-east-1.amazonaws.com`--output`"text"`Output: `import com.amazonaws.services.glue.ChoiceOption import com.amazonaws.services.glue.GlueContext import com.amazonaws.services.glue.MappingSpec import com.amazonaws.services.glue.ResolveSpec import com.amazonaws.services.glue.errors.CallSite import com.amazonaws.services.glue.util.GlueArgParser import com.amazonaws.services.glue.util.Job import com.amazonaws.services.glue.util.JsonOptions import org.apache.spark.SparkContext import scala.collection.JavaConverters._ object GlueApp { def main(sysArgs: Array[String]) { val spark: SparkContext = new SparkContext() val glueContext: GlueContext = new GlueContext(spark) // @params: [JOB_NAME] val args = GlueArgParser.getResolvedOptions(sysArgs, Seq("JOB_NAME").toArray) Job.init(args("JOB_NAME"), glueContext, args.asJava) // @type: DataSource // @args: [database = "tempdb", table_name = "s3-source", transformation_ctx = "datasource0"] // @return: datasource0 // @inputs: [] val datasource0 = glueContext.getCatalogSource(database = "tempdb", tableName = "s3-source", redshiftTmpDir = "", transformationContext = "datasource0").getDynamicFrame() // @type: ApplyMapping // @args: [mapping = [("sensorid", "int", "sensorid", "int"), ("currenttemperature", "int", "currenttemperature", "int"), ("status", "string", "status", "string")], transformation_ctx = "applymapping1"] // @return: applymapping1 // @inputs: [frame = datasource0] val applymapping1 = datasource0.applyMapping(mappings = Seq(("sensorid", "int", "sensorid", "int"), ("currenttemperature", "int", "currenttemperature", "int"), ("status", "string", "status", "string")), caseSensitive = false, transformationContext = "applymapping1") // @type: SelectFields // @args: [paths = ["sensorid", "currenttemperature", "status"], transformation_ctx = "selectfields2"] // @return: selectfields2 // @inputs: [frame = applymapping1] val selectfields2 = applymapping1.selectFields(paths = Seq("sensorid", "currenttemperature", "status"), transformationContext = "selectfields2") // @type: ResolveChoice // @args: [choice = "MATCH_CATALOG", database = "tempdb", table_name = "my-s3-sink", transformation_ctx = "resolvechoice3"] // @return: resolvechoice3 // @inputs: [frame = selectfields2] val resolvechoice3 = selectfields2.resolveChoice(choiceOption = Some(ChoiceOption("MATCH_CATALOG")), database = Some("tempdb"), tableName = Some("my-s3-sink"), transformationContext = "resolvechoice3") // @type: DataSink // @args: [database = "tempdb", table_name = "my-s3-sink", transformation_ctx = "datasink4"] // @return: datasink4 // @inputs: [frame = resolvechoice3] val datasink4 = glueContext.getCatalogSink(database = "tempdb", tableName = "my-s3-sink", redshiftTmpDir = "", transformationContext = "datasink4").writeDynamicFrame(resolvechoice3) Job.commit() } }`For more information, see [Editing Scripts in AWS Glue](https://docs.aws.amazon.com/glue/latest/dg/edit-script.html)in the*AWS Glue Developer Guide*.- 
                    For API details, see [GetPlan](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/glue/get-plan.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `get-tables`.

- **AWS CLI**
- 
            
                    **To list the definitions of some or all of the tables in the specified database**The following `get-tables`example returns information about the tables in the specified database.`aws glue get-tables --database-name '``tempdb`'Output: `{ "TableList": [ { "Name": "my-s3-sink", "DatabaseName": "tempdb", "CreateTime": 1602730539.0, "UpdateTime": 1602730539.0, "Retention": 0, "StorageDescriptor": { "Columns": [ { "Name": "sensorid", "Type": "int" }, { "Name": "currenttemperature", "Type": "int" }, { "Name": "status", "Type": "string" } ], "Location": "s3://janetst-bucket-01/test-s3-output/", "Compressed": false, "NumberOfBuckets": 0, "SerdeInfo": { "SerializationLibrary": "org.openx.data.jsonserde.JsonSerDe" }, "SortColumns": [], "StoredAsSubDirectories": false }, "Parameters": { "classification": "json" }, "CreatedBy": "arn:aws:iam::007436865787:user/JRSTERN", "IsRegisteredWithLakeFormation": false, "CatalogId": "007436865787" }, { "Name": "s3-source", "DatabaseName": "tempdb", "CreateTime": 1602730658.0, "UpdateTime": 1602730658.0, "Retention": 0, "StorageDescriptor": { "Columns": [ { "Name": "sensorid", "Type": "int" }, { "Name": "currenttemperature", "Type": "int" }, { "Name": "status", "Type": "string" } ], "Location": "s3://janetst-bucket-01/", "Compressed": false, "NumberOfBuckets": 0, "SortColumns": [], "StoredAsSubDirectories": false }, "Parameters": { "classification": "json" }, "CreatedBy": "arn:aws:iam::007436865787:user/JRSTERN", "IsRegisteredWithLakeFormation": false, "CatalogId": "007436865787" }, { "Name": "test-kinesis-input", "DatabaseName": "tempdb", "CreateTime": 1601507001.0, "UpdateTime": 1601507001.0, "Retention": 0, "StorageDescriptor": { "Columns": [ { "Name": "sensorid", "Type": "int" }, { "Name": "currenttemperature", "Type": "int" }, { "Name": "status", "Type": "string" } ], "Location": "my-testing-stream", "Compressed": false, "NumberOfBuckets": 0, "SerdeInfo": { "SerializationLibrary": "org.openx.data.jsonserde.JsonSerDe" }, "SortColumns": [], "Parameters": { "kinesisUrl": "https://kinesis.us-east-1.amazonaws.com", "streamName": "my-testing-stream", "typeOfData": "kinesis" }, "StoredAsSubDirectories": false }, "Parameters": { "classification": "json" }, "CreatedBy": "arn:aws:iam::007436865787:user/JRSTERN", "IsRegisteredWithLakeFormation": false, "CatalogId": "007436865787" } ] }`For more information, see [Defining Tables in the AWS Glue Data Catalog](https://docs.aws.amazon.com/glue/latest/dg/tables-described.html)in the*AWS Glue Developer Guide*.- 
                    For API details, see [GetTables](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/glue/get-tables.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `start-crawler`.

- **AWS CLI**
- 
            
                    **To start a crawler**The following `start-crawler`example starts a crawler.`aws glue start-crawler --name``my-crawler`Output: `None`For more information, see [Defining Crawlers](https://docs.aws.amazon.com/glue/latest/dg/add-crawler.html)in the*AWS Glue Developer Guide*.- 
                    For API details, see [StartCrawler](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/glue/start-crawler.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `start-job-run`.

- **AWS CLI**
- 
            
                    **To start running a job**The following `start-job-run`example starts a job.`aws glue start-job-run \ --job-name``my-job`Output: `{ "JobRunId": "jr_22208b1f44eb5376a60569d4b21dd20fcb8621e1a366b4e7b2494af764b82ded" }`For more information, see [Authoring Jobs](https://docs.aws.amazon.com/glue/latest/dg/author-job.html)in the*AWS Glue Developer Guide*.- 
                    For API details, see [StartJobRun](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/glue/start-job-run.html)in*AWS CLI Command Reference*.
 
-