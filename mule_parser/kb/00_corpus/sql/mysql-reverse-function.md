# MySQL REVERSE() Function

**Source:** [https://www.w3schools.com/sql/func_mysql_reverse.asp](https://www.w3schools.com/sql/func_mysql_reverse.asp)

---

# MySQL REVERSE() Function

## Definition and Usage

The REVERSE() function reverses a string and returns the result.

## Syntax

```
  REVERSE(
```
*string*)
## Parameter Values

| Parameter | Description | 
|---|---|
| string | Required. The string to reverse | 

## Technical Details

| Works in: | From MySQL 4.0 | 
|---|

## More Examples

### Example

Reverse the text in CustomerName:

```
  SELECT REVERSE(CustomerName)
FROM Customers; 
```
[Try it Yourself »](trymysql.asp?filename=trysql_func_mysql_reverse2)

Ad