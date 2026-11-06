# MySQL LOWER() Function

**Source:** [https://www.w3schools.com/sql/func_mysql_lower.asp](https://www.w3schools.com/sql/func_mysql_lower.asp)

---

# MySQL LOWER() Function

### Example[Get your own SQL Server](/sql/sql_server.asp)

Convert the text to lower-case:

```
SELECT LOWER("SQL Tutorial is FUN!");  
```
[Try it Yourself »](trymysql.asp?filename=trysql_func_mysql_lower)

## Definition and Usage

The LOWER() function converts a string to lower-case.

**Note:** The [LCASE()](func_mysql_lcase.asp) 
function is equal to the LOWER() function.

## Syntax

```
  LOWER(
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
SELECT LOWER(CustomerName) AS LowercaseCustomerName
FROM Customers;  
```
[Try it Yourself »](trymysql.asp?filename=trysql_func_mysql_lower2)

Ad