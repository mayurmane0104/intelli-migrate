# MySQL DATE_SUB() Function

**Source:** [https://www.w3schools.com/sql/func_mysql_date_sub.asp](https://www.w3schools.com/sql/func_mysql_date_sub.asp)

---

# MySQL DATE_SUB() Function

### Example[Get your own SQL Server](/sql/sql_server.asp)

Subtract 10 days from a date and return the date:

```
  SELECT DATE_SUB("2017-06-15", INTERVAL 10 DAY); 
```
[Try it Yourself »](trymysql.asp?filename=trysql_func_mysql_date_sub)

## Definition and Usage

The DATE_SUB() function subtracts a time/date interval from a date and then returns the date.

## Syntax

```
  DATE_SUB(
```
*date*, INTERVAL *value interval*)
  
## Parameter Values

| Parameter | Description | 
|---|---|
| date | Required. The date to be modified | 
| value | Required. The value of the time/date interval to subtract. Both positive and negative values are allowed | 
| interval | Required. The type of interval to subtract. Can be one of the following 
    values: 
 | 

Ad

## Technical Details

| Works in: | From MySQL 4.0 | 
|---|

## More Examples

### Example

Subtract 15 minutes from a date and return the date:

```
SELECT DATE_SUB("2017-06-15 09:34:21", INTERVAL 15 MINUTE); 
```
[Try it Yourself »](trymysql.asp?filename=trysql_func_mysql_date_sub2)

### Example

Subtract 3 hours from a date and return the date:

```
SELECT DATE_SUB("2017-06-15 09:34:21", INTERVAL 3 HOUR); 
```
[Try it Yourself »](trymysql.asp?filename=trysql_func_mysql_date_sub3)

### Example

Add 2 months to a date and return the date:

```
SELECT DATE_SUB("2017-06-15", INTERVAL -2 MONTH); 
```
[Try it Yourself »](trymysql.asp?filename=trysql_func_mysql_date_sub4)