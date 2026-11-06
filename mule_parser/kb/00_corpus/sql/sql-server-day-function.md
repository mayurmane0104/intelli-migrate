# SQL Server DAY() Function

**Source:** [https://www.w3schools.com/sql/func_sqlserver_day.asp](https://www.w3schools.com/sql/func_sqlserver_day.asp)

---

# SQL Server DAY() Function

### Example[Get your own SQL Server](/sql/sql_server.asp)

Return the day of the month for a date:

```
  SELECT DAY('2017/08/25') AS DayOfMonth; 
```
[Try it Yourself »](trysqlserver.asp?filename=trysql_func_sqlserver_day)

## Definition and Usage

The DAY() function returns the day of the month (from 1 to 31) for a specified date.

## Syntax

```
  DAY(
```
*date*)
## Parameter Values

| Parameter | Description | 
|---|---|
| date | Required. The date to return the day of the month from | 

## Technical Details

| Return type: | int | 
|---|---|
| Works in: | SQL Server (starting with 2008), Azure SQL Database, Azure SQL Data Warehouse, Parallel Data Warehouse | 

## More Examples

### Example

Return the day of the month for a date:

```
  SELECT DAY('2017/08/13 09:08') AS DayOfMonth; 
```
[Try it Yourself »](trysqlserver.asp?filename=trysql_func_sqlserver_day2)

Ad