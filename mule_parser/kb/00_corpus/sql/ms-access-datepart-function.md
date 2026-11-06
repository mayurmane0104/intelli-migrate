# MS Access DatePart() Function

**Source:** [https://www.w3schools.com/sql/func_msaccess_datepart.asp](https://www.w3schools.com/sql/func_msaccess_datepart.asp)

---

# MS Access DatePart() Function

### Example[Get your own SQL Server](/sql/sql_server.asp)

Return the year part of the specified date:

```
  SELECT DatePart("yyyy", #09/05/2017#); 
```
[Try it Yourself »](trysql.asp?filename=trysql_func_ms_datepart&ss=-1)

## Definition and Usage

The DatePart() function returns a specified part of a date, as an integer.

## Syntax

```
DatePart(
```
*datepart*, *date*, *firstdayofweek*, *
  firstweekofyear*)
## Parameter Values

| Parameter | Description | 
|---|---|
| datepart | Required. The date part to return. Can be one of the following values: 
 | 
| date | Required. The date value to be evaluated | 
| firstdayofweek | Optional. Specifies the first day of the week. 
    Can be one of the following values: 
 | 
| firstdayofyear | Optional. Specifies the first week of the year. Can be one of the following values: 
 | 

Ad

## Technical Details

| Works in: | From Access 2000 | 
|---|

## More Examples

### Example

Return the month part of the specified date:

```
  SELECT DatePart("m", #09/05/2017#); 
```
[Try it Yourself »](trysql.asp?filename=trysql_func_ms_datepart2&ss=-1)