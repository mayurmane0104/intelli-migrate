# MySQL CEILING() Function

**Source:** [https://www.w3schools.com/sql/func_mysql_ceiling.asp](https://www.w3schools.com/sql/func_mysql_ceiling.asp)

---

# MySQL CEILING() Function

### Example[Get your own SQL Server](/sql/sql_server.asp)

Return the smallest integer value that is greater than or equal to 25.75:

```
  SELECT CEILING(25.75); 
```
[Try it Yourself »](trymysql.asp?filename=trysql_func_mysql_ceiling)

## Definition and Usage

The CEILING() function returns the smallest integer value that is bigger than or equal to a number.

**Note:** This function is equal to the [CEIL()](func_mysql_ceil.asp) function.

## Syntax

```
  CEILING(
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
SELECT CEILING(25); 
```
[Try it Yourself »](trymysql.asp?filename=trysql_func_mysql_ceiling2)

Ad