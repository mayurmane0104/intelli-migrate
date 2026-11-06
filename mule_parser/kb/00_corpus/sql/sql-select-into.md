# SQL SELECT INTO

**Source:** [https://www.w3schools.com/sql/sql_ref_select_into.asp](https://www.w3schools.com/sql/sql_ref_select_into.asp)

---

# SQL SELECT INTO Keyword

## SELECT INTO

The `SELECT INTO` command copies data 
from one table and inserts it into a new table.

The following SQL statement creates a backup copy of Customers:

```
SELECT * INTO CustomersBackup2017
FROM Customers; 
```
The following SQL statement uses the IN clause to copy the table into a new table in another database:

```
SELECT *
INTO CustomersBackup2017 IN 'Backup.mdb'
FROM Customers; 
```
The following SQL statement copies only a few columns into a new table:

```
SELECT CustomerName, ContactName INTO CustomersBackup2017
FROM Customers; 
```
The following SQL statement copies only the German customers into a new table:

```
SELECT *
INTO CustomersGermany
FROM Customers
WHERE Country = 'Germany'; 
```
The following SQL statement copies data from more than one table into a new table:

```
 SELECT Customers.CustomerName, Orders.OrderID
INTO CustomersOrderBackup2017
FROM Customers
 LEFT JOIN Orders
 ON Customers.CustomerID = Orders.CustomerID; 
```