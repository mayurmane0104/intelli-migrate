# SQL Server DATEADD() Function

**Source:** [https://www.w3schools.com/sql/func_sqlserver_dateadd.asp](https://www.w3schools.com/sql/func_sqlserver_dateadd.asp)

---

# SQL Server DATEADD() Function

### Example[Get your own SQL Server](/sql/sql_server.asp)

Add one year to a date, then return the date:

```
  SELECT DATEADD(year, 1, '2017/08/25') AS DateAdd; 
```
[Try it Yourself »](trysqlserver.asp?filename=trysql_func_sqlserver_dateadd)

## Definition and Usage

The DATEADD() function adds a time/date interval to a date and then returns the date.

## Syntax

```
  DATEADD(
```
*interval*, *number*, *date*)
## Parameter Values

| Parameter | Description | 
|---|---|
| interval | Required. The time/date interval to add. Can be one of the following values: 
 | 
| number | Required. The number of intervalto add to date. Can be 
    positive (to get dates in the future) or negative (to get dates in the past) | 
| date | Required. The date that will be modified | 

## Technical Details

| Works in: | SQL Server (starting with 2008), Azure SQL Database, Azure SQL Data Warehouse, Parallel Data Warehouse | 
|---|

Ad

## More Examples

### Example

Add two months to a date, then return the date:

```
  SELECT DATEADD(month, 2, '2017/08/25') AS DateAdd; 
```
[Try it Yourself »](trysqlserver.asp?filename=trysql_func_sqlserver_dateadd2)

### Example

Subtract two months from a date, then return the date:

```
  SELECT DATEADD(month, -2, '2017/08/25') AS DateAdd; 
```
[Try it Yourself »](trysqlserver.asp?filename=trysql_func_sqlserver_dateadd3)

### Example

Add 18 years to the date in the BirthDate column, then return the date:

```
  SELECT LastName, 
  BirthDate, DATEADD(year, 18, BirthDate) AS DateAdd FROM Employees; 
```
[Try it Yourself »](trysqlserver.asp?filename=trysql_func_sqlserver_dateadd4)