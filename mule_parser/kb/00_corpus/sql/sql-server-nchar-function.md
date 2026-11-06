# SQL Server NCHAR() Function

**Source:** [https://www.w3schools.com/sql/func_sqlserver_nchar.asp](https://www.w3schools.com/sql/func_sqlserver_nchar.asp)

---

# SQL Server NCHAR() Function

### Example[Get your own SQL Server](/sql/sql_server.asp)

Return the Unicode character based on the number code 65:

```
SELECT NCHAR(65) AS NumberCodeToUnicode;  
```
[Try it Yourself »](trysqlserver.asp?filename=trysql_func_sqlserver_nchar)

## Definition and Usage

The NCHAR() function returns the Unicode character based on the number code.

## Syntax

```
  NCHAR(
```
*number_code*)
## Parameter Values

| Parameter | Description | 
|---|---|
| number_code | Required. The number code in the Unicode standard to return the character for | 

## Technical Details

| Works in: | SQL Server (starting with 2008), Azure SQL Database, Azure SQL Data Warehouse, Parallel Data Warehouse | 
|---|

Ad