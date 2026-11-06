# MySQL SUBSTRING_INDEX() Function

**Source:** [https://www.w3schools.com/sql/func_mysql_substring_index.asp](https://www.w3schools.com/sql/func_mysql_substring_index.asp)

---

# MySQL SUBSTRING_INDEX() Function

### Example[Get your own SQL Server](/sql/sql_server.asp)

Return a substring of a string before a specified number of delimiter occurs:

```
  SELECT SUBSTRING_INDEX("www.w3schools.com", ".", 1); 
```
[Try it Yourself »](trymysql.asp?filename=trysql_func_mysql_substring_index)

## Definition and Usage

The SUBSTRING_INDEX() function returns a substring of a string before a specified number of delimiter occurs.

## Syntax

```
  SUBSTRING_INDEX(
```
*string*, *delimiter*, *number*)
## Parameter Values

| Parameter | Description | 
|---|---|
| string | Required. The original string | 
| delimiter | Required. The delimiter to search for | 
| number | Required. The number of times to search for the delimiter.Can 
    be both a positive or negative number. If it is a positive number, this 
    function returns all to the left of thedelimiter. If it is a 
    negative number, this function returns all to the right of thedelimiter. | 

## Technical Details

| Works in: | From MySQL 4.0 | 
|---|

## More Examples

### Example

Return a substring of a string before a specified number of delimiter occurs:

```
  SELECT SUBSTRING_INDEX("www.w3schools.com", ".", 2); 
```
[Try it Yourself »](trymysql.asp?filename=trysql_func_mysql_substring_index2)

Ad