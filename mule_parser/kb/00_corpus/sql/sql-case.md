# SQL CASE

**Source:** [https://www.w3schools.com/sql/sql_ref_case.asp](https://www.w3schools.com/sql/sql_ref_case.asp)

---

# SQL CASE Keyword

## CASE

The `CASE` command is used is to 
create different output based on conditions.

The following SQL goes through several conditions and returns a value when the specified condition is met:

### Example[Get your own SQL Server](/sql/sql_server.asp)

```
  SELECT OrderID, Quantity,
CASE
    WHEN Quantity > 30 
  THEN 'The quantity is greater than 30'
    WHEN Quantity = 
  30 THEN 'The quantity is 30'
    ELSE 'The quantity is under 30'
END
FROM OrderDetails; 
```
[Try it Yourself »](trymysql.asp?filename=trysql_case)

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

Ad