# MS Access Format() Function

**Source:** [https://www.w3schools.com/sql/func_msaccess_format_number.asp](https://www.w3schools.com/sql/func_msaccess_format_number.asp)

---

# MS Access Format() Function

### Example[Get your own SQL Server](/sql/sql_server.asp)

Format a numeric expression to percent:

```
  SELECT Format(0.5, "Percent") AS FormattedNum;  
```
[Try it Yourself »](trysql.asp?filename=trysql_func_ms_format_number&ss=-1)

## Definition and Usage

The Format() function formats a numeric value with the specified format.

## Syntax

```
  Format(
```
*value*, *format*)
## Parameter Values

| Parameter | Description | ||||||||||||||||||||
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| value | Required. The numeric value to format | ||||||||||||||||||||
| format | Optional. The format to to use. 
 | 

Ad

## Technical Details

| Works in: | From Access 2000 | 
|---|

## More Examples

### Example

Format the "Price" column to currency:

```
  SELECT Format(Price, "Currency") AS FormattedPrice
FROM Products;  
```
[Try it Yourself »](trysql.asp?filename=trysql_func_ms_format_number2&ss=-1)