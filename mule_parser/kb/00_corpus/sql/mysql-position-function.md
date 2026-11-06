# MySQL POSITION() Function

**Source:** [https://www.w3schools.com/sql/func_mysql_position.asp](https://www.w3schools.com/sql/func_mysql_position.asp)

---

# MySQL POSITION() Function

### Example[Get your own SQL Server](/sql/sql_server.asp)

Search for "3" in string "W3Schools.com", and return position:

```
  SELECT POSITION("3" IN "W3Schools.com") AS MatchPosition; 
```
[Try it Yourself »](trymysql.asp?filename=trysql_func_mysql_position)

## Definition and Usage

The POSITION() function returns the position of the first occurrence of a substring in a string.

If the substring is not found within the original string, this function returns 0.

This function performs a case-insensitive search.

**Note:** The [LOCATE()](func_mysql_locate.asp) function is 
equal to the 
POSITION() function.

## Syntax

```
  POSITION(
```
*substring* IN *string*)
## Parameter Values

| Parameter | Description | 
|---|---|
| substring | Required. The substring to search for in string | 
| string | Required. The original string that will be searched | 

## Technical Details

| Works in: | From MySQL 4.0 | 
|---|

Ad

## More Examples

### Example

Search for "COM" in string "W3Schools.com", and return position:

```
SELECT POSITION("COM" IN "W3Schools.com") AS MatchPosition; 
```
[Try it Yourself »](trymysql.asp?filename=trysql_func_mysql_position2)

### Example

Search for "a" in CustomerName column, and return position:

```
  SELECT POSITION("a" IN CustomerName)
FROM Customers; 
```
[Try it Yourself »](trymysql.asp?filename=trysql_func_mysql_position3)