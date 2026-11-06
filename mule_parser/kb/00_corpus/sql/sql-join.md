# SQL JOIN

**Source:** [https://www.w3schools.com/sql/sql_ref_join.asp](https://www.w3schools.com/sql/sql_ref_join.asp)

---

# SQL JOIN Keyword

## INNER JOIN

The `INNER JOIN` command returns rows that have matching values in both tables.

The following SQL selects all orders with customer information:

### Example[Get your own SQL Server](/sql/sql_server.asp)

```
  SELECT Orders.OrderID, Customers.CustomerName
FROM Orders
INNER JOIN 
  Customers ON Orders.CustomerID = Customers.CustomerID; 
```
[Try it Yourself »](trysql.asp?filename=trysql_select_join_inner)

**Note:** The INNER JOIN keyword selects all rows from both 
tables as long as there is a match between the columns. If there are records in the 
"Orders" table that do not have matches in "Customers", these orders will not 
be shown!

The following SQL statement selects all orders with customer and shipper information:

### Example

```
  SELECT Orders.OrderID, Customers.CustomerName, Shippers.ShipperName
FROM 
  ((Orders
INNER JOIN Customers ON Orders.CustomerID = Customers.CustomerID)
  INNER JOIN Shippers ON Orders.ShipperID = Shippers.ShipperID); 
```
[Try it Yourself »](trysql.asp?filename=trysql_select_join_inner2)

## LEFT JOIN

The `LEFT JOIN` command returns all rows from 
the left table, and the matching rows from the right table. The result is NULL 
from the right side, if there is no match.

The following SQL will select all customers, and any orders they might have:

### Example

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

## RIGHT JOIN

The `RIGHT JOIN` command returns all rows from 
the right table, and the matching records from the left table. The result is 
NULL from the left side, when there is no match.

The following SQL will return all employees, and any orders they might have placed:

### Example

```
 SELECT Orders.OrderID, Employees.LastName, Employees.FirstName
FROM Orders
RIGHT JOIN Employees ON Orders.EmployeeID = Employees.EmployeeID
 ORDER BY Orders.OrderID; 
```
[Try it Yourself »](trysql.asp?filename=trysql_select_join_right)

**Note:** The `RIGHT JOIN` keyword returns all records from the 
right table (Employees), even if there are no matches in the left table 
(Orders).

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