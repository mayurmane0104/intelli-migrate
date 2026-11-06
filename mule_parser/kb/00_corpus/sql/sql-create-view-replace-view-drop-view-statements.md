# SQL CREATE VIEW, REPLACE VIEW, DROP VIEW Statements

**Source:** [https://www.w3schools.com/sql/sql_view.asp](https://www.w3schools.com/sql/sql_view.asp)

---

# SQL Views

## SQL CREATE VIEW Statement

An SQL view is a virtual table based on the result-set of an SQL statement. An SQL view contains rows and columns, just like a real table. The fields in the view are fields from one or more real tables in the database.

You can add SQL statements and functions to a view and present the data as if it were coming from one single table.

A view is created with the `CREATE VIEW` statement.

### CREATE VIEW Syntax

```
CREATE VIEW 
SELECT 
FROM 
WHERE 
```
*view_name* AS*column1*, *column2*, ...*table_name**condition*; **Note:** A view always shows real-time data! The database engine only 
stores the view's definition (the SELECT statement), not a copy of the data.

## CREATE VIEW Examples

The following SQL creates a view named "Brazil Customers", that shows all customers from Brazil:

### Example[Get your own SQL Server](/sql/sql_server.asp)

```
CREATE VIEW [Brazil Customers] AS
SELECT CustomerName, ContactName
FROM Customers
WHERE Country = 'Brazil'; 
```
To query the view above, use the following SQL syntax:

### Example

```
SELECT * FROM [Brazil Customers]; 
```
The following SQL creates a view named "Products Above Average Price", that selects all products in the "Products" table with a Price higher than the average price:

### Example

```
CREATE VIEW [Products Above Average Price] AS
SELECT ProductName, Price
FROM Products
WHERE Price > (SELECT AVG(Price) FROM Products); 
```
To query the view above, use the following SQL syntax:

### Example

```
SELECT * FROM [Products Above Average Price]; 
```
## ALTER VIEW Statement (SQL Server)

In SQL Server, a view can be updated with the ```
ALTER 
VIEW
```
 statement.

### ALTER VIEW Syntax

```
  ALTER VIEW 
SELECT 
FROM 
WHERE 
```
*view_name* AS*column1*, *column2*, ...*table_name**condition*; The following SQL adds the "City" column to the "Brazil Customers" view:

### Example

```
  ALTER VIEW [Brazil Customers] AS
SELECT CustomerName, ContactName, City
FROM Customers
WHERE Country = 'Brazil'; 
```
## CREATE OR REPLACE VIEW Statement (MySQL and Oracle)

In MySQL and Oracle, a view can be updated with the ```
CREATE OR REPLACE 
VIEW
```
 statement.

### CREATE OR REPLACE VIEW Syntax

```
CREATE OR REPLACE VIEW 
SELECT 
FROM 
WHERE 
```
*view_name* AS*column1*, *column2*, ...*table_name**condition*; The following SQL adds the "City" column to the "Brazil Customers" view:

### Example

```
CREATE OR REPLACE VIEW [Brazil Customers] AS
SELECT CustomerName, ContactName, City
FROM Customers
WHERE Country = 'Brazil'; 
```
## DROP VIEW Statement

A view is deleted with the `DROP VIEW` 
statement.

### DROP VIEW Syntax

```
DROP VIEW 
```
*view_name*; The following SQL deletes the "Brazil Customers" view:

### Example

```
DROP VIEW [Brazil Customers]; 
```
## Exercise?**What is this?**

Test your skills by answering a few questions about the topics of this page

What is an SQL view?