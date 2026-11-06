# SQL Server TRANSLATE() Function

**Source:** [https://www.w3schools.com/sql/func_sqlserver_translate.asp](https://www.w3schools.com/sql/func_sqlserver_translate.asp)

---

# SQL Server TRANSLATE() Function

### Example[Get your own SQL Server](/sql/sql_server.asp)

Return the string from the first argument AFTER the characters specified in the second argument are translated into the characters specified in the third argument:

```
  SELECT TRANSLATE('Monday', 'Monday', 'Sunday'); // Results in Sunday 
```
[Try it Yourself »](trysqlserver.asp?filename=trysql_func_sqlserver_translate)

## Definition and Usage

The TRANSLATE() function returns the string from the first argument after the characters specified in the second argument are translated into the characters specified in the third argument.

**Note:** The TRANSLATE() function will return an error if *characters* and 
*translations* have different lengths.

## Syntax

```
  TRANSLATE(
```
*string, characters, translations*)
## Parameter Values

| Parameter | Description | 
|---|---|
| string | Required. The input string | 
| characters | Required. The characters that should be replaced | 
| translations | Required. The new characters | 

## Technical Details

| Works in: | SQL Server (starting with 2017) | 
|---|

## More Examples

### Example

Return the string from the first argument AFTER the characters specified in the second argument are translated into the characters specified in the third argument:

```
  SELECT TRANSLATE('3*[2+1]/{8-4}', '[]{}', '()()'); // Results in 3*(2+1)/(8-4) 
```
[Try it Yourself »](trysqlserver.asp?filename=trysql_func_sqlserver_translate2)