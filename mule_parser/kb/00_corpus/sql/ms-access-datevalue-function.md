# MS Access DateValue() Function

**Source:** [https://www.w3schools.com/sql/func_msaccess_datevalue.asp](https://www.w3schools.com/sql/func_msaccess_datevalue.asp)

---

# MS Access DateValue() Function

### Example[Get your own SQL Server](/sql/sql_server.asp)

Return a date based on the given string:

```
  SELECT DateValue("May 17, 2017"); 
```
[Try it Yourself »](trysql.asp?filename=trysql_func_ms_datevalue&ss=-1)

## Definition and Usage

The DateValue() function returns a date based on a string.

**Note:** If the given string does not include a year component, this function will use the current year.

## Syntax

```
DateValue(
```
*string_date*)
## Parameter Values

| Parameter | Description | 
|---|---|
| string_date | Required. A string that represents a date (from January 1, 100 to December 31, 9999) | 

## Technical Details

| Works in: | From Access 2000 | 
|---|

## More Examples

### Example

Return a date based on the given string (without year component):

```
  SELECT DateValue("May 17"); 
```
[Try it Yourself »](trysql.asp?filename=trysql_func_ms_datevalue2&ss=-1)

Ad