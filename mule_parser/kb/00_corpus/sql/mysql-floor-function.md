# MySQL FLOOR() Function

**Source:** [https://www.w3schools.com/sql/func_mysql_floor.asp](https://www.w3schools.com/sql/func_mysql_floor.asp)

---

# MySQL FLOOR() Function

### Example[Get your own SQL Server](/sql/sql_server.asp)

Return the largest integer value that is less than or equal to 25.75:

```
  SELECT FLOOR(25.75); 
```
[Try it Yourself »](trymysql.asp?filename=trysql_func_mysql_floor)

## Definition and Usage

The FLOOR() function returns the largest integer value that is smaller than or equal to a number.

**Note:** Also look at the [ROUND()](func_mysql_round.asp), [
CEIL()](func_mysql_ceil.asp), [CEILING()](func_mysql_ceiling.asp), 
[TRUNCATE()](func_mysql_truncate.asp), and
[DIV](func_mysql_div.asp) functions.

## Syntax

```
  FLOOR(
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

Return the largest integer value that is less than or equal to 25:

```
  SELECT FLOOR(25); 
```
[Try it Yourself »](trymysql.asp?filename=trysql_func_mysql_floor2)

Ad