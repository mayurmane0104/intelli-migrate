# MySQL DATEDIFF() Function

**Source:** [https://www.w3schools.com/sql/func_mysql_datediff.asp](https://www.w3schools.com/sql/func_mysql_datediff.asp)

---

# MySQL DATEDIFF() Function

### Example[Get your own SQL Server](/sql/sql_server.asp)

Return the number of days between two date values:

```
  SELECT DATEDIFF("2017-06-25", "2017-06-15"); 
```
[Try it Yourself »](trymysql.asp?filename=trysql_func_mysql_datediff)

## Definition and Usage

The DATEDIFF() function returns the number of days between two date values.

## Syntax

```
  DATEDIFF(
```
*date1*, *date2*)
  
## Parameter Values

| Parameter | Description | 
|---|---|
| date1, date2 | Required. Two dates to calculate the number of days between. (date1 - date2) | 

## Technical Details

| Works in: | From MySQL 4.0 | 
|---|

Ad

## More Examples

### Example

Return the number of days between two date values:

```
  SELECT DATEDIFF("2017-06-25 09:34:21", "2017-06-15 15:25:35"); 
```
[Try it Yourself »](trymysql.asp?filename=trysql_func_mysql_datediff2)

### Example

Return the number of days between two date values:

```
  SELECT DATEDIFF("2017-01-01", 
  "2016-12-24"); 
```
[Try it Yourself »](trymysql.asp?filename=trysql_func_mysql_datediff3)