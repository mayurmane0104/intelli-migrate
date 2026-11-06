# For Each Scope | MuleSoft Documentation

**Source:** [https://docs.mulesoft.com/mule-runtime/latest/for-each-scope-concept](https://docs.mulesoft.com/mule-runtime/latest/for-each-scope-concept)

---

![A For Each component showing a flow with settings](_images/component-foreach-example.png) 

# For Each Scope

The For Each scope splits a payload into elements and processes them one by one through the components that you place in the scope.
It is similar to a `for-each`/`for` loop code block in most programming languages and can process any collection, including lists and arrays.
The collection can be any supported content type, such as `application/json`, `application/java`, or `application/xml`.

General considerations about the For Each scope:

- 
By default, For Each tries to split the payload. If the payload is a simple Java collection, the For Each scope can split it without any configuration. The payload inside the For Each scope is each of the split elements. Attributes within the original message are ignored because they are related to the entire message. 
- 
For Each does not modify the current payload. The output payload is the same as the input. 
- 
For non-Java collections, such as XML or JSON, use a DataWeave expression to split data. Use the **Collection**field for this purpose.In the following example, the **Collection**field in For Each is set to iterate over an array stored in`payload.topics`:![A For Each component showing a flow with settings](_images/component-foreach-example.png)  

The For Each scope stores each item of the collection in `payload` during each iteration.

You can also split an array into batches to enable quicker processing. Each batch is treated as a separate Mule message. For example, if a collection has 200 elements and you set **Batch Size** to `50`, the For Each scope iteratively processes 4 batches of 50 elements, each as a separate Mule message.

## Example XML

This is an example XML based on the For Each scope configuration detailed above:

```
...
  <foreach doc:name="For Each" collection="#[payload.topics]" batchSize="1" rootMessageVariableName="rootMessage" counterVariableName="counter">
      <file:write ... >
      <!--Any other module that you want to include in the For Each scope -->
  </foreach>
...
```
xml## Variable Propagation

Every execution of the For Each scope starts with the variables and values from the previous execution of the block. New variables or modifications to existing variables that take place when processing one element are visible during the processing of another element. These changes to variables continue to be available outside the For Each scope.

```
<set-variable variableName="var1" value="var1"/>
<set-variable variableName="var2" value="var2"/>
<foreach collection="#[['apple', 'banana', 'orange']]">
    <choice>
        <when expression="#[payload == 'apple']">
            <set-variable variableName="var2" value="newValue"/>
            <set-variable variableName="var3" value="appleVal"/>
        </when>
        <when expression="#[payload == 'banana']">
            <set-variable variableName="var3" value="#[vars.var3 ++ ' bananaVal']"/>
            <!-- var3 will now have value 'appleVal bananaVal'-->
        </when>
        <otherwise>
            <set-variable variableName="var3" value="otherVal"/>
            <set-variable variableName="var4" value="val4"/>
        </otherwise>
    </choice>
</foreach>
```
xmlAfter aggregation, the variables are:

`{var1: "var1", var2: "newValue", var3: "otherVal", var4: "val4"}`json## Error Handling

If one of the elements in a collection throws an exception, the For Each scope stops processing that collection and invokes the error handler.

## Example Projects

There are several example projects in Anypoint Exchange that you can open in Anypoint Studio to learn more about how to use the For Each scope:

- 
*Authenticating Salesforce using OAuth2*
- 
*Import contacts into Microsoft Dynamics CRM*
- 
*Importing a CSV file into mongoDB*
- 
*Importing an Email Attachment using the IMAP Connector*
- 
*Importing Email Attachments using the POP3 Connector*
- 
*Querying a Database and Attaching Results to an Email*

To download and open an example project while you are in Anypoint Studio, click the Exchange icon in the upper-left corner. Then, in the window that opens, log into Anypoint Exchange and search on the name of the project.

## XML Reference

For Each scopes open and close with a `<foreach>` tag. Components that are affected by this scope are defined as child elements of the `<foreach>` tag.

### Configurable Variables

| Variable | Default | Description | 
|---|---|---|
| 
 | 
 | An expression that returns a Java collection, object array, map, or DOM nodes. | 
| 
 | 
 | Name of the variable that stores the number of messages over which it iterates. | 
| 
 | 
 | Partitions the collection into sub-collections of the specified size. For example, if a collection has 200 elements and you set the batch size to 50, it processes 4 batches of 50 elements each. | 
| 
 | 
 | Name of the variable that stores the parent message. The parent is the complete, non-split message. | 

## Differences between For Each and Parallel For Each Scopes

Both For Each and Parallel For Each split the defined collection, and the components within the scope process each element in the collection. Also, in both cases, each route runs with the same initial context. The difference between these two scopes are:

- 
For Each works sequentially, while the Parallel For Each processes in parallel. This difference affects *error handling*:Because of the processing differences, the execution of For Each execution is interrupted when an error is raised (and the Error Handler is invoked), while Parallel For Each processes every route before invoking the Error Handler with a `MULE:COMPOSITE_ROUTE`error type.
- 
For Each does not modify the payload, while the Parallel For Each outputs a collection of the output messages from each iteration.