# SQL Server STUFF() Function

**Source:** [https://www.w3schools.com/sql/func_sqlserver_stuff.asp](https://www.w3schools.com/sql/func_sqlserver_stuff.asp)

---

# SQL Server STUFF() Function

### Example[Get your own SQL Server](/sql/sql_server.asp)

Delete 3 characters from a string, starting in position 1, and then insert "HTML" in position 1:

```
  SELECT STUFF('SQL Tutorial', 1, 3, 'HTML'); 
```
[Try it Yourself »](trysqlserver.asp?filename=trysql_func_sqlserver_stuff)

## Definition and Usage

The STUFF() function deletes a part of a string and then inserts another part into the string, starting at a specified position.

**Tip:** Also look at the [REPLACE()](func_sqlserver_replace.asp) function.

## Syntax

```
  STUFF(
```
*string*, *start*, *length*, *new_string*)
## Parameter Values

| Parameter | Description | 
|---|---|
| string | Required. The string to be modified | 
| start | Required. The position in stringto start to delete some 
    characters | 
| length | Required. The number of characters to delete from string | 
| new_string | Required. The new string to insert into stringat 
    thestartposition | 

## Technical Details

| Works in: | SQL Server (starting with 2008), Azure SQL Database, Azure SQL Data Warehouse, Parallel Data Warehouse | 
|---|

## More Examples

### Example

Delete 1 character from a string, starting in position 13, and then insert " is fun!" in position 13:

```
  SELECT STUFF('SQL Tutorial!', 13, 1, ' is fun!'); 
```
[Try it Yourself »](trysqlserver.asp?filename=trysql_func_sqlserver_stuff2)

Ad