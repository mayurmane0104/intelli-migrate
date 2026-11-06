# MySQL FIND_IN_SET() Function

**Source:** [https://www.w3schools.com/sql/func_mysql_find_in_set.asp](https://www.w3schools.com/sql/func_mysql_find_in_set.asp)

---

# MySQL FIND_IN_SET() Function

### Example[Get your own SQL Server](/sql/sql_server.asp)

Search for "q" within the list of strings:

```
  SELECT FIND_IN_SET("q", "s,q,l"); 
```
[Try it Yourself »](trymysql.asp?filename=trysql_func_mysql_find_in_set)

## Definition and Usage

The FIND_IN_SET() function returns the position of a string within a list of strings.

## Syntax

```
  FIND_IN_SET(
```
*string*, *string_list*)
## Parameter Values

| Parameter | Description | 
|---|---|
| string | Required. The string to search for | 
| string_list | Required. The list of string values to be searched (separated by commas) | 

## Return Values

- If *string*is not found in*string_list*, this function returns 0
- If *string*or*string_list*is NULL, this function returns NULL
- If *string_list*is an empty string (""), this function returns 0

## Technical Details

| Works in: | From MySQL 4.0 | 
|---|

## More Examples

### Example

Search for "a" within the list of strings:

```
  SELECT FIND_IN_SET("a", "s,q,l"); 
```
[Try it Yourself »](trymysql.asp?filename=trysql_func_mysql_find_in_set2)

### Example

Search for "q" within the list of strings (string list is NULL):

```
  SELECT FIND_IN_SET("q", null); 
```
[Try it Yourself »](trymysql.asp?filename=trysql_func_mysql_find_in_set3)