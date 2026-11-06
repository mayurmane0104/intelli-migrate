# Anypoint MQ Connector Overview | MuleSoft Documentation

**Source:** [https://docs.mulesoft.com/anypoint-mq-connector/latest](https://docs.mulesoft.com/anypoint-mq-connector/latest)

---

```
<dependency>
  <groupId>com.mulesoft.connectors</groupId>
  <artifactId>anypoint-mq-connector</artifactId>
  <version>x.x.x</version>
  <classifier>mule-plugin</classifier>
</dependency>
```
xml# Anypoint MQ Connector Overview

Anypoint Connector for Anypoint MQ (Anypoint MQ Connector) provides publish-subscribe messaging to Mule apps using the Anypoint MQ cloud service.

Anypoint MQ supports a wide range of messaging use cases, such as enterprise messaging patterns, asynchronous communications between microservices, and IoT. Anypoint MQ also has a REST API for publishing or consuming messages using frameworks such as node.js, Java, Go, and DevOps bash scripts.

## Requirements

To use this connector, you must be familiar with Anypoint Studio, Anypoint Connectors, and application flows. Anypoint MQ Connector is free, but connecting to the service in Anypoint Platform requires a license.

### Compatibility

| Software | Version | 
|---|---|
| Mule runtime engine | 4.1.1 and later | 
| Anypoint Studio | 7 and later | 

This documentation applies to Anypoint MQ Connector 4.x only. To migrate from version 3.x to the version 4.x, see
[Upgrading and Migrating Anypoint MQ Connector](anypoint-mq-connector-upgrade-migrate).

## Install Anypoint MQ Connector

You can use this connector with apps written in Anypoint Studio, standalone apps, or apps written in XML.

In Anypoint Studio:

- 
Create or open a Mule project. 
- 
Click the **Exchange**icon in the Studio task bar.
- 
Enter your Anypoint Platform username and password and click **Sign in**.
- 
Select **All assets**and search for`MQ`.
- 
Select **Anypoint MQ Connector - Mule 4**, and click**Add to project**.
- 
Follow the prompts to install the connector. 

For standalone apps or apps written in XML:

- 
Open your Mule project in Anypoint Studio. 
- 
Add the connector as a dependency in the `pom.xml`file:

Replace `x.x.x` with the version that corresponds to the connector you are using.

To obtain the most up-to-date `pom.xml` file information, access the connector in [Anypoint Exchange](https://www.mulesoft.com/exchange/) and click **Dependency Snippets**.

## Configure an Operation in a Mule Project

In Anypoint Studio:

- 
Install the connector, if it’s not already installed. 
- 
Create or open a Mule project. 
- 
Search for `mq`in the**Mule Palette**.
- 
Click **Anypoint MQ**to see the available operations for the connector.![The Mule Palette with Anypoint MQ Connector selected,  displaying the available operations](_images/amq-4x-connector-palette.png)  
- 
Configure the operation accordingly. Operation Description Indicates that the message was consumed correctly and deletes the message from `In Flight`status.Consumes messages from a queue. Changes the status of the message from `In Flight`to`In Queue`to be consumed again by an available consumer.Publishes messages to a destination. Listens for messages from a queue. 

### Configure the Connection to the Default Subscriber

For each operation, you must configure a connection to a subscriber.

- 
In Anypoint Studio, drag the name of the operation from the **Mule Palette**to the canvas, and then select it.
- 
Click the green plus sign for **Connector configuration**.
- 
In Anypoint Platform, click **MQ > Destinations**.
- 
Click **Copy**and select**Connector version 4.x and later**from the menu:![Copy button and menu with connector version options](../../mq/_images/mq-tutorial-url.png)  
- 
In Anypoint Studio, in the **Anypoint MQ Config**window, paste the URL in the**URL**field.
- 
In Anypoint MQ, click **MQ > Client Apps**.If needed, create a client app. 
- 
Click the client app name to display the details pane. 
- 
Copy the client app ID and client secret values from the details pane to the **Anypoint MQ Config**window in Studio:![Global Element properties, including URL, client app ID, and client secret](../../mq/_images/mq-tutorial-studio7-mq-config.png)  
- 
Click **Test Connection**to verify the Anypoint MQ Default subscriber.
- 
Click **OK**.

For more information, see
[Create and Connect a Mule 4 App to Anypoint MQ in Anypoint Studio 7](../../mq/mq-tutorial#configure-mule-4-studio) in the
[Anypoint MQ Tutorial](../../mq/mq-tutorial).

## See Also

- 
[Anypoint MQ Connector in Anypoint Exchange](https://anypoint.mulesoft.com/exchange/com.mulesoft.connectors/anypoint-mq-connector/)