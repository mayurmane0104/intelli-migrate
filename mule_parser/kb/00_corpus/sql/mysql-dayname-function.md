# MySQL DAYNAME() Function

**Source:** [https://www.w3schools.com/sql/func_mysql_dayname.asp](https://www.w3schools.com/sql/func_mysql_dayname.asp)

---

# MySQL DAYNAME() Function

### Example[Get your own SQL Server](/sql/sql_server.asp)

Return the weekday name for a date:

```
  SELECT DAYNAME("2017-06-15"); 
```
[Try it Yourself »](trymysql.asp?filename=trysql_func_mysql_dayname)

## Definition and Usage

The DAYNAME() function returns the weekday name for a given date.

## Syntax

```
  DAYNAME(
```
*date*)
  
## Parameter Values

| Parameter | Description | 
|---|---|
| date | Required. The date to extract the weekday name from | 

## Technical Details

| Works in: | From MySQL 4.0 | 
|---|

Ad

## More Examples

### Example

Return the weekday name for a date:

```
SELECT DAYNAME("2017-06-15 09:34:21"); 
```
[Try it Yourself »](trymysql.asp?filename=trysql_func_mysql_dayname2)

### Example

Return the weekday name for the current system date:

```
SELECT DAYNAME(CURDATE()); 
```
[Try it Yourself »](trymysql.asp?filename=trysql_func_mysql_dayname3)