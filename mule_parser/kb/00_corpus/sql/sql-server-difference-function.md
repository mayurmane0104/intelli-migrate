# SQL Server DIFFERENCE() Function

**Source:** [https://www.w3schools.com/sql/func_sqlserver_difference.asp](https://www.w3schools.com/sql/func_sqlserver_difference.asp)

---

# SQL Server DIFFERENCE() Function

### Example[Get your own SQL Server](/sql/sql_server.asp)

Compares two SOUNDEX values, and return an integer:

```
SELECT DIFFERENCE('Juice', 'Jucy'); 
```
[Try it Yourself »](trysqlserver.asp?filename=trysql_func_sqlserver_difference)

## Definition and Usage

The DIFFERENCE() function compares two SOUNDEX values, and returns an integer. The integer value indicates the match for the two SOUNDEX values, from 0 to 4.

0 indicates weak or no similarity between the SOUNDEX values. 4 indicates strong similarity or identically SOUNDEX values.

**Tip:** Also look at the [SOUNDEX()](func_sqlserver_soundex.asp) 
function.

## Syntax

```
  DIFFERENCE(
```
*expression, expression*)
## Parameter Values

| Parameter | Description | 
|---|---|
| expression, expression | Required. Two expressions to be compared. Can be a constant, variable, or column | 

## Technical Details

| Works in: | SQL Server (starting with 2008), Azure SQL Database, Azure SQL Data Warehouse, Parallel Data Warehouse | 
|---|

## More Examples

### Example

Compares two SOUNDEX values, and return an integer:

```
SELECT DIFFERENCE('Juice', 'Banana'); 
```
[Try it Yourself »](trysqlserver.asp?filename=trysql_func_sqlserver_difference2)

Ad