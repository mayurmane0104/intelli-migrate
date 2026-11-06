# MySQL INSERT() Function

**Source:** [https://www.w3schools.com/sql/func_mysql_insert.asp](https://www.w3schools.com/sql/func_mysql_insert.asp)

---

# MySQL INSERT() Function

### Example[Get your own SQL Server](/sql/sql_server.asp)

Insert the string "Example" into the string "W3Schools.com". Replace the first nine characters:

```
  SELECT INSERT("W3Schools.com", 1, 9, "Example"); 
```
[Try it Yourself »](trymysql.asp?filename=trysql_func_mysql_insert)

## Definition and Usage

The INSERT() function inserts a string within a string at the specified position and for a certain number of characters.

## Syntax

```
  INSERT(
```
*string*, *position*, *number*, *string2*)
## Parameter Values

| Parameter | Description | 
|---|---|
| string | Required. The string that will be modified | 
| position | Required. The position where to insert string2 | 
| number | Required. The number of characters to replace | 
| string2 | Required. The string to insert into string | 

## Return Values

- If *position*is outside the length of*string*, this function returns*string*
- If *number*is higher than the length of the rest of the*string*, this function replaces*string*from*position*until the end of*string*

## Technical Details

| Works in: | From MySQL 4.0 | 
|---|

## More Examples

### Example

Insert the string "no" into the string "W3Schools.com". Replace three characters, starting from position 11:

```
  SELECT INSERT("W3Schools.com", 11, 3, "no"); 
```
[Try it Yourself »](trymysql.asp?filename=trysql_func_mysql_insert2)