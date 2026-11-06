# MySQL FORMAT() Function

**Source:** [https://www.w3schools.com/sql/func_mysql_format.asp](https://www.w3schools.com/sql/func_mysql_format.asp)

---

# MySQL FORMAT() Function

### Example[Get your own SQL Server](/sql/sql_server.asp)

Format the number as "#,###,###.##" (and round with two decimal places):

```
  SELECT FORMAT(250500.5634, 2); 
```
[Try it Yourself »](trymysql.asp?filename=trysql_func_mysql_format)

## Definition and Usage

The FORMAT() function formats a number to a format like "#,###,###.##", rounded to a specified number of decimal places, then it returns the result as a string.

## Syntax

```
  FORMAT(
```
*number*, *decimal_places*)
## Parameter Values

| Parameter | Description | 
|---|---|
| number | Required. The number to be formatted | 
| decimal_places | Required. The number of decimal places for number.If this 
    parameter is 0, this function returns a string 
  with no decimal places | 

## Technical Details

| Works in: | From MySQL 4.0 | 
|---|

## More Examples

### Example

Format the number as a format of "#,###,###.##" (and round with 0 decimal places):

```
  SELECT FORMAT(250500.5634, 0); 
```
[Try it Yourself »](trymysql.asp?filename=trysql_func_mysql_format2)

Ad