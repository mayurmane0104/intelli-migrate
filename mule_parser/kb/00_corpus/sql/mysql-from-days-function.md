# MySQL FROM_DAYS() Function

**Source:** [https://www.w3schools.com/sql/func_mysql_from_days.asp](https://www.w3schools.com/sql/func_mysql_from_days.asp)

---

# MySQL FROM_DAYS() Function

### Example[Get your own SQL Server](/sql/sql_server.asp)

Return a date from a numeric representation of the day:

```
  SELECT FROM_DAYS(685467); 
```
[Try it Yourself »](trymysql.asp?filename=trysql_func_mysql_from_days)

## Definition and Usage

The FROM_DAYS() function returns a date from a numeric datevalue.

The FROM_DAYS() function is to be used only with dates within the Gregorian calendar.

**Note:** This function is the opposite of the
[TO_DAYS()](func_mysql_to_days.asp) function.

## Syntax

```
  FROM_DAYS(
```
*number*)
  
## Parameter Values

| Parameter | Description | 
|---|---|
| number | Required. The numeric day to convert to a date | 

## Technical Details

| Works in: | From MySQL 4.0 | 
|---|

## More Examples

### Example

Return a date from a numeric representation of the day:

```
  SELECT FROM_DAYS(780500); 
```
[Try it Yourself »](trymysql.asp?filename=trysql_func_mysql_from_days2)

Ad