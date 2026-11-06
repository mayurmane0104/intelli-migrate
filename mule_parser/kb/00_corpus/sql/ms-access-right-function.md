# MS Access Right() Function

**Source:** [https://www.w3schools.com/sql/func_msaccess_right.asp](https://www.w3schools.com/sql/func_msaccess_right.asp)

---

# MS Access Right() Function

### Example[Get your own SQL Server](/sql/sql_server.asp)

Extract 4 characters from a string (starting from right):

```
  SELECT 
  Right("SQL Tutorial is cool", 4) AS ExtractString; 
```
[Try it Yourself »](trysql.asp?filename=trysql_func_ms_right&ss=-1)

## Definition and Usage

The Right() function extracts a number of characters from a string (starting from right).

**Note:** See also the [Left()](func_msaccess_left.asp) function.

## Syntax

```
  Right(
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

Extract 5 characters from the text in the "CustomerName" column (starting from right):

```
  SELECT Right(CustomerName, 5) AS ExtractString
FROM Customers; 
```
[Try it Yourself »](trysql.asp?filename=trysql_func_ms_right2&ss=-1)

Ad