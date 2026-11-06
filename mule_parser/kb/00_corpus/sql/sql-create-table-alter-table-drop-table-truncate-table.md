# SQL CREATE TABLE, ALTER TABLE, DROP TABLE, TRUNCATE TABLE

**Source:** [https://www.w3schools.com/sql/sql_ref_table.asp](https://www.w3schools.com/sql/sql_ref_table.asp)

---

# SQL TABLE Keyword

## CREATE TABLE

The `CREATE TABLE` command creates a new table 
in the database.

The following SQL creates a table called "Persons" that contains five columns: PersonID, LastName, FirstName, Address, and City:

### Example[Get your own SQL Server](/sql/sql_server.asp)

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

A copy of an existing table can also be created using 
`CREATE TABLE`.

The following SQL creates a new table called "TestTables" (which is a copy of the "Customers" table):

### Example

```
  CREATE TABLE TestTable AS
SELECT customername, contactname
FROM 
  customers;  
```
## ALTER TABLE

The `ALTER TABLE` command adds, deletes, or 
modifies columns in a table.

The `ALTER TABLE` command also adds and 
deletes various constraints in a table.

The following SQL adds an "Email" column to the "Customers" table:

### Example

```
  ALTER TABLE Customers
ADD Email varchar(255);
 
```
The following SQL deletes the "Email" column from the "Customers" table:

### Example

```
  ALTER TABLE Customers
DROP COLUMN Email;
 
```
## DROP TABLE

The `DROP TABLE` command deletes a table in 
the database.

The following SQL deletes the table "Shippers":

### Example

```
  DROP TABLE Shippers;
 
```
**Note****:** Be careful before deleting a table. Deleting a 
table results in loss of all information stored in the table!

## TRUNCATE TABLE

The `TRUNCATE TABLE` command deletes the data inside a table, but 
not the table itself.

The following SQL truncates the table "Categories":

### Example

```
  TRUNCATE TABLE Categories;
 
```