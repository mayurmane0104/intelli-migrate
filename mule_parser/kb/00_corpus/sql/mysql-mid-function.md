# MySQL MID() Function

**Source:** [https://www.w3schools.com/sql/func_mysql_mid.asp](https://www.w3schools.com/sql/func_mysql_mid.asp)

---

# MySQL MID() Function

### Example[Get your own SQL Server](/sql/sql_server.asp)

Extract a substring from a string (start at position 5, extract 3 characters):

```
  SELECT MID("SQL Tutorial", 5, 3) AS ExtractString; 
```
[Try it Yourself »](trymysql.asp?filename=trysql_func_mysql_mid)

## Definition and Usage

The MID() function extracts a substring from a string (starting at any position).

**Note:** The position of the first character in the string is 1.

| 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 | 
| S | Q | L | T | u | t | o | r | i | a | l | 

**Note:** The position of the last character in the string is -1.

| -12 | -11 | -10 | -9 | -8 | -7 | -6 | -5 | -4 | -3 | -2 | -1 | 
| S | Q | L | T | u | t | o | r | i | a | l | 

**Note:** The MID() and [SUBSTR()](func_mysql_substr.asp) functions 
equals the [SUBSTRING()](func_mysql_substring.asp) function. 

## Syntax

```
  MID(
```
*string*, *start*, *length*)
## Parameter Values

| Parameter | Description | 
|---|---|
| string | Required. The string to extract from | 
| start | Required. The start position. Can be both a positive or negative number. If it is a positive number, this function extracts from the beginning of the string. If it is a negative number, this function extracts from the end of the string. The position of the first character in the string is 1 and the position of the last character in the string is -1 | 
| length | Optional. The number of characters to extract. If omitted, the whole 
    string will be returned (from the startposition) | 

## Technical Details

| Works in: | From MySQL 4.0 | 
|---|

## More Examples

### Example

Extract a substring from the text in a column (start at position 2, extract 5 characters):

```
  SELECT MID(CustomerName, 
  2, 5) AS ExtractString
FROM Customers; 
```
[Try it Yourself »](trymysql.asp?filename=trysql_func_mysql_mid2)

### Example

Extract a substring from a string (start from the end, at position -5, extract 5 characters):

```
  SELECT MID("SQL Tutorial", -5, 5) AS ExtractString; 
```
[Try it Yourself »](trymysql.asp?filename=trysql_func_mysql_mid3)