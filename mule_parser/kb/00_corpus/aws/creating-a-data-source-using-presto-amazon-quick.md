# Creating a data source using Presto - Amazon Quick

**Source:** [https://docs.aws.amazon.com/quick/latest/userguide/create-a-data-source-presto.html](https://docs.aws.amazon.com/quick/latest/userguide/create-a-data-source-presto.html)

---

Presto (or PrestoDB) is an open-source, distributed SQL query engine, designed for fast analytic queries against data of any size. It supports both nonrelational and relational data sources. Supported nonrelational data sources include the Hadoop Distributed File System (HDFS), Amazon S3, Cassandra, MongoDB, and HBase. Supported relational data sources include MySQL, PostgreSQL, Amazon Redshift, Microsoft SQL Server, and Teradata.

For more information about Presto, see the following:

- 
                [Introduction to presto](https://aws.amazon.com/big-data/what-is-presto/), a description of Presto on the AWS website.
- 
                [Creating a presto cluster with Amazon elastic MapReduce (EMR)](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/emr-presto.html)in the*Amazon EMR Release Guide.*
- 
                For general information on Presto, see the [Presto documentation](https://trino.io/docs/current/).

The results of the queries that you run through the Presto query engine can be turned into Quick Sight datasets. Presto processes the analytic queries on the backend databases. Then it returns results to the Quick Sight client. You can directly query your data through Presto, or you can import the results of your query into SPICE.

Before you use Quick Sight as a Presto client to run queries, make sure that you configure data source profiles. You need a data source profile in Quick Sight for each Presto data source that you want to access. Use the following procedure to create a connection to Presto.

###### To create a new connection to a presto data source from Amazon Quick Sight (console)

- 
                On the Amazon Quick Sight start page, choose **Data**at left.
- 
                Choose **Create**then**New dataset**.
- 
                Choose the **Presto**tile.###### NoteIn most browsers, you can use Ctrl-F or Cmd-F to open a search box and enter `presto`to locate it.
- 
                Add the settings for the new data source: - 
                        **Data source name**– Enter a descriptive name for your data source connection. This name appears in the**Existing data sources**section at the bottom of the**Data sets**screen.
- 
                        **Connection type**– Choose the connection type that you need to use to connect to Presto.To connect through the public network, choose **Public network**.If you use a public network, your Presto server must be secured and authenticated using Lightweight Directory Access Protocol (LDAP). For information on configuring Presto to use LDAP, see [LDAP authentication](https://trino.io/docs/current/security/ldap.html)in the Presto documentation.To connect through a virtual private connection, choose the appropriate VPC name from the **VPC connections**list.If your Presto server allows unauthenticated access, AWS requires that you connect to it securely by using a private VPC connection. For information on configuring a new VPC, see [Configuring VPC connections in Amazon Quick Sight](./working-with-aws-vpc.html).
- 
                        **Database server**– The name of the database server.
- 
                        **Port**– The port that the server using to accept incoming connections from Amazon Quick Sight
- 
                        **Catalog**– The name of the catalog that you want to use.
- 
                        **Authentication required**– (Optional) This option only appears if you choose a VPC connection type. If the Presto data source that you're connecting to doesn't require authentication, choose**No**. Otherwise, keep the default setting (**Yes**).
- 
                        **Username**– Enter a user name to use to connect to Presto. Quick Sight applies the same user name and password to all connections that use this data source profile. If you want to monitor Quick Sight separately from other accounts, create a Presto account for each Quick Sight data source profile.The Presto account that you use needs be able to access to the database and run `SELECT`statements on at least one table.
- 
                        **Password**– The password to use with the Presto user name. Amazon Quick Sight encrypts all credentials that you use in data source profile. For more information, see[Data encryption in Amazon Quick](./data-encryption.html).
- 
                        **Enable SSL**– SSL is enabled by default.
 
- 
                        
- 
                Choose **Validate connection**to test your settings.
- 
                After you validate your settings, choose **Create data source**to complete the connection.