# SQL Server USER_NAME() Function

**Source:** [https://www.w3schools.com/sql/func_sqlserver_user_name.asp](https://www.w3schools.com/sql/func_sqlserver_user_name.asp)

---

# SQL Server USER_NAME() Function

### Example[Get your own SQL Server](/sql/sql_server.asp)

Return the database user name (will return the current user since no id is specified):

```
  SELECT USER_NAME(); 
```
[Try it Yourself »](trysqlserver.asp?filename=trysql_func_sqlserver_user_name)

## Definition and Usage

The USER_NAME() function returns the database user name based on the specified id.

If no id is specified, this function will return the name of the current user.

## Syntax

```
USER_NAME(
```
*id_number*)
## Parameter Values

| Parameter | Description | 
|---|---|
| id_number | Optional. The id number of a user in the database | 

## Technical Details

| Works in: | SQL Server (starting with 2008), Azure SQL Database, Azure SQL Data Warehouse, Parallel Data Warehouse | 
|---|

## More Examples

Ad