# MySQL MICROSECOND() Function

**Source:** [https://www.w3schools.com/sql/func_mysql_microsecond.asp](https://www.w3schools.com/sql/func_mysql_microsecond.asp)

---

# MySQL MICROSECOND() Function

### Example[Get your own SQL Server](/sql/sql_server.asp)

Return the microsecond part of a datetime:

```
  SELECT MICROSECOND("2017-06-20 09:34:00.000023"); 
```
[Try it Yourself »](trymysql.asp?filename=trysql_func_mysql_microsecond)

## Definition and Usage

The MICROSECOND() function returns the microsecond part of a time/datetime (from 0 to 999999).

## Syntax

```
  MICROSECOND(
```
*datetime*)
  
## Parameter Values

| Parameter | Description | 
|---|---|
| datetime | Required. The time or datetime to extract the microsecond from | 

## Technical Details

| Works in: | From MySQL 4.0 | 
|---|

## More Examples

### Example

Return the microsecond part of a time value:

```
  SELECT MICROSECOND("23:59:59.000045"); 
```
[Try it Yourself »](trymysql.asp?filename=trysql_func_mysql_microsecond2)

Ad