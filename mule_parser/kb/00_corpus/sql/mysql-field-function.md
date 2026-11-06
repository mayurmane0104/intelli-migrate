# MySQL FIELD() Function

**Source:** [https://www.w3schools.com/sql/func_mysql_field.asp](https://www.w3schools.com/sql/func_mysql_field.asp)

---

# MySQL FIELD() Function

### Example[Get your own SQL Server](/sql/sql_server.asp)

Return the index position of "q" in the string list:

```
 SELECT FIELD("q", "s", "q", "l");  
```
[Try it Yourself »](trymysql.asp?filename=trysql_func_mysql_field)

## Definition and Usage

The FIELD() function returns the index position of a value in a list of values.

This function performs a case-insensitive search.

**Note:** If the specified value is not found in the list of values, this function 
will return 0. If value is NULL, this function will return 0.

## Syntax

```
  FIELD(
```
*value*, *val1*, *val2*, *val3*, ...)
## Parameter Values

| Parameter | Description | 
|---|---|
| value | Required. The value to search for in the list | 
| val1,val2,val3, .... | Required. The list of values to search | 

## Technical Details

| Works in: | From MySQL 4.0 | 
|---|

Ad

## More Examples

### Example

Return the index position of "c" in the string list:

```
 SELECT FIELD("c", "a", "b");  
```
[Try it Yourself »](trymysql.asp?filename=trysql_func_mysql_field2)

### Example

Return the index position of "Q" in the string list:

```
 SELECT FIELD("Q", "s", "q", "l");  
```
[Try it Yourself »](trymysql.asp?filename=trysql_func_mysql_field3)

### Example

Return the index position of 5 in the numeric list:

```
 SELECT FIELD(5, 0, 1, 2, 3, 4, 5); 
```
[Try it Yourself »](trymysql.asp?filename=trysql_func_mysql_field4)