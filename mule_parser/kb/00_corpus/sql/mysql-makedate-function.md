# MySQL MAKEDATE() Function

**Source:** [https://www.w3schools.com/sql/func_mysql_makedate.asp](https://www.w3schools.com/sql/func_mysql_makedate.asp)

---

# MySQL MAKEDATE() Function

### Example[Get your own SQL Server](/sql/sql_server.asp)

Create and return a date based on a year and a number of days value:

```
  SELECT MAKEDATE(2017, 3); 
```
[Try it Yourself »](trymysql.asp?filename=trysql_func_mysql_makedate)

## Definition and Usage

The MAKEDATE() function creates and returns a date based on a year and a number of days value.

## Syntax

```
  MAKEDATE(
```
*year*, *day*)
  
## Parameter Values

| Parameter | Description | 
|---|---|
| year | Required. A year (4-digits) | 
| day | Required. A number that indicates the day of the year | 

## Technical Details

| Works in: | From MySQL 4.0 | 
|---|

Ad

## More Examples

### Example

Create and return a date based on a year and a number of days value:

```
  SELECT MAKEDATE(2017, 175); 
```
[Try it Yourself »](trymysql.asp?filename=trysql_func_mysql_makedate2)

### Example

Create and return a date based on a year and a number of days value:

```
  SELECT MAKEDATE(2017, 100); 
```
[Try it Yourself »](trymysql.asp?filename=trysql_func_mysql_makedate3)

### Example

Create and return a date based on a year and a number of days value:

```
  SELECT MAKEDATE(2017, 366); 
```
[Try it Yourself »](trymysql.asp?filename=trysql_func_mysql_makedate4)