# MS Access DateDiff() Function

**Source:** [https://www.w3schools.com/sql/func_msaccess_datediff.asp](https://www.w3schools.com/sql/func_msaccess_datediff.asp)

---

# MS Access DateDiff() Function

### Example[Get your own SQL Server](/sql/sql_server.asp)

Return the difference between two dates, in years:

```
  SELECT DateDiff("yyyy", #13/01/1998#, #09/05/2017#); 
```
[Try it Yourself »](trysql.asp?filename=trysql_func_ms_datediff&ss=-1)

## Definition and Usage

The DateDiff() function returns the difference between two dates.

## Syntax

```
DateDiff(
```
*datepart*, *date1*, *date2*, *firstdayofweek*, *
  firstweekofyear*)
## Parameter Values

| Parameter | Description | 
|---|---|
| datepart | Required. The part to return. Can be one of the following values: 
 | 
| date1anddate2 | Required. The two dates to calculate the difference between | 
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

Return the difference between two dates, in months:

```
  SELECT DateDiff("m", #13/01/1998#, #09/05/2017#); 
```
[Try it Yourself »](trysql.asp?filename=trysql_func_ms_datediff2&ss=-1)

### Example

Return the difference between a specified date and today's date, in days:

```
  SELECT DateDiff("d", #13/01/1998#, Date()); 
```
[Try it Yourself »](trysql.asp?filename=trysql_func_ms_datediff3&ss=-1)