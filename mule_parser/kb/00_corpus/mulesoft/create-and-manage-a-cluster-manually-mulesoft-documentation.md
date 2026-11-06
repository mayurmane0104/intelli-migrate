# Create and Manage a Cluster Manually | MuleSoft Documentation

**Source:** [https://docs.mulesoft.com/mule-runtime/latest/creating-and-managing-a-cluster-manually](https://docs.mulesoft.com/mule-runtime/latest/creating-and-managing-a-cluster-manually)

---

`... mule.cluster.nodes=192.168.10.21,192.168.10.22,192.168.10.23 mule.cluster.multicastenabled=false mule.clusterId=<Cluster_ID> mule.clusterNodeId=<Cluster_Node_ID> ...`text

# Create and Manage a Cluster Manually

There are two ways to create and manage clusters for on-premises deployments:

- 
Using Runtime Manager See [Clusters](../../runtime-manager/cluster-about)for configuration instructions.
- 
Manually, using a configuration file 

## Cluster Requirements and Restrictions

- 
Do not mix cluster management tools. Manual cluster configuration is not synced to Anypoint Runtime Manager, so any change you make in the platform overrides the cluster configuration files. To avoid this scenario, use only one method for creating and managing your clusters: either manual configuration or configuration using Anypoint Runtime Manager. 
- 
All nodes in a cluster must have the same versions of: - 
Mule runtime engine If you are using a cumulative patch release, such as 4.3.0-20210322, all instances of Mule must be the same cumulative patch version. 
- 
Runtime Manager agent version 
- 
Java 
 
- 

## Creating a Cluster Manually

Follow this procedure to create a cluster manually, using a configuration file.

- 
Ensure that the node is not running, that is that the Mule Runtime Server is stopped. 
- 
Create a file named `mule-cluster.properties`inside the node’s`$MULE_HOME/.mule`directory.
- 
Edit the file with parameter = value pairs, one per line. See the example below. **Note**:`mule.clusterId`and`mule.clusterNodeId`must be in the properties file.
- 
Repeat this procedure for all Mule servers that you want to be in the cluster. 
- 
Start the Mule servers in the nodes. 

For the full list of available parameters, see [Cluster Configuration Parameters](#cluster-config-params).

## Managing a Cluster Manually

You can manually manage only manually created clusters.

To manually change the configuration of a cluster node, follow these steps:

- 
Stop the node’s Mule server. 
- 
Edit the node’s `mule-cluster.properties`as desired, then save the file.
- 
Restart the node’s Mule server. 

| Failure to ensure that the options you apply in the configuration file are valid for all cluster nodes can break cluster configuration and disable the cluster. | 

### Quorum Management

When managing a *manually configured cluster* you can now set a minimum quorum of machines required for the cluster to be operational.

When partitioning a network, clusters are available by default. However, by setting a minimum quorum size you can configure your cluster to reject updates that do not pass a minimum threshold.

This helps you achieve better consistency and protects your cluster in case of an unexpected loss of one of your nodes (Mule Runtimes in the cluster).

Under normal circumstances, if a node were to die in the cluster, you may still have enough memory available to store your data, but the amount of threads available to process requests would be reduced as you now would have less nodes available and the partition threads in the cluster could quickly become overwhelmed. This could lead to

- 
Clients left without threads to process their requests. 
- 
The remaining members of the cluster become so overwhelmed with requests that they’re unable to respond and are forced out of the cluster on the assumption that they are dead. 

To protect the rest of the cluster in the event of member loss, you can set a minimum quorum size to stop concurrent updates to your nodes, and throwing a QuorumException whenever the number of active nodes in the cluster is below your configured value.

| Ensure you catch QuorumExceptions when configuring a Quorum Size for your cluster, and then make any decision as to send an email, stop a process, perform some logging, activate retry strategies, etc. | 

To enable quorum, place in the cluster configurations file `{MULE_HOME}/.mule/mule-cluster.properties` the `mule.cluster.quorumsize` property, and then define the minimum number of nodes of the cluster to remain in an operational state.

| Quorum feature is only valid for components that use Object Store. | 

### Object Store Persistence

| Ensure you set up a centralized JDBC store for the cluster object store persistence. Otherwise, shutting down all cluster nodes causes the content of object stores to be lost, no matter if the persistent setting is enabled on the object store configuration. | 

You can persistently store JDBC data in a central system that is accessible by all cluster nodes when using Mule runtime engine on-premises.

The following relational database systems are supported:

- 
MySQL 5.5+ 
- 
PostgreSQL 9 
- 
Microsoft SQL Server 2014 
- 
Microsoft SQL Server 2019 
- 
Microsoft SQL Server 2022 

To enable object store persistence, create a database and define its configuration values in the `{MULE_HOME}/.mule/mule-cluster.properties` file:

- 
`mule.cluster.jdbcstoreurl`: JDBC URL for connection to the database
- 
`mule.cluster.jdbcstoreusername`: Database username
- 
`mule.cluster.jdbcstorepassword`: Database user password
- 
`mule.cluster.jdbcstoredriver`: JDBC Driver class name
- 
`mule.cluster.jdbcstorequerystrategy`: SQL dialectSee [Cluster Configuration Parameters](#cluster-config-params)for possible configuration values for this parameter.

The database’s tables are created automatically, as this feature creates tables for each different object store that you want to persist.

Two tables are created per object store:

- 
One table stores data 
- 
Another table stores partitions. 

#### Recommendations for the Object Store Database

- 
MuleSoft recommends that you create a dedicated database/schema that will only be used for JDBC store. 
- 
The database username needs to have permission to: - 
Create objects in the database ( `DDL`),`CREATE`and`DROP`for tables.
- 
Access and manage the objects it creates ( `DML`),`INSERT`,`UPDATE`,`DELETE`, and`SELECT`.
 
- 
- 
Always keep in mind that the data storage needs to be hosted in a centralized DB reachable from all nodes. Don’t use more than one database per cluster. 
 Check the[cluster configuration reference for persistency](#persistency-config)for details on how to configure these values.
- 
Some relational databases have certain constraints regarding the name length of tables. Use the `mule.cluster.jdbcstoretableNametransformerstrategy`property to transform long table names into shorter values.
 Check the[Table Name Transformers](#table-name-transformers)section for more details on how to configure this property.
- 
The persistent object store uses a database connection pool based on the `ComboPooledDataSource`Java class. The Mule runtime engine does not set any explicit values for the connection pool behavior. The standard configuration uses the default value for each property.
 For example, the default value for`maxIdleTime`is 0, which means that idle connections never expire and are not removed from the pool. Idle connections remain connected to the database in an idle state.
 You can configure the connection pool behavior by passing your desired parameter values to the runtime, using either of the following options:- 
Pass multiple parameters in the command line when starting Mule: `$ $MULE_HOME/bin/mule start \ -M-Dc3p0.maxIdleTime=<value> \ -M-Dc3p0.maxIdleTimeExcessConnections=<value>`Replace `<value>`with your desired value in milliseconds.
- 
Add multiple lines to the `$MULE_HOME/conf/wrapper.conf`file:wrapper.java.additional.<n>=-Dc3p0.maxIdleTime=<value> wrapper.java.additional.<n>=-Dc3p0.maxIdleTimeExcessConnections=<value> Replace `<n>`with the next highest sequential value from the`wrapper.conf`file.You can find more information about the pool configuration of the `ComboPooledDataSource`Java class in[this article](https://www.mchange.com/projects/c3p0/).
 
- 

### Monitoring

You can monitor the events thrown by the cluster members through the [JMX technology](https://www.oracle.com/java/technologies/javase/javamanagement.html).

The JMX monitoring option is disabled by default. To enable it, add the `mule.cluster.jmxenabled` property to the `{MULE_HOME}/.mule/mule-cluster.properties` configuration file.

Please note that enabling JMX might cause some performance overheads given that the underlying structure adds listeners to get the statistics for each individual node.

#### Table Name Transformers

The `mule.cluster.jdbcstoretableNametransformerstrategy` property enables you to define a custom transformer to modify table names.

For example, if you set the following property in the `mule-cluster.properties` file, Mule hashes table names using MD5 and a prefix to identify tables as Mule tables:

`mule.cluster.jdbcstoretableNametransformerstrategy=com.mulesoft.mule.runtime.module.cluster.api.persistence.query.MD5TableNameTransformerStrategy`Hashing table names guarantees that the length constraint is honored.

You can also create a custom transformer strategy by implementing the `com.mulesoft.mule.runtime.module.cluster.api.persistence.query.TableNameTransformerStrategy` interface, and then configure your custom transformer strategy in the `mule.cluster.jdbcstoretableNametransformerstrategy` property.

### Membership Listener

The membership listener allows you to get notifications whenever:

- 
A new member is added to the cluster 
- 
An existing member leaves the cluster 

When one of these events is triggered, the membership listener outputs the addresses of the members that joined or left respectively.

## Cluster Configuration Parameters

The following table lists the parameters of the `mule-cluster.properties` file.

| Property Name | Description | Required | 
|---|---|---|
| 
 | Unique identifier for the cluster. It can be any alphanumeric string. | Yes | 
| 
 | Unique ID of the node within the cluster. It can be any integer between 1 and the number of nodes in the cluster. | Yes | 
| 
 | The number of nodes that belong to the cluster. | Yes | 
| 
 | Comma-separated list of interfaces to use by Hazelcast. Wildcards are supported, as shown below. 192.168.1.*,192.168.100.25 | No | 
| 
 | The nodes that belong to the cluster, in the form  The port number is optional; if not set, the default is 5701. To include more than one host, create a comma-separated list. This option configures the cluster with the specified fixed IP addresses. Use this option if you are not relying on multicast for cluster node discovery. If using this option, set  Examples: Two nodes listening on port 9000: 172.16.9.24:9000,172.16.9.51:9000 Two nodes listening on port 5701: 192.168.1.19,192.168.1.20 | No | 
| 
 | Enables you to define the minimum number of machines required in a cluster to remain in an operational state. | No | 
| 
 | 
 | No | 
| 
 | Multicast group IP address to use. | No | 
| 
 | Multicast port number to use. | No | 
| The JDBC URL for connection to the database | Required only when storing persistent data. | |
| 
 | Database username | Required only when storing persistent data. | 
| 
 | Database user password | Required only when storing persistent data. | 
| 
 | JDBC Driver class name | Required only when storing persistent data. | 
| 
 | SQL dialect for accessing the stored object data.
This property can take three different values:  | Required only when storing persistent data. | 
| 
 | 
 | No | 
| 
 | 
 | No |