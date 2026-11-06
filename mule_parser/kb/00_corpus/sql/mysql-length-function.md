# MySQL LENGTH() Function

**Source:** [https://www.w3schools.com/sql/func_mysql_length.asp](https://www.w3schools.com/sql/func_mysql_length.asp)

---

# MySQL LENGTH() Function

### Example[Get your own SQL Server](/sql/sql_server.asp)

Return the length of the string, in bytes:

```
SELECT LENGTH("SQL Tutorial") AS LengthOfString; 
```
[Try it Yourself »](trymysql.asp?filename=trysql_func_mysql_length)

## Definition and Usage

The LENGTH() function returns the length of a string (in bytes).

## Syntax

```
  LENGTH(
```
*string*)
## Parameter Values

| Parameter | Description | 
|---|---|
| string | Required. The string to count the length for | 

## Technical Details

| Works in: | From MySQL 4.0 | 
|---|

## More Examples

### Example

Return the length of the text in the "CustomerName" column, in bytes:

```
  SELECT LENGTH(CustomerName) AS LengthOfName
FROM Customers; 
```
[Try it Yourself »](trymysql.asp?filename=trysql_func_mysql_length2)

Ad