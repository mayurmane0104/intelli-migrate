# SQL FULL OUTER JOIN

**Source:** [https://www.w3schools.com/sql/sql_ref_outer_join.asp](https://www.w3schools.com/sql/sql_ref_outer_join.asp)

---

# SQL FULL OUTER JOIN Keyword

## FULL OUTER JOIN

The `FULL OUTER JOIN` command returns all rows 
when there is a match in either left table or right table.

The following SQL statement selects all customers, and all orders:

```
SELECT Customers.CustomerName, Orders.OrderID
FROM Customers
FULL OUTER JOIN Orders
ON Customers.CustomerID=Orders.CustomerID
ORDER BY Customers.CustomerName;
 
```
**Note:** The `FULL OUTER JOIN` keyword returns all the rows from 
the left table (Customers), and all the rows from the right table (Orders). If 
there are rows in "Customers" that do not have matches in "Orders", or if there 
are rows in "Orders" that do not have matches in "Customers", those rows will be 
listed as well.

Ad