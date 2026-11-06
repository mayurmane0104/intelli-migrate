# SQL Server MONTH() Function

**Source:** [https://www.w3schools.com/sql/func_sqlserver_month.asp](https://www.w3schools.com/sql/func_sqlserver_month.asp)

---

# SQL Server MONTH() Function

### Example[Get your own SQL Server](/sql/sql_server.asp)

Return the month part of a date:

```
  SELECT MONTH('2017/08/25') AS Month; 
```
[Try it Yourself »](trysqlserver.asp?filename=trysql_func_sqlserver_month)

## Definition and Usage

The MONTH() function returns the month part for a specified date (a number from 1 to 12).

## Syntax

```
  MONTH(
```
*date*)
## Parameter Values

| Parameter | Description | 
|---|---|
| date | Required. The date or datetime to extract the month from | 

## Technical Details

| Return type: | int | 
|---|---|
| Works in: | SQL Server (starting with 2008), Azure SQL Database, Azure SQL Data Warehouse, Parallel Data Warehouse | 

## More Examples

### Example

Return the month part of a date:

```
  SELECT MONTH('2017/05/25 09:08') AS Month; 
```
[Try it Yourself »](trysqlserver.asp?filename=trysql_func_sqlserver_month2)

Ad