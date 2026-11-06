# SQL Server LOG() Function

**Source:** [https://www.w3schools.com/sql/func_sqlserver_log.asp](https://www.w3schools.com/sql/func_sqlserver_log.asp)

---

# SQL Server LOG() Function

## Definition and Usage

The LOG() function returns the natural logarithm of a specified *number*, or the logarithm of 
the 
*number* to the 
specified *base*.

From SQL Server 2012, you can also change the base of the logarithm to another value by using the optional base parameter.

**Note:** Also look at the [EXP()](func_sqlserver_exp.asp) function.

## Syntax

```
LOG(
```
*number, base*) -- Syntax for SQL Server
OR:

```
LOG(
```
*number*) -- Syntax for Azure SQL Database, Azure SQL Data Warehouse, Parallel Data Warehouse
## Parameter Values

| Parameter | Description | 
|---|---|
| number | Required. The number to return the natural logarithm of. Must be greater than 0 | 
| base | Optional. The base the natural logarithm is to be calculated with. Must be greater than 1 | 

## Technical Details

| Works in: | SQL Server (starting with 2008), Azure SQL Database, Azure SQL Data Warehouse, Parallel Data Warehouse | 
|---|

## More Examples

### Example

Return the natural logarithm of 2 to a specified base (4):

```
SELECT LOG(2, 4); 
```
[Try it Yourself »](trysqlserver.asp?filename=trysql_func_sqlserver_log2)

Ad