# SQL Server FORMAT() Function

**Source:** [https://www.w3schools.com/sql/func_sqlserver_format.asp](https://www.w3schools.com/sql/func_sqlserver_format.asp)

---

# SQL Server FORMAT() Function

### Example[Get your own SQL Server](/sql/sql_server.asp)

Format a date:

```
  DECLARE @d DATETIME = '12/01/2018'; 
SELECT FORMAT (@d, 'd', 'en-US') AS 
  'US English Result',
               
  FORMAT (@d, 'd', 'no') AS 'Norwegian Result',
               
  FORMAT (@d, 'd', 'zu') AS 'Zulu Result'; 
```
[Try it Yourself »](trysqlserver.asp?filename=trysql_func_sqlserver_format)

## Definition and Usage

The FORMAT() function formats a value with the specified format (and an optional culture in SQL Server 2017).

Use the FORMAT() function to format date/time values and number 
values. For general data type conversions, use
[CAST()](func_sqlserver_cast.asp) or
[CONVERT()](func_sqlserver_convert.asp).

## Syntax

```
  FORMAT(
```
*value, format*, *
  culture*)
## Parameter Values

| Parameter | Description | 
|---|---|
| value | Required. The value to be formatted | 
| format | Required. The format pattern | 
| culture | Optional. Specifies a culture (from SQL Server 2017) | 

## Technical Details

| Works in: | SQL Server (starting with 2012), Azure SQL Database | 
|---|

## More Examples

Ad