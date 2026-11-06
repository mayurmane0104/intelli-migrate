# MS Access LCase() Function

**Source:** [https://www.w3schools.com/sql/func_msaccess_lcase.asp](https://www.w3schools.com/sql/func_msaccess_lcase.asp)

---

# MS Access LCase() Function

### Example[Get your own SQL Server](/sql/sql_server.asp)

Convert the text in "CustomerName" to lower-case:

```
SELECT LCASE(CustomerName) AS LowercaseCustomerName
FROM Customers;  
```
[Try it Yourself »](trysql.asp?filename=trysql_func_ms_lcase&ss=-1)

## Definition and Usage

The LCase() function converts a string to lower-case.

**Tip:** Also look at the [
UCase()](func_msaccess_ucase.asp) function.

## Syntax

```
  LCase(
```
*text*)
## Parameter Values

| Parameter | Description | 
|---|---|
| text | Required. The string to convert | 

## Technical Details

| Works in: | From Access 2000 | 
|---|

Ad