# MySQL DATE() Function

**Source:** [https://www.w3schools.com/sql/func_mysql_date.asp](https://www.w3schools.com/sql/func_mysql_date.asp)

---

# MySQL DATE() Function

## Definition and Usage

The DATE() function extracts the date part from a datetime expression.

## Syntax

```
  DATE(
```
*expression*)
## Parameter Values

| Parameter | Description | 
|---|---|
| expression | Required. A valid date/datetime value. Returns NULL if expression is not a date or a datetime | 

## Technical Details

| Works in: | From MySQL 4.0 | 
|---|

Ad

## More Examples

### Example

Extract the date part (will return NULL):

```
SELECT DATE("The 
  date is 2017-06-15"); 
```
[Try it Yourself »](trymysql.asp?filename=trysql_func_mysql_date3)