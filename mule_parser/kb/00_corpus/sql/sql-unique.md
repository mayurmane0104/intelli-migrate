# SQL UNIQUE

**Source:** [https://www.w3schools.com/sql/sql_ref_unique.asp](https://www.w3schools.com/sql/sql_ref_unique.asp)

---

# SQL UNIQUE Keyword

## UNIQUE

The `UNIQUE` constraint ensures that all 
values in a column are unique.

## SQL UNIQUE Constraint on CREATE TABLE

The following SQL creates a UNIQUE constraint on the "ID" column when the "Persons" table is created:

**SQL Server / Oracle / MS Access:**

```
CREATE TABLE Persons
(
    ID int NOT NULL UNIQUE,
   
LastName varchar(255) NOT NULL,
   
FirstName varchar(255),
   
Age int
);
 
```
**MySQL:**

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
To name a UNIQUE constraint, and to define a UNIQUE constraint on multiple columns, use the following SQL syntax:

**MySQL / SQL Server / Oracle / MS Access:**

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
## SQL UNIQUE Constraint on ALTER TABLE

To create a UNIQUE constraint on the "ID" column when the table is already created, use the following SQL:

**MySQL / SQL Server / Oracle / MS Access:**

```
ALTER TABLE Persons
ADD UNIQUE (ID); 
```
To name a UNIQUE constraint, and to define a UNIQUE constraint on multiple columns, use the following SQL syntax:

**MySQL / SQL Server / Oracle / MS Access:**

```
ALTER TABLE Persons
ADD CONSTRAINT UC_Person UNIQUE (ID,LastName); 
```
## DROP a UNIQUE Constraint

To drop a UNIQUE constraint, use the following SQL:

**MySQL:**

```
ALTER TABLE Persons
DROP INDEX UC_Person; 
```
**SQL Server / Oracle / MS Access:**

```
ALTER TABLE Persons
DROP CONSTRAINT UC_Person; 
```