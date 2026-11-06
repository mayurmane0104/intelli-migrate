# MySQL ASCII() Function

**Source:** [https://www.w3schools.com/sql/func_mysql_ascii.asp](https://www.w3schools.com/sql/func_mysql_ascii.asp)

---

# MySQL ASCII() Function

### Example[Get your own SQL Server](/sql/sql_server.asp)

Return the ASCII value of the first character in "CustomerName":

```
 SELECT ASCII(CustomerName) AS NumCodeOfFirstChar
FROM Customers;  
```
[Try it Yourself »](trymysql.asp?filename=trysql_func_mysql_ascii)

## Definition and Usage

The ASCII() function returns the ASCII value for the specific character.

## Syntax

```
  ASCII(
```
*character*)
## Parameter Values

| Parameter | Description | 
|---|---|
| character | Required. The character to return the ASCII value for. If more than one character is entered, it will only return the value for the first character | 

## Technical Details

| Works in: | From MySQL 4.0 | 
|---|