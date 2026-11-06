# MS Access DateSerial() Function

**Source:** [https://www.w3schools.com/sql/func_msaccess_dateserial.asp](https://www.w3schools.com/sql/func_msaccess_dateserial.asp)

---

# MS Access DateSerial() Function

### Example[Get your own SQL Server](/sql/sql_server.asp)

Return a date from it's parts:

```
  SELECT DateSerial(2017, 4, 20); 
```
[Try it Yourself »](trysql.asp?filename=trysql_func_ms_dateserial&ss=-1)

## Definition and Usage

The DateSerial() function returns a date from the specified parts (year, month, and day values).

## Syntax

```
DateSerial(
```
*year*, *month*, *day*)
## Parameter Values

| Parameter | Description | 
|---|---|
| year | Required. Specifies a year (4 digits) | 
| month | Required. Specifies a month (from 1 to 12) | 
| day | Required. Specifies a day (from 1 to 31) | 

## Technical Details

| Works in: | From Access 2000 | 
|---|

## More Examples

Ad