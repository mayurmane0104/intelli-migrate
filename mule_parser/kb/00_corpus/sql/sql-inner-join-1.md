# SQL INNER JOIN

**Source:** [https://www.w3schools.com/sql/sql_ref_inner_join.asp](https://www.w3schools.com/sql/sql_ref_inner_join.asp)

---

# SQL INNER JOIN Keyword

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