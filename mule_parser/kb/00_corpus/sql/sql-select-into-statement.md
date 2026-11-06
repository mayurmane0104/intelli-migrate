# SQL SELECT INTO Statement

**Source:** [https://www.w3schools.com/sql/sql_select_into.asp](https://www.w3schools.com/sql/sql_select_into.asp)

---

# SQL SELECT INTO Statement

## The SQL SELECT INTO Statement

The `SELECT INTO` statement is used to create 
a new table and fill it with data from an existing table.

The `SELECT INTO` statement is useful for 
creating backups or for creating a temporary table for analysis.

**Note:** The new table will be created with the same column names and 
data types as defined in the source table. However, primary keys, indexes, or NOT NULL
constraints are not automatically transferred.

### SELECT INTO Syntax

Copy entire table into a new table:

```
SELECT * INTO 
FROM 
WHERE 
```
*newtable* [IN *external_db*]*sourcetable**condition*;
 Copy only some columns into a new table:

```
SELECT 
INTO 
 
FROM 
WHERE 
```
*column1*, *column2*, *column3*, ...*newtable* [IN *external_db*]*sourcetable**condition;*
 ## SQL SELECT INTO Examples

The following SQL creates a backup copy of the "Customers" table:

```
SELECT * INTO CustomersBackup2026
FROM Customers; 
```
The following SQL creates a backup copy of the "Customers" table in another database ('Backup.mdb'):

```
SELECT *
INTO CustomersBackup2026 IN 'Backup.mdb'
FROM Customers; 
```
The following SQL copies only a few columns from the "Customers" table into a new table:

```
SELECT CustomerName, ContactName INTO Customers2
FROM Customers; 
```
The following SQL copies only the customers from USA in the "Customers" table, into a new table:

```
SELECT *
INTO US_Customers
FROM Customers
WHERE Country = 'USA'; 
```
The following SQL copies data from more than one table into a new table:

```
 SELECT Customers.CustomerName, Orders.OrderID INTO CustomersOrder
FROM Customers
 LEFT JOIN Orders
 ON Customers.CustomerID = Orders.CustomerID; 
```
**Tip:** `SELECT INTO` can also be used to create a 
new, empty table using the schema of another. Just add a 
`WHERE` clause that 
causes the query to return no data:

```
SELECT * INTO 
FROM 
WHERE 1 = 0; 
```
*newtable**sourcetable*
## Exercise?**What is this?**

Test your skills by answering a few questions about the topics of this page

What is the primary purpose of the SQL `SELECT INTO` statement?