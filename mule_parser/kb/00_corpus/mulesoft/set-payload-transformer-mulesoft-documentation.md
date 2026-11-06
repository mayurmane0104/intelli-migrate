# Set Payload Transformer | MuleSoft Documentation

**Source:** [https://docs.mulesoft.com/mule-runtime/latest/set-payload-transformer-reference](https://docs.mulesoft.com/mule-runtime/latest/set-payload-transformer-reference)

---

`<set-payload value="{ 'name' : 'Ana', 'office' : 'BA' }" mimeType="application/json" encoding="UTF-8"/>`xml# Set Payload Transformer

The Set Payload (`set-payload`) component lets you update the payload of the message.
The payload can be a literal string or a DataWeave expression. The `set-payload`
component, however, is not recommended for complex expressions or transformations
but rather, simple ones, such as selections. You should use [Transform Message Component](transform-component-about)
for complex scenarios.

| Field | Usage | Description | 
|---|---|---|
| Value ( | Required | Accepts a literal string or DataWeave expression that defines how to set the payload, for example,  | 
| Mime Type ( | Optional | The mime type of the value assigned to the payload, for example,  | 
| Encoding ( | Optional | The encoding of the value assigned to the payload, for example,  | 

| The  | 

This XML example sets a payload with static values:

The next example sets the message payload to "Hello, World" appending today’s date using a DataWeave expression:
`#['Hello World!' ++ ' Today is ' ++ now()]`

`<set-payload value="#['Hello World!' ++ ' Today is ' ++ now()]"/>`xml