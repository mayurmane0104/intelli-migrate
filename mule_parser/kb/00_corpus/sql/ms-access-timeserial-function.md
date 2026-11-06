# MS Access TimeSerial() Function

**Source:** [https://www.w3schools.com/sql/func_msaccess_timeserial.asp](https://www.w3schools.com/sql/func_msaccess_timeserial.asp)

---

# MS Access TimeSerial() Function

### Example[Get your own SQL Server](/sql/sql_server.asp)

Return a time from it's parts:

```
  SELECT TimeSerial(15, 9, 20); 
```
[Try it Yourself »](trysql.asp?filename=trysql_func_ms_timeserial&ss=-1)

## Definition and Usage

The TimeSerial() function returns a time from the specified parts (hour, minute, and second value).

## Syntax

```
  TimeSerial(
```
*hour*, *minute*, *second*)
## Parameter Values

| Parameter | Description | 
|---|---|
| hour | Required. Specifies the hour (an integer between 0 and 23) | 
| minute | Required. Specifies the minute (an integer between 0 and 59) | 
| second | Required. Specifies the seconds (an integer between 0 and 59) | 

## Technical Details

| Works in: | From Access 2000 | 
|---|

## More Examples

Ad