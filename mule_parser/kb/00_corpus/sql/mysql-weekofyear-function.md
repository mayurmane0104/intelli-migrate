# MySQL WEEKOFYEAR() Function

**Source:** [https://www.w3schools.com/sql/func_mysql_weekofyear.asp](https://www.w3schools.com/sql/func_mysql_weekofyear.asp)

---

# MySQL WEEKOFYEAR() Function

### Example[Get your own SQL Server](/sql/sql_server.asp)

Return the week number for a date:

```
  SELECT WEEKOFYEAR("2017-06-15"); 
```
[Try it Yourself »](trymysql.asp?filename=trysql_func_mysql_weekofyear)

## Definition and Usage

The WEEKOFYEAR() function returns the week number for a given date (a number from 1 to 53).

**Note:** This function assumes that the first day 
of the week is Monday and the first week of the year has more than 3 days.

**Tip:** Also look at the [WEEK()](func_mysql_week.asp) 
function.

## Syntax

```
  WEEKOFYEAR(
```
*date*)
  
## Parameter Values

| Parameter | Description | 
|---|---|
| date | Required. The date or datetime to extract the week number from | 

## Technical Details

| Works in: | From MySQL 4.0 | 
|---|

## More Examples

### Example

Return the week number for the current system date:

```
SELECT WEEKOFYEAR(CURDATE()); 
```
[Try it Yourself »](trymysql.asp?filename=trysql_func_mysql_weekofyear3)