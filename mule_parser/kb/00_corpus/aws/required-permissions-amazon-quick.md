# Required permissions - Amazon Quick

**Source:** [https://docs.aws.amazon.com/quick/latest/userguide/required-permissions.html](https://docs.aws.amazon.com/quick/latest/userguide/required-permissions.html)

---

When you connect to a Amazon Quick Sight data source that requires a user name, the user name must
        have `SELECT` permissions on some system tables. These permissions allow Amazon Quick Sight
        to do things such as discover table schemas and estimate table size. 

The following table identifies the tables that the account must have `SELECT`
        permissions for, depending on the type of database you are connecting to. These requirements
        apply for all database instances you connect to, regardless of their environment. In other
        words, they apply whether your database instances are on-premises, in Amazon RDS, in Amazon EC2, or
        elsewhere.

| Instance type | Tables | 
|---|---|
| Amazon Aurora | 
 
 | 
| Amazon Redshift | 
 
 
 | 
| MariaDB | 
 
 | 
| Microsoft SQL Server | 
 
 | 
| MySQL | 
 INFORMATION_SCHEMA.TABLES | 
| 
 | DBA_TAB_COLS ALL_TABLES dba_segments all_segments user_segments | 
| PostgreSQL | 
 
 
 | 
| ServiceNow | 
 
 
 | 

###### Note

 If you are using MySQL or PostgreSQL, verify that you are connecting from an allowed
            host or IP address. For more detail, see [Database configuration requirements for self-administered
                instances](https://docs.aws.amazon.com/quicksuite/latest/userguide/configure-access.html#database-configuration-requirements).