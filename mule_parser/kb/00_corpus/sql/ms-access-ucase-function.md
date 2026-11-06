# MS Access UCase() Function

**Source:** [https://www.w3schools.com/sql/func_msaccess_ucase.asp](https://www.w3schools.com/sql/func_msaccess_ucase.asp)

---

# MS Access UCase() Function

### Example[Get your own SQL Server](/sql/sql_server.asp)

Convert the text in "CustomerName" to upper-case:

```
 SELECT UCASE(CustomerName) AS UppercaseCustomerName
FROM Customers;  
```
[Try it Yourself »](trysql.asp?filename=trysql_func_ms_ucase&ss=-1)

## Definition and Usage

The UCase() function converts a string to upper-case.

**Tip:** Also look at the [
LCase()](func_msaccess_lcase.asp) function.

## Syntax

```
UCase(
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