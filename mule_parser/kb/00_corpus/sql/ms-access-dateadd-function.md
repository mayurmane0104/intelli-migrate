# MS Access DateAdd() Function

**Source:** [https://www.w3schools.com/sql/func_msaccess_dateadd.asp](https://www.w3schools.com/sql/func_msaccess_dateadd.asp)

---

# MS Access DateAdd() Function

### Example[Get your own SQL Server](/sql/sql_server.asp)

Add two years to a specified date:

```
  SELECT DateAdd("yyyy", 2, #22/11/2017#); 
```
[Try it Yourself »](trysql.asp?filename=trysql_func_ms_dateadd&ss=-1)

## Definition and Usage

The DateAdd() function adds a time/date interval to a date and then returns the date.

## Syntax

```
DateAdd(
```
*interval*, *number*, *date*)
## Parameter Values

| Parameter | Description | 
|---|---|
| interval | Required. The time/date interval to add. Can be one of the following values: 
 | 
| number | Required. The number of intervalto add to date. Can be 
    positive (to get dates in the future) or negative (to get dates in the past) | 
| date | Required. The date to which the interval should be added | 

## Technical Details

| Works in: | From Access 2000 | 
|---|

Ad

## More Examples

### Example

Add one year to the current system date:

```
  SELECT DateAdd("yyyy", 1, Date()); 
```
[Try it Yourself »](trysql.asp?filename=trysql_func_ms_dateadd2&ss=-1)

### Example

Add 6 months to the employees' birth date:

```
  SELECT LastName, DateAdd("m", 6, BirthDate) FROM Employees; 
```
[Try it Yourself »](trysql.asp?filename=trysql_func_ms_dateadd3&ss=-1)