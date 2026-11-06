# Remove Variable Transformer | MuleSoft Documentation

**Source:** [https://docs.mulesoft.com/mule-runtime/latest/remove-variable](https://docs.mulesoft.com/mule-runtime/latest/remove-variable)

---

Customize to display a unique name for this component in Anypoint Studio. Defaults to `Remove Variable`.

# Remove Variable Transformer

The Remove Variable component takes a Mule variable name and removes the variable from a Mule event.

| Field | XML | Description | 
|---|---|---|
| Display Name | 
 | |
| Name | 
 | Name of the variable to remove. If the variable does not exist in the flow, the component logs a warning ( | 

## Example

This basic example shows how to remove a Mule variable from the flow:

```
<flow name="remove-variable-ex" >
  <scheduler doc:name="Scheduler" >
    <scheduling-strategy >
      <fixed-frequency frequency="10" timeUnit="SECONDS"/>
    </scheduling-strategy>
  </scheduler>
  <set-variable value='"value of my Mule variable"' doc:name="Set Variable"
                variableName="myMuleVar"/>
  <logger level="INFO" doc:name="Logger"
          message="#[vars.myMuleVar]"
          category="PRINT VALUE OF VARIABLE"/>
  <remove-variable doc:name="Remove Variable"
                   variableName="myMuleVar"/>
  <logger level="INFO" doc:name="Logger"
           category="ATTEMPT TO PRINT VALUE OF REMOVED VARIABLE"
           message="#[vars.myMuleVar]"/>
  <remove-variable doc:name="Remove Variable"
                   variableName="banana"/>
</flow>
```
xmlThe flow uses the following processors:

- 
The Scheduler component triggers the flow. 
- 
Set Variable creates a Mule variable ( `myMuleVar`).
- 
The first Logger in the flow prints the value of the variable ( `"value of my Mule variable"`).
- 
Remove Variable provides a string with the name of the variable ( `variableName="myMuleVar"`) to remove the variable from the Mule event.
- 
The second Logger prints `null`because the Mule variable no longer exists.
- 
The second Remove Variable logs a `WARN`message because it attempts to remove a Mule variable (`banana`) that does not exist in the Mule event.

The following example shows the logs for an execution of this flow:

`INFO 2022-12-15 08:33:20,151 ...event: 2f65e920-7c96-11ed-97ec-147ddaaf4f97] PRINT VALUE OF VARIABLE: "value of my Mule variable" INFO 2022-12-15 08:33:20,155 ...event: 2f65e920-7c96-11ed-97ec-147ddaaf4f97] ATTEMPT TO PRINT VALUE OF REMOVED VARIABLE: null WARN 2022-12-15 08:33:20,156 ...event: 2f65e920-7c96-11ed-97ec-147ddaaf4f97] ...RemoveFlowVariableProcessor: There is no variable named 'banana'. Check the 'variableName' parameter in the 'remove-variable' component at remove-variable-ex/processors/4`logs