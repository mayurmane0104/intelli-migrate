# MS Access Concat with &

**Source:** [https://www.w3schools.com/sql/func_msaccess_concat.asp](https://www.w3schools.com/sql/func_msaccess_concat.asp)

---

# MS Access Concat With &

### Example[Get your own SQL Server](/sql/sql_server.asp)

Add 3 columns together into one "Address" column:

```
SELECT Address & ", " & PostalCode & ", " & City AS Address
FROM Customers;  
```
[Try it Yourself »](trysql.asp?filename=trysql_func_ms_concat&ss=-1)

## Definition and Usage

The & operator allows you to add two or more strings together.

## Syntax

```
  
```
*string1* & *string2* & *string_n*
## Parameter Values

| Parameter | Description | 
|---|---|
| string1, string2, string_n | Required. The strings to add together | 

## Technical Details

| Works in: | From Access 2000 | 
|---|

Ad