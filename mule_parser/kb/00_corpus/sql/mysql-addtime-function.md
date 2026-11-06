# MySQL ADDTIME() Function

**Source:** [https://www.w3schools.com/sql/func_mysql_addtime.asp](https://www.w3schools.com/sql/func_mysql_addtime.asp)

---

# MySQL ADDTIME() Function

### Example[Get your own SQL Server](/sql/sql_server.asp)

Add 2 seconds to a time and return the datetime:

```
  SELECT ADDTIME("2017-06-15 
  09:34:21", "2"); 
```
[Try it Yourself »](trymysql.asp?filename=trysql_func_mysql_addtime)

## Definition and Usage

The ADDTIME() function adds a time interval to a time/datetime and then returns the time/datetime.

## Syntax

```
ADDTIME(
```
*datetime*, *addtime*)
## Parameter Values

| Parameter | Description | 
|---|---|
| datetime | Required. The time/datetime to be modified | 
| addtime | Required. The time interval to add to datetime. Both 
    positive and negative values are allowed | 

## Technical Details

| Works in: | From MySQL 4.0 | 
|---|

Ad

## More Examples

### Example

Add 5 seconds and 3 microseconds to a time and return the datetime:

```
  SELECT ADDTIME("2017-06-15 
  09:34:21.000001", "5.000003"); 
```
[Try it Yourself »](trymysql.asp?filename=trysql_func_mysql_addtime2)

### Example

Add 2 hours, 10 minutes, 5 seconds, and 3 microseconds to a time and return the datetime:

```
  SELECT ADDTIME("2017-06-15 09:34:21.000001", "2:10:5.000003"); 
```
[Try it Yourself »](trymysql.asp?filename=trysql_func_mysql_addtime3)

### Example

Add 5 days, 2 hours, 10 minutes, 5 seconds, and 3 microseconds to a time and return the datetime:

```
  SELECT ADDTIME("2017-06-15 
  09:34:21.000001", "5 2:10:5.000003"); 
```
[Try it Yourself »](trymysql.asp?filename=trysql_func_mysql_addtime4)

### Example

Add 2 hours, 10 minutes, 5 seconds, and 3 microseconds to a time and return the time:

```
  SELECT ADDTIME("09:34:21.000001", "2:10:5.000003"); 
```
[Try it Yourself »](trymysql.asp?filename=trysql_func_mysql_addtime5)