# Set Variable Transformer | MuleSoft Documentation

**Source:** [https://docs.mulesoft.com/mule-runtime/latest/variable-transformer-reference](https://docs.mulesoft.com/mule-runtime/latest/variable-transformer-reference)

---

Variable Name (`variableName`)

# Set Variable Transformer

The Set Variable (`set-variable`) component is for creating or updating a [Mule variable](about-mule-variables) to store values for use within the flow of a Mule app. A Mule variable is part of the [Mule event](about-mule-event). You can store simple literal values such as strings or messages, message payloads, or attribute objects. For example, you might store the original payload of a message (before it is processed) so you can use it later in the flow or within an error handler.

The `set-variable` component is not recommended for complex expressions or transformations. You should instead use it for simple ones, such as selections, and use the [Transform Component](transform-component-about)
for complex scenarios.

## Reference

Set Variable provides a way to set the name and value of Mule variable, along with configurable properties.

| Field | Usage | Description | 
|---|---|---|
| Required | Name of the variable, which must be a string. Variable names can include only numbers, characters, and underscores. For example, hyphens are not allowed in the name. | |
| Value ( | Required | Value for the variable, which can be a string or a DataWeave expression. For an example that uses an expression, see  | 
| Mime Type ( | Optional | Sets the variable MIME type, such as  | 
| Encoding ( | Optional | Sets the variable encoding, such as  | 

| The  | 

## Examples

This example sets the variable to a string:

- 
Name = `myVar`
- 
Value = `my first variable`

This example sets the variable by using a DataWeave operation that results in a value of `5`:

- 
Name = `myVar`
- 
Value = `#[max([1,2,3] ++ [3,4,5])]`in Anypoint Studio.

This example sets the variable to the message payload:

- 
Name = `myVar`
- 
Value = `payload`in Design Center,`#[payload]`in Anypoint Studio.

This example sets the variable to the message attributes:

- 
Name = `myVar`
- 
Value = `attributes`in Design Center,`#[attributes]`in Anypoint Studio.

This example sets the variable to the entire message:

- 
Name = `myVar`
- 
Value = `message`in Design Center,`#[message]`in Anypoint Studio.

This XML example sets a variable that takes a map as a value:
`<set-variable variableName="employee" value="{ 'name' : 'Ana', 'office' : 'BA' }" mimeType="application/json" encoding="UTF-8"/>`

This example sets the same variable using selectors in a DataWeave script. It assumes the `name` attribute is available as input to Set Variable:
`<set-variable variableName="employee" value="#[output application/java --- payload.name]"/>`

These examples set the variable to a Boolean value, `true`:

- 
Name = `myVar`
- 
Value = - 
`true`in Design Center,`#[true]`in Anypoint Studio
- 
`true as Boolean`in Design Center,`#[true as Boolean]`in Anypoint Studio
- 
`(1 + 1 == 2)`evaluates to`true`in Design Center,`#[(1 + 1 == 2)]`evaluates to`true`in Anypoint Studio.
 
- 

This example sets a variable to a Java object by using a DataWeave script. The script outputs the object in Java format:  ```
<set-variable value='#[%dw 2.0
output application/java
---
{
  name: "Tomo",
  lastName: "Chibana",
  expirationDate: now(),
  salesRepr: {
  name: "Mariano",
  lastName: "de Achaval",
  }
} as Object {class: "Customer"}]' doc:name="Set Variable" variableName="Variable to Java Object"/>
```
.

For more information about the Java data format, refer to the [Java Format examples](../../dataweave/latest/dataweave-formats-java#format_examples) documentation.

To display the value of a variable through the Logger component in Design Center, you might need to use the Anypoint Studio syntax, for example, `#[vars.myVar]` instead of `vars.myVar`.

## Accessing Variables in Other Event Processors

Set Variable sets a variable in the current Mule event, and the variables then travel with the Mule event to downstream event processors. You can access any variable with DataWeave using `vars`. So if you set a variable named lastMessage, you can access it as `vars.lastMessage`.  You can set variables in a Transform Message component, and also many connectors and event processors have a Target that can be set in the Advanced tab. These all set flow variables and they are accessed the same way, through the keyword `vars.`.