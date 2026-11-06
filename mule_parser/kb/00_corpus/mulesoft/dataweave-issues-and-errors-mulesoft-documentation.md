# DataWeave Issues and Errors | MuleSoft Documentation

**Source:** [https://docs.mulesoft.com/anypoint-code-builder/troubleshoot-dataweave](https://docs.mulesoft.com/anypoint-code-builder/troubleshoot-dataweave)

---

!['Unable to find sample input' error](_images/dw-issue-sample-data.png) 

# DataWeave Issues and Errors

When Anypoint Code Builder can’t process a value, the IDE provides a visual indicator to identify an issue with the value. Issues include:

## Unable to Find Sample Input

The DataWeave error `Unable to find sample input` applies to a Mule event variable, such as `payload`. In this case, the IDE places a wavy blue line under the value in the configuration XML file.

!['Unable to find sample input' error](_images/dw-issue-sample-data.png) 

If your application isn’t running, the IDE can’t provide any information about Mule variables unless you provide sample data.
Use [Quick Fix](int-configure-dw-expressions#sample-data) to provide sample data in the format and data structure that you expect to be present when the application runs.

For more information about Mule event variables, see [Predefined Variables](../dataweave/latest/dataweave-variables-context).

## Unable to Resolve Reference

The error `Unable to resolve reference` is typically for a sequence of characters like `afkdldjf` that isn’t recognized.

![`Unable to resolve reference` error](_images/dw-issue-reference-resolution.png) 

Either provide the intended value or use [Quick Fix](int-configure-dw-expressions#sample-data) to convert the character sequence into a DataWeave variable. For more information, see [DataWeave Variables](../dataweave/latest/dataweave-variables).

## Expects *x* but Got *y*

The error similar to `Expects ` typically indicates that something is wrong with the provided function. For example, *x* but got *y*`Expects 1 argument but got 0` occurs for `round()` because the function is missing an argument, in this case, a number to round. An example of a fix is `round(1.65)`. Similar errors indicate that an argument is of the wrong data type or that a function is otherwise malformed and requires correction.

Read the error message to determine what part of the expression to fix, and review the function description after the error message to learn more about the function. See [DataWeave Modules](../dataweave/latest/dw-functions#dw_modules) to find additional DataWeave function documentation.

## Invalid Input

The error `Invalid input` typically occurs when special characters, such as `?`, appear in a DataWeave expression and aren’t escaped, for example:

!['Invalid input' error](_images/dw-issue-invalid-input.png) 

For more information, see [Rules for Declaring Valid Identifiers](../dataweave/latest/dataweave-language-introduction#valid-identifiers) and [Escape Special Characters](../dataweave/latest/dataweave-language-introduction#escape-special-characters).