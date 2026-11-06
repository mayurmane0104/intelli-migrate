# SQL Server DATEFROMPARTS() Function

**Source:** [https://www.w3schools.com/sql/func_sqlserver_datefromparts.asp](https://www.w3schools.com/sql/func_sqlserver_datefromparts.asp)

---

# SQL Server DATEFROMPARTS() Function

### Example[Get your own SQL Server](/sql/sql_server.asp)

Return a date from its parts:

```
  SELECT DATEFROMPARTS(2018, 10, 31) AS DateFromParts; 
```
[Try it Yourself »](trysqlserver.asp?filename=trysql_func_sqlserver_datefromparts)

## Definition and Usage

The DATEFROMPARTS() function returns a date from the specified parts (year, month, and day values).

## Syntax

```
  DATEFROMPARTS(
```
*year*, *month*, *day*)
## Parameter Values

| Parameter | Description | 
|---|---|
| year | Required. Specifies a year (4 digits) | 
| month | Required. Specifies a month (from 1 to 12) | 
| day | Required. Specifies a day (from 1 to 31) | 

## Technical Details

| Return type: | date | 
|---|---|
| Works in: | SQL Server (starting with 2012), Azure SQL Database, Azure SQL Data Warehouse, Parallel Data Warehouse | 

Ad