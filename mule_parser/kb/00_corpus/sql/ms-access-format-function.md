# MS Access Format() Function

**Source:** [https://www.w3schools.com/sql/func_msaccess_format.asp](https://www.w3schools.com/sql/func_msaccess_format.asp)

---

# MS Access Format() Function

### Example[Get your own SQL Server](/sql/sql_server.asp)

Format the "Price" column to Currency:

```
  SELECT Format(Price, "Currency") AS FormattedPrice
FROM Products;  
```
[Try it Yourself »](trysql.asp?filename=trysql_func_ms_format&ss=-1)

## Definition and Usage

The Format() function formats a value with the specified format.

## Syntax

```
  Format(
```
*value*, *format*)
## Parameter Values

| Parameter | Description | ||||||||||||||||||||||||||||||||||
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| value | Required. The string to format | ||||||||||||||||||||||||||||||||||
| format | Optional. The format to to use. 
 | 

## Technical Details

| Works in: | From Access 2000 | 
|---|