# MySQL CHAR_LENGTH() Function

**Source:** [https://www.w3schools.com/sql/func_mysql_char_length.asp](https://www.w3schools.com/sql/func_mysql_char_length.asp)

---

# MySQL CHAR_LENGTH() Function

### Example[Get your own SQL Server](/sql/sql_server.asp)

Return the length of the string:

```
SELECT CHAR_LENGTH("SQL Tutorial") AS LengthOfString; 
```
[Try it Yourself »](trymysql.asp?filename=trysql_func_mysql_char_length)

## Definition and Usage

The CHAR_LENGTH() function return the length of a string (in characters).

**Note:** This function is equal to the 
[CHARACTER_LENGTH()](func_mysql_character_length.asp) function.

## Syntax

```
  CHAR_LENGTH(
```
*string*)
## Parameter Values

| Parameter | Description | 
|---|---|
| string | Required. The string to count the length for | 

## Technical Details

| Works in: | From MySQL 4.0 | 
|---|

## More Examples

### Example

Return the length of the text in the "CustomerName" column:

```
  SELECT CHAR_LENGTH(CustomerName) AS LengthOfName
FROM Customers; 
```
[Try it Yourself »](trymysql.asp?filename=trysql_func_mysql_char_length2)

Ad