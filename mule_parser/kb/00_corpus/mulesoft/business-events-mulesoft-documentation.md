# Business Events | MuleSoft Documentation

**Source:** [https://docs.mulesoft.com/mule-runtime/latest/business-events](https://docs.mulesoft.com/mule-runtime/latest/business-events)

---

# Business Events

Mule applications collect *business event* information (such as transaction execution time, errors, success or failure results, and message payload information) about flows and message processors that handle your *business transactions*:

- 
Events map to message processors and connectors and are the low-level details of a transaction. Events are not supported in batch processing. 
- 
Transactions are logical groupings of related events that often correspond to a business view of the system, at the flow level. 

## Business Event Types

You can track two types of business events: *default events* and *custom events*.

Default event tracking is supported by all connectors and selected message processors. Enabling default events for these elements enables you to perform advanced debugging at runtime. You can enable default event tracking at either the flow level or the message processor level.

See [Configure Default Events Tracking](business-events-in-components) for configuration details.

Custom event tracking is supported by the Custom Business Event component. Custom events are always tracked, enabling you to monitor high-level activities in your flow that are relevant to your business.

See [Custom Business Event Component](business-events-custom) for configuration details.

## Monitoring Business Events

You can enable Insight in Runtime Manager to monitor business events at runtime. These events can help you analyze the root cause of failures, isolate performance bottlenecks, and test for compliance with company procedures.

Certain default events are tracked automatically after you enable Insight, but you must enable others in your application before they are tracked.

See the [Insight](../../runtime-manager/insight) documentation for more details.

## Best Practices for Business Events

Consider the following recommended practices when configuring business events tracking:

- 
Enable default events only for processes that have particular value to you. To filter out unnecessary information, determine which stages within a business transaction you need to track, and enable tracking for only those stages. 
- 
Use custom events to track key process indicators: for example, "Total Order Amount" or "Tracking Number" to surface the high-level business activities in your flow. 
- 
Customize the transaction ID so that meaningful information, such as an order number, an employee identification number, or a shipment tracking number, is displayed for a transaction. 
 This practice makes analysis and debugging easier and more intuitive at runtime.