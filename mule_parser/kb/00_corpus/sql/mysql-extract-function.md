# MySQL EXTRACT() Function

**Source:** [https://www.w3schools.com/sql/func_mysql_extract.asp](https://www.w3schools.com/sql/func_mysql_extract.asp)

---

# MySQL EXTRACT() Function

### Example[Get your own SQL Server](/sql/sql_server.asp)

Extract the month from a date:

```
  SELECT EXTRACT(MONTH FROM "2017-06-15"); 
```
[Try it Yourself »](trymysql.asp?filename=trysql_func_mysql_extract)

## Definition and Usage

The EXTRACT() function extracts a part from a given date.

## Syntax

```
  EXTRACT(
```
*part* FROM *date*)
  
## Parameter Values

| Parameter | Description | 
|---|---|
| part | Required. The part to extract. Can be one of the following: 
 | 
| date | Required. The date to extract a part from | 

## Technical Details

| Works in: | From MySQL 4.0 | 
|---|

Ad

## More Examples

### Example

Extract the minute from a datetime:

```
SELECT EXTRACT(MINUTE FROM "2017-06-15 09:34:21"); 
```
[Try it Yourself »](trymysql.asp?filename=trysql_func_mysql_extract3)

### Example

Extract the year and month from a datetime:

```
SELECT EXTRACT(YEAR_MONTH FROM "2017-06-15 09:34:21"); 
```
[Try it Yourself »](trymysql.asp?filename=trysql_func_mysql_extract4)