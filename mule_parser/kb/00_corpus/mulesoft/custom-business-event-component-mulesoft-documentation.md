# Custom Business Event Component | MuleSoft Documentation

**Source:** [https://docs.mulesoft.com/mule-runtime/latest/business-events-custom](https://docs.mulesoft.com/mule-runtime/latest/business-events-custom)

---

![Setup for a custom business event](_images/mruntime-custom-business-event.png) 

# Custom Business Event Component

Use the Custom Business Event component (`tracking:custom-event` element in the XML view) to add metadata and Key Performance Indicators (KPIs) to your flow. Configure the component as follows:

- 
Click the **Mule Palette**tab in Anypoint Studio.
- 
Drag **Custom Business Event**to any point of your flow.
- 
Open the component properties view and specify values for **Display Name**and**Event Name**:![Setup for a custom business event](_images/mruntime-custom-business-event.png)  

You can also configure Key Performance Indicators (KPIs) to capture information from the message payload:

- 
In the UI: - 
Click the plus button ( ![Add icon](_images/green-plus-icon.png) ]) inside ]) inside**Key Performance Indicators**.
- 
Configure **Name**and**Expression / Value**:![A configuration panel showing settings for a key performance indicator](_images/mruntime-business-events-kpi.png)  
 
- 
- 
In the XML: - 
Add a child `tracking:meta-data`element to the`tracking:custom-event`.
- 
Configure the `key`and`value`attributes inside`tracking:meta-data`:For example: `<tracking:custom-event doc:name="Custom Business Event" event-name="New order"> <tracking:meta-data key="order-id" value="#[payload.order.header.orderID]" /> </tracking:custom-event>`xml
 
- 

For your KPIs, use names that are easy to search for in the Anypoint Runtime Manager interface, and use a representative value, which can be any Mule expression:

| Name | Expression / Value | 
|---|---|
| 
 | 
 | 
| 
 | 
 | 
| 
 | 
 | 
| 
 | 
 | 
| 
 | 
 | 
| 
 | 
 |