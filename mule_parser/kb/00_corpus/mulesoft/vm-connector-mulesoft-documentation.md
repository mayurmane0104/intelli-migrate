# VM Connector | MuleSoft Documentation

**Source:** [https://docs.mulesoft.com/vm-connector/latest](https://docs.mulesoft.com/vm-connector/latest)

---

# VM Connector

Anypoint Connector for Virtual Machine (VM Connector) manages intra-app and inter-app communication through either transient or persistent asynchronous queues:

- 
Transient queues are faster than persistent queues, but they are not reliable if the system crashes. 
- 
Persistent queues are slower but reliable. When running a Mule application in single runtime instance mode, persistent queues work by serializing and storing the contents on the disk. However, when running the Mule application in cluster runtime instance mode, the persistent queues are backed up in the memory grid. Thereby, when a flow uses VM Connector to publish content to a queue, Mule runtime engine determines whether to process the message in the same origin node or to send the message to the cluster to pick another node. Using VM Connector facilitates the load distribution across a cluster. In either single or cluster runtime instance mode, when using persistent queues, the data you send must be serializable. Although you can enable Kryo serialization to get a wider range of serializable values, Kryo does have some limitations. Refer to the [considerations when using serialization](../../mule-runtime/latest/configure-custom-serializers#considerations-when-using-serialization)documentation for details.When using persistent queues: - 
Keep your values simple because complex structures might result in serialization errors or performance issues if they are not easy to serialize. 
- 
Ensure complex Java objects implement the `Serializable`interface and that they conform to the JavaBean contract.
- 
Use streams, JSON objects, maps, and so on only if the associated values comply with the previous recommendations. 
 
- 

Note that persistent queues are unavailable in CloudHub 2.0 and Runtime Fabric.

## Before You Begin

To use this connector, you must be familiar with:

- 
Anypoint Connectors 
- 
Mule runtime engine (Mule) 
- 
Elements and global elements in a Mule flow 
- 
Creating a Mule app using Anypoint Studio or Anypoint Code Builder 

Before creating an app, you must have access to Anypoint Studio.

## Common Use Cases for the Connector

Use VM Connector when you want to:

- 
Pass messages from one flow to another through a queueing mechanism, instead of using a `<flow-ref />`directly
- 
Distribute work across a cluster 
- 
Communicate with different apps that are running in the same Mule domain 
- 
Perform simple queueing that does not justify the use of a full JMS broker 

For examples, see [Examples](vm-examples).

## Audience

- 
New users, read: - 
[Using Anypoint Studio to Configure the Connector](vm-studio-configuration)to create your Mule app
- 
[Examples](vm-examples), which provide one or more use cases for the connector
 
- 
- 
Advanced users, read: 
- 
[Examples](vm-examples), which provide one or more use cases for the connector
 

## Next Step

After you complete the prerequisites and experiment with templates and examples, you are ready to create your own app and configure the connector using [Anypoint Studio](vm-studio-configuration).

## See Also

- 
[Use Exchange to Discover Connectors, Templates, and Examples](../../connectors/introduction/intro-use-exchange)
- 
[Salesforce Help](https://help.salesforce.com)