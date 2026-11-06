# MS Access Format() Function

**Source:** [https://www.w3schools.com/sql/func_msaccess_format_date.asp](https://www.w3schools.com/sql/func_msaccess_format_date.asp)

---

# MS Access Format() Function

### Example[Get your own SQL Server](/sql/sql_server.asp)

Format the "BirthDate" column to a long date:

```
  SELECT Format(BirthDate, "Long Date") AS FormattedBirthDate
FROM Employees;  
```
[Try it Yourself »](trysql.asp?filename=trysql_func_ms_format_date&ss=-1)

## Definition and Usage

The Format() function formats a date value with the specified format.

## Syntax

```
Format(
```
*value*, *format*, *firstdayofweek*, *firstweekofyear*)
## Parameter Values

| Parameter | Description | ||||||||||||||||
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| value | Required. The date value to format | ||||||||||||||||
| format | Optional. The format to use. 
 | ||||||||||||||||
| firstdayofweek | Optional. Specifies the first day of the week. 
    Can be one of the following values: 
 | ||||||||||||||||
| firstdayofyear | Optional. Specifies the first week of the year. Can be one of the following values: 
 | 

Ad

## Technical Details

| Works in: | From Access 2000 | 
|---|