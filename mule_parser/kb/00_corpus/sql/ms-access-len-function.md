# MS Access Len() Function

**Source:** [https://www.w3schools.com/sql/func_msaccess_len.asp](https://www.w3schools.com/sql/func_msaccess_len.asp)

---

# MS Access Len() Function

### Example[Get your own SQL Server](/sql/sql_server.asp)

Return the length of a string:

```
  SELECT Len("SQL Tutorial") AS LengthOfString; 
```
[Try it Yourself »](trysql.asp?filename=trysql_func_ms_len&ss=-1)

## Definition and Usage

The Len() function returns the length of a string.

## Syntax

```
  Len(
```
*string/varname*)
## Parameter Values

| Parameter | Description | 
|---|---|
| string/varname | Required. The string or variable name to return the length for | 

## Technical Details

| Works in: | From Access 2000 | 
|---|

## More Examples

### Example

Return the length of the text in the "CustomerName" column:

```
  SELECT Len(CustomerName) AS LengthOfString
FROM Customers; 
```
[Try it Yourself »](trysql.asp?filename=trysql_func_ms_len2&ss=-1)

Ad