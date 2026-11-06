# SQL UNIQUE Constraint

**Source:** [https://www.w3schools.com/sql/sql_unique.asp](https://www.w3schools.com/sql/sql_unique.asp)

---

# SQL UNIQUE Constraint

## SQL UNIQUE Constraint

The `UNIQUE` constraint ensures that all values in a column are unique.

Both the `UNIQUE` and [PRIMARY KEY](sql_primarykey.asp)`UNIQUE` constraints per table, but only one 
`PRIMARY KEY` constraint per table.

## UNIQUE Constraint on CREATE TABLE

The following SQL defines a `UNIQUE` constraint 
for the "ID" column upon creation of the "Persons" table:

### SQL Server / Oracle / MS Access:

```
CREATE TABLE Persons
(
    ID int NOT NULL UNIQUE,
   
LastName varchar(255) NOT NULL,
   
FirstName varchar(255),
   
Age int
);
 
```
### MySQL:

```
CREATE TABLE Persons
(
    ID int NOT NULL,
   
LastName varchar(255) NOT NULL,
   
FirstName varchar(255),
   
Age int,
   
UNIQUE (ID)
); 
```
### Naming a Unique Constraint

To name a `UNIQUE` constraint, and to define a 
`UNIQUE` constraint on multiple columns, use the following SQL syntax:

```
CREATE TABLE Persons
(
    ID int NOT NULL,
   
LastName varchar(255) NOT NULL,
   
FirstName varchar(255),
   
Age int,
   
CONSTRAINT UC_Person UNIQUE (ID,LastName)
); 
```
## UNIQUE Constraint on ALTER TABLE

To create a `UNIQUE` constraint on the "ID" column when the table is already created, use the following SQL 
syntax:

```
ALTER TABLE Persons
ADD UNIQUE (ID); 
```
### Naming a Unique Constraint

To name a `UNIQUE` constraint, and to define a 
`UNIQUE` constraint on multiple columns, use the following SQL syntax:

```
ALTER TABLE Persons
ADD CONSTRAINT UC_Person UNIQUE (ID,LastName); 
```
## Drop a UNIQUE Constraint

To drop a `UNIQUE` constraint, use the following SQL:

### MySQL:

```
ALTER TABLE Persons
DROP INDEX UC_Person; 
```
### SQL Server / Oracle / MS Access:

```
ALTER TABLE Persons
DROP CONSTRAINT UC_Person; 
```
## Exercise?**What is this?**

Test your skills by answering a few questions about the topics of this page

What does the SQL `UNIQUE` constraint ensure?