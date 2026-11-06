# MS Access InstrRev() Function

**Source:** [https://www.w3schools.com/sql/func_msaccess_instrrev.asp](https://www.w3schools.com/sql/func_msaccess_instrrev.asp)

---

# MS Access InstrRev() Function

### Example[Get your own SQL Server](/sql/sql_server.asp)

Search for "t" in string "Customer" (start from the end of the string) and return position:

```
  SELECT InstrRev("Customer", "t") AS 
  MatchPosition;  
```
## Definition and Usage

The InstrRev() function gets the position of the first occurrence of a string in another, from the end of string.

This function performs a case-insensitive search.

## Syntax

```
  InstrRev(
```
*string1*, *string2*, *
  start*, *
  compare*)
## Parameter Values

| Parameter | Description | 
|---|---|
| string1 | Required. The string to be searched | 
| string2 | Required. The string to search for | 
| start | Optional. The start position for the search. Position -1 is default (which means that it starts with the last character position) | 
| compare | Optional. The type of string comparison. Possible values: -1: Use the setting of Option Compare 0: Binary comparison 1: Textual comparison 2: Comparison based on info in your database | 

## Return Values

- If string2 is not found within string1, this function returns 0
- If string2 is zero-length, this function returns the value in the start parameter
- If string1 is zero-length, this function returns 0
- If string1 is null, this function returns null
- If start is > than the length of string2, this function returns 0

## Technical Details

| Works in: | From Access 2000 | 
|---|