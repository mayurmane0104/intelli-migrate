# MS Access Round() Function

**Source:** [https://www.w3schools.com/sql/func_msaccess_round.asp](https://www.w3schools.com/sql/func_msaccess_round.asp)

---

# MS Access Round() Function

### Example[Get your own SQL Server](/sql/sql_server.asp)

Round the Price column to 1 decimal in the "Products" table:

```
 SELECT ProductName, Price, Round(Price, 1) AS RoundedPrice
FROM Products; 
```
[Try it Yourself »](trysql.asp?filename=trysql_func_ms_round&ss=-1)

## Definition and Usage

The Round() function rounds a number to a specified number of decimal places.

**Note:** If the expression ends with a 5, 
this function rounds so that the last digit is an even 
number. Here are some examples:

Round(34.55, 1) - Result: 34.6 (rounds up)

Round(34.65, 1) -
Result: 34.6 (rounds down)

## Syntax

```
  Round(
```
*expression*, *decimal_places*)
## Parameter Values

| Parameter | Description | 
|---|---|
| expression | Required. A numeric expression to be rounded | 
| decimal_places | Optional. The number of decimal places to round the expression to. If omitted, the function rounds to the nearest whole number | 

## Technical Details

| Works in: | From Access 2000 | 
|---|

Ad