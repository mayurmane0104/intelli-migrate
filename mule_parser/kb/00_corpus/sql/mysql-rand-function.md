# MySQL RAND() Function

**Source:** [https://www.w3schools.com/sql/func_mysql_rand.asp](https://www.w3schools.com/sql/func_mysql_rand.asp)

---

# MySQL RAND() Function

### Example[Get your own SQL Server](/sql/sql_server.asp)

Return a random decimal number (no seed value - so it returns a completely random number >= 0 and <1):

```
  SELECT RAND(); 
```
[Try it Yourself »](trymysql.asp?filename=trysql_func_mysql_rand)

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

| Works in: | From MySQL 4.0 | 
|---|

Ad