# MySQL UPPER() Function

**Source:** [https://www.w3schools.com/sql/func_mysql_upper.asp](https://www.w3schools.com/sql/func_mysql_upper.asp)

---

# MySQL UPPER() Function

### Example[Get your own SQL Server](/sql/sql_server.asp)

Convert the text to upper-case:

```
SELECT UPPER("SQL Tutorial is FUN!");  
```
[Try it Yourself »](trymysql.asp?filename=trysql_func_mysql_upper)

## Definition and Usage

The UPPER() function converts a string to upper-case.

**Note:** This function is equal to the [UCASE()](func_mysql_ucase.asp) 
function.

## Syntax

```
  UPPER(
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

Convert the text in "CustomerName" to upper-case:

```
SELECT UPPER(CustomerName) AS UppercaseCustomerName
FROM Customers;  
```
[Try it Yourself »](trymysql.asp?filename=trysql_func_mysql_upper2)

Ad