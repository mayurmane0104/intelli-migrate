# MySQL TIME() Function

**Source:** [https://www.w3schools.com/sql/func_mysql_time.asp](https://www.w3schools.com/sql/func_mysql_time.asp)

---

# MySQL TIME() Function

### Example[Get your own SQL Server](/sql/sql_server.asp)

Extract the time part from a time expression:

```
  SELECT TIME("19:30:10"); 
```
[Try it Yourself »](trymysql.asp?filename=trysql_func_mysql_time)

## Definition and Usage

The TIME() function extracts the time part from a given time/datetime.

**Note:** This function returns "00:00:00" if *expression* is not a 
datetime/time, or NULL if *expression* is NULL.

## Syntax

```
  TIME(
```
*expression*)
## Parameter Values

| Parameter | Description | 
|---|---|
| expression | Required. The time/datetime to extract the time from | 

## Technical Details

| Works in: | From MySQL 4.0 | 
|---|

Ad

## More Examples

### Example

Extract the time part from the datetime expression:

```
  SELECT TIME("2017-08-15 19:30:10"); 
```
[Try it Yourself »](trymysql.asp?filename=trysql_func_mysql_time2)

### Example

Extract the time part from the datetime expression:

```
  SELECT TIME("2017-08-15 19:30:10.000001"); 
```
[Try it Yourself »](trymysql.asp?filename=trysql_func_mysql_time3)