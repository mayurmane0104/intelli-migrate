# SQL CREATE

**Source:** [https://www.w3schools.com/sql/sql_ref_create.asp](https://www.w3schools.com/sql/sql_ref_create.asp)

---

# SQL CREATE Keyword

## CREATE DATABASE

The `CREATE DATABASE` command is used is to 
create a new SQL database.

The following SQL creates a database called "testDB":

### Example[Get your own SQL Server](/sql/sql_server.asp)

```
CREATE DATABASE testDB;
 
```
**Tip:** Make sure you have admin privilege before creating any database. Once a 
database is created, you can check it in the list of databases with the 
following SQL command: SHOW DATABASES;

## CREATE TABLE

The `CREATE TABLE` command creates a new table 
in the database.

The following SQL creates a table called "Persons" that contains five columns: PersonID, LastName, FirstName, Address, and City:

### Example

```
CREATE TABLE Persons
(
   
PersonID int,
   
LastName varchar(255),
   
FirstName varchar(255),
   
Address varchar(255),
   
City varchar(255) 
);
 
```
## CREATE TABLE Using Another Table

The following SQL creates a new table called "TestTables" (which is a copy of two columns of the "Customers" table):

### Example

```
CREATE TABLE TestTable AS
SELECT customername, contactname
FROM customers; 
```
## CREATE INDEX

The `CREATE INDEX` command is used to 
create indexes in tables (allows duplicate values).

Indexes are used to retrieve data from the database very fast. The users cannot see the indexes, they are just used to speed up searches/queries.

The following SQL creates an index named "idx_lastname" on the "LastName" column in the "Persons" table:

```
CREATE INDEX idx_lastname
ON Persons (LastName); 
```
If you want to create an index on a combination of columns, you can list the column names within the parentheses, separated by commas:

```
CREATE INDEX idx_pname
ON Persons (LastName, FirstName); 
```
**Note:** The syntax for creating indexes varies among different databases. Therefore: Check the syntax for creating indexes in your database.

**Note:** Updating a table with indexes takes more time than updating a table without (because the indexes also need an update).
So, only create indexes on columns that will be frequently searched against.

## CREATE UNIQUE INDEX

The `CREATE UNIQUE INDEX` command creates a unique index on a table (no duplicate values 
allowed)

The following SQL creates an index named "uidx_pid" on the "PersonID" column in the "Persons" table:

```
CREATE UNIQUE INDEX uidx_pid
ON Persons (PersonID); 
```
## CREATE VIEW

The `CREATE VIEW` command creates a view.

A view is a virtual table based on the result set of an SQL statement.

The following SQL creates a view that selects all customers from Brazil:

### Example

```
CREATE VIEW [Brazil Customers] AS
SELECT CustomerName, ContactName
FROM Customers
WHERE Country = "Brazil"; 
```
## CREATE OR REPLACE VIEW

The `CREATE OR REPLACE VIEW` command updates a view.

The following SQL adds the "City" column to the "Brazil Customers" view:

### Example

```
CREATE OR REPLACE VIEW [Brazil Customers] AS
SELECT CustomerName, ContactName, City
FROM Customers
WHERE Country = "Brazil"; 
```
## Query The View

We can query the view above as follows:

### Example

```
SELECT * FROM [Brazil 
  Customers]; 
```
## CREATE PROCEDURE

The `CREATE PROCEDURE` command is used to 
create a stored procedure.

A stored procedure is a prepared SQL code that you can save, so the code can be reused over and over again.

The following SQL creates a stored procedure named "SelectAllCustomers" that selects all records from the "Customers" table:

### Example

```
  CREATE PROCEDURE SelectAllCustomers
AS
SELECT * FROM Customers
GO;
 
```
Execute the stored procedure above as follows:

### Example

```
  EXEC SelectAllCustomers;
 
```