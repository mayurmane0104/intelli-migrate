# SQL Server TRIM() Function

**Source:** [https://www.w3schools.com/sql/func_sqlserver_trim.asp](https://www.w3schools.com/sql/func_sqlserver_trim.asp)

---

# SQL Server TRIM() Function

### Example[Get your own SQL Server](/sql/sql_server.asp)

Remove leading and trailing spaces from a string:

```
  SELECT TRIM('     SQL Tutorial!     ') AS TrimmedString; 
```
[Try it Yourself »](trysqlserver.asp?filename=trysql_func_sqlserver_trim)

## Definition and Usage

The TRIM() function removes the space character OR other specified characters from the start or end of a string.

By default, the TRIM() function removes leading and trailing spaces from a string.

**Note:** Also look at the [
LTRIM()](func_sqlserver_ltrim.asp) and [RTRIM()](func_sqlserver_rtrim.asp) functions.

## Syntax

```
  TRIM([
```
*characters *FROM* *]*string*)
## Parameter Values

| Parameter | Description | 
|---|---|
| charactersFROM | Optional. Specific characters to remove | 
| string | Required. The string to remove spaces or characters from | 

## Technical Details

| Works in: | SQL Server (starting with 2017), Azure SQL Database, | 
|---|

## More Examples

### Example

Remove characters and spaces from a string:

```
  SELECT TRIM('#! ' FROM '    #SQL Tutorial!    ') AS 
  TrimmedString; 
```
[Try it Yourself »](trysqlserver.asp?filename=trysql_func_sqlserver_trim2)

Ad