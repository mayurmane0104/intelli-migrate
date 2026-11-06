# Try Scope XML Reference | MuleSoft Documentation

**Source:** [https://docs.mulesoft.com/mule-runtime/latest/try-scope-xml-reference](https://docs.mulesoft.com/mule-runtime/latest/try-scope-xml-reference)

---

```
<try>
  <!-- COMPONENTS TO TRY TO USE -->
  <error-handler>
    <on-error-continue>
      <!-- COMPONENTS TO USE IN CASE OF ERROR -->
    </on-error-continue>
    <on-error-propagate>
      <!-- COMPONENTS TO USE IN CASE OF ERROR -->
    </on-error-propagate>
  </error-handler>
</try>
```
xml# Try Scope XML Reference

A Try scope follows the structure described below.

- 
A single root element `<try>`
- 
Components that are executed under the error-handling rules defined by the Try scope are defined as child elements of the `try`element. You can place one or many here.
- 
A single `<error-handler>`element holds all error handling strategies for the scope.
- 
In the error handler, one or several `on-error-continue`and`on-error-propagate`define the various strategies. At least one of these must be present.
- 
Components that are executed when a matching error occurs are defined as child elements of the `on-error`element. You can place one or many here.

Each error handling strategy in a Try scope (`on-error-*`) follows a condition. This condition is typically an error type (or a list of several) which must match the current error. You can also define this condition as a freely written expression, such as `error.cause.message.contains("fatal")`.

| Note that conditions are evaluated in order and only the first strategy to match is executed. | 

Below is an example that includes two error handling strategies, each executing a logger component:

```
<try>
  <http:request config-ref="HTTP-config" method="GET" path="/" />
  <error-handler>
    <on-error-continue enableNotifications="true" logException="true" type="CONNECTIVITY">
      <logger level="INFO" doc:name="Logger" message="Connectivity Error"/>
    </on-error-continue>
    <on-error-propagate enableNotifications="true" logException="true" doc:name="On Error Propagate" type="EXPRESSION">
      <logger level="INFO" doc:name="Logger" message="Expression error" />
    </on-error-propagate>
  </error-handler>
</try>
```
xml## Properties of Try

| Property | Default | Description | 
|---|---|---|
| 
 | INDIFFERENT | Defines if what’s in the scope is treated as a transaction. Possible values: 
 | 
| 
 | LOCAL | Defines the type of transaction to use. Possible values: 
 |