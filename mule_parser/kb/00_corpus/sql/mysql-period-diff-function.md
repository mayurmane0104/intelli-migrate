# MySQL PERIOD_DIFF() Function

**Source:** [https://www.w3schools.com/sql/func_mysql_period_diff.asp](https://www.w3schools.com/sql/func_mysql_period_diff.asp)

---

# MySQL PERIOD_DIFF() Function

### Example[Get your own SQL Server](/sql/sql_server.asp)

Return the difference between two periods:

```
  SELECT PERIOD_DIFF(201710, 201703); 
```
[Try it Yourself »](trymysql.asp?filename=trysql_func_mysql_period_diff)

## Definition and Usage

The PERIOD_DIFF() function returns the difference between two periods. The result will be in months.

**Note:** *period1* and *period2* should be in the 
same format.

## Syntax

```
  PERIOD_DIFF(
```
*period1*, *period2*)
  
## Parameter Values

| Parameter | Description | 
|---|---|
| period1 | Required. A period. Format: YYMM or YYYYMM | 
| period2 | Required. Another period. Format: YYMM or YYYYMM | 

## Technical Details

| Works in: | From MySQL 4.0 | 
|---|

Ad

## More Examples

### Example

Return the difference between two periods:

```
  SELECT PERIOD_DIFF(201703, 201803); 
```
[Try it Yourself »](trymysql.asp?filename=trysql_func_mysql_period_diff2)

### Example

Return the difference between two periods:

```
  SELECT PERIOD_DIFF(1703, 1612); 
```
[Try it Yourself »](trymysql.asp?filename=trysql_func_mysql_period_diff3)