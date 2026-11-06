# MySQL STRCMP() Function

**Source:** [https://www.w3schools.com/sql/func_mysql_strcmp.asp](https://www.w3schools.com/sql/func_mysql_strcmp.asp)

---

# MySQL STRCMP() Function

### Example[Get your own SQL Server](/sql/sql_server.asp)

Compare two strings:

```
SELECT STRCMP("SQL Tutorial", 
  "SQL Tutorial"); 
```
[Try it Yourself »](trymysql.asp?filename=trysql_func_mysql_strcmp)

## Definition and Usage

The STRCMP() function compares two strings.

## Syntax

```
  STRCMP(
```
*string1*, *string2*)
## Parameter Values

| Parameter | Description | 
|---|---|
| string1, string2 | Required. The two strings to be compared | 

## Return Values

- If *string1*=*string2*, this function returns 0
- If *string1*<*string2*, this function returns -1
- If *string1*>*string2*, this function returns 1

## Technical Details

| Works in: | From MySQL 4.0 | 
|---|