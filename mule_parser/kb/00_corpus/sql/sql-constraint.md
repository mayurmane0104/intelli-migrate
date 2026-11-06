# SQL CONSTRAINT

**Source:** [https://www.w3schools.com/sql/sql_ref_constraint.asp](https://www.w3schools.com/sql/sql_ref_constraint.asp)

---

# SQL CONSTRAINT Keyword

## ADD CONSTRAINT

The `ADD CONSTRAINT` command is used to create 
a constraint after a table is already created.

The following SQL adds a constraint named "PK_Person" that is a PRIMARY KEY constraint on multiple columns (ID and LastName):

### Example[Get your own SQL Server](/sql/sql_server.asp)

```
  ALTER TABLE Persons
ADD CONSTRAINT PK_Person PRIMARY KEY (ID,LastName);
 
```
## DROP CONSTRAINT

The `DROP CONSTRAINT` command is used to delete 
a UNIQUE, PRIMARY KEY, FOREIGN KEY, or CHECK constraint.

## DROP a UNIQUE Constraint

To drop a UNIQUE constraint, use the following SQL:

**SQL Server / Oracle / MS Access:**

```
ALTER TABLE Persons
DROP CONSTRAINT UC_Person; 
```
**MySQL:**

```
ALTER TABLE Persons
DROP INDEX UC_Person; 
```
## DROP a PRIMARY KEY Constraint

To drop a PRIMARY KEY constraint, use the following SQL:

**SQL Server / Oracle / MS Access:**

```
ALTER TABLE Persons
DROP CONSTRAINT PK_Person; 
```
**MySQL:**

```
ALTER TABLE Persons
DROP PRIMARY KEY; 
```
## DROP a FOREIGN KEY Constraint

To drop a FOREIGN KEY constraint, use the following SQL:

**SQL Server / Oracle / MS Access:**

```
ALTER TABLE Orders
DROP CONSTRAINT FK_PersonOrder; 
```
**MySQL:**

```
ALTER TABLE Orders
DROP FOREIGN KEY FK_PersonOrder; 
```
## DROP a CHECK Constraint

To drop a CHECK constraint, use the following SQL:

**SQL Server / Oracle / MS Access:**

```
ALTER TABLE Persons
DROP CONSTRAINT CHK_PersonAge; 
```
**MySQL:**

```
ALTER TABLE Persons
DROP CHECK CHK_PersonAge; 
```