# MySQL YEARWEEK() Function

**Source:** [https://www.w3schools.com/sql/func_mysql_yearweek.asp](https://www.w3schools.com/sql/func_mysql_yearweek.asp)

---

# MySQL YEARWEEK() Function

### Example[Get your own SQL Server](/sql/sql_server.asp)

Return the year and week number for a date:

```
  SELECT YEARWEEK("2017-06-15"); 
```
[Try it Yourself »](trymysql.asp?filename=trysql_func_mysql_yearweek)

## Definition and Usage

The YEARWEEK() function returns the year and week number (a number from 0 to 53) for a given date.

## Syntax

```
  YEARWEEK(
```
*date*, *firstdayofweek*)
  
## Parameter Values

| Parameter | Description | 
|---|---|
| date | Required. The date or datetime value to extract the year and week number from | 
| firstdayofweek | Optional. Specifies what day the week starts on. Can be one of the following: 
 | 

## Technical Details

| Works in: | From MySQL 4.0 | 
|---|

Ad

## More Examples

### Example

Return the year and week number for a date:

```
  SELECT YEARWEEK("2017-10-25"); 
```
[Try it Yourself »](trymysql.asp?filename=trysql_func_mysql_yearweek2)

### Example

Return the year and week number for the current system date:

```
SELECT YEARWEEK(CURDATE()); 
```
[Try it Yourself »](trymysql.asp?filename=trysql_func_mysql_yearweek3)