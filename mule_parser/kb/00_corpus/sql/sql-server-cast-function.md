# SQL Server CAST() Function

**Source:** [https://www.w3schools.com/sql/func_sqlserver_cast.asp](https://www.w3schools.com/sql/func_sqlserver_cast.asp)

---

# SQL Server CAST() Function

### Example[Get your own SQL Server](/sql/sql_server.asp)

Convert a value to an int datatype:

```
SELECT CAST(25.65 AS int); 
```
[Try it Yourself »](trysqlserver.asp?filename=trysql_func_sqlserver_cast)

## Definition and Usage

The CAST() function converts a value (of any type) into a specified datatype.

**Tip:** Also look at the [
CONVERT()](func_sqlserver_convert.asp) function.

## Syntax

```
CAST(
```
*expression* 
  AS *datatype(length)*)
## Parameter Values

| Value | Description | 
|---|---|
| expression | Required. The value to convert | 
| datatype | Required. The datatype to convert expressionto. Can be one of 
    the following: bigint, int, smallint, tinyint, bit, decimal, numeric, money, 
    smallmoney, float, real, datetime, smalldatetime, char, varchar, text, nchar, 
    nvarchar, ntext, binary, varbinary, or image | 
| (length) | Optional. The length of the resulting data type (for char, varchar, nchar, nvarchar, binary and varbinary) | 

## Technical Details

| Works in: | SQL Server (starting with 2008), Azure SQL Database, Azure SQL Data Warehouse, Parallel Data Warehouse | 
|---|

Ad

## More Examples

### Example

Convert a value to a datetime datatype:

```
SELECT CAST('2017-08-25' AS datetime); 
```
[Try it Yourself »](trysqlserver.asp?filename=trysql_func_sqlserver_cast3)