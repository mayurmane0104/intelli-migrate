# MySQL ROUND() Function

**Source:** [https://www.w3schools.com/sql/func_mysql_round.asp](https://www.w3schools.com/sql/func_mysql_round.asp)

---

# MySQL ROUND() Function

### Example[Get your own SQL Server](/sql/sql_server.asp)

Round the number to 2 decimal places:

```
  SELECT ROUND(135.375, 2); 
```
[Try it Yourself »](trymysql.asp?filename=trysql_func_mysql_round)

## Definition and Usage

The ROUND() function rounds a number to a specified number of decimal places.

**Note:** See also the [FLOOR()](func_mysql_floor.asp), [
CEIL()](func_mysql_ceil.asp), [CEILING()](func_mysql_ceiling.asp), and 
[TRUNCATE()](func_mysql_truncate.asp) functions.

## Syntax

```
  ROUND(
```
*number*, *decimals*)
## Parameter Values

| Parameter | Description | 
|---|---|
| number | Required. The number to be rounded | 
| decimals | Optional. The number of decimal places to round numberto. If omitted, 
    it returns the integer (no decimals) | 

## Technical Details

| Works in: | From MySQL 4.0 | 
|---|

## More Examples

### Example

Round the Price column (to 1 decimal) in the "Products" table:

```
 SELECT ProductName, Price, ROUND(Price, 1) AS RoundedPrice
FROM Products; 
```
[Try it Yourself »](trysql.asp?filename=trysql_func_mysql_round3)