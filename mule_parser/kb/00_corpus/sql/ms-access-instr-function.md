# MS Access InStr() Function

**Source:** [https://www.w3schools.com/sql/func_msaccess_instr.asp](https://www.w3schools.com/sql/func_msaccess_instr.asp)

---

# MS Access InStr() Function

### Example[Get your own SQL Server](/sql/sql_server.asp)

Search for "t" in string "Customer", and return position:

```
  SELECT InStr("Customer", "t") AS MatchPosition; 
```
[Try it Yourself »](trysql.asp?filename=trysql_func_ms_instr&ss=-1)

## Definition and Usage

The InStr() function gets the position of the first occurrence of a string in another.

This function performs a case-insensitive search.

## Syntax

```
  InStr(
```
*start*, *string1*, *string2*, *
  compare*)
## Parameter Values

| Parameter | Description | 
|---|---|
| start | Optional. The start position for the search. Position 1 is default | 
| string1 | Required. The string to be searched | 
| string2 | Required. The string to search for | 
| compare | Optional. The type of string comparison. Possible values: -1: Use the setting of Option Compare 0: Binary comparison 1: Textual comparison 2: Comparison based on info in your database | 

## Return Values

- If string2 is not found within string1, this function returns 0
- If string1 is zero-length, this function returns 0
- If string1 is null, this function returns null
- If string2 is zero-length, this function returns the value in the start parameter
- If start is > than the length of string2, this function returns 0

## Technical Details

| Works in: | From Access 2000 | 
|---|