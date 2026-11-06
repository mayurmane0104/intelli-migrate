# MS Access Val() Function

**Source:** [https://www.w3schools.com/sql/func_msaccess_val.asp](https://www.w3schools.com/sql/func_msaccess_val.asp)

---

# MS Access Val() Function

### Example[Get your own SQL Server](/sql/sql_server.asp)

Read a string and return the numbers found in the string:

```
  SELECT Val(PostalCode) FROM Customers; 
```
[Try it Yourself »](trysql.asp?filename=trysql_func_ms_val&ss=-1)

## Definition and Usage

The Val() function reads a string and returns the numbers found in the string.

**Note:** This function stops reading once it 
encounters a NON-numeric character.

## Syntax

```
  Val(
```
*string*)
## Parameter Values

| Parameter | Description | 
|---|---|
| string | Required. A string expression | 

## Technical Details

| Works in: | From Access 2000 | 
|---|

Ad