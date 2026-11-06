# MS Access Mid() Function

**Source:** [https://www.w3schools.com/sql/func_msaccess_mid.asp](https://www.w3schools.com/sql/func_msaccess_mid.asp)

---

# MS Access Mid() Function

### Example[Get your own SQL Server](/sql/sql_server.asp)

Extract characters from a string, starting at position 3:

```
  SELECT Mid("SQL Tutorial", 3) AS ExtractString; 
```
[Try it Yourself »](trysql.asp?filename=trysql_func_ms_mid&ss=-1)

## Definition and Usage

The Mid() function extracts some characters from a string (starting at any position).

## Syntax

```
  Mid(
```
*string*, *start*, *length*)
## Parameter Values

| Parameter | Description | 
|---|---|
| string | Required. The string to extract from | 
| start | Required. The start position | 
| length | Optional. The number of characters to extract. If omitted, this 
    function returns all characters from the startposition | 

## Technical Details

| Works in: | From Access 2000 | 
|---|

## More Examples

### Example

Extract characters from the text in a column (start at position 4, and extract 6 characters):

```
  SELECT Mid(CustomerName, 4, 6) AS ExtractString
FROM Customers; 
```
[Try it Yourself »](trysql.asp?filename=trysql_func_ms_mid2&ss=-1)

Ad