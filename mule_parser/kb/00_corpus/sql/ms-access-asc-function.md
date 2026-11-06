# MS Access Asc() Function

**Source:** [https://www.w3schools.com/sql/func_msaccess_asc.asp](https://www.w3schools.com/sql/func_msaccess_asc.asp)

---

# MS Access Asc() Function

### Example[Get your own SQL Server](/sql/sql_server.asp)

Return the ASCII value of the first character in "CustomerName":

```
 SELECT Asc(CustomerName) AS NumCodeOfFirstChar
FROM Customers;  
```
[Try it Yourself »](trysql.asp?filename=trysql_func_ms_asc&ss=-1)

## Definition and Usage

The Asc() function returns the ASCII value for the specific character.

## Syntax

```
  Asc(
```
*character*)
## Parameter Values

| Parameter | Description | 
|---|---|
| character | Required. The character to return the ASCII value for. If more than one character is entered, it will only return the value for the first character | 

## Technical Details

| Works in: | From Access 2000 | 
|---|

Ad