# MySQL REPLACE() Function

**Source:** [https://www.w3schools.com/sql/func_mysql_replace.asp](https://www.w3schools.com/sql/func_mysql_replace.asp)

---

# MySQL REPLACE() Function

### Example[Get your own SQL Server](/sql/sql_server.asp)

Replace "SQL" with "HTML":

```
  SELECT REPLACE("SQL Tutorial", "SQL", "HTML"); 
```
[Try it Yourself »](trymysql.asp?filename=trysql_func_mysql_replace)

## Definition and Usage

The REPLACE() function replaces all occurrences of a substring within a string, with a new substring.

**Note:** This function performs a case-sensitive 
replacement.

## Syntax

```
  REPLACE(
```
*string*, *from_string*, *new_string*)
## Parameter Values

| Parameter | Description | 
|---|---|
| string | Required. The original string | 
| from_string | Required. The substring to be replaced | 
| new_string | Required. The new replacement substring | 

## Technical Details

| Works in: | From MySQL 4.0 | 
|---|

Ad