# Supported VPC data sources - Amazon Quick

**Source:** [https://docs.aws.amazon.com/quick/latest/userguide/vpc-connection-supported-data-sources.html](https://docs.aws.amazon.com/quick/latest/userguide/vpc-connection-supported-data-sources.html)

---

Amazon Quick VPC connections work only with specific Amazon Quick Sight data sources. Use this section to know which data sources are compatible and what requirements they must meet.

The following Amazon Quick Sight data sources can connect to Amazon Quick through a VPC connection:

- 
            Amazon OpenSearch Service 
- 
            Amazon Redshift 
- 
            Amazon Relational Database Service 
- 
            Amazon Aurora 
- 
            Databricks 
- 
            Exasol 
- 
            MariaDB 
- 
            Microsoft SQL Server 
- 
            MySQL 
- 
            Oracle 
- 
            PostgreSQL 
- 
            Presto 
- 
            Snowflake 
- 
            Starburst Enterprise 
- 
            Teradata 
- 
            Trino 

For a VPC data source to be accessed from Amazon Quick Sight, the following statements must be true of your configuration:

- 
            The Domain Name System (DNS) name of the VPC data source can be resolved from outside of your VPC. 
- 
            The connection returns the private IP address of your instance. Databases hosted by Amazon Redshift, Amazon RDS, and Aurora automatically meet this requirement. 
- 
            There is a clearly defined network path from the data source to Amazon Quick Sight. 
- 
            You registered the VPC with Amazon Quick by creating or using a VPC connection with the Amazon Quick console.