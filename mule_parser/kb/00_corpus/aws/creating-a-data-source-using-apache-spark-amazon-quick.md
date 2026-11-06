# Creating a data source using Apache Spark - Amazon Quick

**Source:** [https://docs.aws.amazon.com/quick/latest/userguide/create-a-data-source-spark.html](https://docs.aws.amazon.com/quick/latest/userguide/create-a-data-source-spark.html)

---

You can connect directly to Apache Spark using Quick Sight, or you can connect to
            Spark through Spark SQL. Using the results of queries, or direct links to tables or
            views, you create data sources in Quick Sight. You can either directly query your data
            through Spark, or you can import the results of your query into [SPICE](./spice.html).

Before you use Quick Sight with Spark products, you must configure Spark for Quick Sight.

Quick Sight requires your Spark server to be secured and authenticated using LDAP, which is available to Spark version 2.0 or later. If Spark is configured to allow unauthenticated access, Quick Sight refuses the connection to the server. To use Quick Sight as a Spark client, you must configure LDAP authentication to work with Spark.

The Spark documentation contains information on how to set this up. To start, you need
            to configure it to enable front-end LDAP authentication over HTTPS. For general
            information on Spark, see [the Apache spark
                website](http://spark.apache.org/). For information specifically on Spark and security, see 

[Spark security documentation](http://spark.apache.org/docs/latest/security.html).

To make sure that you have configured your server for Quick Sight access, follow the
            instructions in [Network and database configuration requirements](./configure-access.html).