# MySQL CONCAT() Function

**Source:** [https://www.w3schools.com/sql/func_mysql_concat.asp](https://www.w3schools.com/sql/func_mysql_concat.asp)

---

# MySQL CONCAT() Function

### Example[Get your own SQL Server](/sql/sql_server.asp)

Add several strings together:

```
SELECT CONCAT("SQL ", "Tutorial ", "is ", "fun!") AS ConcatenatedString; 
```
[Try it Yourself »](trymysql.asp?filename=trysql_func_mysql_concat)

## Definition and Usage

The CONCAT() function adds two or more expressions together.

**Note:** Also look at the [CONCAT_WS()](func_mysql_concat_ws.asp) function.

## Syntax

```
  CONCAT(
```
*expression1*, *expression2*, *expression3*,...)
## Parameter Values

| Parameter | Description | 
|---|---|
| expression1,expression2, expression3, etc. | Required. The expressions to add together. 
 | 

## Technical Details

| Works in: | From MySQL 4.0 | 
|---|

## More Examples

### Example

Add three columns into one "Address" column:

```
  SELECT CONCAT(Address, " ", PostalCode, " ", City) AS Address
FROM 
  Customers; 
```
[Try it Yourself »](trymysql.asp?filename=trysql_func_mysql_concat2)

Ad