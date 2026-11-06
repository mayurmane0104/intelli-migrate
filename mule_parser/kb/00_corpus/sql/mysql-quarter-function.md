# MySQL QUARTER() Function

**Source:** [https://www.w3schools.com/sql/func_mysql_quarter.asp](https://www.w3schools.com/sql/func_mysql_quarter.asp)

---

# MySQL QUARTER() Function

### Example[Get your own SQL Server](/sql/sql_server.asp)

Return the quarter of the year for the date:

```
  SELECT QUARTER("2017-06-15"); 
```
[Try it Yourself »](trymysql.asp?filename=trysql_func_mysql_quarter)

## Definition and Usage

The QUARTER() function returns the quarter of the year for a given date value (a number from 1 to 4).

- January-March returns 1
- April-June returns 2
- July-Sep returns 3
- Oct-Dec returns 4

## Syntax

```
  QUARTER(
```
*date*)
  
## Parameter Values

| Parameter | Description | 
|---|---|
| date | Required. The date or datetime to extract the quarter from | 

## Technical Details

| Works in: | From MySQL 4.0 | 
|---|

Ad

## More Examples

### Example

Return the quarter of the year for the date:

```
SELECT QUARTER("2017-01-01 09:34:21"); 
```
[Try it Yourself »](trymysql.asp?filename=trysql_func_mysql_quarter2)