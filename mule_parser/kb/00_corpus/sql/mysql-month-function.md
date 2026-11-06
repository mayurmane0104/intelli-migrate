# MySQL MONTH() Function

**Source:** [https://www.w3schools.com/sql/func_mysql_month.asp](https://www.w3schools.com/sql/func_mysql_month.asp)

---

# MySQL MONTH() Function

### Example[Get your own SQL Server](/sql/sql_server.asp)

Return the month part of a date:

```
  SELECT MONTH("2017-06-15"); 
```
[Try it Yourself »](trymysql.asp?filename=trysql_func_mysql_month)

## Definition and Usage

The MONTH() function returns the month part for a given date (a number from 1 to 12).

## Syntax

```
  MONTH(
```
*date*)
  
## Parameter Values

| Parameter | Description | 
|---|---|
| date | Required. The date or datetime to extract the month from | 

## Technical Details

| Works in: | From MySQL 4.0 | 
|---|

Ad

## More Examples

### Example

Return the month part of the current system date:

```
SELECT MONTH(CURDATE()); 
```
[Try it Yourself »](trymysql.asp?filename=trysql_func_mysql_month3)