# SQL Server DATEPART() Function

**Source:** [https://www.w3schools.com/sql/func_sqlserver_datepart.asp](https://www.w3schools.com/sql/func_sqlserver_datepart.asp)

---

# SQL Server DATEPART() Function

### Example[Get your own SQL Server](/sql/sql_server.asp)

Return a specified part of a date:

```
  SELECT DATEPART(year, '2017/08/25') AS DatePartInt; 
```
[Try it Yourself »](trysqlserver.asp?filename=trysql_func_sqlserver_datepart)

## Definition and Usage

The DATEPART() function returns a specified part of a date.

This function returns the result as an integer value.

## Syntax

```
  DATEPART(
```
*interval*, *date*)
## Parameter Values

| Parameter | Description | 
|---|---|
| interval | Required. The part of the dateargument to return. Can be one of the following values:
 | 
| date | Required. The date to use. Can be one of the following data types: date, datetime, datetimeoffset, datetime2, smalldatetime, or time | 

## Technical Details

| Return type: | int | 
|---|---|
| Works in: | SQL Server (starting with 2008), Azure SQL Database, Azure SQL Data Warehouse, Parallel Data Warehouse | 

Ad

## More Examples

### Example

Return a specified part of a date:

```
  SELECT DATEPART(yy, '2017/08/25') AS DatePartInt; 
```
[Try it Yourself »](trysqlserver.asp?filename=trysql_func_sqlserver_datepart2)

### Example

Return a specified part of a date:

```
  SELECT DATEPART(month, '2017/08/25') AS DatePartInt; 
```
[Try it Yourself »](trysqlserver.asp?filename=trysql_func_sqlserver_datepart3)

### Example

Return a specified part of a date:

```
  SELECT DATEPART(hour, '2017/08/25 08:36') AS DatePartInt; 
```
[Try it Yourself »](trysqlserver.asp?filename=trysql_func_sqlserver_datepart4)

### Example

Return a specified part of a date:

```
  SELECT DATEPART(minute, '2017/08/25 08:36') AS DatePartInt; 
```
[Try it Yourself »](trysqlserver.asp?filename=trysql_func_sqlserver_datepart5)