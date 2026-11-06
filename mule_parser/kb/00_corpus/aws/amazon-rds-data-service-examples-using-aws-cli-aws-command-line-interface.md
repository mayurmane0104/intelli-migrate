# Amazon RDS Data Service examples using AWS CLI - AWS Command Line Interface

**Source:** [https://docs.aws.amazon.com/cli/latest/userguide/cli_rds-data_code_examples.html](https://docs.aws.amazon.com/cli/latest/userguide/cli_rds-data_code_examples.html)

---

The following code examples show you how to perform actions and implement common scenarios by using the AWS Command Line Interface with Amazon RDS Data Service.

*Actions* are code excerpts from larger programs and must be run in context. While actions show you how to call individual service functions, you can see actions in context in their related scenarios.

Each example includes a link to the complete source code, where you can find instructions on how to set up and run the code in context.

###### Topics

## Actions

    The following code example shows how to use `batch-execute-statement`.

- **AWS CLI**
- 
            
                    **To execute a batch SQL statement**The following `batch-execute-statement`example executes a batch SQL statement over an array of data with a parameter set.`aws rds-data batch-execute-statement \ --resource-arn``"arn:aws:rds:us-west-2:123456789012:cluster:mydbcluster"`\ --database`"mydb"`\ --secret-arn`"arn:aws:secretsmanager:us-west-2:123456789012:secret:mysecret"`\ --sql`"insert into mytable values (:id, :val)"`\ --parameter-sets "[[{\"name\": \"id\", \"value\": {\"longValue\": 1}},{\"name\": \"val\", \"value\": {\"stringValue\": \"ValueOne\"}}], [{\"name\": \"id\", \"value\": {\"longValue\": 2}},{\"name\": \"val\", \"value\": {\"stringValue\": \"ValueTwo\"}}], [{\"name\": \"id\", \"value\": {\"longValue\": 3}},{\"name\": \"val\", \"value\": {\"stringValue\": \"ValueThree\"}}]]"This command produces no output. For more information, see [Using the Data API for Aurora Serverless](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/data-api.html)in the*Amazon RDS User Guide*.- 
                    For API details, see [BatchExecuteStatement](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rds-data/batch-execute-statement.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `begin-transaction`.

- **AWS CLI**
- 
            
                    **To start a SQL transaction**The following `begin-transaction`example starts a SQL transaction.`aws rds-data begin-transaction \ --resource-arn``"arn:aws:rds:us-west-2:123456789012:cluster:mydbcluster"`\ --database`"mydb"`\ --secret-arn`"arn:aws:secretsmanager:us-west-2:123456789012:secret:mysecret"`Output: `{ "transactionId": "ABC1234567890xyz" }`For more information, see [Using the Data API for Aurora Serverless](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/data-api.html)in the*Amazon RDS User Guide*.- 
                    For API details, see [BeginTransaction](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rds-data/begin-transaction.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `commit-transaction`.

- **AWS CLI**
- 
            
                    **To commit a SQL transaction**The following `commit-transaction`example ends the specified SQL transaction and commits the changes that you made as part of it.`aws rds-data commit-transaction \ --resource-arn``"arn:aws:rds:us-west-2:123456789012:cluster:mydbcluster"`\ --secret-arn`"arn:aws:secretsmanager:us-west-2:123456789012:secret:mysecret"`\ --transaction-id`"ABC1234567890xyz"`Output: `{ "transactionStatus": "Transaction Committed" }`For more information, see [Using the Data API for Aurora Serverless](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/data-api.html)in the*Amazon RDS User Guide*.- 
                    For API details, see [CommitTransaction](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rds-data/commit-transaction.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `execute-statement`.

- **AWS CLI**
- 
            
                    **Example 1: To execute a SQL statement that is part of a transaction**The following `execute-statement`example runs a SQL statement that is part of a transaction.`aws rds-data execute-statement \ --resource-arn``"arn:aws:rds:us-west-2:123456789012:cluster:mydbcluster"`\ --database`"mydb"`\ --secret-arn`"arn:aws:secretsmanager:us-west-2:123456789012:secret:mysecret"`\ --sql`"update mytable set quantity=5 where id=201"`\ --transaction-id`"ABC1234567890xyz"`Output: `{ "numberOfRecordsUpdated": 1 }`**Example 2: To execute a SQL statement with parameters**The following `execute-statement`example runs a SQL statement with parameters.`aws rds-data execute-statement \ --resource-arn``"arn:aws:rds:us-east-1:123456789012:cluster:mydbcluster"`\ --database`"mydb"`\ --secret-arn`"arn:aws:secretsmanager:us-east-1:123456789012:secret:mysecret"`\ --sql`"insert into mytable values (:id, :val)"`\ --parameters "[{\"name\": \"id\", \"value\": {\"longValue\": 1}},{\"name\": \"val\", \"value\": {\"stringValue\": \"value1\"}}]"Output: `{ "numberOfRecordsUpdated": 1 }`For more information, see [Using the Data API for Aurora Serverless](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/data-api.html)in the*Amazon RDS User Guide*.- 
                    For API details, see [ExecuteStatement](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rds-data/execute-statement.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `rollback-transaction`.

- **AWS CLI**
- 
            
                    **To roll back a SQL transaction**The following `rollback-transaction`example rolls back the specified SQL transaction.`aws rds-data rollback-transaction \ --resource-arn``"arn:aws:rds:us-west-2:123456789012:cluster:mydbcluster"`\ --secret-arn`"arn:aws:secretsmanager:us-west-2:123456789012:secret:mysecret"`\ --transaction-id`"ABC1234567890xyz"`Output: `{ "transactionStatus": "Rollback Complete" }`For more information, see [Using the Data API for Aurora Serverless](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/data-api.html)in the*Amazon RDS User Guide*.- 
                    For API details, see [RollbackTransaction](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rds-data/rollback-transaction.html)in*AWS CLI Command Reference*.
 
-