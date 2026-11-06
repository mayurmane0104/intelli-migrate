# MySQL DAYOFMONTH() Function

**Source:** [https://www.w3schools.com/sql/func_mysql_dayofmonth.asp](https://www.w3schools.com/sql/func_mysql_dayofmonth.asp)

---

# MySQL DAYOFMONTH() Function

### Example[Get your own SQL Server](/sql/sql_server.asp)

Return the day of the month for a date:

```
  SELECT DAYOFMONTH("2017-06-15"); 
```
[Try it Yourself »](trymysql.asp?filename=trysql_func_mysql_dayofmonth)

## Definition and Usage

The DAYOFMONTH() function returns the day of the month for a given date (a number from 1 to 31).

**Note:** This function equals the [DAY()](func_mysql_day.asp) function.

## Syntax

```
  DAYOFMONTH(
```
*date*)
  
## Parameter Values

| Parameter | Description | 
|---|---|
| date | Required. The date to extract the day from | 

## Technical Details

| Works in: | From MySQL 4.0 | 
|---|

Ad

## More Examples

### Example

Return the day of the month for a date:

```
SELECT DAYOFMONTH("2017-06-15 09:34:21"); 
```
[Try it Yourself »](trymysql.asp?filename=trysql_func_mysql_dayofmonth2)

### Example

Return the day of the month for the current system date:

```
SELECT DAYOFMONTH(CURDATE()); 
```
[Try it Yourself »](trymysql.asp?filename=trysql_func_mysql_dayofmonth3)