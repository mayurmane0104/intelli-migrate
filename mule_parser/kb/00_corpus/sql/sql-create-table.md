# SQL CREATE TABLE

**Source:** [https://www.w3schools.com/sql/sql_ref_create_table.asp](https://www.w3schools.com/sql/sql_ref_create_table.asp)

---

# SQL CREATE TABLE Keyword

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

The following SQL creates a new table called "TestTables" (which is a copy of two columns of the "Customers" table):

### Example

```
  CREATE TABLE TestTable AS
SELECT customername, contactname
FROM 
  customers;  
```
Ad