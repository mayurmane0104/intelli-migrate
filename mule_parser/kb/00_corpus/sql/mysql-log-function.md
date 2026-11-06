# MySQL LOG() Function

**Source:** [https://www.w3schools.com/sql/func_mysql_log.asp](https://www.w3schools.com/sql/func_mysql_log.asp)

---

# MySQL LOG() Function

## Definition and Usage

The LOG() function returns the natural logarithm of a specified *number*, or the logarithm of 
the 
*number* to the 
specified *base*.

**Note:** See also the [LN()](func_mysql_ln.asp) and
[EXP()](func_mysql_exp.asp) functions.

## Syntax

```
LOG(
```
*number*)
OR:

```
  LOG(
```
*base, number*)
## Parameter Values

| Parameter | Description | 
|---|---|
| number | Required. A number. Must be greater than 0 | 
| base | The base of number. Must be greater 
    than 1 | 

## Technical Details

| Works in: | From MySQL 4.0 | 
|---|

## More Examples

### Example

Return the natural logarithm of 4 to a specified base (2):

```
SELECT LOG(2, 4); 
```
[Try it Yourself »](trymysql.asp?filename=trysql_func_mysql_log2)

Ad