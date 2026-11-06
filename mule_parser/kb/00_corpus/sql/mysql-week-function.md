# MySQL WEEK() Function

**Source:** [https://www.w3schools.com/sql/func_mysql_week.asp](https://www.w3schools.com/sql/func_mysql_week.asp)

---

# MySQL WEEK() Function

### Example[Get your own SQL Server](/sql/sql_server.asp)

Return the week number for a date:

```
  SELECT WEEK("2017-06-15"); 
```
[Try it Yourself »](trymysql.asp?filename=trysql_func_mysql_week)

## Definition and Usage

The WEEK() function returns the week number for a given date (a number from 0 to 53).

## Syntax

```
  WEEK(
```
*date*, *firstdayofweek*)
  
## Parameter Values

| Parameter | Description | 
|---|---|
| date | Required. The date or datetime to extract the week number form | 
| firstdayofweek | Optional. Specifies what day the week starts on. Can be one of the following: 
 | 

## Technical Details

| Works in: | From MySQL 4.0 | 
|---|

Ad

## More Examples

### Example

Return the week number for the current system date:

```
SELECT WEEK(CURDATE()); 
```
[Try it Yourself »](trymysql.asp?filename=trysql_func_mysql_week3)