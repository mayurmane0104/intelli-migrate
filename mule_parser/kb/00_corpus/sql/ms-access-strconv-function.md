# MS Access StrConv() Function

**Source:** [https://www.w3schools.com/sql/func_msaccess_strconv.asp](https://www.w3schools.com/sql/func_msaccess_strconv.asp)

---

# MS Access StrConv() Function

### Example[Get your own SQL Server](/sql/sql_server.asp)

Convert a string:

```
  SELECT StrConv("SQL Tutorial is cool", 1) AS ConvertedString;  
```
[Try it Yourself »](trysql.asp?filename=trysql_func_ms_strconv&ss=-1)

## Definition and Usage

The StrConv() function returns a converted string.

## Syntax

```
  StrConv(
```
*string1*, *
  conversion*, *
  LCID*)
## Parameter Values

| Parameter | Description | 
|---|---|
| string1 | Required. The string to be converted | 
| conversion | Required. The type of conversion to perform. Possible values: 1: Convert to upper-case 2: Convert to lower-case 3: Convert the first letter of every word to upper-case 4: Convert narrow characters to wide 16: Converts Hiragana into Katakana (Japan only) 32: Converts Katakane into Hiragana (Japan only) 64: Converts to unicode 128: Converts from Unicode to default page code | 
| LCID | Optional. The LocaleID. If omitted, this function uses the system LocaleID | 

## Technical Details

| Works in: | From Access 2000 | 
|---|

Ad

## More Examples

### Example

Convert a string:

```
  SELECT StrConv("SQL Tutorial is cool", 2) AS ConvertedString;  
```
[Try it Yourself »](trysql.asp?filename=trysql_func_ms_strconv2&ss=-1)

### Example

Convert a string:

```
  SELECT StrConv("SQL Tutorial is cool", 3) AS ConvertedString;  
```
[Try it Yourself »](trysql.asp?filename=trysql_func_ms_strconv3&ss=-1)