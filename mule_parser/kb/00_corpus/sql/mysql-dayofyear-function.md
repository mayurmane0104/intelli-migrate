# MySQL DAYOFYEAR() Function

**Source:** [https://www.w3schools.com/sql/func_mysql_dayofyear.asp](https://www.w3schools.com/sql/func_mysql_dayofyear.asp)

---

# MySQL DAYOFYEAR() Function

### Example[Get your own SQL Server](/sql/sql_server.asp)

Return the day of the year for a date:

```
  SELECT DAYOFYEAR("2017-06-15"); 
```
[Try it Yourself »](trymysql.asp?filename=trysql_func_mysql_dayofyear)

## Definition and Usage

The DAYOFYEAR() function returns the day of the year for a given date (a number from 1 to 366).

## Syntax

```
  DAYOFYEAR(
```
*date*)
  
## Parameter Values

| Parameter | Description | 
|---|---|
| date | Required. The date to return the day of the year from | 

## Technical Details

| Works in: | From MySQL 4.0 | 
|---|

Ad

## More Examples

### Example

Return the day of the year for the current system date:

```
SELECT DAYOFYEAR(CURDATE()); 
```
[Try it Yourself »](trymysql.asp?filename=trysql_func_mysql_dayofyear3)