# MS Access Left() Function

**Source:** [https://www.w3schools.com/sql/func_msaccess_left.asp](https://www.w3schools.com/sql/func_msaccess_left.asp)

---

# MS Access Left() Function

### Example[Get your own SQL Server](/sql/sql_server.asp)

Extract 3 characters from a string (starting from left):

```
  SELECT Left("SQL Tutorial", 3) AS ExtractString; 
```
[Try it Yourself »](trysql.asp?filename=trysql_func_ms_left&ss=-1)

## Definition and Usage

The Left() function extracts a number of characters from a string (starting from left).

**Note:** See also the [Right()](func_msaccess_right.asp) function.

## Syntax

```
  Left(
```
*string*, *number_of_chars*)
## Parameter Values

| Parameter | Description | 
|---|---|
| string | Required. The string to extract from | 
| number_of_chars | Required. The number of characters to extract. If this parameter is 
    higher than the number of characters in string, 
  this function will return the entirestring | 

## Technical Details

| Works in: | From Access 2000 | 
|---|

## More Examples

### Example

Extract 5 characters from the text in the "CustomerName" column (starting from left):

```
  SELECT Left(CustomerName, 5) AS ExtractString
FROM Customers; 
```
[Try it Yourself »](trysql.asp?filename=trysql_func_ms_left2&ss=-1)

Ad