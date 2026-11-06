# Notifications Configuration Reference | MuleSoft Documentation

**Source:** [https://docs.mulesoft.com/mule-runtime/latest/notifications-configuration-reference](https://docs.mulesoft.com/mule-runtime/latest/notifications-configuration-reference)

---

# Notifications Configuration Reference

This topic provides details on the elements to configure for notifications. For more information on notifications, see [Mule Server Notifications](mule-server-notifications).

## Notifications

Registers listeners for notifications, and associates interfaces with specific events.

### Attributes of Notifications

| Name | Description | 
|---|---|
| 
 | If the notification manager is dynamic, you can set up the listeners to be registered dynamically at runtime. Otherwise, some parts of Mule will cache the notification configurations for efficiency reasons and will not generate events for newly-enabled notifications or listeners. | 

### Child Elements of Notifications

Use the `notification` and `disable-notification` elements to configure the relationship between interfaces and events.

| Name | Cardinality | Description | 
|---|---|---|
| 
 | 0..* | Associates an event with an interface. Listeners that implement the interface receive instances of the event. | 
| 
 | 0..* | Blocks the association of an event with a particular interface. This filters events after the association is made with the interface, so it takes precedence over other elements, such as  | 
| 
 | 0..* | Registers a bean as a listener with the notification system. Events are dispatched by reflection, which means that the listener receives all events associated with the interfaces it implements. | 

## Notification

Associates an event with an interface. Listeners that implement the interface will receive instances of the event.

### Attributes of Notification

| Name | Description | 
|---|---|
| 
 | The class name of the notification event to deliver to the interface. You can use this instead of the  | 
| 
 | The notification event to deliver. | 
| 
 | The class name of the interface that receives the notification event. | 
| 
 | The name of the interface that receives the notification event. | 

There are no child elements for `notification`.

## Disable Notification

Blocks the association of an event with a particular interface. This filters events after the association is made with the interface, so it takes precedence over other elements, such as `notification-listener`.

### Attributes of disable-notification

| Name | Description | 
|---|---|
| 
 | The class name of the event that is no longer delivered to an interface. You can use this instead of the  | 
| 
 | The event you no longer want to deliver. | 
| 
 | The class name of the interface that no longer receives the event. | 
| 
 | The name of the interface that no longer receives the event. | 

There are no child elements for `disable-notification`.

## Notification Listener

Registers a bean as a listener with the notification system. Events are dispatched by reflection, which means that the listener receives all events associated with the interfaces it implements.

## Notification Types

You can specify the following types of notifications using the `event` attribute of the `notification` and `disable-notification` elements:

- 
ASYNC-MESSAGE 
- 
CONNECTION 
- 
CONNECTOR-MESSAGE 
- 
CONTEXT 
- 
CUSTOM 
- 
EXCEPTION 
- 
EXCEPTION-STRATEGY 
- 
MANAGEMENT 
- 
MESSAGE-PROCESSOR 
- 
PIPELINE-MESSAGE 
- 
ROUTING 
- 
SECURITY 
- 
TRANSACTION