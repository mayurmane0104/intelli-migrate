# SQL ANY

**Source:** [https://www.w3schools.com/sql/sql_ref_any.asp](https://www.w3schools.com/sql/sql_ref_any.asp)

---

# SQL ANY Keyword

## ANY

The `ANY` command returns true if any of the subquery values meet 
the 
condition.

The following SQL statement returns TRUE and lists the productnames if it finds ANY records in the OrderDetails table where quantity = 10:

### Example[Get your own SQL Server](/sql/sql_server.asp)

```
  SELECT ProductName
FROM Products
WHERE ProductID = ANY (SELECT 
  ProductID FROM OrderDetails WHERE Quantity = 10); 
```
[Try it Yourself »](trysql.asp?filename=trysql_select_any)

The following SQL statement returns TRUE and lists the productnames if it finds ANY records in the OrderDetails table where quantity > 99:

### Example

```
  SELECT ProductName
FROM Products
WHERE ProductID = ANY (SELECT ProductID 
  FROM OrderDetails WHERE Quantity > 99); 
```
[Try it Yourself »](trysql.asp?filename=trysql_select_any2)