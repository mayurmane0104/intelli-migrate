# SQL Server YEAR() Function

**Source:** [https://www.w3schools.com/sql/func_sqlserver_year.asp](https://www.w3schools.com/sql/func_sqlserver_year.asp)

---

# SQL Server YEAR() Function

### Example[Get your own SQL Server](/sql/sql_server.asp)

Return the year part of a date:

```
  SELECT YEAR('2017/08/25') AS Year; 
```
[Try it Yourself »](trysqlserver.asp?filename=trysql_func_sqlserver_year)

## Definition and Usage

The YEAR() function returns the year part for a specified date.

## Syntax

```
  YEAR(
```
*date*)
## Parameter Values

| Parameter | Description | 
|---|---|
| date | Required. The date or datetime to extract the year from | 

## Technical Details

| Return type: | int | 
|---|---|
| Works in: | SQL Server (starting with 2008), Azure SQL Database, Azure SQL Data Warehouse, Parallel Data Warehouse | 

## More Examples

Ad