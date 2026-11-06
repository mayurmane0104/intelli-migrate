# MS Access Split() Function

**Source:** [https://www.w3schools.com/sql/func_msaccess_split.asp](https://www.w3schools.com/sql/func_msaccess_split.asp)

---

# MS Access Split() Function

### Example[Get your own SQL Server](/sql/sql_server.asp)

Split strings:

```
SELECT Split("SQL Tutorial is fun!") AS SplitString;
Result: {"SQL", 
  "Tutorial", "is", "fun!"}
  SELECT Split ("red:green:yellow:blue", ":", 2) AS SplitString;
Result: {"red", "green"} 
```
## Definition and Usage

The Split() function splits a string into an array of strings.

## Syntax

```
  Split(
```
*string*, *separator*, *limit*, *compare*)
## Parameter Values

| Parameter | Description | 
|---|---|
| string | Required. The string to split | 
| separator | Optional. The separator used to split the string. The default is a space character | 
| limit | Optional. The number of strings to be returned. The default is -1, which returns all strings (splitted) | 
| compare | Optional. The type of string comparison. Possible values: -1: Use the setting of Option Compare 0: Binary comparison 1: Textual comparison 2: Comparison based on info in your database | 

## Technical Details

| Works in: | From Access 2000 | 
|---|

Ad