# MS Access StrComp() Function

**Source:** [https://www.w3schools.com/sql/func_msaccess_strcomp.asp](https://www.w3schools.com/sql/func_msaccess_strcomp.asp)

---

# MS Access StrComp() Function

### Example[Get your own SQL Server](/sql/sql_server.asp)

Compare two strings:

```
  SELECT 
  StrComp("SQL Tutorial", "SQL Tutorial") AS CompString;  
```
[Try it Yourself »](trysql.asp?filename=trysql_func_ms_strcomp&ss=-1)

## Definition and Usage

The StrComp() function compares two strings.

The result is returned as an integer based on the comparison:

- If string1 = string2, this function returns 0
- If string1 < string2, this function returns -1
- If string1 > string2, this function returns 1
- If string1 or string2 is null, this function returns null

## Syntax

```
  StrComp(
```
*string1*, *string2*, *
  compare*)
## Parameter Values

| Parameter | Description | 
|---|---|
| string1 and string2 | Required. The two strings to compare | 
| compare | Optional. The type of comparison to perform. Possible values: -1: Uses option compare 0: Binary comparison 1: Textual comparison 2: Comparison based on your database | 

## Technical Details

| Works in: | From Access 2000 | 
|---|

Ad