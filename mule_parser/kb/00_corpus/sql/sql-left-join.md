# SQL LEFT JOIN

**Source:** [https://www.w3schools.com/sql/sql_ref_left_join.asp](https://www.w3schools.com/sql/sql_ref_left_join.asp)

---

# SQL LEFT JOIN Keyword

## LEFT JOIN

The `LEFT JOIN` command returns all rows from 
the left table, and the matching rows from the right table. The result is NULL 
from the right side, if there is no match.

The following SQL will select all customers, and any orders they might have:

### Example[Get your own SQL Server](/sql/sql_server.asp)

```
 SELECT Customers.CustomerName, Orders.OrderID
 FROM Customers
 LEFT JOIN Orders
 ON Customers.CustomerID = Orders.CustomerID
 ORDER BY Customers.CustomerName;
 
```
[Try it Yourself »](trysql.asp?filename=trysql_select_join_left)

**Note:** The `LEFT JOIN` keyword returns all records from the 
left table (Customers), even if there are no matches in the right table 
(Orders).

Ad