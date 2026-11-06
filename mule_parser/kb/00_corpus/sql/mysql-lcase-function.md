# MySQL LCASE() Function

**Source:** [https://www.w3schools.com/sql/func_mysql_lcase.asp](https://www.w3schools.com/sql/func_mysql_lcase.asp)

---

# MySQL LCASE() Function

### Example[Get your own SQL Server](/sql/sql_server.asp)

Convert the text to lower-case:

```
SELECT LCASE("SQL Tutorial is FUN!");  
```
[Try it Yourself »](trymysql.asp?filename=trysql_func_mysql_lcase)

## Definition and Usage

The LCASE() function converts a string to lower-case.

**Note:** The [LOWER()](func_mysql_lower.asp) function is a synonym for the LCASE() 
function.

## Syntax

```
  LCASE(
```
*text*)
## Parameter Values

| Parameter | Description | 
|---|---|
| text | Required. The string to convert | 

## Technical Details

| Works in: | From MySQL 4.0 | 
|---|

## More Examples

### Example

Convert the text in "CustomerName" to lower-case:

```
SELECT LCASE(CustomerName) AS LowercaseCustomerName
FROM Customers;  
```
[Try it Yourself »](trymysql.asp?filename=trysql_func_mysql_lcase2)