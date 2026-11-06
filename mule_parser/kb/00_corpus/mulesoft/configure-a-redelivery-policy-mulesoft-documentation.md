# Configure a Redelivery Policy | MuleSoft Documentation

**Source:** [https://docs.mulesoft.com/mule-runtime/latest/redelivery-policy](https://docs.mulesoft.com/mule-runtime/latest/redelivery-policy)

---

**Max Redelivery Count**

# Configure a Redelivery Policy

A redelivery policy is a filter that helps you conserve resources by limiting the number of times the Mule runtime engine (Mule) executes messages that generate errors. You can add a redelivery policy to any source in a flow.

When you add a redelivery policy to a flow’s source, Mule evaluates the received data before it executes the flow’s components. If a message delivery fails a specified number of times, the redelivery policy prevents the flow from processing the received data and raises a REDELIVERY_EXHAUSTED error.

## Redelivery Policy Configuration Parameters

| Field | Type | Default Value | Description | 
|---|---|---|---|
| Number | 5 | Maximum number of times that a message can be redelivered to the flow and processed unsuccessfully before raising a MULE:REDELIVERY_EXHAUSTED error. | |
| 
 | Boolean | True | Indicates whether to use a secure hash algorithm to identify a redelivered message. | 
| 
 | String | SHA-256 | Secure hashing algorithm to use for the message. If the payload of the message is a Java object, Mule ignores the  | 
| 
 | Expression | - | Defines one or more expressions that determine when a message has been redelivered. This property can be set only if the value of  | 
| 
 | String | Object Store created by Mule’s default  | Object Store in which the redelivery counter for each message is stored. You can configure the Object Store as a reference or an inner element. For information, see the  | 

## How the Redelivery Policy Works

Each time the source receives a new message, Mule identifies the message by generating its key.

- 
If the processing flow causes an exception, Mule increments the counter associated with the message key. When the counter reaches a value greater than the configured **maxRedeliveryCount**value, Mule throws a MULE:REDELIVERY_EXHAUSTED error.
- 
If the processing flow does not cause an exception, its counter is reset. 

## Errors

- 
MULE:REDELIVERY_EXHAUSTED Thrown when the number of executions that raise an error is greater than the configured **maxRedeliveryCount**value.

## Example

In this example, Mule logs an error with a `Redelivery exhausted in http listener` message when the **maxRedeliveryCount** of 2 is exceeded:

```
<flow name="logOnRedeliveryExhausted">
    <http:listener path="test" config-ref="listenerConfig">
        <redelivery-policy maxRedeliveryCount="2" useSecureHash="true"/>
    </http:listener>
    <flow-ref name="processData"/>
    <error-handler>
        <on-error-continue type="MULE:REDELIVERY_EXHAUSTED">
            <logger message="Redelivery exhausted in http listener" level="ERROR"/>
        </on-error-continue>
    </error-handler>
</flow>
```
xml