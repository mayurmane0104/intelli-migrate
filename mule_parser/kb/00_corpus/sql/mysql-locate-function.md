# MySQL LOCATE() Function

**Source:** [https://www.w3schools.com/sql/func_mysql_locate.asp](https://www.w3schools.com/sql/func_mysql_locate.asp)

---

# MySQL LOCATE() Function

### Example[Get your own SQL Server](/sql/sql_server.asp)

Search for "3" in string "W3Schools.com", and return position:

```
SELECT LOCATE("3", "W3Schools.com") AS MatchPosition; 
```
[Try it Yourself »](trymysql.asp?filename=trysql_func_mysql_locate)

## Definition and Usage

The LOCATE() function returns the position of the first occurrence of a substring in a string.

If the substring is not found within the original string, this function returns 0.

This function performs a case-insensitive search.

**Note:** This function is equal to the
[POSITION()](func_mysql_position.asp) function.

## Syntax

```
LOCATE(
```
*substring*, *string*, *start*)
## Parameter Values

| Parameter | Description | 
|---|---|
| substring | Required. The substring to search for in string | 
| string | Required. The string that will be searched | 
| start | Optional. The starting position for the search. Position 1 is default | 

## Technical Details

| Works in: | From MySQL 4.0 | 
|---|

Ad

## More Examples

### Example

Search for "com" in string "W3Schools.com" (start at position 3), and return position:

```
  SELECT LOCATE("com", "W3Schools.com", 3) AS MatchPosition; 
```
[Try it Yourself »](trymysql.asp?filename=trysql_func_mysql_locate2)

### Example

Search for "a" in CustomerName column, and return position:

```
  SELECT LOCATE("a", CustomerName)
FROM Customers; 
```
[Try it Yourself »](trymysql.asp?filename=trysql_func_mysql_locate3)