# MySQL RIGHT() Function

**Source:** [https://www.w3schools.com/sql/func_mysql_right.asp](https://www.w3schools.com/sql/func_mysql_right.asp)

---

# MySQL RIGHT() Function

### Example[Get your own SQL Server](/sql/sql_server.asp)

Extract 4 characters from a string (starting from right):

```
  SELECT RIGHT("SQL Tutorial is cool", 4) AS ExtractString; 
```
[Try it Yourself »](trymysql.asp?filename=trysql_func_mysql_right)

## Definition and Usage

The RIGHT() function extracts a number of characters from a string (starting from right).

**Tip:** Also look at the [LEFT()](func_mysql_left.asp) 
function.

## Syntax

```
  RIGHT(
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

Extract 5 characters from the text in the "CustomerName" column (starting from right):

```
  SELECT RIGHT(CustomerName, 5) AS ExtractString
FROM Customers; 
```
[Try it Yourself »](trymysql.asp?filename=trysql_func_mysql_right2)

Ad