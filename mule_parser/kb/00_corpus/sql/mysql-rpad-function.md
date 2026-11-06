# MySQL RPAD() Function

**Source:** [https://www.w3schools.com/sql/func_mysql_rpad.asp](https://www.w3schools.com/sql/func_mysql_rpad.asp)

---

# MySQL RPAD() Function

### Example[Get your own SQL Server](/sql/sql_server.asp)

Right-pad the string with "ABC", to a total length of 20:

```
SELECT RPAD("SQL Tutorial", 
  20, "ABC"); 
```
[Try it Yourself »](trymysql.asp?filename=trysql_func_mysql_rpad)

## Definition and Usage

The RPAD() function right-pads a string with another string, to a certain length.

**Note:** Also look at the [LPAD()](func_mysql_lpad.asp) 
function.

## Syntax

```
  RPAD(
```
*string*, *
  length*, *rpad_string*)
## Parameter Values

| Parameter | Description | 
|---|---|
| string | Required. The original string. If the length of the original string is 
    larger than the lengthparameter, this function removes the overfloating characters fromstring | 
| length | Required. The length of the string after it has been right-padded | 
| rpad_string | Required. The string to right-pad to string | 

## Technical Details

| Works in: | From MySQL 4.0 | 
|---|

## More Examples

### Example

Right-pad the text in "CustomerName" with "ABC", to a total length of 30:

```
  SELECT 
  RPAD(CustomerName, 30, "ABC") AS RightPadCustomerName
FROM Customers;  
```
[Try it Yourself »](trymysql.asp?filename=trysql_func_mysql_rpad2)

Ad