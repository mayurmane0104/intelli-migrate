# MySQL CONV() Function

**Source:** [https://www.w3schools.com/sql/func_mysql_conv.asp](https://www.w3schools.com/sql/func_mysql_conv.asp)

---

# MySQL CONV() Function

### Example[Get your own SQL Server](/sql/sql_server.asp)

Convert a number from numeric base system 10 to numeric base system 2:

```
  SELECT CONV(15, 
  10, 2); 
```
[Try it Yourself »](trymysql.asp?filename=trysql_func_mysql_conv)

## Definition and Usage

The CONV() function converts a number from one numeric base system to another, and returns the result as a string value.

**Note:** This function returns NULL if any of the parameters 
are NULL.

**Tip:** Also look at the [BIN()](func_mysql_bin.asp) function.

## Syntax

```
  CONV(
```
*number*, *from_base*, *to_base*)
## Parameter Values

| Parameter | Description | 
|---|---|
| number | Required. A number | 
| from_base | The numeric base system of number(a number between 2 and 36) | 
| to_base | The numeric base system to convert to (a number between 2 and 36 or -2 and -36) | 

## Technical Details

| Works in: | From MySQL 4.0 | 
|---|

Ad

## More Examples

### Example

Convert a number from numeric base system 2 to numeric base system 10:

```
SELECT CONV(1111, 2, 10);  
```
[Try it Yourself »](trymysql.asp?filename=trysql_func_mysql_conv2)

### Example

Convert a number from numeric base system 10 to numeric base system 16:

```
SELECT CONV(88, 10, 16);  
```
[Try it Yourself »](trymysql.asp?filename=trysql_func_mysql_conv3)