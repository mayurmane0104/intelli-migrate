# Cluster Runtime Instances | MuleSoft Documentation

**Source:** [https://docs.mulesoft.com/mule-runtime/latest/choosing-the-right-clustering-topology](https://docs.mulesoft.com/mule-runtime/latest/choosing-the-right-clustering-topology)

---

Mule High Availability provides basic failover capability for Mule. When the primary Mule instance become unavailable (e.g., because of a fatal JVM or hardware failure or it’s taken offline for maintenance), a backup Mule instance immediately becomes the primary node and resumes processing where the failed instance left off. After a system administrator has recovered the failed Mule instance and brought it back online, it automatically becomes the backup node.

Seamless failover is made possible by a distributed memory store that shares all transient state information among clustered Mule instances, such as:

- 
SEDA service event queues 
- 
In-memory message queues 

Mule High Availability is currently available for the following transports:

- 
HTTP (including CXF Web Services) 
- 
JMS 
- 
WebSphere MQ 
- 
JDBC 
- 
File 
- 
FTP 
- 
Clustered (replaces the local VM transport)