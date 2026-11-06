# MySQL SUBDATE() Function

**Source:** [https://www.w3schools.com/sql/func_mysql_subdate.asp](https://www.w3schools.com/sql/func_mysql_subdate.asp)

---

# MySQL SUBDATE() Function

### Example[Get your own SQL Server](/sql/sql_server.asp)

Subtract 10 days from a date and return the date:

```
  SELECT SUBDATE("2017-06-15", INTERVAL 10 DAY); 
```
[Try it Yourself »](trymysql.asp?filename=trysql_func_mysql_subdate)

## Definition and Usage

The SUBDATE() function subtracts a time/date interval from a date and then returns the date.

## Syntax

```
  SUBDATE(
```
*date*, INTERVAL *value unit*)
OR:

```
  SUBDATE(
```
*date*, *days*)
## Parameter Values

| Parameter | Description | 
|---|---|
| date | Required. The original date | 
| days | Required. The number of days to subtract from date | 
| value | Required. The value of the time/date interval to subtract. Both positive and negative values are allowed | 
| unit | Required. The type of interval. Can be one of the following 
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
SELECT SUBDATE("2017-06-15 09:34:21", INTERVAL 15 MINUTE); 
```
[Try it Yourself »](trymysql.asp?filename=trysql_func_mysql_subdate2)

### Example

Subtract 3 hours from a date and return the date:

```
SELECT SUBDATE("2017-06-15 09:34:21", INTERVAL 3 HOUR); 
```
[Try it Yourself »](trymysql.asp?filename=trysql_func_mysql_subdate3)

### Example

Add 2 months to a date and return the date:

```
SELECT SUBDATE("2017-06-15", INTERVAL -2 MONTH); 
```
[Try it Yourself »](trymysql.asp?filename=trysql_func_mysql_subdate4)