# MySQL CONCAT_WS() Function

**Source:** [https://www.w3schools.com/sql/func_mysql_concat_ws.asp](https://www.w3schools.com/sql/func_mysql_concat_ws.asp)

---

# MySQL CONCAT_WS() Function

### Example[Get your own SQL Server](/sql/sql_server.asp)

Add several expressions together, and add a "-" separator between them:

```
SELECT CONCAT_WS("-", "SQL", "Tutorial", "is", "fun!") AS ConcatenatedString; 
```
[Try it Yourself »](trymysql.asp?filename=trysql_func_mysql_concat_ws)

## Definition and Usage

The CONCAT_WS() function adds two or more expressions together with a separator.

**Note:** Also look at the [CONCAT()](func_mysql_concat.asp) function.

## Syntax

```
  CONCAT_WS(
```
*separator*, *expression1*, *expression2*, *expression3*,...)
## Parameter Values

| Parameter | Description | 
|---|---|
| separator | Required. The separator to add between each of the expressions. If separator is NULL, this function returns NULL | 
| expression1,expression2, expression3, etc. | Required. The expressions to add together. An expression with a NULL value will be skipped | 

## Technical Details

| Works in: | From MySQL 4.0 | 
|---|

## More Examples

### Example

Add three columns (and add a space between them) into one "Address" column:

```
  SELECT CONCAT_WS(" ", Address, PostalCode, City) AS Address
FROM 
  Customers; 
```
[Try it Yourself »](trymysql.asp?filename=trysql_func_mysql_concat_ws2)

Ad