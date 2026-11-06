# MySQL CEIL() Function

**Source:** [https://www.w3schools.com/sql/func_mysql_ceil.asp](https://www.w3schools.com/sql/func_mysql_ceil.asp)

---

# MySQL CEIL() Function

### Example[Get your own SQL Server](/sql/sql_server.asp)

Return the smallest integer value that is greater than or equal to 25.75:

```
  SELECT CEIL(25.75); 
```
[Try it Yourself »](trymysql.asp?filename=trysql_func_mysql_ceil)

## Definition and Usage

The CEIL() function returns the smallest integer value that is bigger than or equal to a number.

**Note:** This function is equal to the 
[CEILING()](func_mysql_ceiling.asp) 
function.

## Syntax

```
  CEIL(
```
*number*)
## Parameter Values

| Parameter | Description | 
|---|---|
| number | Required. A numeric value | 

## Technical Details

| Works in: | From MySQL 4.0 | 
|---|

## More Examples

### Example

Return the smallest integer value that is greater than or equal to 25:

```
SELECT CEIL(25); 
```
[Try it Yourself »](trymysql.asp?filename=trysql_func_mysql_ceil2)

Ad