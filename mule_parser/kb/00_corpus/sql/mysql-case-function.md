# MySQL CASE Function

**Source:** [https://www.w3schools.com/sql/func_mysql_case.asp](https://www.w3schools.com/sql/func_mysql_case.asp)

---

# MySQL CASE Function

### Example[Get your own SQL Server](/sql/sql_server.asp)

Go through conditions and return a value when the first condition is met:

```
  SELECT OrderID, Quantity,
CASE
    WHEN Quantity > 30 
  THEN "The quantity is greater than 30"
    WHEN Quantity = 
  30 THEN "The quantity is 30"
    ELSE "The quantity is 
  under 30"
END
FROM OrderDetails; 
```
[Try it Yourself »](trymysql.asp?filename=trysql_case)

## Definition and Usage

The CASE statement goes through conditions and return a value when the first condition is met (like an IF-THEN-ELSE statement). So, once a condition is true, it will stop reading and return the result.

If no conditions are true, it will return the value in the ELSE clause.

If there is no ELSE part and no conditions are true, it returns NULL.

## Syntax

```
  CASE
    WHEN 
    
  WHEN 
    WHEN 
  
    ELSE 
END;
```
*condition1* THEN *result1**condition2* THEN *result2**conditionN* THEN *resultN**result*
## Parameter Values

| Parameter | Description | 
|---|---|
| condition1, condition2, ...conditionN | Required. The conditions. These are evaluated in the same order as they are listed | 
| result1, result2, ...resultN | Required. The value to return once a condition is true | 

## Technical Details

| Works in: | From MySQL 4.0 | 
|---|

## More Examples

The following SQL will order the customers by City. However, if City is NULL, then order by Country:

### Example

```
  SELECT CustomerName, City, Country
FROM Customers
ORDER BY
(CASE
    
  WHEN City IS NULL THEN Country
    ELSE City
END); 
```
[Try it Yourself »](trymysql.asp?filename=trysql_case2)