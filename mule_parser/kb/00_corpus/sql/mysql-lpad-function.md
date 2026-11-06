# MySQL LPAD() Function

**Source:** [https://www.w3schools.com/sql/func_mysql_lpad.asp](https://www.w3schools.com/sql/func_mysql_lpad.asp)

---

# MySQL LPAD() Function

### Example[Get your own SQL Server](/sql/sql_server.asp)

Left-pad the string with "ABC", to a total length of 20:

```
SELECT LPAD("SQL Tutorial", 
  20, "ABC"); 
```
[Try it Yourself »](trymysql.asp?filename=trysql_func_mysql_lpad)

## Definition and Usage

The LPAD() function left-pads a string with another string, to a certain length.

**Note:** Also look at the [RPAD()](func_mysql_rpad.asp) 
function.

## Syntax

```
  LPAD(
```
*string*, *
  length*, *lpad_string*)
## Parameter Values

| Parameter | Description | 
|---|---|
| string | Required. The original string. If the length of the original string is 
    larger than the lengthparameter, this function removes the overfloating characters fromstring | 
| length | Required. The length of the string after it has been left-padded | 
| lpad_string | Required. The string to left-pad to string | 

## Technical Details

| Works in: | From MySQL 4.0 | 
|---|

## More Examples

### Example

Left-pad the text in "CustomerName" with "ABC", to a total length of 30:

```
  SELECT LPAD(CustomerName, 30, "ABC") AS LeftPadCustomerName
FROM Customers;  
```
[Try it Yourself »](trymysql.asp?filename=trysql_func_mysql_lpad2)

Ad