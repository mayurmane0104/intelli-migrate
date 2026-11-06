# MySQL LAST_DAY() Function

**Source:** [https://www.w3schools.com/sql/func_mysql_last_day.asp](https://www.w3schools.com/sql/func_mysql_last_day.asp)

---

# MySQL LAST_DAY() Function

### Example[Get your own SQL Server](/sql/sql_server.asp)

Extract the last day of the month for the given date:

```
  SELECT LAST_DAY("2017-06-20"); 
```
[Try it Yourself »](trymysql.asp?filename=trysql_func_mysql_last_day)

## Definition and Usage

The LAST_DAY() function extracts the last day of the month for a given date.

## Syntax

```
  LAST_DAY(
```
*date*)
  
## Parameter Values

| Parameter | Description | 
|---|---|
| date | Required. The date to extract the last day of the month from | 

## Technical Details

| Works in: | From MySQL 4.0 | 
|---|

## More Examples

### Example

Extract the last day of the month for the given date:

```
  SELECT LAST_DAY("2017-02-10 09:34:00"); 
```
[Try it Yourself »](trymysql.asp?filename=trysql_func_mysql_last_day2)

Ad