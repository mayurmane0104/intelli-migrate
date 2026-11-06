# Batch Errors | MuleSoft Documentation

**Source:** [https://docs.mulesoft.com/mule-runtime/latest/batch-error-concept](https://docs.mulesoft.com/mule-runtime/latest/batch-error-concept)

---

`#[Batch::failureErrorForStep(String)]`

# Batch Errors

When a Mule app processes records through batch steps, record-level failures result in a `BatchError` object associated with the failed record. You can use DataWeave functions and selector expressions to inspect error details such as description, type, and stack trace. Starting with Mule 4.11, batch record errors replace exception-based tracking and wrap [Mule error](mule-error-concept) objects with enhanced error data.

## Accessing Batch Errors

Within a batch step, you can access record errors using these DataWeave functions:

| DataWeave Function | Description | 
|---|---|
| Receives the name of a step as a String argument. Returns the  | |
| 
 | Returns a  | 
| 
 | Returns the  | 
| 
 | Returns the  | 

## Selector Expressions for Batch Errors

Batch errors are complex data types with several fields, such as a description and type. When logging and handling batch errors, you can select values from any of these fields. This table shows selector expressions for the first step in which the current record failed:

| Field | Description | Selector Expression | 
|---|---|---|
| Description | A description of the problem. | 
 | 
| Detailed Description | A description of the problem, which can be the same or more extensive than the description field. | 
 | 
| Type | A type that characterizes the problem and allows for routing within an error handler. | 
 | 
| Failing Component | The component where the error is generated. | 
 | 
| DSL Source | The DSL source of the component where the error is generated. | 
 | 
| Error Message | An optional Mule message with error data (for example, HTTP response content for invalid status codes). | 
 | 
| Child Errors | An optional collection of inner errors, used by elements like Scatter-Gather to provide aggregated route errors. | 
 | 
| Failure During Handling | Any error that occurs while handling this error. | 
 | 
| Stack Trace | The Java stack trace of the exception. | 
 | 

## Batch Error Types

Batch errors follow the same error type hierarchy as standard Mule errors. A special `MULE:BATCH` error type exists for errors that arise during internal batch processing (rather than chain execution) and don’t belong to any specific type.