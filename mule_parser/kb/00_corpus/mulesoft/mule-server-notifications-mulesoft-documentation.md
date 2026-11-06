# Mule Server Notifications | MuleSoft Documentation

**Source:** [https://docs.mulesoft.com/mule-runtime/latest/mule-server-notifications](https://docs.mulesoft.com/mule-runtime/latest/mule-server-notifications)

---

`<bean name="notificationLogger" class="org.myfirm.ProcessorNotificationStore"/>`xml# Mule Server Notifications

Mule provides an internal notification mechanism that you can use to access changes that occur on the Mule Server, such as adding a flow component, a request for authorization failing, or Mule starting. You can set up your agents or flow components to react to these notifications.

## Configuring Notifications

Message notifications provide a snapshot of all information sent into and out of the Mule Server. Mule fire these notifications whenever it receives or sends a message. These additional notifications have some impact on performance, so they are disabled by default. To enable message notifications, you set the type of messages you want to enable using the `<notifications>` element in your Mule configuration file. You also register the notification listeners and associate interfaces with specific notifications.

For example, first you create beans for the notification listeners in your spring configuration file, specifying the class of the type of notification you want to receive:

And then, add the reference for your spring configuration:

`<spring:config name="springConfig" files="notification-beans.xml"/>`xmlNext, you specify the notifications you want to receive using the `<notification>` element, and then register the listeners using the `<notification-listener>` element:

```
<notifications>
    <notification event="MESSAGE-PROCESSOR"/>
    <notification-listener ref="notificationLogger"/>
</notifications>
```
xmlWhen you specify the MESSAGE-PROCESSOR notification, a notification is sent before and after a message processor is invoked. Because the listeners implement the interface for the type of notification they want to receive, the listeners receive the correct notifications.

For example, the `ProcessorNotificationLogger` class would implement `org.mule.runtime.api.notification.MessageProcessorNotificationListener`:

```
public class ProcessorNotificationLogger implements MessageProcessorNotificationListener<MessageProcessorNotification> {
    @Override
    public void onNotification(MessageProcessorNotification notification) {
        // write here the logic to process the notification event
    }
}
```
java| Don’t forget to add the mule-api dependency in your pom file with `provided`as scope, so the api classes will be available in your classpath. The dependency will then be provided by mule in runtime. | 

For a list of notification types, see [Notifications Configuration Reference](notifications-configuration-reference). For a list of notification listener interfaces, see [Notification Interfaces](#notification-interfaces) below.

### Specifying a Different Interface

If you want to change the interface associated with a notification, you specify the new interface with the `interface-class` attribute:

```
<notifications>
    <notification event="COMPONENT-MESSAGE" interface-class="org.myfirm.MyMessageNotifications"/>
</notifications>
```
xml### Configuring a Custom Notification

If you create a custom notification, you also specify the `event-class` attribute:

```
<notifications>
  <notification event="CUSTOM" event-class="org.myfirm.MyMessageNotificationsCustomMessage"
  interface-class="org.myfirm.MyMessageNotifications"/>
</notifications>
```
xml### Disabling Notifications

If you want to block a specific interface from receiving a notification, you specify it with the `<disable-notification>` element. You can specify the notification type (event), event class, interface, and/or interface class to block.

```
<notifications>
    <disable-notification interface="SECURITY"/>
</notifications>
```
xml### Using Subscriptions

When registering a listener, you can specify that it only receives notifications from a specific component using the `subscription` attribute. For example, to specify that the listener only receives notifications from a flow component called "MyService1", you would configure the listener as follows:

```
<notification-listener ref="endpointNotificationLogger" subscription="MyService1"/>
<object name="endpointNotificationLogger" class="org.myfirm.EndpointNotificationLogger"/>
```
xmlTo register interest in notifications from all flow components with "Service" in the name, you would use a wildcard string as follows:

<notification-listener ref="endpointNotificationLogger" subscription="*Service*"/>

For more information, see [Registering Listeners Programmatically](#registering-listeners-programmatically) below.

## Firing Custom Notifications

Objects can fire custom notifications in Mule to notify custom listeners. For example, a discovery agent might fire a Client Found notification when a client connects.

You fire a custom notification as follows:

`CustomNotification n = new CustomNotification("Hello"); notificationDispatcher.dispatch(n);`text

Any objects implementing `CustomNotificationListener` will receive this notification. It’s a good idea to extend `CustomNotification` and define actions for your custom notification type. For example:

`DiscoveryNotification n = new DiscoveryNotification(client, DiscoveryNotification.CLIENT_ADDED); notificationDispatcher.dispatch(n);`text

## Notification Interfaces

The following table describes the Mule server notifications and the interfaces in the `org.mule.runtime.api.notification` package. An object can implement one of these interfaces to become a listener for the associated notification. All listeners extend the `NotificationListener` interface.

| Notification | Description | Interface | 
|---|---|---|
| Connection Notification | Is fired when a connection is made or disconnected. | 
 | 
| Custom Notification | Can be fired by components and other objects such as routers, transformers, agents to communicate a change of state to each other. | 
 | 
| Exception Notification | An exception was thrown. | 
 | 
| Management Notification | The state of the Mule instance or its resources have changed, such as internal queues reach capacity. | 
 | 
| Mule Context Notification | Can be fired when an event such as the mule context start occurs. | 
 | 
| Routing Notification | Async-Reply routers use this when an event is received for an event group that has already been processed. | 
 | 
| Security Notification | Is fired when a request for authorization failed. | 
 | 
| Transaction Notification | Is fired after a transaction has begun, was committed, or was rolled back. | 
 | 
| Async-Message Notification | Can be fired when async work is scheduled and completed for a given flow. | 
 | 
| Pipeline-Message Notification | Is fired at key steps in the processing of pipeline. | 
 | 
| Message-Processor Notification | A message processor was invoked. | 
 | 
| Exception Strategy Notification | An exception strategy was invoked. | 
 | 
| Extension Notification | Can be fired by extensions, including custom data. | 
 | 
| Connector-Message Notification | Is fired when a message is received or sent through a Connector. | 
 | 

The listener interfaces all have a single method:

`public void onNotification(T notification);`javawhere T is a notification class (listener class without the 'Listener' at the end).

Depending on the listener implemented, only certain notifications will be received. For example, if the object implements `ManagementNotificationListener`, only notifications of type `ManagementNotification` will be received. Objects can implement more than one listener to receive more types of notifications.

## Registering Listeners Programmatically

You can register listeners as follows:

notificationListenerRegistry.registerListener(listener);

or:

notificationListenerRegistry.registerListener(listener, selector);

where `listener` is a `NotificationListener<N>` instance and `selector` is a `Predicate<N>` that works as a filter to apply on a fired notification before calling the listener with it.

## Notification Action Codes

Each notification has an action code that determines the notification type. You can query the action code to determine its type. For example:

**MyObject.java**

```
public class MyObject implements ConnectionNotificationListener<ConnectionNotification> {
    (...)
    public void onNotification(ConnectionNotification notification) {
        if (valueOf(ConnectionNotification.CONNECTION_FAILED).equals(notification.getAction().getIdentifier())) {
            // write here the logic to handle the connection failed notification
        }
     }
}
```
java## Notification Payloads

All notifications extend `java.util.EventObject`, and you can use the `getSource()` method to access the payload of the object. The following table describes the payloads for each type of notification.

| Notification | Payload Type | Resource ID | Description | 
|---|---|---|---|
| Connection Notification | String | 
 | The message receiver or message dispatcher that was connected. | 
| Custom Notification | Any object | Any String | The object type is custom to the object firing the notification. | 
| Exception Notification | ComponentLocation | Component name | The flow component that triggered this notification. | 
| Management Notification | Object | The object ID | The monitored object that triggered this notification. | 
| Mule Context Notification | MuleContext | Mule context ID | The Mule context instance. Equivalent to calling getMuleContext(). | 
| Routing Notification | Message | Message ID | The message sent or received. | 
| Security Notification | SecurityException | The exception message | The security exception that occurred. | 
| Transaction Notification | String | Transaction ID | The transaction that have triggered this notification. | 
| Async-Message Notification | ComponentLocation | Component name | Component that has scheduled the async work. | 
| Pipeline-Message Notification | String | Name | Pipeline name. | 
| Message-Processor Notification | ComponentLocation | Component name | The flow component that triggered this notification. | 
| Exception Strategy Notification | ComponentLocation | Component name | The flow component that triggered this notification. | 
| Extension Notification | Object | Extension name | The payload can change from one extension to another. | 
| Connector-Message Notification | ComponentLocation | Component name | The flow component that triggered this notification. |