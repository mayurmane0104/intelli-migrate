# MySQL ADDDATE() Function

**Source:** [https://www.w3schools.com/sql/func_mysql_adddate.asp](https://www.w3schools.com/sql/func_mysql_adddate.asp)

---

# MySQL ADDDATE() Function

### Example[Get your own SQL Server](/sql/sql_server.asp)

Add 10 days to a date and return the date:

```
  SELECT ADDDATE("2017-06-15", INTERVAL 10 DAY); 
```
[Try it Yourself »](trymysql.asp?filename=trysql_func_mysql_adddate)

## Definition and Usage

The ADDDATE() function adds a time/date interval to a date and then returns the date.

## Syntax

```
  ADDDATE(
```
*date*, INTERVAL *value addunit*)
**OR:**

```
  ADDDATE(
```
*date*, *days*)
## Parameter Values

| Parameter | Description | 
|---|---|
| date | Required. The date to be modified | 
| days | Required. The number of days to add to date | 
| value | Required. The value of the time/date interval to add. Both positive and negative values are allowed | 
| addunit | Required. The type of interval to add. Can be one of the following 
    values: 
 | 

Ad

## Technical Details

| Works in: | From MySQL 4.0 | 
|---|

## More Examples

### Example

Add 15 minutes to a date and return the date:

```
SELECT ADDDATE("2017-06-15 09:34:21", INTERVAL 15 MINUTE); 
```
[Try it Yourself »](trymysql.asp?filename=trysql_func_mysql_adddate2)

### Example

Subtract 3 hours to a date and return the date:

```
SELECT ADDDATE("2017-06-15 09:34:21", INTERVAL -3 HOUR); 
```
[Try it Yourself »](trymysql.asp?filename=trysql_func_mysql_adddate3)

### Example

Subtract 2 months to a date and return the date:

```
SELECT ADDDATE("2017-06-15", INTERVAL -2 MONTH); 
```
[Try it Yourself »](trymysql.asp?filename=trysql_func_mysql_adddate4)