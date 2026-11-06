# MySQL UCASE() Function

**Source:** [https://www.w3schools.com/sql/func_mysql_ucase.asp](https://www.w3schools.com/sql/func_mysql_ucase.asp)

---

# MySQL UCASE() Function

### Example[Get your own SQL Server](/sql/sql_server.asp)

Convert the text to upper-case:

```
SELECT UCASE("SQL Tutorial is FUN!");  
```
[Try it Yourself »](trymysql.asp?filename=trysql_func_mysql_ucase)

## Definition and Usage

The UCASE() function converts a string to upper-case.

**Note:** This function is equal to the [UPPER()](func_mysql_upper.asp) function.

## Syntax

```
  UCASE(
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
SELECT UCASE(CustomerName) AS UppercaseCustomerName
FROM Customers;  
```
[Try it Yourself »](trymysql.asp?filename=trysql_func_mysql_ucase2)

Ad