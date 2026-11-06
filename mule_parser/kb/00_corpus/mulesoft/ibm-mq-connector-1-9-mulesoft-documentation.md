# IBM MQ Connector 1.9 | MuleSoft Documentation

**Source:** [https://docs.mulesoft.com/ibm-mq-connector/latest](https://docs.mulesoft.com/ibm-mq-connector/latest)

---

![Client Connection](_images/ibm-mq-client-connection-mode.png) 

# IBM MQ Connector 1.9

Anypoint Connector for IBM MQ (IBM MQ Connector) enables an app to do messaging to a IBM MQ Broker using the IBM MQ JMS implementation. The main features include:

- 
Pub/Sub pattern support on any given destination. 
- 
Listen/Reply pattern support on any given destination. 
- 
Publish-Consume pattern support on any given destination, with fixed or temporary reply Queue. 
- 
Non-blocking publishing and consumption of messages. 

Release Notes: [IBM MQ Connector Release Notes](../../release-notes/connector/connector-ibm-mq)

Exchange: [IBM MQ Connector](https://www.mulesoft.com/exchange/com.mulesoft.connectors/mule-ibm-mq-connector/)

## Connection Mode

When creating the IBM configuration, choose
is the [IBM connection mode](https://www.ibm.com/docs/en/ibm-mq/9.0.x?topic=SSFKSJ_9.0.0/com.ibm.mq.dev.doc/q031720_.html) to use.

As of IBM MQ 8, there are only two available connection modes, **Client** and **Binding**.

### Client Connection Mode

The client connection mode lets you connect to the IBM MQ Queue Manager running in the same system that is being run the Mule Application or in other system. In both cases the IBM MQ Connector will connect to the IBM MQ Queue Manager over TCP/IP.

For this connection mode are available the following configurations:

| Parameter | Required | Default Value | Description | 
|---|---|---|---|
| Host | TRUE | Host containing the IBM MQ Broker. | |
| Port | FALSE | 1414 | Queue manager listener port. | 
| Queue Manager | FALSE | The queue manager used when selecting a channel definition. | |
| Channel | FALSE | Name of the channel to connect to. | |
| Connection Name List | FALSE | Hosts to which the client attempts to reconnect after its connection is broken. | 

![Client Connection](_images/ibm-mq-client-connection-mode.png) 

```
<ibm-mq:config name="IBM_MQ_Config">
 <ibm-mq:connection >
   <ibm-mq:connection-mode >
	 	<ibm-mq:client host="0.0.0.0" port="1414" queueManager="QM1" channel="DEV.ADMIN.SVRCONN" />
		</ibm-mq:connection-mode>
	</ibm-mq:connection>
</ibm-mq:config>
```
xml### Binding Connection Mode

The binding connection mode connects automatically to the IBM MQ broker running in the same system.

The unique parameter that is optionally configurable is the Queue Manager to connect to. If the IBM MQ broker has a default Queue Manager, this configuration is not required.

![Client Connection](_images/ibm-mq-binding-connection-mode.png) 

```
<ibm-mq:config name="IBM_MQ_Config">
  <ibm-mq:connection >
    <ibm-mq:connection-mode >
      <ibm-mq:binding queueManager="QM1" />
    </ibm-mq:connection-mode>
  </ibm-mq:connection>
</ibm-mq:config>
```
xml## Define Global Defaults

The IBM MQ `config` allows you to define multiple parameters to use as
a default while consuming or publishing messages. This way, you can define a
global default behavior for all the operations associated with the config and
override each parameter only in the operations that require a custom behavior.

For example, we can define a default `selector` behavior when consuming a Message
in any of the operations that are associated to this config, and also a default.

```
<ibm-mq:config name="IBM_MQ_Config">
  <ibm-mq:connection/>
  <ibm-mq:consumer-config selector="JMSType = `INVOICE`"/>
  <ibm-mq:producer-config timeToLive="60000"/>
</ibm-mq:config>
```
xmlIn this case, every consume or listener operation associated with this configuration
uses the `selector` by default, while every time a publish or publish-consume occurs,
the outgoing message has a TTL of 60 seconds.

All of these properties can be overridden at operation level when required. To publish a message with a shorter TTL, use this example configuration that overrides the parameter:

`<ibm-mq:publish config-ref="IBM_MQ_Config" timeToLive="10000"/>`xml## Select the JMS Spec

The main common parameter is the JMS specification used to select between all the supported specifications, which are 2.0 and 1.1. This specification must be supported by the broker implementation associated to this connection, otherwise the connection fails.

| Features available only in JMS 2.0 won’t work with any other specification. | 

## Provide Credentials For Authentication

To establish an authenticated connection, you need to configure the username and password in the connection element:

```
<ibm-mq:config name="IBM_MQ_Config">
	<ibm-mq:connection username="<username>" password="<password>" >
		<ibm-mq:connection-mode >
			<ibm-mq:client
			host="0.0.0.0"
			port="1414"
			queueManager="QM1"
			channel="DEV.ADMIN.SVRCONN" />
		</ibm-mq:connection-mode>
	</ibm-mq:connection>
</ibm-mq:config>
```
xml## Configure Connections Caching

To connect with a broker and execute the required operations, the JMS connector creates multiple sessions, consumers, and producers that can be cached and reused to increase the performance of the application. Because of this capability, the IBM MQ connector allows you to configure which caching strategy to use when creating new connections, caching by default both consumers and producers, and preserving as many instances as possible in memory at the same time.

Customizing the cache configuration can be done directly in the connection declaration:

```
<ibm-mq:config name="IBM_MQ_Config">
  <ibm-mq:connection>
    <ibm-mq:caching-strategy>
      <ibm-mq:default-caching sessionCacheSize="100" consumersCache="false" producersCache="true"/>
    </ibm-mq:caching-strategy>
  </ibm-mq:connection>
</ibm-mq:config>
```
xml## Identify the Connection Client

The client identifier associates a connection and its objects
with a state maintained on behalf of the client by a provider, and it is **mandatory**
for identifying an unshared durable subscription.

```
<ibm-mq:config name="IBM_MQ_Config">
  <ibm-mq:connection clientId="${env.clientId}"/>
</ibm-mq:config>
```
xml| By definition, the client state identified by a `clientId`can be "in use" by only one connection at a time. | 

## Set Up the Connection Required Libraries

**Important:** No matter what type of connection you are using, you always need to configure a library containing the JMS client implementation, since the connector is not bound to any particular implementation.

### IBM MQ External Libraries

To use the IBM MQ Connector, configure the external IBM MQ library,
The IBM MQ Client library must provide the `com.ibm.mq.jms.MQConnectionFactory` implementation.

| Use the IBM MQ Allclient library. | 

For example, you can use:

```
<dependency>
    <groupId>com.ibm.mq</groupId>
    <artifactId>com.ibm.mq.allclient</artifactId>
    <version>9.0.5.0</version>
</dependency>
```
xml## See Also

- 
[Salesforce Help](https://help.salesforce.com)