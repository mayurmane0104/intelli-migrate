# MySQL LEFT() Function

**Source:** [https://www.w3schools.com/sql/func_mysql_left.asp](https://www.w3schools.com/sql/func_mysql_left.asp)

---

# MySQL LEFT() Function

### Example[Get your own SQL Server](/sql/sql_server.asp)

Extract 3 characters from a string (starting from left):

```
  SELECT LEFT("SQL Tutorial", 3) AS ExtractString; 
```
[Try it Yourself »](trymysql.asp?filename=trysql_func_mysql_left)

## Definition and Usage

The LEFT() function extracts a number of characters from a string (starting from left).

**Tip:** Also look at the [RIGHT()](func_mysql_right.asp) 
function.

## Syntax

```
  LEFT(
```
*string*, *number_of_chars*)
## Parameter Values

| Parameter | Description | 
|---|---|
| string | Required. The string to extract from | 
| number_of_chars | Required. The number of characters to extract. If this parameter is 
    larger than the number of characters in string, 
  this function will returnstring | 

## Technical Details

| Works in: | From MySQL 4.0 | 
|---|

## More Examples

### Example

Extract 5 characters from the text in the "CustomerName" column (starting from left):

```
  SELECT LEFT(CustomerName, 5) AS ExtractString
FROM Customers; 
```
[Try it Yourself »](trymysql.asp?filename=trysql_func_mysql_left2)