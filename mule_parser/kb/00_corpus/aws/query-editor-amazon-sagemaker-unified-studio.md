# Query Editor - Amazon SageMaker Unified Studio

**Source:** [https://docs.aws.amazon.com/sagemaker-unified-studio/latest/userguide/sql-query.html](https://docs.aws.amazon.com/sagemaker-unified-studio/latest/userguide/sql-query.html)

---

Use the query editor in Amazon SageMaker Unified Studio to write SQL queries, run them against your data sources, and visualize results, all within your project. You can work with multiple query engines, browse your data catalog, generate SQL using natural language, and schedule queries to run automatically.

## Supported query engines

  
  The query editor supports the following engines. You can switch between engines within the same querybook.

| Engine | Description | SQL reference | 
|---|---|---|
| Amazon Athena | Serverless query engine for data stored in Amazon S3 and AWS Glue Data Catalog. Best for ad-hoc queries against lakehouse data. | [Athena
        SQL reference](https://docs.aws.amazon.com/athena/latest/ug/ddl-sql-reference.html) | 
| Amazon Redshift | Data warehouse engine for structured and semi-structured data. Best for complex analytical queries and joins across large datasets. | [Redshift SQL reference](https://docs.aws.amazon.com/redshift/latest/dg/c_redshift-sql.html) |