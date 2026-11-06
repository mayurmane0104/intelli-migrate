# SQL RIGHT JOIN Keyword

**Source:** [https://www.w3schools.com/sql/sql_join_right.asp](https://www.w3schools.com/sql/sql_join_right.asp)

---

# SQL RIGHT JOIN

## SQL RIGHT JOIN

The `RIGHT JOIN` returns **all rows from the right table** (table2), and only the matched rows from the left table (table1).

If there is no match in the left table, the result for the columns from the left table will be NULL.

The `RIGHT JOIN` and `RIGHT OUTER JOIN` keywords are equal - the `OUTER` keyword is optional.

![SQL RIGHT JOIN](img_right_join.png)


### RIGHT JOIN Syntax

```
SELECT 
FROM 
RIGHT JOIN 
 
```
*column_name(s)**table1**table2*ON *table1.column_name *=* table2.column_name*;
 **Note:** The syntax combines two tables based on a **related column**, 
and the `ON` keyword is used to specify the matching condition.

## Demo Database

Below is a selection from the "Orders" table:

| OrderID | CustomerID | EmployeeID | OrderDate | ShipperID | 
|---|---|---|---|---|
| 10308 | 2 | 7 | 1996-09-18 | 3 | 
| 10309 | 37 | 3 | 1996-09-19 | 1 | 
| 10310 | 77 | 8 | 1996-09-20 | 2 | 

And a selection from the "Employees" table:

| EmployeeID | LastName | FirstName | BirthDate | Photo | 
|---|---|---|---|---|
| 1 | Davolio | Nancy | 1968-12-08 | EmpID1.pic | 
| 2 | Fuller | Andrew | 1952-02-19 | EmpID2.pic | 
| 3 | Leverling | Janet | 1963-08-30 | EmpID3.pic | 

Here we see that the related column between the two tables above, is the "EmployeeID" column.

## SQL RIGHT JOIN Example

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

## Exercise?**What is this?**

Test your skills by answering a few questions about the topics of this page

What does the SQL `RIGHT JOIN` keyword do?