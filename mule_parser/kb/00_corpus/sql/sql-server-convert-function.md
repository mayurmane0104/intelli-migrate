# SQL Server CONVERT() Function

**Source:** [https://www.w3schools.com/sql/func_sqlserver_convert.asp](https://www.w3schools.com/sql/func_sqlserver_convert.asp)

---

# SQL Server CONVERT() Function

### Example[Get your own SQL Server](/sql/sql_server.asp)

Convert an expression to int:

```
SELECT CONVERT(int, 25.65); 
```
[Try it Yourself »](trysqlserver.asp?filename=trysql_func_sqlserver_convert)

## Definition and Usage

The CONVERT() function converts a value (of any type) into a specified datatype.

**Tip:** Also look at the [CAST()](func_sqlserver_cast.asp) 
function.

## Syntax

```
CONVERT(
```
*data_type(length)**,** expression**,** style*)
## Parameter Values

| Value | Description | ||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| data_type | Required. The datatype to convert expressionto. Can be one of 
    the following: bigint, int, smallint, tinyint, bit, decimal, numeric, money, 
    smallmoney, float, real, datetime, smalldatetime, char, varchar, text, nchar, 
    nvarchar, ntext, binary, varbinary, or image | ||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
| (length) | Optional. The length of the resulting data type (for char, varchar, nchar, nvarchar, binary and varbinary) | ||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
| expression | Required. The value to convert to another data type | ||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
| style | Optional. The format used to convert between data types, such as a date 
    or string format. Can be one of the following values: Converting datetime to character: 
 
 
 | 

## Technical Details

| Works in: | SQL Server (starting with 2008), Azure SQL Database, Azure SQL Data Warehouse, Parallel Data Warehouse | 
|---|

## More Examples

### Example

Convert an expression from one data type to another (varchar):

```
SELECT CONVERT(varchar, 25.65); 
```
[Try it Yourself »](trysqlserver.asp?filename=trysql_func_sqlserver_convert2)

### Example

Convert an expression from one data type to another (datetime):

```
SELECT CONVERT(datetime, '2017-08-25'); 
```
[Try it Yourself »](trysqlserver.asp?filename=trysql_func_sqlserver_convert3)

### Example

Convert an expression from one data type to another (varchar):

```
SELECT CONVERT(varchar, 
  '2017-08-25', 101); 
```
[Try it Yourself »](trysqlserver.asp?filename=trysql_func_sqlserver_convert4)