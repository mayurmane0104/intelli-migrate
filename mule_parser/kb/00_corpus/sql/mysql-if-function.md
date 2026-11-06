# MySQL IF() Function

**Source:** [https://www.w3schools.com/sql/func_mysql_if.asp](https://www.w3schools.com/sql/func_mysql_if.asp)

---

# MySQL IF() Function

### Example[Get your own SQL Server](/sql/sql_server.asp)

Return "YES" if the condition is TRUE, or "NO" if the condition is FALSE:

```
  SELECT 
  IF(500<1000, "YES", "NO"); 
```
[Try it Yourself »](trymysql.asp?filename=trysql_func_mysql_if)

## Definition and Usage

The IF() function returns a value if a condition is TRUE, or another value if a condition is FALSE.

## Syntax

```
  IF(
```
*condition*, *value_if_true*, *value_if_false*)
## Parameter Values

| Parameter | Description | 
|---|---|
| condition | Required. The value to test | 
| value_if_true | Required. The value to return if conditionis TRUE | 
| value_if_false | Required. The value to return if conditionis FALSE | 

## Technical Details

| Works in: | From MySQL 4.0 | 
|---|

Ad

## More Examples

### Example

Return 5 if the condition is TRUE, or 10 if the condition is FALSE:

```
  SELECT IF(500<1000, 5, 10); 
```
[Try it Yourself »](trymysql.asp?filename=trysql_func_mysql_if2)

### Example

Test whether two strings are the same and return "YES" if they are, or "NO" if not:

```
  SELECT IF(STRCMP("hello","bye") = 0, "YES", "NO"); 
```
[Try it Yourself »](trymysql.asp?filename=trysql_func_mysql_if3)

### Example

Return "MORE" if the condition is TRUE, or "LESS" if the condition is FALSE:

```
  SELECT OrderID, Quantity, IF(Quantity>10, "MORE", "LESS")
FROM 
  OrderDetails; 
```
[Try it Yourself »](trymysql.asp?filename=trysql_func_mysql_if4)