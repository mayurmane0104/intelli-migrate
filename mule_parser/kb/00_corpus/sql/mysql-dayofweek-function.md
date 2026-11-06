# MySQL DAYOFWEEK() Function

**Source:** [https://www.w3schools.com/sql/func_mysql_dayofweek.asp](https://www.w3schools.com/sql/func_mysql_dayofweek.asp)

---

# MySQL DAYOFWEEK() Function

### Example[Get your own SQL Server](/sql/sql_server.asp)

Return the weekday index for a date:

```
  SELECT DAYOFWEEK("2017-06-15"); 
```
[Try it Yourself »](trymysql.asp?filename=trysql_func_mysql_dayofweek)

## Definition and Usage

The DAYOFWEEK() function returns the weekday index for a given date (a number from 1 to 7).

**Note:** 1=Sunday, 2=Monday, 3=Tuesday, 4=Wednesday, 
5=Thursday, 6=Friday, 7=Saturday.

## Syntax

```
  DAYOFWEEK(
```
*date*)
  
## Parameter Values

| Parameter | Description | 
|---|---|
| date | Required. The date to return the weekday index from | 

## Technical Details

| Works in: | From MySQL 4.0 | 
|---|

## More Examples

### Example

Return the weekday index for a date:

```
SELECT DAYOFWEEK("2017-06-15 09:34:21"); 
```
[Try it Yourself »](trymysql.asp?filename=trysql_func_mysql_dayofweek2)

### Example

Return the weekday index for the current system date:

```
SELECT DAYOFWEEK(CURDATE()); 
```
[Try it Yourself »](trymysql.asp?filename=trysql_func_mysql_dayofweek3)