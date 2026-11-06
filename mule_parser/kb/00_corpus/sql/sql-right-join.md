# SQL RIGHT JOIN

**Source:** [https://www.w3schools.com/sql/sql_ref_right_join.asp](https://www.w3schools.com/sql/sql_ref_right_join.asp)

---

# SQL RIGHT JOIN Keyword

## RIGHT JOIN

The `RIGHT JOIN` command returns all rows from 
the right table, and the matching records from the left table. The result is 
NULL from the left side, when there is no match.

The following SQL will return all employees, and any orders they might have placed:

### Example[Get your own SQL Server](/sql/sql_server.asp)

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

Ad