# MS Access Replace() Function

**Source:** [https://www.w3schools.com/sql/func_msaccess_replace.asp](https://www.w3schools.com/sql/func_msaccess_replace.asp)

---

# MS Access Replace() Function

### Example[Get your own SQL Server](/sql/sql_server.asp)

Replace "i" with "a" in the string:

```
  SELECT Replace("My name is Willy Wonka", "i", "a") AS ReplaceString;  
```
## Definition and Usage

The Replace() function replaces a substring within a string, with another substring, a specified number of times.

## Syntax

```
  Replace(
```
*string1*, *find*, *replacement*, *
  start*, *
  count*, *
  compare*)
## Parameter Values

| Parameter | Description | 
|---|---|
| string1 | Required. The original string | 
| find | Required. The substring to search for in string1 | 
| replacement | Required. The substring to replace findinstring1 | 
| start | Optional. The start position in string1to begin the search. If 
    omitted, start is 1 | 
| count | Optional. The number of replaces to perform. If omitted, it will replace all occurrences of findwith
    replacement | 
| compare | Optional. The type of string comparison. Possible values: -1: Use the setting of Option Compare 0: Binary comparison 1: Textual comparison 2: Comparison based on info in your database | 

## Technical Details

| Works in: | From Access 2000 | 
|---|

Ad