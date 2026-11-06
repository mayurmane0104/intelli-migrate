# MySQL TO_DAYS() Function

**Source:** [https://www.w3schools.com/sql/func_mysql_to_days.asp](https://www.w3schools.com/sql/func_mysql_to_days.asp)

---

# MySQL TO_DAYS() Function

### Example[Get your own SQL Server](/sql/sql_server.asp)

Return the number of days between the date and year 0:

```
  SELECT TO_DAYS("2017-06-20"); 
```
[Try it Yourself »](trymysql.asp?filename=trysql_func_mysql_to_days)

## Definition and Usage

The TO_DAYS() function returns the number of days between a date and year 0 (date "0000-00-00").

The TO_DAYS() function can be used only with dates within the Gregorian calendar.

**Note:** This function is the opposite of the 
[FROM_DAYS()](func_mysql_from_days.asp) function.

## Syntax

```
  TO_DAYS(
```
*date*)
  
## Parameter Values

| Parameter | Description | 
|---|---|
| date | Required. The given date | 

## Technical Details

| Works in: | From MySQL 4.0 | 
|---|

## More Examples

### Example

Return the number of days between the date and year 0:

```
  SELECT TO_DAYS("2017-06-20 09:34:00"); 
```
[Try it Yourself »](trymysql.asp?filename=trysql_func_mysql_to_days2)

Ad