# MySQL TIMEDIFF() Function

**Source:** [https://www.w3schools.com/sql/func_mysql_timediff.asp](https://www.w3schools.com/sql/func_mysql_timediff.asp)

---

# MySQL TIMEDIFF() Function

### Example[Get your own SQL Server](/sql/sql_server.asp)

Return the difference between two time expressions:

```
  SELECT TIMEDIFF("13:10:11", "13:10:10"); 
```
[Try it Yourself »](trymysql.asp?filename=trysql_func_mysql_timediff)

## Definition and Usage

The TIMEDIFF() function returns the difference between two time/datetime expressions.

**Note:** *time1* and *time2* should be in the 
same format, and the calculation is *time1* - *time2*.

## Syntax

```
  TIMEDIFF(
```
*time1*, *time2*)
  
## Parameter Values

| Parameter | Description | 
|---|---|
| time1 | Required. A time value | 
| time2 | Required. Another time value | 

## Technical Details

| Works in: | From MySQL 4.0 | 
|---|

## More Examples

### Example

Return the difference between two datetime expressions:

```
  SELECT TIMEDIFF("2017-06-25 13:10:11", "2017-06-15 13:10:10"); 
```
[Try it Yourself »](trymysql.asp?filename=trysql_func_mysql_timediff2)

Ad