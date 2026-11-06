# SQL Server DATENAME() Function

**Source:** [https://www.w3schools.com/sql/func_sqlserver_datename.asp](https://www.w3schools.com/sql/func_sqlserver_datename.asp)

---

# SQL Server DATENAME() Function

### Example[Get your own SQL Server](/sql/sql_server.asp)

Return a specified part of a date:

```
  SELECT DATENAME(year, '2017/08/25') AS DatePartString; 
```
[Try it Yourself »](trysqlserver.asp?filename=trysql_func_sqlserver_datename)

## Definition and Usage

The DATENAME() function returns a specified part of a date.

This function returns the result as a string value.

## Syntax

```
  DATENAME(
```
*interval*, *date*)
## Parameter Values

| Parameter | Description | 
|---|---|
| interval | Required. The part to return. Can be one of the following values: 
 | 
| date | Required. The date to use | 

## Technical Details

| Return type: | nvarchar | 
|---|---|
| Works in: | SQL Server (starting with 2008), Azure SQL Database, Azure SQL Data Warehouse, Parallel Data Warehouse | 

Ad

## More Examples

### Example

Return a specified part of a date:

```
  SELECT DATENAME(yy, '2017/08/25') AS DatePartString; 
```
[Try it Yourself »](trysqlserver.asp?filename=trysql_func_sqlserver_datename2)

### Example

Return a specified part of a date:

```
  SELECT DATENAME(month, '2017/08/25') AS DatePartString; 
```
[Try it Yourself »](trysqlserver.asp?filename=trysql_func_sqlserver_datename3)

### Example

Return a specified part of a date:

```
  SELECT DATENAME(hour, '2017/08/25 08:36') AS DatePartString; 
```
[Try it Yourself »](trysqlserver.asp?filename=trysql_func_sqlserver_datename4)

### Example

Return a specified part of a date:

```
  SELECT DATENAME(minute, '2017/08/25 08:36') AS DatePartString; 
```
[Try it Yourself »](trysqlserver.asp?filename=trysql_func_sqlserver_datename5)