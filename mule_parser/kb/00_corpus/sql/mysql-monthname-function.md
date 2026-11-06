# MySQL MONTHNAME() Function

**Source:** [https://www.w3schools.com/sql/func_mysql_monthname.asp](https://www.w3schools.com/sql/func_mysql_monthname.asp)

---

# MySQL MONTHNAME() Function

### Example[Get your own SQL Server](/sql/sql_server.asp)

Return the name of the month for a date:

```
  SELECT MONTHNAME("2017-06-15"); 
```
[Try it Yourself »](trymysql.asp?filename=trysql_func_mysql_monthname)

## Definition and Usage

The MONTHNAME() function returns the name of the month for a given date.

## Syntax

```
  MONTHNAME(
```
*date*)
  
## Parameter Values

| Parameter | Description | 
|---|---|
| date | Required. The date or datetime value to extract the month name from | 

## Technical Details

| Works in: | From MySQL 4.0 | 
|---|

Ad

## More Examples

### Example

Return the name of the month for a date:

```
SELECT MONTHNAME("2017-06-15 09:34:21"); 
```
[Try it Yourself »](trymysql.asp?filename=trysql_func_mysql_monthname2)

### Example

Return the name of the month for the current system date:

```
SELECT MONTHNAME(CURDATE()); 
```
[Try it Yourself »](trymysql.asp?filename=trysql_func_mysql_monthname3)