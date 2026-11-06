# MySQL WEEKDAY() Function

**Source:** [https://www.w3schools.com/sql/func_mysql_weekday.asp](https://www.w3schools.com/sql/func_mysql_weekday.asp)

---

# MySQL WEEKDAY() Function

### Example[Get your own SQL Server](/sql/sql_server.asp)

Return the weekday number for a date:

```
  SELECT WEEKDAY("2017-06-15"); 
```
[Try it Yourself »](trymysql.asp?filename=trysql_func_mysql_weekday)

## Definition and Usage

The WEEKDAY() function returns the weekday number for a given date.

**Note:** 0 = Monday, 1 = Tuesday, 2 = Wednesday, 3 = Thursday, 
4 = Friday, 5 = Saturday, 6 = Sunday.

## Syntax

```
  WEEKDAY(
```
*date*)
  
## Parameter Values

| Parameter | Description | 
|---|---|
| date | Required. The date or datetime to extract the weekday number from | 

## Technical Details

| Works in: | From MySQL 4.0 | 
|---|

Ad

## More Examples

### Example

Return the weekday number for the current system date:

```
SELECT WEEKDAY(CURDATE()); 
```
[Try it Yourself »](trymysql.asp?filename=trysql_func_mysql_weekday3)