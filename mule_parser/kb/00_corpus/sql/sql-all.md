# SQL ALL

**Source:** [https://www.w3schools.com/sql/sql_ref_all.asp](https://www.w3schools.com/sql/sql_ref_all.asp)

---

# SQL ALL Keyword

## ALL

The `ALL` command returns true if all of the subquery values meet 
the 
condition.

The following SQL statement returns TRUE and lists the productnames if ALL the records in the OrderDetails table has quantity = 10:

### Example[Get your own SQL Server](/sql/sql_server.asp)

```
  SELECT ProductName
FROM Products
WHERE ProductID = ALL (SELECT ProductID FROM OrderDetails WHERE Quantity = 10); 
```
[Try it Yourself »](trysql.asp?filename=trysql_select_all2)

Ad