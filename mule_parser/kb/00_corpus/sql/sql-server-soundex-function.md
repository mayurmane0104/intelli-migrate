# SQL Server SOUNDEX() Function

**Source:** [https://www.w3schools.com/sql/func_sqlserver_soundex.asp](https://www.w3schools.com/sql/func_sqlserver_soundex.asp)

---

# SQL Server SOUNDEX() Function

### Example[Get your own SQL Server](/sql/sql_server.asp)

Evaluate the similarity of two strings, and return a four-character code:

```
SELECT SOUNDEX('Juice'), SOUNDEX('Jucy'); 
```
[Try it Yourself »](trysqlserver.asp?filename=trysql_func_sqlserver_soundex)

## Definition and Usage

The SOUNDEX() function returns a four-character code to evaluate the similarity of two expressions.

**Note:** The SOUNDEX() converts the string to a four-character 
code based on how the string sounds when spoken.

**Tip:** Also look at the [DIFFERENCE()](func_sqlserver_difference.asp) function.

## Syntax

```
  SOUNDEX(
```
*expression*)
## Parameter Values

| Parameter | Description | 
|---|---|
| expression | Required. The expression to evaluate. Can be a constant, variable, or column | 

## Technical Details

| Works in: | SQL Server (starting with 2008), Azure SQL Database, Azure SQL Data Warehouse, Parallel Data Warehouse | 
|---|

## More Examples

### Example

Evaluate the similarity of two strings, and return a four-character code:

```
SELECT SOUNDEX('Juice'), SOUNDEX('Banana'); 
```
[Try it Yourself »](trysqlserver.asp?filename=trysql_func_sqlserver_soundex2)

Ad