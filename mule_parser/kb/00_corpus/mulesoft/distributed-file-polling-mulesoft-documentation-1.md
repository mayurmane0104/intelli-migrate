# Distributed File Polling | MuleSoft Documentation

**Source:** [https://docs.mulesoft.com/mule-runtime/latest/distributed-file-polling](https://docs.mulesoft.com/mule-runtime/latest/distributed-file-polling)

---

# Distributed File Polling

*Enterprise Edition*

Some connectors, such as the File connector or FTP connector, poll directories and read certain files as they are created in the directories polled. These files can reside on a remote file system, including file systems of nodes belonging to a Mule High Availability (HA) Cluster.

In Mule 4, distributed file polling makes it possible to poll files in all cluster nodes. Enabled by default, this feature is used by the following connectors:

You can configure connectors to only poll from the primary node, `@PrimaryNodeOnly`, which ignores the default setting set by the Mule runtime engine. This feature is only available in Mule 4.x