# MySQL INSTR() Function

**Source:** [https://www.w3schools.com/sql/func_mysql_instr.asp](https://www.w3schools.com/sql/func_mysql_instr.asp)

---

# MySQL INSTR() Function

### Example[Get your own SQL Server](/sql/sql_server.asp)

Search for "3" in string "W3Schools.com", and return position:

```
  SELECT INSTR("W3Schools.com", "3") AS MatchPosition; 
```
[Try it Yourself »](trymysql.asp?filename=trysql_func_mysql_instr)

## Definition and Usage

The INSTR() function returns the position of the first occurrence of a string in another string.

This function performs a case-insensitive search.

## Syntax

```
  INSTR(
```
*string1*, *string2*)
## Parameter Values

| Parameter | Description | 
|---|---|
| string1 | Required. The string that will be searched | 
| string2 | Required. The string to search for in string1. Ifstring2is not found, this function returns 0 | 

## Technical Details

| Works in: | From MySQL 4.0 | 
|---|

Ad

## More Examples

### Example

Search for "COM" in string "W3Schools.com", and return position:

```
SELECT INSTR("W3Schools.com", "COM") AS MatchPosition; 
```
[Try it Yourself »](trymysql.asp?filename=trysql_func_mysql_instr2)

### Example

Search for "a" in CustomerName column, and return position:

```
  SELECT INSTR(CustomerName, "a")
FROM Customers; 
```
[Try it Yourself »](trymysql.asp?filename=trysql_func_mysql_instr3)