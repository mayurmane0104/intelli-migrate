# MySQL TIMESTAMP() Function

**Source:** [https://www.w3schools.com/sql/func_mysql_timestamp.asp](https://www.w3schools.com/sql/func_mysql_timestamp.asp)

---

# MySQL TIMESTAMP() Function

### Example[Get your own SQL Server](/sql/sql_server.asp)

Return a datetime value based on the arguments:

```
  SELECT TIMESTAMP("2017-07-23",  "13:10:11"); 
```
[Try it Yourself »](trymysql.asp?filename=trysql_func_mysql_timestamp)

## Definition and Usage

The TIMESTAMP() function returns a datetime value based on a date or datetime value.

**Note:** If there are specified two arguments with this 
function, it first adds the second argument to the first, and then returns a 
datetime value.

## Syntax

```
  TIMESTAMP(
```
*expression*, *time*)
  
## Parameter Values

| Parameter | Description | 
|---|---|
| expression | Required. A date or datetime value | 
| time | Optional. A time value to add to expression | 

## Technical Details

| Works in: | From MySQL 4.0 | 
|---|

## More Examples

### Example

Return a datetime value based on the arguments:

```
  SELECT TIMESTAMP("2017-07-23"); 
```
[Try it Yourself »](trymysql.asp?filename=trysql_func_mysql_timestamp2)

Ad