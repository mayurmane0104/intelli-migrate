# SQL Server RAND() Function

**Source:** [https://www.w3schools.com/sql/func_sqlserver_rand.asp](https://www.w3schools.com/sql/func_sqlserver_rand.asp)

---

# SQL Server RAND() Function

### Example[Get your own SQL Server](/sql/sql_server.asp)

Return a random decimal number (no seed value - so it returns a completely random number >= 0 and <1):

```
SELECT RAND(); 
```
[Try it Yourself »](trysqlserver.asp?filename=trysql_func_sqlserver_rand)

## Definition and Usage

The RAND() function returns a random number between 0 (inclusive) and 1 (exclusive).

## Syntax

```
  RAND(
```
*seed*)
## Parameter Values

| Parameter | Description | 
|---|---|
| seed | Optional. If seed is specified, it returns a repeatable sequence of random numbers. If no seed is specified, it returns a completely random number | 

## Technical Details

| Works in: | SQL Server (starting with 2008), Azure SQL Database, Azure SQL Data Warehouse | 
|---|

Ad