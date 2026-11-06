# SQL Server DATEDIFF() Function

**Source:** [https://www.w3schools.com/sql/func_sqlserver_datediff.asp](https://www.w3schools.com/sql/func_sqlserver_datediff.asp)

---

# SQL Server DATEDIFF() Function

### Example[Get your own SQL Server](/sql/sql_server.asp)

Return the difference between two date values, in years:

```
  SELECT DATEDIFF(year, '2017/08/25', '2011/08/25') AS DateDiff; 
```
[Try it Yourself »](trysqlserver.asp?filename=trysql_func_sqlserver_datediff)

## Definition and Usage

The DATEDIFF() function returns the difference between two dates, as an integer.

## Syntax

```
  DATEDIFF(
```
*interval*, *date1*, *date2*)
## Parameter Values

| Parameter | Description | 
|---|---|
| interval | Required. The part to return. Can be one of the following values: 
 | 
| date1, date2 | Required. The two dates to calculate the difference between | 

## Technical Details

| Return type: | int | 
|---|---|
| Works in: | SQL Server (starting with 2008), Azure SQL Database, Azure SQL Data Warehouse, Parallel Data Warehouse | 

Ad

## More Examples

### Example

Return the difference between two date values, in months:

```
  SELECT DATEDIFF(month, '2017/08/25', 
  '2011/08/25') AS DateDiff; 
```
[Try it Yourself »](trysqlserver.asp?filename=trysql_func_sqlserver_datediff2)

### Example

Return the difference between two date values, in hours:

```
  SELECT DATEDIFF(hour, '2017/08/25 07:00', '2017/08/25 12:45') AS DateDiff; 
```
[Try it Yourself »](trysqlserver.asp?filename=trysql_func_sqlserver_datediff3)